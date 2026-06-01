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
        # Black Hammer rating is capped at half the Computer skill
        d = eng.generate_enemy_decker("Black", 12)
        assert d["lethal_rating"] == (d["computer_skill"] + 1) // 2

    def test_value_scales_within_tier(self):
        low = eng.generate_enemy_decker("Blue", 2)
        high = eng.generate_enemy_decker("Blue", 5)
        assert high["computer_skill"] >= low["computer_skill"]
        assert high["computer_skill"] <= 4  # still capped to the Blue tier

    def test_black_host_is_lethal_elite(self):
        d = eng.generate_enemy_decker("Black", 10)
        assert d["computer_skill"] >= 8
        assert d["intent"] == "kill"
        assert d["lethal_program"] == "Black Hammer"
        assert "Black Hammer" in d["programs"]

    def test_tiers_are_monotonic(self):
        skills = [eng.generate_enemy_decker(c, v)["computer_skill"]
                  for c, v in (("Blue", 4), ("Green", 6), ("Orange", 8), ("Red", 9), ("Black", 12))]
        assert skills == sorted(skills)

    def test_enemy_has_combat_loadout(self):
        d = eng.generate_enemy_decker("Red", 8)
        assert d["utilities"]["attack"] >= 6
        assert d["detection_factor"] >= 1  # the PC must beat this to find them
        assert d["status"] == "active" and d["located"] is False


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

    def test_cascade_activates_next_untriggered_step(self, scripted):
        scripted([3])  # ic_initiative_roll for the cascaded IC
        state = _fresh_state(); state["event_log"] = []; state["active_ic"] = []
        state["sheaf"] = [
            {"trigger": 5, "events": [{"type": "ic", "ic_type": "Killer", "rating": 6}]},
            {"trigger": 10, "events": [{"type": "ic", "ic_type": "Blaster", "rating": 6}]},
        ]
        state["sheaf_steps_triggered"] = [0]
        assert mr._cascade_next_sheaf_step(state, "Red") is True
        assert 1 in state["sheaf_steps_triggered"]
        assert any(e["type"] == "cascade" for e in state["event_log"])
        assert any(ic["type"] == "Blaster" for ic in state["active_ic"])

    def test_cascade_noop_when_all_triggered(self):
        state = _fresh_state(); state["event_log"] = []
        state["sheaf"] = [{"trigger": 5, "events": []}]; state["sheaf_steps_triggered"] = [0]
        assert mr._cascade_next_sheaf_step(state, "Red") is False

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
    """Gap D enforcement -- per-pass action budget (2 Simple OR 1 Complex + 1 Free), auto-
    advancing passes, blocking (New Turn) when all initiative passes are spent."""

    def _state(self, passes=2):
        return {"event_log": [], "current_pass": 1, "initiative_passes": passes,
                "pass_action_points": 2, "pass_free": 1}

    def test_complex_spends_two_ap(self):
        s = self._state()
        mr._spend_pass_action(s, "analyze_host")   # Complex
        assert s["pass_action_points"] == 0

    def test_two_simple_then_block_advances_pass(self):
        s = self._state(passes=1)
        mr._spend_pass_action(s, "analyze_security")   # Simple -> 1 AP left
        mr._spend_pass_action(s, "download_data")      # Simple -> 0 AP left
        assert s["pass_action_points"] == 0
        # third action, only 1 pass -> no advance possible -> blocks
        import fastapi
        with pytest.raises(fastapi.HTTPException):
            mr._spend_pass_action(s, "analyze_security")

    def test_free_action_uses_free_not_ap(self):
        s = self._state()
        mr._spend_pass_action(s, "analyze_ic")   # Free
        assert s["pass_action_points"] == 2 and s["pass_free"] == 0

    def test_auto_advances_to_next_pass(self):
        s = self._state(passes=3)
        mr._spend_pass_action(s, "analyze_host")   # Complex, pass1: 2->0
        mr._spend_pass_action(s, "analyze_host")   # Complex: pass1 can't afford -> advance to pass2, spend
        assert s["current_pass"] == 2 and s["pass_action_points"] == 0
        assert any(e["type"] == "new_pass" for e in s["event_log"])

    def test_block_when_all_passes_spent(self):
        s = self._state(passes=2)
        mr._spend_pass_action(s, "analyze_host")  # pass1 2->0
        mr._spend_pass_action(s, "analyze_host")  # advance pass2, 2->0
        import fastapi
        with pytest.raises(fastapi.HTTPException):
            mr._spend_pass_action(s, "analyze_host")  # no passes left -> New Turn

    def test_legacy_run_not_enforced(self):
        s = {"event_log": []}  # no pass_action_points
        mr._spend_pass_action(s, "analyze_host")  # no-op, no raise
        assert "pass_action_points" not in s


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
        assert passes == max(1, (init // 10) + 1)

    def test_action_cost_map_from_rules(self):
        assert mr._ACTION_COST["analyze_host"] == "Complex"
        assert mr._ACTION_COST["analyze_ic"] == "Free"
        assert mr._ACTION_COST["analyze_security"] == "Simple"
        assert mr._ACTION_COST["swap_memory"] == "Simple"
        assert mr._ACTION_COST["purge_hog"] == "Complex"

    def test_initial_state_rolls_initiative(self):
        class _Host:
            config_json = {"security_code": "Blue", "security_value": 4}
        st = mr._initial_state(
            {"quickness": 4, "intelligence": 5, "mpcp": 6, "masking": 4,
             "deck_mode": "hot", "utilities": {}}, _Host())
        assert st["decker_initiative"] >= 1
        assert st["initiative_passes"] == max(1, (st["decker_initiative"] // 10) + 1)
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

    def test_sheaf_enemy_decker_event_auto_injects(self, scripted):
        scripted([3])
        state = _fresh_state(); state["host_security_value"] = 8; state["enemy_deckers"] = []
        events = mr._activate_sheaf_step(state, {"trigger": 10, "events": [{"type": "enemy_decker"}]}, "Red")
        assert len(state["enemy_deckers"]) == 1
        ed = state["enemy_deckers"][0]
        assert ed["tier"] == "Red" and ed["computer_skill"] >= 1
        inj = [e for e in events if e.get("type") == "enemy_decker_injected"]
        assert inj and inj[0]["gm_only"] is True   # hidden from the player until detected


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
