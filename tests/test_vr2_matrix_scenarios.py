"""VR2.0 scenario-validation suite -- run-engine integration layer.

Complements tests/test_matrix_engine.py (which unit-tests the pure dice/combat
functions). This file drives the *run* layer in app.routers.matrix_runs --
sheaf activation, alert escalation, subsystem-rating modifiers, IC placement --
to validate the rules a decker actually experiences during a run.

Each test cites the vr2_rules.md behaviour it validates. Dice are made
deterministic by monkeypatching app.services.matrix_engine.random.

Covers test-matrix items:
  #1  every IC type placed/resolved (isolation + stacking)
  #7  Trap IC, Party IC, Construct activation
  #8  Passive Alert -> +2 all subsystem ratings, with player-facing notice
  #10 Tar Baby / Tar Pit deck-wipe representation
  #11 Detection Factor / masking / trace-factor (satlink) fields
"""
from __future__ import annotations

import pytest

from app.services import matrix_engine as eng
from app.services import matrix_rules as rules
from app.routers import matrix_runs as mr


# -- Deterministic dice helper (mirrors test_matrix_engine._ScriptedRandom) -----

class _ScriptedRandom:
    def __init__(self, values):
        self._v = list(values)
        self._i = 0

    def randint(self, a, b):
        v = self._v[self._i % len(self._v)]
        self._i += 1
        return max(a, min(b, v))

    def choice(self, seq):
        return seq[0]

    def seed(self, *a, **k):
        pass

    def getstate(self):
        return None

    def setstate(self, s):
        pass


@pytest.fixture
def scripted(monkeypatch):
    def _install(values):
        monkeypatch.setattr(eng, "random", _ScriptedRandom(values))
    return _install


def _fresh_state(acifs=None, sec_code="Green", sec_value=6):
    """Minimal run state sufficient for sheaf-activation / subsystem helpers."""
    return {
        "security_tally": 0,
        "alert_status": "none",
        "active_ic": [],
        "lurking_ic": [],
        "current_turn": 1,
        "host_security_code": sec_code,
        "host_security_value": sec_value,
        "host_acifs": acifs or [8, 10, 9, 9, 8],
        "sheaf": [],
        "has_legitimate_status": True,
        "decoy_successes": 3,
        "decoy_hp": 2,
    }


# -- #1 Every IC type: catalog completeness + placement -------------------------

class TestEveryICType:
    """vr2_rules IC Programs -- the engine must know every canonical IC type."""

    EXPECTED = {
        "Probe", "Killer", "Acid", "Binder", "Jammer", "Marker", "Tar Baby",
        "Data Bomb", "Scramble", "Blaster", "Sparky", "Acid-rip", "Bind-rip",
        "Jam-rip", "Mark-rip", "Tar Pit", "Worm", "Trace", "Black IC",
    }

    def test_catalog_has_every_canonical_ic(self):
        assert self.EXPECTED.issubset(set(rules.IC_CATALOG.keys()))

    def test_cripplers_and_rippers_declare_targets(self):
        for name, meta in rules.IC_CATALOG.items():
            if meta.get("subtype") in ("crippler", "ripper"):
                assert meta.get("targets") in ("Bod", "Evasion", "Masking", "Sensor"), name

    @pytest.mark.parametrize("ic_type", sorted(EXPECTED))
    def test_each_ic_activates_into_run_state(self, scripted, ic_type):
        """Each IC type can be placed via a sheaf 'ic' event without error.

        Reactive ambush IC (Tar Baby/Tar Pit) lurk; everything else goes active.
        """
        scripted([3])  # deterministic initiative roll
        state = _fresh_state()
        step = {"trigger": 10, "events": [{"type": "ic", "ic_type": ic_type, "rating": 6}]}
        events = mr._activate_sheaf_step(state, step, state["host_security_code"])
        assert events, f"{ic_type} produced no event"
        if ic_type in ("Tar Baby", "Tar Pit"):
            assert len(state["lurking_ic"]) == 1
            assert state["lurking_ic"][0]["type"] == ic_type
            assert state["active_ic"] == []
        else:
            assert len(state["active_ic"]) == 1
            placed = state["active_ic"][0]
            assert placed["type"] == ic_type
            assert placed["rating"] == 6
            assert placed["category"] == rules.IC_CATALOG.get(ic_type, {}).get("category", "gray")

    def test_stacked_ic_accumulate_in_active_list(self, scripted):
        """Isolation -> stacking: multiple proactive IC coexist on the host."""
        scripted([3])
        state = _fresh_state()
        step = {"trigger": 10, "events": [
            {"type": "ic", "ic_type": "Killer", "rating": 6},
            {"type": "ic", "ic_type": "Blaster", "rating": 5},
            {"type": "ic", "ic_type": "Acid", "rating": 4},
        ]}
        mr._activate_sheaf_step(state, step, state["host_security_code"])
        assert len(state["active_ic"]) == 3
        assert {ic["type"] for ic in state["active_ic"]} == {"Killer", "Blaster", "Acid"}


# -- #1 stacking: cumulative crippler reductions --------------------------------

class TestCumulativeCripplerEffects:
    """vr2_rules Crippler IC -- reductions persist and stack across attributes."""

    def test_two_cripplers_reduce_two_attributes(self):
        decker = {"bod": 6, "evasion": 6, "masking": 6, "sensor": 6, "mpcp": 6}
        state = _fresh_state()
        # Marker reduced Masking by 2, Binder reduced Evasion by 3 (recorded as persona_damage)
        state["condition_monitor"] = {
            "persona_damage": {"bod": 0, "evasion": 3, "masking": 2, "sensor": 0},
            "mpcp_damage": 0,
        }
        eff = mr._get_decker_effective(decker, state)
        assert eff["masking"] == 4
        assert eff["evasion"] == 3
        assert eff["bod"] == 6
        assert eff["mpcp"] == 6

    def test_crippler_cannot_reduce_below_one(self):
        decker = {"bod": 2, "evasion": 4, "masking": 4, "sensor": 4, "mpcp": 6}
        state = _fresh_state()
        state["condition_monitor"] = {
            "persona_damage": {"bod": 9, "evasion": 0, "masking": 0, "sensor": 0},
            "mpcp_damage": 0,
        }
        eff = mr._get_decker_effective(decker, state)
        assert eff["bod"] == 1  # floor at 1, never 0/negative


# -- #7 Trap IC, Party IC, Construct --------------------------------------------

class TestTrapPartyConstruct:
    def test_trap_ic_places_surface_and_conceals_hidden(self, scripted):
        scripted([3])
        state = _fresh_state()
        step = {"trigger": 12, "events": [{
            "type": "trap_ic", "surface_ic_type": "Probe", "surface_ic_rating": 5,
            "hidden_ic_type": "Blaster", "hidden_ic_rating": 6,
        }]}
        events = mr._activate_sheaf_step(state, step, state["host_security_code"])
        assert len(state["active_ic"]) == 1
        ic = state["active_ic"][0]
        assert ic["type"] == "Probe"
        assert ic["trap_hidden"] == {"type": "Blaster", "rating": 6}
        assert any(e.get("is_trap") for e in events)

    def test_party_ic_forms_cluster(self, scripted):
        scripted([3])
        state = _fresh_state()
        step = {"trigger": 14, "events": [{
            "type": "party_ic", "threat_rating": 6,
            "components": [{"type": "Killer", "rating": 6}, {"type": "Acid", "rating": 5}],
        }]}
        mr._activate_sheaf_step(state, step, state["host_security_code"])
        clustered = [ic for ic in state["active_ic"] if ic.get("cluster_id")]
        assert clustered, "party IC should tag its members with a cluster_id"
        cid = clustered[0]["cluster_id"]
        assert mr._cluster_size(state, cid) == len(clustered)

    def test_construct_is_single_icon(self, scripted):
        scripted([3])
        state = _fresh_state()
        step = {"trigger": 16, "events": [{
            "type": "construct", "threat_rating": 7,
            "components": [{"type": "Killer", "rating": 7}, {"type": "Trace", "rating": 6}],
        }]}
        events = mr._activate_sheaf_step(state, step, state["host_security_code"])
        assert len(state["active_ic"]) == 1  # one combined icon
        assert events


# -- #8 Passive/Active Alert escalation -----------------------------------------

class TestAlertEscalation:
    """vr2_rules Alerts -- Passive Alert raises ALL subsystem ratings by +2."""

    def test_passive_alert_adds_two_to_every_subsystem(self):
        base = _fresh_state(acifs=[8, 10, 9, 9, 8])
        passive = _fresh_state(acifs=[8, 10, 9, 9, 8])
        passive["alert_status"] = "passive"
        for sub in ("access", "control", "index", "files", "slave"):
            assert mr._subsystem_rating(passive, sub) == mr._subsystem_rating(base, sub) + 2

    def test_passive_alert_emits_player_notice(self):
        state = _fresh_state()
        step = {"trigger": 25, "events": [{"type": "passive_alert"}]}
        events = mr._activate_sheaf_step(state, step, state["host_security_code"])
        assert state["alert_status"] == "passive"
        notice = next((e for e in events if e.get("level") == "passive"), None)
        assert notice is not None
        assert "+2" in notice["description"]  # player is told ratings went up

    def test_passive_alert_does_not_re_trigger(self):
        state = _fresh_state()
        state["alert_status"] = "passive"
        step = {"trigger": 25, "events": [{"type": "passive_alert"}]}
        events = mr._activate_sheaf_step(state, step, state["host_security_code"])
        assert events == []  # already passive -> no duplicate notice

    def test_active_alert_revokes_passcode_and_decoy(self):
        state = _fresh_state()
        step = {"trigger": 30, "events": [{"type": "active_alert"}]}
        events = mr._activate_sheaf_step(state, step, state["host_security_code"])
        assert state["alert_status"] == "active"
        assert "has_legitimate_status" not in state
        assert state["decoy_successes"] == 0 and state["decoy_hp"] == 0
        assert any(e.get("level") == "active" for e in events)

    def test_active_alert_has_no_blanket_subsystem_modifier(self):
        """Active alert escalates response, but does NOT stack another +2 on ratings."""
        base = _fresh_state()
        active = _fresh_state()
        active["alert_status"] = "active"
        assert mr._subsystem_rating(active, "access") == mr._subsystem_rating(base, "access")


# -- #10 Tar Baby / Tar Pit deck-wipe -------------------------------------------

class TestTarBabyTarPit:
    """vr2_rules Tar Baby / Tar Pit -- crash utility; Tar Pit corrupts all copies."""

    def test_tar_baby_crashes_both_when_ic_wins(self, scripted):
        # IC rolls 6,6 (2 hits vs util TN); util rolls 1,1 (0 hits) -> IC wins
        scripted([6, 6, 1, 1])
        r = eng.tar_baby_test(ic_rating=6, utility_rating=6)
        assert r["ic_wins"] is True
        assert r["utility_crashed"] is True and r["ic_crashed"] is True

    def test_tar_pit_wipes_all_copies_on_pit_success(self, scripted):
        # IC wins the duel, then the pit roll scores a hit vs MPCP -> all copies gone
        scripted([6, 6, 1, 1, 6])
        r = eng.tar_baby_test(ic_rating=6, utility_rating=6, is_tar_pit=True, mpcp_rating=4)
        assert r["ic_wins"] is True
        assert r["all_copies_corrupted"] is True  # the full deck-wipe representation

    def test_tar_pit_no_wipe_when_pit_misses(self, scripted):
        scripted([6, 6, 1, 1, 1])  # pit roll misses vs MPCP
        r = eng.tar_baby_test(ic_rating=6, utility_rating=6, is_tar_pit=True, mpcp_rating=8)
        assert r["ic_wins"] is True
        assert r["all_copies_corrupted"] is False


# -- #11 Detection Factor / masking / trace (satlink fields) --------------------

class TestDetectionAndTrace:
    def test_detection_factor_average_with_sleaze(self):
        # vr2_rules: DF = round-up average of Masking and Sleaze. M6/S8 -> 7.
        assert eng.detection_factor(6, 8) == 7

    def test_detection_factor_masking_only_halves(self):
        # No sleaze: DF = ceil(Masking / 2). M6 -> 3.
        assert eng.detection_factor(6, 0) == 3

    def test_masking_reduction_lowers_detection_factor(self):
        # A Marker crippler cuts Masking; DF must drop accordingly.
        assert eng.detection_factor(6, 0) == 3
        assert eng.detection_factor(2, 0) == 1  # masking reduced 6->2

    def test_trace_factor_and_bandwidth_feed_trace_tn(self):
        """Satlink jackpoint surfaces as decker trace_factor / bandwidth_modifier;
        both must flow into the Trace IC target number."""
        decker = {"evasion": 6, "trace_factor": 0, "bandwidth_modifier": 0, "utilities": {}}
        state = {"redirects_placed": 0}
        eff = {"evasion": 6}
        base = mr._compute_trace_tn(state, decker, ic_rating=4, eff=eff)
        decker_sat = dict(decker, trace_factor=4)  # satellite uplink raises Trace Factor
        raised = mr._compute_trace_tn(state, decker_sat, ic_rating=4, eff=eff)
        assert raised == base + 4

    def test_redirects_reduce_trace_tn(self):
        decker = {"evasion": 6, "trace_factor": 2, "bandwidth_modifier": 0, "utilities": {}}
        eff = {"evasion": 6}
        no_redirect = mr._compute_trace_tn({"redirects_placed": 0}, decker, 4, eff)
        with_redirect = mr._compute_trace_tn({"redirects_placed": 2}, decker, 4, eff)
        assert with_redirect == no_redirect - 2

    def test_trace_tn_floors_at_two(self):
        decker = {"evasion": 1, "trace_factor": -10, "bandwidth_modifier": 0, "utilities": {}}
        eff = {"evasion": 1}
        assert mr._compute_trace_tn({"redirects_placed": 0}, decker, 9, eff) == 2
