"""VR2.0 rules-validation suite for the Matrix engine.

Each test cites the vr2_rules.md section it validates. Green tests assert the engine
matches the rules; `xfail` tests encode a rule the engine does NOT yet satisfy (the
reason names the rule + the deviation) so the gap is tracked without breaking CI.

Dice are made deterministic by monkeypatching app.services.matrix_engine.random.
"""
from __future__ import annotations

import random as _stdrandom

import pytest

from app.services import matrix_engine as eng
from app.services import matrix_rules as rules


# -- Deterministic dice helper -------------------------------------------------

class _ScriptedRandom:
    """Stands in for the module's `random`; returns scripted randint values."""
    def __init__(self, values):
        self._v = list(values)
        self._i = 0

    def randint(self, a, b):
        v = self._v[self._i % len(self._v)]
        self._i += 1
        # clamp into range so scripts stay legal
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


# -- Rules tables match VR2 (Reference Tables / Cybercombat Summary) ------------

class TestRulesTables:
    def test_damage_boxes(self):
        # vr2_rules.md "Condition Monitor Fill": L1 M2 S3 Deadly6
        assert rules.DAMAGE_BOXES == {"Light": 1, "Moderate": 2, "Serious": 3, "Deadly": 6}

    def test_damage_levels_order(self):
        assert rules.DAMAGE_LEVELS == ["Light", "Moderate", "Serious", "Deadly"]

    def test_ic_damage_level_by_host(self):
        # "IC Damage Level by Host Security"
        assert rules.IC_DAMAGE_LEVEL == {
            "Blue": "Light", "Green": "Moderate", "Orange": "Moderate",
            "Red": "Serious", "Black": "Serious",
        }

    def test_dump_shock_level_by_host(self):
        # "Dump Shock Damage Level by Host Security"
        assert rules.DUMP_SHOCK_LEVEL == {
            "Blue": "Light", "Green": "Moderate", "Orange": "Serious",
            "Red": "Deadly", "Black": "Deadly",
        }

    def test_combat_tn(self):
        # "Cybercombat Target Numbers": intruding / legitimate
        assert rules.COMBAT_TN["Blue"] == {"intruding": 6, "legitimate": 3}
        assert rules.COMBAT_TN["Green"] == {"intruding": 5, "legitimate": 4}
        assert rules.COMBAT_TN["Orange"] == {"intruding": 4, "legitimate": 5}
        assert rules.COMBAT_TN["Red"] == {"intruding": 5, "legitimate": 6}
        assert rules.COMBAT_TN["Black"] == {"intruding": 3, "legitimate": 8}

    def test_simsense_overload_tn(self):
        # "Simsense Overload TN": L2 M3 S5 (no Deadly entry)
        assert rules.SIMSENSE_OVERLOAD_TN == {"Light": 2, "Moderate": 3, "Serious": 5}

    def test_ic_initiative_dice(self):
        # "IC Initiative": Blue+1D6 ... Black+5D6
        assert rules.IC_INITIATIVE_DICE == {
            "Blue": 1, "Green": 2, "Orange": 3, "Red": 4, "Black": 5,
        }

    def test_ic_ratings_table(self):
        # "IC Ratings Table" columns SV<=4 / 5-7 / 8-10 / 11+
        assert rules.IC_RATINGS_TABLE == [
            ((2, 5), [4, 5, 6, 8]),
            ((6, 8), [5, 7, 8, 10]),
            ((9, 11), [6, 9, 10, 11]),
            ((12, 12), [7, 10, 12, 12]),
        ]

    def test_trap_ic_table(self):
        # "Trap IC Table": 2-5 Blaster, 6-8 Killer, 9-11 Sparky, 12 Black IC
        assert rules.SHEAF_TRAP_IC_TABLE == [
            ((2, 5), "Blaster"), ((6, 8), "Killer"),
            ((9, 11), "Sparky"), ((12, 12), "Black IC"),
        ]

    def test_crippler_target_table(self):
        # "Crippler/Ripper Target Attribute Table"
        assert rules.SHEAF_CRIPPLER_RIPPER_TARGET_TABLE == [
            ((1, 2), "Bod"), ((3, 3), "Evasion"),
            ((4, 5), "Masking"), ((6, 6), "Sensor"),
        ]


# -- Detection Factor + Hacking Pool (Matrix Overview) -------------------------

class TestDerivedStats:
    def test_detection_factor_with_sleaze(self):
        # "Average (round up) of Masking and Sleaze" -- example: 6 & 8 -> 7
        assert eng.detection_factor(masking=6, sleaze_rating=8) == 7

    def test_detection_factor_no_sleaze(self):
        # "Masking / 2 round up"
        assert eng.detection_factor(masking=6, sleaze_rating=0) == 3
        assert eng.detection_factor(masking=7, sleaze_rating=0) == 4  # ceil(3.5)

    def test_hacking_pool(self):
        # "(Intelligence + MPCP) / 3, round down"
        assert eng.hacking_pool(intelligence=5, mpcp=8) == 4   # 13//3
        assert eng.hacking_pool(intelligence=6, mpcp=6) == 4   # 12//3


# -- Dice engine (Rule of Six) -------------------------------------------------

class TestDiceEngine:
    def test_pool_floor_and_counts(self, scripted):
        scripted([4, 4, 1, 6])  # TN<=6 so no explosion
        r = eng.roll_dice(4, tn=4)
        assert r["pool"] == 4 and r["tn"] == 4
        assert r["dice"] == [4, 4, 1, 6]
        assert r["successes"] == 3   # 4,4,6 >= 4
        assert r["ones"] == 1

    def test_pool_minimum_one(self, scripted):
        scripted([5])
        r = eng.roll_dice(0, tn=4)   # pool clamped to >=1
        assert r["pool"] == 1

    def test_rule_of_six_explodes_above_tn6(self, scripted):
        # vs TN>6 a 6 is rerolled and added; keep going while the sub-roll is a 6
        scripted([6, 6, 3])  # first die: 6 -> +6 -> +3 = 15
        r = eng.roll_dice(1, tn=8)
        assert r["dice"] == [15]
        assert r["successes"] == 1   # 15 >= 8
        assert r["ones"] == 0


# -- System Test (opposed decker vs host) --------------------------------------

class TestSystemTest:
    def test_decker_wins_on_more_successes(self, scripted):
        # decker pool first (vs subsystem TN), then host pool (vs det factor)
        # decker: 3 dice all 5 (TN 4 -> 3 successes); host: 2 dice all 2 (TN 6 -> 0)
        scripted([5, 5, 5, 2, 2])
        t = eng.system_test(decker_pool=3, subsystem_rating=4, security_value=2, det_factor=6)
        assert t["success"] is True
        assert t["tally_increase"] == 0           # host successes
        assert t["decker_net_successes"] == 3

    def test_tie_is_failure(self, scripted):
        # decker 1 success, host 1 success -> tie -> fail; tally += host successes
        scripted([4, 1, 6])  # decker: [4,1] vs TN4 -> 1 success; host: [6] vs TN5 -> 1
        t = eng.system_test(decker_pool=2, subsystem_rating=4, security_value=1, det_factor=5)
        assert t["success"] is False
        assert t["tally_increase"] == 1

    def test_utility_reduces_decker_tn(self, scripted):
        # extra_tn_modifier is applied to the decker TN; floor at 2
        scripted([2, 2, 2, 1])
        t = eng.system_test(decker_pool=3, subsystem_rating=10, security_value=1,
                            det_factor=6, extra_tn_modifier=-9)
        assert t["decker_roll"]["tn"] == 2        # max(2, 10-9)=2... 10-9=1 -> floored to 2


# -- Damage staging + resistance (Icon Damage) ---------------------------------

class TestDamageStaging:
    def test_stage_up(self):
        # +1 level per 2 successes
        assert eng.stage_damage("Light", net_successes=2, direction=1) == "Moderate"
        assert eng.stage_damage("Light", net_successes=4, direction=1) == "Serious"
        assert eng.stage_damage("Light", net_successes=5, direction=1) == "Serious"  # 5//2=2

    def test_stage_down_and_clamp(self):
        assert eng.stage_damage("Serious", net_successes=2, direction=-1) == "Moderate"
        assert eng.stage_damage("Light", net_successes=10, direction=-1) == "Light"   # clamp low
        assert eng.stage_damage("Deadly", net_successes=10, direction=1) == "Deadly"  # clamp high

    def test_damage_resistance_armor_reduces_power(self, scripted):
        # Power 6, Armor 4 -> effective power 2; resist with Bod dice vs TN 2
        scripted([2, 2])  # 2 resist successes -> stage down 1
        res = eng.damage_resistance(bod=2, power=6, armor_rating=4,
                                    base_damage_level="Serious", attacker_successes=0)
        assert res["effective_power"] == 2
        assert res["final_damage_level"] == "Moderate"   # Serious staged down 1

    def test_resistance_effective_power_floor(self):
        # Armor cannot drop power below 1
        res = eng.damage_resistance(bod=1, power=2, armor_rating=10,
                                    base_damage_level="Light", attacker_successes=0)
        assert res["effective_power"] == 1


# -- Dump shock (Cybercombat / Dump Shock) -------------------------------------

class TestDumpShock:
    def test_tortoise_immune(self):
        ds = eng.dump_shock_roll(security_code="Red", security_value=8, body=4, is_tortoise=True)
        assert ds["immune"] is True

    def test_power_is_security_value_and_level_by_host(self, scripted):
        scripted([1, 1, 1, 1])  # no resist successes
        ds = eng.dump_shock_roll(security_code="Orange", security_value=9, body=4)
        assert ds["immune"] is False
        assert ds["power"] == 9
        assert ds["base_level"] == "Serious"        # Orange dump shock = Serious

    def test_cool_deck_minus2_power_and_minus1_level(self, scripted):
        scripted([1, 1, 1, 1])
        ds = eng.dump_shock_roll(security_code="Red", security_value=8, body=4, is_cool_deck=True)
        assert ds["power"] == 6                      # 8 - 2
        assert ds["base_level"] == "Serious"         # Red(Deadly) staged down 1 -> Serious

    def test_cool_and_iccm_cumulative(self, scripted):
        scripted([1, 1, 1, 1])
        ds = eng.dump_shock_roll(security_code="Red", security_value=8, body=4,
                                 is_cool_deck=True, has_iccm=True)
        assert ds["power"] == 4                       # 8 - 2 - 2
        assert ds["base_level"] == "Moderate"         # Deadly -> -2 levels -> Moderate


# -- Simsense overload (Cybercombat / Simsense Overload) -----------------------

class TestSimsense:
    def test_cool_and_tortoise_immune(self):
        assert eng.simsense_check(damage_level="Serious", willpower=4, deck_mode="cool")["immune"]
        assert eng.simsense_check(damage_level="Serious", willpower=4, deck_mode="tortoise")["immune"]

    def test_deadly_not_subject(self):
        # Deadly auto-crashes -> not a simsense case
        out = eng.simsense_check(damage_level="Deadly", willpower=4, deck_mode="hot")
        assert out["immune"] is True

    def test_tn_by_level_and_stun_on_zero(self, scripted):
        scripted([1, 1, 1, 1])  # 0 successes vs any TN -> stun taken
        out = eng.simsense_check(damage_level="Moderate", willpower=4, deck_mode="hot")
        assert out["tn"] == 3                # Moderate -> 3
        assert out["stun_taken"] is True

    def test_iccm_reduces_tn(self, scripted):
        scripted([6, 6, 6, 6])  # successes -> no stun
        out = eng.simsense_check(damage_level="Serious", willpower=4, deck_mode="hot", has_iccm=True)
        assert out["tn"] == 3                # Serious 5, ICCM -2 -> 3
        assert out["stun_taken"] is False


# -- Initiative (Cybercombat / Initiative) -------------------------------------

class TestInitiative:
    def test_ic_initiative_dice_count(self, scripted):
        scripted([3])  # each d6 -> 3
        # Red = 4D6: rating 6 + 4*3 = 18
        assert eng.ic_initiative_roll(ic_rating=6, security_code="Red") == 6 + 12

    def test_decker_response_increase_caps_at_3(self, scripted):
        scripted([1])  # each d6 -> 1
        # ri capped at 3: reaction + 6, dice = 1 + 3 = 4 -> +4
        out = eng.decker_initiative_roll(reaction=5, response_increase=9)
        assert out == (5 + 6) + 4


# -- Cybercombat attack (Resolving Attacks) ------------------------------------

class TestCybercombat:
    def test_attack_tn_by_status_and_armor(self, scripted):
        # Orange intruding TN = 4; attacker 3 dice; then resist roll
        scripted([4, 4, 4, 1, 1, 1])
        out = eng.cybercombat_attack(
            attacker_pool=3, security_code="Orange", target_status="intruding",
            target_bod=3, armor_rating=2, ic_rating=6,
        )
        assert out["attack_tn"] == 4
        assert out["base_damage_level"] == "Moderate"   # Orange IC damage
        assert out["resistance"]["effective_power"] == 4  # 6 - 2 armor


# -- Cripplers + Rippers (White/Gray IC) ---------------------------------------

class TestCrippler:
    def test_crippler_reduction_is_net_over_two(self, scripted):
        # attack (SV dice vs combat TN) then defense (attr dice vs ic rating)
        # attack: 4 successes; defense: 0 -> net 4 -> reduction 2
        scripted([6, 6, 6, 6, 1, 1, 1])
        out = eng.crippler_attack(
            security_value=4, security_code="Orange", target_status="intruding",
            target_attribute_rating=3, ic_rating=6,
        )
        assert out["attribute_reduction"] == 2     # 4 // 2

    def test_ripper_chip_is_one_per_success(self, scripted):
        # crippler attack lands (net>0), then ripper test: ic_rating dice vs mpcp+hard
        # script: attack 2 succ, defense 0 -> net 2 -> reduction 1; ripper roll 3 succ
        scripted([6, 6, 1, 1, 1, 6, 6, 6])
        out = eng.crippler_attack(
            security_value=2, security_code="Orange", target_status="intruding",
            target_attribute_rating=3, ic_rating=3, is_ripper=True,
            mpcp_rating=6, hardening=0,
        )
        assert out["is_ripper"] is True
        assert out.get("chip_damage") == out["ripper_roll"]["successes"]


# -- Tar Baby / Tar Pit (White/Gray IC) ----------------------------------------

class TestTarBaby:
    def test_ic_wins_crashes_both(self, scripted):
        # ic roll (ic_rating dice vs util TN) more successes than util roll
        scripted([6, 6, 1, 1])  # ic: 2 successes; util: 0
        out = eng.tar_baby_test(ic_rating=2, utility_rating=2)
        assert out["ic_wins"] is True
        assert out["utility_crashed"] is True and out["ic_crashed"] is True

    def test_tar_pit_corruption_on_success(self, scripted):
        # ic wins, then pit test (ic_rating dice vs mpcp) gets a success
        scripted([6, 6, 1, 1, 6])
        out = eng.tar_baby_test(ic_rating=2, utility_rating=2, is_tar_pit=True, mpcp_rating=6)
        assert out["ic_wins"] is True
        assert out["all_copies_corrupted"] is True


# -- Probe + Trace (Reactive / Trace IC) ---------------------------------------

class TestProbeTrace:
    def test_probe_tally_is_successes(self, scripted):
        scripted([6, 6, 1])  # 2 successes vs det factor
        out = eng.probe_test(ic_rating=3, det_factor=4)
        assert out["tally_increase"] == out["roll"]["successes"] == 2

    def test_trace_hunt_hit_on_any_success(self, scripted):
        scripted([6, 1, 1])
        out = eng.trace_hunt_cycle_attack(security_value=3, trace_factor=4)
        assert out["hit"] is True


# -- IC rating lookup (Random Host Rating Generation) --------------------------

class TestIcRatingLookup:
    def test_column_by_security_value(self, scripted):
        # 2D6 -> force a 7 (sum of 3+4) which lands in the 6-8 row
        scripted([3, 4])
        assert eng._ic_rating(security_value=6) == 7    # SV5-7 col -> row 6-8 = 7
        scripted([3, 4])
        assert eng._ic_rating(security_value=12) == 10  # SV11+ col -> row 6-8 = 10


# -- Sheaf generation (Mapping Matrices and Security Sheaves) ------------------

class TestSheafGeneration:
    def test_seeded_determinism(self):
        a = eng.generate_sheaf(security_code="Red", security_value=8, seed=7)
        b = eng.generate_sheaf(security_code="Red", security_value=8, seed=7)
        assert a == b

    def test_structure_triggers_increasing_and_shutdown_last(self):
        sheaf = eng.generate_sheaf(security_code="Orange", security_value=8, seed=3)
        triggers = [s["trigger"] for s in sheaf]
        assert triggers == sorted(triggers)              # monotonic non-decreasing
        assert any(e["type"] == "shutdown" for e in sheaf[-1]["events"])
        # passive + active alerts both appear somewhere
        kinds = {e["type"] for s in sheaf for e in s["events"]}
        assert "passive_alert" in kinds and "active_alert" in kinds

    @pytest.mark.xfail(reason=(
        "VR2 'Generating Trigger Steps' (vr2_rules.md): every interval is 1D3+modifier "
        "(Blue 5-7, Green 4-6, Orange 3-5, Red/Black 2-4) for ALL steps. matrix_rules."
        "SHEAF_INTERVALS uses a lower interval_range than first_range, so subsequent "
        "triggers cluster closer than the rules allow."
    ), strict=True)
    def test_interval_range_matches_first_range(self):
        for code in ("Blue", "Green", "Orange", "Red", "Black"):
            iv = rules.SHEAF_INTERVALS[code]
            assert iv["interval_range"] == iv["first_range"]
