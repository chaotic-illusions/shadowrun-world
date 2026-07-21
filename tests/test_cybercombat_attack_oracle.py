"""Cybercombat icon-damage -- rules oracle (Layer 1).

Pins the EXACT vr2 numbers for the unified cybercombat attack that ALL four directions
(IC->PC, decker->PC, PC->IC, PC->enemy) resolve through the single engine core
``eng.cybercombat_attack``. Dice are forced via a scripted RNG so each assertion is a rules
citation, not a probability.

vr2_rules.md (Cybercombat / Icon Damage / Damage Resistance) citations, encoded in
app/services/matrix_rules.py as the single source of truth:
  - Cybercombat TN Table (``COMBAT_TN``): to-hit TN by host security code and target status
    (Intruding vs Legitimate). This is the column a Validate-Passcode flip changes.
  - Icon Damage: an attack's Power = the attacking program's Rating (IC Rating for IC, the
    Attack utility Rating for a decker); the base Damage Level comes from the IC Damage Table
    (``IC_DAMAGE_LEVEL``). Stage the Damage Level UP one level for every 2 attack successes.
  - Damage Resistance: the targeted icon rolls a Bod Resistance Test (Bod dice for a persona,
    Security Value dice for IC) against a TN equal to the Power of the attack; an Armor utility
    REDUCES that Power. Stage the Damage Level DOWN one level for every 2 resistance successes.
  - Condition Monitor (``ICON_DAMAGE_BOXES``): boxes a single hit deals -- Light 1 / Moderate 2 /
    Serious 3 / Deadly 6. (``DAMAGE_BOXES`` 1/3/6/10 are the separate wound-level thresholds.)
  - Shield: net Shield parry successes cancel attack successes 1:1 BEFORE staging up (a parry
    can blunt a hit but never reverse it); Armor (a Power reduction) is a separate defence.
"""
from __future__ import annotations

import pytest

from app.services import matrix_engine as eng
from app.services import matrix_rules as rules


# -- Deterministic dice helper (mirrors test_attribute_attack_oracle._ScriptedRandom) --

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
        return 0.5

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


# =============================================================================
# Base damage level -- straight from the IC Damage Table (no staging)
# =============================================================================

@pytest.mark.parametrize("sec_code, base", [
    ("Blue", "Light"), ("Green", "Moderate"), ("Orange", "Moderate"),
    ("Red", "Serious"), ("Black", "Serious"),
])
def test_base_damage_level_matches_ic_damage_table(scripted, sec_code, base):
    """With 0 attack successes and 0 resistance successes the final Damage Level is exactly the
    IC Damage Table entry for the host security code (nothing to stage in either direction)."""
    scripted([1])   # every die shows 1 -> below any TN -> 0 successes on both rolls
    out = eng.cybercombat_attack(
        attacker_pool=1, security_code=sec_code, target_status="intruding",
        target_bod=1, ic_rating=4, attacker_is_ic=True)
    assert out["base_damage_level"] == base
    assert out["resistance"]["final_damage_level"] == base
    assert out["resistance"]["boxes"] == rules.ICON_DAMAGE_BOXES[base]


# =============================================================================
# Attack successes stage the Damage Level UP (1 level per 2 successes)
# =============================================================================

def test_attack_successes_stage_up_one_level_per_two(scripted):
    """Orange base Moderate; 4 attack successes -> +2 levels -> Deadly. Defender resists with 0
    successes so nothing stages back down: 6 boxes (a Deadly hit)."""
    # attack: 4d6 vs Orange-intruding TN 4 -> [4,4,4,4] = 4 succ.
    # resist: 6d6 vs Power 6              -> [1,1,1,1,1,1] = 0 succ.
    scripted([4, 4, 4, 4, 1, 1, 1, 1, 1, 1])
    out = eng.cybercombat_attack(
        attacker_pool=4, security_code="Orange", target_status="intruding",
        target_bod=6, ic_rating=6, attacker_is_ic=True)
    assert out["attack_tn"] == 4
    assert out["attack_roll"]["successes"] == 4
    assert out["base_damage_level"] == "Moderate"
    assert out["resistance"]["staged_up_level"] == "Deadly"
    assert out["resistance"]["resist_roll"]["successes"] == 0
    assert out["resistance"]["final_damage_level"] == "Deadly"
    assert out["resistance"]["boxes"] == 6


# =============================================================================
# Resistance successes stage the Damage Level DOWN (1 level per 2 successes)
# =============================================================================

def test_resistance_stages_down_one_level_per_two(scripted):
    """Same Deadly hit as above, but the defender scores 4 resistance successes -> -2 levels ->
    Moderate (2 boxes). Resistance never inverts a hit below the base after staging."""
    # attack: 4d6 vs TN 4 -> [4,4,4,4] = 4 succ (staged up to Deadly).
    # resist: 6d6 vs Power 6 -> [6,6,6,6,1,1] = 4 succ -> stage Deadly down 2 -> Moderate.
    scripted([4, 4, 4, 4, 6, 6, 6, 6, 1, 1])
    out = eng.cybercombat_attack(
        attacker_pool=4, security_code="Orange", target_status="intruding",
        target_bod=6, ic_rating=6, attacker_is_ic=True)
    assert out["resistance"]["staged_up_level"] == "Deadly"
    assert out["resistance"]["resist_roll"]["successes"] == 4
    assert out["resistance"]["final_damage_level"] == "Moderate"
    assert out["resistance"]["boxes"] == 2


# =============================================================================
# Power = attacking program rating; Armor reduces Power (not the to-hit TN)
# =============================================================================

def test_power_is_attack_rating_and_armor_reduces_it(scripted):
    """The resistance TN is the attack Power (ic_rating = attacking program rating). An Armor
    utility subtracts from that Power ONLY -- the to-hit TN stays the host's Cybercombat TN."""
    # attack: 2d6 vs Orange TN 4 -> [4,4] = 2 succ -> Moderate staged up 1 -> Serious.
    # resist: 3d6 vs effective Power (8 - 3 armor = 5) -> [1,1,1] = 0 succ -> stays Serious.
    scripted([4, 4, 1, 1, 1])
    out = eng.cybercombat_attack(
        attacker_pool=2, security_code="Orange", target_status="intruding",
        target_bod=3, ic_rating=8, armor_rating=3, attacker_is_ic=True)
    assert out["attack_tn"] == 4                          # to-hit TN unchanged by Armor
    assert out["resistance"]["effective_power"] == 5      # Power 8 - Armor 3
    assert out["resistance"]["resist_roll"]["tn"] == 5    # defender rolled Bod vs the reduced Power
    assert out["resistance"]["staged_up_level"] == "Serious"
    assert out["resistance"]["final_damage_level"] == "Serious"
    assert out["resistance"]["boxes"] == 3


# =============================================================================
# To-hit TN column -- Intruding vs Legitimate (the Validate-Passcode axis)
# =============================================================================

@pytest.mark.parametrize("sec_code, status, tn", [
    ("Orange", "intruding", 4), ("Orange", "legitimate", 5),
    ("Red", "intruding", 3),    ("Red", "legitimate", 6),
    ("Blue", "intruding", 6),   ("Blue", "legitimate", 3),
])
def test_target_status_selects_combat_tn_column(scripted, sec_code, status, tn):
    """The to-hit TN is COMBAT_TN[security_code][status]. Flipping a target Intruding->Legitimate
    (Validate Passcode) swaps the column, changing the to-hit TN for the same attacker."""
    scripted([1])
    out = eng.cybercombat_attack(
        attacker_pool=1, security_code=sec_code, target_status=status,
        target_bod=1, ic_rating=4, attacker_is_ic=True)
    assert out["attack_tn"] == tn
    assert rules.COMBAT_TN[sec_code][status] == tn


def test_tn_modifier_floors_at_two(scripted):
    """A negative tn_modifier (e.g. a Position/Targeting bonus) can never push the to-hit TN below
    2 -- max(2, base + modifier)."""
    scripted([1])
    out = eng.cybercombat_attack(
        attacker_pool=1, security_code="Red", target_status="intruding",
        target_bod=1, ic_rating=4, attacker_is_ic=True, tn_modifier=-5)
    assert out["attack_tn"] == 2   # Red-intruding 3 - 5 -> floored at 2


# =============================================================================
# Shield parry blunts BEFORE staging (successes cancelled 1:1, clamped at 0)
# =============================================================================

def test_shield_successes_cancel_attack_successes_before_staging(scripted):
    """4 attack successes with 2 Shield parry successes -> net 2 -> +1 level only (Moderate ->
    Serious), NOT +2. Shield reduces successes; Armor (separately) reduces Power."""
    # attack: 4d6 vs Orange TN 4 -> [4,4,4,4] = 4 succ; shield cancels 2 -> net 2 -> Serious.
    # resist: 3d6 vs Power 4 -> [1,1,1] = 0 succ -> stays Serious.
    scripted([4, 4, 4, 4, 1, 1, 1])
    out = eng.cybercombat_attack(
        attacker_pool=4, security_code="Orange", target_status="intruding",
        target_bod=3, ic_rating=4, attacker_is_ic=True, shield_successes=2)
    assert out["attack_roll"]["successes"] == 4
    assert out["resistance"]["shield_successes"] == 2
    assert out["resistance"]["attacker_successes"] == 2       # net after the parry
    assert out["resistance"]["staged_up_level"] == "Serious"  # +1 level, not +2
    assert out["resistance"]["final_damage_level"] == "Serious"
    assert out["resistance"]["boxes"] == 3
