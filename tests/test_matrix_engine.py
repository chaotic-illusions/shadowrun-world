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
        # Wound-level thresholds (1/3/6/10) + the "None" (0) fully-resisted floor.
        assert rules.DAMAGE_BOXES == {"None": 0, "Light": 1, "Moderate": 3, "Serious": 6, "Deadly": 10}

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
        assert rules.COMBAT_TN["Red"] == {"intruding": 3, "legitimate": 6}
        assert rules.COMBAT_TN["Black"] == {"intruding": 3, "legitimate": 6}

    def test_simsense_overload_tn(self):
        # "Simsense Overload TN": L2 M3 S5 (no Deadly entry)
        assert rules.SIMSENSE_OVERLOAD_TN == {"Light": 2, "Moderate": 3, "Serious": 5}

    def test_medic_tn(self):
        # vr2 Medic Target Numbers Table: Light 4 / Moderate 5 / Serious 6 (no Deadly entry)
        assert rules.MEDIC_TN == {"Light": 4, "Moderate": 5, "Serious": 6}

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

    def test_tie_goes_to_decker(self, scripted):
        # House rule (vr2 line 152, modified): decker 1 success, host 1 success -> tie -> the
        # decker SUCCEEDS; tally still += host successes.
        scripted([4, 1, 6])  # decker: [4,1] vs TN4 -> 1 success; host: [6] vs TN5 -> 1
        t = eng.system_test(decker_pool=2, subsystem_rating=4, security_value=1, det_factor=5)
        assert t["success"] is True
        assert t["tally_increase"] == 1

    def test_zero_vs_zero_tie_is_a_mutual_whiff(self, scripted):
        # House rule edge: a 0-vs-0 tie means EVERYTHING missed -> nothing happened -> the task
        # fails. The decker needs at least 1 success for a tie to count.
        scripted([1, 1, 1])  # decker: [1,1] vs TN4 -> 0 success; host: [1] vs TN5 -> 0
        t = eng.system_test(decker_pool=2, subsystem_rating=4, security_value=1, det_factor=5)
        assert t["success"] is False
        assert t["tally_increase"] == 0

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
        # Staging DOWN below Light reaches "None" (fully resisted -- no damage), then clamps there.
        assert eng.stage_damage("Light", net_successes=2, direction=-1) == "None"
        assert eng.stage_damage("Light", net_successes=10, direction=-1) == "None"   # clamp low
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

    def test_hot_dnil_adds_two_to_tn(self, scripted):
        # vr2 Simsense Overload: "Running hot with DNI-only interface: +2 to TN."
        scripted([1])                        # roll outcome irrelevant; asserting the TN only
        out = eng.simsense_check(damage_level="Moderate", willpower=4,
                                 deck_mode="hot", hot_dnil_only=True)
        assert out["tn"] == 5                # Moderate 3, +2 pure-DNI

    def test_hot_dnil_and_iccm_cancel(self, scripted):
        # The ICCM filter (-2) exactly offsets the pure-DNI penalty (+2).
        scripted([1])
        out = eng.simsense_check(damage_level="Moderate", willpower=4,
                                 deck_mode="hot", hot_dnil_only=True, has_iccm=True)
        assert out["tn"] == 3                # Moderate 3, +2 DNI, -2 ICCM

    def test_tn_floors_at_two(self, scripted):
        scripted([1])
        out = eng.simsense_check(damage_level="Light", willpower=4,
                                 deck_mode="hot", has_iccm=True)
        assert out["tn"] == 2                # Light 2, -2 ICCM -> 0, floored to 2


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

    def test_decker_hot_dni_adds_one_die(self, scripted):
        scripted([1])  # each d6 -> 1
        # Hot deck on pure DNI: base 1D6 + hot 1D6 = 2 dice; no RI -> reaction unchanged
        out = eng.decker_initiative_roll(
            reaction=5, response_increase=0, has_hot_dnl=True, deck_mode="hot")
        assert out == 5 + 2

    def test_decker_cool_deck_loses_one_init_die(self, scripted):
        scripted([1])  # each d6 -> 1
        # Cool deck: -1D6. ri=2 -> reaction 5+4=9, dice = 1 + 2 - 1 = 2 -> +2
        out = eng.decker_initiative_roll(
            reaction=5, response_increase=2, deck_mode="cool")
        assert out == (5 + 4) + 2

    def test_decker_cool_deck_never_drops_below_one_die(self, scripted):
        scripted([1])  # each d6 -> 1
        # No RI: base 1 die - 1 (cool) floors at 1 (SR2 minimum) -> reaction + 1
        out = eng.decker_initiative_roll(
            reaction=4, response_increase=0, deck_mode="cool")
        assert out == 4 + 1

    def test_decker_tortoise_halves_reaction_and_rolls_single_die(self, scripted):
        scripted([6])  # the single init die -> 6 (init dice do not explode)
        # Tortoise: half Reaction (7 -> 3, min 1), 1 die regardless of RI/RF, no RI reaction bonus
        out = eng.decker_initiative_roll(
            reaction=7, response_increase=3, has_reality_filter=True, deck_mode="tortoise")
        assert out == 3 + 6

    def test_decker_tortoise_reaction_floors_at_one(self, scripted):
        scripted([2])  # the single init die -> 2
        # Reaction 1 -> half = 0 -> floored to 1; single die
        out = eng.decker_initiative_roll(reaction=1, response_increase=0, deck_mode="tortoise")
        assert out == 1 + 2


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


# -- Shield parry gate: fires ONLY when the attack lands (vr2) ------------------

class TestShieldParryGate:
    def test_shield_not_fired_on_a_clean_miss(self, scripted):
        # Attacker rolls all 1s vs TN 4 -> 0 successes; the persona is never affected, so the
        # deferred Shield callback must NOT be invoked (no roll, no wear).
        scripted([1, 1, 1, 1, 1, 1])
        calls = []
        out = eng.cybercombat_attack(
            attacker_pool=3, security_code="Orange", target_status="intruding",
            target_bod=3, armor_rating=0, ic_rating=6,
            shield_parry=lambda: (calls.append(1) or 2),
        )
        assert out["attack_roll"]["successes"] == 0
        assert calls == []                              # callback never fired

    def test_shield_fired_when_the_attack_lands(self, scripted):
        # Attacker rolls successes vs TN 4 -> the strike lands, so the callback fires and its
        # returned successes are applied to the resistance stage.
        scripted([6, 6, 1, 1, 1])
        calls = []
        out = eng.cybercombat_attack(
            attacker_pool=3, security_code="Orange", target_status="intruding",
            target_bod=3, armor_rating=0, ic_rating=6,
            shield_parry=lambda: (calls.append(1) or 2),
        )
        assert out["attack_roll"]["successes"] > 0
        assert calls == [1]                             # callback fired exactly once
        # The parried successes are surfaced in the resistance stage (2 parried off the hit).
        assert out["resistance"]["shield_successes"] == 2


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


# -- Shield utility on DEFENSE (Utility Programs / Shield) ----------------------

class TestShieldDefense:
    """vr2_rules Shield: 'Parry attacks in cybercombat. When an attack affects the decker's
    persona, make a Shield Test (TN = attacker skill). Net successes reduce the attacker's
    damage successes. Effective against crippler/ripper attacks: add Shield Test successes to
    the decker's opposed test successes. Shield loses 1 Rating Point every time it is used.'"""

    def test_shield_parry_rolls_effective_rating_vs_attacker_skill(self, scripted):
        scripted([6, 5, 1])                # Shield-3 vs TN 5 -> 6,5 hit
        out = eng.shield_parry(shield_rating=3, attacker_skill=5)
        assert out["shield_rating"] == 3
        assert out["tn"] == 5
        assert out["successes"] == 2
        assert out["roll"]["dice"] == [6, 5, 1]

    def test_shield_parry_floors_rating_and_tn(self, scripted):
        scripted([6])
        out = eng.shield_parry(shield_rating=0, attacker_skill=1)
        assert out["shield_rating"] == 1   # rating floored to 1 die
        assert out["tn"] == 2              # TN floored to 2
        assert out["successes"] == 1

    def test_shield_reduces_attacker_successes_before_staging(self, scripted):
        # 4 attack successes would stage Light -> Serious; 2 Shield successes -> net 2 -> Moderate
        scripted([1])                      # defender Bod resist roll (1 die) -> 0 successes
        res = eng.damage_resistance(
            bod=1, power=4, base_damage_level="Light",
            attacker_successes=4, shield_successes=2)
        assert res["attacker_successes"] == 2          # 4 - 2 shield
        assert res["shield_successes"] == 2
        assert res["staged_up_level"] == "Moderate"    # 2 net successes -> +1 level only
        assert res["final_damage_level"] == "Moderate"

    def test_shield_never_reverses_a_hit(self, scripted):
        scripted([1])
        res = eng.damage_resistance(
            bod=1, power=4, base_damage_level="Moderate",
            attacker_successes=1, shield_successes=5)
        assert res["attacker_successes"] == 0          # clamped at 0, not negative
        assert res["staged_up_level"] == "Moderate"    # no stage-up

    def test_shield_adds_to_crippler_defence(self, scripted):
        # attack 4 succ, defense 0, shield 2 -> net 4-0-2 = 2 -> reduction 1 (vs 2 without shield)
        scripted([6, 6, 6, 6, 1, 1, 1])
        out = eng.crippler_attack(
            security_value=4, security_code="Orange", target_status="intruding",
            target_attribute_rating=3, ic_rating=6, shield_successes=2)
        assert out["shield_successes"] == 2
        assert out["net_successes"] == 2
        assert out["attribute_reduction"] == 1

    def test_shield_adds_to_decker_attribute_attack_defence(self, scripted):
        # enemy-decker Poison/Restrict/Reveal: attack 4, resist 0, shield 2 -> net 2 -> reduction 1
        scripted([6, 6, 6, 6, 1, 1, 1])
        out = eng.attribute_attack_core(
            attacker_pool=4, resist_tn=6, security_code="Orange", target_status="intruding",
            target_attribute_rating=3, shield_successes=2)
        assert out["shield_successes"] == 2
        assert out["net"] == 2
        assert out["reduction"] == 1

    def test_decker_attribute_attack_pc_direction_omits_shield(self, scripted):
        # PC firing Poison / Restrict / Reveal at an enemy decker: omitting the Shield param
        # leaves shield_successes 0, and the reduction is always floor(net / 2) per the rule.
        scripted([5, 5, 5, 1, 1, 1, 1, 1])
        out = eng.attribute_attack_core(
            attacker_pool=5, resist_tn=6, security_code="Orange", target_status="intruding",
            target_attribute_rating=4)
        assert out["shield_successes"] == 0
        assert out["reduction"] == out["net"] // 2

    def test_shield_stages_data_bomb_damage_down(self, scripted):
        # Data bomb is a fixed (rating)M -- Shield successes stage the resolved damage DOWN
        scripted([1, 1, 1])                # Bod resist (3 dice) -> 0 successes -> Moderate
        det = eng.data_bomb_detonate(ic_rating=6, target_bod=3, shield_successes=2)
        assert det["resistance"]["final_damage_level"] == "Light"   # Moderate -1 level
        assert det["resistance"]["shield_successes"] == 2

    def test_data_bomb_without_shield_stays_moderate(self, scripted):
        scripted([1, 1, 1])
        det = eng.data_bomb_detonate(ic_rating=6, target_bod=3)
        assert det["resistance"]["final_damage_level"] == "Moderate"


class TestMedicHeal:
    """vr2 Medic: 'Heals the decker's icon. Make a Medic Test against a target number based on the
    damage to the Icon (Light 4 / Moderate 5 / Serious 6). Recovers 1 box per success. Medic loses
    1 Rating Point each time it is used, regardless of outcome.' (matrix_engine.medic_heal is the
    pure roll -- the run engine applies/caps the boxes and degrades the program.)"""

    def test_medic_tn_for_light_wound(self, scripted):
        scripted([4, 1])                   # Medic-2 vs Light TN 4 -> 4 hits, 1 misses
        out = eng.medic_heal(medic_rating=2, wound_level="Light")
        assert out["tn"] == 4
        assert out["wound_level"] == "Light"
        assert out["medic_rating"] == 2
        assert out["boxes_healed"] == 1
        assert out["roll"]["dice"] == [4, 1]

    def test_medic_tn_for_moderate_wound(self, scripted):
        scripted([5, 4])                   # Medic-2 vs Moderate TN 5 -> only the 5 hits
        out = eng.medic_heal(medic_rating=2, wound_level="Moderate")
        assert out["tn"] == 5
        assert out["boxes_healed"] == 1

    def test_medic_tn_for_serious_wound(self, scripted):
        scripted([6, 6, 1])                # Medic-3 vs Serious TN 6 -> two 6s hit
        out = eng.medic_heal(medic_rating=3, wound_level="Serious")
        assert out["tn"] == 6
        assert out["boxes_healed"] == 2

    def test_medic_boxes_equal_successes(self, scripted):
        scripted([4, 4, 4, 1])             # Medic-4 vs Light TN 4 -> 3 successes
        out = eng.medic_heal(medic_rating=4, wound_level="Light")
        assert out["boxes_healed"] == 3
        assert out["roll"]["successes"] == 3

    def test_medic_floors_rating_to_one_die(self, scripted):
        scripted([6])
        out = eng.medic_heal(medic_rating=0, wound_level="Light")
        assert out["medic_rating"] == 1   # rating floored to a single die
        assert out["boxes_healed"] == 1


class TestRestoreRepair:
    """vr2 Restore: 'Repairs damage to online icon attributes. Cannot repair permanent damage to
    Persona chips caused by gray or black IC. Restore Test: TN = rating of the program that caused
    the damage (highest if several). Repairs 1 point of damage per 2 successes.' Unlike Medic,
    Restore does NOT lose a Rating Point per use. matrix_engine.restore_repair is the pure roll --
    the run engine selects the attribute, supplies the repairable (temporary-only) damage, and
    applies the result."""

    def test_restore_tn_is_the_causing_program_rating(self, scripted):
        scripted([5, 5, 1])               # Restore-3 vs TN 5 -> two 5s hit
        out = eng.restore_repair(restore_rating=3, causing_rating=5, damage_points=4)
        assert out["tn"] == 5
        assert out["restore_rating"] == 3
        assert out["causing_rating"] == 5
        assert out["successes"] == 2
        assert out["points_repaired"] == 1            # 2 successes // 2
        assert out["roll"]["dice"] == [5, 5, 1]

    def test_restore_points_are_successes_floordiv_two(self, scripted):
        scripted([4, 4, 4, 4, 4, 1])      # Restore-5 vs TN 4 -> 5 successes
        out = eng.restore_repair(restore_rating=5, causing_rating=4, damage_points=10)
        assert out["successes"] == 5
        assert out["points_repaired"] == 2            # 5 // 2 = 2 (odd success is wasted)

    def test_restore_points_capped_by_damage(self, scripted):
        scripted([4, 4, 4, 4, 4, 4])      # Restore-6 vs TN 4 -> 6 successes -> 3 points...
        out = eng.restore_repair(restore_rating=6, causing_rating=4, damage_points=1)
        assert out["successes"] == 6
        assert out["points_repaired"] == 1            # ...but only 1 point of damage exists

    def test_restore_floors_rating_and_tn(self, scripted):
        scripted([6])
        out = eng.restore_repair(restore_rating=0, causing_rating=1, damage_points=5)
        assert out["restore_rating"] == 1            # rating floored to a single die
        assert out["tn"] == 2                         # TN floored to 2
        assert out["successes"] == 1
        assert out["points_repaired"] == 0            # 1 success // 2 = 0 (needs 2 per point)

    def test_restore_zero_successes_repairs_nothing(self, scripted):
        scripted([1, 1, 1])               # Restore-3 vs TN 6 -> no hits
        out = eng.restore_repair(restore_rating=3, causing_rating=6, damage_points=4)
        assert out["successes"] == 0
        assert out["points_repaired"] == 0

    def test_restore_explodes_sixes_to_beat_a_high_causing_rating(self, scripted):
        # Rule of 6: a flat d6 maxes at 6 and could never beat TN 8 -- exploding sixes must apply.
        scripted([6, 6, 5, 5])            # Restore-2 vs TN 8: each 6 re-rolls +5 = 11 >= 8
        out = eng.restore_repair(restore_rating=2, causing_rating=8, damage_points=3)
        assert out["tn"] == 8
        assert out["successes"] == 2                  # both dice exploded past TN 8
        assert out["points_repaired"] == 1            # 2 // 2


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


class TestSteamroller:
    """vr2_rules.md L1581-1585 -- Steamroller is the anti-tar weapon: it inflicts (Rating)D on a
    Tar Baby / Tar Pit and is IMMUNE to the tar crash-backlash (it never runs tar_baby_test). The
    engine resolves it as a normal IC-damage hit so the existing staging math decides the outcome:
    a solid (Rating)D chips the tar's full 10-box condition monitor (TAR_IC_CONDITION_BOXES) and a
    two-strike Steamroller crashes it, while a badly under-rated Steamroller (low Power) lets the
    tar stage the Deadly hit down to a survivable graze."""

    def test_tar_condition_monitor_is_full(self):
        # A tar IC uses the SAME 10-box monitor as any other IC (user ruling 2026-07-17).
        assert eng.TAR_IC_CONDITION_BOXES == 10

    def test_full_rating_two_strikes_crash_the_tar(self, scripted):
        # Power 6 -> the tar resists vs TN 6: 4s are NOT successes, so the Deadly hit stands
        # (6 icon boxes). One strike does NOT fill the 10-box track; a second accumulates to
        # 12 >= 10 and crashes it.
        scripted([4])
        out = eng.steamroller_attack(steamroller_rating=6, steamroller_pool=6, tar_ic_rating=6)
        assert out["damage_level"] == "Deadly"
        assert out["boxes"] == 6
        assert out["total_boxes"] == 6
        assert out["crashed"] is False
        scripted([4])
        out2 = eng.steamroller_attack(steamroller_rating=6, steamroller_pool=6,
                                      tar_ic_rating=6, existing_boxes=out["total_boxes"])
        assert out2["total_boxes"] == 12
        assert out2["crashed"] is True

    def test_very_low_rating_can_fail(self, scripted):
        # Under net-successes-first staging the tar only stages the Deadly hit down by the amount
        # its resistance EXCEEDS the to-hit successes. A rating-1 Steamroller (Power 1 -> the tar
        # resists at TN 2) that also rolls a weak to-hit is out-resisted: to-hit rolls 6 misses
        # (0 succ), the tar resists with 6 hits -> net -6 -> Deadly staged all the way down to a
        # Light graze (1 box < 10). The tar survives. Draw order: 6 to-hit dice, then 6 resist dice.
        scripted([1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4])
        out = eng.steamroller_attack(steamroller_rating=1, steamroller_pool=6, tar_ic_rating=6)
        assert out["damage_level"] == "Light"
        assert out["total_boxes"] < eng.TAR_IC_CONDITION_BOXES
        assert out["crashed"] is False

    def test_resisting_nothing_still_needs_accumulation(self, scripted):
        # Tar rolls all 1s (resists nothing) -> the Deadly hit stands regardless of Power, dealing
        # 6 icon boxes. A single hit no longer fills the 10-box track, so it does not crash yet.
        scripted([1])
        out = eng.steamroller_attack(steamroller_rating=2, steamroller_pool=6, tar_ic_rating=8)
        assert out["damage_level"] == "Deadly"
        assert out["boxes"] == 6
        assert out["crashed"] is False

    def test_boxes_accumulate_across_strikes(self, scripted):
        # A single out-resisted strike only grazes (Light, 1 box), but it adds to existing damage:
        # 1 + 9 prior boxes = 10 reaches the monitor and crashes the tar. To-hit rolls 6 misses
        # (0 succ), the tar resists with 6 hits -> net -6 -> Light. Draw order: 6 to-hit, 6 resist.
        scripted([1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4])
        out = eng.steamroller_attack(steamroller_rating=1, steamroller_pool=6,
                                     tar_ic_rating=6, existing_boxes=9)
        assert out["boxes"] == 1
        assert out["total_boxes"] == 10
        assert out["crashed"] is True
        assert out["crashed"] is True


class TestSlowEngine:
    """vr2_rules.md L1572-1578 -- the Slow utility's opposed Resistance (Slow Rating) Test.
    ``slow_test`` is the PURE dice helper: the decker (the Slow program) and the IC make a
    symmetric SR2 opposed test (like ``tar_baby_test``) and the IC loses one action per 2 NET
    successes -- a pure floor (``actions_lost = max(0, net) // 2``). The run layer applies the
    min-one-on-a-win and the hang/resume rules; the engine only reports the math."""

    @pytest.mark.parametrize("d_succ,i_succ,exp_net,exp_lost", [
        (4, 0, 4, 2),    # net 4 -> 2 actions
        (3, 0, 3, 1),    # net 3 -> 1 (floor)
        (2, 0, 2, 1),    # net 2 -> 1
        (1, 0, 1, 0),    # net 1 -> 0 (the caller applies the min-one-on-win)
        (5, 1, 4, 2),    # IC resists one; net 4 -> 2
        (2, 2, 0, 0),    # tie -> no effect
        (1, 3, -2, 0),   # IC wins -> negative net, 0 actions
    ])
    def test_actions_lost_is_floor_of_net_over_two(self, scripted, d_succ, i_succ,
                                                   exp_net, exp_lost):
        # Both sides roll 6 dice vs TN 6 (slow_rating == ic_dice == 6): a 6 is a hit and -- at
        # TN 6 -- does NOT explode (the rule of 6 only fires above TN 6), so the scripted
        # successes are exact. Decker dice come first, then the IC's.
        decker = [6] * d_succ + [1] * (6 - d_succ)
        ic = [6] * i_succ + [1] * (6 - i_succ)
        scripted(decker + ic)
        out = eng.slow_test(decker_pool=6, slow_rating=6, ic_dice=6)
        assert out["decker_roll"]["successes"] == d_succ
        assert out["ic_roll"]["successes"] == i_succ
        assert out["net_successes"] == exp_net
        assert out["actions_lost"] == exp_lost

    def test_tie_or_loss_costs_no_actions(self, scripted):
        # IC ties the decker (2 vs 2) -> net 0 -> 0 actions lost (the "IC more or equal successes:
        # no effect" clause; the run layer reports this as 'resisted').
        scripted([6, 6, 1, 1, 1, 1] + [6, 6, 1, 1, 1, 1])
        out = eng.slow_test(decker_pool=6, slow_rating=6, ic_dice=6)
        assert out["net_successes"] == 0 and out["actions_lost"] == 0

    def test_rule_of_six_lets_slow_beat_a_high_rating_ic(self, scripted):
        # vs a Rating-8 IC the decker's TN is 8 (> 6), so 6s EXPLODE: a die 6 then 3 totals 9 >= 8.
        # Without the rule of 6 the test would be unbeatable (a flat d6 maxes at 6). roll_dice rolls
        # BOTH base dice first ([6, 6]) and then explodes each (+3 -> 9), so the scripted order is
        # base sixes then their rerolls. The IC (TN = slow_rating 4) rolls all 1s -> 0. net 2 -> 1.
        scripted([6, 6, 3, 3] + [1, 1, 1, 1, 1, 1, 1, 1])
        out = eng.slow_test(decker_pool=2, slow_rating=4, ic_dice=8)
        assert out["decker_roll"]["successes"] == 2
        assert out["ic_roll"]["successes"] == 0
        assert out["net_successes"] == 2 and out["actions_lost"] == 1


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

    def test_structure_triggers_increasing_and_alerts_escalate_in_order(self):
        # vr2 L857-873 (RAW): alert state EMERGES from the per-step 1D6+ramp roll and escalates in
        # strict order No -> Passive -> Active -> Shutdown; it is not pinned to fixed positions and
        # shutdown is not guaranteed. Over a long sheaf the ramp forces at least Passive then Active.
        sheaf = eng.generate_sheaf(security_code="Orange", security_value=8,
                                   step_count=24, seed=3)
        triggers = [s["trigger"] for s in sheaf]
        assert triggers == sorted(triggers)              # monotonic non-decreasing
        # Collect alert markers in step order and confirm they only ever climb the severity ladder.
        severity = {"passive_alert": 1, "active_alert": 2, "shutdown": 3}
        seen = [e["type"] for s in sheaf for e in s["events"] if e["type"] in severity]
        levels = [severity[k] for k in seen]
        assert levels == sorted(levels)                  # never de-escalates
        assert "passive_alert" in seen and "active_alert" in seen
        assert seen.index("passive_alert") < seen.index("active_alert")


    def test_interval_range_matches_first_range(self):
        # VR2 "Generating Trigger Steps": every interval is 1D3+modifier for ALL steps,
        # so interval_range must equal first_range for each code (fixed: was lower).
        for code in ("Blue", "Green", "Orange", "Red", "Black"):
            iv = rules.SHEAF_INTERVALS[code]
            assert iv["interval_range"] == iv["first_range"]
