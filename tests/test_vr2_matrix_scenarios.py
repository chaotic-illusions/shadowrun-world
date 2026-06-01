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
        scripted([6, 6])
        r = eng.worm_attack(ic_rating=6, mpcp_rating=4)
        assert r["tn"] == 4
        assert r["mpcp_infected"] is True
        assert r["chip_replacement_required"] is True

    def test_worm_disinfect_raises_tn_and_defends(self, scripted):
        scripted([3, 3])  # below TN
        r = eng.worm_attack(ic_rating=6, mpcp_rating=4, disinfect_utility=4)
        assert r["tn"] == 8  # 4 + 0 + 4
        assert r["mpcp_infected"] is False


class TestEnemyDeckerGeneration:
    """vr2 #5 -- security decker auto-generation stays in-band with the host tier."""

    def test_blue_host_stays_weak(self):
        # The user's constraint: a Blue-5 host must NOT field a Computer-12 decker.
        d = eng.generate_enemy_decker("Blue", 5)
        assert d["computer_skill"] <= 4
        assert d["mpcp"] <= 4
        assert d["intent"] == "boot"

    def test_value_scales_within_tier(self):
        low = eng.generate_enemy_decker("Blue", 2)
        high = eng.generate_enemy_decker("Blue", 5)
        assert high["computer_skill"] >= low["computer_skill"]
        assert high["computer_skill"] <= 4  # still capped to the Blue tier

    def test_black_host_is_lethal_elite(self):
        d = eng.generate_enemy_decker("Black", 10)
        assert d["computer_skill"] >= 8
        assert d["intent"] == "kill"
        assert d["black_hammer"] is True

    def test_tiers_are_monotonic(self):
        skills = [eng.generate_enemy_decker(c, v)["computer_skill"]
                  for c, v in (("Blue", 4), ("Green", 6), ("Orange", 8), ("Red", 9), ("Black", 12))]
        assert skills == sorted(skills)

    def test_enemy_has_combat_loadout(self):
        d = eng.generate_enemy_decker("Red", 8)
        assert d["utilities"]["attack"] >= 6
        assert d["detection_factor"] >= 1  # the PC must beat this to find them
        assert d["status"] == "active" and d["located"] is False


class TestEnemyLocateAndIntent:
    def test_locate_progress_is_net_enemy_successes(self, scripted):
        # enemy 3 hits (TN low), PC 1 hit -> progress +2
        scripted([6, 6, 6, 1, 6, 1, 1])
        r = eng.enemy_locate_test(computer_skill=8, scanner_rating=2,
                                  sensor_rating=4, pc_detection_factor=6, pc_evasion=4)
        assert r["progress_gain"] >= 0
        assert r["enemy_tn"] == 4  # 6 - 2 scanner

    def test_locate_never_negative(self, scripted):
        scripted([1, 1, 1, 6, 6, 6])  # enemy whiffs, PC resists well
        r = eng.enemy_locate_test(computer_skill=4, scanner_rating=0,
                                  sensor_rating=6, pc_detection_factor=8, pc_evasion=6)
        assert r["progress_gain"] == 0

    def test_intent_escalates_with_tally(self):
        assert eng.escalate_enemy_intent("boot", security_tally=5) == "boot"
        assert eng.escalate_enemy_intent("boot", security_tally=15) == "dump"
        assert eng.escalate_enemy_intent("dump", security_tally=15) == "kill"
        assert eng.escalate_enemy_intent("kill", security_tally=99) == "kill"

    def test_player_view_redacts_enemy_internals(self):
        enemy = eng.generate_enemy_decker("Red", 8)
        enemy["id"] = "ed_1"
        enemy["condition_monitor"] = {"persona_boxes": 4, "mpcp_damage": 0}
        red = mr._redact_enemy_decker(enemy)
        # presence + condition only -- no raw ratings leak to the player
        assert red["name"] and red["tier"] == "Red" and red["intent"]
        assert red["condition_monitor"]["persona_boxes"] == 4
        for secret in ("computer_skill", "mpcp", "utilities", "detection_factor"):
            assert secret not in red


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

    def test_poison_failure_destroys_key_data(self):
        c = eng.scramble_failure_consequence(variant="poison", is_key=True)
        assert c["data_destroyed"] is True
        assert c["key_data_lost"] is True
        assert "KEY DATA DESTROYED" in c["message"]

    def test_poison_failure_destroys_nonkey_data_quietly(self):
        c = eng.scramble_failure_consequence(variant="poison", is_key=False)
        assert c["data_destroyed"] is True
        assert c["key_data_lost"] is False
        assert "KEY DATA DESTROYED" not in c["message"]

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

    def test_secret_state_keys_are_gm_only(self):
        for k in ("scrambles", "paydata", "data_bombs"):
            assert k in mr._GM_ONLY_STATE_KEYS


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
        assert out["category"] == "white"

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

    def test_reactive_level2_shows_type_not_rating(self):
        out = mr._redact_ic(self._reactive(detection_level=2))
        assert out["type"] == "Probe" and out["rating"] is None

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
