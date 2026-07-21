"""Black-family attack -- rules oracle (Layer 1).

Pins the EXACT vr2 numbers for the single engine core ``eng.black_attack`` that EVERY Black-family
strike resolves through -- enemy Black IC (lethal + non-lethal), an enemy decker's Black Hammer /
Killjoy, and the PC's own Black Hammer / Killjoy. Dice are forced via a scripted RNG so each
assertion is a rules citation, not a probability.

vr2_rules.md citations:
  - Black IC (lethal, ~L615-635): "Fights like killer IC. Damage Code based on host Security
    Code" -> base Damage Level = ``IC_DAMAGE_LEVEL[sec]`` with Power = IC Rating. "Stage up one
    level for every 2 successes on the IC's Attack Test." "On each hit the decker makes TWO
    Resistance Tests: (1) a Body Test to resist damage to his physical body -- Hardening reduces
    Power; (2) a Bod Test to resist damage to the icon -- Hardening reduces Power and Armor
    protects normally."  => ONE Attack Test drives BOTH resistance tests off the same successes.
  - Black IC (non-lethal, ~L639-647): "Same as lethal black IC, except: causes Stun (not
    Physical); the decker resists with Willpower Tests." => the meat test flips Body->Willpower
    (Stun); the Bod->icon test remains.
  - Black Hammer (decker program, ~L1533, Multiplier 20): "Functions like black IC but from a
    decker. If the attack hits, the target resists with Body (damage to person) AND Bod (damage
    to icon). Hardening reduces the damage target number for resistance tests."
  - Killjoy (decker program, ~L1551, Multiplier 10): "Functions exactly like Black Hammer,
    except it does Stun damage instead of Physical."
  - Cybercombat TN Table (``COMBAT_TN``): to-hit TN by host Security Code and target status.
  - Damage Resistance / Condition Monitor (``ICON_DAMAGE_BOXES``, boxes a hit deals): Light 1 /
    Moderate 2 / Serious 3 / Deadly 6; Shield parry cancels attack successes 1:1 BEFORE staging up; Armor reduces Power.

House ruling encoded by the router callers (documented, not asserted here): the Black Hammer /
Killjoy PROGRAMS use a fixed "Serious" base regardless of host code, while Black IC (the construct)
uses the host Security Code table. ``black_attack`` itself is base-agnostic -- the caller supplies
``base_damage_level`` -- so this oracle exercises the rider with several bases.
"""
from __future__ import annotations

import pytest

from app.services import matrix_engine as eng
from app.services import matrix_rules as rules


# -- Deterministic dice helper (mirrors test_cybercombat_attack_oracle._ScriptedRandom) --

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
# Base damage level -- supplied by the caller (the actor/program rider)
# =============================================================================

@pytest.mark.parametrize("base", ["Light", "Moderate", "Serious", "Deadly"])
def test_base_damage_level_is_caller_supplied(scripted, base):
    """With 0 attack successes and 0 resistance successes the final icon/meat Damage Level is
    exactly the caller-supplied base (nothing to stage in either direction)."""
    scripted([1])   # every die shows 1 -> below any TN -> 0 successes on every roll
    out = eng.black_attack(
        attacker_pool=1, security_code="Red", base_damage_level=base,
        power=4, icon_bod=1, meat_pool=1)
    assert out["base_damage_level"] == base
    assert out["icon"]["final_damage_level"] == base
    assert out["meat"]["final_damage_level"] == base


def test_black_ic_base_follows_host_security_code_table(scripted):
    """A black-IC caller passes ``IC_DAMAGE_LEVEL[sec]`` -- verify the rider carries the host-code
    table entry through unchanged (Red -> Serious)."""
    scripted([1])
    out = eng.black_attack(
        attacker_pool=1, security_code="Red",
        base_damage_level=rules.IC_DAMAGE_LEVEL["Red"], power=4, icon_bod=1)
    assert out["base_damage_level"] == "Serious"


# =============================================================================
# ONE Attack Test drives BOTH resistance tests (the defining Black rule)
# =============================================================================

def test_single_attack_roll_stages_both_icon_and_meat(scripted):
    """4 attack successes stage the base UP by 4//2 = 2 levels for BOTH the icon (Bod) and the
    meat (Body/Willpower) test -- they share the one Attack Test's successes."""
    # attack pool 4 (all 5s vs Red-intruding TN 3 -> 4 successes); icon 1 die + meat 1 die (1s ->
    # 0 resist successes). Draw order: attack(4) -> icon(1) -> meat(1) = 6 draws.
    scripted([5, 5, 5, 5, 1, 1])
    out = eng.black_attack(
        attacker_pool=4, security_code="Red", target_status="intruding",
        base_damage_level="Serious", power=9, icon_bod=1, meat_pool=1)
    # Serious (index 2) + 2 levels -> Deadly (clamped top).
    assert out["icon"]["final_damage_level"] == "Deadly"
    assert out["meat"]["final_damage_level"] == "Deadly"
    # Icon damage uses the icon box table (Deadly = 6); meat uses the 1/3/6/10 body table (Deadly = 10).
    assert out["icon"]["boxes"] == 6 and out["meat"]["boxes"] == 10
    # Both resistance tests staged from the SAME attack successes.
    assert out["icon"]["attacker_successes"] == out["meat"]["attacker_successes"] == 4


def test_resistance_stages_both_tests_down(scripted):
    """4 resistance successes on each test stage the base DOWN by 2 levels for BOTH icon and meat."""
    # attack 1 die (1 -> 0 successes); icon 4 dice + meat 4 dice (5s vs Power 4 -> 4 successes each).
    scripted([1, 5, 5, 5, 5, 5, 5, 5, 5])
    out = eng.black_attack(
        attacker_pool=1, security_code="Red", target_status="intruding",
        base_damage_level="Serious", power=4, icon_bod=4, meat_pool=4)
    # Serious (index 2) - 2 levels -> Light.
    assert out["icon"]["final_damage_level"] == "Light"
    assert out["meat"]["final_damage_level"] == "Light"
    assert out["icon"]["boxes"] == 1 and out["meat"]["boxes"] == 1


# =============================================================================
# Hardening / Armor -- Power reductions
# =============================================================================

def test_hardening_reduces_both_resist_powers(scripted):
    """Hardening reduces the Power (resistance TN) of BOTH the icon and the meat test (vr2:
    'Hardening reduces the damage target number for resistance tests')."""
    scripted([1])
    out = eng.black_attack(
        attacker_pool=1, security_code="Red", base_damage_level="Serious",
        power=8, hardening=3, icon_bod=1, icon_armor=0, meat_pool=1)
    assert out["icon"]["effective_power"] == 5   # 8 - 3 hardening
    assert out["meat"]["effective_power"] == 5   # 8 - 3 hardening (Armor does not apply to meat)


def test_armor_reduces_icon_power_only_not_meat(scripted):
    """Armor protects the ICON (vr2: 'Armor protects normally' on the Bod test) but NOT the
    operator's flesh -- the meat resist Power is unreduced by Armor."""
    scripted([1])
    out = eng.black_attack(
        attacker_pool=1, security_code="Red", base_damage_level="Serious",
        power=6, hardening=0, icon_bod=1, icon_armor=2, meat_pool=1)
    assert out["icon"]["effective_power"] == 4   # 6 - 2 armor
    assert out["meat"]["effective_power"] == 6   # armor does not reach the operator


def test_shield_cancels_attack_successes_before_staging_on_both(scripted):
    """Net Shield parry successes cancel attack successes 1:1 BEFORE staging up -- and because the
    one strike drives both tests, the parry blunts the icon AND the meat identically."""
    # 4 attack successes, Shield cancels 2 -> net 2 -> +1 level from Moderate -> Serious (both).
    scripted([5, 5, 5, 5, 1, 1])
    out = eng.black_attack(
        attacker_pool=4, security_code="Red", target_status="intruding",
        base_damage_level="Moderate", power=9, icon_bod=1, meat_pool=1,
        shield_successes=2)
    assert out["icon"]["staged_up_level"] == "Serious"
    assert out["meat"]["staged_up_level"] == "Serious"
    assert out["icon"]["attacker_successes"] == out["meat"]["attacker_successes"] == 2


# =============================================================================
# Actor riders -- meat presence and stun flag
# =============================================================================

def test_meat_pool_none_yields_icon_only(scripted):
    """An NPC target whose flesh is not simulated (PC -> enemy decker) passes ``meat_pool=None``:
    the strike resolves the icon only, with no meat resistance test."""
    scripted([5, 5, 5, 1])
    out = eng.black_attack(
        attacker_pool=3, security_code="Red", base_damage_level="Serious",
        power=6, icon_bod=1, meat_pool=None)
    assert out["meat"] is None
    assert isinstance(out["icon"], dict) and "boxes" in out["icon"]


def test_meat_is_stun_flag_passes_through(scripted):
    """The ``meat_is_stun`` rider (Killjoy / non-lethal Black IC -> Stun; Black Hammer / lethal
    Black IC -> Physical) is carried on the result for the caller to route the boxes."""
    scripted([1])
    stun = eng.black_attack(
        attacker_pool=1, security_code="Red", base_damage_level="Serious",
        power=4, icon_bod=1, meat_pool=1, meat_is_stun=True)
    phys = eng.black_attack(
        attacker_pool=1, security_code="Red", base_damage_level="Serious",
        power=4, icon_bod=1, meat_pool=1, meat_is_stun=False)
    assert stun["meat_is_stun"] is True
    assert phys["meat_is_stun"] is False


# =============================================================================
# To-hit TN column -- target status (a Validate-Passcode flip changes this)
# =============================================================================

@pytest.mark.parametrize("status, tn", [("intruding", 3), ("legitimate", 6)])
def test_target_status_selects_combat_tn_column(scripted, status, tn):
    """The to-hit TN is the host ``COMBAT_TN`` entry for the target status column (Red:
    intruding 3 / legitimate 6). Damage SEVERITY follows the caller's base; to-hit follows the
    host as usual."""
    scripted([1])
    out = eng.black_attack(
        attacker_pool=1, security_code="Red", target_status=status,
        base_damage_level="Serious", power=4, icon_bod=1)
    assert out["attack_tn"] == tn
    assert out["attack_tn"] == rules.COMBAT_TN["Red"][status]
