"""Cybercombat icon-damage -- actor parity (Layer 2).

Proves the "same mechanic, same math, whoever fires it" guarantee for cybercombat: all four
attack directions resolve icon damage through the SINGLE engine core
``eng.cybercombat_attack``, and the core is direction-agnostic (the ``attacker_is_ic`` flag is
a cosmetic trace label -- it changes no number). The router-level guard pins the A1 fix: the
PC->IC path (``mr.attack_ic``) and the PC->enemy path (``mr.attack_enemy_decker`` plain Attack)
BOTH pass the decker's own Attack-utility Rating as the attack Power -- NOT the Cybercombat
to-hit TN -- exactly like the two IC-attacker directions pass the IC Rating.

vr2_rules.md (Icon Damage / Damage Resistance): the targeted icon resists with a Bod Resistance
Test against a TN equal to the Power of the attack, and Power = the attacking program's Rating.
Regression guard: before A1, PC->IC alone made the IC resist against the host Cybercombat TN
(3-6) instead of the Attack utility Rating -- the lone asymmetry in the four-way surface.
"""
from __future__ import annotations

import asyncio

import pytest

from app.services import matrix_engine as eng
from app.services import matrix_rules as rules
from app.routers import matrix_runs as mr
from app.schemas.matrix_run import RunAttackInput, RunEnemyAttackInput

# Reuse the sanctioned maximal-run harness (stable test infrastructure).
from tests.test_scenario_fuzz import _fresh_run, _FakeDB, _ADMIN


# -- Deterministic dice helper --------------------------------------------------

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
# Engine parity -- the core is direction-agnostic (attacker_is_ic is cosmetic)
# =============================================================================

@pytest.mark.parametrize("seq", [
    [4, 4, 4, 5, 5, 2, 2, 2, 2, 2, 2],
    [6, 3, 4, 1, 5, 6, 1, 1, 2, 3, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
])
def test_engine_result_is_identical_regardless_of_attacker(scripted, seq):
    """Given identical numeric inputs and identical dice, ``cybercombat_attack`` returns the SAME
    result whether the attacker is IC or a decker -- the flag only labels the trace line. This is
    what lets one core serve IC->PC, decker->PC, PC->IC and PC->enemy."""
    kw = dict(attacker_pool=5, security_code="Red", target_status="intruding",
              target_bod=6, armor_rating=1, ic_rating=6, tn_modifier=0)
    scripted(seq)
    as_ic = eng.cybercombat_attack(**kw, attacker_is_ic=True)
    scripted(seq)
    as_decker = eng.cybercombat_attack(**kw, attacker_is_ic=False)
    assert as_ic == as_decker


# =============================================================================
# Router parity -- both PC attack directions use the Attack Rating as Power
# =============================================================================

_CANNED = {
    "attack_roll": {"successes": 1, "ones": 0, "dice": [4], "tn": 3, "pool": 8},
    "attack_tn": 3,
    "base_damage_level": "Serious",
    "resistance": {
        "effective_power": 5, "attacker_successes": 1, "shield_successes": 0,
        "staged_up_level": "Serious",
        "resist_roll": {"successes": 0, "ones": 0, "dice": [1], "tn": 5, "pool": 1},
        "final_damage_level": "Light", "boxes": 1,
    },
}


def _capture_engine(monkeypatch):
    """Patch the shared engine core to record the kwargs the router hands it, returning a canned
    (non-crashing) result so the endpoint completes and serializes."""
    captured: dict = {}

    def _spy(**kw):
        captured.clear()
        captured.update(kw)
        return _CANNED

    monkeypatch.setattr(eng, "cybercombat_attack", _spy)
    return captured


def _boot(monkeypatch, attack_rating: int):
    """A fresh maximal run (Red host, SV 9) with the decker's Attack utility set to a distinctive
    rating and its Attack options cleared (so a plain Killer sees no Area/Shift perturbation)."""
    import random
    rng = random.Random(20260706)
    monkeypatch.setattr(mr, "random", rng)
    monkeypatch.setattr(eng, "random", rng)
    run = _fresh_run()
    run.decker_json["utilities"]["attack"] = attack_rating
    run.decker_json["program_options"]["attack"] = {}

    async def _get(db, run_id, _r=run):
        return _r
    monkeypatch.setattr(mr, "_get_run_or_404", _get)
    return run


def test_pc_vs_ic_uses_attack_rating_as_power_not_combat_tn(monkeypatch):
    """PC->IC (attack_ic): the IC resists with Security Value dice against a Power equal to the
    Attack utility Rating (5), NOT the host Cybercombat to-hit TN (Red legitimate = 6). This is the
    A1 regression guard."""
    captured = _capture_engine(monkeypatch)
    run = _boot(monkeypatch, attack_rating=5)
    killer = next(ic for ic in run.state_json["active_ic"]
                  if ic["type"] == "Killer" and ic["status"] == "active")

    asyncio.run(mr.attack_ic(
        run_id=1,
        body=RunAttackInput(target_ic_id=killer["id"], attack_pool=8,
                            hacking_pool_dice=0, armor_utility=0),
        auth=_ADMIN, db=_FakeDB()))

    assert captured["attacker_is_ic"] is False
    assert captured["ic_rating"] == 5                                   # Power = Attack Rating
    assert captured["ic_rating"] != rules.COMBAT_TN["Red"]["legitimate"]  # NOT the to-hit TN (6)
    assert captured["security_code"] == "Red"
    assert captured["target_status"] == "legitimate"                    # IC = legitimate host resident
    assert captured["target_bod"] == 9                                  # IC resists with SV dice
    assert captured["armor_rating"] == 0                               # plain Killer, no Armor IC


def test_pc_vs_enemy_uses_attack_rating_as_power(monkeypatch):
    """PC->enemy (attack_enemy_decker plain Attack): the enemy resists with Bod dice against a
    Power equal to the SAME Attack utility Rating (5) -- identical Power source to PC->IC."""
    captured = _capture_engine(monkeypatch)
    run = _boot(monkeypatch, attack_rating=5)
    enemy = next(e for e in run.state_json["enemy_deckers"]
                 if e.get("revealed") and e.get("status") == "active")

    asyncio.run(mr.attack_enemy_decker(
        run_id=1,
        body=RunEnemyAttackInput(enemy_id=enemy["id"], attack_pool=8,
                                 hacking_pool_dice=0, program="attack"),
        auth=_ADMIN, db=_FakeDB()))

    assert captured["attacker_is_ic"] is False
    assert captured["ic_rating"] == 5                # Power = Attack Rating (same as PC->IC)
    assert captured["security_code"] == "Red"
    assert captured["target_status"] == "legitimate"  # enemy security decker = legitimate resident
    assert captured["target_bod"] == enemy["bod"]    # enemy resists with Bod, exactly like the PC
