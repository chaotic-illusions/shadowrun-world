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
from fastapi import HTTPException


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

    def random(self):
        return 0.5   # deterministic probability for tests (e.g. enemy hot/RF/RI rolls)

    def seed(self, *a, **k):
        pass

    def getstate(self):
        return None

    def setstate(self, s):
        pass


class _ProbRandom:
    """Scripts random() (probability rolls, e.g. enemy spawn chance / nerve check) and
    randint()/choice() for the wounded-AI and spawn tests, which drive ``matrix_runs.random``
    rather than the engine RNG. ``random()`` cycles the supplied floats (default 0.5); ``randint``
    cycles the supplied ints clamped to [a, b] (default: the low end)."""
    def __init__(self, randoms=(0.5,), randints=()):
        self._rf = list(randoms) or [0.5]
        self._rfi = 0
        self._ri = list(randints)
        self._rii = 0

    def randint(self, a, b):
        if not self._ri:
            return a
        v = self._ri[self._rii % len(self._ri)]
        self._rii += 1
        return max(a, min(b, v))

    def choice(self, seq):
        return seq[0]

    def random(self):
        v = self._rf[self._rfi % len(self._rf)]
        self._rfi += 1
        return v

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
        if ic_type in ("Tar Baby", "Tar Pit", "Worm"):
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

    def test_jackpoint_access_modifier_only_affects_access(self):
        # Legal Access -2 lowers the Access Test rating but not other subsystems
        st = _fresh_state(acifs=[8, 10, 9, 9, 8]); st["access_modifier"] = -2
        assert mr._subsystem_rating(st, "access") == 6   # 8 - 2
        assert mr._subsystem_rating(st, "control") == 10  # unchanged
        # Remote Device +4 raises it
        st["access_modifier"] = 4
        assert mr._subsystem_rating(st, "access") == 12

    def test_console_access_halves_access_rating(self):
        st = _fresh_state(acifs=[9, 10, 9, 9, 8]); st["console_access"] = True
        assert mr._subsystem_rating(st, "access") == 5   # ceil(9/2)
        assert mr._subsystem_rating(st, "control") == 10  # other subsystems unaffected


# -- Bouncer: mid-run host security upgrade (vr2 L300) --------------------------

class TestBouncer:
    """vr2 Bouncer (L300) -- a triggered sheaf step HARDENS the host, upgrading the security
    code/value the whole engine reads from (host_security_code / host_security_value) for the
    rest of the run. Previously buildable in the designer but inert in the run engine."""

    def test_bouncer_upgrades_host_security(self):
        state = _fresh_state(sec_code="Green", sec_value=6)
        step = {"trigger": 20, "events": [{
            "type": "bouncer", "new_security_code": "Red", "new_security_value": 9}]}
        events = mr._activate_sheaf_step(state, step, state["host_security_code"])
        assert state["host_security_code"] == "Red"
        assert state["host_security_value"] == 9
        ev = next((e for e in events if e.get("type") == "bouncer"), None)
        assert ev is not None
        assert ev["old_security_code"] == "Green" and ev["old_security_value"] == 6
        assert ev["new_security_code"] == "Red" and ev["new_security_value"] == 9

    def test_bouncer_missing_payload_leaves_host_unchanged(self):
        # A malformed bouncer (no payload) must not blank the host -- it falls back to current.
        state = _fresh_state(sec_code="Orange", sec_value=7)
        step = {"trigger": 20, "events": [{"type": "bouncer"}]}
        mr._activate_sheaf_step(state, step, state["host_security_code"])
        assert state["host_security_code"] == "Orange"
        assert state["host_security_value"] == 7

    def test_bouncer_field_survives_schema_round_trip(self):
        # SheafEvent must persist new_security_* through model_dump (the designer save path);
        # this is exactly what was missing while the Bouncer was inert.
        from app.schemas.matrix_run import SheafEvent
        dumped = SheafEvent(type="bouncer", new_security_code="Black",
                            new_security_value=12).model_dump()
        assert dumped["new_security_code"] == "Black"
        assert dumped["new_security_value"] == 12


def _shutdown_decker(sensor=4):
    return {"bod": 6, "evasion": 6, "masking": 6, "sensor": sensor, "mpcp": 6, "utilities": {}}


class TestHostShutdown:
    """vr2_rules Host Shutdown (L771-789) -- the host starts a multi-turn self-shutdown that
    dumps every decker when it completes, secret until a Sensor Test succeeds or the final
    warning turn. Modeled as a countdown initiated by the sheaf 'shutdown' event and resolved
    each Combat Turn in _process_host_shutdown_countdown."""

    def test_shutdown_event_starts_countdown_not_instant_end(self):
        state = _fresh_state(sec_value=6)
        step = {"trigger": 40, "events": [{"type": "shutdown"}]}
        events = mr._activate_sheaf_step(state, step, state["host_security_code"])
        assert not state.get("run_ended")
        cd = state.get("shutdown_countdown")
        assert cd is not None
        assert cd["turns_remaining"] >= 1          # SV6 -> 3D6
        assert 1 <= cd["final_warning_turn"] <= 3   # 1D3
        assert cd["known"] is False
        ev = next((e for e in events if e.get("type") == "shutdown_initiated"), None)
        assert ev is not None and ev.get("gm_only") is True

    def test_second_shutdown_trigger_does_not_restart_clock(self):
        state = _fresh_state(sec_value=6)
        step = {"trigger": 40, "events": [{"type": "shutdown"}]}
        mr._activate_sheaf_step(state, step, state["host_security_code"])
        first = dict(state["shutdown_countdown"])
        mr._activate_sheaf_step(state, step, state["host_security_code"])
        assert state["shutdown_countdown"]["turns_remaining"] == first["turns_remaining"]

    def test_countdown_completes_and_dumps_decker(self, scripted):
        scripted([1])  # dump-shock resist dice: all misses (deterministic)
        state = _fresh_state()
        state["event_log"] = []
        state["condition_monitor"] = {"persona_damage": {}, "mpcp_damage": 0}
        state["shutdown_countdown"] = {
            "turns_remaining": 1, "total_turns": 3, "final_warning_turn": 1,
            "elapsed": 2, "known": True,
        }
        mr._process_host_shutdown_countdown(state, _shutdown_decker())
        assert state.get("run_ended") is True
        assert state.get("end_reason") == "host_shutdown"
        assert "shutdown_countdown" not in state
        ev = next((e for e in state["event_log"] if e.get("type") == "shutdown"), None)
        assert ev is not None and "dump_shock" in ev

    def test_sensor_success_reveals_shutdown(self, scripted):
        scripted([6])  # Sensor Test succeeds
        state = _fresh_state()
        state["event_log"] = []
        state["shutdown_countdown"] = {
            "turns_remaining": 3, "total_turns": 3, "final_warning_turn": 99,
            "elapsed": 0, "known": False,
        }
        mr._process_host_shutdown_countdown(state, _shutdown_decker())
        assert state["shutdown_countdown"]["known"] is True
        ev = next((e for e in state["event_log"] if e.get("type") == "shutdown_detected"), None)
        assert ev is not None

    def test_secret_tick_when_sensor_fails(self, scripted):
        scripted([1])  # Sensor Test fails
        state = _fresh_state()
        state["event_log"] = []
        state["shutdown_countdown"] = {
            "turns_remaining": 3, "total_turns": 3, "final_warning_turn": 99,
            "elapsed": 0, "known": False,
        }
        mr._process_host_shutdown_countdown(state, _shutdown_decker())
        assert state["shutdown_countdown"]["known"] is False
        ev = next((e for e in state["event_log"] if e.get("type") == "shutdown_tick"), None)
        assert ev is not None and ev.get("gm_only") is True

    def test_final_warning_turn_auto_informs(self, scripted):
        scripted([1])  # even a failed sensor roll is irrelevant on the warning turn
        state = _fresh_state()
        state["event_log"] = []
        state["shutdown_countdown"] = {
            "turns_remaining": 4, "total_turns": 4, "final_warning_turn": 1,
            "elapsed": 0, "known": False,
        }
        mr._process_host_shutdown_countdown(state, _shutdown_decker())
        assert state["shutdown_countdown"]["known"] is True
        ev = next((e for e in state["event_log"] if e.get("type") == "shutdown_warning"), None)
        assert ev is not None


def _black_state():
    state = _fresh_state(sec_code="Green", sec_value=6)
    state["event_log"] = []
    state["program_damage"] = {}
    state["condition_monitor"] = {
        "persona_boxes": 0, "stun_boxes": 0, "physical_boxes": 0, "mpcp_damage": 0,
        "persona_damage": {}, "persona_chip_damage": {}, "crippler_rating": {},
    }
    return state


def _black_decker():
    return {"bod": 6, "body": 6, "willpower": 6, "mpcp": 6, "hardening": 0,
            "utilities": {}, "deck_mode": "hot"}


class TestBlackICJackOut:
    """vr2_rules Black IC in Combat (L610-614) -- after a Black IC hit, jacking out needs a
    Willpower(Black IC Rating) Test and the IC gets one final attack. Helpers only (the endpoint
    is async); the flag is set by the cybercombat resolver."""

    def test_highest_engaged_black_ic_picks_top_rating(self):
        state = _black_state()
        state["active_ic"] = [
            {"id": "a", "type": "Black IC", "rating": 5, "status": "active"},
            {"id": "b", "type": "Black IC", "rating": 8, "status": "active"},
            {"id": "c", "type": "Killer", "rating": 9, "status": "active"},
        ]
        pick = mr._highest_engaged_black_ic(state)
        assert pick is not None and pick["id"] == "b"

    def test_no_black_ic_returns_none(self):
        state = _black_state()
        state["active_ic"] = [{"id": "c", "type": "Killer", "rating": 9, "status": "active"}]
        assert mr._highest_engaged_black_ic(state) is None

    def test_final_attack_applies_damage_and_logs(self, scripted):
        # High attack successes + failed resists -> the final strike lands damage.
        scripted([6])
        state = _black_state()
        ic = {"id": "b", "type": "Black IC", "rating": 6, "status": "active"}
        state["active_ic"] = [ic]
        res = mr._black_ic_final_attack(state, _black_decker(), ic)
        assert "attack_roll" in res
        assert any(e.get("type") == "ic_attack" for e in state["event_log"])


class TestWormVariants:
    """vr2 Worm variants + user rulings (2026-07): infection is the GATE -- every worm must first
    compromise the MPCP (recorded in state["mpcp_infections"], carried across runs). Only an
    INFECTED Deathworm raises cybercombat TNs; only an INFECTED Tapeworm erases paydata at run end.
    Dataworm is narrative-only (not modeled)."""

    def _dl_state(self, files):
        state = _fresh_state()
        state["event_log"] = []
        state["downloaded_files"] = list(files)
        return state

    # -- Infection is the gate: a merely-lurking worm has no payload yet --------

    def test_lurking_deathworm_has_no_bonus_until_infected(self):
        state = _fresh_state()
        state["lurking_ic"] = [{"type": "Worm", "variant": "deathworm", "status": "lurking"}]
        assert mr._deathworm_tn_bonus(state) == 0   # not yet infected

    def test_infected_worm_recorded_and_payload_activates(self):
        # A guaranteed infection (host 6d6 vs MPCP TN 2, no hardening) moves the worm into
        # mpcp_infections and its Deathworm payload then applies.
        state = _fresh_state(sec_value=6)
        state["event_log"] = []
        worm = {"id": "w1", "type": "Worm", "variant": "deathworm", "rating": 6, "status": "lurking"}
        state["lurking_ic"] = [worm]
        decker = {"mpcp": 2, "hardening": 0}
        mr._resolve_lurking_worm(state, decker, worm)
        assert state.get("mpcp_infected") is True
        assert any(i["variant"] == "deathworm" for i in state["mpcp_infections"])
        assert worm not in state["lurking_ic"]
        assert mr._deathworm_tn_bonus(state) == 2

    # -- RAW trigger: a System Test against the infested subsystem risks infection --

    def test_trigger_fires_only_for_matching_subsystem(self):
        # vr2 L548: a worm on Files only rolls its Infection Test on a Files System Test.
        state = _fresh_state(sec_value=6)
        state["event_log"] = []
        worm = {"id": "w1", "type": "Worm", "variant": "standard", "rating": 6,
                "subsystem": "files", "status": "lurking"}
        state["lurking_ic"] = [worm]
        decker = {"mpcp": 2, "hardening": 0}
        # A test against a DIFFERENT subsystem must NOT trip it.
        mr._trigger_subsystem_worms(state, decker, "index")
        assert not any(e["type"] == "worm_resolved" for e in state["event_log"])
        assert worm in state["lurking_ic"]
        # A test against the worm's own subsystem trips it (guaranteed infection here).
        mr._trigger_subsystem_worms(state, decker, "files")
        assert state.get("mpcp_infected") is True
        assert any(e["type"] == "worm_resolved" for e in state["event_log"])

    def test_subsystemless_worm_triggers_on_any_test(self):
        # A worm authored without a subsystem (legacy gap) covers any System Test.
        state = _fresh_state(sec_value=6)
        state["event_log"] = []
        worm = {"id": "w1", "type": "Worm", "variant": "standard", "rating": 6, "status": "lurking"}
        state["lurking_ic"] = [worm]
        mr._trigger_subsystem_worms(state, {"mpcp": 2, "hardening": 0}, "control")
        assert state.get("mpcp_infected") is True

    # -- Deathworm TN bonus (gated on infection) --------------------------------

    def test_no_deathworm_gives_zero_bonus(self):
        state = _fresh_state()
        state["mpcp_infections"] = [{"variant": "standard", "rating": 6, "ic_id": "a"}]
        assert mr._deathworm_tn_bonus(state) == 0

    def test_one_infected_deathworm_gives_two(self):
        state = _fresh_state()
        state["mpcp_infections"] = [{"variant": "deathworm", "rating": 6, "ic_id": "a"}]
        assert mr._deathworm_tn_bonus(state) == 2

    def test_two_infected_deathworms_give_three(self):
        state = _fresh_state()
        state["mpcp_infections"] = [
            {"variant": "deathworm", "rating": 6, "ic_id": "a"},
            {"variant": "deathworm", "rating": 6, "ic_id": "b"},
        ]
        assert mr._deathworm_tn_bonus(state) == 3

    # -- Tapeworm run-end paydata sabotage (gated on infection) ------------------

    def test_tapeworm_not_infected_is_noop(self):
        state = self._dl_state([{"name": "f1", "is_key": False}])
        state["mpcp_infections"] = [{"variant": "standard", "rating": 6, "ic_id": "a"}]
        mr._apply_tapeworm_run_end(state)
        assert len(state["downloaded_files"]) == 1
        assert not state.get("tapeworm_resolved")

    def test_tapeworm_deletes_non_key_files(self, monkeypatch):
        # 1D6-1 non-key deletions: randint(1,6)=6 -> delete 5; no key data present.
        monkeypatch.setattr(mr, "random", _ProbRandom(randints=[6]))
        files = [{"name": f"f{i}", "is_key": False} for i in range(6)]
        state = self._dl_state(files)
        state["mpcp_infections"] = [{"variant": "tapeworm", "rating": 6, "ic_id": "w"}]
        mr._apply_tapeworm_run_end(state)
        assert len(state["downloaded_files"]) == 1
        assert any(e["type"] == "tapeworm_payload_loss" for e in state["event_log"])

    def test_tapeworm_key_data_erased_on_five_or_six(self, monkeypatch):
        # First randint (non-key count) = 1 -> delete 0; second (key roll) = 5 -> erase key.
        monkeypatch.setattr(mr, "random", _ProbRandom(randints=[1, 5]))
        state = self._dl_state([{"name": "k", "is_key": True}])
        state["mpcp_infections"] = [{"variant": "tapeworm", "rating": 6, "ic_id": "w"}]
        mr._apply_tapeworm_run_end(state)
        assert state["downloaded_files"] == []
        assert any(e.get("key_erased") for e in state["event_log"])

    def test_tapeworm_key_data_survives_low_roll(self, monkeypatch):
        monkeypatch.setattr(mr, "random", _ProbRandom(randints=[1, 4]))
        state = self._dl_state([{"name": "k", "is_key": True}])
        state["mpcp_infections"] = [{"variant": "tapeworm", "rating": 6, "ic_id": "w"}]
        mr._apply_tapeworm_run_end(state)
        assert state["downloaded_files"] == [{"name": "k", "is_key": True}]

    def test_tapeworm_is_idempotent(self, monkeypatch):
        monkeypatch.setattr(mr, "random", _ProbRandom(randints=[6]))
        files = [{"name": f"f{i}", "is_key": False} for i in range(6)]
        state = self._dl_state(files)
        state["mpcp_infections"] = [{"variant": "tapeworm", "rating": 6, "ic_id": "w"}]
        mr._apply_tapeworm_run_end(state)
        remaining = len(state["downloaded_files"])
        mr._apply_tapeworm_run_end(state)   # second call must be a no-op
        assert len(state["downloaded_files"]) == remaining

    # -- Carry-forward: a deck arrives already infected -------------------------

    def test_carried_infection_seeds_run_state(self):
        from app.models.matrix_host import MatrixHost
        host = MatrixHost(name="H", config_json={"security_code": "Green", "security_value": 6})
        decker = {"mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                  "mpcp_infections": [{"variant": "deathworm", "rating": 5, "ic_id": "old"}]}
        state = mr._initial_state(decker, host)
        assert state["mpcp_infected"] is True
        assert mr._deathworm_tn_bonus(state) == 2


class TestRunDeckDamageWriteback:
    """User ruling (2026-07): runs -- not the GM -- are the source of deck damage. Every permanent
    hardware consequence (MPCP damage, Ripper persona-chip burn, persistent MPCP Worm infection)
    is stamped onto the owning character's saved deck at run end, so the player must institute a
    (GM-approved) Deck Workshop repair before the deck is whole again."""

    from app.auth.core import hash_token as _hash_token
    _hash = staticmethod(_hash_token)
    _TOK = "player-tok"
    _AUTH = {"is_admin": False, "is_user": True, "user_token": _TOK}

    def _char(self, deck):
        from app.models.character import Character
        c = Character(name="Decker", is_pc=True)
        c.id = 1
        c.owner_token = self._hash(self._TOK)
        c.deck_builder_state = {"version": 1, "stores": {"sr2_decks_v1": [deck]}}
        return c

    def _run(self, state):
        from app.models.matrix_run import MatrixRun
        run = MatrixRun()
        run.id = 7
        run.decker_json = {"character_id": 1, "deck_name": "Cobra"}
        run.state_json = state
        run.owner_token_hash = self._hash(self._TOK)
        return run

    def _fake_db(self, char):
        class _FakeDB:
            def __init__(self, ch):
                self._ch = ch
                self.commits = 0
            async def get(self, model, pk):
                return self._ch if pk == self._ch.id else None
            async def commit(self):
                self.commits += 1
        return _FakeDB(char)

    def _apply(self, deck, state):
        import asyncio
        char = self._char(deck)
        db = self._fake_db(char)
        run = self._run(state)
        asyncio.run(mr._apply_run_damage_to_deck(db, run, self._AUTH))
        return char.deck_builder_state["stores"]["sr2_decks_v1"][0], run.state_json

    def test_mpcp_damage_degrades_saved_deck(self):
        deck = {"name": "Cobra", "mpcp": 6}
        state = _fresh_state()
        state["condition_monitor"] = {"mpcp_damage": 2}
        out, st = self._apply(deck, state)
        assert out["damage"]["mpcp"] == 4
        assert st["deck_damage_applied"] is True

    def test_ripper_chip_burn_degrades_persona_chip(self):
        deck = {"name": "Cobra", "mpcp": 6, "pBod": 5, "pSensor": 4}
        state = _fresh_state()
        state["condition_monitor"] = {"persona_chip_damage": {"bod": 2, "evasion": 0, "masking": 0, "sensor": 1}}
        out, _ = self._apply(deck, state)
        assert out["damage"]["pBod"] == 3
        assert out["damage"]["pSensor"] == 3

    def test_infection_merges_onto_deck(self):
        deck = {"name": "Cobra", "mpcp": 6}
        state = _fresh_state()
        state["mpcp_infections"] = [{"variant": "deathworm", "rating": 5, "ic_id": "w1"}]
        out, _ = self._apply(deck, state)
        assert out["mpcp_infections"] == [{"variant": "deathworm", "rating": 5, "ic_id": "w1"}]

    def test_idempotent_no_double_apply(self):
        deck = {"name": "Cobra", "mpcp": 6}
        state = _fresh_state()
        state["condition_monitor"] = {"mpcp_damage": 2}
        state["deck_damage_applied"] = True
        out, _ = self._apply(deck, state)
        assert "damage" not in out

    def test_unlinked_run_is_noop(self):
        import asyncio
        deck = {"name": "Cobra", "mpcp": 6}
        char = self._char(deck)
        db = self._fake_db(char)
        run = self._run(_fresh_state())
        run.decker_json = {}   # no character_id / deck_name
        run.state_json["condition_monitor"] = {"mpcp_damage": 3}
        asyncio.run(mr._apply_run_damage_to_deck(db, run, self._AUTH))
        assert "damage" not in char.deck_builder_state["stores"]["sr2_decks_v1"][0]

    def test_non_owner_cannot_write(self):
        import asyncio
        deck = {"name": "Cobra", "mpcp": 6}
        char = self._char(deck)
        db = self._fake_db(char)
        state = _fresh_state()
        state["condition_monitor"] = {"mpcp_damage": 2}
        run = self._run(state)
        asyncio.run(mr._apply_run_damage_to_deck(db, run, {"is_admin": False, "is_user": True, "user_token": "someone-else"}))
        assert "damage" not in char.deck_builder_state["stores"]["sr2_decks_v1"][0]


class TestShieldShift:
    """vr2 Shield/Shift -- +2 to-hit, with Penetration/Chaser negation + extra-effectiveness."""

    def test_shield_plain_plus_two(self):
        ic = {"shield": True}
        assert mr._shield_shift_tn_modifier(ic, penetration=False, chaser=False) == 2

    def test_penetration_defeats_shield(self):
        assert mr._shield_shift_tn_modifier({"shield": True}, penetration=True, chaser=False) == 0

    def test_chaser_makes_shield_extra_effective(self):
        assert mr._shield_shift_tn_modifier({"shield": True}, penetration=False, chaser=True) == 4

    def test_shift_plain_plus_two_and_chaser_defeats(self):
        assert mr._shield_shift_tn_modifier({"shift": True}, penetration=False, chaser=False) == 2
        assert mr._shield_shift_tn_modifier({"shift": True}, penetration=False, chaser=True) == 0
        assert mr._shield_shift_tn_modifier({"shift": True}, penetration=True, chaser=False) == 4

    def test_no_shield_or_shift_no_penalty(self):
        assert mr._shield_shift_tn_modifier({"type": "Killer"}, penetration=False, chaser=False) == 0

    def test_designer_options_set_shield_on_active_ic(self, scripted):
        # The designer writes options=['Shielding'/'Shifting'] on the IC sheaf event;
        # _activate_sheaf_step must copy those onto the placed active IC.
        scripted([3])
        state = _fresh_state()
        step = {"trigger": 10, "events": [
            {"type": "ic", "ic_type": "Killer", "rating": 6, "options": ["Shielding"]}]}
        mr._activate_sheaf_step(state, step, state["host_security_code"])
        ic = state["active_ic"][0]
        assert ic["shield"] is True and ic["shift"] is False
        assert mr._shield_shift_tn_modifier(ic, penetration=False, chaser=False) == 2

    def test_designer_shift_option_on_active_ic(self, scripted):
        scripted([3])
        state = _fresh_state()
        step = {"trigger": 10, "events": [
            {"type": "ic", "ic_type": "Killer", "rating": 6, "options": ["Shifting"]}]}
        mr._activate_sheaf_step(state, step, state["host_security_code"])
        assert state["active_ic"][0]["shift"] is True


class TestLinkedPasscodeAndConsole:
    """vr2 -- linked passcode -2 to Logon; Console halves Security Value (loaded into state)."""

    def test_linked_passcode_loaded_into_state(self):
        class _Host:
            config_json = {"security_code": "Blue", "security_value": 4}
        st = mr._initial_state(
            {"masking": 4, "intelligence": 5, "mpcp": 6, "utilities": {},
             "linked_passcode": True, "console_access": True}, _Host())
        assert st["linked_passcode"] is True
        assert st["console_access"] is True


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


class TestLurkingTarApplication:
    """Router-level tar IC -> decker APPLICATION path (vr2_rules.md L1655-1667). The engine
    duel (eng.tar_baby_test) is pinned by TestTarBabyTarPit above; this class pins the single
    run-layer resolver that consumes it -- _resolve_lurking_tar (and the _autofire_lurking_tar
    fan-out that drives it on every System Test) -- so the tar direction has the same router
    coverage TestSteamroller gives the anti-tar counter. There is exactly ONE such resolver for
    ALL tar IC (no per-actor duplication: enemy deckers never fight IC), so this is the whole
    surface. Asserts: IC-wins removes the tar + emits reactive_ic_resolved; a Tar Pit additionally
    corrupts all copies; a One-Shot copy is wiped from the deck (never reloadable this run); a
    utility win leaves the tar lurking; and the autofire gate skips when no reducible utility ran."""

    def _decker(self, **kw):
        d = {"utilities": {"analyze": 6}, "mpcp": 4, "hardening": 0}
        d.update(kw)
        return d

    def _state_with_tars(self, tars):
        s = _fresh_state()
        s["event_log"] = []
        s["lurking_ic"] = [dict(t) for t in tars]
        return s

    # -- direct resolver: IC wins -> crash + remove -----------------------------

    def test_ic_wins_crashes_utility_and_removes_tar(self, scripted):
        # ic 6d @ TN(util=6) all 6s -> 6 hits; util 6d @ TN(ic=6) all 1s -> 0 hits -> IC wins.
        scripted([6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1])
        state = self._state_with_tars(
            [{"id": "lc_t", "type": "Tar Baby", "rating": 6, "status": "lurking"}])
        tar = state["lurking_ic"][0]
        mr._resolve_lurking_tar(state, self._decker(), tar, "analyze", 6)
        assert state["lurking_ic"] == []                       # tar crashed + removed
        ev = state["event_log"][-1]
        assert ev["type"] == "reactive_ic_resolved"
        assert ev["outcome"] == "ic_wins" and ev["ic_type"] == "Tar Baby"
        # A plain Tar Baby crash emits no all-copies corruption event.
        assert not any(e["type"] == "tar_pit_corruption" for e in state["event_log"])

    def test_util_wins_leaves_tar_lurking(self, scripted):
        # ic 4d @ TN6 all 1s -> 0 hits; util 6d @ TN4 all 6s -> 6 hits -> utility wins.
        scripted([1, 1, 1, 1, 6, 6, 6, 6, 6, 6])
        state = self._state_with_tars(
            [{"id": "lc_t", "type": "Tar Baby", "rating": 4, "status": "lurking"}])
        tar = state["lurking_ic"][0]
        mr._resolve_lurking_tar(state, self._decker(), tar, "analyze", 6)
        assert [ic["id"] for ic in state["lurking_ic"]] == ["lc_t"]   # survives, still lurking
        assert state["event_log"][-1]["outcome"] == "util_wins"

    # -- Tar Pit: corrupt-all-copies + One-Shot deck wipe -----------------------

    def test_tar_pit_corrupts_all_copies_and_wipes_one_shot(self, scripted):
        # ic 6d @ TN(util=5) all 6s -> 6 hits; util 5d @ TN(ic=6) all 1s -> 0 -> IC wins;
        # pit 6d @ TN(mpcp4+hard0=4) all 6s -> corrupt all copies.
        scripted([6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6, 6])
        decker = self._decker(
            utilities={"attack": 5},
            program_options={"attack": {"one_shot": True}},
        )
        state = self._state_with_tars(
            [{"id": "lc_p", "type": "Tar Pit", "rating": 6, "status": "lurking"}])
        state["storage_programs"] = [
            {"name": "attack", "rating": 5, "size": 5},
            {"name": "analyze", "rating": 4, "size": 4},
        ]
        tar = state["lurking_ic"][0]
        mr._resolve_lurking_tar(state, decker, tar, "attack", 5)
        assert state["lurking_ic"] == []
        types = [e["type"] for e in state["event_log"]]
        assert "tar_pit_corruption" in types                    # every copy corrupted
        assert "one_shot_wiped" in types                        # deck copies destroyed
        assert state["program_damage"]["attack"] == 5           # active copy -> effective 0
        assert "attack" in state["one_shot_wiped"]              # Swap Memory refuses to reload
        names = [p["name"] for p in state["storage_programs"]]
        assert names == ["analyze"]                             # storage copy dropped, others kept

    # -- autofire fan-out (app-as-GM: one opposed test per utility use) ---------

    def test_autofire_skips_when_no_reducible_utility(self):
        # A System Test that ran no reducible utility (rating 0) fires NO tar.
        state = self._state_with_tars(
            [{"id": "lc_t", "type": "Tar Baby", "rating": 6, "status": "lurking"}])
        mr._autofire_lurking_tar(state, self._decker(), "logon_to_host", 0)
        assert len(state["lurking_ic"]) == 1                    # untouched
        assert state["event_log"] == []                        # nothing fired

    def test_autofire_fires_every_lurking_tar(self, scripted):
        # Two lurking tars, both IC-win (12-draw all-6/all-1 script cycles once per tar).
        scripted([6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1])
        state = self._state_with_tars([
            {"id": "lc_a", "type": "Tar Baby", "rating": 6, "status": "lurking"},
            {"id": "lc_b", "type": "Tar Pit", "rating": 6, "status": "lurking"},
        ])
        mr._autofire_lurking_tar(state, self._decker(), "analyze_host", 6)
        assert state["lurking_ic"] == []                        # both fired + crashed
        resolved = [e for e in state["event_log"] if e["type"] == "reactive_ic_resolved"]
        assert len(resolved) == 2 and all(e["outcome"] == "ic_wins" for e in resolved)


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

    def test_redirects_raise_trace_tn(self):
        # vr2_rules.md L578: each Redirect Datatrail operation ADDS to the decker's Trace Factor
        # (the Trace IC's target number), so more redirects make the jackpoint HARDER to trace --
        # the same direction as Camo, not the opposite.
        decker = {"evasion": 6, "trace_factor": 2, "bandwidth_modifier": 0, "utilities": {}}
        eff = {"evasion": 6}
        no_redirect = mr._compute_trace_tn({"redirects_placed": 0}, decker, 4, eff)
        with_redirect = mr._compute_trace_tn({"redirects_placed": 2}, decker, 4, eff)
        assert with_redirect == no_redirect + 2

    def test_trace_tn_floors_at_two(self):
        decker = {"evasion": 1, "trace_factor": -10, "bandwidth_modifier": 0, "utilities": {}}
        eff = {"evasion": 1}
        assert mr._compute_trace_tn({"redirects_placed": 0}, decker, 9, eff) == 2


class TestDataBombAndWorm:
    """vr2 #7 -- Data Bomb defuse/detonate and Worm infection resolution."""

    def test_data_bomb_defuse_tn_reduced_by_defuse_utility(self, scripted):
        scripted([6])  # one success
        r = eng.data_bomb_defuse(decker_pool=8, subsystem_rating=9, defuse_utility=4)
        assert r["tn"] == 5  # 9 - 4
        assert r["defused"] is True

    def test_data_bomb_defuse_floors_tn_at_two(self, scripted):
        scripted([1])
        r = eng.data_bomb_defuse(decker_pool=4, subsystem_rating=3, defuse_utility=9)
        assert r["tn"] == 2
        assert r["defused"] is False

    def test_data_bomb_defuse_higher_defuse_is_easier(self, scripted):
        # Carrying a stronger Defuse utility lowers the TN to disarm the same bomb.
        scripted([3])
        weak = eng.data_bomb_defuse(decker_pool=6, subsystem_rating=9, defuse_utility=2)
        scripted([3])
        strong = eng.data_bomb_defuse(decker_pool=6, subsystem_rating=9, defuse_utility=6)
        assert weak["tn"] == 7 and strong["tn"] == 3       # 9-2 vs 9-6
        assert weak["defused"] is False                    # 3 < 7
        assert strong["defused"] is True                   # 3 (with rule-of-6) clears TN 3

    def test_data_bomb_defuse_success_is_not_a_crash(self, scripted):
        # A successful defuse never reports a security-tally increase -- it is not a crash.
        scripted([6])
        r = eng.data_bomb_defuse(decker_pool=6, subsystem_rating=6, defuse_utility=2)
        assert r["defused"] is True
        assert r["detonated"] is False
        assert "tally_increase" not in r                   # caller adds NO tally on success

    def test_data_bomb_defuse_all_ones_detonates(self, scripted):
        # Botch: every die a 1 sets the bomb off mid-defuse.
        scripted([1])
        r = eng.data_bomb_defuse(decker_pool=3, subsystem_rating=8, defuse_utility=0)
        assert r["defused"] is False
        assert r["detonated"] is True

    def test_data_bomb_defuse_plain_failure_leaves_primed(self, scripted):
        # An ordinary failure (no successes, but not all 1s) does NOT detonate -- bomb stays primed.
        scripted([2])
        r = eng.data_bomb_defuse(decker_pool=3, subsystem_rating=8, defuse_utility=0)
        assert r["defused"] is False
        assert r["detonated"] is False

    def test_data_bomb_detonate_tally_equals_rating(self, scripted):
        scripted([1, 1, 1])  # poor resist
        r = eng.data_bomb_detonate(ic_rating=6, target_bod=6)
        assert r["tally_increase"] == 6
        assert r["damage_level"] == "Moderate"
        assert "final_damage_level" in r["resistance"]

    def test_data_bomb_armor_reduces_power(self, scripted):
        scripted([1, 1, 1])
        r = eng.data_bomb_detonate(ic_rating=6, target_bod=6, armor_rating=2)
        assert r["resistance"]["effective_power"] == 4  # 6 - 2

    def test_worm_infects_mpcp_on_success(self, scripted):
        # Host SV dice vs MPCP TN; net successes (after Hardening) > 0 infects.
        scripted([6, 6])
        r = eng.worm_attack(security_value=6, mpcp_rating=4)
        assert r["tn"] == 4
        assert r["mpcp_infected"] is True
        assert r["chip_replacement_required"] is True

    def test_worm_hardening_threshold_defends(self, scripted):
        # Hardening is subtracted from the worm's successes; net must exceed 0 to infect.
        scripted([6, 6])  # 3 successes at TN 4
        r = eng.worm_attack(security_value=3, mpcp_rating=4, hardening=3)
        assert r["tn"] == 4
        assert r["net_successes"] == 0  # 3 - 3
        assert r["mpcp_infected"] is False


class TestEnemyDeckerGeneration:
    """vr2 #5 -- security decker auto-generation stays in-band with the host tier."""

    def test_blue_host_stays_weak(self):
        # The user's constraint: a Blue host must NOT field an elite decker. Bands are TIER-only
        # (the host's numeric value never scales the decker); Blue centers 4 -> band 3-5.
        for _ in range(30):
            d = eng.generate_enemy_decker("Blue", 5)
            assert 3 <= d["computer_skill"] <= 5
            assert 3 <= d["mpcp"] <= 5
            assert d["intent"] == "dump"          # crash the icon (no decker-run "trace")
            assert d["lethal_program"] is None    # non-deadly host: Attack only, no deck-frying
            assert d["programs"] == ["Attack"]

    def test_lethal_programs_only_on_deadly_force_hosts(self):
        # vr2 line 2310: NPC deckers carry Black Hammer/Killjoy only where deadly force is
        # expected -- Red/Black. Lower tiers do icon-only damage with Attack.
        assert eng.generate_enemy_decker("Green", 6)["lethal_program"] is None
        assert eng.generate_enemy_decker("Orange", 7)["lethal_program"] is None
        assert eng.generate_enemy_decker("Red", 9)["lethal_program"] == "Black Hammer"
        assert eng.generate_enemy_decker("Black", 10)["lethal_program"] == "Black Hammer"
        # Black Hammer rating is capped at ceil(Computer/2); the band roll may land below the cap.
        for _ in range(30):
            d = eng.generate_enemy_decker("Black", 12)
            assert 1 <= d["lethal_rating"] <= (d["computer_skill"] + 1) // 2

    def test_value_does_not_scale_within_tier(self):
        # Bands are TIER-only now: the host's numeric security value has ZERO effect on the decker.
        # A Blue-2 and a Blue-5 decker both roll the same Blue band (centers 4 -> 3-5).
        for _ in range(30):
            for value in (2, 5):
                d = eng.generate_enemy_decker("Blue", value)
                assert 3 <= d["computer_skill"] <= 5
                assert 3 <= d["mpcp"] <= 5

    def test_black_host_is_lethal_elite(self):
        d = eng.generate_enemy_decker("Black", 10)
        assert d["computer_skill"] >= 8
        assert d["intent"] == "kill"
        assert d["lethal_program"] == "Black Hammer"
        assert "Black Hammer" in d["programs"]

    def test_tiers_are_monotonic(self):
        # Per-instance bands overlap between adjacent tiers, so a single sample isn't strictly
        # ordered; the tier CENTERS are monotonic, so the MEAN Computer skill over many rolls is.
        def avg_skill(code, value):
            return sum(eng.generate_enemy_decker(code, value)["computer_skill"]
                       for _ in range(40)) / 40
        means = [avg_skill(c, v) for c, v in
                 (("Blue", 4), ("Green", 6), ("Orange", 8), ("Red", 9), ("Black", 12))]
        assert means == sorted(means)
        assert means[0] < means[-1]   # Blue strictly softer than Black

    def test_enemy_has_combat_loadout(self):
        d = eng.generate_enemy_decker("Red", 8)
        assert d["utilities"]["attack"] >= 6
        assert d["detection_factor"] >= 1  # the PC must beat this to find them
        assert d["status"] == "active" and d["located"] is False

    def test_initiative_stats_scale_by_tier(self):
        # Enemy initiative scales with host difficulty -- pseudo-random within tier bands.
        for _ in range(30):
            blue = eng.generate_enemy_decker("Blue", 4)
            green = eng.generate_enemy_decker("Green", 6)
            red = eng.generate_enemy_decker("Red", 9)
            black = eng.generate_enemy_decker("Black", 12)
            assert blue["response_increase"] in (0, 1)
            assert green["response_increase"] in (0, 1)
            assert red["response_increase"] in (1, 2)
            assert black["response_increase"] in (2, 3)
            assert black["intelligence"] >= 7 and black["intelligence"] > blue["intelligence"]
            for d in (blue, green, red, black):
                assert d["response_increase"] <= d["mpcp"] // 4   # RI <= MPCP/4 (vr2)
                assert d["deck_mode"] in ("hot", "cool")
                assert isinstance(d["reality_filter"], bool)


class TestEnemyDeckerNameReveal:
    """Directive #4 -- a security decker shows only the generic "Security Decker" identifier until
    the PC Analyzes/Scans its icon, then its street handle is disclosed as "Enemy Decker (Handle)"."""

    def test_generated_decker_has_generic_name_and_hidden_handle(self):
        d = eng.generate_enemy_decker("Red", 9)
        assert d["name"] == "Security Decker"
        assert d["handle"] in eng._ENEMY_DECKER_HANDLES
        assert d["name_revealed"] is False

    def test_display_name_generic_until_scanned(self):
        e = {"handle": "Redline", "name": "Security Decker"}
        assert mr._enemy_name_revealed(e) is False
        assert mr._enemy_display_name(e) == "Security Decker"

    def test_display_name_reveals_handle_after_scan(self):
        e = {"handle": "Redline", "name": "Security Decker", "scan_reveal": 1}
        assert mr._enemy_name_revealed(e) is True
        assert mr._enemy_display_name(e) == "Enemy Decker (Redline)"

    def test_name_revealed_flag_alone_reveals_handle(self):
        e = {"handle": "Nyx", "name_revealed": True}
        assert mr._enemy_display_name(e) == "Enemy Decker (Nyx)"

    def test_gm_name_always_includes_handle(self):
        e = {"handle": "Cutter", "name": "Security Decker"}
        assert mr._enemy_gm_name(e) == "Security Decker (Cutter)"

    def test_redaction_hides_handle_until_scanned(self):
        e = {"id": "ed1", "handle": "Wraith", "name": "Security Decker", "tier": "Red",
             "revealed": True, "condition_monitor": {}}
        red = mr._redact_enemy_decker(e)
        assert red["name"] == "Security Decker"
        assert red["handle"] is None
        assert red["name_revealed"] is False
        e["scan_reveal"] = 2
        red2 = mr._redact_enemy_decker(e)
        assert red2["name"] == "Enemy Decker (Wraith)"
        assert red2["handle"] == "Wraith"
        assert red2["name_revealed"] is True

    def test_handle_excludes_supplied_names_case_insensitive(self):
        # Every handle but one is off-limits -> the survivor is always picked (case-insensitive).
        survivor = eng._ENEMY_DECKER_HANDLES[3]
        banned = {h.upper() for h in eng._ENEMY_DECKER_HANDLES if h != survivor}
        for _ in range(20):
            assert eng.pick_enemy_handle(banned) == survivor

    def test_handle_falls_back_when_whole_pool_banned(self):
        banned = {h.lower() for h in eng._ENEMY_DECKER_HANDLES}
        h = eng.pick_enemy_handle(banned)
        assert h.lower() not in banned
        assert h.startswith("Decker-")

    def test_generate_respects_exclude_handles(self):
        banned = {h.lower() for h in eng._ENEMY_DECKER_HANDLES if h != "Kestrel"}
        for _ in range(20):
            d = eng.generate_enemy_decker("Red", 9, exclude_handles=banned)
            assert d["handle"] == "Kestrel"


class TestPaydataHaulFinalization:
    """Directive #6 -- at run end compressed paydata auto-counts, a GM AAR + generic player summary
    are emitted, and the deck's working memory is wiped (a persisted summary survives for the UI)."""

    def _state(self, files):
        return {
            "event_log": [], "downloaded_files": list(files), "paydata": [],
            "storage_used_mp": sum(int(f.get("size_mp", 0) or 0) for f in files),
            "active_download": None,
        }

    def test_compressed_files_auto_count_at_full_size(self):
        st = self._state([
            {"name": "R&D", "size_mp": 50, "full_size_mp": 100, "is_key": False, "compressed": True},
            {"name": "Ledger", "size_mp": 20, "full_size_mp": 20, "is_key": True, "compressed": False},
        ])
        mr._finalize_paydata_haul(st)
        sec = st["paydata_secured"]
        assert sec["count"] == 2
        assert sec["total_mp"] == 120          # 100 (decompressed) + 20
        assert sec["key_count"] == 1
        rnd = {f["name"]: f for f in sec["files"]}
        assert rnd["R&D"]["size_mp"] == 100 and rnd["R&D"]["was_compressed"] is True
        assert rnd["Ledger"]["was_compressed"] is False

    def test_emits_player_and_gm_events(self):
        st = self._state([{"name": "R&D", "size_mp": 50, "full_size_mp": 100, "compressed": True}])
        mr._finalize_paydata_haul(st)
        types = {e["type"]: e for e in st["event_log"]}
        assert "paydata_secured" in types and not types["paydata_secured"].get("gm_only")
        assert "paydata_aar" in types and types["paydata_aar"]["gm_only"] is True
        assert "auto-decompressed" in types["paydata_aar"]["description"]
        # Player event stays generic -- no per-file GM detail leaked.
        assert "auto-decompressed" not in types["paydata_secured"]["description"]

    def test_clears_deck_memory(self):
        st = self._state([{"name": "R&D", "size_mp": 50, "full_size_mp": 100, "compressed": True}])
        mr._finalize_paydata_haul(st)
        assert st["downloaded_files"] == []
        assert st["storage_used_mp"] == 0
        assert st["active_download"] is None

    def test_idempotent(self):
        st = self._state([{"name": "R&D", "size_mp": 100, "full_size_mp": 100, "compressed": False}])
        mr._finalize_paydata_haul(st)
        mr._finalize_paydata_haul(st)
        aars = [e for e in st["event_log"] if e["type"] == "paydata_aar"]
        assert len(aars) == 1

    def test_skipped_while_trap_door_stack_suspended(self):
        st = self._state([{"name": "R&D", "size_mp": 100, "full_size_mp": 100, "compressed": False}])
        st["host_stack"] = [{"host_id": 1}]
        mr._finalize_paydata_haul(st)
        assert "paydata_secured" not in st
        assert st["downloaded_files"]                    # NOT wiped mid-run

    def test_no_paydata_reports_empty(self):
        st = self._state([])
        mr._finalize_paydata_haul(st)
        assert st["paydata_secured"]["count"] == 0
        aar = next(e for e in st["event_log"] if e["type"] == "paydata_aar")
        assert "no paydata" in aar["description"].lower()

    def test_finalize_run_end_runs_tapeworm_then_haul(self):
        st = self._state([{"name": "R&D", "size_mp": 100, "full_size_mp": 100, "compressed": False}])
        mr._finalize_run_end(st)
        assert st.get("paydata_finalized") is True
        assert st["paydata_secured"]["count"] == 1


class TestICExtrasRunSide:
    """Gap E -- run-side application of IC Options/Defenses (Armor / Expert / Cascading)
    and construct defenses."""

    def test_ic_armor_helper(self):
        assert mr._ic_has_armor({"options": ["Armor", "Shielding"]}) is True
        assert mr._ic_has_armor({"options": ["Shielding"]}) is False
        assert mr._ic_has_armor({}) is False

    def test_ic_expert_helper(self):
        ic = {"expert": {"type": "offense", "value": 2}}
        assert mr._ic_expert(ic, "offense") == 2
        assert mr._ic_expert(ic, "defense") == 0
        assert mr._ic_expert({}, "offense") == 0

    def test_cascade_miss_raises_sv_bonus_capped(self):
        # vr2: a cascading IC that MISSES gains +1 attack Security Value per miss, cumulative,
        # capped by the Cascading IC Table. Blue cap = 1.
        ic = {"cascading": True, "rating": 6}
        mr._apply_cascade_outcome(ic, "Blue", hit=False, damage_dealt=False)
        assert ic["cascade_sv_bonus"] == 1
        mr._apply_cascade_outcome(ic, "Blue", hit=False, damage_dealt=False)
        assert ic["cascade_sv_bonus"] == 1   # Blue cap is 1

    def test_cascade_resisted_hit_raises_rating(self):
        # Hit but the decker resisted ALL damage -> +1 to the IC's rating (cumulative).
        ic = {"cascading": True, "rating": 8}
        mr._apply_cascade_outcome(ic, "Red", hit=True, damage_dealt=False)
        assert ic["cascade_rating_bonus"] == 1
        # a damaging hit does not change the bonuses
        mr._apply_cascade_outcome(ic, "Red", hit=True, damage_dealt=True)
        assert ic["cascade_rating_bonus"] == 1

    def test_cascade_noop_for_non_cascading(self):
        ic = {"rating": 6}
        mr._apply_cascade_outcome(ic, "Black", hit=False, damage_dealt=False)
        assert "cascade_sv_bonus" not in ic

    def test_cascade_cap_table(self):
        assert mr._cascade_max_increase("Blue", 8) == 1
        assert mr._cascade_max_increase("Green", 8) == 2     # min(25% of 8 = 2, +2) = 2
        assert mr._cascade_max_increase("Orange", 4) == 2    # min(50% of 4 = 2, +3) = 2
        assert mr._cascade_max_increase("Red", 12) == 4      # min(75% of 12 = 9, +4) = 4
        assert mr._cascade_max_increase("Black", 5) == 5     # min(100% of 5 = 5, +6) = 5

    def test_construct_gets_defenses_list(self, scripted):
        scripted([3, 3, 1, 1, 1, 1])  # rating 2D6=6; defense 2D6=2 -> Armor and Shifting
        ev = eng._build_construct_or_party_event(6)
        assert ev["type"] == "construct"          # _ScriptedRandom.choice -> first option
        assert isinstance(ev["defenses"], list) and set(ev["defenses"]) == {"Armor", "Shifting"}


class TestICOptionsAndDefensesTables:
    """vr2 IC Options Table + IC Defenses Table -- now rolled when generating combat IC."""

    def test_tables_exist_and_cover_2d6(self):
        for tbl in (rules.IC_OPTIONS_TABLE, rules.IC_DEFENSE_TABLE):
            covered = set()
            for (lo, hi), _ in tbl:
                covered |= set(range(lo, hi + 1))
            assert {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12} <= covered

    def test_roll_ic_extras_cascading(self, scripted):
        scripted([1, 1, 5, 2])  # options 2D6=2 -> Cascading; defenses 2D6=7 -> None
        e = eng._roll_ic_extras()
        assert e.get("cascading") is True
        assert "options" not in e

    def test_roll_ic_extras_defense_armor_shifting(self, scripted):
        scripted([4, 4, 1, 1])  # options 2D6=8 -> None; defenses 2D6=2 -> Armor and Shifting
        e = eng._roll_ic_extras()
        assert set(e.get("options", [])) == {"Armor", "Shifting"}
        assert "cascading" not in e and "expert" not in e

    def test_roll_ic_extras_expert_offense(self, scripted):
        scripted([2, 1, 2, 4, 3])  # options 2D6=3 -> Expert Offense; value=2; defenses 2D6=7 -> None
        e = eng._roll_ic_extras()
        assert e.get("expert", {}).get("type") == "offense"
        assert 1 <= e["expert"]["value"] <= 3

    def test_generated_killer_can_carry_extras(self, scripted):
        # proactive_white roll -> Killer (2D6=6); then options/defenses rolls attach extras.
        # 2D6=6 -> [3,3]; rating roll; options [1,1]=2 Cascading; defenses [1,1]=2 Armor+Shifting
        scripted([3, 3, 3, 3, 1, 1, 1, 1])
        ev = eng._build_ic_event("proactive_white", 6)
        assert ev and ev["ic_type"] == "Killer"
        # extras present (cascading and/or options from the tables)
        assert ("cascading" in ev) or ("options" in ev) or ("expert" in ev)


class TestActionEconomyEnforcement:
    """Gap D enforcement -- per-pass action budget (2 Simple OR 1 Complex + 1 Free). Running out
    of action points BLOCKS with a 400 (the decker must click End Turn to close the pass so the
    hostiles on it act, then open the next pass); passes never auto-advance mid-action. The Free
    slot is separate, so a Free action still works after the action points are gone."""

    def _state(self, passes=2):
        return {"event_log": [], "current_pass": 1, "initiative_passes": passes,
                "pass_action_points": 2, "pass_free": 1}

    def test_complex_spends_two_ap(self):
        s = self._state()
        mr._spend_pass_action(s, "analyze_host")   # Complex
        assert s["pass_action_points"] == 0

    def test_two_simple_then_block(self):
        s = self._state(passes=1)
        mr._spend_pass_action(s, "analyze_security")   # Simple -> 1 AP left
        mr._spend_pass_action(s, "download_data")      # Simple -> 0 AP left
        assert s["pass_action_points"] == 0
        # third action, out of AP -> blocks (single pass, so no next pass anyway)
        import fastapi
        with pytest.raises(fastapi.HTTPException):
            mr._spend_pass_action(s, "analyze_security")

    def test_free_action_uses_free_not_ap(self):
        s = self._state()
        mr._spend_pass_action(s, "analyze_ic")   # Free
        assert s["pass_action_points"] == 2 and s["pass_free"] == 0

    def test_free_action_blocks_when_free_slot_spent(self):
        s = self._state()
        mr._spend_pass_action(s, "analyze_ic")   # Free -> free slot gone
        import fastapi
        with pytest.raises(fastapi.HTTPException):
            mr._spend_pass_action(s, "analyze_ic")   # no Free left -> block
        assert s["pass_action_points"] == 2          # action points untouched

    def test_out_of_ap_blocks_without_advancing(self):
        # New economy: running out of AP does NOT silently roll into the next pass. The decker
        # must click End Turn (so the hostiles on the pass being left get to act).
        s = self._state(passes=3)
        mr._spend_pass_action(s, "analyze_host")   # Complex, pass1: 2->0
        import fastapi
        with pytest.raises(fastapi.HTTPException):
            mr._spend_pass_action(s, "analyze_host")   # can't afford -> block (no auto-advance)
        assert s["current_pass"] == 1
        assert not any(e["type"] == "new_pass" for e in s["event_log"])

    def test_block_message_points_to_end_turn(self):
        s = self._state(passes=2)
        mr._spend_pass_action(s, "analyze_host")   # 2->0
        import fastapi
        with pytest.raises(fastapi.HTTPException) as ei:
            mr._spend_pass_action(s, "analyze_host")
        assert "End Turn" in str(ei.value.detail)

    def test_legacy_run_not_enforced(self):
        s = {"event_log": []}  # no pass_action_points
        mr._spend_pass_action(s, "analyze_host")  # no-op, no raise
        assert "pass_action_points" not in s

    def test_reset_pass_budget_refreshes_hacking_pool(self):
        # SR2 RAW: the pool refills at the start of each of the decker's passes. End Turn advances
        # the pass via _reset_pass_budget, which restores the action points, the Free slot, and
        # the Hacking Pool together.
        s = self._state(passes=2)
        s.update({"hackingPool_total": 8, "hackingPool_remaining": 8})
        mr._spend_hp(s, 8)                          # drain pool on pass 1
        assert s["hackingPool_remaining"] == 0
        mr._spend_pass_action(s, "analyze_host")    # drain AP on pass 1
        mr._reset_pass_budget(s)                    # what End Turn's pass-advance calls
        assert s["pass_action_points"] == 2 and s["pass_free"] == 1
        assert s["hackingPool_remaining"] == 8


class TestInitiativeFoundation:
    """Gap D (foundation) -- Matrix initiative + action passes tracked; action costs surfaced.
    (Full action-economy ENFORCEMENT is the documented next step.)"""

    def test_reaction_is_roundup_avg_quickness_intelligence(self):
        assert mr._decker_reaction({"quickness": 3, "intelligence": 5}) == 4   # ceil(8/2)
        assert mr._decker_reaction({"quickness": 4, "intelligence": 5}) == 5   # ceil(9/2)=5

    def test_initiative_passes_increment_of_ten(self, scripted):
        scripted([5])  # reaction + 1d6 ~ small -> 1 pass; exact value not asserted
        init, passes = mr._roll_decker_initiative(
            {"quickness": 4, "intelligence": 5, "response_increase": 0, "deck_mode": "cool"})
        assert passes == max(1, -(-init // 10))  # ceil(init/10)

    def test_action_cost_map_from_rules(self):
        assert mr._ACTION_COST["analyze_host"] == "Complex"
        assert mr._ACTION_COST["analyze_ic"] == "Free"
        assert mr._ACTION_COST["analyze_security"] == "Simple"
        assert mr._ACTION_COST["swap_memory"] == "Simple"
        assert mr._ACTION_COST["purge_hog"] == "Complex"

    # Standard Shadowrun / VR2 initiative (vr2_rules.md L1913): a decker acts on their score, then
    # subtracts 10 and acts again while it stays ABOVE 0 -- so passes = ceil(score / 10). A score
    # landing exactly on a multiple of 10 (10, 20) does NOT grant a phantom extra pass "on 0"
    # (10 -> 1 pass, 20 -> 2 passes). This is the boundary an earlier `(score//10)+1` formula got
    # wrong. Cover the 9..21 band: single pass (9, 10), two passes (11..20 incl. the 20 boundary),
    # three passes (21). The initiative roll is pinned so the test is deterministic (not flaky).
    @pytest.mark.parametrize("score, expected_passes", [
        (9, 1), (10, 1),                       # <= 10 -> a single action pass
        (11, 2), (15, 2), (19, 2), (20, 2),    # 11..20 -> two passes (20 = 20/10, no pass "on 0")
        (21, 3),                               # 21 -> three passes (21/11/1)
    ])
    def test_initial_state_rolls_initiative(self, monkeypatch, score, expected_passes):
        monkeypatch.setattr(eng, "decker_initiative_roll", lambda *a, **k: score)

        class _Host:
            config_json = {"security_code": "Blue", "security_value": 4}
        st = mr._initial_state(
            {"quickness": 4, "intelligence": 5, "mpcp": 6, "masking": 4,
             "deck_mode": "hot", "utilities": {}}, _Host())
        assert st["decker_initiative"] == score
        assert st["initiative_passes"] == expected_passes
        assert st["initiative_passes"] == max(1, -(-score // 10))   # ceil(score/10) cross-check
        assert st["current_pass"] == 1 and st["actions_this_turn"] == 0


class _RunStub:
    status = "active"


class TestEnemyAutoActAndAutoInject:
    """Gap C -- the app-as-GM runs the enemy decker automatically (shared helper) and an
    authored host can dispatch one via a sheaf event."""

    def _decker(self):
        return {"bod": 5, "evasion": 5, "masking": 5, "sensor": 5, "mpcp": 6,
                "intelligence": 5, "body": 5, "hardening": 0, "utilities": {"sleaze": 4}}

    def _state(self):
        s = _fresh_state()
        s["event_log"] = []
        s["condition_monitor"] = {"persona_boxes": 0, "physical_boxes": 0, "mpcp_damage": 0,
                                  "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0}}
        return s

    def test_take_turn_phase1_locates_and_reveals(self, scripted):
        scripted([6, 6, 6, 1, 1])  # enemy locate roll beats the PC -> progress, reveal
        state = self._state()
        enemy = eng.generate_enemy_decker("Red", 8); enemy["id"] = "ed1"
        mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy)
        assert enemy["revealed"] is True   # PC now aware a hostile decker hunts them
        assert any(e["type"] == "enemy_decker" for e in state["event_log"])

    def test_take_turn_noop_when_run_ended_or_crashed(self, scripted):
        scripted([6])
        state = self._state(); state["run_ended"] = True
        enemy = eng.generate_enemy_decker("Red", 8); enemy["id"] = "ed1"
        mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy)
        assert enemy.get("revealed") in (None, False)  # did nothing

    def test_spawn_enemy_decker_injects_hidden(self, scripted):
        # The authored `enemy_decker` sheaf branch is GONE; every decker now comes from the
        # programmatic spawner. _spawn_enemy_decker builds one, rolls its initiative, adds it to
        # the run hidden, and logs a GM-only enemy_decker_injected event.
        scripted([3])
        state = self._state(); state["host_security_value"] = 8
        state["host_security_code"] = "Red"; state["enemy_deckers"] = []
        enemy = mr._spawn_enemy_decker(state, "Red")
        assert len(state["enemy_deckers"]) == 1
        ed = state["enemy_deckers"][0]
        assert ed is enemy
        assert ed["tier"] == "Red" and ed["computer_skill"] >= 1
        assert ed["id"].startswith("ed_")
        assert "initiative" in ed and "initiative_passes" in ed
        inj = [e for e in state["event_log"] if e.get("type") == "enemy_decker_injected"]
        assert inj and inj[0]["gm_only"] is True   # hidden from the player until detected

    def test_authored_enemy_decker_sheaf_branch_is_gone(self, scripted):
        # A sheaf step literally containing {"type": "enemy_decker"} must NOT spawn anything now --
        # the dead branch was removed; only the probabilistic spawner injects deckers.
        scripted([3])
        state = self._state(); state["host_security_value"] = 8; state["enemy_deckers"] = []
        events = mr._activate_sheaf_step(
            state, {"trigger": 10, "events": [{"type": "enemy_decker"}]}, "Red")
        assert state["enemy_deckers"] == []
        assert not any(e.get("type") == "enemy_decker_injected" for e in events)


class TestEnemyActionEconomy:
    """Enemy-decker symmetry (Tier 3): a hostile decker gets the SAME per-pass action budget as
    the PC -- 2 action points (+ 1 Free). ``_enemy_decker_take_pass`` spends the 2 points by
    calling the single-action ``_enemy_decker_take_turn`` up to twice, so a located, healthy enemy
    strikes TWICE per pass (each cybercombat attack is a Simple action) while a Complex action
    (Locate / self-Restore) still consumes the whole pass. The lone Free action is not modelled --
    the enemy AI carries no DINAB / Free-action program to spend it on."""

    def _decker(self):
        return {"name": "Ghost", "bod": 5, "evasion": 5, "masking": 5, "sensor": 5, "mpcp": 6,
                "intelligence": 5, "body": 5, "hardening": 0, "utilities": {"sleaze": 4}}

    def _state(self):
        s = _fresh_state(sec_code="Red", sec_value=9)
        s["event_log"] = []
        s["security_tally"] = 0   # keep a 'dump' enemy from escalating its intent to 'kill'
        s["condition_monitor"] = {"persona_boxes": 0, "physical_boxes": 0, "stun_boxes": 0,
                                  "mpcp_damage": 0,
                                  "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0}}
        return s

    def _located_enemy(self, **over):
        e = {"id": "ed1", "name": "Red Decker", "tier": "Red", "status": "active",
             "revealed": True, "located": True, "intent": "dump",
             "bod": 5, "evasion": 5, "masking": 5, "sensor": 5,
             "computer_skill": 8, "mpcp": 6, "intelligence": 5, "initiative": 20,
             "utilities": {"attack": 5}, "condition_monitor": {"persona_boxes": 0}}
        e.update(over)
        return e

    @staticmethod
    def _canned_cybercombat(boxes=0):
        """A deterministic eng.cybercombat_attack stand-in: `boxes` icon damage, no dice."""
        def _fake(**kw):
            return {"attack_roll": {"successes": 0, "ones": 0},
                    "resistance": {"final_damage_level": "None" if boxes == 0 else "Deadly",
                                   "boxes": boxes, "resist_roll": {"successes": 0}}}
        return _fake

    def _attacks(self, state):
        return [e for e in state["event_log"]
                if e.get("type") == "enemy_decker" and "attack_roll" in e]

    def test_located_healthy_enemy_attacks_twice_per_pass(self, monkeypatch):
        # The core buff: 2 action points -> two Simple cybercombat attacks in a single pass.
        monkeypatch.setattr(eng, "cybercombat_attack", self._canned_cybercombat(boxes=0))
        state = self._state()
        mr._enemy_decker_take_pass(state, self._decker(), _RunStub(), self._located_enemy())
        assert len(self._attacks(state)) == 2

    def test_single_take_turn_still_acts_once(self, monkeypatch):
        # The single-action primitive is unchanged: ONE call = ONE attack (the wrapper grants the
        # second). Guards the direct-call contract the other enemy tests rely on, and the cost token.
        monkeypatch.setattr(eng, "cybercombat_attack", self._canned_cybercombat(boxes=0))
        state = self._state()
        cost = mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), self._located_enemy())
        assert len(self._attacks(state)) == 1 and cost == "simple"

    def test_locate_is_complex_one_locate_per_pass(self, monkeypatch):
        # Locate is a Complex action (2 AP) -> the enemy locates ONCE per pass, not twice, and the
        # single-action call reports the "complex" cost that makes the wrapper stop.
        monkeypatch.setattr(eng, "enemy_locate_test",
                            lambda **kw: {"located": False, "net_successes": 0})
        state = self._state()
        enemy = self._located_enemy(located=False, revealed=False)
        assert mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy) == "complex"
        # Fresh enemy, full pass: only a SINGLE locate attempt is made (one probing event, not two).
        state2 = self._state()
        enemy2 = self._located_enemy(located=False, revealed=False)
        mr._enemy_decker_take_pass(state2, self._decker(), _RunStub(), enemy2)
        probing = [e for e in state2["event_log"]
                   if e.get("type") == "enemy_decker" and e.get("outcome") == "probing"]
        assert len(probing) == 1 and enemy2.get("located") is not True

    def test_pass_stops_when_first_attack_ends_the_run(self, monkeypatch):
        # If the first attack crashes the PC's icon (run ends), the wrapper must NOT drive a second.
        monkeypatch.setattr(eng, "cybercombat_attack", self._canned_cybercombat(boxes=10))
        state = self._state()
        mr._enemy_decker_take_pass(state, self._decker(), _RunStub(), self._located_enemy())
        assert state.get("run_ended") is True
        assert len(self._attacks(state)) == 1   # stopped after the kill; no phantom second action

    def test_pass_stops_when_enemy_leaves_play(self):
        # An enemy whose own icon is already crashing is dumped on its first action ("end" cost);
        # the wrapper honours the status guard and takes no second action.
        state = self._state()
        enemy = self._located_enemy(condition_monitor={"persona_boxes": 10})
        mr._enemy_decker_take_pass(state, self._decker(), _RunStub(), enemy)
        assert enemy["status"] == "fled"
        fled = [e for e in state["event_log"]
                if e.get("type") == "enemy_decker" and e.get("outcome") == "fled"]
        assert len(fled) == 1

    def test_take_turn_returns_end_when_run_already_over(self):
        state = self._state(); state["run_ended"] = True
        assert mr._enemy_decker_take_turn(state, self._decker(), _RunStub(),
                                          self._located_enemy()) == "end"


class TestEnemyHogSelfPurge:
    """Spec #1 -- a security decker infected by the PC's Hog must be able to Purge the virus and
    reload its drained programs (Swap Memory), so a Hog is not a permanent disable."""

    def _decker(self):
        return {"name": "Ghost", "bod": 5, "evasion": 5, "masking": 5, "sensor": 5, "mpcp": 6,
                "intelligence": 5, "body": 5, "hardening": 0, "utilities": {"sleaze": 4}}

    def _state(self):
        s = _fresh_state(sec_code="Red", sec_value=9)
        s["event_log"] = []
        s["security_tally"] = 0
        s["condition_monitor"] = {"persona_boxes": 0, "physical_boxes": 0, "stun_boxes": 0,
                                  "mpcp_damage": 0,
                                  "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0}}
        return s

    def _infected_enemy(self, **over):
        # attack drained from 6 -> 2 (4 points lost); base_utilities remembers the pre-drain rating.
        e = {"id": "ed1", "name": "Red Decker", "tier": "Red", "status": "active",
             "revealed": True, "located": True, "scanned_pc": True, "intent": "dump",
             "bod": 5, "evasion": 5, "masking": 5, "sensor": 5,
             "computer_skill": 8, "mpcp": 6, "intelligence": 5, "initiative": 20, "hardening": 0,
             "utilities": {"attack": 2}, "base_utilities": {"attack": 6},
             "condition_monitor": {"persona_boxes": 0}}
        e.update(over)
        return e

    def test_lost_points_and_infection_lookup(self):
        state = self._state()
        enemy = self._infected_enemy()
        state["hog_infections"] = [{"id": "h1", "attacker_id": "pc", "target_id": "ed1",
                                    "rating": 4, "drain": 2}]
        assert mr._enemy_hog_lost_points(enemy) == 4
        assert mr._enemy_hog_infection(state, enemy)["id"] == "h1"

    def test_purge_success_removes_virus_and_arms_reload(self, scripted):
        # TN = (Hog 4 - Hardening 0) + base program 6 = 10. One die explodes 6+6+1 = 13 >= 10.
        scripted([6, 1, 1, 1, 1, 1, 1, 1, 6, 1])
        state = self._state()
        enemy = self._infected_enemy()
        state["hog_infections"] = [{"id": "h1", "attacker_id": "pc", "target_id": "ed1",
                                    "rating": 4, "drain": 2}]
        acted = mr._enemy_purge_hog(state, enemy)
        assert acted is True
        assert state["hog_infections"] == []          # virus wiped
        assert enemy["hog_reload_pending"] is True     # Swap Memory queued
        assert any(e.get("outcome") == "purge_hog" and not e.get("gm_only")
                   for e in state["event_log"])        # player sees it

    def test_swap_reload_restores_drained_programs(self):
        state = self._state()
        enemy = self._infected_enemy(hog_reload_pending=True)
        restored = mr._enemy_swap_reload(state, enemy)
        assert restored is True
        assert enemy["utilities"]["attack"] == 6       # back to base
        assert enemy["base_utilities"] == {}
        assert enemy["hog_reload_pending"] is False
        assert any(e.get("outcome") == "swap_memory" for e in state["event_log"])

    def test_purge_skipped_when_drain_trivial(self):
        state = self._state()
        # only 1 point lost -> below the >= 2 threshold, not worth an action
        enemy = self._infected_enemy(utilities={"attack": 5}, base_utilities={"attack": 6})
        state["hog_infections"] = [{"id": "h1", "attacker_id": "pc", "target_id": "ed1",
                                    "rating": 4, "drain": 1}]
        assert mr._enemy_purge_hog(state, enemy) is False

    def test_take_turn_prefers_recovery_over_attack(self, scripted):
        # A located, infected enemy spends its action purging rather than attacking.
        scripted([6, 1, 1, 1, 1, 1, 1, 1, 6, 1])
        state = self._state()
        enemy = self._infected_enemy()
        state["hog_infections"] = [{"id": "h1", "attacker_id": "pc", "target_id": "ed1",
                                    "rating": 4, "drain": 2}]
        cost = mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy)
        assert cost == "complex"
        assert enemy.get("hog_reload_pending") is True
        # next action reloads (Swap Memory, Simple)
        cost2 = mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy)
        assert cost2 == "simple"
        assert enemy["utilities"]["attack"] == 6


class TestEnemyLocateAndIntent:
    def test_locate_progress_is_net_enemy_successes(self, scripted):
        # enemy 3 hits (TN low), PC 1 hit -> net +2
        scripted([6, 6, 6, 1, 6, 1, 1])
        r = eng.enemy_locate_test(computer_skill=8, scanner_rating=2,
                                  sensor_rating=4, pc_detection_factor=6, pc_evasion=4)
        assert r["net_successes"] >= 0
        assert r["enemy_tn"] == 4  # 6 - 2 scanner

    def test_locate_never_negative(self, scripted):
        scripted([1, 1, 1, 6, 6, 6])  # enemy whiffs, PC resists well
        r = eng.enemy_locate_test(computer_skill=4, scanner_rating=0,
                                  sensor_rating=6, pc_detection_factor=8, pc_evasion=6)
        assert r["net_successes"] == 0 and r["located"] is False

    def test_pc_locate_decker_tn_is_full_mask_plus_sleaze(self, scripted):
        # Correction #6 (vr2 L1880): the PC's Sensor Test TN is the enemy's FULL Masking +
        # Sleaze minus Scanner -- NOT the halved Detection Factor. mask 5 + sleaze 3 - scanner 2
        # = 6; the old halved Detection-Factor basis would have been only ceil(8/2) - 2 = 2.
        scripted([6, 6, 1, 1, 1, 1, 1, 1])  # PC: two 6s vs TN6 -> 2 successes; enemy resist whiffs
        r = eng.pc_locate_decker_test(sensor_rating=5, scanner_rating=2,
                                      enemy_mask_sleaze=5 + 3, enemy_evasion=3)
        assert r["target_tn"] == 6                              # full mask+sleaze (8) - scanner (2)
        assert r["target_tn"] > eng.detection_factor(5, 3) - 2  # strictly harder than the old halved basis
        assert r["located"] is True and r["net_successes"] == 2

    def test_intent_escalates_with_tally(self):
        # A 'dump' decker turns lethal once the alarm is high; 'kill' stays 'kill'.
        assert eng.escalate_enemy_intent("dump", security_tally=5) == "dump"
        assert eng.escalate_enemy_intent("dump", security_tally=15) == "kill"
        assert eng.escalate_enemy_intent("kill", security_tally=2) == "kill"
        assert eng.escalate_enemy_intent("kill", security_tally=99) == "kill"

    def test_program_loadouts_scale_by_tier(self):
        assert eng.generate_enemy_decker("Blue", 4)["programs"] == ["Attack"]
        assert "Hog" in eng.generate_enemy_decker("Green", 6)["programs"]
        red = eng.generate_enemy_decker("Red", 9)["programs"]
        assert {"Hog", "Poison", "Reveal", "Black Hammer"} <= set(red)
        black = eng.generate_enemy_decker("Black", 12)["programs"]
        assert {"Restrict", "Killjoy"} <= set(black)

    def test_hog_reduction_is_net_over_two(self, scripted):
        # attack 4 hits (TN low), MPCP resist 0 -> net 4 -> reduction 2
        scripted([6, 6, 6, 6, 1, 1, 1])
        r = eng.hog_attack(attacker_pool=8, security_code="Red", target_status="intruding",
                           hog_rating=8, mpcp_rating=6)
        assert r["reduction"] == r["net"] // 2 and r["reduction"] >= 1

    def test_decker_crippler_reduction(self, scripted):
        scripted([6, 6, 6, 1, 1])  # attack 3 hits, attr resist ~0 -> net 3 -> reduction 1
        r = eng.decker_attribute_attack(attacker_pool=6, security_code="Red",
                                        target_status="intruding", program_rating=6,
                                        target_attribute_rating=4)
        assert r["reduction"] == r["net"] // 2

    def test_hog_purge_tn_and_success(self, scripted):
        # roll_dice rolls all 10 raw dice first, THEN explodes 6s. raw die0=6, the explosion
        # reroll (11th value)=3 -> 6+3=9 >= TN 9 -> one success. Other raw dice are 1s.
        scripted([6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3])
        r = eng.hog_purge_test(computer_skill=10, hog_rating=6, infected_program_rating=4, hardening=1)
        assert r["tn"] == (6 - 1) + 4   # (Hog rating - Hardening) + infected program rating = 9
        assert r["purged"] is True

    def test_apply_hog_drain_hits_highest_running(self):
        decker = {"utilities": {"deception": 6, "analyze": 4}}
        state = {"program_damage": {}}
        frag = mr._apply_hog_drain(state, decker, 2)
        assert "Deception" in frag and state["program_damage"]["deception"] == 2
        # next drain still hits Deception (now 4) over analyze (4) on a tie -> first found
        mr._apply_hog_drain(state, decker, 5)   # 4 left -> capped, crashes
        assert state["program_damage"]["deception"] == 6  # crashed (>= base)

    def test_apply_hog_drain_noop_when_nothing_running(self):
        decker = {"utilities": {"deception": 2}}
        state = {"program_damage": {"deception": 2}}  # already crashed
        assert mr._apply_hog_drain(state, decker, 3) == ""

    def test_player_view_redacts_enemy_internals(self):
        enemy = eng.generate_enemy_decker("Red", 8)
        enemy["id"] = "ed_1"
        enemy["condition_monitor"] = {"persona_boxes": 4, "mpcp_damage": 0}
        red = mr._redact_enemy_decker(enemy)
        # presence + condition only -- name is shown, but the threat TIER is hidden until the PC
        # runs Scan Icon, and INTENT (the decker's plan) is never surfaced to the player at all.
        assert red["name"]
        assert red["tier"] is None            # unscanned -> threat tier hidden
        assert "intent" not in red            # a decker's intent is never disclosed
        assert red["condition_monitor"]["persona_boxes"] == 4
        for secret in ("computer_skill", "mpcp", "utilities", "detection_factor"):
            assert secret not in red
        # Once Scan Icon has revealed ratings, the tier becomes visible (still no intent).
        enemy["scan_reveal"] = 2
        red2 = mr._redact_enemy_decker(enemy)
        assert red2["tier"] == "Red" and "intent" not in red2


class TestPCCripplerStrikeBack:
    """vr2 -- the PC's Poison / Restrict / Reveal offensive cripplers vs an enemy decker,
    fired through the Strike Back endpoint. Poison->Bod, Restrict->Evasion, Reveal->Masking;
    the attacker's net successes // 2 reduce the targeted attribute, floored at 1; a miss does
    nothing. Cripplers target enemy DECKERS only (the endpoint never touches IC)."""

    def _decker(self):
        return {"name": "Ghost", "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                "mpcp": 6, "computer_skill": 8, "intelligence": 5, "body": 5, "hardening": 0,
                "utilities": {"attack": 6, "poison": 6, "restrict": 6, "reveal": 6}}

    def _enemy(self, **over):
        e = {"id": "ed1", "name": "Red Decker", "tier": "Red", "status": "active",
             "revealed": True, "intent": "dump",
             "bod": 5, "evasion": 5, "masking": 5, "sensor": 5,
             "computer_skill": 8, "detection_factor": 4,
             "utilities": {"sleaze": 5}, "condition_monitor": {"persona_boxes": 0}}
        e.update(over)
        return e

    def _strike(self, monkeypatch, *, program, enemy, reduction, attack_pool=6, extra_ic=None):
        import asyncio
        from app.schemas.matrix_run import RunEnemyAttackInput

        # Deterministic crippler resolution: drive the engine's reduction directly so the test
        # exercises the router application path (_resolve_attribute_attack: attribute mapping /
        # floor / Detection-Factor recompute / event), not the dice. The shared resolver calls
        # eng.crippler_attack for every attribute attack, so we fake that primitive.
        def _fake_attr(**kw):
            return {"attack_roll": {"successes": reduction * 2, "ones": 0,
                                    "pool": kw.get("security_value", 6)},
                    "defense_roll": {"successes": 0}, "net_successes": reduction * 2,
                    "attribute_reduction": reduction, "shield_successes": 0, "is_ripper": False}
        monkeypatch.setattr(eng, "crippler_attack", _fake_attr)

        decker = self._decker()
        state = _fresh_state(sec_code="Red", sec_value=9)
        state["event_log"] = []
        state["hackingPool_remaining"] = 10
        state["enemy_deckers"] = [enemy]
        if extra_ic is not None:
            state["active_ic"] = [extra_ic]

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        inp = RunEnemyAttackInput(enemy_id="ed1", attack_pool=attack_pool,
                                  hacking_pool_dice=0, program=program)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.attack_enemy_decker(run_id=7, body=inp, auth=auth, db=_FakeDB()))
        return run.state_json

    def _last_crippled(self, state):
        evs = [x for x in state["event_log"] if x.get("type") == "decker_crippled"]
        assert evs, "no decker_crippled event emitted"
        return evs[-1]

    def test_poison_reduces_bod_by_net_over_two(self, monkeypatch):
        state = self._strike(monkeypatch, program="poison", enemy=self._enemy(bod=5), reduction=2)
        e = state["enemy_deckers"][0]
        assert e["bod"] == 5                                    # base untouched (ledger model)
        assert e["condition_monitor"]["persona_damage"]["bod"] == 2
        assert mr._enemy_effective_attr(e, "bod") == 3          # effective = 5 - (net // 2 = 2)
        ev = self._last_crippled(state)
        assert ev["attribute"] == "bod" and ev["reduction"] == 2
        assert ev["success"] is True and ev["enemy_attr_value"] == 3

    def test_restrict_reduces_evasion(self, monkeypatch):
        state = self._strike(monkeypatch, program="restrict", enemy=self._enemy(evasion=5), reduction=2)
        assert mr._enemy_effective_attr(state["enemy_deckers"][0], "evasion") == 3
        assert self._last_crippled(state)["attribute"] == "evasion"

    def test_reveal_reduces_masking_and_recomputes_detection_factor(self, monkeypatch):
        enemy = self._enemy(masking=6, detection_factor=7, utilities={"sleaze": 4})
        state = self._strike(monkeypatch, program="reveal", enemy=enemy, reduction=2)
        e = state["enemy_deckers"][0]
        assert mr._enemy_effective_attr(e, "masking") == 4     # 6 - 2 (base untouched)
        # Reveal lowers Masking -> Detection Factor recomputed = ceil((4 + 4 sleaze) / 2) = 4.
        assert e["detection_factor"] == 4
        assert self._last_crippled(state)["attribute"] == "masking"

    def test_reduction_floors_attribute_at_one(self, monkeypatch):
        state = self._strike(monkeypatch, program="poison", enemy=self._enemy(bod=2), reduction=9)
        e = state["enemy_deckers"][0]
        assert mr._enemy_effective_attr(e, "bod") == 1          # never below 1
        ev = self._last_crippled(state)
        assert ev["reduction"] == 1 and ev["enemy_attr_value"] == 1   # only 2->1 was possible

    def test_miss_does_nothing(self, monkeypatch):
        state = self._strike(monkeypatch, program="restrict", enemy=self._enemy(evasion=5), reduction=0)
        assert state["enemy_deckers"][0]["evasion"] == 5   # unchanged
        ev = self._last_crippled(state)
        assert ev["success"] is False and ev["reduction"] == 0

    def test_three_programs_map_to_bems_attributes(self, monkeypatch):
        for program, attr in (("poison", "bod"), ("restrict", "evasion"), ("reveal", "masking")):
            state = self._strike(monkeypatch, program=program, enemy=self._enemy(), reduction=1)
            e = state["enemy_deckers"][0]
            assert mr._enemy_effective_attr(e, attr) == 4       # 5 - 1, the targeted attribute
            for other in ("bod", "evasion", "masking"):
                if other != attr:
                    assert mr._enemy_effective_attr(e, other) == 5   # the others are untouched

    def test_crippler_targets_decker_not_ic(self, monkeypatch):
        ic = {"id": "ic1", "type": "Killer", "rating": 6, "status": "active", "bod": 9}
        state = self._strike(monkeypatch, program="poison", enemy=self._enemy(bod=5),
                             reduction=2, extra_ic=ic)
        assert state["active_ic"] == [ic]                  # IC is irrelevant to a crippler strike
        assert mr._enemy_effective_attr(state["enemy_deckers"][0], "bod") == 3   # only the decker was hit


class _QueueRoll:
    """Fake eng.roll_dice: returns scripted result dicts in order, recording (pool, tn) per call.

    Lets a test drive the lethal-strike to-hit and the post-crash MPCP-burn rolls independently
    and assert the dice pools (e.g. that the MPCP test rolls at DOUBLE the program rating)."""

    def __init__(self, results):
        self.results = list(results)
        self.calls = []

    def __call__(self, pool, tn=4):
        self.calls.append((pool, tn))
        r = self.results.pop(0) if self.results else {}
        out = {"successes": 0, "ones": 0, "rolls": [], "pool": pool, "tn": tn}
        out.update(r)
        out["tn"] = tn
        return out


class TestPCLethalStrikeBack:
    """vr2 -- the PC's lethal offensive programs Black Hammer (Physical) / Killjoy (Stun) vs an
    enemy decker, fired through the Strike Back endpoint. They "function like black IC but from a
    decker": a hard icon hit (resisted with the enemy's Bod) that, on an icon CRASH, burns the
    enemy's MPCP via a blaster-style test at DOUBLE the program rating and takes the hostile
    decker out. The effective rating is capped at ceil(Computer skill / 2). For an NPC enemy the
    Physical/Stun distinction is narrative only (same icon crash). Deckers only -- never IC."""

    def _enemy(self, **over):
        e = {"id": "ed1", "name": "Black Decker", "tier": "Black", "status": "active",
             "revealed": True, "intent": "kill",
             "bod": 6, "evasion": 6, "masking": 6, "sensor": 6, "mpcp": 8,
             "computer_skill": 10, "hardening": 1, "detection_factor": 4,
             "utilities": {"sleaze": 6},
             "condition_monitor": {"persona_boxes": 0, "mpcp_damage": 0}}
        e.update(over)
        return e

    def _strike(self, monkeypatch, *, program, enemy, boxes, mpcp_succ=0,
                attack_pool=6, computer=10, carried=None, extra_ic=None):
        import asyncio
        from app.schemas.matrix_run import RunEnemyAttackInput

        captured = {}

        # Drive the icon-damage result directly so the test exercises the router (crash logic,
        # MPCP burn, rating clamp, event shape), not the resistance dice. Capture the effective
        # power (= the clamped program rating) the branch passes in.
        def _fake_dr(**kw):
            captured["power"] = kw["power"]
            captured["base"] = kw["base_damage_level"]
            captured["bod"] = kw["bod"]
            return {"boxes": boxes, "final_damage_level": "Serious", "effective_power": kw["power"],
                    "attacker_successes": kw["attacker_successes"], "resist_roll": {"successes": 0}}
        monkeypatch.setattr(eng, "damage_resistance", _fake_dr)

        # roll_dice: call 0 = the to-hit; call 1 (crash only) = the MPCP burn (rating*2 dice).
        roller = _QueueRoll([{"successes": 2}, {"successes": mpcp_succ * 2}])
        monkeypatch.setattr(eng, "roll_dice", roller)

        util = {"attack": 6}
        if carried is not None:
            util[program] = carried
        decker = {"name": "Ghost", "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                  "mpcp": 6, "computer_skill": computer, "intelligence": 5, "body": 5,
                  "hardening": 0, "utilities": util}
        state = _fresh_state(sec_code="Red", sec_value=9)
        state["event_log"] = []
        state["hackingPool_remaining"] = 10
        state["enemy_deckers"] = [enemy]
        if extra_ic is not None:
            state["active_ic"] = [extra_ic]

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        inp = RunEnemyAttackInput(enemy_id="ed1", attack_pool=attack_pool,
                                  hacking_pool_dice=0, program=program)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.attack_enemy_decker(run_id=7, body=inp, auth=auth, db=_FakeDB()))
        return run.state_json, captured, roller

    def _events(self, state, outcome=None):
        evs = [x for x in state["event_log"] if x.get("type") == "decker_lethal"]
        if outcome is not None:
            evs = [x for x in evs if x.get("outcome") == outcome]
        return evs

    def test_hit_damages_enemy_icon_without_crash(self, monkeypatch):
        state, _cap, _r = self._strike(monkeypatch, program="black_hammer",
                                       enemy=self._enemy(), boxes=3, carried=5)
        e = state["enemy_deckers"][0]
        assert e["condition_monitor"]["persona_boxes"] == 3   # icon took the hit
        assert e["status"] == "active"                        # not yet crashed
        hit = self._events(state, "hit")
        assert len(hit) == 1 and hit[0]["success"] is True
        assert not self._events(state, "crash")               # no crash event below 10 boxes

    def test_black_hammer_is_physical_killjoy_is_stun(self, monkeypatch):
        bh, _c, _r = self._strike(monkeypatch, program="black_hammer",
                                  enemy=self._enemy(), boxes=3, carried=5)
        kj, _c2, _r2 = self._strike(monkeypatch, program="killjoy",
                                    enemy=self._enemy(), boxes=3, carried=5)
        bh_hit = self._events(bh, "hit")[0]
        kj_hit = self._events(kj, "hit")[0]
        assert bh_hit["program"] == "black_hammer" and bh_hit["damage_kind"] == "Physical"
        assert kj_hit["program"] == "killjoy" and kj_hit["damage_kind"] == "Stun"

    def test_crash_burns_mpcp_at_double_rating_and_removes_enemy(self, monkeypatch):
        # computer 10 -> cap 5; carried 5 -> effective rating 5. boxes 10 -> icon crashes.
        # mpcp_succ 2 -> the MPCP roll returns 4 successes -> 4 // 2 = 2 MPCP burned.
        enemy = self._enemy(mpcp=8, hardening=1)
        state, _cap, roller = self._strike(monkeypatch, program="black_hammer",
                                           enemy=enemy, boxes=10, mpcp_succ=2, carried=5)
        e = state["enemy_deckers"][0]
        assert e["status"] == "crashed"                       # enemy taken out of the run
        assert e["condition_monitor"]["mpcp_damage"] == 2     # permanent MPCP burn
        assert e["mpcp"] == 8                                 # raw MPCP intact (effective = 8-2)
        # The 2nd roll_dice call is the MPCP burn: rating(5) * 2 = 10 dice vs mpcp(8)+hardening(1).
        assert roller.calls[1] == (10, 9)
        crash = self._events(state, "crash")
        assert len(crash) == 1 and crash[0]["mpcp_reduction"] == 2

    def test_rating_clamped_to_ceil_computer_over_two(self, monkeypatch):
        # computer 8 -> cap ceil(8/2)=4; carried 10 is above the cap -> clamped to 4.
        state, captured, _r = self._strike(monkeypatch, program="black_hammer",
                                           enemy=self._enemy(), boxes=2, computer=8, carried=10)
        # rating clamped to 4; then the enemy's Hardening (1) reduces the resist Power to 3.
        assert captured["power"] == 3
        hit = self._events(state, "hit")[0]
        assert hit["program_rating"] == 4
        assert "clamp" in hit["description"].lower()

    def test_odd_computer_skill_rounds_cap_up(self, monkeypatch):
        # computer 7 -> ceil(7/2)=4 (round up); carried 6 is above 4 -> clamped to 4.
        state, captured, _r = self._strike(monkeypatch, program="killjoy",
                                           enemy=self._enemy(), boxes=2, computer=7, carried=6)
        # rating clamped to 4; then the enemy's Hardening (1) reduces the resist Power to 3.
        assert captured["power"] == 3

    def test_carried_rating_at_or_below_cap_is_used_unclamped(self, monkeypatch):
        # computer 10 -> cap 5; carried 3 (<= cap) -> used as-is, no clamp note.
        state, captured, _r = self._strike(monkeypatch, program="black_hammer",
                                           enemy=self._enemy(), boxes=2, computer=10, carried=3)
        # rating 3 (<= cap, unclamped); then the enemy's Hardening (1) reduces the resist Power to 2.
        assert captured["power"] == 2
        assert "clamp" not in self._events(state, "hit")[0]["description"].lower()

    def test_lethal_uses_serious_base_level(self, monkeypatch):
        state, captured, _r = self._strike(monkeypatch, program="black_hammer",
                                           enemy=self._enemy(), boxes=2, carried=5)
        assert captured["base"] == "Serious"                  # fixed lethal base, not host code
        assert captured["bod"] == 6                           # enemy resists icon damage with Bod

    def test_lethal_targets_decker_not_ic(self, monkeypatch):
        ic = {"id": "ic1", "type": "Killer", "rating": 6, "status": "active", "bod": 9}
        state, _cap, _r = self._strike(monkeypatch, program="killjoy",
                                       enemy=self._enemy(), boxes=10, mpcp_succ=2,
                                       carried=5, extra_ic=ic)
        assert state["active_ic"] == [ic]                     # IC untouched by a lethal strike
        assert state["enemy_deckers"][0]["status"] == "crashed"

    def test_roll_enemy_mpcp_damage_doubles_rating_and_accrues(self, monkeypatch):
        # Direct unit test of the helper: rating 4 -> 4*2 = 8 dice vs mpcp(8)+hardening(2)=10.
        roller = _QueueRoll([{"successes": 5}])
        monkeypatch.setattr(eng, "roll_dice", roller)
        enemy = {"mpcp": 8, "hardening": 2, "condition_monitor": {"mpcp_damage": 0}}
        hits, _roll = mr._roll_enemy_mpcp_damage(enemy, 4, pool_multiplier=2)
        assert roller.calls == [(8, 10)]                      # double rating dice vs MPCP+Hardening
        assert hits == 2                                      # 5 successes // 2
        assert enemy["condition_monitor"]["mpcp_damage"] == 2
        assert enemy["mpcp"] == 8                             # raw MPCP left intact (mirror PC side)


class TestPersonaModes:
    """vr2 Persona Modes -- boosted attribute +50%, others -50%; flows into DF + combat."""

    def _decker(self, mode):
        return {"bod": 6, "evasion": 6, "masking": 6, "sensor": 6, "mpcp": 6,
                "persona_mode": mode, "utilities": {"sleaze": 8}}

    def _state(self):
        s = _fresh_state()
        s["condition_monitor"] = {"persona_damage": {}, "mpcp_damage": 0}
        return s

    def test_masking_mode_boosts_masking_and_raises_df(self):
        eff = mr._get_decker_effective(self._decker("masking"), self._state())
        assert eff["masking"] == 9   # 6 * 1.5
        assert eff["evasion"] == 3 and eff["sensor"] == 3
        assert eff["bod"] == 6       # Masking mode leaves Bod alone
        # DF rises: ceil((9 + 8)/2) = 9 (vs 7 in standard mode)
        assert mr._effective_detection_factor(self._state(), self._decker("masking")) == 9

    def test_sensor_mode_boosts_sensor_cuts_masking(self):
        eff = mr._get_decker_effective(self._decker("sensor"), self._state())
        assert eff["sensor"] == 9 and eff["masking"] == 3

    def test_no_mode_is_unchanged(self):
        eff = mr._get_decker_effective(self._decker("none"), self._state())
        assert eff == {"bod": 6, "evasion": 6, "masking": 6, "sensor": 6, "mpcp": 6}


class TestScramblePaydata:
    """vr2 #6 -- Decrypt vs Scramble IC; Poison wipes key data on failure."""

    def test_decrypt_tn_reduced_by_decrypt_utility(self, scripted):
        scripted([6])
        r = eng.scramble_decrypt_test(decker_pool=8, scramble_rating=8, decrypt_utility=3)
        assert r["tn"] == 5  # 8 - 3
        assert r["decrypted"] is True

    def test_decrypt_floor_tn_two(self, scripted):
        scripted([1])
        r = eng.scramble_decrypt_test(decker_pool=6, scramble_rating=4, decrypt_utility=9)
        assert r["tn"] == 2
        assert r["decrypted"] is False

    def test_poison_failure_destroys_key_data(self, scripted):
        # Failed decrypt -> the IC's Poison Test (rating vs TN = Computer skill) SUCCEEDS -> wipe.
        scripted([6])                                            # IC dice all 6 -> successes
        c = eng.scramble_failure_consequence(
            variant="poison", is_key=True, scramble_rating=6, decker_computer_skill=6)
        assert c["data_destroyed"] is True
        assert c["key_data_lost"] is True
        assert "KEY DATA DESTROYED" in c["message"]

    def test_poison_failure_destroys_nonkey_data_quietly(self, scripted):
        scripted([6])                                            # IC Poison Test succeeds
        c = eng.scramble_failure_consequence(
            variant="poison", is_key=False, scramble_rating=6, decker_computer_skill=6)
        assert c["data_destroyed"] is True
        assert c["key_data_lost"] is False
        assert "KEY DATA DESTROYED" not in c["message"]

    def test_poison_test_miss_leaves_data_safe(self, scripted):
        # Failed decrypt, but the IC's Poison Test MISSES (all 1s) -> the protected data survives.
        scripted([1])
        c = eng.scramble_failure_consequence(
            variant="poison", is_key=True, scramble_rating=6, decker_computer_skill=6)
        assert c["data_destroyed"] is False
        assert c["key_data_lost"] is False
        assert "survives" in c["message"]

    def test_exploding_failure_triggers_data_bomb_not_wipe(self):
        c = eng.scramble_failure_consequence(variant="exploding", is_key=True)
        assert c["data_destroyed"] is False
        assert c["detonate_data_bomb"] is True
        # the detonation itself reuses the data-bomb engine (rating)Moderate + tally
        det = eng.data_bomb_detonate(ic_rating=8, target_bod=6)
        assert det["tally_increase"] == 8 and det["damage_level"] == "Moderate"

    def test_standard_failure_no_destruction(self):
        c = eng.scramble_failure_consequence(variant="standard", is_key=True)
        assert c["data_destroyed"] is False

    def test_initial_state_loads_paydata_and_scrambles(self):
        class _Host:
            config_json = {
                "security_code": "Blue", "security_value": 4, "acifs": [8, 10, 9, 9, 8],
                "paydata": [{"name": "Personnel Files", "is_key": True}],
                "scrambles": [{"target_key": "Files:file:Personnel Files",
                               "rating": 6, "variant": "poison"}],
            }
        st = mr._initial_state(
            {"masking": 4, "intelligence": 5, "mpcp": 6, "utilities": {}}, _Host())
        assert st["paydata"][0]["is_key"] is True
        assert st["scrambles"][0]["variant"] == "poison"

    def test_initial_state_loads_data_bombs(self):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6,
                           "data_bombs": [{"target": "Secure File", "rating": 6}]}
        st = mr._initial_state({"masking": 4, "intelligence": 5, "mpcp": 6, "utilities": {}}, _Host())
        assert st["data_bombs"][0]["rating"] == 6
        assert st["defused_bombs"] == []

    def test_initial_state_loads_trap_doors_undiscovered(self):
        # vr2 trap door: concealed on a subsystem, undiscovered until Analyze Subsystem; the
        # destination is seeded but stays GM-only until entered (see _serialize_run).
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6}
            ltg_address = None
            trap_doors_json = [{
                "id": 12345, "source_piece": "Maglock Controller", "subsystem": "slave",
                "destination_host_id": 4, "destination_ltg": "LTG 2207",
                "destination_label": "Shiseki Clan Host",
            }]
        st = mr._initial_state({"masking": 4, "intelligence": 5, "mpcp": 6, "utilities": {}}, _Host())
        door = st["trap_doors"][0]
        assert door["id"] == "12345"            # normalized to str for path round-trip
        assert door["subsystem"] == "slave"
        assert door["discovered"] is False and door["filed"] is False
        assert door["destination_label"] == "Shiseki Clan Host"

    def test_initial_state_host_ltg_hidden_until_revealed(self):
        # The host's own LTG-access status + grid address are seeded but stay unrevealed until a
        # successful Analyze Subsystem on Access. The Security Rating is likewise hidden for every
        # host (host_security_revealed False) until Analyze Host reveals it.
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6}
            ltg_address = "LTG 4080"
        st = mr._initial_state({"masking": 4, "intelligence": 5, "mpcp": 6, "utilities": {}}, _Host())
        assert st["host_has_ltg"] is True
        assert st["host_ltg_address"] == "LTG 4080"
        assert st["host_ltg_revealed"] is False
        assert st["host_security_revealed"] is False

    def test_initial_state_trap_doors_default_empty(self):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6}
        st = mr._initial_state({"masking": 4, "intelligence": 5, "mpcp": 6, "utilities": {}}, _Host())
        assert st["trap_doors"] == []
        assert st["host_has_ltg"] is False

    def test_secret_state_keys_are_gm_only(self):
        for k in ("scrambles", "paydata", "data_bombs", "trap_doors"):
            assert k in mr._GM_ONLY_STATE_KEYS


class TestTrapDoorHostStack:
    """B34: entering a trap door SUSPENDS the current host onto a stack (persona carried), and a
    graceful logoff / host crash on the deeper host POPS back to it. host_stack is GM-only; only a
    host_stack_depth count reaches the player."""

    class _Host:
        def __init__(self, hid, name):
            self.id = hid
            self.name = name
            self.config_json = {"security_code": "Green", "security_value": 6}
            self.ltg_address = None

    def _decker(self):
        return {"masking": 4, "intelligence": 5, "mpcp": 6, "utilities": {}, "computer_skill": 6}

    def test_push_suspends_current_and_carries_persona(self):
        decker = self._decker()
        src = self._Host(1, "Alpha")
        dst = self._Host(2, "Bravo")
        state = mr._initial_state(decker, src)
        state["security_tally"] = 7
        state["condition_monitor"]["persona_boxes"] = 3
        state["hackingPool_remaining"] = 1
        state["logon_complete"] = True

        new_state = mr._push_host_stack(state, src, dst, decker)
        # Fresh host frame for the destination...
        assert new_state["security_tally"] == 0
        assert new_state["logon_complete"] is False
        # ...persona carried forward...
        assert new_state["condition_monitor"]["persona_boxes"] == 3
        assert new_state["hackingPool_remaining"] == 1
        # ...and the parent suspended on the stack.
        assert len(new_state["host_stack"]) == 1
        frame = new_state["host_stack"][0]
        assert frame["_stack_host_id"] == 1
        assert frame["security_tally"] == 7

    def test_pop_resumes_parent_and_carries_persona_back(self):
        decker = self._decker()
        src = self._Host(1, "Alpha")
        dst = self._Host(2, "Bravo")
        state = mr._initial_state(decker, src)
        state["security_tally"] = 7
        deep = mr._push_host_stack(state, src, dst, decker)
        # Take damage on the deeper host, then log off back to the parent.
        deep["condition_monitor"]["persona_boxes"] = 5
        popped = mr._pop_host_stack(deep)
        assert popped is not None
        resumed, host_id = popped
        assert host_id == 1
        # Parent host frame restored (its tally)...
        assert resumed["security_tally"] == 7
        assert resumed["run_ended"] is False
        assert resumed["host_stack"] == []
        # ...but the damage taken on the deeper host follows the persona back.
        assert resumed["condition_monitor"]["persona_boxes"] == 5

    def test_pop_empty_stack_returns_none(self):
        state = mr._initial_state(self._decker(), self._Host(1, "Alpha"))
        assert mr._pop_host_stack(state) is None

    def test_host_stack_is_gm_only_but_depth_surfaces(self):
        assert "host_stack" in mr._GM_ONLY_STATE_KEYS



class TestScrambleDiscovery:
    """vr2 #17 -- Decrypt File requires the protecting Scramble IC to be DISCOVERED first, via an
    Analyze Subsystem on the Files/Slave subsystem that holds it (vr2 L1864). Discovery flips the
    scramble's ``discovered`` flag + emits ``scramble_found``; ``_serialize_run`` exposes only the
    discovered ones (target_key/subsystem/label -- never rating/variant); and Decrypt File matches
    the scramble by its full target_key (never silently falling back to ``scrambles[0]``), refusing
    the op outright when no discovered scramble matches (no test, no tally)."""

    FILES_KEY = "files::file::Lone Star IC Design"
    SLAVE_KEY = "slave::piece::LAN to Payroll"

    def _decker(self):
        return {"name": "Static", "mpcp": 8, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                "computer_skill": 6, "intelligence": 6, "utilities": {"decrypt": 4}}

    def _host(self, scrambles):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6,
                           "acifs": [8, 9, 8, 10, 10], "scrambles": scrambles}
            ltg_address = None
            trap_doors_json = None
        return _Host()

    def _state(self, scrambles):
        st = mr._initial_state(self._decker(), self._host(scrambles))
        st["logon_complete"] = True
        return st

    class _FakeDB:
        async def commit(self):
            pass

        async def refresh(self, obj):
            pass

    def _drive(self, monkeypatch, state, *, action_type, subsystem="files",
               target_file="", system_success=True, decrypt_result=None):
        """Run the REAL ``perform_action`` (analyze_subsystem discovery + decrypt are both inline in
        it) against a stub run, mirroring the other /action drive helpers. Returns (final_state, decrypt_calls)."""
        import asyncio
        from app.schemas.matrix_run import RunActionInput

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = None
            state_json = None

        run = _StubRun()
        run.decker_json = self._decker()
        run.state_json = state

        async def _fake_get_run(db, run_id):
            return run

        def _fake_test(**kw):
            if system_success:
                return {"success": True, "decker_roll": {"successes": 3, "ones": 0},
                        "host_roll": {"successes": 0}, "decker_net_successes": 3, "tally_increase": 0}
            return {"success": False, "decker_roll": {"successes": 0, "ones": 0},
                    "host_roll": {"successes": 3}, "decker_net_successes": -3, "tally_increase": 0}

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "system_test", _fake_test)
        calls = []
        if decrypt_result is not None:
            def _fake_decrypt(**kw):
                calls.append(kw)
                return decrypt_result
            monkeypatch.setattr(eng, "scramble_decrypt_test", _fake_decrypt)

        inp = RunActionInput(action_type=action_type, subsystem=subsystem,
                             utility_rating=0, hacking_pool_dice=0, target_file=target_file)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.perform_action(run_id=7, body=inp, auth=auth, db=self._FakeDB()))
        return run.state_json, calls

    # -- Analyze Subsystem discovery ------------------------------------------

    def test_analyze_files_discovers_only_the_files_scramble(self, monkeypatch):
        scr = [{"target_key": self.FILES_KEY, "rating": 6, "variant": "standard"},
               {"target_key": self.SLAVE_KEY, "rating": 5, "variant": "standard"}]
        out, _ = self._drive(monkeypatch, self._state(scr),
                             action_type="analyze_subsystem", subsystem="files")
        by_key = {s["target_key"]: s for s in out["scrambles"]}
        assert by_key[self.FILES_KEY]["discovered"] is True
        assert by_key[self.SLAVE_KEY].get("discovered") in (None, False)
        found = [e for e in out["event_log"] if e["type"] == "scramble_found"]
        assert len(found) == 1 and found[0]["subsystem"] == "files"
        assert found[0]["target_key"] == self.FILES_KEY

    def test_analyze_slave_discovers_only_the_slave_scramble(self, monkeypatch):
        scr = [{"target_key": self.FILES_KEY, "rating": 6, "variant": "standard"},
               {"target_key": self.SLAVE_KEY, "rating": 5, "variant": "standard"}]
        out, _ = self._drive(monkeypatch, self._state(scr),
                             action_type="analyze_subsystem", subsystem="slave")
        by_key = {s["target_key"]: s for s in out["scrambles"]}
        assert by_key[self.SLAVE_KEY]["discovered"] is True
        assert by_key[self.FILES_KEY].get("discovered") in (None, False)
        found = [e for e in out["event_log"] if e["type"] == "scramble_found"]
        assert len(found) == 1 and found[0]["subsystem"] == "slave"

    # -- Serializer redaction --------------------------------------------------

    def test_serialize_redacts_scrambles_but_exposes_discovered(self):
        from types import SimpleNamespace
        from datetime import datetime, UTC
        scr = [{"target_key": self.FILES_KEY, "rating": 6, "variant": "poison", "discovered": True},
               {"target_key": self.SLAVE_KEY, "rating": 5, "variant": "standard"}]  # undiscovered
        run = SimpleNamespace(id=1, host_id=3, status="active",
                              decker_json=self._decker(), state_json=self._state(scr),
                              created_at=datetime.now(UTC), updated_at=datetime.now(UTC))
        out = mr._serialize_run(run, {"is_admin": False, "is_user": True, "user_token": None})
        st = out["state_json"]
        assert "scrambles" not in st                       # raw scrambles fully redacted for players
        ds = st["discovered_scrambles"]
        assert len(ds) == 1                                # only the DISCOVERED one is surfaced
        entry = ds[0]
        assert entry["target_key"] == self.FILES_KEY
        assert entry["subsystem"] == "files"
        assert entry["label"] == "File: Lone Star IC Design"
        assert "rating" not in entry and "variant" not in entry   # never leak the GM-only bits

    def test_serialize_admin_view_keeps_raw_scrambles(self):
        from types import SimpleNamespace
        from datetime import datetime, UTC
        scr = [{"target_key": self.FILES_KEY, "rating": 6, "variant": "poison", "discovered": True}]
        run = SimpleNamespace(id=1, host_id=3, status="active",
                              decker_json=self._decker(), state_json=self._state(scr),
                              created_at=datetime.now(UTC), updated_at=datetime.now(UTC))
        out = mr._serialize_run(run, {"is_admin": True, "is_user": False, "user_token": None})
        assert out["state_json"]["scrambles"][0]["variant"] == "poison"   # GM keeps full detail

    # -- Decrypt File target matching -----------------------------------------

    def test_decrypt_targets_scramble_by_key_removes_the_correct_one(self, monkeypatch):
        # Two discovered scrambles; target the SECOND by its full key -> only it is removed, and the
        # decrypt runs vs ITS rating (5) -- proving no silent fallback to scrambles[0] (rating 6).
        scr = [{"target_key": self.FILES_KEY, "rating": 6, "variant": "standard", "discovered": True},
               {"target_key": self.SLAVE_KEY, "rating": 5, "variant": "standard", "discovered": True}]
        out, calls = self._drive(monkeypatch, self._state(scr), action_type="decrypt_file",
                                 subsystem="files", target_file=self.SLAVE_KEY,
                                 decrypt_result={"decrypted": True, "roll": {"successes": 5, "ones": 0}})
        remaining = [s["target_key"] for s in out["scrambles"]]
        assert self.SLAVE_KEY not in remaining             # the TARGETED scramble was removed
        assert self.FILES_KEY in remaining                 # the other stays untouched
        assert calls and calls[0]["scramble_rating"] == 5  # decrypt ran vs the slave scramble
        assert any(e["type"] == "decrypt" and e.get("success") for e in out["event_log"])

    def test_decrypt_matches_discovered_scramble_by_bare_name(self, monkeypatch):
        # A bare, differently-cased name still matches the discovered scramble by its trailing segment.
        scr = [{"target_key": self.FILES_KEY, "rating": 6, "variant": "standard", "discovered": True}]
        out, calls = self._drive(monkeypatch, self._state(scr), action_type="decrypt_file",
                                 subsystem="files", target_file="lone star ic design",
                                 decrypt_result={"decrypted": True, "roll": {"successes": 4, "ones": 0}})
        assert calls and calls[0]["scramble_rating"] == 6
        assert out["scrambles"] == []                      # matched via bare-name fallback + removed

    def test_decrypt_undiscovered_scramble_is_refused(self, monkeypatch):
        # The protecting scramble exists but has NOT been discovered: decrypt must not run the test,
        # must not remove any scramble, and must emit the "No discovered scramble" guard event.
        scr = [{"target_key": self.FILES_KEY, "rating": 6, "variant": "standard"}]  # discovered=False
        out, calls = self._drive(monkeypatch, self._state(scr), action_type="decrypt_file",
                                 subsystem="files", target_file=self.FILES_KEY,
                                 decrypt_result={"decrypted": True, "roll": {"successes": 5, "ones": 0}})
        assert calls == []                                 # the decrypt test never ran
        assert len(out["scrambles"]) == 1                  # nothing removed
        assert out["scrambles"][0].get("discovered") in (None, False)
        guard = [e for e in out["event_log"] if e["type"] == "decrypt"][-1]
        assert guard["success"] is False
        assert "No discovered scramble" in guard["description"]
        assert "decker_roll" not in guard                  # guard event carries no roll

    def test_decrypt_wrong_target_among_discovered_is_refused(self, monkeypatch):
        # A discovered scramble exists, but the requested target matches none of the discovered keys.
        scr = [{"target_key": self.FILES_KEY, "rating": 6, "variant": "standard", "discovered": True}]
        out, calls = self._drive(monkeypatch, self._state(scr), action_type="decrypt_file",
                                 subsystem="files", target_file="slave::piece::Nonexistent",
                                 decrypt_result={"decrypted": True, "roll": {"successes": 5, "ones": 0}})
        assert calls == []                                 # no matching discovered scramble -> no test
        assert len(out["scrambles"]) == 1                  # the discovered one is untouched


class TestEditFile:
    """vr2 Edit File (Files Test) has two in-app sub-modes on a located paydata file: ERASE
    (destroy it) and MODIFY (tamper with / corrupt the host's copy in place). Both are sabotage
    that deny CLEAN data to the owner; neither changes the Mp the decker can bank. RAW create/copy
    are intentionally omitted (this app has no value/mission consumer for a fabricated or duplicated
    file). These drive the REAL ``perform_action`` (the edit_file block is inline in it), forcing
    the Files Test result -- mirroring the other /action drive helpers."""

    def _decker(self):
        return {"name": "Static", "mpcp": 8, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                "computer_skill": 6, "intelligence": 6, "utilities": {}}

    def _host(self):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6,
                           "acifs": [8, 9, 8, 10, 10]}
            ltg_address = None
            trap_doors_json = None
        return _Host()

    def _state(self):
        st = mr._initial_state(self._decker(), self._host())
        st["logon_complete"] = True
        st["paydata"] = [{"name": "Payroll DB", "density": 120, "is_key": True, "located": True}]
        return st

    class _FakeDB:
        async def commit(self):
            pass

        async def refresh(self, obj):
            pass

    def _drive(self, monkeypatch, state, *, target_file="Payroll DB", edit_mode="erase",
               system_success=True):
        import asyncio
        from app.schemas.matrix_run import RunActionInput

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = None
            state_json = None

        run = _StubRun()
        run.decker_json = self._decker()
        run.state_json = state

        async def _fake_get_run(db, run_id):
            return run

        def _fake_test(**kw):
            if system_success:
                return {"success": True, "decker_roll": {"successes": 3, "ones": 0},
                        "host_roll": {"successes": 0}, "decker_net_successes": 3, "tally_increase": 0}
            return {"success": False, "decker_roll": {"successes": 0, "ones": 0},
                    "host_roll": {"successes": 3}, "decker_net_successes": -3, "tally_increase": 0}

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "system_test", _fake_test)

        inp = RunActionInput(action_type="edit_file", subsystem="files", utility_rating=0,
                             hacking_pool_dice=0, target_file=target_file, edit_mode=edit_mode)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.perform_action(run_id=7, body=inp, auth=auth, db=self._FakeDB()))
        return run.state_json

    def _pd(self, state, name="Payroll DB"):
        return next(p for p in state["paydata"] if p["name"] == name)

    def test_modify_marks_file_tampered_not_destroyed(self, monkeypatch):
        out = self._drive(monkeypatch, self._state(), edit_mode="modify")
        pd = self._pd(out)
        assert pd.get("tampered") is True
        assert pd.get("destroyed") in (None, False)        # MODIFY leaves the file in place
        ev = [e for e in out["event_log"] if e["type"] == "file_modified"]
        assert len(ev) == 1 and ev[0]["file_name"] == "Payroll DB"

    def test_erase_marks_file_destroyed(self, monkeypatch):
        out = self._drive(monkeypatch, self._state(), edit_mode="erase")
        pd = self._pd(out)
        assert pd.get("destroyed") is True
        assert pd.get("tampered") in (None, False)         # ERASE never sets the tamper flag
        ev = [e for e in out["event_log"] if e["type"] == "file_deleted"]
        assert len(ev) == 1 and ev[0]["file_name"] == "Payroll DB"

    def test_default_edit_mode_is_erase(self, monkeypatch):
        # A client that omits edit_mode (schema default "erase") keeps the legacy delete behavior.
        out = self._drive(monkeypatch, self._state(), edit_mode="erase")
        assert self._pd(out).get("destroyed") is True

    def test_failed_files_test_changes_nothing(self, monkeypatch):
        out = self._drive(monkeypatch, self._state(), edit_mode="modify", system_success=False)
        pd = self._pd(out)
        assert pd.get("tampered") in (None, False)
        assert pd.get("destroyed") in (None, False)
        assert not [e for e in out["event_log"] if e["type"] in ("file_modified", "file_deleted")]

    def test_tampered_flag_surfaces_in_player_projection(self):
        # The player-facing located_paydata projection carries the tamper flag so the UI can badge it.
        from types import SimpleNamespace
        from datetime import datetime, UTC
        st = self._state()
        st["paydata"][0]["tampered"] = True
        run = SimpleNamespace(id=1, host_id=3, status="active",
                              decker_json=self._decker(), state_json=st,
                              created_at=datetime.now(UTC), updated_at=datetime.now(UTC))
        ser = mr._serialize_run(run, {"is_admin": False, "is_user": True, "user_token": None})
        entry = next(p for p in ser["state_json"]["located_paydata"] if p["name"] == "Payroll DB")
        assert entry["tampered"] is True


class TestAnalyzeGatedICReveal:
    """vr2 #9 + reactive-IC detection (line 409) -- graduated, surreptitious reveal."""

    def _proactive(self, **kw):
        return {"id": "ic_1", "type": "Killer", "rating": 6, "category": "white",
                "status": "active", **kw}

    def _reactive(self, **kw):
        return {"id": "ic_2", "type": "Probe", "rating": 6, "category": "white",
                "status": "active", **kw}

    # -- proactive IC betray themselves (visible, rating still hidden) --
    def test_proactive_ic_visible_as_unknown(self):
        out = mr._redact_ic(self._proactive())
        assert out is not None
        assert out["type"] == "Unknown IC"
        assert out["rating"] is None
        assert out["category"] is None  # threat class withheld until analyzed

    def test_analyzed_ic_fully_revealed(self):
        out = mr._redact_ic(self._proactive(analyzed=True))
        assert out["type"] == "Killer" and out["rating"] == 6

    def test_trap_hidden_still_collapsed(self):
        out = mr._redact_ic(self._proactive(analyzed=True, trap_hidden={"type": "Blaster", "rating": 6}))
        assert out["trap_hidden"] is True

    # -- reactive IC are invisible until detected --
    def test_undetected_reactive_ic_hidden_entirely(self):
        # Probe is reactive; no detection_level -> decker unaware -> dropped from list
        assert mr._redact_ic(self._reactive()) is None

    def test_reactive_level1_shows_presence_only(self):
        out = mr._redact_ic(self._reactive(detection_level=1))
        assert out is not None
        assert out["type"] == "Unknown IC" and out["rating"] is None
        assert out["category"] is None  # threat class withheld below level 2

    def test_reactive_level2_shows_type_not_rating(self):
        out = mr._redact_ic(self._reactive(detection_level=2))
        assert out["type"] == "Probe" and out["rating"] is None
        assert out["category"] == "white"  # type known -> threat class revealed

    def test_reactive_level3_full_reveal(self):
        out = mr._redact_ic(self._reactive(detection_level=3))
        assert out["type"] == "Probe" and out["rating"] == 6

    def test_detection_level_derivation(self):
        assert mr._ic_detection_level(self._reactive()) == 0          # reactive default
        assert mr._ic_detection_level(self._proactive()) == 1         # proactive default
        assert mr._ic_detection_level(self._reactive(analyzed=True)) == 3

    # -- secret Sensor Test raises level + emits graduated notice --
    def test_secret_sensor_test_raises_level_and_notifies(self, scripted):
        # IC rating 4 (TN 4); 6 Sensor dice scripted to exactly 2 successes (no rule-of-6)
        scripted([4, 5, 1, 1, 1, 1])
        state = _fresh_state()
        state["event_log"] = []
        state["condition_monitor"] = {"persona_damage": {}, "mpcp_damage": 0}
        ic = self._reactive(rating=4)
        decker = {"sensor": 6}
        lvl = mr._secret_sensor_test(state, decker, ic)
        assert lvl == 2
        assert ic["detection_level"] == 2
        assert any(e["type"] == "ic_detected" for e in state["event_log"])

    def test_secret_sensor_test_never_lowers(self, scripted):
        scripted([1, 1])  # 0 successes
        state = _fresh_state(); state["event_log"] = []
        state["condition_monitor"] = {"persona_damage": {}, "mpcp_damage": 0}
        ic = self._reactive(detection_level=2)
        lvl = mr._secret_sensor_test(state, {"sensor": 6}, ic)
        assert lvl == 2  # stays at 2, not lowered to 0


class TestLiveDetectionFactor:
    """vr2_rules Detection Factor + Suppression -- DF is recomputed live, not frozen."""

    def _decker(self, masking=6, sleaze=8):
        return {"bod": 6, "evasion": 6, "masking": masking, "sensor": 6, "mpcp": 6,
                "utilities": {"sleaze": sleaze}}

    def test_base_matches_masking_sleaze_average(self):
        state = _fresh_state()
        state["condition_monitor"] = {"persona_damage": {"masking": 0}, "mpcp_damage": 0}
        # M6/S8 -> 7
        assert mr._effective_detection_factor(state, self._decker(6, 8)) == 7

    def test_masking_crippler_lowers_detection_factor(self):
        state = _fresh_state()
        state["condition_monitor"] = {"persona_damage": {"masking": 4}, "mpcp_damage": 0}
        # Masking 6->2, with Sleaze 8 -> ceil((2+8)/2) = 5
        assert mr._effective_detection_factor(state, self._decker(6, 8)) == 5

    def test_suppression_subtracts_one_per_ic(self):
        state = _fresh_state()
        state["condition_monitor"] = {"persona_damage": {"masking": 0}, "mpcp_damage": 0}
        state["active_ic"] = [
            {"status": "active", "suppressed": True},
            {"status": "active", "suppressed": True},
            {"status": "active", "suppressed": False},  # not suppressed -> no DF cost
        ]
        # base 7 - 2 suppressed = 5
        assert mr._effective_detection_factor(state, self._decker(6, 8)) == 5

    def test_crashed_ic_still_costs_df_while_suppressed(self):
        # vr2: a suppressed IC stays crashed but keeps draining DF until released
        state = _fresh_state()
        state["condition_monitor"] = {"persona_damage": {"masking": 0}, "mpcp_damage": 0}
        state["active_ic"] = [
            {"status": "crashed", "suppressed": True},   # crashed + suppressed -> still -1
            {"status": "crashed", "suppressed": False, "suppression_released": True},  # released -> no cost
        ]
        # base 7 - 1 (only the un-released crash) = 6
        assert mr._effective_detection_factor(state, self._decker(6, 8)) == 6

    def test_detection_factor_floored_at_one(self):
        state = _fresh_state()
        state["condition_monitor"] = {"persona_damage": {"masking": 5}, "mpcp_damage": 0}
        state["active_ic"] = [{"status": "active", "suppressed": True} for _ in range(9)]
        assert mr._effective_detection_factor(state, self._decker(6, 0)) == 1

    def test_suppress_then_release_round_trips_df_and_tally(self):
        # suppressing one IC drops DF by 1; the math reflects the flag immediately
        state = _fresh_state()
        state["condition_monitor"] = {"persona_damage": {"masking": 0}, "mpcp_damage": 0}
        ic = {"id": "ic_1", "status": "active", "rating": 6, "suppressed": False}
        state["active_ic"] = [ic]
        base = mr._effective_detection_factor(state, self._decker(6, 8))  # 7
        ic["suppressed"] = True
        assert mr._effective_detection_factor(state, self._decker(6, 8)) == base - 1


class TestSwapMemory:
    """vr2 Swap Memory -- move programs between storage and active memory mid-run."""

    def _state_decker(self, active_cap=100):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6}
        decker = {
            "masking": 4, "intelligence": 5, "mpcp": 6,
            "active_memory": active_cap,
            "utilities": {"read_write": 6, "attack": 5},
            "program_sizes": {"read_write": 30, "attack": 20, "analyze": 18},
            "storage_programs": [{"name": "analyze", "rating": 6, "size": 18}],
        }
        return mr._initial_state(decker, _Host()), decker

    def test_initial_state_seeds_program_memory(self):
        st, _ = self._state_decker(active_cap=60)
        assert st["active_memory_cap"] == 60
        assert st["program_sizes"]["analyze"] == 18
        assert st["storage_programs"] == [{"name": "analyze", "rating": 6, "size": 18}]
        # Program memory is the decker's own deck data -- player-visible, not GM-only.
        assert "storage_programs" not in mr._GM_ONLY_STATE_KEYS

    def test_load_storage_program_into_active(self):
        st, decker = self._state_decker(active_cap=100)
        changed, desc = mr._apply_swap_memory(
            st, decker, target_program="analyze", swap_out_program="")
        assert changed is True
        assert decker["utilities"]["analyze"] == 6   # now active
        assert st["storage_programs"] == []          # left storage
        assert "loaded Analyze" in desc

    def test_load_overflow_requires_swap_out(self):
        # cap 50: read_write 30 + attack 20 = 50 used; loading analyze (18) overflows.
        st, decker = self._state_decker(active_cap=50)
        with pytest.raises(mr.HTTPException) as exc:
            mr._apply_swap_memory(st, decker, target_program="analyze", swap_out_program="")
        assert exc.value.status_code == 400
        assert decker["utilities"].get("analyze", 0) == 0   # not loaded
        assert st["storage_programs"][0]["name"] == "analyze"

    def test_load_with_swap_out_frees_room(self):
        st, decker = self._state_decker(active_cap=50)
        changed, _ = mr._apply_swap_memory(
            st, decker, target_program="analyze", swap_out_program="attack")
        assert changed is True
        assert decker["utilities"]["analyze"] == 6
        assert decker["utilities"]["attack"] == 0           # pushed to storage
        names = {p["name"] for p in st["storage_programs"]}
        assert "attack" in names and "analyze" not in names

    def test_unload_active_to_storage(self):
        st, decker = self._state_decker(active_cap=100)
        changed, _ = mr._apply_swap_memory(
            st, decker, target_program="", swap_out_program="read_write")
        assert changed is True
        assert decker["utilities"]["read_write"] == 0
        assert any(p["name"] == "read_write" for p in st["storage_programs"])

    def test_reload_damaged_active_program(self):
        st, decker = self._state_decker(active_cap=100)
        st["program_damage"] = {"attack": 5}                # crashed by Hog
        changed, desc = mr._apply_swap_memory(
            st, decker, target_program="attack", swap_out_program="")
        assert changed is False                             # decker utilities unchanged
        assert st["program_damage"]["attack"] == 0          # rating restored
        assert "reloaded Attack" in desc

    def test_swap_in_grows_icon_bandwidth(self):
        # Loading a stored program into active memory enlarges the live Icon Bandwidth (vr2):
        # its rating now counts toward the active-memory footprint.
        st, decker = self._state_decker(active_cap=100)
        before = mr._live_icon_bandwidth(decker, st)
        mr._apply_swap_memory(st, decker, target_program="analyze", swap_out_program="")
        assert mr._live_icon_bandwidth(decker, st) == before + 6

    def test_swap_action_cost_is_simple(self):
        assert mr._ACTION_COST["swap_memory"] == "Simple"


class TestRouteRegistration:
    """Guard against run-engine handlers losing their @router decorator.

    Regression: the POST /{run_id}/new-turn handler was once left without its
    @router.post(...) decorator, so the route never registered -- the client's
    "New Turn" button (and any new-turn call) returned 404 while the function sat
    dead in the module. import app.main still succeeded and no test exercised the
    HTTP route, so the gap went unnoticed. These checks fail fast if it recurs.
    """

    def _paths(self):
        return {getattr(r, "path", None) for r in mr.router.routes}

    def test_new_turn_route_is_registered(self):
        assert "/{run_id}/new-turn" in self._paths()

    def test_core_run_routes_registered(self):
        paths = self._paths()
        for p in ("/{run_id}/action", "/{run_id}/attack", "/{run_id}/logoff",
                  "/{run_id}/jack-out", "/{run_id}/new-turn", "/{run_id}/trap-door/{td_id}"):
            assert p in paths, f"run-engine route not registered: {p}"


class TestShieldDefenseRunLayer:
    """vr2 Shield on DEFENSE -- the run engine applies the decker's Shield against incoming
    persona attacks, degrades it 1 Rating Point per use, stops parrying once worn out, and
    treats a Swap Memory reload (which clears program_damage['shield']) as a fresh copy."""

    def _decker(self, shield=4):
        return {"utilities": {"shield": shield, "armor": 0}, "computer_skill": 5,
                "bod": 4, "evasion": 4, "masking": 4, "sensor": 4, "mpcp": 4}

    def _state(self):
        s = _fresh_state()
        s["event_log"] = []
        return s

    def test_effective_shield_subtracts_wear_and_floors_at_zero(self):
        decker = self._decker(shield=4)
        state = self._state()
        assert mr._effective_shield(decker, state) == 4
        state["program_damage"] = {"shield": 1}
        assert mr._effective_shield(decker, state) == 3
        state["program_damage"] = {"shield": 9}        # cannot go negative
        assert mr._effective_shield(decker, state) == 0

    def test_no_shield_loaded_is_zero(self):
        decker = {"utilities": {"armor": 4}, "computer_skill": 5}
        assert mr._effective_shield(decker, self._state()) == 0

    def test_shield_parry_degrades_one_per_use_and_emits_event(self, scripted):
        scripted([6, 6, 1, 1])             # Shield-4 vs TN 5 -> 6,6 hit -> 2 successes
        decker = self._decker(shield=4)
        state = self._state()
        succ = mr._shield_parry(state, decker, attacker_skill=5, context="Killer")
        assert succ == 2
        assert state["program_damage"]["shield"] == 1          # -1 Rating Point per use
        assert mr._effective_shield(decker, state) == 3
        ev = state["event_log"][-1]
        assert ev["type"] == "shield_parry"
        assert ev["successes"] == 2
        assert ev["shield_remaining"] == 3
        assert ev["context"] == "Killer"

    def test_shield_wears_out_then_stops_parrying(self, scripted):
        scripted([6])                      # Shield-1 -> 1 die, hits
        decker = self._decker(shield=1)
        state = self._state()
        first = mr._shield_parry(state, decker, attacker_skill=4, context="Killer")
        assert first == 1
        assert state["program_damage"]["shield"] == 1
        assert mr._effective_shield(decker, state) == 0
        events_after_first = len(state["event_log"])
        # Second use: worn out -> no test, no further wear, no event, returns 0
        second = mr._shield_parry(state, decker, attacker_skill=4, context="Killer")
        assert second == 0
        assert state["program_damage"]["shield"] == 1          # unchanged
        assert len(state["event_log"]) == events_after_first   # no new event emitted

    def test_swap_memory_reload_restores_a_fresh_shield(self, scripted):
        scripted([6, 6, 6])
        decker = self._decker(shield=3)
        state = self._state()
        mr._shield_parry(state, decker, attacker_skill=4, context="Killer")
        assert mr._effective_shield(decker, state) == 2
        # Swap Memory Mode-3 reloads a fresh copy: it clears the shield's program_damage slot.
        changed, desc = mr._apply_swap_memory(
            state, decker, target_program="shield", swap_out_program="")
        assert state["program_damage"]["shield"] == 0
        assert mr._effective_shield(decker, state) == 3        # back to full rating
        assert "reloaded Shield" in desc


class TestArmorWear:
    """vr2 Armor: "loses 1 Rating Point every time the decker takes damage." The run engine reads
    the EFFECTIVE (worn) Armor rating when resisting persona hits, degrades it 1 point per LANDED
    hit (PC via state['program_damage']['armor'], enemy via enemy['program_damage']['armor']),
    never wears past 0, and a Swap Memory reload restores a fresh copy. PC and enemy deckers use
    the SAME wear mechanic (parity), mirroring Shield/Medic wear."""

    def _decker(self, armor=4):
        return {"utilities": {"armor": armor, "shield": 0}, "computer_skill": 5,
                "bod": 4, "evasion": 4, "masking": 4, "sensor": 4, "mpcp": 4}

    def _state(self):
        s = _fresh_state()
        s["event_log"] = []
        s.pop("program_damage", None)
        return s

    def test_effective_armor_subtracts_wear_and_floors_at_zero(self):
        decker = self._decker(armor=4)
        state = self._state()
        assert mr._effective_armor(decker, state) == 4
        state["program_damage"] = {"armor": 1}
        assert mr._effective_armor(decker, state) == 3
        state["program_damage"] = {"armor": 9}          # cannot go negative
        assert mr._effective_armor(decker, state) == 0

    def test_no_armor_loaded_is_zero(self):
        decker = {"utilities": {"shield": 4}, "computer_skill": 5}
        assert mr._effective_armor(decker, self._state()) == 0

    def test_enemy_armor_helper_subtracts_wear_and_floors_at_zero(self):
        # Parity: the enemy helper degrades from the enemy's OWN program_damage slot.
        enemy = {"utilities": {"armor": 5}}
        assert mr._enemy_armor(enemy) == 5
        enemy["program_damage"] = {"armor": 2}
        assert mr._enemy_armor(enemy) == 3
        enemy["program_damage"] = {"armor": 12}          # cannot go negative
        assert mr._enemy_armor(enemy) == 0

    def test_pc_armor_degrades_one_per_landed_hit_and_emits_player_event(self):
        decker = self._decker(armor=4)
        state = self._state()
        mr._wear_armor(state, state, decker, boxes=3)    # a hit landed 3 boxes
        assert state["program_damage"]["armor"] == 1     # -1 Rating Point
        assert mr._effective_armor(decker, state) == 3
        ev = state["event_log"][-1]
        assert ev["type"] == "armor_wear"
        assert ev.get("gm_only") is None                 # player-visible for the PC
        assert ev["armor_remaining"] == 3

    def test_no_wear_when_no_boxes_land(self):
        decker = self._decker(armor=4)
        state = self._state()
        mr._wear_armor(state, state, decker, boxes=0)     # fully resisted -> no damage taken
        assert state.get("program_damage", {}).get("armor", 0) == 0
        assert not state["event_log"]                     # no event

    def test_no_wear_when_no_armor_loaded(self):
        decker = self._decker(armor=0)
        state = self._state()
        mr._wear_armor(state, state, decker, boxes=5)
        assert state.get("program_damage", {}).get("armor", 0) == 0
        assert not state["event_log"]

    def test_armor_wears_out_then_stops_with_burnout_event(self):
        decker = self._decker(armor=1)
        state = self._state()
        mr._wear_armor(state, state, decker, boxes=2)     # wears the 1-rating armor to 0
        assert state["program_damage"]["armor"] == 1
        assert mr._effective_armor(decker, state) == 0
        assert state["event_log"][-1]["armor_remaining"] == 0
        events_after = len(state["event_log"])
        mr._wear_armor(state, state, decker, boxes=2)     # already worn out -> no-op
        assert state["program_damage"]["armor"] == 1      # unchanged
        assert len(state["event_log"]) == events_after    # no new event

    def test_enemy_armor_wears_on_its_own_slot_with_gm_only_event(self):
        state = self._state()
        enemy = {"id": "e1", "name": "Shade", "utilities": {"armor": 3}}
        mr._wear_armor(state, enemy, enemy, boxes=4, gm_only=True, actor=enemy["name"])
        assert enemy["program_damage"]["armor"] == 1
        assert mr._enemy_armor(enemy) == 2
        assert "program_damage" not in state              # enemy wear does NOT touch PC state slot
        ev = state["event_log"][-1]
        assert ev["type"] == "armor_wear"
        assert ev["gm_only"] is True                      # hidden from the player (redacted)
        assert ev["armor_remaining"] == 2

    def test_swap_memory_reload_restores_a_fresh_armor(self):
        decker = self._decker(armor=3)
        state = self._state()
        mr._wear_armor(state, state, decker, boxes=2)
        assert mr._effective_armor(decker, state) == 2
        # Swap Memory Mode-3 reloads a fresh copy: it clears the armor's program_damage slot.
        changed, desc = mr._apply_swap_memory(
            state, decker, target_program="armor", swap_out_program="")
        assert state["program_damage"]["armor"] == 0
        assert mr._effective_armor(decker, state) == 3    # back to full rating


class TestMedicRunLayer:
    """vr2 Medic on the run engine: the /action 'medic' path heals persona/icon Condition Monitor
    boxes (1 per Medic Test success, TN by current wound level), degrades the Medic 1 Rating Point
    per use regardless of outcome, stops healing once worn out / not loaded, caps the heal at the
    current damage, and treats a Swap Memory reload (which clears program_damage['medic']) as a
    fresh copy. _apply_medic is exactly what the /action medic handler invokes before the generic
    subsystem test, so it never logs a bogus system_test result."""

    def _decker(self, medic=4):
        return {"utilities": {"medic": medic}, "computer_skill": 5,
                "bod": 4, "evasion": 4, "masking": 4, "sensor": 4, "mpcp": 4}

    def _state(self, persona_boxes=0):
        s = _fresh_state()
        s["event_log"] = []
        s["condition_monitor"] = {
            "persona_boxes": persona_boxes, "mpcp_damage": 0, "physical_boxes": 0,
            "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
        }
        return s

    def test_medic_action_is_complex_and_validates(self):
        from app.schemas.matrix_run import RunActionInput
        assert mr._ACTION_COST.get("medic") == "Complex"
        inp = RunActionInput(action_type="medic", subsystem="control")
        assert inp.action_type == "medic"

    def test_effective_medic_subtracts_wear_and_floors_at_zero(self):
        decker = self._decker(medic=4)
        state = self._state()
        assert mr._effective_medic(decker, state) == 4
        state["program_damage"] = {"medic": 1}
        assert mr._effective_medic(decker, state) == 3
        state["program_damage"] = {"medic": 9}        # cannot go negative
        assert mr._effective_medic(decker, state) == 0

    def test_no_medic_loaded_is_zero(self):
        decker = {"utilities": {"armor": 4}, "computer_skill": 5}
        assert mr._effective_medic(decker, self._state()) == 0

    def test_current_wound_level_by_filled_boxes(self):
        # vr2 Condition Monitor Table floors: Light >=1, Moderate >=3, Serious >=6 boxes. The
        # Deadly box-range (up to the 10-box crash) still reports Serious for Medic TN purposes.
        assert mr._current_icon_wound_level(self._state(persona_boxes=0)) is None
        assert mr._current_icon_wound_level(self._state(persona_boxes=1)) == "Light"
        assert mr._current_icon_wound_level(self._state(persona_boxes=2)) == "Light"
        assert mr._current_icon_wound_level(self._state(persona_boxes=3)) == "Moderate"
        assert mr._current_icon_wound_level(self._state(persona_boxes=5)) == "Moderate"
        assert mr._current_icon_wound_level(self._state(persona_boxes=6)) == "Serious"
        assert mr._current_icon_wound_level(self._state(persona_boxes=9)) == "Serious"

    def test_medic_reduces_persona_damage_and_emits_event(self, scripted):
        # 3 boxes filled -> Moderate -> TN 5. Medic-4 rolls [6,6,6,1] -> 3 successes -> 3 healed.
        scripted([6, 6, 6, 1])
        decker = self._decker(medic=4)
        state = self._state(persona_boxes=3)
        mr._apply_medic(state, decker)
        assert state["condition_monitor"]["persona_boxes"] == 0     # 3 - 3 healed
        assert state["program_damage"]["medic"] == 1               # -1 Rating Point per use
        assert mr._effective_medic(decker, state) == 3
        ev = state["event_log"][-1]
        assert ev["type"] == "medic_heal"
        assert ev["wound_level"] == "Moderate"
        assert ev["healed"] == 3
        assert ev["persona_boxes"] == 0
        assert ev["medic_remaining"] == 3

    def test_medic_heal_capped_by_current_damage(self, scripted):
        # 1 box filled -> Light -> TN 4. Medic-3 rolls 3 successes but only 1 box of damage exists.
        scripted([4, 4, 4])
        decker = self._decker(medic=3)
        state = self._state(persona_boxes=1)
        mr._apply_medic(state, decker)
        assert state["condition_monitor"]["persona_boxes"] == 0     # capped at the 1 box
        assert state["program_damage"]["medic"] == 1
        ev = state["event_log"][-1]
        assert ev["wound_level"] == "Light"
        assert ev["healed"] == 1                                   # not 3

    def test_medic_degrades_even_on_a_failed_heal(self, scripted):
        # Moderate wound (3 boxes -> TN 5); Medic-2 rolls [4,4] -> 0 successes -> 0 healed, but still wears.
        scripted([4, 4])
        decker = self._decker(medic=2)
        state = self._state(persona_boxes=3)
        mr._apply_medic(state, decker)
        assert state["condition_monitor"]["persona_boxes"] == 3     # nothing healed
        assert state["program_damage"]["medic"] == 1               # -1 Rating Point regardless
        ev = state["event_log"][-1]
        assert ev["wound_level"] == "Moderate"
        assert ev["healed"] == 0

    def test_undamaged_icon_is_a_noop(self, scripted):
        scripted([6, 6, 6, 6])             # dice must NOT be consumed -- no heal happens
        decker = self._decker(medic=4)
        state = self._state(persona_boxes=0)
        mr._apply_medic(state, decker)
        assert state["condition_monitor"]["persona_boxes"] == 0
        assert state.get("program_damage", {}).get("medic", 0) == 0  # no degrade on a no-op
        ev = state["event_log"][-1]
        assert ev["type"] == "medic_heal"
        assert ev["healed"] == 0
        assert "undamaged" in ev["description"]

    def test_worn_out_medic_heals_nothing_and_does_not_degrade_further(self, scripted):
        scripted([6, 6, 6, 6])             # would-be successes -- must NOT be rolled
        decker = self._decker(medic=2)
        state = self._state(persona_boxes=4)            # Moderate damage remains
        state["program_damage"] = {"medic": 2}          # already worn to effective 0
        assert mr._effective_medic(decker, state) == 0
        mr._apply_medic(state, decker)
        assert state["condition_monitor"]["persona_boxes"] == 4   # unchanged -- no heal
        assert state["program_damage"]["medic"] == 2             # no further wear
        ev = state["event_log"][-1]
        assert ev["type"] == "medic_heal"
        assert ev["healed"] == 0
        assert "offline" in ev["description"].lower()

    def test_swap_memory_reload_restores_a_fresh_medic(self, scripted):
        scripted([4, 4, 4])
        decker = self._decker(medic=3)
        state = self._state(persona_boxes=1)
        mr._apply_medic(state, decker)
        assert state["program_damage"]["medic"] == 1
        assert mr._effective_medic(decker, state) == 2
        # Swap Memory Mode-3 reloads a fresh copy: it clears the medic's program_damage slot.
        changed, desc = mr._apply_swap_memory(
            state, decker, target_program="medic", swap_out_program="")
        assert state["program_damage"]["medic"] == 0
        assert mr._effective_medic(decker, state) == 3           # back to full rating
        assert "reloaded Medic" in desc


class TestRestoreRunLayer:
    """vr2 Restore on the run engine: the /action 'restore' path repairs the TEMPORARY crippler
    reductions to the icon's persona attributes (Bod/Evasion/Masking/Sensor). Restore Test TN =
    the highest rating of the crippler program(s) that caused the targeted attribute's current
    damage; every 2 successes repairs 1 point, capped by the repairable damage. Unlike Medic,
    Restore does NOT degrade per use, and it CANNOT touch permanent Persona-chip damage (Rippers).
    _apply_restore is exactly what the /action restore handler invokes before the generic subsystem
    test, so it never logs a bogus system_test result."""

    def _decker(self, restore=4):
        return {"utilities": {"restore": restore}, "computer_skill": 5,
                "bod": 6, "evasion": 6, "masking": 6, "sensor": 6, "mpcp": 4}

    def _state(self, persona_damage=None, chip=None, ratings=None):
        s = _fresh_state()
        s["event_log"] = []
        s["condition_monitor"] = {
            "persona_boxes": 0, "mpcp_damage": 0, "physical_boxes": 0,
            "persona_damage": persona_damage or {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
            "persona_chip_damage": chip or {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
            "crippler_rating": ratings or {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
        }
        return s

    def test_restore_action_is_complex_and_validates(self):
        from app.schemas.matrix_run import RunActionInput
        assert mr._ACTION_COST.get("restore") == "Complex"
        inp = RunActionInput(action_type="restore", subsystem="control")
        assert inp.action_type == "restore"

    def test_effective_restore_subtracts_crash_wear_and_floors_at_zero(self):
        decker = self._decker(restore=4)
        state = self._state()
        assert mr._effective_restore(decker, state) == 4
        state["program_damage"] = {"restore": 1}      # e.g. Tar Baby / Hog crash
        assert mr._effective_restore(decker, state) == 3
        state["program_damage"] = {"restore": 9}       # cannot go negative
        assert mr._effective_restore(decker, state) == 0

    def test_no_restore_loaded_is_zero(self):
        decker = {"utilities": {"armor": 4}, "computer_skill": 5}
        assert mr._effective_restore(decker, self._state()) == 0

    def test_record_crippler_rating_keeps_the_highest(self):
        state = self._state(persona_damage={"bod": 4, "evasion": 0, "masking": 0, "sensor": 0})
        mr._record_crippler_rating(state, "bod", 4)
        mr._record_crippler_rating(state, "bod", 7)    # higher -> wins
        mr._record_crippler_rating(state, "bod", 5)    # lower -> ignored
        assert state["condition_monitor"]["crippler_rating"]["bod"] == 7

    def test_restore_repairs_most_damaged_attribute_and_emits_event(self, scripted):
        # Default target = the most-damaged repairable attribute (Masking, 3). It was crippled by a
        # rating-5 program -> Restore Test TN 5. Restore-6 rolls [5,5,5,5,1,1] -> 4 successes -> 2
        # points repaired. Bod (less damaged) is left alone.
        scripted([5, 5, 5, 5, 1, 1])
        decker = self._decker(restore=6)
        state = self._state(
            persona_damage={"bod": 1, "evasion": 0, "masking": 3, "sensor": 0},
            ratings={"bod": 4, "evasion": 0, "masking": 5, "sensor": 0})
        mr._apply_restore(state, decker)
        pd = state["condition_monitor"]["persona_damage"]
        assert pd["masking"] == 1            # 3 - 2 repaired
        assert pd["bod"] == 1                # untouched
        assert state.get("program_damage", {}).get("restore", 0) == 0   # NO degradation
        ev = state["event_log"][-1]
        assert ev["type"] == "restore_repair"
        assert ev["attribute"] == "masking"
        assert ev["causing_rating"] == 5
        assert ev["decker_roll"]["tn"] == 5
        assert ev["repaired"] == 2
        assert ev["attribute_damage"] == 1

    def test_restore_uses_the_highest_causing_rating_for_tn(self, scripted):
        # Two programs hit Bod (ratings 4 and 7) -> TN = 7 (the highest), per the rule.
        scripted([6, 5, 4, 1])             # cycled; only the TN/causing_rating is asserted
        state = self._state(persona_damage={"bod": 4, "evasion": 0, "masking": 0, "sensor": 0})
        mr._record_crippler_rating(state, "bod", 4)
        mr._record_crippler_rating(state, "bod", 7)
        decker = self._decker(restore=4)
        mr._apply_restore(state, decker, target="bod")
        ev = state["event_log"][-1]
        assert ev["causing_rating"] == 7
        assert ev["decker_roll"]["tn"] == 7

    def test_restore_capped_by_repairable_damage_and_clears_causing_rating(self, scripted):
        # Bod has 1 temp damage; Restore rolls 6 successes (3 points) but caps at the 1 present.
        scripted([4, 4, 4, 4, 4, 4])
        decker = self._decker(restore=6)
        state = self._state(
            persona_damage={"bod": 1, "evasion": 0, "masking": 0, "sensor": 0},
            ratings={"bod": 4, "evasion": 0, "masking": 0, "sensor": 0})
        mr._apply_restore(state, decker, target="bod")
        assert state["condition_monitor"]["persona_damage"]["bod"] == 0
        ev = state["event_log"][-1]
        assert ev["repaired"] == 1
        # Fully repaired -> the causing rating is no longer relevant.
        assert state["condition_monitor"]["crippler_rating"]["bod"] == 0

    def test_restore_does_not_degrade_on_repeated_use(self, scripted):
        # The KEY difference from Medic: Restore keeps its full rating no matter how often it runs.
        scripted([4, 4, 4, 4, 4, 4])
        decker = self._decker(restore=6)
        state = self._state(
            persona_damage={"bod": 6, "evasion": 0, "masking": 0, "sensor": 0},
            ratings={"bod": 4, "evasion": 0, "masking": 0, "sensor": 0})
        mr._apply_restore(state, decker, target="bod")          # 6 successes -> 3 points
        assert state["condition_monitor"]["persona_damage"]["bod"] == 3
        assert state.get("program_damage", {}).get("restore", 0) == 0   # no wear
        assert mr._effective_restore(decker, state) == 6                 # full rating retained
        mr._apply_restore(state, decker, target="bod")          # again -> 3 more
        assert state["condition_monitor"]["persona_damage"]["bod"] == 0
        assert state.get("program_damage", {}).get("restore", 0) == 0   # still no wear
        assert mr._effective_restore(decker, state) == 6

    def test_restore_cannot_repair_permanent_chip_damage(self, scripted):
        # All 4 points of Bod damage are permanent Ripper chip -> nothing is repairable.
        scripted([6, 6, 6, 6])             # dice must NOT be consumed for a repair
        decker = self._decker(restore=6)
        state = self._state(
            persona_damage={"bod": 4, "evasion": 0, "masking": 0, "sensor": 0},
            chip={"bod": 4, "evasion": 0, "masking": 0, "sensor": 0},
            ratings={"bod": 6, "evasion": 0, "masking": 0, "sensor": 0})
        mr._apply_restore(state, decker, target="bod")
        assert state["condition_monitor"]["persona_damage"]["bod"] == 4   # permanent, untouched
        ev = state["event_log"][-1]
        assert ev["repaired"] == 0
        assert "permanent" in ev["description"].lower()

    def test_restore_stops_at_the_permanent_chip_floor(self, scripted):
        # Bod = 2 permanent chip + 3 temporary. Restore repairs the 3 temp and stops at 2.
        scripted([4, 4, 4, 4, 4, 4])       # Restore-6 vs TN 4 -> 6 successes -> 3 points
        decker = self._decker(restore=6)
        state = self._state(
            persona_damage={"bod": 5, "evasion": 0, "masking": 0, "sensor": 0},
            chip={"bod": 2, "evasion": 0, "masking": 0, "sensor": 0},
            ratings={"bod": 4, "evasion": 0, "masking": 0, "sensor": 0})
        mr._apply_restore(state, decker, target="bod")
        assert state["condition_monitor"]["persona_damage"]["bod"] == 2   # floored at the chip
        ev = state["event_log"][-1]
        assert ev["repaired"] == 3
        assert ev["attribute_damage"] == 2

    def test_undamaged_icon_is_a_noop(self, scripted):
        scripted([6, 6, 6, 6])             # must NOT be rolled
        decker = self._decker(restore=4)
        state = self._state()              # all attributes at 0
        mr._apply_restore(state, decker)
        assert state["condition_monitor"]["persona_damage"] == {
            "bod": 0, "evasion": 0, "masking": 0, "sensor": 0}
        assert state.get("program_damage", {}).get("restore", 0) == 0
        ev = state["event_log"][-1]
        assert ev["type"] == "restore_repair"
        assert ev["repaired"] == 0
        assert "no temporary" in ev["description"].lower()

    def test_offline_restore_repairs_nothing(self, scripted):
        scripted([6, 6, 6, 6])             # would-be successes -- must NOT be rolled
        decker = self._decker(restore=4)
        state = self._state(
            persona_damage={"bod": 3, "evasion": 0, "masking": 0, "sensor": 0},
            ratings={"bod": 4, "evasion": 0, "masking": 0, "sensor": 0})
        state["program_damage"] = {"restore": 4}        # crashed to effective 0
        assert mr._effective_restore(decker, state) == 0
        mr._apply_restore(state, decker, target="bod")
        assert state["condition_monitor"]["persona_damage"]["bod"] == 3   # unchanged
        ev = state["event_log"][-1]
        assert ev["repaired"] == 0
        assert "offline" in ev["description"].lower()

    def test_explicit_target_overrides_the_most_damaged_default(self, scripted):
        # Masking is the most-damaged, but the player explicitly targets Sensor.
        scripted([4, 4, 4, 4, 4, 4])
        decker = self._decker(restore=6)
        state = self._state(
            persona_damage={"bod": 0, "evasion": 0, "masking": 4, "sensor": 2},
            ratings={"bod": 0, "evasion": 0, "masking": 3, "sensor": 4})
        mr._apply_restore(state, decker, target="sensor")
        pd = state["condition_monitor"]["persona_damage"]
        assert pd["sensor"] == 0            # 2 repaired (capped at the 2 present)
        assert pd["masking"] == 4           # the most-damaged attr is left untouched
        ev = state["event_log"][-1]
        assert ev["attribute"] == "sensor"
        assert ev["causing_rating"] == 4    # sensor's causing rating, not masking's


class TestDisinfect:
    """vr2 Disinfect: the carried Disinfect utility defends against worm infection automatically
    (raises the Worm Infection Test TN), and the active Disinfect operation (Complex) makes a
    System Test against the worm's host subsystem to DESTROY the worm -- no security-tally cost
    (it is a Disinfect, not a cybercombat crash) -- with a failed sweep risking the MPCP infection.
    _apply_disinfect is exactly what the /action 'disinfect' handler invokes before the generic
    subsystem test, so it never logs a bogus system_test result."""

    def _decker(self, disinfect=6, mpcp=4, hardening=0):
        return {"utilities": {"disinfect": disinfect}, "computer_skill": 6, "mpcp": mpcp,
                "hardening": hardening, "bod": 4, "evasion": 4, "masking": 4, "sensor": 4}

    def _state_with_worm(self, rating=5, worm_id="lc_worm1", tally=7):
        s = _fresh_state()
        s["event_log"] = []
        s["security_tally"] = tally
        s["lurking_ic"] = [{"id": worm_id, "type": "Worm", "rating": rating, "status": "lurking"}]
        return s

    # -- schema / wiring -------------------------------------------------------

    def test_schema_accepts_disinfect_utility_and_action(self):
        from app.schemas.matrix_run import DeckerUtilities, RunActionInput
        assert DeckerUtilities().disinfect == 0                 # default
        assert DeckerUtilities(disinfect=4).disinfect == 4
        inp = RunActionInput(action_type="disinfect", subsystem="files")
        assert inp.action_type == "disinfect"
        assert mr._ACTION_COST.get("disinfect") == "Complex"    # Disinfect is a Complex Action

    def test_effective_disinfect_reads_carried_and_subtracts_wear(self):
        decker = self._decker(disinfect=5)
        state = _fresh_state()
        assert mr._effective_disinfect(decker, state) == 5
        state["program_damage"] = {"disinfect": 2}              # e.g. Tar Baby / Hog crash
        assert mr._effective_disinfect(decker, state) == 3
        state["program_damage"] = {"disinfect": 9}              # cannot go negative
        assert mr._effective_disinfect(decker, state) == 0
        # Not loaded -> 0 (decker carries no anti-worm defense).
        assert mr._effective_disinfect({"utilities": {"armor": 4}}, _fresh_state()) == 0

    # -- deck Hardening = passive infection defense ----------------------------

    def test_worm_defense_uses_carried_disinfect(self, scripted):
        # The SAME Worm roll infects a bare deck (net > 0) but is repelled when the deck has
        # Hardening-4 subtracted from the worm's successes (net drops to 0).
        scripted([4, 4, 4, 4])
        bare = eng.worm_attack(security_value=4, mpcp_rating=4)
        assert bare["tn"] == 4 and bare["mpcp_infected"] is True
        scripted([4, 4, 4, 4])
        guarded = eng.worm_attack(security_value=4, mpcp_rating=4, hardening=4)
        assert guarded["tn"] == 4 and guarded["net_successes"] == 0 and guarded["mpcp_infected"] is False

    # -- active Disinfect operation -------------------------------------------

    def test_disinfect_test_tn_reduced_by_utility_and_floored(self, scripted):
        scripted([6])
        r = eng.disinfect_test(decker_pool=8, subsystem_rating=9, disinfect_utility=4)
        assert r["tn"] == 5                                     # 9 - 4
        assert r["worm_destroyed"] is True                     # all 6s vs TN 5
        scripted([1])
        r2 = eng.disinfect_test(decker_pool=4, subsystem_rating=3, disinfect_utility=9)
        assert r2["tn"] == 2                                    # floored at 2
        assert r2["worm_destroyed"] is False

    def test_disinfect_destroys_worm_on_success_no_tally_add(self, scripted):
        # System Test vs files-8 reduced by Disinfect-6 -> TN 2; pool rolls 6 successes.
        scripted([4, 4, 4, 4, 4, 4])
        decker = self._decker(disinfect=6)
        state = self._state_with_worm(rating=5, tally=7)
        mr._apply_disinfect(state, decker, subsystem="files", subsystem_rating=8,
                            decker_pool=6, target_ic_id="")
        assert state["lurking_ic"] == []                       # worm destroyed + removed
        assert state["security_tally"] == 7                    # NO tally add (not a crash)
        assert not state.get("mpcp_infected")
        ev = state["event_log"][-1]
        assert ev["type"] == "worm_disinfected"
        assert ev["destroyed"] is True
        assert ev["ic_type"] == "Worm"

    def test_disinfect_targets_named_worm(self, scripted):
        scripted([4, 4, 4, 4, 4, 4])
        decker = self._decker(disinfect=6)
        state = _fresh_state(); state["event_log"] = []
        state["lurking_ic"] = [
            {"id": "lc_a", "type": "Worm", "rating": 4, "status": "lurking"},
            {"id": "lc_b", "type": "Worm", "rating": 5, "status": "lurking"},
        ]
        mr._apply_disinfect(state, decker, subsystem="files", subsystem_rating=8,
                            decker_pool=6, target_ic_id="lc_b")
        assert [ic["id"] for ic in state["lurking_ic"]] == ["lc_a"]   # only the named worm removed
        ev = state["event_log"][-1]
        assert ev["ic_id"] == "lc_b" and ev["destroyed"] is True

    def test_failed_disinfect_can_infect_mpcp(self, scripted):
        # Disinfect fails (TN 5, rolls 1s) -> Worm Infection Test (TN 4+1=5, rolls 6s) infects.
        scripted([1, 1, 6, 6])
        decker = self._decker(disinfect=1, mpcp=4)
        state = self._state_with_worm(rating=2, worm_id="lc_w")
        mr._apply_disinfect(state, decker, subsystem="files", subsystem_rating=6,
                            decker_pool=2, target_ic_id="")
        assert state.get("mpcp_infected") is True
        assert state.get("chip_replacement_required") is True
        assert state["lurking_ic"] == []                       # infected worm removed
        ev = state["event_log"][-1]
        assert ev["type"] == "worm_resolved"
        assert ev["outcome"] == "mpcp_infected"

    def test_failed_disinfect_without_infection_leaves_worm_lurking(self, scripted):
        # Disinfect fails (TN 2) but carried Disinfect-6 holds off the infection (TN 10) -> worm survives.
        scripted([1, 1, 1, 1])
        decker = self._decker(disinfect=6, mpcp=4)
        state = self._state_with_worm(rating=2, worm_id="lc_w", tally=7)
        mr._apply_disinfect(state, decker, subsystem="files", subsystem_rating=8,
                            decker_pool=2, target_ic_id="")
        assert not state.get("mpcp_infected")
        assert len(state["lurking_ic"]) == 1                   # worm survived, still lurking
        assert state["security_tally"] == 7                    # no tally add either way
        ev = state["event_log"][-1]
        assert ev["type"] == "worm_disinfected"
        assert ev["destroyed"] is False

    def test_disinfect_no_worm_reports_clean(self, scripted):
        scripted([6, 6, 6, 6])             # dice must NOT be consumed -- no worm to test
        decker = self._decker(disinfect=6)
        state = _fresh_state(); state["event_log"] = []; state["security_tally"] = 3
        mr._apply_disinfect(state, decker, subsystem="files", subsystem_rating=8,
                            decker_pool=6, target_ic_id="")
        ev = state["event_log"][-1]
        assert ev["type"] == "worm_disinfected"
        assert ev["destroyed"] is False
        assert "clean" in ev["description"].lower()
        assert state["security_tally"] == 3

    def test_offline_disinfect_does_nothing(self, scripted):
        scripted([6, 6, 6, 6])             # would-be successes -- must NOT be rolled
        decker = {"utilities": {"armor": 4}, "computer_skill": 6, "mpcp": 4, "hardening": 0}
        state = self._state_with_worm(rating=5)
        mr._apply_disinfect(state, decker, subsystem="files", subsystem_rating=8,
                            decker_pool=6, target_ic_id="")
        assert len(state["lurking_ic"]) == 1                   # worm untouched (no Disinfect loaded)
        ev = state["event_log"][-1]
        assert ev["type"] == "worm_disinfected"
        assert "offline" in ev["description"].lower()


class TestSteamroller:
    """vr2_rules.md L1581-1585 -- Steamroller is the dedicated anti-tar weapon. The active
    Steamroller operation (Complex) inflicts (Rating)D on a Tar Baby / Tar Pit lurking-IC and is
    IMMUNE to the tar crash-backlash: unlike every other utility that touches a tar IC, it NEVER
    runs the opposed tar crash test, so the decker's loaded utilities are never crashed or
    corrupted (a Tar Pit's "corrupt all copies" path can therefore never fire). Crashing the tar
    adds its rating to the security tally UNLESS the Steamroller carries the Stealth/Skulk option
    (which reduces the bump, mirroring the Attack-utility skulk rule) or the tar is suppressed
    (no tally at all). Steamroller targets ONLY tar IC -- a non-tar target is rejected.

    _apply_steamroller is exactly what the /action 'steamroller' handler invokes before the
    generic subsystem test, so it is unit-tested directly (mirrors TestDisinfect)."""

    def _decker(self, steamroller=6, **opts):
        d = {"utilities": {"steamroller": steamroller, "attack": 5, "analyze": 4},
             "computer_skill": 6, "mpcp": 4, "hardening": 0,
             "bod": 4, "evasion": 4, "masking": 4, "sensor": 4}
        if opts:
            d["program_options"] = {"steamroller": dict(opts)}
        return d

    def _state_with_tar(self, rating=6, tar_id="lc_tar1", tar_type="Tar Baby",
                        tally=4, suppressed=False, boxes=4):
        # Tar IC now use a full 10-box monitor (like every other IC); a single (Rating)D Steamroller
        # hit lands 6 icon boxes, so the crash tests pre-damage the tar to 4/10 -- one clean Deadly
        # strike (4 + 6 = 10) then crashes it. Steamroller "takes it out faster" = ~2 strikes fresh.
        s = _fresh_state()
        s["event_log"] = []
        s["security_tally"] = tally
        ic = {"id": tar_id, "type": tar_type, "rating": rating, "status": "lurking", "boxes": boxes}
        if suppressed:
            ic["suppressed"] = True
        s["lurking_ic"] = [ic]
        return s

    # -- schema / wiring -------------------------------------------------------

    def test_schema_accepts_steamroller_utility_and_action(self):
        from app.schemas.matrix_run import DeckerUtilities, RunActionInput
        assert DeckerUtilities().steamroller == 0                 # default
        assert DeckerUtilities(steamroller=6).steamroller == 6
        inp = RunActionInput(action_type="steamroller", subsystem="control",
                             target_ic_id="lc_tar1")
        assert inp.action_type == "steamroller"
        assert inp.target_ic_id == "lc_tar1"
        assert mr._ACTION_COST.get("steamroller") == "Simple"     # Steamroller is a Simple Action

    def test_effective_steamroller_reads_carried_and_subtracts_wear(self):
        decker = self._decker(steamroller=6)
        state = _fresh_state()
        assert mr._effective_steamroller(decker, state) == 6
        # Steamroller is immune to tar, but a Hog drain can still wear it (program_damage).
        state["program_damage"] = {"steamroller": 2}
        assert mr._effective_steamroller(decker, state) == 4
        state["program_damage"] = {"steamroller": 9}              # cannot go negative
        assert mr._effective_steamroller(decker, state) == 0
        # Not loaded -> 0 (the decker carries no anti-tar weapon).
        assert mr._effective_steamroller({"utilities": {"armor": 4}}, _fresh_state()) == 0

    # -- crash + removal + tally ----------------------------------------------

    def test_steamroller_crashes_tar_and_removes_it(self, scripted):
        # Tar rolls all 1s (resists nothing) -> the (Rating)D Deadly hit stands and crashes it.
        scripted([1])
        decker = self._decker(steamroller=6)
        state = self._state_with_tar(rating=5, tally=4)
        mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6,
                              target_ic_id="lc_tar1")
        assert state["lurking_ic"] == []                          # tar destroyed + removed
        assert state["security_tally"] == 9                       # +5 (tar rating), no mask
        ev = state["event_log"][-1]
        assert ev["type"] == "tar_steamrolled"
        assert ev["destroyed"] is True
        assert ev["ic_type"] == "Tar Baby"
        assert ev["tally_increase"] == 5

    def test_steamroller_targets_named_tar(self, scripted):
        scripted([1])
        decker = self._decker(steamroller=6)
        state = _fresh_state(); state["event_log"] = []; state["security_tally"] = 0
        # Pre-damaged to 4/10 so one clean Deadly strike (6 boxes) crashes the 10-box monitor.
        state["lurking_ic"] = [
            {"id": "lc_a", "type": "Tar Baby", "rating": 4, "status": "lurking"},
            {"id": "lc_b", "type": "Tar Pit", "rating": 6, "status": "lurking", "boxes": 4},
        ]
        mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6,
                              target_ic_id="lc_b")
        assert [ic["id"] for ic in state["lurking_ic"]] == ["lc_a"]   # only the named tar removed
        ev = state["event_log"][-1]
        assert ev["ic_id"] == "lc_b" and ev["destroyed"] is True

    def test_unnamed_target_picks_a_lurking_tar_over_other_ic(self, scripted):
        scripted([1])
        decker = self._decker(steamroller=6)
        state = _fresh_state(); state["event_log"] = []; state["security_tally"] = 0
        # Tar pre-damaged to 4/10 so a single Deadly strike (6 boxes) crashes it.
        state["lurking_ic"] = [
            {"id": "lc_worm", "type": "Worm", "rating": 4, "status": "lurking"},
            {"id": "lc_tar", "type": "Tar Baby", "rating": 5, "status": "lurking", "boxes": 4},
        ]
        mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6, target_ic_id="")
        # The worm is skipped (not a tar); the Tar Baby is crushed.
        assert [ic["id"] for ic in state["lurking_ic"]] == ["lc_worm"]
        ev = state["event_log"][-1]
        assert ev["ic_id"] == "lc_tar" and ev["destroyed"] is True

    # -- IMMUNITY: no tar crash-backlash --------------------------------------

    def test_steamroller_immune_no_utility_backlash(self, scripted):
        # The tar is crushed, but because tar_baby_test is NEVER run the decker's loaded utilities
        # are untouched and no program_damage (crash wear) accrues.
        scripted([1])
        decker = self._decker(steamroller=6)
        before = dict(decker["utilities"])
        state = self._state_with_tar(rating=6)
        mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6,
                              target_ic_id="lc_tar1")
        assert decker["utilities"] == before                     # no utility crashed
        assert not state.get("program_damage")                   # no crash wear from the tar
        assert not state.get("mpcp_infected")

    def test_tar_pit_corruption_path_is_bypassed(self, scripted):
        # Crushing a Tar Pit with Steamroller does NOT trigger its "corrupt all copies" backlash
        # (immunity): the decker's programs survive and no tar_pit_corruption event is logged.
        scripted([1])
        decker = self._decker(steamroller=6)
        state = self._state_with_tar(rating=6, tar_type="Tar Pit", tally=4)
        mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6,
                              target_ic_id="lc_tar1")
        assert state["lurking_ic"] == []                         # Tar Pit crushed
        assert decker["utilities"]["attack"] == 5                # no copies corrupted
        assert not any(e["type"] == "tar_pit_corruption" for e in state["event_log"])
        ev = state["event_log"][-1]
        assert ev["type"] == "tar_steamrolled" and ev["destroyed"] is True

    # -- tally masking: Stealth/Skulk + suppression ---------------------------

    def test_crash_tally_reduced_by_steamroller_skulk(self, scripted):
        # The Steamroller's Stealth/Skulk option masks the crash: tally += max(0, rating - skulk).
        scripted([1])
        decker = self._decker(steamroller=6, skulk=2)
        state = self._state_with_tar(rating=5, tally=4)
        mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6,
                              target_ic_id="lc_tar1")
        assert state["security_tally"] == 7                      # +max(0, 5 - 2) = +3
        ev = state["event_log"][-1]
        assert ev["tally_increase"] == 3
        assert "skulk" in ev["description"].lower()

    def test_high_skulk_zeroes_the_tally(self, scripted):
        scripted([1])
        decker = self._decker(steamroller=6, skulk=9)            # skulk >= rating -> no leak
        state = self._state_with_tar(rating=5, tally=4)
        mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6,
                              target_ic_id="lc_tar1")
        assert state["lurking_ic"] == []                         # still crushed
        assert state["security_tally"] == 4                      # fully masked -> no tally add
        assert state["event_log"][-1]["tally_increase"] == 0

    def test_suppressed_tar_adds_no_tally(self, scripted):
        # "...unless the decker suppresses the IC" -- a suppressed tar crash adds no tally at all.
        scripted([1])
        decker = self._decker(steamroller=6)
        state = self._state_with_tar(rating=5, tally=4, suppressed=True)
        mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6,
                              target_ic_id="lc_tar1")
        assert state["lurking_ic"] == []                         # still crushed
        assert state["security_tally"] == 4                      # NO tally add (suppressed)
        ev = state["event_log"][-1]
        assert ev["tally_increase"] == 0
        assert ev["destroyed"] is True
        assert "suppress" in ev["description"].lower()

    # -- target validation -----------------------------------------------------

    def test_non_tar_target_is_rejected(self, scripted):
        from fastapi import HTTPException
        scripted([1])                      # must NOT matter -- rejected before any roll
        decker = self._decker(steamroller=6)
        state = _fresh_state(); state["event_log"] = []
        state["lurking_ic"] = [{"id": "lc_worm", "type": "Worm", "rating": 5, "status": "lurking"}]
        with pytest.raises(HTTPException) as exc:
            mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6,
                                  target_ic_id="lc_worm")
        assert exc.value.status_code == 400
        assert "tar" in exc.value.detail.lower()
        assert len(state["lurking_ic"]) == 1                     # worm untouched

    # -- failure / no-op paths -------------------------------------------------

    def test_low_steamroller_fails_tar_stays_lurking(self, scripted):
        # Net-successes-first: the tar survives only when its resistance out-rolls the to-hit. A
        # rating-1 Steamroller (Power 1 -> tar resists at TN 2) with a weak to-hit (6 misses,
        # 0 succ) is out-resisted by the tar's 6 hits -> net -6 -> Deadly staged down to a graze:
        # it survives, takes some boxes, and NO tally is added (no crash). Draw order: 6 to-hit
        # dice, then 6 resist dice.
        scripted([1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4])
        decker = self._decker(steamroller=1)
        state = self._state_with_tar(rating=6, tally=4)
        mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6,
                              target_ic_id="lc_tar1")
        assert len(state["lurking_ic"]) == 1                     # tar survived, still lurking
        assert state["lurking_ic"][0]["boxes"] >= 1              # accumulated damage
        assert state["security_tally"] == 4                      # no crash -> no tally
        ev = state["event_log"][-1]
        assert ev["type"] == "tar_steamrolled" and ev["destroyed"] is False

    def test_no_tar_present_reports_miss(self, scripted):
        scripted([1])
        decker = self._decker(steamroller=6)
        state = _fresh_state(); state["event_log"] = []; state["security_tally"] = 3
        mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6, target_ic_id="")
        ev = state["event_log"][-1]
        assert ev["type"] == "tar_steamrolled" and ev["destroyed"] is False
        assert state["security_tally"] == 3                      # untouched (nothing to crush)

    def test_offline_steamroller_does_nothing(self, scripted):
        # Manual Steamroller with none loaded must raise 400 (endpoint never commits the spent
        # action point) rather than logging a no-op event. DINAB (via_dinab) still logs.
        from fastapi import HTTPException
        scripted([1])                      # would-be crash -- must NOT be rolled
        decker = {"utilities": {"armor": 4}, "computer_skill": 6, "mpcp": 4, "hardening": 0}
        state = self._state_with_tar(rating=6)
        with pytest.raises(HTTPException) as exc:
            mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6,
                                  target_ic_id="lc_tar1")
        assert exc.value.status_code == 400
        assert "steamroller" in exc.value.detail.lower()
        assert len(state["lurking_ic"]) == 1                     # tar untouched (no Steamroller)


class TestDefuseDataBomb:
    """vr2 Defuse Data Bomb (vr2_rules.md L463-480): the carried Defuse utility reduces the TN of
    the deliberate Defuse operation. It is an OPPOSED System Test (user ruling 2026-07-10): the
    host rolls Security Value vs the Detection Factor and its successes add to the security tally on
    EVERY attempt; the decker disarms the bomb only on a net win. A successful defuse adds no
    bomb-RATING tally (a defuse is not a crash); an all-1s botch detonates it; any other failure
    leaves it primed. A still-armed bomb only goes off when the decker SUCCESSFULLY accesses the
    protected target (failed access does not trigger it). In these tests the host dice are scripted
    to all 1s (0 host successes) so the opposed roll adds no tally and the decker's net = its hits.

    _apply_defuse_bomb / _trigger_access_data_bomb are exactly what the /action handler and the
    post-success access path invoke, so they are unit-tested directly (no async endpoint needed)."""

    def _decker(self, defuse=4):
        return {"utilities": {"defuse": defuse}, "computer_skill": 6, "mpcp": 4,
                "hardening": 0, "bod": 4, "evasion": 4, "masking": 4, "sensor": 4}

    def _eff(self):
        return {"bod": 4}

    def _state_with_bomb(self, *, target="files::Secret Files", rating=6, tally=2):
        s = _fresh_state()
        s["event_log"] = []
        s["security_tally"] = tally
        s["data_bombs"] = [{"target": target, "rating": rating}]
        s["defused_bombs"] = []
        return s

    # -- schema / wiring -------------------------------------------------------

    def test_schema_accepts_defuse_utility_and_action(self):
        from app.schemas.matrix_run import DeckerUtilities, RunActionInput
        assert DeckerUtilities().defuse == 0                       # default
        assert DeckerUtilities(defuse=4).defuse == 4
        inp = RunActionInput(action_type="defuse_data_bomb", subsystem="files")
        assert inp.action_type == "defuse_data_bomb"
        assert mr._ACTION_COST.get("defuse_data_bomb") == "Complex"  # Defuse is a Complex Action

    def test_effective_defuse_reads_carried_and_subtracts_wear(self):
        decker = self._decker(defuse=5)
        state = _fresh_state()
        assert mr._effective_defuse(decker, state) == 5
        state["program_damage"] = {"defuse": 2}                   # e.g. Tar Baby / Hog crash wear
        assert mr._effective_defuse(decker, state) == 3
        state["program_damage"] = {"defuse": 9}                   # cannot go negative
        assert mr._effective_defuse(decker, state) == 0
        # Not loaded -> 0 (no Defuse carried, so no TN reduction).
        assert mr._effective_defuse({"utilities": {"armor": 4}}, _fresh_state()) == 0

    # -- deliberate Defuse operation ------------------------------------------

    def test_defuse_success_disarms_with_no_tally(self, scripted):
        # Computer Test vs Files-8 reduced by carried Defuse-4 -> TN 4; pool rolls 6s -> disarmed.
        # Opposed: 6 decker dice (all 6 -> hits) then 6 host dice (all 1 -> 0 host successes).
        scripted([6] * 6 + [1] * 6)
        state = self._state_with_bomb(rating=6, tally=5)
        decker = self._decker(defuse=4)
        mr._apply_defuse_bomb(state, decker, self._eff(), subsystem="files",
                              subsystem_rating=8, decker_pool=6, sec_value=6, sec_code="Green")
        assert state["data_bombs"] == []                          # bomb removed
        assert state["defused_bombs"] == ["files::Secret Files"]  # recorded as inert
        assert state["security_tally"] == 5                       # NO tally add (defuse is not a crash)
        ev = state["event_log"][-1]
        assert ev["type"] == "data_bomb" and ev["outcome"] == "defused"
        assert "TN 4" in ev["description"] and "Defuse 4" in ev["description"]  # carried Defuse reduced TN

    def test_carried_defuse_reduces_the_tn(self, scripted):
        # Same bomb, same dice: bare decker fails (TN 8) but a Defuse-6 deck clears it (TN 2).
        # 3 decker dice then 6 host dice each attempt. House rule: a defuse tie goes to the decker,
        # so the bare-deck FAILURE needs the host to strictly win -- host takes 1 success here.
        scripted([3, 3, 3, 2] + [1] * 5)  # decker 0 succ (TN 8); host 1 succ (TN 2) -> host wins
        bare = self._state_with_bomb(rating=6)
        mr._apply_defuse_bomb(bare, self._decker(defuse=0), self._eff(), subsystem="files",
                              subsystem_rating=8, decker_pool=3, sec_value=6, sec_code="Green")
        assert len(bare["data_bombs"]) == 1                       # TN 8 -- 3s miss, still primed
        assert bare["event_log"][-1]["outcome"] == "primed"
        scripted([3, 3, 3] + [1] * 6)
        armed = self._state_with_bomb(rating=6)
        mr._apply_defuse_bomb(armed, self._decker(defuse=6), self._eff(), subsystem="files",
                              subsystem_rating=8, decker_pool=3, sec_value=6, sec_code="Green")
        assert armed["data_bombs"] == []                          # TN 2 -- 3s clear it, disarmed
        assert armed["event_log"][-1]["outcome"] == "defused"

    def test_defuse_plain_failure_leaves_bomb_primed(self, scripted):
        # Ordinary miss -> bomb stays primed. House rule: a tie now defuses, so a genuine failure
        # means the host strictly won -- which adds its successes to the tally.
        # 3 decker dice (2s -> miss vs TN 8) then 6 host dice (one 2 -> 1 success vs TN 2).
        scripted([2, 2, 2, 2] + [1] * 5)
        state = self._state_with_bomb(rating=6, tally=4)
        mr._apply_defuse_bomb(state, self._decker(defuse=0), self._eff(), subsystem="files",
                              subsystem_rating=8, decker_pool=3, sec_value=6, sec_code="Green")
        assert len(state["data_bombs"]) == 1                      # still armed
        assert state["defused_bombs"] == []
        assert state["security_tally"] == 5                       # host won -> +1 tally (no crash)
        ev = state["event_log"][-1]
        assert ev["type"] == "data_bomb" and ev["outcome"] == "primed"

    def test_defuse_all_ones_botch_detonates(self, scripted):
        # Every die a 1 -> the bomb goes off mid-defuse: removed, blast damage, tally += rating.
        scripted([1])
        state = self._state_with_bomb(rating=6, tally=2)
        mr._apply_defuse_bomb(state, self._decker(defuse=0), self._eff(), subsystem="files",
                              subsystem_rating=8, decker_pool=3, sec_value=6, sec_code="Green")
        assert state["data_bombs"] == []                          # one-shot, consumed
        assert state["defused_bombs"] == []                       # never disarmed
        assert state["security_tally"] == 8                       # 2 + rating 6
        assert state["condition_monitor"]["persona_boxes"] > 0    # took the blast
        ev = state["event_log"][-1]
        assert ev["type"] == "data_bomb" and ev["outcome"] == "detonated"

    def test_defuse_targets_named_bomb(self, scripted):
        scripted([6] * 6 + [1] * 6)
        state = _fresh_state(); state["event_log"] = []; state["security_tally"] = 0
        state["data_bombs"] = [
            {"target": "files::Alpha", "rating": 5},
            {"target": "files::Bravo", "rating": 6},
        ]
        state["defused_bombs"] = []
        mr._apply_defuse_bomb(state, self._decker(defuse=4), self._eff(), subsystem="files",
                              subsystem_rating=8, decker_pool=6, sec_value=6, sec_code="Green",
                              target_file="Bravo")
        assert [b["target"] for b in state["data_bombs"]] == ["files::Alpha"]  # only Bravo disarmed
        assert state["defused_bombs"] == ["files::Bravo"]

    def test_defuse_opposed_host_successes_raise_tally(self, scripted):
        # Opposed system test: even on a failed defuse the host's successes add to the tally.
        # 3 decker dice (2s -> miss vs TN 8) then 6 host dice (all 6 -> 6 host successes vs DF 2).
        scripted([2, 2, 2] + [6] * 6)
        state = self._state_with_bomb(rating=6, tally=1)
        mr._apply_defuse_bomb(state, self._decker(defuse=0), self._eff(), subsystem="files",
                              subsystem_rating=8, decker_pool=3, sec_value=6, sec_code="Green")
        assert len(state["data_bombs"]) == 1                      # defuse failed -> still primed
        assert state["security_tally"] == 7                       # 1 + 6 host successes
        ev = state["event_log"][-1]
        assert ev["outcome"] == "primed" and ev["tally_increase"] == 6

    def test_defuse_no_target_reports_clean(self, scripted):
        scripted([6, 6, 6])                                       # dice must NOT be consumed
        state = _fresh_state(); state["event_log"] = []; state["security_tally"] = 3
        state["data_bombs"] = []; state["defused_bombs"] = []
        mr._apply_defuse_bomb(state, self._decker(defuse=4), self._eff(), subsystem="files",
                              subsystem_rating=8, decker_pool=6, sec_value=6, sec_code="Green")
        ev = state["event_log"][-1]
        assert ev["type"] == "data_bomb" and ev["outcome"] == "no_target"
        assert state["security_tally"] == 3

    # -- access trigger (the only way a still-armed bomb goes off) -------------

    def test_successful_access_detonates_armed_bomb(self, scripted):
        scripted([1])                                            # poor blast resist
        state = self._state_with_bomb(target="files::Payroll", rating=6, tally=2)
        triggered = mr._trigger_access_data_bomb(
            state, self._decker(), self._eff(), action_type="download_data",
            target_file="Payroll", test_success=True, sec_value=6, sec_code="Green")
        assert triggered is True
        assert state["data_bombs"] == []                         # one-shot, consumed
        assert state["security_tally"] == 8                      # 2 + rating 6
        assert state["event_log"][-1]["outcome"] == "detonated"

    def test_failed_access_does_not_trigger_bomb(self, scripted):
        scripted([1])
        state = self._state_with_bomb(target="files::Payroll", rating=6, tally=2)
        triggered = mr._trigger_access_data_bomb(
            state, self._decker(), self._eff(), action_type="download_data",
            target_file="Payroll", test_success=False, sec_value=6, sec_code="Green")
        assert triggered is False
        assert len(state["data_bombs"]) == 1                     # bomb survives -- defuse it first
        assert state["security_tally"] == 2                      # untouched

    def test_defused_bomb_is_inert_on_access(self, scripted):
        scripted([1])
        state = self._state_with_bomb(target="files::Payroll", rating=6, tally=2)
        state["defused_bombs"] = ["files::Payroll"]              # already disarmed
        triggered = mr._trigger_access_data_bomb(
            state, self._decker(), self._eff(), action_type="download_data",
            target_file="Payroll", test_success=True, sec_value=6, sec_code="Green")
        assert triggered is False
        assert state["security_tally"] == 2                      # no blast

    def test_non_access_action_does_not_trigger_bomb(self, scripted):
        scripted([1])
        state = self._state_with_bomb(target="files::Payroll", rating=6, tally=2)
        triggered = mr._trigger_access_data_bomb(
            state, self._decker(), self._eff(), action_type="analyze_icon",
            target_file="Payroll", test_success=True, sec_value=6, sec_code="Green")
        assert triggered is False
        assert len(state["data_bombs"]) == 1

    def test_access_to_unbombed_file_is_safe(self, scripted):
        scripted([1])
        state = self._state_with_bomb(target="files::Payroll", rating=6, tally=2)
        triggered = mr._trigger_access_data_bomb(
            state, self._decker(), self._eff(), action_type="download_data",
            target_file="Some Other File", test_success=True, sec_value=6, sec_code="Green")
        assert triggered is False
        assert len(state["data_bombs"]) == 1

    def test_failed_defuse_then_successful_access_detonates(self, scripted):
        # The headline scenario: fail to defuse (bomb stays primed), then a SUCCESSFUL access of
        # the protected file sets it off.
        state = self._state_with_bomb(target="files::Vault", rating=6, tally=2)
        decker = self._decker(defuse=0)
        scripted([2, 2, 2, 2] + [1] * 5)                        # defuse miss; host 1 succ -> host wins
        mr._apply_defuse_bomb(state, decker, self._eff(), subsystem="files",
                              subsystem_rating=8, decker_pool=3, sec_value=6, sec_code="Green")
        assert len(state["data_bombs"]) == 1                     # primed
        assert state["security_tally"] == 3                      # host won the defuse -> +1 tally
        scripted([1])                                            # now the blast resist
        triggered = mr._trigger_access_data_bomb(
            state, decker, self._eff(), action_type="download_data", target_file="Vault",
            test_success=True, sec_value=6, sec_code="Green")
        assert triggered is True
        assert state["data_bombs"] == []
        assert state["security_tally"] == 9                      # 3 + rating 6
        assert state["event_log"][-1]["outcome"] == "detonated"

    def test_offline_defuse_still_attempts_at_bare_tn(self, scripted):
        # No Defuse loaded -> TN is the full Files rating (no reduction), but the operation still runs.
        scripted([6, 6, 6])
        state = self._state_with_bomb(rating=6, tally=0)
        mr._apply_defuse_bomb(state, self._decker(defuse=0), self._eff(), subsystem="files",
                              subsystem_rating=6, decker_pool=6, sec_value=6, sec_code="Green")
        ev = state["event_log"][-1]
        assert ev["type"] == "data_bomb"
        assert "Defuse 0" in ev["description"]                   # bare TN, no carried reduction

    # -- slave-device bombs (hardened path) -----------------------------------

    def test_defuse_target_subsystem_picks_slave_for_device_bomb(self):
        # The caller derives the controlling subsystem from the bomb's scope, so a device bomb is
        # tested against the Slave rating (vr2 L463-471), not whatever the client sent.
        state = self._state_with_bomb(target="slave::Maglock")
        assert mr._defuse_target_subsystem(state, "Maglock") == "slave"

    def test_defuse_target_subsystem_picks_files_for_file_bomb(self):
        state = self._state_with_bomb(target="files::Vault")
        assert mr._defuse_target_subsystem(state, "Vault") == "files"

    def test_defuse_target_subsystem_handles_legacy_slave_token(self):
        # The legacy "__slave__" encoding still resolves to the Slave subsystem + "Slave device".
        state = self._state_with_bomb(target="__slave__")
        assert mr._defuse_target_subsystem(state, "Slave device") == "slave"

    def test_defuse_target_subsystem_none_when_unmatched(self):
        state = self._state_with_bomb(target="files::Vault")
        assert mr._defuse_target_subsystem(state, "Nonexistent") is None

    def test_defuse_matches_slave_bomb_by_device_name(self, scripted):
        # A device bomb is defused against the Slave rating the caller derived (here passed in).
        scripted([6] * 6 + [1] * 6)
        state = self._state_with_bomb(target="slave::Maglock", rating=6, tally=0)
        mr._apply_defuse_bomb(state, self._decker(defuse=4), self._eff(), subsystem="slave",
                              subsystem_rating=8, decker_pool=6, sec_value=6, sec_code="Green",
                              target_file="Maglock")
        assert state["data_bombs"] == []
        assert state["defused_bombs"] == ["slave::Maglock"]
        assert "slave 8" in state["event_log"][-1]["description"]   # tested vs the Slave rating

    def test_defuse_matches_legacy_slave_token_by_display_name(self, scripted):
        # Regression: the legacy "__slave__" encoding surfaces as "Slave device"; the defuse must
        # match that display name (previously _target_file_name returned "__slave__" -> no match).
        scripted([6] * 6 + [1] * 6)
        state = self._state_with_bomb(target="__slave__", rating=6, tally=0)
        mr._apply_defuse_bomb(state, self._decker(defuse=4), self._eff(), subsystem="slave",
                              subsystem_rating=8, decker_pool=6, sec_value=6, sec_code="Green",
                              target_file="Slave device")
        assert state["data_bombs"] == []
        assert state["defused_bombs"] == ["__slave__"]


class TestAnalyzeIcon:
    """vr2 Analyze Icon (Control test, Analyze utility, Free): the targeted scan that DETECTS a
    data bomb on the protected file or device (vr2 L463). It is the ONLY discovery path -- a broad
    Analyze Subsystem no longer reveals bombs. ``_apply_analyze_icon`` is exactly what the /action
    success handler invokes, so it is unit-tested directly (no async endpoint needed)."""

    def _state(self, bombs):
        s = _fresh_state()
        s["event_log"] = []
        s["data_bombs"] = bombs
        return s

    def test_analyze_file_reveals_file_bomb(self):
        state = self._state([{"target": "files::Monthly Payroll", "rating": 6}])
        mr._apply_analyze_icon(state, target_file="files::Monthly Payroll")
        assert state["data_bombs"][0]["discovered"] is True
        ev = state["event_log"][-1]
        assert ev["type"] == "data_bomb_found" and ev["subsystem"] == "files"
        assert "Monthly Payroll" in ev["description"]

    def test_analyze_clean_file_reports_clear(self):
        # Scanning a DIFFERENT file does not reveal the Other-file bomb; it reports the icon clear.
        state = self._state([{"target": "files::Other", "rating": 6}])
        mr._apply_analyze_icon(state, target_file="files::Payroll")
        assert "discovered" not in state["data_bombs"][0]
        ev = state["event_log"][-1]
        assert ev["type"] == "data_bomb_clear" and ev["subsystem"] == "files"

    def test_analyze_slave_device_reveals_slave_bomb(self):
        state = self._state([{"target": "slave::Maglock", "rating": 6}])
        mr._apply_analyze_icon(state, target_file="slave::__device__")
        assert state["data_bombs"][0]["discovered"] is True
        ev = state["event_log"][-1]
        assert ev["type"] == "data_bomb_found" and ev["subsystem"] == "slave"
        assert "Slave device" in ev["description"]

    def test_analyze_slave_reveals_legacy_token_bomb(self):
        # The single Slave-device scan matches any slave-scoped bomb, incl. the legacy token.
        state = self._state([{"target": "__slave__", "rating": 6}])
        mr._apply_analyze_icon(state, target_file="slave::__device__")
        assert state["data_bombs"][0]["discovered"] is True
        assert state["event_log"][-1]["type"] == "data_bomb_found"

    def test_analyze_slave_with_no_slave_bomb_reports_clear(self):
        # A file bomb is NOT surfaced by scanning the Slave device (scope mismatch).
        state = self._state([{"target": "files::Payroll", "rating": 6}])
        mr._apply_analyze_icon(state, target_file="slave::__device__")
        assert "discovered" not in state["data_bombs"][0]
        assert state["event_log"][-1]["type"] == "data_bomb_clear"

    def test_analyze_skips_already_discovered_bomb(self):
        # Re-scanning a known-bombed icon finds nothing NEW (the bomb is already on record).
        state = self._state([{"target": "files::Payroll", "rating": 6, "discovered": True}])
        mr._apply_analyze_icon(state, target_file="files::Payroll")
        assert state["event_log"][-1]["type"] == "data_bomb_clear"

    def test_analyze_named_slave_device_reveals_only_that_device(self):
        # Two bombed slave devices: scanning ONE names it and leaves the OTHER undiscovered, so the
        # decker can tell a honeypot terminal apart from bombed security cameras (user scenario).
        state = self._state([
            {"target": "slave::Honeypot Terminal", "rating": 6},
            {"target": "slave::Security Cameras", "rating": 8},
        ])
        mr._apply_analyze_icon(state, target_file="slave::Security Cameras")
        by_target = {b["target"]: b for b in state["data_bombs"]}
        assert by_target["slave::Security Cameras"]["discovered"] is True
        assert "discovered" not in by_target["slave::Honeypot Terminal"]
        ev = state["event_log"][-1]
        assert ev["type"] == "data_bomb_found" and ev["subsystem"] == "slave"
        assert "Security Cameras" in ev["description"]

    def test_analyze_named_slave_device_clean_reports_clear(self):
        # Scanning a DIFFERENT device does not reveal the bomb on the other one.
        state = self._state([{"target": "slave::Security Cameras", "rating": 6}])
        mr._apply_analyze_icon(state, target_file="slave::Honeypot Terminal")
        assert "discovered" not in state["data_bombs"][0]
        assert state["event_log"][-1]["type"] == "data_bomb_clear"

    def test_analyze_generic_slave_scan_matches_any_device(self):
        # The generic "Slave device" option (hosts with no named devices) still finds a slave bomb.
        state = self._state([{"target": "slave::Security Cameras", "rating": 6}])
        mr._apply_analyze_icon(state, target_file="slave::__device__")
        assert state["data_bombs"][0]["discovered"] is True
        ev = state["event_log"][-1]
        assert ev["type"] == "data_bomb_found" and "Slave device" in ev["description"]


class TestAnalyzeHostReveal:
    """vr2 Analyze Host (Control test, Analyze utility), USER OVERRIDE: successes reveal the host's
    subsystem ratings -- the 5 ACIFS ratings PLUS the host Security Rating (6 items in all); 6+ net
    successes (or enough to cover every still-hidden item) reveals ALL, otherwise the credits are
    banked and the decker CHOOSES which hidden items to reveal in a second phase. The Security Rating
    is gated by ``host_security_revealed`` (its code/value stay redacted until it flips); VM status
    is NOT modeled. ``_apply_analyze_host`` / ``_reveal_host_ratings`` are exactly what the /action
    handler and the /reveal-host-ratings endpoint invoke, so they are unit-tested directly."""

    ACIFS = [8, 9, 8, 10, 10]  # access, control, index, files, slave

    def _state(self, revealed=None, security_revealed=False):
        s = _fresh_state(acifs=list(self.ACIFS))
        s["event_log"] = []
        s["current_turn"] = 1
        s["host_ratings_revealed"] = dict(revealed or {})
        if security_revealed:
            s["host_security_revealed"] = True
        return s

    def test_six_plus_reveals_all_including_security(self):
        # net >= 6 auto-reveals every ACIFS rating AND the Security Rating, banking no pending.
        state = self._state()
        out = mr._apply_analyze_host(state, 6)
        assert set(state["host_ratings_revealed"]) == {"access", "control", "index", "files", "slave"}
        assert state["host_ratings_revealed"]["files"] == 10
        assert state["host_ratings_revealed"]["control"] == 9
        assert state["host_security_revealed"] is True
        assert "host_analyze_pending" not in state
        assert out["pending"] == 0 and len(out["revealed"]) == 6
        assert {"subsystem": "security", "rating": "Green-6"} in out["revealed"]
        assert state["event_log"][-1]["type"] == "host_analyzed"

    def test_five_net_with_security_hidden_banks_choice(self):
        # net=5 but 6 items hidden (5 ACIFS + security): a genuine choice exists -> bank 5 credits,
        # reveal NOTHING yet (5 < 6, so it is no longer an auto-reveal-all).
        state = self._state()
        out = mr._apply_analyze_host(state, 5)
        assert state["host_ratings_revealed"] == {}
        assert state.get("host_security_revealed") is not True
        assert state["host_analyze_pending"]["credits"] == 5
        assert out["pending"] == 5 and out["revealed"] == []
        assert "choose 5" in state["event_log"][-1]["description"]

    def test_partial_success_banks_pending_and_reveals_nothing(self):
        # net=2 with all 5 hidden: bank 2 credits, reveal NOTHING yet (a genuine choice exists).
        state = self._state()
        out = mr._apply_analyze_host(state, 2)
        assert state["host_ratings_revealed"] == {}
        assert state["host_analyze_pending"]["credits"] == 2
        assert state["host_analyze_pending"]["turn"] == 1
        assert out["pending"] == 2 and out["revealed"] == []
        ev = state["event_log"][-1]
        assert ev["type"] == "host_analyzed" and "choose 2" in ev["description"]

    def test_reveal_chosen_ratings_clears_pending(self):
        # After banking 2 credits, revealing Files + Slave yields their true ACIFS ratings and
        # clears the banked pending.
        state = self._state()
        mr._apply_analyze_host(state, 2)
        result = mr._reveal_host_ratings(state, ["files", "slave"])
        assert dict(result) == {"files": 10, "slave": 10}
        assert state["host_ratings_revealed"] == {"files": 10, "slave": 10}
        assert "host_analyze_pending" not in state
        ev = state["event_log"][-1]
        assert ev["type"] == "host_analyzed"
        assert {"subsystem": "files", "rating": 10} in ev["revealed"]

    def test_reveal_wrong_count_raises(self):
        # Banked 2 credits but only 1 pick supplied -> reject (must reveal exactly 2).
        state = self._state()
        mr._apply_analyze_host(state, 2)
        with pytest.raises(HTTPException):
            mr._reveal_host_ratings(state, ["files"])

    def test_reveal_unknown_subsystem_raises(self):
        state = self._state()
        mr._apply_analyze_host(state, 2)
        with pytest.raises(HTTPException):
            mr._reveal_host_ratings(state, ["files", "cpu"])

    def test_reveal_already_revealed_subsystem_raises(self):
        # Files is already known; picking it again is rejected.
        state = self._state(revealed={"files": 10})
        mr._apply_analyze_host(state, 2)
        with pytest.raises(HTTPException):
            mr._reveal_host_ratings(state, ["files", "slave"])

    def test_reveal_without_pending_raises(self):
        # No Analyze Host has banked anything -> nothing to spend.
        state = self._state()
        with pytest.raises(HTTPException):
            mr._reveal_host_ratings(state, ["files"])

    def test_net_at_least_hidden_count_reveals_all_remaining(self):
        # net=3 with only 2 ratings still hidden (net >= U): auto-reveal both, bank no pending.
        # Security already revealed, so the hidden set is exactly the 2 remaining ACIFS ratings.
        state = self._state(revealed={"access": 8, "control": 9, "index": 8}, security_revealed=True)
        out = mr._apply_analyze_host(state, 3)
        assert set(state["host_ratings_revealed"]) == {"access", "control", "index", "files", "slave"}
        assert "host_analyze_pending" not in state
        assert out["pending"] == 0
        assert {"subsystem": "files", "rating": 10} in out["revealed"]
        assert {"subsystem": "slave", "rating": 10} in out["revealed"]

    def test_reveal_security_as_sixth_item(self):
        # After banking, the decker may spend a credit on the Security Rating ("security"): it flips
        # host_security_revealed and reports the "Code-Value" string (never an ACIFS integer).
        state = self._state()
        mr._apply_analyze_host(state, 1)          # 1 credit banked, 6 items hidden
        result = mr._reveal_host_ratings(state, ["security"])
        assert dict(result) == {"security": "Green-6"}
        assert state["host_security_revealed"] is True
        assert "security" not in state["host_ratings_revealed"]   # not an ACIFS integer
        ev = state["event_log"][-1]
        assert ev["type"] == "host_analyzed"
        assert {"subsystem": "security", "rating": "Green-6"} in ev["revealed"]

    def test_reveal_security_mixed_with_acifs(self):
        # A 2-credit bank spent on one ACIFS rating + the Security Rating reveals both.
        state = self._state()
        mr._apply_analyze_host(state, 2)
        result = mr._reveal_host_ratings(state, ["files", "security"])
        assert dict(result) == {"files": 10, "security": "Green-6"}
        assert state["host_ratings_revealed"] == {"files": 10}
        assert state["host_security_revealed"] is True

    def test_reveal_already_revealed_security_raises(self):
        # Security already known; picking it again is rejected.
        state = self._state(security_revealed=True)
        mr._apply_analyze_host(state, 2)
        with pytest.raises(HTTPException):
            mr._reveal_host_ratings(state, ["files", "security"])


class TestAnalyzeAccessLtgReveal:
    """Grounded LTG-Access discovery: a successful Analyze Subsystem on ACCESS learns whether the
    host has regular-grid LTG access. If it does, it surfaces the real grid address AND flips the
    host visible on the grid (a persisted edit), mirroring the reveal onto its org LTG listing so a
    host first reached via a trap door becomes reachable normally. A host with no LTG stays
    trap-door-only. A FAILED access analysis reveals nothing, is retryable, and emits a themed
    'blocked' event. Driven through the REAL ``perform_action`` with the host + org-sync stubbed."""

    def _decker(self):
        return {"name": "Static", "mpcp": 8, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                "computer_skill": 6, "intelligence": 6, "utilities": {}}

    def _host(self, ltg_address, visible=False):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6, "acifs": [8, 9, 8, 10, 10]}
            trap_doors_json = None
        h = _Host()
        h.ltg_address = ltg_address
        h.is_visible_to_players = visible
        return h

    def _state(self, host):
        st = mr._initial_state(self._decker(), host)
        st["logon_complete"] = True
        return st

    class _FakeDB:
        async def commit(self):
            pass

        async def refresh(self, obj):
            pass

    def _drive(self, monkeypatch, host, *, success=True):
        import asyncio
        from app.schemas.matrix_run import RunActionInput

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = None
            state_json = None

        run = _StubRun()
        run.decker_json = self._decker()
        run.state_json = self._state(host)

        async def _fake_get_run(db, run_id):
            return run

        async def _fake_get_host(db, host_id):
            return host

        def _fake_test(**kw):
            if success:
                return {"success": True, "decker_roll": {"successes": 3, "ones": 0},
                        "host_roll": {"successes": 0}, "decker_net_successes": 3, "tally_increase": 0}
            return {"success": False, "decker_roll": {"successes": 0, "ones": 0},
                    "host_roll": {"successes": 3}, "decker_net_successes": -3, "tally_increase": 0}

        reveal_calls = []

        async def _fake_reveal_sync(db, h):
            reveal_calls.append(h)

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_get_host_or_404", _fake_get_host)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(mr, "sync_host_reveal_to_org", _fake_reveal_sync)
        monkeypatch.setattr(eng, "system_test", _fake_test)

        inp = RunActionInput(action_type="analyze_subsystem", subsystem="access",
                             utility_rating=0, hacking_pool_dice=0, target_file="")
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.perform_action(run_id=7, body=inp, auth=auth, db=self._FakeDB()))
        return run.state_json, reveal_calls

    def test_access_success_with_ltg_flips_visibility_and_reveals_address(self, monkeypatch):
        host = self._host("LTG 4080", visible=False)
        st, reveal_calls = self._drive(monkeypatch, host, success=True)
        assert st["host_ltg_revealed"] is True
        assert st["host_has_ltg"] is True
        assert st["host_ltg_address"] == "LTG 4080"
        assert host.is_visible_to_players is True            # persisted grid reveal
        assert reveal_calls == [host]                        # org LTG listing mirrored once
        ev = [e for e in st["event_log"] if e["type"] == "host_ltg_revealed"][-1]
        assert ev["has_ltg"] is True and ev["ltg_address"] == "LTG 4080"

    def test_access_success_no_ltg_stays_trapdoor_only(self, monkeypatch):
        host = self._host(None, visible=False)
        st, reveal_calls = self._drive(monkeypatch, host, success=True)
        assert st["host_ltg_revealed"] is True
        assert st["host_has_ltg"] is False
        assert host.is_visible_to_players is False           # NOT surfaced on the grid
        assert reveal_calls == []                            # no org sync for a trap-door-only host
        ev = [e for e in st["event_log"] if e["type"] == "host_ltg_revealed"][-1]
        assert ev["has_ltg"] is False

    def test_access_failure_emits_blocked_and_reveals_nothing(self, monkeypatch):
        host = self._host("LTG 4080", visible=False)
        st, reveal_calls = self._drive(monkeypatch, host, success=False)
        assert st["host_ltg_revealed"] is False              # nothing revealed on a failed probe
        assert host.is_visible_to_players is False
        assert reveal_calls == []
        assert any(e["type"] == "access_analysis_blocked" for e in st["event_log"])
        assert not any(e["type"] == "host_ltg_revealed" for e in st["event_log"])


class TestHostSecurityRedaction:
    """The host Security Rating (SC/SV) is GM-only for EVERY host until Analyze Host reveals it
    (host_security_revealed); the grid address is hidden until host_ltg_revealed. ``_serialize_run``
    strips them from the player payload while hidden and exposes them once revealed. Admins see all."""

    def _decker(self):
        return {"name": "Static", "mpcp": 8, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                "computer_skill": 6, "intelligence": 6, "utilities": {}}

    def _host(self):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6, "acifs": [8, 9, 8, 10, 10]}
            ltg_address = "LTG 4080"
            trap_doors_json = None
        return _Host()

    def _run(self, **overrides):
        from types import SimpleNamespace
        from datetime import datetime, UTC
        st = mr._initial_state(self._decker(), self._host())
        st.update(overrides)
        return SimpleNamespace(id=1, host_id=3, status="active",
                               decker_json=self._decker(), state_json=st,
                               created_at=datetime.now(UTC), updated_at=datetime.now(UTC))

    _PLAYER = {"is_admin": False, "is_user": True, "user_token": None}
    _ADMIN = {"is_admin": True, "is_user": False, "user_token": None}

    def test_player_view_hides_sc_sv_until_revealed(self):
        out = mr._serialize_run(self._run(), self._PLAYER)
        st = out["state_json"]
        assert "host_security_code" not in st
        assert "host_security_value" not in st

    def test_player_view_shows_sc_sv_once_revealed(self):
        out = mr._serialize_run(self._run(host_security_revealed=True), self._PLAYER)
        st = out["state_json"]
        assert st["host_security_code"] == "Green"
        assert st["host_security_value"] == 6

    def test_admin_view_always_shows_sc_sv(self):
        out = mr._serialize_run(self._run(), self._ADMIN)
        st = out["state_json"]
        assert st["host_security_code"] == "Green"
        assert st["host_security_value"] == 6

    def test_player_view_hides_ltg_address_until_revealed(self):
        out = mr._serialize_run(self._run(), self._PLAYER)
        st = out["state_json"]
        assert "host_ltg_address" not in st
        assert "host_has_ltg" not in st

    def test_player_view_shows_ltg_address_once_revealed(self):
        out = mr._serialize_run(self._run(host_ltg_revealed=True), self._PLAYER)
        st = out["state_json"]
        assert st["host_ltg_address"] == "LTG 4080"
        assert st["host_has_ltg"] is True


class TestValidatePasscode:
    """vr2 L1899 Validate Passcode: planting a fake passcode is an ordinary opposed Control System
    Test -- there is NO flat +2 (the +2/+6 only apply to elevated superuser/supervisor passcodes the
    app doesn't model). A NET success grants Legitimate status (``has_legitimate_status``) so IC
    attack the persona on the Legitimate COMBAT_TN column until logoff / active alert; it does NOT
    buff the decker's other System Tests and does NOT affect enemy deckers. A FAILED plant may be
    retried and still raised the security tally by the host's opposed successes. Drives the REAL
    ``perform_action`` so the inline TN math + success/fail handlers are exercised end to end."""

    def _decker(self):
        return {"name": "Ghost", "mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                "computer_skill": 6, "intelligence": 6, "quickness": 4, "willpower": 4,
                "body": 4, "utilities": {}}

    def _host(self):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6,
                           "acifs": [8, 9, 8, 10, 10]}
            ltg_address = None
            trap_doors_json = None
        return _Host()

    def _state(self):
        st = mr._initial_state(self._decker(), self._host())
        st["logon_complete"] = True
        return st

    class _FakeDB:
        async def commit(self):
            pass

        async def refresh(self, obj):
            pass

    def _drive(self, monkeypatch, state, *, action_type, subsystem="access",
               system_success=True, host_succ=2):
        """Run the REAL ``perform_action`` against a stub run with a scripted ``system_test`` that
        records the kwargs it was called with (so we can assert the exact ``extra_tn_modifier``).
        NOTE: ``perform_action`` deepcopies ``run.state_json``, so callers that chain drives must
        feed the RETURNED state into the next drive. Returns (final_state, captured_kwargs)."""
        import asyncio
        from app.schemas.matrix_run import RunActionInput

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = None
            state_json = None

        run = _StubRun()
        run.decker_json = self._decker()
        # Guarantee the per-pass action economy never interferes (we test the house rule, not AP).
        state["pass_action_points"] = 4
        state["pass_free"] = 4
        state["initiative_passes"] = 4
        state["current_pass"] = 1
        run.state_json = state

        async def _fake_get_run(db, run_id):
            return run

        captured: dict = {}

        def _fake_test(**kw):
            captured.clear()
            captured.update(kw)
            if system_success:
                return {"success": True, "decker_roll": {"successes": 3, "ones": 0},
                        "host_roll": {"successes": host_succ},
                        "decker_net_successes": 3, "tally_increase": host_succ}
            return {"success": False, "decker_roll": {"successes": 0, "ones": 0},
                    "host_roll": {"successes": host_succ},
                    "decker_net_successes": -host_succ, "tally_increase": host_succ}

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "system_test", _fake_test)

        inp = RunActionInput(action_type=action_type, subsystem=subsystem,
                             utility_rating=0, hacking_pool_dice=0, target_file="")
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.perform_action(run_id=7, body=inp, auth=auth, db=self._FakeDB()))
        return run.state_json, captured

    def test_validate_test_has_no_flat_tn_penalty(self, monkeypatch):
        # No house-rule +2: a normal passcode plant runs at the decker's base TN (extra mod 0).
        _out, cap = self._drive(monkeypatch, self._state(),
                                action_type="validate_passcode", system_success=True)
        assert cap["extra_tn_modifier"] == 0

    def test_success_sets_only_legitimate_status(self, monkeypatch):
        out, _ = self._drive(monkeypatch, self._state(),
                             action_type="validate_passcode", system_success=True)
        assert out["has_legitimate_status"] is True
        assert "passcode_tn_bonus" not in out          # the global -2 buff is gone

    def test_success_does_not_buff_other_system_tests(self, monkeypatch):
        st1, _ = self._drive(monkeypatch, self._state(),
                             action_type="validate_passcode", system_success=True)
        assert st1["has_legitimate_status"] is True
        # A subsequent System Test runs at its normal TN -- Legitimate status is NOT a -2 buff.
        _out, cap = self._drive(monkeypatch, st1, action_type="analyze_host",
                                subsystem="control", system_success=True)
        assert cap["extra_tn_modifier"] == 0

    def test_failure_does_not_lock_out_and_raises_tally(self, monkeypatch):
        st0 = self._state()
        tally0 = st0["security_tally"]
        out, _ = self._drive(monkeypatch, st0, action_type="validate_passcode",
                             system_success=False, host_succ=3)
        assert "validate_passcode_attempted" not in out     # no one-shot lockout
        assert out.get("passcode_tn_bonus") in (None, False)
        assert out.get("has_legitimate_status") in (None, False)
        assert out["security_tally"] == tally0 + 3          # tally += host (opposed) successes

    def test_failed_validate_can_be_retried(self, monkeypatch):
        st1, _ = self._drive(monkeypatch, self._state(),
                             action_type="validate_passcode", system_success=False, host_succ=2)
        assert "validate_passcode_attempted" not in st1
        # Retrying is allowed (no HTTPException) and a later success grants Legitimate status.
        st2, _ = self._drive(monkeypatch, st1, action_type="validate_passcode", system_success=True)
        assert st2["has_legitimate_status"] is True


class TestInvalidatePasscode:
    """vr2 L1879 Invalidate Passcode: a successful Control/Validate System Test ERASES a host
    passcode so the affected security icon flips Legitimate -> Intruding and the PC then attacks it on
    the Intruding COMBAT_TN column (its to-hit TN is revised). One success flips a SINGLE named IC /
    enemy decker at the base TN; the ``__all__`` whole-list variant wipes EVERY active IC and enemy
    decker at once for +4 TN. The flip is PERMANENT -- unlike the PC's own Validate Passcode (wiped on
    active alert / logoff) an enemy never regains Legitimate status. A failed erase may be retried and
    still raised the tally. Drives the REAL ``perform_action`` so the +4 injection + flip handlers are
    exercised end to end."""

    def _decker(self):
        return {"name": "Ghost", "mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                "computer_skill": 6, "intelligence": 6, "quickness": 4, "willpower": 4,
                "body": 4, "utilities": {}}

    def _host(self):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6,
                           "acifs": [8, 9, 8, 10, 10]}
            ltg_address = None
            trap_doors_json = None
        return _Host()

    def _state(self, *, ic=None, enemy_deckers=None):
        st = mr._initial_state(self._decker(), self._host())
        st["logon_complete"] = True
        st["active_ic"] = ic if ic is not None else []
        st["enemy_deckers"] = enemy_deckers if enemy_deckers is not None else []
        return st

    def _ic(self, ic_id="ic1", ic_type="Killer", rating=6):
        # acted_pass == the drive's current_pass (1) so the proactive IC loop treats it as having
        # already acted and skips its cybercombat -- we unit-test the Invalidate flip, not the IC's
        # attack (whose unseeded global-RNG damage roll could otherwise flatline the decker and end
        # the run, making test_flip_persists_through_a_later_pass intermittently fail). Mirrors _enemy.
        return {"id": ic_id, "type": ic_type, "rating": rating, "status": "active",
                "initiative": 10, "acted_pass": 1}

    def _enemy(self, ed_id="ed_test1", name="Black Hat"):
        # acted_pass == the drive's current_pass (1) so the proactive enemy loop treats it as having
        # already acted and skips its AI turn -- we unit-test the Invalidate flip, not the enemy AI
        # (a live enemy turn needs a fully spawned dict: computer_skill / utilities / attributes).
        # name_revealed so the flip log shows the decker's handle (Directive #4 identifier reveal).
        return {"id": ed_id, "name": "Security Decker", "handle": name, "name_revealed": True,
                "status": "active", "revealed": True, "acted_pass": 1}

    class _FakeDB:
        async def commit(self):
            pass

        async def refresh(self, obj):
            pass

    def _drive(self, monkeypatch, state, *, target_ic_id, system_success=True, host_succ=2):
        """Run the REAL ``perform_action`` against a stub run with a scripted ``system_test`` that
        records its kwargs (so we can assert the exact ``extra_tn_modifier``). ``perform_action``
        deepcopies ``run.state_json``, so chained drives must feed the RETURNED state into the next
        drive. Returns (final_state, captured_kwargs)."""
        import asyncio
        from app.schemas.matrix_run import RunActionInput

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = None
            state_json = None

        run = _StubRun()
        run.decker_json = self._decker()
        # Guarantee the per-pass action economy never interferes (we test the flip, not AP).
        state["pass_action_points"] = 4
        state["pass_free"] = 4
        state["initiative_passes"] = 4
        state["current_pass"] = 1
        run.state_json = state

        async def _fake_get_run(db, run_id):
            return run

        captured: dict = {}

        def _fake_test(**kw):
            captured.clear()
            captured.update(kw)
            if system_success:
                return {"success": True, "decker_roll": {"successes": 3, "ones": 0},
                        "host_roll": {"successes": host_succ},
                        "decker_net_successes": 3, "tally_increase": host_succ}
            return {"success": False, "decker_roll": {"successes": 0, "ones": 0},
                    "host_roll": {"successes": host_succ},
                    "decker_net_successes": -host_succ, "tally_increase": host_succ}

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "system_test", _fake_test)

        inp = RunActionInput(action_type="invalidate_passcode", subsystem="control",
                             utility_rating=0, hacking_pool_dice=0, target_file="",
                             target_ic_id=target_ic_id)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.perform_action(run_id=7, body=inp, auth=auth, db=self._FakeDB()))
        return run.state_json, captured

    def _last_invalidate(self, state):
        evs = [e for e in state.get("event_log", []) if e.get("type") == "invalidate_passcode"]
        assert evs, "no invalidate_passcode event was logged"
        return evs[-1]

    def test_single_flip_sets_intruding_no_tn_penalty(self, monkeypatch):
        out, cap = self._drive(monkeypatch, self._state(ic=[self._ic("ic1")]), target_ic_id="ic1")
        assert cap["extra_tn_modifier"] == 0                    # a single erase runs at the base TN
        ic = out["active_ic"][0]
        assert ic["intruding"] is True
        assert mr._combat_target_status(ic) == "intruding"     # PC now hits it on the Intruding column
        ev = self._last_invalidate(out)
        assert ev["success"] is True and ev["whole_list"] is False
        assert len(ev["flipped"]) == 1

    def test_whole_list_adds_plus4_and_flips_all(self, monkeypatch):
        st = self._state(ic=[self._ic("ic1"), self._ic("ic2", "Trace")],
                         enemy_deckers=[self._enemy("ed_1", "Null")])
        out, cap = self._drive(monkeypatch, st, target_ic_id="__all__")
        assert cap["extra_tn_modifier"] == 4                   # the whole-list erase is a +4 TN test
        assert all(ic["intruding"] is True for ic in out["active_ic"])
        assert out["enemy_deckers"][0]["intruding"] is True
        ev = self._last_invalidate(out)
        assert ev["whole_list"] is True and len(ev["flipped"]) == 3

    def test_enemy_decker_single_flip(self, monkeypatch):
        out, _ = self._drive(monkeypatch, self._state(enemy_deckers=[self._enemy("ed_1", "Wraith")]),
                             target_ic_id="ed_1")
        assert out["enemy_deckers"][0]["intruding"] is True
        assert "Enemy Decker (Wraith)" in self._last_invalidate(out)["flipped"]

    def test_flip_persists_through_a_later_pass(self, monkeypatch):
        st1, _ = self._drive(monkeypatch, self._state(ic=[self._ic("ic1")]), target_ic_id="ic1")
        assert st1["active_ic"][0]["intruding"] is True
        # The active-alert / logoff wipes clear only the PC's OWN forged passcode
        # (has_legitimate_status) -- they never restore an enemy icon's Legitimate status.
        st1.pop("has_legitimate_status", None)
        st2, _ = self._drive(monkeypatch, st1, target_ic_id="ic1")
        assert st2["active_ic"][0]["intruding"] is True

    def test_failed_invalidate_can_be_retried_and_raises_tally(self, monkeypatch):
        st0 = self._state(ic=[self._ic("ic1")])
        tally0 = st0["security_tally"]
        out, _ = self._drive(monkeypatch, st0, target_ic_id="ic1", system_success=False, host_succ=3)
        assert out["active_ic"][0].get("intruding") in (None, False)   # nothing flips on a miss
        assert self._last_invalidate(out)["success"] is False
        assert out["security_tally"] == tally0 + 3                     # tally += host successes


class TestDecoyIntercept:
    """vr2 Decoy redirect + Condition Monitor (correction #8, user-amended: at most ONE decoy, and
    ties go to the decoy so the redirect roll is 1D6 <= successes, not <). Drives the extracted
    `_decoy_intercept` helper with a FIXED d6 (mr.random) and scripted cybercombat dice
    (eng.random -> all 1s -> 0 attack successes -> base Moderate = 2 boxes on a Green host). The
    decoy takes full staged damage with no resistance roll, accrues its own 10-box CM, and is
    removed when the CM fills. (Trace-IC exclusion is a caller-side placement invariant -- the IC
    loop skips this helper for trace IC -- so it is not re-tested at the helper level.)"""

    def _ic(self, ic_type="Killer", rating=6):
        return {"id": "ic1", "type": ic_type, "rating": rating, "status": "active",
                "initiative": 10}

    def _state(self, *, successes=3, hp=0, sec_code="Green", sec_value=6):
        st = _fresh_state(sec_code=sec_code, sec_value=sec_value)
        st["event_log"] = []
        st["decoy_successes"] = successes
        st["decoy_hp"] = hp
        st["has_legitimate_status"] = False        # intruding TN column
        return st

    def _fix_d6(self, monkeypatch, val):
        class _FixedD6:
            def randint(self, a, b):
                return val
        monkeypatch.setattr(mr, "random", _FixedD6())

    def test_tie_redirects_to_decoy(self, monkeypatch, scripted):
        scripted([1])                              # decoy attack -> 0 successes -> Moderate (2 boxes)
        self._fix_d6(monkeypatch, 3)               # d6 == decoy_successes (3): a TIE -> decoy (<=)
        st = self._state(successes=3, hp=0)
        hit = mr._decoy_intercept(st, self._ic(), sec_code="Green", sec_value=6,
                                  ic_target_status="intruding")
        assert hit is True
        assert st["decoy_hp"] == 2                 # base Moderate = 2 boxes accrued
        ev = st["event_log"][-1]
        assert ev["type"] == "decoy_intercepted"
        assert ev["d6"] == 3

    def test_roll_above_successes_hits_decker(self, monkeypatch, scripted):
        scripted([1])
        self._fix_d6(monkeypatch, 4)               # d6 (4) > successes (3) -> decker, not decoy
        st = self._state(successes=3, hp=0)
        hit = mr._decoy_intercept(st, self._ic(), sec_code="Green", sec_value=6,
                                  ic_target_status="intruding")
        assert hit is False
        assert st["decoy_hp"] == 0
        assert st["event_log"] == []

    def test_no_decoy_present_is_no_intercept(self, monkeypatch, scripted):
        scripted([1])
        self._fix_d6(monkeypatch, 1)
        st = self._state(successes=0, hp=0)
        assert mr._decoy_intercept(st, self._ic(), sec_code="Green", sec_value=6,
                                   ic_target_status="intruding") is False

    def test_full_cm_no_longer_intercepts(self, monkeypatch, scripted):
        scripted([1])
        self._fix_d6(monkeypatch, 1)               # would tie, but the CM is already full
        st = self._state(successes=3, hp=10)
        assert mr._decoy_intercept(st, self._ic(), sec_code="Green", sec_value=6,
                                   ic_target_status="intruding") is False

    def test_damage_accrues_on_the_decoy_cm(self, monkeypatch, scripted):
        scripted([1])
        self._fix_d6(monkeypatch, 2)               # <= 3 -> hit
        st = self._state(successes=3, hp=2)
        mr._decoy_intercept(st, self._ic(), sec_code="Green", sec_value=6,
                            ic_target_status="intruding")
        assert st["decoy_hp"] == 4                 # 2 existing + 2 (Moderate)

    def test_decoy_removed_when_cm_fills(self, monkeypatch, scripted):
        scripted([1])
        self._fix_d6(monkeypatch, 3)               # tie -> hit; 9 + 2 = 11 >= 10 -> destroyed
        st = self._state(successes=3, hp=9)
        mr._decoy_intercept(st, self._ic(), sec_code="Green", sec_value=6,
                            ic_target_status="intruding")
        assert st["decoy_successes"] == 0          # decoy removed
        assert st["decoy_hp"] == 0
        ev = st["event_log"][-1]
        assert ev["decoy_destroyed"] is True
        assert "DECOY DESTROYED" in ev["description"]


# -- Slow (cripple proactive IC) -----------------------------------------------

class TestSlow:
    """vr2_rules.md L1572-1578 -- Slow reduces a PROACTIVE IC's execution speed. ``_apply_slow`` is
    exactly what the /action 'slow' handler invokes (an early-return action, before the generic
    test), so it is unit-tested directly (mirrors TestSteamroller): a to-hit Computer Test
    (Computer + Hacking Pool vs the host combat TN, eased -2 by the Targeting option) must land,
    then an opposed Resistance (Slow Rating) Test is rolled for the IC. On a win the IC loses one
    action per 2 net successes (>= 1 on a win) and HANGS once its passes are gone. Reactive IC are
    immune; a trace IC is only vulnerable during its Hunt Cycle (both rejected with 400)."""

    def _decker(self, slow=4, **opts):
        d = {"utilities": {"slow": slow, "analyze": 4}, "computer_skill": 6, "mpcp": 4,
             "hardening": 0, "bod": 4, "evasion": 4, "masking": 4, "sensor": 4}
        if opts:
            d["program_options"] = {"slow": dict(opts)}
        return d

    def _state_with_ic(self, *, ic_type="Killer", rating=2, initiative=10, ic_id="ic1",
                       trace_phase=None, suppressed=False):
        s = _fresh_state()
        s["event_log"] = []
        s["current_turn"] = 1
        ic = {"id": ic_id, "type": ic_type, "rating": rating, "status": "active",
              "initiative": initiative}
        if trace_phase:
            ic["trace_phase"] = trace_phase
        if suppressed:
            ic["suppressed"] = True
        s["active_ic"] = [ic]
        return s

    # -- schema / wiring -------------------------------------------------------

    def test_schema_accepts_slow_utility_and_action(self):
        from app.schemas.matrix_run import DeckerUtilities, RunActionInput
        assert DeckerUtilities().slow == 0                       # default: not carried
        assert DeckerUtilities(slow=6).slow == 6
        inp = RunActionInput(action_type="slow", subsystem="control", target_ic_id="ic1")
        assert inp.action_type == "slow" and inp.target_ic_id == "ic1"
        assert mr._ACTION_COST.get("slow") == "Simple"           # a Simple action

    def test_effective_slow_reads_carried_and_subtracts_wear(self):
        decker = self._decker(slow=6)
        state = _fresh_state()
        assert mr._effective_slow(decker, state) == 6
        state["program_damage"] = {"slow": 2}                   # crash wear lowers it
        assert mr._effective_slow(decker, state) == 4
        state["program_damage"] = {"slow": 9}                   # worn past zero -> offline
        assert mr._effective_slow(decker, state) == 0
        assert mr._effective_slow({"utilities": {"armor": 4}}, _fresh_state()) == 0  # not loaded

    # -- offline / no target ---------------------------------------------------

    def test_no_slow_loaded_rejects_and_spends_nothing(self):
        # Manual Slow with no utility loaded must raise 400 (so the endpoint never commits the
        # spent action point) rather than logging a no-op event. DINAB (via_dinab) still logs.
        from fastapi import HTTPException
        state = self._state_with_ic()
        with pytest.raises(HTTPException) as exc:
            mr._apply_slow(state, {"utilities": {}}, sec_code="Green", decker_pool=6,
                           target_ic_id="ic1")
        assert exc.value.status_code == 400
        assert "slow" in exc.value.detail.lower()
        assert "actions_lost" not in state["active_ic"][0]      # IC untouched

    def test_no_eligible_target_emits_no_target(self):
        # Only a reactive Probe is present and no id is named -> the auto-pick finds nothing.
        state = self._state_with_ic(ic_type="Probe", rating=4, ic_id="pr1")
        mr._apply_slow(state, self._decker(), sec_code="Green", decker_pool=6, target_ic_id="")
        ev = state["event_log"][-1]
        assert ev["type"] == "ic_slowed" and ev["outcome"] == "no_target"

    # -- target eligibility (rejections, no dice rolled) ----------------------

    def test_reactive_ic_is_immune(self):
        import fastapi
        state = self._state_with_ic(ic_type="Probe", rating=4, ic_id="pr1")
        with pytest.raises(fastapi.HTTPException) as exc:
            mr._apply_slow(state, self._decker(), sec_code="Green", decker_pool=6,
                           target_ic_id="pr1")
        assert exc.value.status_code == 400
        assert "reactive" in str(exc.value.detail).lower()

    def test_location_cycle_trace_is_rejected(self):
        import fastapi
        state = self._state_with_ic(ic_type="Trace", rating=5, ic_id="tr1", trace_phase="locate")
        with pytest.raises(fastapi.HTTPException) as exc:
            mr._apply_slow(state, self._decker(), sec_code="Green", decker_pool=6,
                           target_ic_id="tr1")
        assert exc.value.status_code == 400
        assert "location cycle" in str(exc.value.detail).lower()

    # -- to-hit + opposed test outcomes ---------------------------------------

    def test_missed_to_hit_leaves_ic_untouched(self, scripted):
        # to-hit: 6 dice all 1 vs Green-legitimate TN 4 -> 0 hits -> missed (no opposed test).
        scripted([1, 1, 1, 1, 1, 1])
        state = self._state_with_ic(ic_type="Killer", rating=4, initiative=10)
        mr._apply_slow(state, self._decker(slow=4), sec_code="Green", decker_pool=6,
                       target_ic_id="ic1")
        ev = state["event_log"][-1]
        assert ev["outcome"] == "missed"
        assert "actions_lost" not in state["active_ic"][0]

    def test_opposed_test_resisted_no_effect(self, scripted):
        # to-hit hits (six 6s); but the IC wins the opposed test (decker 0 vs IC 4) -> no effect.
        scripted([6, 6, 6, 6, 6, 6] + [1, 1, 1, 1] + [6, 6, 6, 6])
        state = self._state_with_ic(ic_type="Killer", rating=4, initiative=10)
        mr._apply_slow(state, self._decker(slow=4), sec_code="Green", decker_pool=6,
                       target_ic_id="ic1")
        ev = state["event_log"][-1]
        assert ev["outcome"] == "resisted" and ev["net_successes"] == -4
        assert "actions_lost" not in state["active_ic"][0]

    def test_win_reduces_actions_without_hanging(self, scripted):
        # to-hit hits; opposed net 2 -> 1 action lost. IC has 2 passes (init 12) -> slowed, 1 left.
        scripted([6, 6, 6, 6, 6, 6] + [6, 6, 1, 1] + [1, 1])
        state = self._state_with_ic(ic_type="Killer", rating=2, initiative=12)
        mr._apply_slow(state, self._decker(slow=4), sec_code="Green", decker_pool=6,
                       target_ic_id="ic1")
        ic = state["active_ic"][0]
        ev = state["event_log"][-1]
        assert ev["outcome"] == "slowed" and ev["hung"] is False and ev["actions_lost"] == 1
        assert ic["actions_lost"] == 1 and ic["slow_turn"] == 1 and "hung_turn" not in ic

    def test_win_hangs_ic_when_actions_exhausted(self, scripted):
        # Same net 2 -> 1 action lost, but the IC has only 1 pass (init 5) -> HANGS for the turn.
        scripted([6, 6, 6, 6, 6, 6] + [6, 6, 1, 1] + [1, 1])
        state = self._state_with_ic(ic_type="Killer", rating=2, initiative=5)
        mr._apply_slow(state, self._decker(slow=4), sec_code="Green", decker_pool=6,
                       target_ic_id="ic1")
        ic = state["active_ic"][0]
        ev = state["event_log"][-1]
        assert ev["outcome"] == "hung" and ev["hung"] is True
        assert ic["actions_lost"] == 1 and ic["hung_turn"] == 1

    def test_hunt_cycle_trace_can_be_slowed(self, scripted):
        # A trace IC in its Hunt Cycle IS a legal Slow target (it acts proactively). net 2 -> slowed.
        scripted([6, 6, 6, 6, 6, 6] + [6, 6, 1, 1] + [1, 1, 1, 1])
        state = self._state_with_ic(ic_type="Trace", rating=4, initiative=12, ic_id="tr1",
                                    trace_phase="hunt")
        mr._apply_slow(state, self._decker(slow=4), sec_code="Green", decker_pool=6,
                       target_ic_id="tr1")
        ic = state["active_ic"][0]
        assert state["event_log"][-1]["outcome"] == "slowed"
        assert ic["actions_lost"] == 1

    def test_accumulates_within_a_turn_then_hangs(self, scripted):
        # Two Slow strikes the same Combat Turn stack actions_lost up to the IC's pass count, then
        # HANG -- proving the slow_turn-scoped accumulation.
        state = self._state_with_ic(ic_type="Killer", rating=2, initiative=12)  # 2 passes
        scripted([6, 6, 6, 6, 6, 6] + [6, 6, 1, 1] + [1, 1])   # net 2 -> 1 lost (slowed)
        mr._apply_slow(state, self._decker(slow=4), sec_code="Green", decker_pool=6,
                       target_ic_id="ic1")
        assert state["active_ic"][0]["actions_lost"] == 1
        assert state["event_log"][-1]["outcome"] == "slowed"
        scripted([6, 6, 6, 6, 6, 6] + [6, 6, 1, 1] + [1, 1])   # +1 -> 2 == passes -> HANG
        mr._apply_slow(state, self._decker(slow=4), sec_code="Green", decker_pool=6,
                       target_ic_id="ic1")
        ic = state["active_ic"][0]
        assert ic["actions_lost"] == 2 and ic["hung_turn"] == 1
        assert state["event_log"][-1]["outcome"] == "hung"


class TestSlowHangLoop:
    """Definition-of-Done clause 2: the proactive-IC loop INSIDE ``perform_action`` must RESPECT the
    hang. Proven against the REAL handler with a Trace IC in its Hunt Cycle (which acts every Combat
    Turn on its initiative and -- in either hunt outcome -- emits an ``ic_attack`` event): with no
    actions lost it acts; once ``actions_lost`` has drained its passes it is SKIPPED and stays
    silent. The player's own action's System Test is stubbed so only the IC loop drives the result."""

    class _Host:
        config_json = {"security_code": "Green", "security_value": 6}
        ltg_address = None

    def _decker(self):
        return {"name": "Ghost", "mpcp": 6, "bod": 5, "evasion": 5, "masking": 5, "sensor": 5,
                "computer_skill": 6, "intelligence": 5, "quickness": 5, "willpower": 4, "body": 5,
                "hardening": 0, "deck_mode": "cool", "utilities": {"sleaze": 4, "deception": 4}}

    def _drive(self, monkeypatch, *, actions_lost):
        import asyncio
        from app.schemas.matrix_run import RunActionInput

        decker = self._decker()
        state = mr._initial_state(decker, self._Host())
        state["logon_complete"] = True
        state["has_legitimate_status"] = True
        state["current_pass"] = 1
        state["initiative_passes"] = 4
        state["pass_action_points"] = 2
        state["pass_free"] = 1
        # init 30 -> 4 passes, so the un-slowed IC acts regardless of which pass we land on; the
        # hung case drains all 4 so its effective passes are 0.
        ic = {"id": "trace1", "type": "Trace", "rating": 5, "status": "active",
              "initiative": 30, "trace_phase": "hunt"}
        if actions_lost:
            ic["actions_lost"] = actions_lost
            ic["slow_turn"] = state["current_turn"]
        state["active_ic"] = [ic]

        class _StubRun:
            id = 11
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        def _fake_test(**kw):
            return {"success": True, "decker_roll": {"successes": 3, "ones": 0},
                    "host_roll": {"successes": 0}, "decker_net_successes": 3, "tally_increase": 0}

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "system_test", _fake_test)
        monkeypatch.setattr(eng, "random", _ScriptedRandom([3]))   # deterministic trace hunt roll

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        inp = RunActionInput(action_type="null_operation", subsystem="control", utility_rating=6)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.perform_action(run_id=11, body=inp, auth=auth, db=_FakeDB()))
        return run.state_json

    def test_active_trace_ic_acts_when_not_hung(self, monkeypatch):
        st = self._drive(monkeypatch, actions_lost=0)
        assert any(e.get("type") == "ic_attack" and e.get("ic_id") == "trace1"
                   for e in st["event_log"]), "a non-hung trace IC must take its hunt action"

    def test_hung_ic_is_skipped_by_the_loop(self, monkeypatch):
        # actions_lost 4 == its 4 passes -> effective passes 0 -> HANGS: the loop takes no action.
        st = self._drive(monkeypatch, actions_lost=4)
        assert not any(e.get("type") == "ic_attack" and e.get("ic_id") == "trace1"
                       for e in st["event_log"]), "a hung IC must take NO action this turn"


class TestSlowResume:
    """vr2_rules.md L1578 -- a hung/slowed IC RESUMES at the start of the next Combat Turn UNLESS it
    is still suppressed. ``new_turn`` clears the per-turn slow markers (actions_lost / slow_turn /
    hung_turn) for every NON-suppressed active IC and LEAVES them on a suppressed IC (which stays
    out of play until released). Driven against the real ``new_turn`` endpoint."""

    class _Host:
        config_json = {"security_code": "Green", "security_value": 6}
        ltg_address = None

    def _decker(self):
        return {"name": "Ghost", "mpcp": 6, "bod": 5, "evasion": 5, "masking": 5, "sensor": 5,
                "computer_skill": 6, "intelligence": 5, "quickness": 5, "willpower": 4, "body": 5,
                "hardening": 0, "deck_mode": "cool", "utilities": {"sleaze": 4}}

    def _drive(self, monkeypatch):
        import asyncio
        decker = self._decker()
        state = mr._initial_state(decker, self._Host())
        state["initiative_passes"] = 1   # single pass -> one End Turn ends the Combat Turn (IC markers reset)
        state["active_ic"] = [
            {"id": "free", "type": "Killer", "rating": 5, "status": "active",
             "initiative": 12, "actions_lost": 2, "slow_turn": 1, "hung_turn": 1},
            {"id": "supp", "type": "Killer", "rating": 5, "status": "active", "suppressed": True,
             "initiative": 12, "actions_lost": 2, "slow_turn": 1, "hung_turn": 1},
        ]

        class _StubRun:
            id = 12
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.new_turn(run_id=12, auth=auth, db=_FakeDB()))
        return run.state_json

    def test_non_suppressed_ic_resumes_next_turn(self, monkeypatch):
        st = self._drive(monkeypatch)
        ic = next(i for i in st["active_ic"] if i["id"] == "free")
        assert "actions_lost" not in ic and "slow_turn" not in ic and "hung_turn" not in ic

    def test_suppressed_ic_stays_hung(self, monkeypatch):
        st = self._drive(monkeypatch)
        ic = next(i for i in st["active_ic"] if i["id"] == "supp")
        assert ic.get("actions_lost") == 2 and ic.get("hung_turn") == 1


# -- #12 Compressor (halve a downloaded file's stored footprint) ----------------

class TestCompressor:
    """vr2_rules.md L1512-1515 -- the Compressor utility "reduces size of data being transferred
    by 50%" up to a "max file size [of] Program Rating * 100 Mp"; the file "must be decompressed
    before being able to read or use [it]" and the deck must hold the uncompressed size to expand
    it. Compressor is a passive data tool that never wears (no program_damage read), so a download
    always stores at half size when within the cap. The download storage pre-check and the success
    handler share ``_compressed_store_size`` as one source of truth, and Decompress File is a
    no-test storage action (like Swap Memory) that expands a chosen compressed file back to full."""

    # -- schema / wiring -------------------------------------------------------

    def test_schema_accepts_compressor_utility_and_action(self):
        from app.schemas.matrix_run import DeckerUtilities, RunActionInput
        assert DeckerUtilities().compressor == 0                 # default: not carried
        assert DeckerUtilities(compressor=6).compressor == 6
        inp = RunActionInput(action_type="decompress_file", subsystem="files", target_file="Vault")
        assert inp.action_type == "decompress_file" and inp.target_file == "Vault"
        assert mr._ACTION_COST.get("decompress_file") == "Complex"   # a full Complex action

    # -- _effective_compressor: carried rating, never wears --------------------

    def test_effective_compressor_reads_carried_no_wear(self):
        assert mr._effective_compressor({"utilities": {"compressor": 6}}) == 6
        assert mr._effective_compressor({"utilities": {}}) == 0
        assert mr._effective_compressor({}) == 0
        # Unlike Slow / Steamroller a crash record never lowers it (no program_damage subtraction).
        assert mr._effective_compressor(
            {"utilities": {"compressor": 4}, "program_damage": {"compressor": 3}}) == 4

    # -- _compressed_store_size: halving, round-up, Rating*100 cap -------------

    def test_compressed_store_size_halves_within_cap(self):
        assert mr._compressed_store_size(6, 100) == (50, True)   # 100 <= 600 -> half
        assert mr._compressed_store_size(3, 300) == (150, True)  # exactly at the Rating*100 cap

    def test_compressed_store_size_rounds_up_so_one_mp_survives(self):
        assert mr._compressed_store_size(6, 1) == (1, True)      # (1+1)//2 = 1, never collapses to 0
        assert mr._compressed_store_size(6, 7) == (4, True)      # (7+1)//2 = 4

    def test_compressed_store_size_over_cap_stores_full(self):
        assert mr._compressed_store_size(3, 301) == (301, False)  # 301 > 300 cap -> not compressed

    def test_compressed_store_size_without_compressor_stores_full(self):
        assert mr._compressed_store_size(0, 100) == (100, False)

    # -- _apply_decompress: expand, clear flag, storage math ------------------

    def _compressed_state(self, *, storage_free=-1, storage_used=50, stored=50, full=100):
        state = _fresh_state()
        state["event_log"] = []
        state["storage_free_mp"] = storage_free
        state["storage_used_mp"] = storage_used
        state["downloaded_files"] = [{"name": "Vault", "size_mp": stored, "is_key": True,
                                      "turn": 1, "compressed": True, "full_size_mp": full}]
        state["paydata"] = [{"name": "Vault", "density": full, "is_key": True,
                             "downloaded": True, "compressed": True}]
        return state

    def test_decompress_expands_and_clears_flag(self):
        state = self._compressed_state(storage_free=200, storage_used=50, stored=50, full=100)
        mr._apply_decompress(state, {"utilities": {"compressor": 6}}, target_file="Vault")
        entry = state["downloaded_files"][0]
        assert entry["size_mp"] == 100 and entry["compressed"] is False
        assert state["paydata"][0]["compressed"] is False        # readable/usable now
        assert state["storage_used_mp"] == 100                   # +50 to hold the full size
        ev = state["event_log"][-1]
        assert ev["type"] == "file_decompressed" and ev["outcome"] == "expanded"
        assert ev["size_mp"] == 100

    def test_decompress_blocked_when_storage_full(self):
        # 60 free, 50 used -> only 10 free; expanding needs +50 -> rejected, nothing changes.
        state = self._compressed_state(storage_free=60, storage_used=50, stored=50, full=100)
        with pytest.raises(mr.HTTPException) as exc:
            mr._apply_decompress(state, {"utilities": {"compressor": 6}}, target_file="Vault")
        assert exc.value.status_code == 400
        assert state["downloaded_files"][0]["compressed"] is True   # untouched
        assert state["storage_used_mp"] == 50

    def test_decompress_untracked_storage_skips_math(self):
        state = self._compressed_state(storage_free=-1, storage_used=50, stored=50, full=100)
        mr._apply_decompress(state, {"utilities": {"compressor": 6}}, target_file="Vault")
        entry = state["downloaded_files"][0]
        assert entry["compressed"] is False and entry["size_mp"] == 100
        assert state["event_log"][-1]["outcome"] == "expanded"

    def test_decompress_no_target_is_noop_event(self):
        state = self._compressed_state(storage_free=200)
        mr._apply_decompress(state, {"utilities": {"compressor": 6}}, target_file="")
        assert state["event_log"][-1]["outcome"] == "no_target"
        assert state["downloaded_files"][0]["compressed"] is True    # nothing expanded

    def test_decompress_unknown_file_is_noop_event(self):
        state = self._compressed_state(storage_free=200)
        mr._apply_decompress(state, {"utilities": {"compressor": 6}}, target_file="Ghost")
        assert state["event_log"][-1]["outcome"] == "no_target"

    def test_decompress_already_expanded_is_noop(self):
        state = self._compressed_state(storage_free=200)
        state["downloaded_files"][0]["compressed"] = False           # already readable
        mr._apply_decompress(state, {"utilities": {"compressor": 6}}, target_file="Vault")
        assert state["event_log"][-1]["outcome"] == "no_target"

    # -- full /action download path: shared storage footprint -----------------

    def _host(self, *, density=100, name="Paydata", is_key=False):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6,
                           "paydata": [{"name": name, "density": density, "is_key": is_key}]}
            ltg_address = None
            trap_doors_json = None
        return _Host()

    def _decker(self, *, compressor=0, storage_free=-1):
        return {"masking": 4, "intelligence": 5, "mpcp": 6, "sensor": 4, "evasion": 4, "bod": 4,
                "computer_skill": 6, "storage_free_mp": storage_free,
                "utilities": {"read_write": 6, "compressor": compressor}}

    def _drive(self, monkeypatch, *, decker, host, action, state=None, success=True):
        import asyncio

        if state is None:
            state = mr._initial_state(decker, host)

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        def _fake_test(**kw):
            if success:
                return {"success": True, "decker_roll": {"successes": 3, "ones": 0},
                        "host_roll": {"successes": 0}, "decker_net_successes": 3,
                        "tally_increase": 0}
            return {"success": False, "decker_roll": {"successes": 0, "ones": 0},
                    "host_roll": {"successes": 3}, "decker_net_successes": -3, "tally_increase": 3}

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "system_test", _fake_test)

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.perform_action(run_id=7, body=action, auth=auth, db=_FakeDB()))
        return run.state_json

    def test_download_with_compressor_halves_stored_size(self, monkeypatch):
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker(compressor=6, storage_free=500)
        action = RunActionInput(action_type="download_data", subsystem="files",
                                target_file="Paydata")
        state = self._drive(monkeypatch, decker=decker, host=self._host(density=100), action=action)
        f = state["downloaded_files"][0]
        assert f["compressed"] is True and f["size_mp"] == 50 and f["full_size_mp"] == 100
        assert state["storage_used_mp"] == 50
        ev = next(e for e in state["event_log"] if e.get("type") == "data_downloaded")
        assert ev["compressed"] is True and ev["size_mp"] == 50

    def test_download_over_cap_stores_full_not_compressed(self, monkeypatch):
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker(compressor=3, storage_free=1000)   # cap = 300 Mp
        action = RunActionInput(action_type="download_data", subsystem="files",
                                target_file="Paydata")
        state = self._drive(monkeypatch, decker=decker, host=self._host(density=400), action=action)
        f = state["downloaded_files"][0]
        assert f["compressed"] is False and f["size_mp"] == 400
        assert state["storage_used_mp"] == 400

    def test_download_without_compressor_stores_full(self, monkeypatch):
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker(compressor=0, storage_free=500)
        action = RunActionInput(action_type="download_data", subsystem="files",
                                target_file="Paydata")
        state = self._drive(monkeypatch, decker=decker, host=self._host(density=100), action=action)
        f = state["downloaded_files"][0]
        assert f["compressed"] is False and f["size_mp"] == 100
        assert state["storage_used_mp"] == 100

    def test_precheck_lets_a_file_fit_compressed(self, monkeypatch):
        # 60 Mp free; a 100 Mp file stores at 50 with the Compressor, so the download is allowed.
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker(compressor=6, storage_free=60)
        action = RunActionInput(action_type="download_data", subsystem="files",
                                target_file="Paydata")
        state = self._drive(monkeypatch, decker=decker, host=self._host(density=100), action=action)
        assert state["downloaded_files"][0]["size_mp"] == 50
        assert state["storage_used_mp"] == 50

    def test_precheck_blocks_same_file_without_compressor(self, monkeypatch):
        # Same 60 Mp free, same 100 Mp file, but NO Compressor -> full size won't fit -> 400.
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker(compressor=0, storage_free=60)
        action = RunActionInput(action_type="download_data", subsystem="files",
                                target_file="Paydata")
        with pytest.raises(mr.HTTPException) as exc:
            self._drive(monkeypatch, decker=decker, host=self._host(density=100), action=action)
        assert exc.value.status_code == 400

    # -- full /action decompress path ------------------------------------------

    def test_action_decompress_expands_via_perform_action(self, monkeypatch):
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker(compressor=6, storage_free=200)
        host = self._host(density=100)
        state = mr._initial_state(decker, host)
        state["storage_used_mp"] = 50
        state["downloaded_files"] = [{"name": "Paydata", "size_mp": 50, "is_key": False,
                                      "turn": 1, "compressed": True, "full_size_mp": 100}]
        for p in state["paydata"]:
            if p["name"] == "Paydata":
                p["downloaded"] = True
                p["compressed"] = True
        action = RunActionInput(action_type="decompress_file", subsystem="files",
                                target_file="Paydata")
        state2 = self._drive(monkeypatch, decker=decker, host=host, action=action, state=state)
        f = state2["downloaded_files"][0]
        assert f["compressed"] is False and f["size_mp"] == 100
        assert state2["storage_used_mp"] == 100
        assert any(e.get("type") == "file_decompressed" and e.get("outcome") == "expanded"
                   for e in state2["event_log"])

    def test_action_decompress_blocked_does_not_spend(self, monkeypatch):
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker(compressor=6, storage_free=60)
        host = self._host(density=100)
        state = mr._initial_state(decker, host)
        state["storage_used_mp"] = 50                            # only 10 free; expand needs +50
        state["downloaded_files"] = [{"name": "Paydata", "size_mp": 50, "is_key": False,
                                      "turn": 1, "compressed": True, "full_size_mp": 100}]
        ap_before = state.get("pass_action_points")
        action = RunActionInput(action_type="decompress_file", subsystem="files",
                                target_file="Paydata")
        with pytest.raises(mr.HTTPException) as exc:
            self._drive(monkeypatch, decker=decker, host=host, action=action, state=state)
        assert exc.value.status_code == 400
        # perform_action mutates a deepcopy, so the original run state is pristine -- NOT spent.
        assert state["downloaded_files"][0]["compressed"] is True
        assert state.get("pass_action_points") == ap_before


# -- #4 Locate Paydata: 1 random paydata point per NET success ------------------

class TestLocatePaydata:
    """vr2_rules.md "Locate Paydata" (ongoing operation): each NET success locates ONE Paydata
    Point, chosen at RANDOM. Corrects the prior bug where a single success revealed EVERY
    undiscovered file at once. The reveal uses a LOCAL random.Random seeded from
    run id + turn + security tally + count-already-located, so it is reproducible for fixed
    inputs yet reveals different files as the run progresses; repeatable until all paydata found.
    """

    def _decker(self):
        return {"masking": 4, "intelligence": 5, "mpcp": 6, "sensor": 4, "evasion": 4, "bod": 4,
                "computer_skill": 6, "utilities": {"browse": 6}}

    def _host(self, paydata):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6,
                           "paydata": [dict(p) for p in paydata]}
            ltg_address = None
            trap_doors_json = None
        return _Host()

    def _paydata(self, n):
        return [{"name": f"File{i}", "density": 10 * (i + 1), "is_key": (i == 0)}
                for i in range(n)]

    def _action(self):
        from app.schemas.matrix_run import RunActionInput
        return RunActionInput(action_type="locate_paydata", subsystem="index")

    def _last_locate_event(self, state):
        return next(e for e in reversed(state["event_log"])
                    if e.get("type") == "paydata_located")

    def _drive(self, monkeypatch, *, decker, host, action, state=None, net=3):
        import asyncio

        if state is None:
            state = mr._initial_state(decker, host)

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        def _fake_test(**kw):
            return {"success": True, "decker_roll": {"successes": net, "ones": 0},
                    "host_roll": {"successes": 0}, "decker_net_successes": net,
                    "tally_increase": 0}

        # Isolate the reveal logic from the action-economy / turn machinery (covered by
        # TestActionEconomyEnforcement): a no-op pass spend keeps current_turn + security_tally
        # fixed across sequential locates, so the only changing seed input is count-already-located.
        monkeypatch.setattr(mr, "_spend_pass_action", lambda *a, **k: None)
        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "system_test", _fake_test)

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.perform_action(run_id=7, body=action, auth=auth, db=_FakeDB()))
        return run.state_json

    def test_reveals_one_file_per_net_success(self, monkeypatch):
        state = self._drive(monkeypatch, decker=self._decker(), host=self._host(self._paydata(5)),
                            action=self._action(), net=3)
        located = [p for p in state["paydata"] if p.get("located")]
        assert len(located) == 3                             # 3 net successes -> 3 files
        ev = self._last_locate_event(state)
        assert len(ev["files"]) == 3
        # The emitted event lists ONLY the newly revealed files.
        assert {f["name"] for f in ev["files"]} == {p["name"] for p in located}

    def test_reveal_caps_at_remaining_pool(self, monkeypatch):
        state = self._drive(monkeypatch, decker=self._decker(), host=self._host(self._paydata(2)),
                            action=self._action(), net=5)
        located = [p for p in state["paydata"] if p.get("located")]
        assert len(located) == 2                             # min(5 successes, 2 remaining) = 2
        assert len(self._last_locate_event(state)["files"]) == 2

    def test_single_net_success_reveals_exactly_one(self, monkeypatch):
        state = self._drive(monkeypatch, decker=self._decker(), host=self._host(self._paydata(5)),
                            action=self._action(), net=1)
        assert sum(1 for p in state["paydata"] if p.get("located")) == 1

    def test_reproducible_for_fixed_inputs(self, monkeypatch):
        # Identical run id / turn / tally / already-located -> the LOCAL seeded RNG picks the SAME
        # set (deterministic given fixed inputs).
        names1 = sorted(f["name"] for f in self._last_locate_event(
            self._drive(monkeypatch, decker=self._decker(), host=self._host(self._paydata(5)),
                        action=self._action(), net=3))["files"])
        names2 = sorted(f["name"] for f in self._last_locate_event(
            self._drive(monkeypatch, decker=self._decker(), host=self._host(self._paydata(5)),
                        action=self._action(), net=3))["files"])
        assert names1 == names2 and len(names1) == 3

    def test_repeatable_until_all_found_then_reports_empty(self, monkeypatch):
        decker, host = self._decker(), self._host(self._paydata(3))
        state = self._drive(monkeypatch, decker=decker, host=host, action=self._action(), net=2)
        assert sum(1 for p in state["paydata"] if p.get("located")) == 2
        # Second locate drains the last remaining file (min(2, 1) = 1).
        state = self._drive(monkeypatch, decker=decker, host=host, action=self._action(),
                            state=state, net=2)
        assert sum(1 for p in state["paydata"] if p.get("located")) == 3
        # Third locate finds nothing left -> empty-pool branch.
        state = self._drive(monkeypatch, decker=decker, host=host, action=self._action(),
                            state=state, net=2)
        assert "no further paydata found" in self._last_locate_event(state)["description"]


# -- #15 One-Shot program option (single-use; Tar IC wipes every copy) ----------

class TestOneShot:
    """vr2_rules.md L1667 -- One-Shot is a single-use program OPTION: the utility executes ONCE
    then "vanishes from active memory"; the decker must Swap Memory a fresh copy to use it again.
    A Tar Baby / Tar Pit crash wipes ALL copies of a one-shot program on the deck (it can never be
    reloaded for the rest of the run).

    "Spent" is expressed through state['program_damage'][util] == its base rating, so a spent
    one-shot reads as effective-0 -- the same gate every _effective_<util> helper already uses --
    and a Swap Memory reload clears it. The helpers/handlers are unit-tested directly (mirrors
    TestSteamroller); the tar-wipe wiring is driven through the live resolve_reactive_ic handler."""

    def _decker(self, util, rating=6, one_shot=True, **utils):
        return {"utilities": {util: rating, **utils},
                "program_options": {util: {"one_shot": one_shot}},
                "computer_skill": 6, "mpcp": 4, "hardening": 0,
                "bod": 4, "evasion": 4, "masking": 4, "sensor": 4}

    def _damaged_state(self, boxes=3):
        s = _fresh_state()
        s["event_log"] = []
        s["condition_monitor"] = {"persona_boxes": boxes}
        return s

    # -- (f) _is_one_shot reads program_options -------------------------------

    def test_is_one_shot_reads_program_options(self):
        decker = {"utilities": {"attack": 6, "medic": 5},
                  "program_options": {"attack": {"one_shot": True},
                                      "medic": {"one_shot": False}}}
        assert mr._is_one_shot(decker, "attack") is True
        assert mr._is_one_shot(decker, "medic") is False
        assert mr._is_one_shot(decker, "shield") is False        # no option entry at all
        # Spaced / cased names normalize to the stored underscore key.
        decker["program_options"]["black_hammer"] = {"one_shot": True}
        assert mr._is_one_shot(decker, "Black Hammer") is True

    # -- (a) consumed once, then effective-0 (hard gate via _effective_*) ------

    def test_one_shot_medic_spent_after_one_use(self, scripted):
        scripted([6])                                            # all dice succeed
        decker = self._decker("medic", rating=6, one_shot=True)
        state = self._damaged_state()
        assert mr._effective_medic(decker, state) == 6
        mr._apply_medic(state, decker)
        assert mr._effective_medic(decker, state) == 0          # spent -> vanished from memory
        assert state["program_damage"]["medic"] == 6
        assert any(e["type"] == "one_shot_spent" and e["utility"] == "medic"
                   for e in state["event_log"])

    def test_one_shot_steamroller_offline_on_second_strike(self, scripted):
        scripted([1])                                           # tar resists nothing -> crush
        decker = self._decker("steamroller", rating=6, one_shot=True)
        state = _fresh_state(); state["event_log"] = []; state["security_tally"] = 0
        state["lurking_ic"] = [{"id": "lc_tar", "type": "Tar Baby", "rating": 5,
                                "status": "lurking"}]
        mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6,
                              target_ic_id="lc_tar")
        assert mr._effective_steamroller(decker, state) == 0    # one-shot spent
        assert any(e["type"] == "one_shot_spent" for e in state["event_log"])
        # A second strike finds the Steamroller offline: manual use raises 400 (so the endpoint
        # never commits the spent action point) and leaves the second tar untouched.
        from fastapi import HTTPException
        state["lurking_ic"] = [{"id": "lc_tar2", "type": "Tar Baby", "rating": 5,
                                "status": "lurking"}]
        with pytest.raises(HTTPException) as exc:
            mr._apply_steamroller(state, decker, sec_code="Green", decker_pool=6,
                                  target_ic_id="lc_tar2")
        assert exc.value.status_code == 400
        assert "steamroller" in exc.value.detail.lower()
        assert state["lurking_ic"][0]["id"] == "lc_tar2"        # second tar untouched

    # -- (b) a non-one-shot copy of the same utility is unaffected -------------

    def test_non_one_shot_medic_only_degrades_by_one(self, scripted):
        scripted([6])
        decker = self._decker("medic", rating=6, one_shot=False)
        state = self._damaged_state()
        mr._apply_medic(state, decker)
        assert mr._effective_medic(decker, state) == 5          # normal -1 wear, NOT spent
        assert not any(e["type"] == "one_shot_spent" for e in state["event_log"])

    def test_spend_one_shot_is_idempotent(self):
        decker = self._decker("slow", rating=5, one_shot=True)
        state = _fresh_state(); state["event_log"] = []
        mr._spend_one_shot(state, decker, "slow")
        mr._spend_one_shot(state, decker, "slow")               # already spent -> no 2nd event
        spent = [e for e in state["event_log"] if e["type"] == "one_shot_spent"]
        assert len(spent) == 1
        assert state["program_damage"]["slow"] == 5

    def test_spend_one_shot_noop_for_non_one_shot(self):
        decker = self._decker("slow", rating=5, one_shot=False)
        state = _fresh_state(); state["event_log"] = []
        mr._spend_one_shot(state, decker, "slow")
        assert not state.get("program_damage")                  # untouched
        assert state["event_log"] == []

    # -- (c) Swap Memory reloads a spent one-shot -----------------------------

    def test_swap_memory_reloads_spent_one_shot(self, scripted):
        scripted([6])
        decker = self._decker("medic", rating=6, one_shot=True)
        state = self._damaged_state()
        mr._apply_medic(state, decker)
        assert mr._effective_medic(decker, state) == 0          # spent
        mr._apply_swap_memory(state, decker, target_program="medic", swap_out_program="")
        assert mr._effective_medic(decker, state) == 6          # fresh copy reloaded
        assert state["program_damage"].get("medic", 0) == 0

    # -- (d) Tar IC wipes EVERY copy ------------------------------------------

    def test_tar_wipe_corrupts_all_copies_and_clears_storage(self):
        decker = self._decker("attack", rating=6, one_shot=True)
        state = _fresh_state(); state["event_log"] = []
        state["storage_programs"] = [{"name": "attack", "rating": 6, "size": 4},
                                     {"name": "medic", "rating": 5, "size": 3}]
        mr._wipe_one_shot(state, decker, "Attack")              # spaced/cased name normalizes
        assert "attack" in state["one_shot_wiped"]
        assert state["program_damage"]["attack"] == 6
        # The wiped one-shot's storage copy is gone; the unrelated program survives.
        assert [p["name"] for p in state["storage_programs"]] == ["medic"]
        assert any(e["type"] == "one_shot_wiped" and e["utility"] == "attack"
                   for e in state["event_log"])

    def test_tar_wipe_noop_for_non_one_shot(self):
        decker = self._decker("attack", rating=6, one_shot=False)
        state = _fresh_state(); state["event_log"] = []
        mr._wipe_one_shot(state, decker, "attack")
        assert not state.get("one_shot_wiped")
        assert not state.get("program_damage")
        assert state["event_log"] == []

    def test_reactive_tar_resolution_wipes_one_shot(self, monkeypatch):
        # The live resolve_reactive_ic handler must call _wipe_one_shot when the tar wins: a
        # one-shot utility used against the tar is corrupted on every copy and cannot be reloaded.
        import asyncio
        from app.schemas.matrix_run import RunReactiveInput
        decker = self._decker("attack", rating=6, one_shot=True)
        state = _fresh_state(); state["event_log"] = []
        state["storage_programs"] = [{"name": "attack", "rating": 6, "size": 4}]
        state["lurking_ic"] = [{"id": "lc_tar", "type": "Tar Baby", "rating": 8,
                                "status": "lurking"}]

        class _StubRun:
            id = 9
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        def _fake_tar(**kw):
            return {"ic_wins": True, "ic_roll": {"successes": 3},
                    "util_roll": {"successes": 0}, "all_copies_corrupted": False}

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "tar_baby_test", _fake_tar)

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        body = RunReactiveInput(ic_id="lc_tar", utility_name="attack", utility_rating=6)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        result = asyncio.run(
            mr.resolve_reactive_ic(run_id=9, body=body, auth=auth, db=_FakeDB()))
        assert "attack" in result["one_shot_wiped"]
        assert result["program_damage"]["attack"] == 6
        assert result["storage_programs"] == []                 # storage copy wiped
        assert any(e["type"] == "one_shot_wiped" for e in result["event_log"])

    # -- (e) Swap Memory refuses to reload a tar-wiped one-shot ---------------

    def test_swap_memory_refuses_tar_wiped_reload(self):
        decker = self._decker("attack", rating=6, one_shot=True)
        state = _fresh_state(); state["event_log"] = []
        state["one_shot_wiped"] = ["attack"]
        state["program_damage"] = {"attack": 6}
        with pytest.raises(mr.HTTPException) as exc:
            mr._apply_swap_memory(state, decker, target_program="attack", swap_out_program="")
        assert exc.value.status_code == 400
        assert "tar" in exc.value.detail.lower()

    # -- (g) OFFENSIVE hard-gate: the attack/strike endpoints refuse a spent one-shot ----
    # The offensive endpoints (attack_ic / attack_enemy_decker) read the carried rating
    # directly, so they cannot lean on an _effective_* helper -- _one_shot_block enforces
    # "executes ONCE" for them explicitly (a spent / tar-wiped copy is refused before any roll).

    def test_one_shot_block_unit(self):
        decker = self._decker("attack", rating=6, one_shot=True)
        state = _fresh_state(); state["event_log"] = []
        mr._one_shot_block(state, decker, "attack")             # not yet spent -> no block
        state["program_damage"] = {"attack": 6}                 # spent (== base rating)
        with pytest.raises(mr.HTTPException) as exc:
            mr._one_shot_block(state, decker, "attack")
        assert exc.value.status_code == 400
        assert "spent" in exc.value.detail.lower()
        state["one_shot_wiped"] = ["attack"]                    # tar-wiped takes priority
        with pytest.raises(mr.HTTPException) as exc2:
            mr._one_shot_block(state, decker, "attack")
        assert exc2.value.status_code == 400
        assert "tar" in exc2.value.detail.lower()
        # A non-one-shot copy is never blocked, even when fully "spent".
        plain = self._decker("attack", rating=6, one_shot=False)
        s2 = _fresh_state(); s2["program_damage"] = {"attack": 6}
        mr._one_shot_block(s2, plain, "attack")                 # no raise

    def test_one_shot_attack_refused_on_second_enemy_strike(self, monkeypatch):
        import asyncio
        from app.schemas.matrix_run import RunEnemyAttackInput
        # Plain-attack resolution returns 0 boxes so the enemy stays active+revealed between strikes.
        monkeypatch.setattr(eng, "cybercombat_attack", lambda **kw: {
            "attack_roll": {"successes": 0, "ones": 0},
            "resistance": {"boxes": 0, "final_damage_level": "None"}})
        decker = self._decker("attack", rating=6, one_shot=True)
        state = _fresh_state(sec_code="Green", sec_value=4)
        state["event_log"] = []
        state["enemy_deckers"] = [{"id": "ed1", "name": "Red Decker", "status": "active",
                                   "revealed": True, "bod": 5,
                                   "condition_monitor": {"persona_boxes": 0}}]

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        inp = RunEnemyAttackInput(enemy_id="ed1", attack_pool=6, hacking_pool_dice=0,
                                  program="attack")
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        # First strike fires and spends the one-shot Attack.
        asyncio.run(mr.attack_enemy_decker(run_id=7, body=inp, auth=auth, db=_FakeDB()))
        assert run.state_json["program_damage"]["attack"] == 6
        assert any(e["type"] == "one_shot_spent" for e in run.state_json["event_log"])
        # Second strike is hard-refused before any roll -- the copy is gone from active memory.
        with pytest.raises(mr.HTTPException) as exc:
            asyncio.run(mr.attack_enemy_decker(run_id=7, body=inp, auth=auth, db=_FakeDB()))
        assert exc.value.status_code == 400
        assert "spent" in exc.value.detail.lower()

    def test_one_shot_attack_refused_on_second_ic_strike(self, monkeypatch):
        # Same one-shot enforcement on the IC-attack endpoint (attack_ic, util="attack"). attack_ic
        # resolves damage inline via eng.stage_damage (NOT eng.cybercombat_attack), so force a
        # sub-lethal Light hit: the Construct stays active between the two strikes, isolating the
        # one-shot gate. (A real roll can stage up to Deadly=10 and crash the IC on strike 1, which
        # would then trip the "already crashed" guard first -- the source of a prior RNG flake.)
        import asyncio
        from app.schemas.matrix_run import RunAttackInput
        monkeypatch.setattr(eng, "stage_damage", lambda *a, **k: "Light")
        decker = self._decker("attack", rating=6, one_shot=True)
        state = _fresh_state(sec_code="Green", sec_value=4)
        state["event_log"] = []
        state["active_ic"] = [{"id": "ic1", "type": "Construct", "rating": 4,
                               "status": "active", "boxes": 0, "cluster_id": None}]

        class _StubRun:
            id = 8
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        inp = RunAttackInput(target_ic_id="ic1", attack_pool=6, hacking_pool_dice=0)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        # First strike fires and spends the one-shot Attack.
        asyncio.run(mr.attack_ic(run_id=8, body=inp, auth=auth, db=_FakeDB()))
        assert run.state_json["program_damage"]["attack"] == 6
        assert any(e["type"] == "one_shot_spent" for e in run.state_json["event_log"])
        # Second strike is hard-refused before any roll -- reload via Swap Memory required.
        with pytest.raises(mr.HTTPException) as exc:
            asyncio.run(mr.attack_ic(run_id=8, body=inp, auth=auth, db=_FakeDB()))
        assert exc.value.status_code == 400
        assert "spent" in exc.value.detail.lower()


# -- DINAB ("Decker In A Box") program option (operational + offensive) ----------

class TestDINAB:
    """vr2_rules.md L1665 -- DINAB equips a utility with a built-in Computer skill = its DINAB
    rating, so the decker spends one Free Action to fire that ONE program autonomously (a "second
    ally") at skill = effective DINAB rating, alongside their own pass. Operational programs run a
    generic System Test; the six offensive utilities reuse cybercombat / crippler resolution. A
    failed run degrades DINAB (-1); a failed all-1s run CRASHES it (program_damage = base; reload
    via Swap Memory). Player-triggered, one run per trigger -- never a background auto-loop."""

    def _host(self):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6, "paydata": []}
            ltg_address = None
            trap_doors_json = None
        return _Host()

    def _decker(self, *, deception_dinab=4, attack_dinab=4):
        return {"masking": 4, "intelligence": 5, "mpcp": 6, "sensor": 4, "evasion": 4, "bod": 4,
                "computer_skill": 6, "hardening": 0, "storage_free_mp": -1,
                "utilities": {"deception": 5, "attack": 5, "analyze": 5},
                "program_options": {"deception": {"dinab": deception_dinab},
                                    "attack": {"dinab": attack_dinab}}}

    def _state(self, decker, *, active_ic=None, enemy_deckers=None):
        state = mr._initial_state(decker, self._host())
        state["logon_complete"] = True
        state["active_ic"] = active_ic or []
        state["enemy_deckers"] = enemy_deckers or []
        return state

    def _drive(self, monkeypatch, *, decker, state, action, op_success=True, all_ones=False):
        import asyncio

        def _fake_test(**kw):
            if op_success:
                return {"success": True, "decker_roll": {"successes": 3, "ones": 0, "pool": 4},
                        "host_roll": {"successes": 0}, "decker_net_successes": 3, "tally_increase": 0}
            dr = {"successes": 0, "ones": 4 if all_ones else 0, "pool": 4}
            return {"success": False, "decker_roll": dr, "host_roll": {"successes": 1},
                    "decker_net_successes": -1, "tally_increase": 1}

        def _fake_roll(pool, tn=4):
            ones = pool if all_ones else 0
            return {"successes": 0, "ones": ones, "pool": pool, "tn": tn, "rolls": []}

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "system_test", _fake_test)
        monkeypatch.setattr(eng, "roll_dice", _fake_roll)

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.perform_action(run_id=7, body=action, auth=auth, db=_FakeDB()))
        return run.state_json

    # -- effective rating gate -------------------------------------------------

    def test_effective_dinab_subtracts_wear_and_gates_offline(self):
        decker = self._decker()
        assert mr._effective_dinab(decker, {}, "attack") == 4
        assert mr._effective_dinab(decker, {"dinab_damage": {"attack": 2}}, "attack") == 2
        # Crashed program (program_damage >= base utility 5) -> DINAB cannot run it.
        assert mr._effective_dinab(decker, {"program_damage": {"attack": 5}}, "attack") == 0
        # Not DINAB-equipped utility -> 0.
        assert mr._effective_dinab(decker, {}, "analyze") == 0

    def test_offline_program_rejected(self, monkeypatch):
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker()
        state = self._state(decker)
        act = RunActionInput(action_type="dinab", subsystem="control", target_program="analyze")
        with pytest.raises(mr.HTTPException) as exc:
            self._drive(monkeypatch, decker=decker, state=state, action=act)
        assert exc.value.status_code == 400

    # -- free action economy ---------------------------------------------------

    def test_dinab_is_free_action(self, monkeypatch):
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker()
        state = self._state(decker)
        ap = state["pass_action_points"]
        act = RunActionInput(action_type="dinab", subsystem="control", target_program="deception")
        st = self._drive(monkeypatch, decker=decker, state=state, action=act)
        assert st["pass_action_points"] == ap          # Complex/Simple budget untouched
        assert st["pass_free"] == 0                     # only the Free was spent

    # -- operational route -----------------------------------------------------

    def test_operational_success_no_wear(self, monkeypatch):
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker()
        state = self._state(decker)
        act = RunActionInput(action_type="dinab", subsystem="control", target_program="deception")
        st = self._drive(monkeypatch, decker=decker, state=state, action=act, op_success=True)
        assert not st.get("dinab_damage")
        assert any(e["type"] == "dinab_op" and e["success"] for e in st["event_log"])

    def test_operational_fail_degrades(self, monkeypatch):
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker()
        state = self._state(decker)
        act = RunActionInput(action_type="dinab", subsystem="control", target_program="deception")
        st = self._drive(monkeypatch, decker=decker, state=state, action=act, op_success=False)
        assert st["dinab_damage"]["deception"] == 1
        assert any(e["type"] == "dinab_degraded" for e in st["event_log"])

    def test_operational_fail_all_ones_crashes(self, monkeypatch):
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker()
        state = self._state(decker)
        act = RunActionInput(action_type="dinab", subsystem="control", target_program="deception")
        st = self._drive(monkeypatch, decker=decker, state=state, action=act,
                         op_success=False, all_ones=True)
        assert st["program_damage"]["deception"] == 5          # base -> effective-0
        assert "deception" not in st.get("dinab_damage", {})
        assert any(e["type"] == "dinab_crashed" for e in st["event_log"])

    # -- offensive route -------------------------------------------------------

    def test_offensive_attack_degrades_on_miss(self, monkeypatch):
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker()
        ic = {"id": "ic1", "type": "Killer", "rating": 5, "status": "active", "boxes": 0}
        state = self._state(decker, active_ic=[ic])
        act = RunActionInput(action_type="dinab", subsystem="control", target_program="attack")
        st = self._drive(monkeypatch, decker=decker, state=state, action=act, all_ones=False)
        assert st["dinab_damage"]["attack"] == 1
        assert any(e["type"] == "dinab_attack" for e in st["event_log"])

    def test_offensive_attack_all_ones_crashes(self, monkeypatch):
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker()
        ic = {"id": "ic1", "type": "Killer", "rating": 5, "status": "active", "boxes": 0}
        state = self._state(decker, active_ic=[ic])
        act = RunActionInput(action_type="dinab", subsystem="control", target_program="attack")
        st = self._drive(monkeypatch, decker=decker, state=state, action=act, all_ones=True)
        assert st["program_damage"]["attack"] == 5
        assert any(e["type"] == "dinab_crashed" for e in st["event_log"])

    def test_offensive_attack_crashes_ic_and_bumps_tally(self, monkeypatch):
        """A hit that pushes the IC to 10 boxes CRASHES it: removed from play, tally rises, no
        DINAB wear (a success leaves the rating intact)."""
        decker = self._decker(attack_dinab=4)
        ic = {"id": "ic1", "type": "Killer", "rating": 5, "status": "active", "boxes": 9}
        state = self._state(decker, active_ic=[ic])
        monkeypatch.setattr(eng, "roll_dice", lambda pool, tn=4: {
            "successes": 6, "ones": 0, "pool": pool, "tn": tn, "rolls": []})
        before = state.get("security_tally", 0)
        failed, all_ones = mr._dinab_attack_ic(state, decker, ic, 4, "Green")
        assert (failed, all_ones) == (False, False)
        assert ic["status"] == "crashed"
        assert state["security_tally"] > before          # crash adds the IC rating to tally
        assert not state.get("dinab_damage")             # success: no degrade

    def test_crash_reloads_via_swap_memory(self, monkeypatch):
        """vr2: a crashed DINAB program reloads via Swap Memory. The crash sets program_damage to
        base (effective DINAB -> 0); a Mode-3 reload clears it and the autonomous skill returns."""
        from app.schemas.matrix_run import RunActionInput
        decker = self._decker()
        state = self._state(decker)
        act = RunActionInput(action_type="dinab", subsystem="control", target_program="deception")
        st = self._drive(monkeypatch, decker=decker, state=state, action=act,
                         op_success=False, all_ones=True)
        assert mr._effective_dinab(decker, st, "deception") == 0   # crashed
        mr._apply_swap_memory(st, decker, target_program="deception", swap_out_program="")
        assert st["program_damage"].get("deception", 0) == 0       # fresh copy
        assert mr._effective_dinab(decker, st, "deception") == 4   # DINAB restored


class TestSkulkCrashTally:
    """vr2_rules.md L1671 -- the Skulk option (book "Stealth") on the Attack utility reduces the
    security-tally increase from crashing IC: tally_increase = max(0, ic_rating - skulk). It is
    read automatically from decker.program_options['attack'].skulk (no manual entry). There is NO
    "Skulk>=6 -> 0" rule: a high-rating IC still leaks tally past the masking. Drives the real
    /attack crash path in app.routers.matrix_runs.attack_ic."""

    def _crash(self, monkeypatch, *, rating, skulk=None, attack_pool=12):
        import asyncio
        from app.schemas.matrix_run import RunAttackInput

        # Deterministic crash: attacker rolls a huge stage-up (-> Deadly = 6 boxes), IC resists
        # nothing. The IC starts at 5 boxes so the single Deadly hit reaches 11 >= 10 = crash.
        # The resist pool (Security Value 9) is < attack_pool, so it scores 0.
        def _fake_roll(pool, tn=4):
            return {"successes": 30 if pool >= attack_pool else 0, "ones": 0,
                    "rolls": [], "pool": pool, "tn": tn}
        monkeypatch.setattr(eng, "roll_dice", _fake_roll)

        decker = {"name": "Ghost", "mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                  "computer_skill": 8, "intelligence": 5, "body": 5, "hardening": 0,
                  "utilities": {"attack": 6}}
        if skulk is not None:
            decker["program_options"] = {"attack": {"skulk": skulk}}
        state = _fresh_state(sec_code="Red", sec_value=9)
        state["event_log"] = []
        state["active_ic"] = [{"id": "ic1", "type": "Killer", "rating": rating,
                               "status": "active", "boxes": 5}]

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self): pass
            async def refresh(self, obj): pass

        inp = RunAttackInput(target_ic_id="ic1", attack_pool=attack_pool, hacking_pool_dice=0)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.attack_ic(run_id=7, body=inp, auth=auth, db=_FakeDB()))
        ev = [e for e in run.state_json["event_log"] if e["type"] == "ic_crashed"][-1]
        return run.state_json, ev

    def test_skulk_reduces_tally_by_rating(self, monkeypatch):
        # Rating-10 IC, Skulk-8 -> tally +2 (not zeroed), masking note present.
        state, ev = self._crash(monkeypatch, rating=10, skulk=8)
        assert state["security_tally"] == 2
        assert ev["tally_increase"] == 2
        assert "Skulk-8 reduced the crash tally by 8" in ev["description"]

    def test_no_zeroing_at_six(self, monkeypatch):
        # NO "Skulk>=6 -> 0" bug: Rating-10 IC, Skulk-6 -> +4, the 6 does not eliminate the tally.
        state, ev = self._crash(monkeypatch, rating=10, skulk=6)
        assert ev["tally_increase"] == 4

    def test_skulk_floors_at_zero_never_negative(self, monkeypatch):
        # Skulk above the IC rating fully masks (0), never below zero.
        state, ev = self._crash(monkeypatch, rating=4, skulk=8)
        assert ev["tally_increase"] == 0
        assert state["security_tally"] == 0

    def test_no_skulk_adds_full_rating(self, monkeypatch):
        # No program_options at all -> full IC rating, no masking note.
        state, ev = self._crash(monkeypatch, rating=6, skulk=None)
        assert ev["tally_increase"] == 6
        assert "masked the crash" not in ev["description"]


class TestTargetingToHitTN:
    """vr2_rules.md L1673 -- the Targeting option gives -2 TN on attacks made with that utility.
    Read automatically from decker.program_options['attack'].targeting. It must lower ONLY the
    attacker's to-hit TN (not the IC's resist TN), clamp at 2 (rule-of-6 minimum), and not bleed
    into any other utility. Drives the real /attack path in app.routers.matrix_runs.attack_ic and
    captures the TN handed to each eng.roll_dice call (attack_pool=12 = to-hit, pool=9 = resist)."""

    def _attack(self, monkeypatch, *, targeting):
        import asyncio
        from app.schemas.matrix_run import RunAttackInput

        calls = []  # (pool, tn) per roll: pool 12 = to-hit, pool 9 = IC resist
        def _fake_roll(pool, tn=4):
            calls.append((pool, tn))
            return {"successes": 0, "ones": 0, "rolls": [], "pool": pool, "tn": tn}
        monkeypatch.setattr(eng, "roll_dice", _fake_roll)

        decker = {"name": "Ghost", "mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                  "computer_skill": 8, "intelligence": 5, "body": 5, "hardening": 0,
                  "utilities": {"attack": 6}}
        if targeting:
            decker["program_options"] = {"attack": {"targeting": True}}
        # Red host: COMBAT_TN Red-legitimate = 6, matching the resist Power (Attack Rating 6), so the
        # base to-hit TN equals the resist TN and the Targeting -2 shows up cleanly (no floor clamp).
        state = _fresh_state(sec_code="Red", sec_value=9)
        state["event_log"] = []
        state["active_ic"] = [{"id": "ic1", "type": "Killer", "rating": 6,
                               "status": "active", "boxes": 0}]

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self): pass
            async def refresh(self, obj): pass

        inp = RunAttackInput(target_ic_id="ic1", attack_pool=12, hacking_pool_dice=0)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.attack_ic(run_id=7, body=inp, auth=auth, db=_FakeDB()))
        to_hit_tn = next(tn for pool, tn in calls if pool == 12)
        resist_tn = next(tn for pool, tn in calls if pool == 9)
        return to_hit_tn, resist_tn

    def test_targeting_lowers_attacker_to_hit_by_two(self, monkeypatch):
        to_hit, _ = self._attack(monkeypatch, targeting=True)
        # without targeting the to-hit TN equals the resist TN; with targeting it is exactly 2 lower
        plain_hit, plain_resist = self._attack(monkeypatch, targeting=False)
        assert plain_hit == plain_resist
        assert to_hit == plain_hit - 2

    def test_targeting_does_not_touch_ic_resist(self, monkeypatch):
        _, resist_on = self._attack(monkeypatch, targeting=True)
        _, resist_off = self._attack(monkeypatch, targeting=False)
        assert resist_on == resist_off

    def test_no_targeting_to_hit_equals_resist(self, monkeypatch):
        to_hit, resist = self._attack(monkeypatch, targeting=False)
        assert to_hit == resist

    def test_to_hit_tn_floors_at_two(self, monkeypatch):
        to_hit, _ = self._attack(monkeypatch, targeting=True)
        assert to_hit >= 2


class TestPenetrationVsShield:
    """vr2_rules.md L681-682, L1668 -- the Penetration option defeats an IC's Shield (no +2 to-hit
    penalty), and Shift is EXTRA-effective against Penetration (+4 instead of +2). Read automatically
    from decker.program_options['attack'].penetration. Must change ONLY the attacker's to-hit TN
    (not the IC's resist TN). Drives the real /attack path (app.routers.matrix_runs.attack_ic) and
    captures the TN handed to each eng.roll_dice (attack_pool=12 = to-hit, sec_value=9 = resist)."""

    def _attack(self, monkeypatch, *, defense, penetration):
        import asyncio
        from app.schemas.matrix_run import RunAttackInput

        calls = []  # (pool, tn) per roll: pool 12 = to-hit, pool 9 = IC resist
        def _fake_roll(pool, tn=4):
            calls.append((pool, tn))
            return {"successes": 0, "ones": 0, "rolls": [], "pool": pool, "tn": tn}
        monkeypatch.setattr(eng, "roll_dice", _fake_roll)

        decker = {"name": "Ghost", "mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                  "computer_skill": 8, "intelligence": 5, "body": 5, "hardening": 0,
                  "utilities": {"attack": 6}}
        if penetration:
            decker["program_options"] = {"attack": {"penetration": True}}
        state = _fresh_state(sec_code="Red", sec_value=9)
        state["event_log"] = []
        ic = {"id": "ic1", "type": "Killer", "rating": 6, "status": "active", "boxes": 0}
        ic[defense] = True  # "shield" or "shift"
        state["active_ic"] = [ic]

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self): pass
            async def refresh(self, obj): pass

        inp = RunAttackInput(target_ic_id="ic1", attack_pool=12, hacking_pool_dice=0)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.attack_ic(run_id=7, body=inp, auth=auth, db=_FakeDB()))
        to_hit_tn = next(tn for pool, tn in calls if pool == 12)
        resist_tn = next(tn for pool, tn in calls if pool == 9)
        return to_hit_tn, resist_tn

    # Post-unification the IC resists with its Security Value dice vs a TN equal to the attack
    # Power (= the decker's Attack Rating, 6), so `resist` is CONSTANT: the Shield/Shift/
    # Penetration options move ONLY the to-hit TN. The PC attacks a legitimate host-resident IC,
    # so the base is COMBAT_TN Red-legitimate = 6.
    def test_shield_adds_two_without_penetration(self, monkeypatch):
        to_hit, resist = self._attack(monkeypatch, defense="shield", penetration=False)
        assert resist == 6 and to_hit == 6 + 2

    def test_penetration_negates_shield_penalty(self, monkeypatch):
        to_hit, resist = self._attack(monkeypatch, defense="shield", penetration=True)
        assert resist == 6 and to_hit == 6

    def test_penetration_is_extra_effective_against_shift(self, monkeypatch):
        to_hit, resist = self._attack(monkeypatch, defense="shift", penetration=True)
        assert resist == 6 and to_hit == 6 + 4

    def test_shift_adds_two_without_penetration(self, monkeypatch):
        to_hit, resist = self._attack(monkeypatch, defense="shift", penetration=False)
        assert resist == 6 and to_hit == 6 + 2


class TestChaserVsShift:
    """vr2_rules.md L681-682, L1664 -- the Chaser option defeats an IC's Shift (negates the +2
    to-hit penalty), while Shield is EXTRA-effective vs Chaser (+4 instead of +2). Cannot combine
    with Penetration. Read automatically from decker.program_options['attack'].chaser. Must change
    ONLY the attacker's to-hit TN, not the IC's resist TN. Drives the real /attack path
    (app.routers.matrix_runs.attack_ic): attack_pool=12 = to-hit, sec_value=9 = IC resist."""

    def _attack(self, monkeypatch, *, defense, chaser, penetration=False):
        import asyncio
        from app.schemas.matrix_run import RunAttackInput

        calls = []  # (pool, tn): pool 12 = to-hit, pool 9 = IC resist
        def _fake_roll(pool, tn=4):
            calls.append((pool, tn))
            return {"successes": 0, "ones": 0, "rolls": [], "pool": pool, "tn": tn}
        monkeypatch.setattr(eng, "roll_dice", _fake_roll)

        decker = {"name": "Ghost", "mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                  "computer_skill": 8, "intelligence": 5, "body": 5, "hardening": 0,
                  "utilities": {"attack": 6}}
        atk = {}
        if chaser: atk["chaser"] = True
        if penetration: atk["penetration"] = True
        if atk: decker["program_options"] = {"attack": atk}
        state = _fresh_state(sec_code="Red", sec_value=9)
        state["event_log"] = []
        ic = {"id": "ic1", "type": "Killer", "rating": 6, "status": "active", "boxes": 0}
        ic[defense] = True
        state["active_ic"] = [ic]

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self): pass
            async def refresh(self, obj): pass

        inp = RunAttackInput(target_ic_id="ic1", attack_pool=12, hacking_pool_dice=0)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.attack_ic(run_id=7, body=inp, auth=auth, db=_FakeDB()))
        to_hit_tn = next(tn for pool, tn in calls if pool == 12)
        resist_tn = next(tn for pool, tn in calls if pool == 9)
        return to_hit_tn, resist_tn

    # Post-unification `resist` == the attack Power (decker Attack Rating 6), CONSTANT; Chaser/
    # Shield/Penetration move ONLY the to-hit TN. The PC attacks a legitimate host-resident IC,
    # so the base is COMBAT_TN Red-legitimate = 6.
    def test_chaser_negates_shift_penalty(self, monkeypatch):
        to_hit, resist = self._attack(monkeypatch, defense="shift", chaser=True)
        assert resist == 6 and to_hit == 6

    def test_shift_adds_two_without_chaser(self, monkeypatch):
        to_hit, resist = self._attack(monkeypatch, defense="shift", chaser=False)
        assert resist == 6 and to_hit == 6 + 2

    def test_chaser_makes_shield_extra_effective(self, monkeypatch):
        to_hit, resist = self._attack(monkeypatch, defense="shield", chaser=True)
        assert resist == 6 and to_hit == 6 + 4

    def test_both_set_runtime_sane_shield_pen_wins(self, monkeypatch):
        # Defensive: if a legacy program somehow sends both, Penetration wins vs Shield (negates).
        to_hit, resist = self._attack(monkeypatch, defense="shield", chaser=True, penetration=True)
        assert resist == 6 and to_hit == 6


class TestAreaClusterToHit:
    """vr2_rules.md L1659-1670 -- the Area option lets one Attack Test cope with an IC cluster.
    In this single-target engine it offsets the cluster's to-hit penalty up to the Area rating
    (easing the attacker only); the IC's resist TN keeps the FULL cluster penalty. Read from
    decker.program_options['attack'].area. vr2 also makes Armor extra-effective vs an Area utility
    (+2 effective Armor). Drives the real /attack path (attack_pool=12 = to-hit, sec_value=9 = resist)."""

    def _attack(self, monkeypatch, *, area, cluster=2, armor=False):
        import asyncio
        from app.schemas.matrix_run import RunAttackInput

        calls = []  # (pool, tn): pool 12 = to-hit, pool 9 = IC resist
        def _fake_roll(pool, tn=4):
            calls.append((pool, tn))
            return {"successes": 0, "ones": 0, "rolls": [], "pool": pool, "tn": tn}
        monkeypatch.setattr(eng, "roll_dice", _fake_roll)

        decker = {"name": "Ghost", "mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                  "computer_skill": 8, "intelligence": 5, "body": 5, "hardening": 0,
                  "utilities": {"attack": 6}}
        if area:
            decker["program_options"] = {"attack": {"area": area}}
        # Red host: COMBAT_TN Red-legitimate = 6 equals the resist Power base (Attack Rating 6), so
        # the cluster-penalty offset reads cleanly against the resist TN (a legitimate resident IC).
        state = _fresh_state(sec_code="Red", sec_value=9)
        state["event_log"] = []
        cid = "c1" if cluster > 1 else None
        ic1 = {"id": "ic1", "type": "Killer", "rating": 6, "status": "active", "boxes": 0,
               "cluster_id": cid}
        if armor:
            ic1["options"] = ["Armor"]
        ics = [ic1]
        for n in range(1, cluster):
            ics.append({"id": f"ic{n+1}", "type": "Killer", "rating": 6, "status": "active",
                        "boxes": 0, "cluster_id": cid})
        state["active_ic"] = ics

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self): pass
            async def refresh(self, obj): pass

        inp = RunAttackInput(target_ic_id="ic1", attack_pool=12, hacking_pool_dice=0)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.attack_ic(run_id=7, body=inp, auth=auth, db=_FakeDB()))
        to_hit_tn = next(tn for pool, tn in calls if pool == 12)
        resist_tn = next(tn for pool, tn in calls if pool == 9)
        return to_hit_tn, resist_tn

    def test_area_offsets_cluster_to_hit_penalty(self, monkeypatch):
        # 2-IC cluster (+2 to-hit). Area-2 fully offsets it: to-hit drops back to the resist base.
        on_hit, on_resist = self._attack(monkeypatch, area=2, cluster=2)
        off_hit, off_resist = self._attack(monkeypatch, area=0, cluster=2)
        assert off_hit == off_resist            # no Area: cluster penalty hits both sides
        assert on_hit == off_hit - 2            # Area-2 removes the +2 to-hit penalty

    def test_area_caps_at_rating(self, monkeypatch):
        # Area-1 only buys back 1 of the 2-IC cluster penalty.
        on_hit, on_resist = self._attack(monkeypatch, area=1, cluster=2)
        assert on_hit == on_resist - 1

    def test_resist_tn_keeps_full_cluster_penalty(self, monkeypatch):
        on_resist = self._attack(monkeypatch, area=2, cluster=2)[1]
        off_resist = self._attack(monkeypatch, area=0, cluster=2)[1]
        assert on_resist == off_resist          # Area eases attacker only, never the IC resist

    def test_single_target_no_op_no_error(self, monkeypatch):
        # No cluster -> penalty 0; a high Area rating is a harmless no-op (no crash, no negative TN).
        to_hit, resist = self._attack(monkeypatch, area=4, cluster=1)
        assert to_hit == resist
        assert to_hit >= 2

    def test_armor_extra_effective_vs_area(self, monkeypatch):
        with_area = self._attack(monkeypatch, area=2, cluster=2, armor=True)[1]
        no_area = self._attack(monkeypatch, area=0, cluster=2, armor=True)[1]
        assert with_area == no_area - 2         # Area-armed strike resists 2 deeper vs Armor


class TestHungIcSuppression:
    """Correction #16 (vr2_rules.md L1578) -- a proactive IC that HANGS from a Slow strike (its
    passes drained to 0 for the turn; status stays "active" with a ``hung_turn`` marker) may be
    SUPPRESSED by the standard suppression rules, exactly like a crashed IC. Unlike a crash, a hang
    adds NO security tally, so suppressing OR releasing a hung IC must leave the tally untouched (the
    "appropriate amount" to defer / refund for a hang is 0). Suppressing a crashed IC must still
    refund its rating (regression guard). Drives the extracted pure helper
    ``mr._toggle_ic_suppression`` directly -- suppression never rolls dice, so no ``scripted`` fixture
    is needed."""

    def _decker(self):
        # Only what _effective_detection_factor reads (masking + sleaze); everything else defaults.
        return {"utilities": {"sleaze": 8}, "masking": 6, "persona_damage": {}}

    def _hung_ic(self, **over):
        ic = {"id": "ic1", "type": "Killer", "rating": 5, "status": "active",
              "initiative": 20, "actions_lost": 3, "slow_turn": 1, "hung_turn": 1,
              "suppressed": False}
        ic.update(over)
        return ic

    def _crashed_ic(self, **over):
        ic = {"id": "ic2", "type": "Killer", "rating": 4, "status": "crashed", "suppressed": False}
        ic.update(over)
        return ic

    def _state(self, ic, *, tally=0):
        st = _fresh_state()
        st["security_tally"] = tally
        st["active_ic"] = [ic]
        st["pass_free"] = 1
        st["event_log"] = []
        return st

    def test_suppress_hung_ic_leaves_tally_unchanged(self):
        ic = self._hung_ic()
        st = self._state(ic, tally=0)
        mr._toggle_ic_suppression(st, self._decker(), ic_id="ic1", release=False)
        assert ic["suppressed"] is True
        assert st["security_tally"] == 0            # Slow added no tally -> nothing to refund
        assert st["detection_factor"] == 6          # base ceil((6+8)/2)=7, -1 for the suppressed IC

    def test_suppress_crashed_ic_refunds_rating(self):
        ic = self._crashed_ic(rating=4)
        st = self._state(ic, tally=6)               # tally >= rating so the refund is visible
        mr._toggle_ic_suppression(st, self._decker(), ic_id="ic2", release=False)
        assert ic["suppressed"] is True
        assert st["security_tally"] == 2            # 6 - 4 crash-tally refund (crash path unbroken)

    def test_release_hung_ic_keeps_tally_and_costs_no_action(self):
        ic = self._hung_ic(suppressed=True)
        st = self._state(ic, tally=0)
        mr._toggle_ic_suppression(st, self._decker(), ic_id="ic1", release=True)
        assert ic["suppressed"] is False
        assert ic["suppression_released"] is True   # one-way: can never be re-suppressed
        assert st["security_tally"] == 0            # a hung IC re-adds nothing on release
        assert st["pass_free"] == 1                 # neither suppress nor release spends an action

    def test_suppress_plain_active_ic_is_rejected(self):
        import pytest
        from fastapi import HTTPException
        ic = {"id": "ic3", "type": "Killer", "rating": 5, "status": "active", "suppressed": False}
        st = self._state(ic, tally=0)
        with pytest.raises(HTTPException):          # neither crashed nor hung -> 400
            mr._toggle_ic_suppression(st, self._decker(), ic_id="ic3", release=False)


# -- #19 Combat maneuvers: Evade Detection / Parry Attack / Position Attack ------

class TestCombatManeuvers:
    """vr2_rules.md L1982-2000 (correction #19) -- the three combat maneuvers are opposed
    Evasion-vs-Sensor tests (eng.maneuver_test) available to the PC, IC, and revealed enemy
    deckers. The router state-transitions are validated with maneuver_test stubbed to a known
    win/loss; one case drives the real engine helper with scripted dice. These are the same pure
    helpers that perform_action, the IC loop, and the enemy-decker turn invoke."""

    @staticmethod
    def _mk_state(**over):
        st = {
            "current_turn": 1,
            "security_tally": 0,
            "host_security_value": 6,
            "active_ic": [],
            "enemy_deckers": [],
            "event_log": [],
            "condition_monitor": {"persona_boxes": 0},
            "npc_combat_maneuvers": True,
        }
        st.update(over)
        return st

    @staticmethod
    def _win(man_succ, opp_succ):
        """A stub eng.maneuver_test returning a fixed opposed-test outcome."""
        def _f(**kw):
            return {
                "maneuvering_roll": {"successes": man_succ, "ones": 0},
                "opposing_roll": {"successes": opp_succ, "ones": 0},
                "maneuvering_tn": kw.get("opposing_sensor_rating", 4),
                "opposing_tn": kw.get("maneuvering_evasion_rating", 4),
                "net_successes": max(0, man_succ - opp_succ),
                "success": man_succ > opp_succ,
            }
        return _f

    @staticmethod
    def _capture(man_succ, opp_succ, sink):
        """A maneuver_test stub that records the call kwargs into ``sink`` so a test can assert the
        router fed the correct Cloak / Lock-On modifiers to the shared opposed test."""
        def _f(**kw):
            sink.clear()
            sink.update(kw)
            return {
                "maneuvering_roll": {"successes": man_succ, "ones": 0},
                "opposing_roll": {"successes": opp_succ, "ones": 0},
                "maneuvering_tn": kw.get("opposing_sensor_rating", 4),
                "opposing_tn": kw.get("maneuvering_evasion_rating", 4),
                "net_successes": max(0, man_succ - opp_succ),
                "success": man_succ > opp_succ,
            }
        return _f

    @staticmethod
    def _body(action_type, **kw):
        from app.schemas.matrix_run import RunActionInput
        return RunActionInput(action_type=action_type, subsystem="control", **kw)

    _EFF = {"evasion": 5, "sensor": 5}

    def _ic(self, **over):
        ic = {"id": "ic1", "type": "Barrier", "rating": 5, "status": "active"}
        ic.update(over)
        return ic

    # -- Evade Detection -------------------------------------------------------

    def test_pc_evade_hides_target_and_sets_redetect_timer(self, monkeypatch):
        ic = self._ic()
        st = self._mk_state(active_ic=[ic], current_turn=2, security_tally=1)
        monkeypatch.setattr(eng, "maneuver_test", self._win(4, 1))     # net 3, PC wins
        mr._apply_maneuver(st, {}, self._EFF, self._body("evade_detection", maneuver_target="ic1"))
        assert ic["evaded"] is True and ic["evade_dir"] == "lost_pc"
        assert ic["redetect_turn"] == 2 + 3                            # current_turn + net successes
        assert ic["redetect_tally_base"] == 1
        assert any(e["type"] == "maneuver" and e["maneuver"] == "evade_detection" and e["success"]
                   for e in st["event_log"])

    def test_evaded_icon_is_hidden_until_timer_then_redetected(self, monkeypatch):
        ic = self._ic(evaded=True, evade_dir="lost_pc", redetect_turn=5, redetect_tally_base=0)
        st = self._mk_state(active_ic=[ic], current_turn=2, security_tally=0)
        assert mr._evade_turns_remaining(st, ic) == 3                  # 5 - 2 - 0
        assert mr._evade_active(st, ic) is True                        # the IC loop skips it
        st["current_turn"] = 5                                         # window elapsed
        assert mr._evade_active(st, ic) is False
        assert not ic.get("evaded")                                    # markers cleared on re-detect

    def test_security_tally_shortens_the_evasion_window(self):
        ic = self._ic(evaded=True, evade_dir="lost_pc", redetect_turn=5, redetect_tally_base=0)
        st = self._mk_state(active_ic=[ic], current_turn=2, security_tally=3)
        # 5 - 2 - 3 = 0 -> each tally point gained since evading shortens the window by a turn (vr2).
        assert mr._evade_turns_remaining(st, ic) <= 0
        assert mr._evade_active(st, ic) is False

    def test_cannot_evade_reactive_trace_ic_in_location_cycle(self, monkeypatch):
        # A trace that has vanished into its (un-located) location cycle is not a selectable
        # maneuver target, so the maneuver is rejected as having no eligible icon.
        ic = self._ic(id="tr1", type="Trace", trace_phase="locate")
        st = self._mk_state(active_ic=[ic])
        monkeypatch.setattr(eng, "maneuver_test", self._win(4, 0))
        with pytest.raises(HTTPException) as exc:
            mr._apply_maneuver(st, {}, self._EFF, self._body("evade_detection", maneuver_target="tr1"))
        assert exc.value.status_code == 400

    def test_maneuver_with_no_eligible_target_is_rejected(self):
        st = self._mk_state()                                          # no IC, no revealed enemy
        with pytest.raises(HTTPException) as exc:
            mr._apply_maneuver(st, {}, self._EFF, self._body("parry_attack"))
        assert exc.value.status_code == 400

    # -- Parry Attack ----------------------------------------------------------

    def test_pc_parry_raises_targets_next_attack_tn_then_consumed(self, monkeypatch):
        ic = self._ic()
        st = self._mk_state(active_ic=[ic])
        monkeypatch.setattr(eng, "maneuver_test", self._win(3, 1))     # net 2, PC wins
        mr._apply_maneuver(st, {}, self._EFF, self._body("parry_attack", maneuver_target="ic1"))
        assert st["pc_parry"] == {"vs": "ic1", "bonus": 2}
        tn_delta, power_delta = mr._consume_attack_mods_vs_pc(st, ic)  # the IC's next attack on the PC
        assert tn_delta == 2 and power_delta == 0
        assert st.get("pc_parry") is None                             # consumed by that attack

    def test_npc_parry_raises_pcs_next_attack_tn_then_consumed(self):
        ic = self._ic(parry_tn_bonus=3)
        st = self._mk_state(active_ic=[ic])
        tn_delta, power_delta = mr._consume_attack_mods_vs_target(st, ic)   # the PC's next attack on it
        assert tn_delta == 3 and power_delta == 0
        assert "parry_tn_bonus" not in ic

    # -- Position Attack -------------------------------------------------------

    def test_pc_position_tn_choice_lowers_next_attack_tn(self, monkeypatch):
        ic = self._ic()
        st = self._mk_state(active_ic=[ic])
        monkeypatch.setattr(eng, "maneuver_test", self._win(3, 1))     # net 2, PC wins
        mr._apply_maneuver(st, {}, self._EFF,
                           self._body("position_attack", maneuver_target="ic1", position_choice="tn"))
        assert st["pc_position"] == {"tn_reduction": 2}
        tn_delta, power_delta = mr._consume_attack_mods_vs_target(st, ic)
        assert tn_delta == -2 and power_delta == 0
        assert st.get("pc_position") is None

    def test_pc_position_power_choice_raises_next_attack_power(self, monkeypatch):
        ic = self._ic()
        st = self._mk_state(active_ic=[ic])
        monkeypatch.setattr(eng, "maneuver_test", self._win(4, 1))     # net 3, PC wins
        mr._apply_maneuver(st, {}, self._EFF,
                           self._body("position_attack", maneuver_target="ic1", position_choice="power"))
        assert st["pc_position"] == {"power_bonus": 3}
        tn_delta, power_delta = mr._consume_attack_mods_vs_target(st, ic)
        assert tn_delta == 0 and power_delta == 3

    def test_position_attack_backfires_to_the_opposing_icon(self, monkeypatch):
        ic = self._ic()
        st = self._mk_state(active_ic=[ic])
        monkeypatch.setattr(eng, "maneuver_test", self._win(1, 3))     # opposing wins by 2 (risky)
        mr._apply_maneuver(st, {}, self._EFF, self._body("position_attack", maneuver_target="ic1"))
        assert ic["position_bonus"] == {"tn_reduction": 2}
        tn_delta, power_delta = mr._consume_attack_mods_vs_pc(st, ic)  # IC attacks the PC at -2 TN
        assert tn_delta == -2 and power_delta == 0
        assert "position_bonus" not in ic

    # -- NPC-initiated maneuvers (full NPC use; gated by npc_combat_maneuvers) --

    def test_badly_wounded_ic_evades_to_break_off(self, monkeypatch):
        ic = self._ic(boxes=8)
        st = self._mk_state(active_ic=[ic])
        monkeypatch.setattr(eng, "maneuver_test", self._win(3, 1))
        assert mr._npc_maybe_maneuver(st, {}, self._EFF, ic, is_ic=True) is True
        assert ic["evaded"] is True and ic["evade_dir"] == "hid_from_pc"

    def test_moderately_wounded_ic_parries(self, monkeypatch):
        ic = self._ic(boxes=5)
        st = self._mk_state(active_ic=[ic])
        monkeypatch.setattr(eng, "maneuver_test", self._win(3, 1))     # net 2
        assert mr._npc_maybe_maneuver(st, {}, self._EFF, ic, is_ic=True) is True
        assert ic["parry_tn_bonus"] == 2

    def test_healthy_ic_seizes_position_when_pc_is_hurt(self, monkeypatch):
        ic = self._ic(boxes=2)
        st = self._mk_state(active_ic=[ic], condition_monitor={"persona_boxes": 3})
        monkeypatch.setattr(eng, "maneuver_test", self._win(3, 1))     # net 2
        assert mr._npc_maybe_maneuver(st, {}, self._EFF, ic, is_ic=True) is True
        assert ic["position_bonus"] == {"tn_reduction": 2}

    def test_npc_maneuvers_are_dormant_when_flag_is_off(self):
        ic = self._ic(boxes=8)
        st = self._mk_state(active_ic=[ic], npc_combat_maneuvers=False)
        assert mr._npc_maybe_maneuver(st, {}, self._EFF, ic, is_ic=True) is False
        assert not ic.get("evaded")

    # -- Enemy-decker parity (revealed enemy deckers, is_ic=False) -------------

    def test_pc_can_maneuver_against_a_revealed_enemy_decker(self, monkeypatch):
        enemy = {"id": "e1", "name": "Cutter", "sensor": 4, "evasion": 4,
                 "status": "active", "revealed": True}
        st = self._mk_state(enemy_deckers=[enemy])
        monkeypatch.setattr(eng, "maneuver_test", self._win(3, 1))     # net 2, PC wins
        mr._apply_maneuver(st, {}, self._EFF, self._body("parry_attack"))  # blank -> first eligible
        assert st["pc_parry"] == {"vs": "e1", "bonus": 2}

    def test_unrevealed_enemy_decker_is_not_a_valid_target(self):
        enemy = {"id": "e1", "name": "Cutter", "sensor": 4, "evasion": 4,
                 "status": "active", "revealed": False}
        st = self._mk_state(enemy_deckers=[enemy])
        with pytest.raises(HTTPException):
            mr._apply_maneuver(st, {}, self._EFF, self._body("parry_attack", maneuver_target="e1"))

    def test_badly_wounded_healless_enemy_decker_stands_and_fights(self, monkeypatch):
        # Enemy-decker DIVERGENCE from IC (Task 4): the "badly wounded -> Evade Detection" branch is
        # IC-ONLY. A healless enemy decker gains nothing by hiding, so _npc_maybe_maneuver leaves it
        # to stand and fight -- breaking off (and Medic-carrier hide-to-heal) is handled earlier in
        # the wounded-AI loop of _enemy_decker_take_turn, not here.
        enemy = {"id": "e1", "name": "Cutter", "sensor": 4, "evasion": 4, "status": "active",
                 "revealed": True, "condition_monitor": {"persona_boxes": 8}}
        st = self._mk_state(enemy_deckers=[enemy])
        monkeypatch.setattr(eng, "maneuver_test", self._win(3, 1))
        assert mr._npc_maybe_maneuver(st, {}, self._EFF, enemy, is_ic=False) is False
        assert not enemy.get("evaded")                         # did NOT slip off sensors
        assert enemy.get("revealed") is True                   # still in view, still fighting

    # -- Engine opposed test (real eng.maneuver_test, scripted dice) -----------

    def test_maneuver_test_requires_a_strict_win_and_reports_net(self, monkeypatch):
        # maneuvering rolls 5,5,5 (>= TN 4) = 3 successes; opposing rolls 2,2,2 = 0 -> net 3, win.
        monkeypatch.setattr(eng, "random", _ScriptedRandom([5, 5, 5, 2, 2, 2]))
        res = eng.maneuver_test(maneuvering_evasion_dice=3, maneuvering_evasion_rating=4,
                                opposing_sensor_dice=3, opposing_sensor_rating=4)
        assert res["success"] is True and res["net_successes"] == 3
        # A tie is NOT a win (vr2: the maneuvering icon must roll strictly more successes).
        monkeypatch.setattr(eng, "random", _ScriptedRandom([5, 2, 2, 5, 2, 2]))
        tie = eng.maneuver_test(maneuvering_evasion_dice=3, maneuvering_evasion_rating=4,
                                opposing_sensor_dice=3, opposing_sensor_rating=4)
        assert tie["success"] is False and tie["net_successes"] == 0

    # -- Cloak / Lock-On utility plumbing (parity: read from whichever side carries them) --

    def test_pc_cloak_lowers_its_evasion_tn_and_an_ic_target_grants_no_lock_on(self, monkeypatch):
        # Cloak aids the MANEUVERING side (the PC here) -> passed as `cloak`; an IC carries no Lock-On.
        seen: dict = {}
        ic = self._ic()
        st = self._mk_state(active_ic=[ic])
        monkeypatch.setattr(eng, "maneuver_test", self._capture(3, 1, seen))
        decker = {"utilities": {"cloak": 3, "lock_on": 9}}   # the PC's own Lock-On is irrelevant when IT maneuvers
        mr._apply_maneuver(st, decker, self._EFF, self._body("parry_attack", maneuver_target="ic1"))
        assert seen["cloak"] == 3        # the PC maneuvers, so its Cloak lowers its Evasion-test TN
        assert seen["lock_on"] == 0      # the opposing IC has no Lock-On to raise that TN

    def test_pc_maneuver_reads_the_opposing_enemy_deckers_lock_on(self, monkeypatch):
        seen: dict = {}
        enemy = {"id": "e1", "name": "Cutter", "sensor": 4, "evasion": 4, "status": "active",
                 "revealed": True, "utilities": {"lock_on": 4}}
        st = self._mk_state(enemy_deckers=[enemy])
        monkeypatch.setattr(eng, "maneuver_test", self._capture(3, 1, seen))
        decker = {"utilities": {"cloak": 2}}
        mr._apply_maneuver(st, decker, self._EFF, self._body("parry_attack", maneuver_target="e1"))
        assert seen["cloak"] == 2        # PC (maneuvering) Cloak
        assert seen["lock_on"] == 4      # the opposing enemy decker's Lock-On is read from ITS utilities

    def test_npc_enemy_decker_maneuver_uses_its_own_cloak_and_the_pcs_lock_on(self, monkeypatch):
        seen: dict = {}
        enemy = {"id": "e1", "name": "Cutter", "sensor": 4, "evasion": 4, "status": "active",
                 "revealed": True, "utilities": {"cloak": 5, "lock_on": 9}}
        st = self._mk_state(enemy_deckers=[enemy])
        monkeypatch.setattr(eng, "maneuver_test", self._capture(3, 1, seen))
        decker = {"utilities": {"lock_on": 3}}
        mr._resolve_npc_maneuver(st, decker, self._EFF, enemy, "parry_attack", is_ic=False)
        assert seen["cloak"] == 5        # the NPC maneuvers -> its OWN Cloak
        assert seen["lock_on"] == 3      # the PC opposes -> the PC's Lock-On (the enemy's own lock_on 9 is unused)

    def test_npc_ic_maneuver_carries_no_cloak_but_the_pcs_lock_on_still_applies(self, monkeypatch):
        seen: dict = {}
        ic = self._ic()
        st = self._mk_state(active_ic=[ic])
        monkeypatch.setattr(eng, "maneuver_test", self._capture(3, 1, seen))
        decker = {"utilities": {"lock_on": 2}}
        mr._resolve_npc_maneuver(st, decker, self._EFF, ic, "parry_attack", is_ic=True)
        assert seen["cloak"] == 0        # IC carry no utilities
        assert seen["lock_on"] == 2      # the PC's Lock-On helps it hold the lock on the evading IC

    def test_maneuver_test_cloak_and_lock_on_reduce_the_tns_and_floor_at_two(self, monkeypatch):
        # Cloak lowers the maneuvering icon's Evasion-test TN (vs the opposing Sensor Rating);
        # Lock-On lowers the opposing icon's Sensor-test TN (vs the maneuvering Evasion Rating).
        monkeypatch.setattr(eng, "random", _ScriptedRandom([1]))   # dice irrelevant; we assert the TNs
        res = eng.maneuver_test(maneuvering_evasion_dice=1, maneuvering_evasion_rating=6,
                                opposing_sensor_dice=1, opposing_sensor_rating=7,
                                cloak=3, lock_on=2)
        assert res["maneuvering_tn"] == 7 - 3      # opposing Sensor Rating 7 - Cloak 3
        assert res["opposing_tn"] == 6 - 2         # maneuvering Evasion Rating 6 - Lock-On 2
        # Both TNs floor at 2 no matter how large the modifier.
        floored = eng.maneuver_test(maneuvering_evasion_dice=1, maneuvering_evasion_rating=3,
                                    opposing_sensor_dice=1, opposing_sensor_rating=3,
                                    cloak=99, lock_on=99)
        assert floored["maneuvering_tn"] == 2 and floored["opposing_tn"] == 2


class TestLocateReDetect:
    """vr2_rules.md L1884/L1880 + L1998-1999 (correction #5, user ruling) -- Locate IC and Locate
    Decker are the re-detect operations for an icon that slipped the decker with an Evade
    Detection maneuver (evade_dir == "hid_from_pc"). They re-acquire ONLY evaded icons, never
    never-seen ones (which betray themselves by acting). Locate IC is a System Test only; Locate
    Decker keeps the #6 opposed Sensor Test vs FULL Masking + Sleaze. A hit clears the evade so
    the icon is visible/actionable again. These drive the pure _apply_locate_* helpers that
    perform_action dispatches to."""

    @staticmethod
    def _state(**over):
        st = {"current_turn": 3, "security_tally": 0,
              "active_ic": [], "enemy_deckers": [], "event_log": []}
        st.update(over)
        return st

    @staticmethod
    def _evaded_ic(**over):
        ic = {"id": "ic1", "type": "Trace", "rating": 5, "status": "active",
              "detection_level": 3, "evaded": True, "evade_dir": "hid_from_pc",
              "redetect_turn": 99, "redetect_tally_base": 0}
        ic.update(over)
        return ic

    @staticmethod
    def _evaded_decker(**over):
        e = {"id": "d1", "name": "Ghost", "tier": 2, "status": "active", "revealed": False,
             "masking": 4, "evasion": 4, "utilities": {"sleaze": 2},
             "evaded": True, "evade_dir": "hid_from_pc",
             "redetect_turn": 99, "redetect_tally_base": 0}
        e.update(over)
        return e

    # -- Locate IC (System Test only) ------------------------------------------

    def test_locate_ic_redetects_evaded_ic(self):
        ic = self._evaded_ic()
        st = self._state(active_ic=[ic])
        mr._apply_locate_ic(st, test_success=True)
        assert "evaded" not in ic and "evade_dir" not in ic          # evade cleared -> visible again
        assert any(e.get("type") == "maneuver" and e.get("maneuver") == "re_detect"
                   for e in st["event_log"])

    def test_locate_ic_failed_test_leaves_ic_hidden(self):
        ic = self._evaded_ic()
        st = self._state(active_ic=[ic])
        mr._apply_locate_ic(st, test_success=False)
        assert ic["evaded"] is True and ic["evade_dir"] == "hid_from_pc"   # still hidden
        assert any(e.get("type") == "ic_relocate" and e.get("outcome") == "fail"
                   for e in st["event_log"])

    def test_locate_ic_no_evaded_ic_reports_none(self):
        # A visible (non-evaded) IC must NOT be affected -- Locate IC only re-detects evaded IC.
        ic = {"id": "ic1", "type": "Killer", "rating": 6, "status": "active", "detection_level": 3}
        st = self._state(active_ic=[ic])
        mr._apply_locate_ic(st, test_success=True)
        assert "evaded" not in ic
        assert any(e.get("type") == "ic_relocate" and e.get("outcome") == "none"
                   for e in st["event_log"])

    # -- Locate Decker (Index test + #6 opposed Sensor test) -------------------

    def test_locate_decker_redetects_evaded_decker(self, monkeypatch):
        e = self._evaded_decker()
        st = self._state(enemy_deckers=[e])
        monkeypatch.setattr(eng, "pc_locate_decker_test",
                            lambda **kw: {"located": True, "net_successes": 2,
                                          "target_tn": kw["enemy_mask_sleaze"]})
        mr._apply_locate_decker(st, {"sensor": 5}, test_success=True, scanner=0)
        assert "evaded" not in e and e["revealed"] is True           # back in view, can Strike Back
        assert any(ev.get("type") == "enemy_decker" and ev.get("outcome") == "scan_hit"
                   for ev in st["event_log"])

    def test_locate_decker_uses_full_mask_plus_sleaze(self, monkeypatch):
        # #6 preserved: the opposed test receives FULL masking + sleaze (4 + 2 = 6), not halved.
        e = self._evaded_decker(masking=4, utilities={"sleaze": 2})
        st = self._state(enemy_deckers=[e])
        seen = {}
        def _cap(**kw):
            seen.update(kw)
            return {"located": True, "net_successes": 1, "target_tn": kw["enemy_mask_sleaze"]}
        monkeypatch.setattr(eng, "pc_locate_decker_test", _cap)
        mr._apply_locate_decker(st, {"sensor": 5}, test_success=True, scanner=3)
        assert seen["enemy_mask_sleaze"] == 6 and seen["scanner_rating"] == 3

    def test_locate_decker_ignores_never_revealed_hunter(self, monkeypatch):
        # User ruling: an unrevealed hunter that has NOT evaded is not a valid target -- only
        # evaded deckers are re-acquired (else you'd discover everything in a system instantly).
        hunter = {"id": "d9", "name": "Hunter", "tier": 3, "status": "active", "revealed": False,
                  "masking": 4, "evasion": 4, "utilities": {}}
        st = self._state(enemy_deckers=[hunter])
        calls = []
        monkeypatch.setattr(eng, "pc_locate_decker_test",
                            lambda **kw: calls.append(kw) or {"located": True, "net_successes": 1,
                                                              "target_tn": 4})
        mr._apply_locate_decker(st, {"sensor": 5}, test_success=True, scanner=0)
        assert calls == [] and hunter["revealed"] is False           # never touched
        assert any(ev.get("type") == "enemy_decker" and ev.get("outcome") == "scan_clear"
                   for ev in st["event_log"])

    def test_locate_decker_failed_sensor_leaves_decker_evaded(self, monkeypatch):
        e = self._evaded_decker()
        st = self._state(enemy_deckers=[e])
        monkeypatch.setattr(eng, "pc_locate_decker_test",
                            lambda **kw: {"located": False, "net_successes": 0, "target_tn": 6})
        mr._apply_locate_decker(st, {"sensor": 3}, test_success=True, scanner=0)
        assert e["evaded"] is True and e["revealed"] is False         # still hidden
        assert any(ev.get("type") == "enemy_decker" and ev.get("outcome") == "scan_fail"
                   for ev in st["event_log"])

    def test_locate_decker_failed_index_test_skips_sensor(self, monkeypatch):
        # The Index System Test failed -> no opposed Sensor Test is even attempted.
        e = self._evaded_decker()
        st = self._state(enemy_deckers=[e])
        calls = []
        monkeypatch.setattr(eng, "pc_locate_decker_test",
                            lambda **kw: calls.append(kw) or {"located": True})
        mr._apply_locate_decker(st, {"sensor": 5}, test_success=False, scanner=0)
        assert calls == [] and e["evaded"] is True
        assert any(ev.get("type") == "enemy_decker" and ev.get("outcome") == "scan_fail"
                   for ev in st["event_log"])


class TestDownloadMultiTurn:
    """vr2_rules.md L1256-1266 / L1873 / L992 + L1512-1515 (correction #10, user rulings) --
    Download Data is an ONGOING operation transferring at the deck's I/O Speed, not an instant
    grab. Turns to transfer = ceil(stored_Mp / io_speed) where ``stored`` is the SAME
    compressor-effective footprint the file occupies on the deck (a Compressor within its
    Rating x 100 Mp cap halves what must move; an oversized file transfers full). A file that fits
    one turn's bandwidth lands immediately; a larger one runs as a BACKGROUND transfer that
    auto-rolls a Null Operation (Control System Test, Computer skill, NO Hacking Pool) each turn --
    its host Security Test raises the tally like any op and can wake the sheaf. While a transfer
    runs the deck's Complex action is committed to that Null Op, so the decker may take only FREE
    actions and cannot start a second download. Ending the run early (log off / dump / host crash)
    before completion CORRUPTS the partial copy -- no storage charged, no paydata credited (a
    Paydata Point needs the COMPLETE file). The ``/3`` duration the doc floated is NOT in RAW and is
    deliberately rejected: this app's io_speed field is already Mp per Combat Turn (schema L84).

    These drive the pure module helpers (_download_turns / _complete_download / _auto_null_operation
    / _corrupt_active_download / _tick_active_download) plus the perform_action / new_turn /
    graceful_logoff wiring."""

    # -- fixtures --------------------------------------------------------------

    @staticmethod
    def _decker(io_speed=40, compressor=0, storage_free=1000, computer=6):
        d = {"name": "Jax", "mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
             "intelligence": 6, "computer_skill": computer, "io_speed": io_speed,
             "storage_free_mp": storage_free, "utilities": {}}
        if compressor:
            d["utilities"]["compressor"] = compressor
        return d

    @staticmethod
    def _host(paydata, sec_code="Green", sec_value=6):
        class _Host:
            config_json = {"security_code": sec_code, "security_value": sec_value,
                           "acifs": [6, 6, 6, 6, 6], "paydata": paydata}
            ltg_address = None
            trap_doors_json = None
        return _Host()

    def _state(self, paydata, *, io_speed=40, compressor=0, storage_free=1000):
        decker = self._decker(io_speed=io_speed, compressor=compressor, storage_free=storage_free)
        st = mr._initial_state(decker, self._host(paydata))
        st["logon_complete"] = True
        # These tests exercise per-Combat-Turn download mechanics; pin the decker to a single
        # initiative pass so one End Turn ends the whole Combat Turn (End Turn now only ends the
        # turn on the decker's LAST pass -- _initial_state otherwise rolls a random pass count).
        st["initiative_passes"] = 1
        return st, decker

    class _FakeDB:
        async def commit(self):
            pass

        async def refresh(self, obj):
            pass

    def _run_action(self, monkeypatch, st, decker, *, action_type, target_file="", success=True):
        """Drive the REAL perform_action against a stub run (mirrors the other /action harnesses).
        eng.system_test is stubbed deterministic. Returns the post-action state_json."""
        import asyncio
        from app.schemas.matrix_run import RunActionInput

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = None
            state_json = None

        run = _StubRun()
        run.decker_json = decker
        run.state_json = st

        async def _fake_get_run(db, run_id):
            return run

        def _fake_test(**kw):
            if success:
                return {"success": True, "decker_roll": {"successes": 3, "ones": 0},
                        "host_roll": {"successes": 0}, "decker_net_successes": 3, "tally_increase": 0}
            return {"success": False, "decker_roll": {"successes": 0, "ones": 0},
                    "host_roll": {"successes": 3}, "decker_net_successes": -3, "tally_increase": 0}

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "system_test", _fake_test)
        inp = RunActionInput(action_type=action_type, subsystem="files",
                             utility_rating=0, hacking_pool_dice=0, target_file=target_file)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.perform_action(run_id=7, body=inp, auth=auth, db=self._FakeDB()))
        return run.state_json

    def _run_new_turn(self, monkeypatch, st, decker, *, tally_increase=0):
        """Drive the REAL new_turn (which ticks an active download) against a stub run."""
        import asyncio

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = None
            state_json = None

        run = _StubRun()
        run.decker_json = decker
        run.state_json = st

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "system_test",
                            lambda **kw: {"success": True, "decker_roll": {"successes": 1},
                                          "host_roll": {"successes": 0},
                                          "tally_increase": tally_increase})
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.new_turn(run_id=7, auth=auth, db=self._FakeDB()))
        return run.state_json

    # -- _download_turns: ceil(stored / io_speed) ------------------------------

    def test_download_turns_is_ceiling_of_stored_over_io(self):
        assert mr._download_turns({"io_speed": 40}, 140) == 4   # ceil(140/40) = 3.5 -> 4
        assert mr._download_turns({"io_speed": 40}, 120) == 3   # exact multiple
        assert mr._download_turns({"io_speed": 40}, 40) == 1    # one turn's bandwidth
        assert mr._download_turns({"io_speed": 40}, 41) == 2    # one Mp over -> a second turn

    def test_download_turns_legacy_deck_transfers_instantly(self):
        # A deck with no configured I/O Speed (<=0) keeps the old instant-download behaviour.
        assert mr._download_turns({"io_speed": 0}, 500) == 1
        assert mr._download_turns({}, 500) == 1
        # Nothing to move is also a single (no-op) turn, never zero or negative.
        assert mr._download_turns({"io_speed": 100}, 0) == 1

    # -- Compressor drives the transfer size (vr2 L1512-1515) ------------------

    def test_compressor_halves_transfer_size_within_cap(self):
        # Rating 3 -> 300 Mp cap. A 200 Mp file compresses to 100 (halved, rounded up).
        assert mr._compressed_store_size(3, 200) == (100, True)
        # Over the Rating x 100 cap the file transfers/stores FULL (not compressible).
        assert mr._compressed_store_size(3, 400) == (400, False)
        # No Compressor loaded -> always full size.
        assert mr._compressed_store_size(0, 200) == (200, False)
        # ...and the halved footprint is exactly what shortens the transfer.
        assert mr._download_turns({"io_speed": 50}, 100) == 2   # compressed 100 Mp
        assert mr._download_turns({"io_speed": 50}, 200) == 4   # full 200 Mp

    # -- _complete_download: land file, charge storage, ledger + event ---------

    def test_complete_download_lands_file_and_charges_storage(self):
        st, decker = self._state([{"name": "Payroll DB", "density": 120, "is_key": True}])
        pd = st["paydata"][0]
        mr._complete_download(st, decker, pd)
        assert pd["downloaded"] is True and pd["located"] is True
        assert st["storage_used_mp"] == 120                     # no compressor -> full 120 Mp
        assert len(st["downloaded_files"]) == 1
        entry = st["downloaded_files"][0]
        assert entry["name"] == "Payroll DB" and entry["size_mp"] == 120 and entry["is_key"] is True
        assert st["event_log"][-1]["type"] == "data_downloaded"

    def test_complete_download_is_idempotent(self):
        # The guard (``if pd.get("downloaded"): return``) prevents a double charge if called twice.
        st, decker = self._state([{"name": "F", "density": 60}])
        pd = st["paydata"][0]
        mr._complete_download(st, decker, pd)
        mr._complete_download(st, decker, pd)
        assert st["storage_used_mp"] == 60 and len(st["downloaded_files"]) == 1

    def test_complete_download_compressed_footprint(self):
        st, decker = self._state([{"name": "Big", "density": 200}], compressor=3)
        pd = st["paydata"][0]
        mr._complete_download(st, decker, pd)
        assert pd["compressed"] is True and pd["full_size_mp"] == 200
        assert st["storage_used_mp"] == 100                     # stored halved on the deck
        assert st["downloaded_files"][0]["size_mp"] == 100

    # -- _auto_null_operation: Control test, Computer skill, tally rises --------

    def test_auto_null_operation_uses_computer_skill_no_hacking_pool(self, monkeypatch):
        st, decker = self._state([{"name": "F", "density": 60}])   # computer_skill 6
        seen = {}
        monkeypatch.setattr(eng, "system_test",
                            lambda **kw: seen.update(kw) or {"success": True, "decker_roll": {},
                                                             "host_roll": {}, "tally_increase": 0})
        hp_before = st.get("hackingPool_remaining")
        mr._auto_null_operation(st, decker)
        assert seen["decker_pool"] == 6                          # Computer skill, no Hacking Pool
        assert st.get("hackingPool_remaining") == hp_before      # Hacking Pool untouched

    def test_auto_null_operation_adds_host_security_tally(self, monkeypatch):
        st, decker = self._state([{"name": "F", "density": 60}])
        st["security_tally"] = 1
        monkeypatch.setattr(eng, "system_test",
                            lambda **kw: {"success": True, "decker_roll": {}, "host_roll": {},
                                          "tally_increase": 2})
        mr._auto_null_operation(st, decker)
        assert st["security_tally"] == 3                         # 1 + host Security Test successes

    # -- _corrupt_active_download ----------------------------------------------

    def test_corrupt_clears_active_download_and_notes(self):
        st, _ = self._state([{"name": "F", "density": 60}])
        st["active_download"] = {"file": "F", "turns_left": 2}
        st["event_log"] = []
        mr._corrupt_active_download(st)
        assert st["active_download"] is None
        assert st["event_log"][-1]["type"] == "download_corrupted"

    def test_corrupt_is_a_noop_when_no_download(self):
        st, _ = self._state([{"name": "F", "density": 60}])
        st["event_log"] = []
        mr._corrupt_active_download(st)
        assert st["active_download"] is None and st["event_log"] == []

    # -- _tick_active_download: decrement, complete, corrupt -------------------

    def test_tick_decrements_then_completes(self, monkeypatch):
        st, decker = self._state([{"name": "Payroll DB", "density": 120, "is_key": True}])
        st["active_download"] = {"file": "Payroll DB", "stored_mp": 120, "full_mp": 120,
                                 "compressed": False, "is_key": True, "turns_total": 3,
                                 "turns_left": 2, "started_turn": 1}
        monkeypatch.setattr(eng, "system_test",
                            lambda **kw: {"success": True, "decker_roll": {"successes": 1},
                                          "host_roll": {"successes": 0}, "tally_increase": 0})
        # First tick: still transferring -- nothing landed, no storage charged.
        mr._tick_active_download(st, decker, st["active_download"])
        assert st["active_download"]["turns_left"] == 1
        assert st["paydata"][0].get("downloaded") is not True
        assert st["storage_used_mp"] == 0
        assert st["event_log"][-1]["type"] == "null_operation"
        # Second tick: transfer completes -> file lands and storage is charged.
        mr._tick_active_download(st, decker, st["active_download"])
        assert st["active_download"] is None
        assert st["paydata"][0]["downloaded"] is True
        assert st["storage_used_mp"] == 120
        assert any(e["type"] == "data_downloaded" for e in st["event_log"])

    def test_tick_corrupts_when_source_file_destroyed_mid_transfer(self, monkeypatch):
        st, decker = self._state([{"name": "F", "density": 60}])
        st["paydata"][0]["destroyed"] = True                    # file erased before it finished
        st["active_download"] = {"file": "F", "stored_mp": 60, "full_mp": 60, "compressed": False,
                                 "is_key": False, "turns_total": 2, "turns_left": 1,
                                 "started_turn": 1}
        monkeypatch.setattr(eng, "system_test",
                            lambda **kw: {"success": True, "decker_roll": {}, "host_roll": {},
                                          "tally_increase": 0})
        mr._tick_active_download(st, decker, st["active_download"])
        assert st["active_download"] is None
        assert st["storage_used_mp"] == 0                       # nothing landed
        assert st["event_log"][-1]["type"] == "download_corrupted"

    # -- perform_action wiring: immediate vs background ------------------------

    def test_small_file_downloads_immediately(self, monkeypatch):
        st, decker = self._state([{"name": "Memo", "density": 30}], io_speed=100)   # 30 <= 100
        out = self._run_action(monkeypatch, st, decker,
                               action_type="download_data", target_file="Memo")
        assert out["active_download"] is None                   # one turn -> lands at once
        assert out["paydata"][0]["downloaded"] is True
        assert out["storage_used_mp"] == 30
        assert any(e["type"] == "data_downloaded" for e in out["event_log"])
        assert not any(e["type"] == "download_started" for e in out["event_log"])

    def test_large_file_starts_background_transfer(self, monkeypatch):
        st, decker = self._state([{"name": "Archive", "density": 120}], io_speed=40)  # 3 turns
        out = self._run_action(monkeypatch, st, decker,
                               action_type="download_data", target_file="Archive")
        dl = out["active_download"]
        assert dl is not None and dl["file"] == "Archive"
        assert dl["turns_total"] == 3 and dl["turns_left"] == 2   # first turn moved at start
        assert dl["stored_mp"] == 120
        assert out["paydata"][0].get("downloaded") is not True    # not landed yet
        assert out["storage_used_mp"] == 0                        # nor charged until complete
        assert any(e["type"] == "download_started" for e in out["event_log"])

    # -- perform_action guard: only Free actions during a transfer -------------

    def test_non_free_action_blocked_during_download(self, monkeypatch):
        st, decker = self._state([{"name": "F", "density": 60}], io_speed=20)
        st["active_download"] = {"file": "F", "stored_mp": 60, "full_mp": 60, "compressed": False,
                                 "is_key": False, "turns_total": 3, "turns_left": 2,
                                 "started_turn": 1}
        with pytest.raises(mr.HTTPException) as exc:
            self._run_action(monkeypatch, st, decker, action_type="analyze_host")
        assert exc.value.status_code == 400
        assert "only free actions" in exc.value.detail.lower()

    def test_second_download_blocked_during_download(self, monkeypatch):
        st, decker = self._state([{"name": "F", "density": 60}, {"name": "G", "density": 40}],
                                 io_speed=20)
        st["active_download"] = {"file": "F", "stored_mp": 60, "full_mp": 60, "compressed": False,
                                 "is_key": False, "turns_total": 3, "turns_left": 2,
                                 "started_turn": 1}
        with pytest.raises(mr.HTTPException) as exc:
            self._run_action(monkeypatch, st, decker,
                             action_type="download_data", target_file="G")
        assert exc.value.status_code == 400
        assert "already in progress" in exc.value.detail.lower()

    # -- new_turn ticks the background transfer --------------------------------

    def test_new_turn_tick_raises_tally_and_advances(self, monkeypatch):
        st, decker = self._state([{"name": "Archive", "density": 120}], io_speed=40)  # 3 turns
        st = self._run_action(monkeypatch, st, decker,
                              action_type="download_data", target_file="Archive")
        base = st["security_tally"]
        st = self._run_new_turn(monkeypatch, st, decker, tally_increase=2)
        assert st["active_download"]["turns_left"] == 1          # 2 -> 1, still transferring
        assert st["security_tally"] == base + 2                  # auto Null Op raised the tally
        assert any(e["type"] == "null_operation" for e in st["event_log"])

    def test_new_turn_completes_finished_download(self, monkeypatch):
        st, decker = self._state([{"name": "Archive", "density": 80}], io_speed=40)   # 2 turns
        st = self._run_action(monkeypatch, st, decker,
                              action_type="download_data", target_file="Archive")
        assert st["active_download"]["turns_left"] == 1
        st = self._run_new_turn(monkeypatch, st, decker)         # 1 -> 0 -> lands
        assert st["active_download"] is None
        assert st["paydata"][0]["downloaded"] is True
        assert st["storage_used_mp"] == 80
        assert any(e["type"] == "data_downloaded" for e in st["event_log"])

    # -- interruption corrupts the partial copy --------------------------------

    def test_graceful_logoff_corrupts_active_download(self, monkeypatch):
        import asyncio
        from app.schemas.matrix_run import RunLogoffInput
        st, decker = self._state([{"name": "F", "density": 60}], io_speed=20)
        st["active_download"] = {"file": "F", "stored_mp": 60, "full_mp": 60, "compressed": False,
                                 "is_key": False, "turns_total": 4, "turns_left": 3,
                                 "started_turn": 1}

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = None
            state_json = None

        run = _StubRun()
        run.decker_json = decker
        run.state_json = st

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(mr, "_apply_graceful_logoff", lambda *a, **k: True)
        body = RunLogoffInput(hacking_pool_dice=0, deception_utility=0)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.graceful_logoff(run_id=7, body=body, auth=auth, db=self._FakeDB()))
        assert run.status == "escaped"
        assert run.state_json["active_download"] is None         # partial copy discarded
        assert run.state_json["storage_used_mp"] == 0            # nothing charged
        assert run.state_json["event_log"][-1]["type"] == "download_corrupted"


# -- App-as-GM automation: ambush IC auto-fire, per-turn Worm, NPC pass flush ----
#
# There is no human GM for a Matrix run -- the player is the only human in the loop and the app
# drives every hostile (ambush IC, background Worms, proactive IC, enemy deckers). These classes
# validate the automation wiring added for that: a lurking Tar auto-fires at the utility the decker
# runs, a lurking Worm attacks the MPCP once each Combat Turn, hostiles always take their full
# initiative passes (even passes the decker never reached, and even on a turn the decker skips), and
# a badly wounded enemy decker breaks off and jacks out instead of fighting to the death.

class _AutoGMHost:
    config_json = {"security_code": "Red", "security_value": 9, "acifs": [9, 10, 9, 10, 10]}
    ltg_address = None
    trap_doors_json = None


class _AutoGMDB:
    async def commit(self):
        pass

    async def refresh(self, obj):
        pass


class TestAmbushTarAutoFire:
    """No human GM -- a lurking Tar Baby / Tar Pit fires AUTOMATICALLY at the utility the decker
    runs on a System Test (vr2 ambush IC). perform_action calls _autofire_lurking_tar after the
    action resolves: one opposed test per lurking tar when a reducible utility ran
    (utility_rating > 0), and nothing at all when the operation carried no utility (rating 0)."""

    def _decker(self):
        return {"name": "Ghost", "mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                "computer_skill": 6, "intelligence": 5, "quickness": 4, "willpower": 4, "body": 5,
                "hardening": 0, "deck_mode": "cool", "utilities": {"analyze": 6, "sleaze": 4}}

    def _state(self):
        st = mr._initial_state(self._decker(), _AutoGMHost())
        st["logon_complete"] = True
        # Neutralise the per-pass action economy -- these tests exercise the tar wiring, not AP.
        st["pass_action_points"] = 4
        st["pass_free"] = 4
        st["initiative_passes"] = 4
        st["current_pass"] = 1
        st["lurking_ic"] = [{"id": "tar1", "type": "Tar Baby", "rating": 6, "status": "lurking"}]
        return st

    def _drive(self, monkeypatch, state, *, utility_rating):
        import asyncio
        from app.schemas.matrix_run import RunActionInput

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = None
            state_json = None

        run = _StubRun()
        run.decker_json = self._decker()
        run.state_json = state

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "system_test",
                            lambda **kw: {"success": True, "decker_roll": {"successes": 3, "ones": 0},
                                          "host_roll": {"successes": 0}, "decker_net_successes": 3,
                                          "tally_increase": 0})
        # Deterministic dice for the tar's opposed test (real eng.tar_baby_test runs).
        monkeypatch.setattr(eng, "random", _ScriptedRandom([3, 1, 5, 2, 4, 6]))
        inp = RunActionInput(action_type="analyze_host", subsystem="access",
                             utility_rating=utility_rating, hacking_pool_dice=0, target_file="")
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.perform_action(run_id=7, body=inp, auth=auth, db=_AutoGMDB()))
        return run.state_json

    def test_tar_fires_on_utility_use(self, monkeypatch):
        out = self._drive(monkeypatch, self._state(), utility_rating=6)
        assert any(e.get("type") == "reactive_ic_resolved" and e.get("ic_id") == "tar1"
                   for e in out["event_log"]), "a lurking Tar must auto-fire when a utility runs"

    def test_tar_silent_when_no_utility_ran(self, monkeypatch):
        out = self._drive(monkeypatch, self._state(), utility_rating=0)
        assert not any(e.get("type") == "reactive_ic_resolved" for e in out["event_log"]), \
            "no reducible utility ran (rating 0) -> the tar must not fire"
        assert any(ic["id"] == "tar1" for ic in out["lurking_ic"]), "the tar is still lurking"


class TestWormAutoTickPerTurn:
    """vr2 L548 reconciliation (2026-07): a Worm is NOT a per-Combat-Turn tick. It booby-traps a
    subsystem and only rolls its Infection Test when the decker makes a System Test AGAINST that
    subsystem (see TestWormVariants.test_trigger_fires_only_for_matching_subsystem). new_turn must
    therefore leave lurking Worms untouched."""

    def _decker(self, disinfect=0):
        d = {"name": "Ghost", "mpcp": 4, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
             "computer_skill": 6, "intelligence": 5, "quickness": 4, "willpower": 4, "body": 5,
             "hardening": 0, "deck_mode": "cool", "utilities": {}}
        if disinfect:
            d["utilities"]["disinfect"] = disinfect
        return d

    def _state(self, decker):
        st = mr._initial_state(decker, _AutoGMHost())
        st["logon_complete"] = True
        st["lurking_ic"] = [{"id": "worm1", "type": "Worm", "rating": 8, "status": "lurking"}]
        st["initiative_passes"] = 1     # single pass -> one End Turn ends the Combat Turn
        return st

    def _new_turn(self, monkeypatch, state, decker):
        import asyncio

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = None
            state_json = None

        run = _StubRun()
        run.decker_json = decker
        run.state_json = state

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.new_turn(run_id=7, auth=auth, db=_AutoGMDB()))
        return run.state_json

    def test_worm_does_not_resolve_on_new_turn(self, monkeypatch):
        # A guaranteed-infection stub proves new_turn never even ROLLS the worm: it stays lurking
        # and no worm_resolved event is emitted just from ending a Combat Turn.
        monkeypatch.setattr(eng, "worm_attack",
                            lambda **kw: {"mpcp_infected": True, "tn": 4, "net_successes": 3,
                                          "roll": {"pool": 6, "successes": 3}})
        decker = self._decker(disinfect=0)
        out = self._new_turn(monkeypatch, self._state(decker), decker)
        assert out.get("mpcp_infected") is not True
        assert any(ic["id"] == "worm1" for ic in out["lurking_ic"]), "Worm keeps lurking across turns"
        assert not any(e.get("type") == "worm_resolved" for e in out["event_log"])


class TestNpcPassFlushOnNewTurn:
    """No human GM -- hostiles ALWAYS take their full initiative passes each Combat Turn. current_pass
    only climbs as far as the DECKER's passes, so a faster IC would be cheated of its extra passes,
    and a turn the decker ends without acting would let no hostile act at all. new_turn flushes the
    remaining NPC passes (current_pass..max_npc_passes) before resetting for the next turn."""

    def _decker(self):
        return {"name": "Ghost", "mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                "computer_skill": 6, "intelligence": 5, "quickness": 4, "willpower": 4, "body": 5,
                "hardening": 0, "deck_mode": "cool", "utilities": {"sleaze": 4}}

    def _state(self, decker, ic):
        st = mr._initial_state(decker, _AutoGMHost())
        st["logon_complete"] = True
        st["active_ic"] = [ic]
        st["initiative_passes"] = 1     # the decker has a single pass this turn
        st["current_pass"] = 1
        st["event_log"] = []
        return st

    def _new_turn(self, monkeypatch, state, decker):
        import asyncio

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = None
            state_json = None

        run = _StubRun()
        run.decker_json = decker
        run.state_json = state

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        # All-1s dice: the IC attack misses but still logs its ic_attack event (proof it acted).
        monkeypatch.setattr(eng, "random", _ScriptedRandom([1]))
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.new_turn(run_id=7, auth=auth, db=_AutoGMDB()))
        return run.state_json

    def test_faster_ic_gets_its_extra_pass_flushed(self, monkeypatch):
        decker = self._decker()
        # IC initiative 20 -> 2 passes; it already acted on pass 1 this turn (acted_pass=1). Its
        # pass-2 action -- which the 1-pass decker never reached -- must be flushed on New Turn.
        ic = {"id": "killer1", "type": "Killer", "rating": 6, "status": "active",
              "initiative": 20, "acted_pass": 1}
        out = self._new_turn(monkeypatch, self._state(decker, ic), decker)
        assert any(e.get("type") == "ic_attack" and e.get("ic_id") == "killer1"
                   for e in out["event_log"]), "the faster IC's 2nd pass must fire on New Turn"

    def test_ic_acts_on_bare_new_turn_with_no_player_action(self, monkeypatch):
        decker = self._decker()
        # The decker ends the turn WITHOUT acting (no acted_pass on the IC). New Turn must still
        # drive the IC's pass-1 action -- a bare New Turn is not a free pass for the runner.
        ic = {"id": "killer2", "type": "Killer", "rating": 6, "status": "active",
              "initiative": 12}
        out = self._new_turn(monkeypatch, self._state(decker, ic), decker)
        assert any(e.get("type") == "ic_attack" and e.get("ic_id") == "killer2"
                   for e in out["event_log"]), "a hostile must act even on a bare New Turn"


class TestEnemyDeckerSelfPreservation:
    """Wounded enemy-decker AI (spec 3.2). The old hard 7-box flee is replaced by an escalating
    NERVE check at 7/8/9 persona boxes (10 = dumped), softened per-instance by bravery, plus a
    hide-heal-return loop for Medic-carriers. Nerve/flee probability rolls read matrix_runs.random;
    generation and dice read matrix_engine.random (the `scripted` fixture)."""

    def _decker(self):
        return {"bod": 5, "evasion": 5, "masking": 5, "sensor": 5, "mpcp": 6,
                "intelligence": 5, "body": 5, "hardening": 0, "computer_skill": 5,
                "utilities": {"sleaze": 4}}

    def _state(self):
        s = _fresh_state(sec_code="Red", sec_value=9)
        s["event_log"] = []
        s["npc_combat_maneuvers"] = False   # isolate the wounded-AI logic from combat maneuvers
        s["security_tally"] = 0
        s["condition_monitor"] = {"persona_boxes": 0, "physical_boxes": 0, "mpcp_damage": 0,
                                  "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0}}
        return s

    def _enemy(self, boxes, *, bravery=0, medic=0, done=None):
        util = {"attack": 6, "sleaze": 5, "scanner": 5}
        if medic:
            util["medic"] = medic
        return {
            "id": "ed1", "name": "Red Security Decker", "tier": "Red",
            "mpcp": 9, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
            "computer_skill": 8, "intelligence": 6, "quickness": 6, "response_increase": 1,
            "deck_mode": "cool", "reality_filter": False,
            "utilities": util, "programs": ["Attack"], "intent": "dump",
            "lethal_program": None, "lethal_rating": 0, "hardening": 0, "bravery": bravery,
            "detection_factor": 4, "located": True, "revealed": True, "status": "active",
            "condition_monitor": {"persona_boxes": boxes, "stun_boxes": 0, "physical_boxes": 0,
                                  "mpcp_damage": 0},
            "program_damage": {}, "nerve_checks_done": list(done or []),
            "locate_progress": 99,
        }

    def test_nerve_break_flees(self, scripted, monkeypatch):
        # boxes 8, bravery 0: threshold 7 (0.30) holds at 0.5, then 8 (0.55) breaks -> flees.
        scripted([1])
        monkeypatch.setattr(mr, "random", _ProbRandom(randoms=[0.5]))
        state = self._state(); enemy = self._enemy(8, bravery=0)
        mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy)
        assert enemy["status"] == "fled"
        assert any(e.get("outcome") == "fled" and e.get("enemy_id") == "ed1"
                   for e in state["event_log"])
        assert 8 in enemy["nerve_checks_done"]

    def test_low_threshold_holds(self, scripted, monkeypatch):
        # boxes 7, bravery 0: 0.5 not < 0.30 -> holds nerve and fights on (still active).
        scripted([1])
        monkeypatch.setattr(mr, "random", _ProbRandom(randoms=[0.5]))
        state = self._state(); enemy = self._enemy(7, bravery=0)
        mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy)
        assert enemy["status"] == "active"
        assert not any(e.get("outcome") == "fled" for e in state["event_log"])
        assert enemy["nerve_checks_done"] == [7]

    def test_high_bravery_holds_longer(self, scripted, monkeypatch):
        # boxes 8, bravery 3: 7 -> 0.30-0.45 clamps to 0.05 (hold); 8 -> 0.55-0.45=0.10 (hold at 0.5).
        scripted([1])
        monkeypatch.setattr(mr, "random", _ProbRandom(randoms=[0.5]))
        state = self._state(); enemy = self._enemy(8, bravery=3)
        mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy)
        assert enemy["status"] == "active"
        assert not any(e.get("outcome") == "fled" for e in state["event_log"])

    def test_nerve_checked_once_per_threshold(self, scripted, monkeypatch):
        # 7 already checked (held): a later turn still at 7 is NOT re-rolled, even with a roll that
        # would now fail (0.0 < 0.30).
        scripted([1])
        monkeypatch.setattr(mr, "random", _ProbRandom(randoms=[0.0]))
        state = self._state(); enemy = self._enemy(7, bravery=0, done=[7])
        mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy)
        assert enemy["status"] == "active"     # threshold 7 not re-checked -> no flee

    def test_ten_boxes_dumped(self, scripted, monkeypatch):
        # 10 persona boxes -> forced dump, ahead of (and independent of) the nerve roll.
        scripted([1])
        monkeypatch.setattr(mr, "random", _ProbRandom(randoms=[0.99]))  # would never flee by choice
        state = self._state(); enemy = self._enemy(10)
        mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy)
        assert enemy["status"] == "fled"
        assert any(e.get("outcome") == "fled" for e in state["event_log"])

    def test_medic_carrier_breaks_contact_to_heal(self, scripted, monkeypatch):
        # A wounded Medic-carrier (boxes >= _ENEMY_WOUNDED_BOXES) that holds its nerve spends the
        # turn on Evade Detection to peel off and heal, instead of pressing the attack.
        scripted([6, 6, 6, 1, 1])
        monkeypatch.setattr(mr, "random", _ProbRandom(randoms=[0.99]))  # nerve holds
        state = self._state(); enemy = self._enemy(6, bravery=3, medic=5)
        mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy)
        assert enemy["status"] == "active"
        assert any(e.get("type") == "maneuver" and e.get("maneuver") == "evade_detection"
                   for e in state["event_log"])
        assert not any(e.get("type") == "enemy_decker"
                       and e.get("outcome") in ("dump", "kill", "hog")
                       for e in state["event_log"])

    def test_medic_carrier_heals_while_hidden(self, scripted):
        # Already hidden: a Medic-carrier above the re-engage line heals its own icon and stays down.
        scripted([6])
        state = self._state()
        enemy = self._enemy(6, medic=5)
        enemy["evaded"] = True; enemy["evade_dir"] = "hid_from_pc"; enemy["revealed"] = False
        enemy["redetect_turn"] = 99; enemy["redetect_tally_base"] = 0
        state["current_turn"] = 1
        mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy)
        assert enemy["condition_monitor"]["persona_boxes"] < 6   # healed while hidden
        assert enemy.get("evaded") is True                        # stayed down

    def test_medic_carrier_reengages_when_healed(self, scripted):
        # Once healed to <= _ENEMY_REENGAGE_BOXES it drops the hide and rejoins the fight, revealed.
        scripted([1])
        state = self._state()
        enemy = self._enemy(2, medic=5)
        enemy["evaded"] = True; enemy["evade_dir"] = "hid_from_pc"; enemy["revealed"] = False
        enemy["redetect_turn"] = 99; enemy["redetect_tally_base"] = 0
        state["current_turn"] = 1
        mr._enemy_decker_take_turn(state, self._decker(), _RunStub(), enemy)
        assert not enemy.get("evaded")                # dropped its hide
        assert enemy["revealed"] is True              # back in the open
        assert any(e.get("outcome") == "reengage" for e in state["event_log"])


# -- Area-option Attack: one Attack Test engages up to (Area rating) icons -------

class TestAreaAttack:
    """vr2 Area utility -- one Attack Test engages up to (Area rating) icons at once, mixing IC
    and revealed enemy deckers. The to-hit TN rises by the number of targets, the strike bypasses
    Party-IC cluster penalties, and any target carrying Armor gains +2 effective Armor. A single
    target collapses to a plain Attack (no Area penalty, no Area armor bonus)."""

    def _decker(self, *, area=3, limit_target="", armor=0):
        opts = {"area": area}
        if limit_target:
            opts["limit_target"] = limit_target
        return {"name": "Ghost", "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                "mpcp": 6, "computer_skill": 8, "intelligence": 5, "body": 5, "hardening": 0,
                "utilities": {"attack": 6, "armor": armor},
                "program_options": {"attack": opts}}

    def _ic(self, iid, *, rating=6, **over):
        ic = {"id": iid, "type": "Killer", "rating": rating, "status": "active",
              "boxes": 0, "category": "gray"}
        ic.update(over)
        return ic

    def _enemy(self, eid="ed1", **over):
        e = {"id": eid, "name": "Red Decker", "tier": "Red", "status": "active",
             "revealed": True, "intent": "dump",
             "bod": 5, "evasion": 5, "masking": 5, "sensor": 5,
             "computer_skill": 8, "detection_factor": 4,
             "utilities": {"sleaze": 5, "armor": 0}, "condition_monitor": {"persona_boxes": 0}}
        e.update(over)
        return e

    def _run_area(self, monkeypatch, *, decker, active_ic, enemies, target_ids,
                  attack_pool=8, resist_successes=0):
        """Drive the async area_attack endpoint with deterministic dice: ONE big Attack Test (all
        dice score against every target), then a scripted resist roll per target so both an IC and
        an enemy reliably crash."""
        import asyncio
        from app.schemas.matrix_run import RunAreaAttackInput

        calls = {"n": 0}

        def _fake_roll(pool, tn):
            calls["n"] += 1
            if calls["n"] == 1:                     # the single shared Attack Test
                dice = [99] * max(1, pool)
                return {"pool": pool, "tn": tn, "dice": dice, "successes": len(dice), "ones": 0}
            return {"pool": pool, "tn": tn, "dice": [1] * max(1, pool),
                    "successes": resist_successes, "ones": 0}
        monkeypatch.setattr(eng, "roll_dice", _fake_roll)

        state = _fresh_state(sec_code="Red", sec_value=9)
        state["event_log"] = []
        state["hackingPool_remaining"] = 10
        state["active_ic"] = active_ic
        state["enemy_deckers"] = enemies

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run
        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        inp = RunAreaAttackInput(target_ids=target_ids, attack_pool=attack_pool, hacking_pool_dice=0)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.area_attack(run_id=7, body=inp, auth=auth, db=_FakeDB()))
        return run.state_json

    def _area_event(self, state):
        evs = [x for x in state["event_log"] if x.get("type") == "area_attack"]
        assert evs, "no area_attack event emitted"
        return evs[-1]

    # -- helpers: enemy Armor symmetry + shared IC-crash resolution ------------

    def test_enemy_armor_reads_utility(self):
        assert mr._enemy_armor({"utilities": {"armor": 4}}) == 4
        assert mr._enemy_armor({"utilities": {}}) == 0
        assert mr._enemy_armor({}) == 0

    def test_apply_ic_crash_bumps_tally_and_logs(self):
        state = _fresh_state(); state["event_log"] = []
        ic = self._ic("ic1", rating=6, boxes=10)
        mr._apply_ic_crash(state, ic, "Green", 0)
        assert ic["status"] == "crashed"
        assert state["security_tally"] == 6
        assert any(e["type"] == "ic_crashed" for e in state["event_log"])

    def test_apply_ic_crash_skulk_masks_tally(self):
        state = _fresh_state(); state["event_log"] = []
        ic = self._ic("ic1", rating=6, boxes=10)
        mr._apply_ic_crash(state, ic, "Green", 4)               # Skulk-4 masks a rating-6 crash
        assert state["security_tally"] == 2

    # -- endpoint: multi-target burst -----------------------------------------

    def test_burst_hits_ic_and_enemy_together(self, monkeypatch):
        decker = self._decker(area=3)
        # A single staged-Deadly burst deals 6 boxes (icon damage table), so both targets carry
        # 4 prior boxes -- 4 + 6 = 10 fills the monitor and crashes each.
        ic = self._ic("ic1", rating=6, boxes=4)
        enemy = self._enemy("ed1", condition_monitor={"persona_boxes": 4})
        st = self._run_area(monkeypatch, decker=decker, active_ic=[ic],
                            enemies=[enemy], target_ids=["ic1", "ed1"])
        ev = self._area_event(st)
        assert ev["n_targets"] == 2 and ev["area_penalty"] == 2
        assert ev["crashed"] == 2
        assert st["active_ic"][0]["status"] == "crashed"
        assert st["enemy_deckers"][0]["status"] == "crashed"
        assert st["security_tally"] >= 6                         # the crashed IC added its rating

    def test_single_target_has_no_area_penalty(self, monkeypatch):
        decker = self._decker(area=3)
        st = self._run_area(monkeypatch, decker=decker, active_ic=[self._ic("ic1", rating=6)],
                            enemies=[], target_ids=["ic1"])
        ev = self._area_event(st)
        assert ev["n_targets"] == 1 and ev["area_penalty"] == 0

    def test_more_targets_than_area_rating_rejected(self, monkeypatch):
        decker = self._decker(area=2)
        ics = [self._ic("ic1"), self._ic("ic2"), self._ic("ic3")]
        with pytest.raises(mr.HTTPException) as exc:
            self._run_area(monkeypatch, decker=decker, active_ic=ics, enemies=[],
                          target_ids=["ic1", "ic2", "ic3"])
        assert exc.value.status_code == 400

    def test_no_area_option_rejected(self, monkeypatch):
        decker = self._decker(area=0)
        with pytest.raises(mr.HTTPException) as exc:
            self._run_area(monkeypatch, decker=decker, active_ic=[self._ic("ic1")], enemies=[],
                          target_ids=["ic1"])
        assert exc.value.status_code == 400

    def test_limit_ic_rejects_enemy_target(self, monkeypatch):
        decker = self._decker(area=3, limit_target="ic")
        with pytest.raises(mr.HTTPException) as exc:
            self._run_area(monkeypatch, decker=decker, active_ic=[self._ic("ic1")],
                          enemies=[self._enemy("ed1")], target_ids=["ic1", "ed1"])
        assert exc.value.status_code == 400

    def test_limit_decker_rejects_ic_target(self, monkeypatch):
        decker = self._decker(area=3, limit_target="decker")
        with pytest.raises(mr.HTTPException) as exc:
            self._run_area(monkeypatch, decker=decker, active_ic=[self._ic("ic1")],
                          enemies=[self._enemy("ed1")], target_ids=["ed1", "ic1"])
        assert exc.value.status_code == 400

    def test_unknown_target_rejected(self, monkeypatch):
        decker = self._decker(area=3)
        with pytest.raises(mr.HTTPException) as exc:
            self._run_area(monkeypatch, decker=decker, active_ic=[self._ic("ic1")], enemies=[],
                          target_ids=["ic1", "ghost"])
        assert exc.value.status_code == 404

    # -- Area armor: +2 effective vs a burst, none on a single target ---------

    def test_area_burst_grants_armored_enemy_plus2(self, monkeypatch):
        captured = {}
        real_dr = eng.damage_resistance

        def _cap(**kw):
            captured["armor"] = kw.get("armor_rating")
            return real_dr(**kw)
        monkeypatch.setattr(eng, "damage_resistance", _cap)
        decker = self._decker(area=3)
        enemy = self._enemy("ed1", utilities={"sleaze": 5, "armor": 3})
        self._run_area(monkeypatch, decker=decker, active_ic=[self._ic("ic1", rating=6)],
                      enemies=[enemy], target_ids=["ic1", "ed1"])
        assert captured["armor"] == 5                           # 3 carried + 2 Area bonus

    def test_single_target_enemy_no_area_armor_bonus(self, monkeypatch):
        captured = {}
        real_dr = eng.damage_resistance

        def _cap(**kw):
            captured["armor"] = kw.get("armor_rating")
            return real_dr(**kw)
        monkeypatch.setattr(eng, "damage_resistance", _cap)
        decker = self._decker(area=3)
        enemy = self._enemy("ed1", utilities={"sleaze": 5, "armor": 3})
        self._run_area(monkeypatch, decker=decker, active_ic=[], enemies=[enemy],
                      target_ids=["ed1"])
        assert captured["armor"] == 3                           # single target -> no Area bonus


# -- Enemy-decker loadout overhaul (docs/enemy-decker-loadout-spec.md) ----------

class TestEnemyDeckerLoadoutBands:
    """Task 1 -- centered per-tier loadout bands. Every generated decker stays inside its tier's
    program caps (kill/survive ratings <= MPCP; lethal <= ceil(Computer/2)), carries the new
    self-preservation fields (bravery / program_damage / nerve_checks_done), drops the vestigial
    Deception utility, gains its defensive survive-kit only at the deadly tiers, and varies
    instance-to-instance within a tier."""

    def test_new_self_preservation_fields_present(self):
        d = eng.generate_enemy_decker("Red", 9)
        assert isinstance(d["bravery"], int) and d["bravery"] >= 0
        assert d["program_damage"] == {}                        # fresh -- no wear yet
        assert d["nerve_checks_done"] == []                     # no thresholds crossed yet

    def test_vestigial_deception_dropped(self):
        for code, value in (("Blue", 4), ("Red", 9), ("Black", 12)):
            d = eng.generate_enemy_decker(code, value)
            assert "deception" not in d
            assert "deception" not in d["utilities"]

    def test_program_ratings_never_exceed_caps(self):
        for _ in range(40):
            d = eng.generate_enemy_decker("Black", 12)
            mpcp = d["mpcp"]
            lethal_cap = (d["computer_skill"] + 1) // 2
            u = d["utilities"]
            for k in ("hog", "reveal", "poison", "restrict", "armor", "shield", "medic"):
                if k in u:
                    assert 1 <= u[k] <= mpcp, (k, u[k], mpcp)
            for k in ("black_hammer", "killjoy"):
                if k in u:
                    assert 1 <= u[k] <= lethal_cap, (k, u[k], lethal_cap)

    def test_defensive_kit_only_on_deadly_tiers(self):
        blue = eng.generate_enemy_decker("Blue", 4)["utilities"]
        assert not ({"armor", "shield", "medic"} & set(blue))   # Blue: no survive-kit
        red = eng.generate_enemy_decker("Red", 9)["utilities"]
        assert {"armor", "shield", "medic"} <= set(red)         # Red carries the full survive-kit
        black = eng.generate_enemy_decker("Black", 12)["utilities"]
        assert {"armor", "shield", "medic"} <= set(black)

    def test_bravery_bands_rise_with_tier(self):
        def mean_bravery(code, value):
            return sum(eng.generate_enemy_decker(code, value)["bravery"] for _ in range(40)) / 40
        assert mean_bravery("Blue", 4) < mean_bravery("Black", 12)   # elites hold their nerve longer

    def test_instances_vary_within_a_tier(self):
        skills = {eng.generate_enemy_decker("Black", 12)["computer_skill"] for _ in range(40)}
        assert len(skills) >= 2                                 # per-instance band variation

    def test_redaction_hides_new_secret_fields(self):
        # Task 6 must keep the Task-1 additions server-side: the player view is a strict whitelist.
        enemy = eng.generate_enemy_decker("Red", 9)
        enemy["id"] = "ed_x"
        enemy["condition_monitor"] = {"persona_boxes": 2, "mpcp_damage": 0}
        red = mr._redact_enemy_decker(enemy)
        for secret in ("bravery", "program_damage", "nerve_checks_done", "lethal_rating",
                       "lethal_program", "utilities", "mpcp", "computer_skill"):
            assert secret not in red


class TestEnemyDeckerSpawnSystem:
    """Task 2 -- probabilistic, count-capped enemy-decker dispatch. _maybe_spawn_enemy_decker rolls
    the per-tier chance after a sheaf step, never exceeds the per-run enemy_decker_cap, lazily rolls
    a missing cap once, and never spawns after the run has ended. Spawn/cap rolls read
    matrix_runs.random; the built decker's stats + initiative read matrix_engine.random."""

    def _state(self, **over):
        s = _fresh_state(sec_code="Red", sec_value=9)
        s["event_log"] = []
        s["enemy_deckers"] = []
        s["enemy_decker_cap"] = 2
        s.update(over)
        return s

    def test_low_roll_spawns_one(self, scripted, monkeypatch):
        scripted([3])
        monkeypatch.setattr(mr, "random", _ProbRandom(randoms=[0.0]))   # 0.0 < Red chance 0.20
        state = self._state()
        mr._maybe_spawn_enemy_decker(state, "Red")
        assert len(state["enemy_deckers"]) == 1
        assert state["enemy_deckers"][0]["id"].startswith("ed_")

    def test_high_roll_does_not_spawn(self, scripted, monkeypatch):
        scripted([3])
        monkeypatch.setattr(mr, "random", _ProbRandom(randoms=[0.99]))  # 0.99 !< 0.20
        state = self._state()
        mr._maybe_spawn_enemy_decker(state, "Red")
        assert state["enemy_deckers"] == []

    def test_cap_blocks_further_spawns(self, scripted, monkeypatch):
        scripted([3])
        monkeypatch.setattr(mr, "random", _ProbRandom(randoms=[0.0]))   # would spawn if uncapped
        state = self._state(enemy_decker_cap=1,
                            enemy_deckers=[{"id": "ed_existing", "status": "active"}])
        mr._maybe_spawn_enemy_decker(state, "Red")
        assert len(state["enemy_deckers"]) == 1                 # already at cap -> no new spawn

    def test_no_spawn_after_run_ended(self, scripted, monkeypatch):
        scripted([3])
        monkeypatch.setattr(mr, "random", _ProbRandom(randoms=[0.0]))
        state = self._state(run_ended=True)
        mr._maybe_spawn_enemy_decker(state, "Red")
        assert state["enemy_deckers"] == []

    def test_missing_cap_is_lazily_rolled_once(self, scripted, monkeypatch):
        scripted([3])
        # cap None -> rolled from Black's (2, 3) range; _ProbRandom.randint returns the low end (2).
        monkeypatch.setattr(mr, "random", _ProbRandom(randoms=[0.99], randints=[2]))
        state = self._state(enemy_decker_cap=None)
        mr._maybe_spawn_enemy_decker(state, "Black")
        assert state["enemy_decker_cap"] == 2                   # banked for the rest of the run
        assert state["enemy_deckers"] == []                     # high roll -> no spawn this step

    def test_unknown_security_code_never_spawns(self, scripted, monkeypatch):
        scripted([3])
        monkeypatch.setattr(mr, "random", _ProbRandom(randoms=[0.0]))
        state = self._state()
        mr._maybe_spawn_enemy_decker(state, "Mauve")            # no spawn config for this code
        assert state["enemy_deckers"] == []


class TestEnemyDefensiveStrikeBack:
    """Task 3 -- a security decker that carries Shield / Armor uses them to blunt the PC's Strike
    Back, EXACTLY like the PC decker: Shield parries successes off the incoming hit (and wears 1
    Rating Point per use, GM-only event), Armor lowers the attack Power fed to the resistance. A
    decker with neither takes the full hit. Fired through the real attack_enemy_decker endpoint."""

    def _decker(self):
        return {"name": "Ghost", "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                "mpcp": 6, "computer_skill": 8, "intelligence": 5, "body": 5, "hardening": 0,
                "utilities": {"attack": 6}}

    def _enemy(self, **over):
        e = {"id": "ed1", "name": "Red Decker", "tier": "Red", "status": "active",
             "revealed": True, "intent": "dump", "bod": 5, "evasion": 5, "masking": 5,
             "sensor": 5, "computer_skill": 8, "detection_factor": 4,
             "utilities": {"attack": 6}, "condition_monitor": {"persona_boxes": 0},
             "program_damage": {}}
        e.update(over)
        return e

    def _strike(self, monkeypatch, *, enemy, shield_succ, capture):
        import asyncio
        from app.schemas.matrix_run import RunEnemyAttackInput

        # Fixed Shield roll so the parry successes are deterministic.
        monkeypatch.setattr(eng, "shield_parry",
                            lambda shield_rating, attacker_skill: {
                                "successes": shield_succ, "roll": {"successes": shield_succ},
                                "tn": 4})

        # Fake cybercombat: capture the defensive kwargs the router fed in. The attack lands
        # (successes=4), so -- like the real engine -- we fire the deferred Shield parry callback
        # and make the boxes a function of the parried successes so a Shield provably reduces the
        # hit the enemy takes.
        def _fake_attack(**kw):
            capture.update(kw)
            parry = kw.get("shield_parry")
            ss = parry() if parry is not None else 0
            capture["shield_successes"] = ss
            boxes = max(0, 5 - int(ss or 0))
            return {"attack_roll": {"successes": 4, "ones": 0},
                    "resistance": {"boxes": boxes, "final_damage_level": "Moderate"}}
        monkeypatch.setattr(eng, "cybercombat_attack", _fake_attack)

        decker = self._decker()
        state = _fresh_state(sec_code="Red", sec_value=9)
        state["event_log"] = []
        state["hackingPool_remaining"] = 10
        state["enemy_deckers"] = [enemy]

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        inp = RunEnemyAttackInput(enemy_id="ed1", attack_pool=6, hacking_pool_dice=0,
                                  program="attack")
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.attack_enemy_decker(run_id=7, body=inp, auth=auth, db=_FakeDB()))
        return run.state_json

    def test_shield_parries_and_reduces_boxes(self, monkeypatch):
        cap = {}
        enemy = self._enemy(utilities={"attack": 6, "shield": 5})
        state = self._strike(monkeypatch, enemy=enemy, shield_succ=2, capture=cap)
        assert cap["shield_successes"] == 2                     # parry fed into the resistance
        e = state["enemy_deckers"][0]
        assert e["condition_monitor"]["persona_boxes"] == 3     # 5 - 2 parried
        assert e["program_damage"]["shield"] == 1              # worn 1 Rating Point per use
        parry = [x for x in state["event_log"] if x.get("type") == "enemy_shield_parry"]
        assert parry and parry[0]["gm_only"] is True and parry[0]["context"] == "attack"

    def test_armor_lowers_attack_power(self, monkeypatch):
        cap = {}
        enemy = self._enemy(utilities={"attack": 6, "armor": 4})
        self._strike(monkeypatch, enemy=enemy, shield_succ=0, capture=cap)
        assert cap["armor_rating"] == 4                         # Armor utility fed to the resistance

    def test_no_defensive_kit_takes_full_hit(self, monkeypatch):
        cap = {}
        enemy = self._enemy(utilities={"attack": 6})            # no shield / armor
        state = self._strike(monkeypatch, enemy=enemy, shield_succ=9, capture=cap)
        assert cap["shield_successes"] == 0                     # no Shield -> nothing parried
        assert cap["armor_rating"] == 0                         # no Armor
        e = state["enemy_deckers"][0]
        assert e["condition_monitor"]["persona_boxes"] == 5     # full 5 boxes
        assert "shield" not in enemy.get("program_damage", {})  # no wear
        assert not any(x.get("type") == "enemy_shield_parry" for x in state["event_log"])


class TestScanIcon:
    """Scan Icon vs a hostile decker (vr2 L1895).

    PC -> enemy: a dedicated Computer Test vs the target's Masking discloses hidden ratings in
    _SCAN_REVEAL_ORDER (1 per success; a decisive 3+ reveals all six), the TN shifting by the
    target's Sleaze vs the PC's Scanner. Enemy -> PC ('vice versa'): a crippler-carrying decker
    that pinpoints the PC pegs and telegraphs its weakest attribute, then opens ONCE with the
    matching crippler. Blue/Green enemies carry no cripplers, so they never scan (unchanged)."""

    # -- PC scans an enemy decker (dedicated /enemy-decker/scan endpoint) --------
    def _decker(self):
        return {"name": "Runner", "bod": 5, "evasion": 5, "masking": 5, "sensor": 5, "mpcp": 6,
                "intelligence": 5, "body": 5, "hardening": 0,
                "computer_skill": 6, "utilities": {"scanner": 6}}

    def _enemy(self, **over):
        e = {"id": "ed1", "name": "Red Decker", "tier": "Red", "status": "active",
             "revealed": True, "intent": "dump",
             "mpcp": 6, "bod": 5, "evasion": 4, "masking": 5, "sensor": 3,
             "response_increase": 2, "computer_skill": 8,
             "utilities": {"sleaze": 0}, "condition_monitor": {"persona_boxes": 0}}
        e.update(over)
        return e

    def _scan(self, monkeypatch, *, enemy, successes, capture=None, hacking_pool_dice=0):
        import asyncio
        from app.schemas.matrix_run import RunEnemyScanInput

        # Drive the reveal directly by the roll's success count so the test exercises the router's
        # reveal-ladder / redaction path, not the dice; capture the TN/pool the router computed.
        def _fake_roll(pool, tn):
            if capture is not None:
                capture["pool"] = pool
                capture["tn"] = tn
            return {"successes": successes, "pool": pool, "target": tn, "rolls": []}
        monkeypatch.setattr(eng, "roll_dice", _fake_roll)

        decker = self._decker()
        state = _fresh_state(sec_code="Red", sec_value=9)
        state["event_log"] = []
        state["hackingPool_remaining"] = 10
        state["enemy_deckers"] = [enemy]

        class _StubRun:
            id = 7
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = decker
            state_json = state

        run = _StubRun()

        async def _fake_get_run(db, run_id):
            return run

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get_run)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)

        class _FakeDB:
            async def commit(self):
                pass

            async def refresh(self, obj):
                pass

        inp = RunEnemyScanInput(enemy_id="ed1", hacking_pool_dice=hacking_pool_dice)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.scan_enemy_decker(run_id=7, body=inp, auth=auth, db=_FakeDB()))
        return run.state_json

    def _scan_event(self, state):
        evs = [e for e in state["event_log"] if e.get("type") == "icon_scanned"]
        assert evs, "no icon_scanned event emitted"
        return evs[-1]

    def test_one_success_reveals_one_rating(self, monkeypatch):
        state = self._scan(monkeypatch, enemy=self._enemy(), successes=1)
        e = state["enemy_deckers"][0]
        assert e["scan_reveal"] == 1
        assert mr._redact_enemy_decker(e)["scanned"] == {"mpcp": 6}   # first in _SCAN_REVEAL_ORDER

    def test_two_successes_reveal_two_ratings(self, monkeypatch):
        state = self._scan(monkeypatch, enemy=self._enemy(), successes=2)
        e = state["enemy_deckers"][0]
        assert e["scan_reveal"] == 2
        assert mr._redact_enemy_decker(e)["scanned"] == {"mpcp": 6, "bod": 5}

    def test_three_successes_reveal_everything(self, monkeypatch):
        state = self._scan(monkeypatch, enemy=self._enemy(), successes=3)
        e = state["enemy_deckers"][0]
        assert e["scan_reveal"] == 6                              # decisive scan -> whole icon bare
        red = mr._redact_enemy_decker(e)
        assert red["scan_level"] == 6
        assert set(red["scanned"]) == set(mr._SCAN_REVEAL_ORDER)
        ev = self._scan_event(state)
        assert ev["success"] is True and ev["scan_level"] == 6

    def test_reveals_accumulate_across_scans(self, monkeypatch):
        # A prior single-success scan (scan_reveal=1) + one more success -> 2 revealed.
        state = self._scan(monkeypatch, enemy=self._enemy(scan_reveal=1), successes=1)
        assert state["enemy_deckers"][0]["scan_reveal"] == 2

    def test_failed_scan_reveals_nothing(self, monkeypatch):
        state = self._scan(monkeypatch, enemy=self._enemy(), successes=0)
        e = state["enemy_deckers"][0]
        assert e.get("scan_reveal", 0) == 0
        assert "scanned" not in mr._redact_enemy_decker(e)        # nothing leaked to the player
        assert self._scan_event(state)["success"] is False

    def test_tn_is_bare_masking_when_target_has_no_sleaze(self, monkeypatch):
        cap = {}
        self._scan(monkeypatch, enemy=self._enemy(masking=5, utilities={"sleaze": 0}),
                   successes=1, capture=cap)
        assert cap["tn"] == 5                                     # bare Masking
        assert cap["pool"] == 6                                   # Computer skill + 0 Hacking Pool

    def test_tn_adjusts_by_target_sleaze_vs_scanner(self, monkeypatch):
        cap = {}
        # Masking 5, target Sleaze 8 vs PC Scanner 6 -> 5 + (8 - 6) = 7.
        self._scan(monkeypatch, enemy=self._enemy(masking=5, utilities={"sleaze": 8}),
                   successes=1, capture=cap)
        assert cap["tn"] == 7

    def test_hacking_pool_adds_to_scan_pool(self, monkeypatch):
        cap = {}
        self._scan(monkeypatch, enemy=self._enemy(), successes=1, capture=cap, hacking_pool_dice=4)
        assert cap["pool"] == 10                                  # Computer 6 + 4 Hacking Pool

    def test_cannot_scan_unrevealed_enemy(self, monkeypatch):
        with pytest.raises(HTTPException) as ei:
            self._scan(monkeypatch, enemy=self._enemy(revealed=False), successes=1)
        assert ei.value.status_code == 404                        # hidden enemy -> 404 (no leak)

    def test_cannot_scan_crashed_enemy(self, monkeypatch):
        with pytest.raises(HTTPException) as ei:
            self._scan(monkeypatch, enemy=self._enemy(status="crashed"), successes=1)
        assert ei.value.status_code == 404

    # -- Enemy scans the PC ('vice versa' telegraph + weakness focus) -----------
    def _tele_state(self):
        s = _fresh_state(sec_code="Red", sec_value=9)
        s["event_log"] = []
        return s

    def test_enemy_pegs_and_telegraphs_pc_weakest_attr(self):
        state = self._tele_state()
        enemy = {"id": "ed1", "name": "Red Decker", "utilities": {"poison": 6, "reveal": 6}}
        eff = {"bod": 2, "evasion": 5, "masking": 5, "sensor": 5}   # Bod is the soft spot
        mr._enemy_scan_pc(state, enemy, eff)
        assert enemy["scanned_pc"] is True
        assert enemy["pc_weakest_attr"] == "bod"
        tele = [e for e in state["event_log"]
                if e.get("type") == "enemy_decker" and e.get("outcome") == "scanned"]
        assert len(tele) == 1                                     # player is warned exactly once

    def test_enemy_scan_is_idempotent(self):
        state = self._tele_state()
        enemy = {"id": "ed1", "name": "X", "scanned_pc": True,
                 "utilities": {"poison": 6, "reveal": 6}}
        mr._enemy_scan_pc(state, enemy, {"bod": 2, "evasion": 5, "masking": 5, "sensor": 5})
        assert not any(e.get("outcome") == "scanned" for e in state["event_log"])   # no re-scan

    def test_enemy_without_cripplers_never_scans(self):
        state = self._tele_state()
        enemy = {"id": "ed1", "name": "Blue Decker", "utilities": {}}   # Blue/Green loadout
        mr._enemy_scan_pc(state, enemy, {"bod": 2, "evasion": 5, "masking": 5, "sensor": 5})
        assert not enemy.get("scanned_pc")
        assert state["event_log"] == []                          # silent -> behaviour unchanged

    def test_focus_returns_weakness_crippler_once_then_attack(self):
        enemy = {"scanned_pc": True, "pc_weakest_attr": "bod", "utilities": {"poison": 6}}
        eff = {"bod": 2, "evasion": 5, "masking": 5, "sensor": 5}
        assert mr._enemy_focus_program(enemy, eff) == "Poison"
        enemy["focus_used"] = True
        assert mr._enemy_focus_program(enemy, eff) == "Attack"   # only the opening move

    def test_focus_skips_a_floored_attribute(self):
        enemy = {"scanned_pc": True, "pc_weakest_attr": "bod", "utilities": {"poison": 6}}
        eff = {"bod": 1, "evasion": 5, "masking": 5, "sensor": 5}   # already at the floor
        assert mr._enemy_focus_program(enemy, eff) == "Attack"

    def test_focus_is_plain_attack_before_any_scan(self):
        enemy = {"utilities": {"poison": 6}}                      # never scanned the PC
        assert mr._enemy_focus_program(enemy, {"bod": 2}) == "Attack"

    def test_located_scanned_enemy_opens_with_weakness_crippler(self, monkeypatch):
        # End-to-end wiring: a located, scanned Red enemy whose PC read is Bod-weak opens its pass
        # with Poison (the Bod crippler) exactly once, via _enemy_decker_take_turn.
        def _fake_crippler(**kw):
            return {"attack_roll": {"successes": 4, "ones": 0, "pool": kw.get("security_value", 6)},
                    "defense_roll": {"successes": 0}, "net_successes": 4,
                    "attribute_reduction": 2, "shield_successes": 0, "is_ripper": False}
        monkeypatch.setattr(eng, "crippler_attack", _fake_crippler)
        decker = {"name": "Runner", "bod": 2, "evasion": 5, "masking": 5, "sensor": 5, "mpcp": 6,
                  "intelligence": 5, "body": 5, "hardening": 0, "utilities": {}}
        state = _fresh_state(sec_code="Red", sec_value=9)
        state["event_log"] = []
        state["security_tally"] = 0                              # keep intent at 'dump' (no lethal)
        state["condition_monitor"] = {"persona_boxes": 0, "physical_boxes": 0, "stun_boxes": 0,
                                      "mpcp_damage": 0,
                                      "persona_damage": {"bod": 0, "evasion": 0,
                                                          "masking": 0, "sensor": 0}}
        enemy = {"id": "ed1", "name": "Red Decker", "tier": "Red", "status": "active",
                 "revealed": True, "located": True, "intent": "dump",
                 "scanned_pc": True, "pc_weakest_attr": "bod",
                 "bod": 5, "evasion": 5, "masking": 5, "sensor": 5,
                 "computer_skill": 8, "mpcp": 6, "intelligence": 5,
                 "utilities": {"attack": 5, "poison": 6},
                 "condition_monitor": {"persona_boxes": 0}}
        mr._enemy_decker_take_turn(state, decker, _RunStub(), enemy)
        crippled = [e for e in state["event_log"]
                    if e.get("type") == "enemy_decker" and e.get("program") == "Poison"]
        assert crippled, "scanned enemy did not open with the Bod crippler"
        assert enemy.get("focus_used") is True


class TestTraceVisibilityGate:
    """vr2 Trace IC visibility (user ruling 2026-07-10): a Trace is targetable while VISIBLE --
    during its Hunt Cycle, or once a Locate IC re-acquires it in its Location Cycle. A trace that
    has vanished into an un-located Location Cycle is off-sensors and cannot be attacked/slowed."""

    @staticmethod
    def _trace(**over):
        ic = {"id": "tr1", "type": "Trace", "rating": 6, "status": "active",
              "trace_phase": "hunt"}
        ic.update(over)
        return ic

    def test_hunt_cycle_trace_is_targetable(self):
        assert mr._trace_is_targetable(self._trace(trace_phase="hunt")) is True
        assert mr._trace_is_targetable(self._trace(trace_phase="hunting")) is True

    def test_unlocated_locating_trace_is_not_targetable(self):
        assert mr._trace_is_targetable(self._trace(trace_phase="locate")) is False

    def test_located_locating_trace_is_targetable(self):
        assert mr._trace_is_targetable(self._trace(trace_phase="locate", located=True)) is True

    def test_locate_ic_reacquires_hidden_trace(self):
        ic = self._trace(trace_phase="locate")
        st = {"active_ic": [ic], "event_log": []}
        mr._apply_locate_ic(st, test_success=True)
        assert ic.get("located") is True
        assert any(e.get("outcome") == "trace_reacquired" for e in st["event_log"])

    def test_failed_locate_ic_leaves_trace_hidden(self):
        ic = self._trace(trace_phase="locate")
        st = {"active_ic": [ic], "event_log": []}
        mr._apply_locate_ic(st, test_success=False)
        assert not ic.get("located")

    def test_trap_trace_factor_normal_is_half_rounded_up(self):
        ic = self._trace(trap_hidden={"type": "Blaster", "rating": 5})
        assert mr._trap_trace_factor_bonus(ic) == 3       # ceil(5/2)

    def test_trap_trace_factor_black_is_full_rating(self):
        ic = self._trace(trap_hidden={"type": "Black IC", "rating": 6})
        assert mr._trap_trace_factor_bonus(ic) == 6

    def test_no_trap_no_bonus(self):
        assert mr._trap_trace_factor_bonus(self._trace()) == 0

    def test_trap_raises_trace_tn(self):
        decker = {"evasion": 5, "utilities": {"camo": 0}, "trace_factor": 0}
        eff = {"evasion": 5}
        st = {"redirects_placed": 0}
        plain = mr._compute_trace_tn(st, decker, 2, eff, self._trace())
        trapped = mr._compute_trace_tn(st, decker, 2, eff,
                                       self._trace(trap_hidden={"type": "Blaster", "rating": 4}))
        assert trapped == plain + 2                        # ceil(4/2)


class TestDataBombSuppression:
    """vr2_rules.md L479 -- when a Data Bomb detonates it adds its rating to the security tally, and
    the decker MAY then spend 1 Detection Factor to suppress the IC and refund that tally (persona
    damage still lands). This is a post-event immediate query (a suppression ledger entry), resolved
    the same way as a crashed IC via _toggle_ic_suppression -- NOT part of the action economy."""

    def _decker(self):
        # masking 6, no sleaze -> Detection Factor 3 (comfortably > 1, so suppression is affordable).
        return {"bod": 6, "body": 6, "willpower": 6, "mpcp": 6, "masking": 6,
                "hardening": 0, "utilities": {}, "deck_mode": "hot"}

    def _state(self):
        st = _fresh_state()
        st["event_log"] = []
        st["condition_monitor"] = {"persona_boxes": 0, "stun_boxes": 0, "physical_boxes": 0,
                                   "mpcp_damage": 0, "persona_damage": {}}
        return st

    def test_detonation_adds_tally_and_registers_entry(self, scripted):
        scripted([1])
        st, dk = self._state(), self._decker()
        eff = mr._get_decker_effective(dk, st)
        mr._detonate_data_bomb(st, dk, eff, ic_rating=6, sec_value=6, sec_code="Green",
                               headline="Data bomb on Payroll")
        assert st["security_tally"] == 6
        sups = st.get("suppressions", [])
        assert len(sups) == 1 and sups[0]["source"] == "data_bomb" and sups[0]["rating"] == 6
        assert sups[0]["suppressed"] is False and sups[0]["released"] is False
        ev = next(e for e in st["event_log"] if e.get("type") == "data_bomb")
        assert ev["suppression_id"] == sups[0]["id"]
        assert ev["suppressible"] is True
        assert "Suppression pending." in ev["description"]

    def test_suppress_refunds_tally_and_costs_one_df(self, scripted):
        scripted([1])
        st, dk = self._state(), self._decker()
        df_before = mr._effective_detection_factor(st, dk)
        eff = mr._get_decker_effective(dk, st)
        mr._detonate_data_bomb(st, dk, eff, ic_rating=6, sec_value=6, sec_code="Green",
                               headline="Data bomb on Payroll")
        sup_id = st["suppressions"][0]["id"]
        mr._toggle_ic_suppression(st, dk, ic_id=sup_id, release=False)
        assert st["security_tally"] == 0                              # tally refunded
        assert st["suppressions"][0]["suppressed"] is True
        assert mr._effective_detection_factor(st, dk) == df_before - 1  # 1 DF held down

    def test_release_readds_tally_restores_df_and_is_one_way(self, scripted):
        scripted([1])
        st, dk = self._state(), self._decker()
        df_before = mr._effective_detection_factor(st, dk)
        eff = mr._get_decker_effective(dk, st)
        mr._detonate_data_bomb(st, dk, eff, ic_rating=6, sec_value=6, sec_code="Green",
                               headline="Data bomb on Payroll")
        sup_id = st["suppressions"][0]["id"]
        mr._toggle_ic_suppression(st, dk, ic_id=sup_id, release=False)
        mr._toggle_ic_suppression(st, dk, ic_id=sup_id, release=True)
        assert st["security_tally"] == 6                              # tally re-added
        assert mr._effective_detection_factor(st, dk) == df_before    # DF restored
        assert st["suppressions"][0]["released"] is True
        # One-way: cannot re-suppress a released entry.
        with pytest.raises(HTTPException):
            mr._toggle_ic_suppression(st, dk, ic_id=sup_id, release=False)

    def test_suppress_release_cost_no_action(self, scripted):
        scripted([1])
        st, dk = self._state(), self._decker()
        st["pass_free"] = 1
        eff = mr._get_decker_effective(dk, st)
        mr._detonate_data_bomb(st, dk, eff, ic_rating=6, sec_value=6, sec_code="Green",
                               headline="Data bomb on Payroll")
        sup_id = st["suppressions"][0]["id"]
        mr._toggle_ic_suppression(st, dk, ic_id=sup_id, release=False)
        mr._toggle_ic_suppression(st, dk, ic_id=sup_id, release=True)
        assert st["pass_free"] == 1                                   # neither direction spends an action


class TestSheafSuppressionDeferral:
    """A crash or data-bomb detonation adds to the security tally, but the decker gets an immediate
    suppress/accept query before that increment is allowed to trip a sheaf step (a passive alert or
    IC spawn). The held-back tally must NOT fire the sheaf while the decision is pending; suppressing
    keeps it hidden; accepting/releasing (or the pass/turn auto-flush) lets it finally fire."""

    def _decker(self):
        return {"bod": 6, "body": 6, "willpower": 6, "mpcp": 6, "masking": 6,
                "hardening": 0, "utilities": {}, "deck_mode": "hot"}

    def _state(self):
        st = _fresh_state()
        st["event_log"] = []
        st["sheaf_steps_triggered"] = []
        # One step that fires the instant the tally reaches 5 (a passive alert).
        st["sheaf"] = [{"trigger": 5, "events": [{"type": "alert", "level": "passive"}]}]
        st["condition_monitor"] = {"persona_boxes": 0, "stun_boxes": 0, "physical_boxes": 0,
                                   "mpcp_damage": 0, "persona_damage": {}}
        return st

    def test_bomb_detonation_does_not_fire_sheaf_while_pending(self, scripted):
        scripted([1])
        st, dk = self._state(), self._decker()
        eff = mr._get_decker_effective(dk, st)
        mr._detonate_data_bomb(st, dk, eff, ic_rating=6, sec_value=6, sec_code="Green",
                               headline="Data bomb on Payroll")
        assert st["security_tally"] == 6                 # tally applied
        assert st["sheaf_steps_triggered"] == []         # ...but the step is HELD, not fired
        # Suppressing keeps it hidden from the sheaf.
        sup_id = st["suppressions"][0]["id"]
        mr._toggle_ic_suppression(st, dk, ic_id=sup_id, release=False)
        assert st["sheaf_steps_triggered"] == []
        # Releasing the suppressed entry fires the deferred step.
        mr._toggle_ic_suppression(st, dk, ic_id=sup_id, release=True)
        assert st["sheaf_steps_triggered"] == [0]

    def test_bomb_accept_from_pending_fires_sheaf(self, scripted):
        scripted([1])
        st, dk = self._state(), self._decker()
        eff = mr._get_decker_effective(dk, st)
        mr._detonate_data_bomb(st, dk, eff, ic_rating=6, sec_value=6, sec_code="Green",
                               headline="Data bomb on Payroll")
        sup_id = st["suppressions"][0]["id"]
        assert st["sheaf_steps_triggered"] == []
        # Accept the pending entry without ever suppressing: tally already applied, so no re-add,
        # but the sheaf now sees it.
        mr._toggle_ic_suppression(st, dk, ic_id=sup_id, release=True)
        assert st["security_tally"] == 6
        assert st["sheaf_steps_triggered"] == [0]
        assert st["suppressions"][0]["released"] is True

    def test_crash_does_not_fire_sheaf_while_pending(self):
        st, dk = self._state(), self._decker()
        ic = {"id": "ic-1", "type": "Killer", "rating": 6, "status": "active",
              "boxes": 10, "category": "gray"}
        st["active_ic"] = [ic]
        mr._apply_ic_crash(st, ic, "Green", 0)
        assert st["security_tally"] == 6
        assert ic.get("crash_pending") is True
        assert st["sheaf_steps_triggered"] == []         # held while pending
        # Suppress -> still hidden.
        mr._toggle_ic_suppression(st, dk, ic_id="ic-1", release=False)
        assert st["sheaf_steps_triggered"] == []
        assert ic.get("crash_pending") is False
        # Release the suppressed crash -> re-adds tally and fires the deferred step.
        mr._toggle_ic_suppression(st, dk, ic_id="ic-1", release=True)
        assert st["security_tally"] == 6
        assert st["sheaf_steps_triggered"] == [0]

    def test_flush_pending_fires_sheaf(self):
        st, dk = self._state(), self._decker()
        ic = {"id": "ic-1", "type": "Killer", "rating": 6, "status": "active",
              "boxes": 10, "category": "gray"}
        st["active_ic"] = [ic]
        mr._apply_ic_crash(st, ic, "Green", 0)
        assert st["sheaf_steps_triggered"] == []
        mr._flush_pending_suppressions(st, "Green")
        assert ic.get("crash_pending") is False
        assert ic.get("suppression_released") is True
        assert st["sheaf_steps_triggered"] == [0]        # auto-accepted -> step fires


class TestSuppressionDfFloor:
    """A suppression costs 1 Detection Factor and DF cannot be spent below its floor of 1. Once the
    decker holds down enough sources that DF is at the floor, a further suppress is REJECTED -- they
    must release one first to free up a point (vr2 Suppression -- can't spend DF you don't have)."""

    def _decker(self):
        # masking 4, no sleaze -> base Detection Factor 2, so exactly ONE suppression is affordable.
        return {"bod": 6, "body": 6, "willpower": 6, "mpcp": 6, "masking": 4,
                "hardening": 0, "utilities": {}, "deck_mode": "hot"}

    def _state(self):
        st = _fresh_state()
        st["event_log"] = []
        st["sheaf_steps_triggered"] = []
        st["sheaf"] = []
        st["condition_monitor"] = {"persona_boxes": 0, "stun_boxes": 0, "physical_boxes": 0,
                                   "mpcp_damage": 0, "persona_damage": {}}
        return st

    def _crash(self, st, ic_id, rating=6):
        ic = {"id": ic_id, "type": "Killer", "rating": rating, "status": "active",
              "boxes": 10, "category": "gray"}
        st["active_ic"].append(ic)
        mr._apply_ic_crash(st, ic, "Green", 0)
        return ic

    def test_second_suppress_rejected_when_df_at_floor(self):
        st, dk = self._state(), self._decker()
        assert mr._base_detection_factor(st, dk) == 2       # room for exactly one suppression
        self._crash(st, "ic-1")
        self._crash(st, "ic-2")
        # First suppression is fine (DF 2 -> 1).
        mr._toggle_ic_suppression(st, dk, ic_id="ic-1", release=False)
        assert mr._effective_detection_factor(st, dk) == 1
        # Second suppression would push DF below the floor -> rejected.
        with pytest.raises(HTTPException):
            mr._toggle_ic_suppression(st, dk, ic_id="ic-2", release=False)
        assert st["active_ic"][1].get("suppressed") is not True

    def test_release_frees_room_to_suppress_the_newest(self):
        st, dk = self._state(), self._decker()
        self._crash(st, "ic-1")
        self._crash(st, "ic-2")
        mr._toggle_ic_suppression(st, dk, ic_id="ic-1", release=False)   # DF at floor now
        with pytest.raises(HTTPException):
            mr._toggle_ic_suppression(st, dk, ic_id="ic-2", release=False)
        # Release the first to free up a DF point...
        mr._toggle_ic_suppression(st, dk, ic_id="ic-1", release=True)
        # ...then the newest can be suppressed.
        mr._toggle_ic_suppression(st, dk, ic_id="ic-2", release=False)
        assert st["active_ic"][1].get("suppressed") is True
        assert mr._effective_detection_factor(st, dk) == 1


class TestNpcPositionBonus:
    """vr2_rules.md L2004 -- the Position Attack winner may take -TN OR +Power. The shared NPC
    heuristic (_npc_position_bonus) presses for +Power when the PC is badly wounded (>=5 persona
    boxes), else takes -TN. Used by both an NPC-initiated win and a PC-initiated backfire."""

    def test_healthy_pc_gives_tn_reduction(self):
        st = {"condition_monitor": {"persona_boxes": 2}}
        assert mr._npc_position_bonus(st, 3) == {"tn_reduction": 3}

    def test_badly_wounded_pc_gives_power(self):
        st = {"condition_monitor": {"persona_boxes": 5}}
        assert mr._npc_position_bonus(st, 2) == {"power_bonus": 2}










