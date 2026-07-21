"""Attribute-crippling family -- rules oracle (Layer 1).

Pins the EXACT vr2 numbers for the unified attribute-attack mechanic that both the
decker programs (Poison / Restrict / Reveal) and the crippler / ripper IC
(Acid / Binder / Marker / Jammer + *-rip) resolve through -- one engine core
(``eng.attribute_attack_core``) and one router application seam
(``mr._resolve_attribute_attack``). Dice are forced via a scripted RNG so each
assertion is a rules citation, not a probability.

vr2_rules.md citations:
  - L435  Cripplers: Acid (Bod), Binder (Evasion), Jammer (Sensor), Marker (Masking).
  - L437  "reduce the targeted attribute by the difference divided by 2 and rounded
          down ... Icon attributes cannot be reduced below 1." Reduction only when the
          attacker's successes EXCEED the defender's.
  - L525  Rippers: "Reduce the targeted persona chip's Rating by 1 for each success"
          (permanent -- only replacing the persona chip restores it).
  - L1557-1570  Poison attacks Bod "like Acid", Restrict attacks Evasion "like Binder",
          Reveal attacks Masking "like Marker"; "reduced by 1 for every 2 net successes."
          (No decker program targets Sensor -- Jammer is IC-only, a rules-correct asymmetry.)
"""
from __future__ import annotations

import pytest

from app.services import matrix_engine as eng
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


def _pc_state() -> dict:
    """Minimal run state for a PC-defence attribute attack (persona ledgers zeroed)."""
    return {"condition_monitor": {
        "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
        "persona_chip_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
        "crippler_rating": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
    }}


# =============================================================================
# Attribute -> program / IC mapping (rules oracle, no dice)
# =============================================================================

def test_program_and_ic_maps_match_vr2_attribute_targets():
    """The decker programs and the crippler IC target the SAME attributes (vr2 L435 + L1557-1570),
    and the maps are DERIVED from one table so they cannot drift."""
    assert mr._PROGRAM_ATTR == {"poison": "bod", "restrict": "evasion", "reveal": "masking"}
    assert mr._CRIPPLER_TARGET == {
        "Acid": "bod", "Binder": "evasion", "Marker": "masking", "Jammer": "sensor",
        "Acid-rip": "bod", "Bind-rip": "evasion", "Mark-rip": "masking", "Jam-rip": "sensor",
    }
    # Jammer / Sensor is IC-ONLY: no decker program in the crippler set targets Sensor.
    assert "sensor" not in mr._PROGRAM_ATTR.values()
    assert mr._ATTRIBUTE_ATTACK["sensor"]["program"] is None


# =============================================================================
# Failure branch (engine) -- resisted attack does nothing
# =============================================================================

def test_attack_resisted_yields_zero_reduction(scripted):
    """vr2 L437: an attribute is reduced only when the attacker's successes EXCEED the
    defender's. Here attack 1 < resist 2, so net = 0 and reduction = 0."""
    # attack: 3 dice vs Orange-intruding TN 4 -> [6,1,1] = 1 success
    # resist: 3 dice vs ic_rating 4          -> [6,6,1] = 2 successes
    scripted([6, 1, 1, 6, 6, 1])
    out = eng.crippler_attack(
        security_value=3, security_code="Orange", target_status="intruding",
        target_attribute_rating=3, ic_rating=4)
    assert out["attack_roll"]["successes"] == 1
    assert out["defense_roll"]["successes"] == 2
    assert out["net_successes"] == 0
    assert out["attribute_reduction"] == 0


def test_resolver_pc_resisted_leaves_ledger_untouched(scripted):
    """A fully-resisted attack through the resolver applies nothing and records no causing rating."""
    scripted([6, 1, 1, 6, 6, 1])
    state = _pc_state()
    res = mr._resolve_attribute_attack(
        state, attacker_pool=3, resist_tn=4, target_attr_rating=3, attr="bod",
        sec_code="Orange", target_status="intruding", target_kind="pc", causing_rating=5)
    assert res["reduction"] == 0 and res["applied"] == 0 and res["new_value"] == 3
    cm = state["condition_monitor"]
    assert cm["persona_damage"]["bod"] == 0
    assert cm["crippler_rating"]["bod"] == 0


# =============================================================================
# Success branch -- reduction = net // 2, applied to the target
# =============================================================================

def test_resolver_pc_applies_reduction_and_records_causing_rating(scripted):
    """vr2 L437 + L1557 (Poison ~ Acid ~ Bod): net 4 -> reduce Bod by 2; the causing program
    rating is stored as the Restore Test TN."""
    # attack: 4 dice vs Orange TN 4 -> [6,6,6,6] = 4 succ; resist: 6 dice all 1 -> 0 succ.
    scripted([6, 6, 6, 6, 1, 1, 1, 1, 1, 1])
    state = _pc_state()
    res = mr._resolve_attribute_attack(
        state, attacker_pool=4, resist_tn=6, target_attr_rating=6, attr="bod",
        sec_code="Orange", target_status="intruding", target_kind="pc", causing_rating=5)
    assert res["reduction"] == 2 and res["applied"] == 2 and res["new_value"] == 4
    cm = state["condition_monitor"]
    assert cm["persona_damage"]["bod"] == 2
    assert cm["crippler_rating"]["bod"] == 5


def test_resolver_enemy_reveal_floors_masking_and_recomputes_df(scripted):
    """vr2 L1567 (Reveal ~ Marker ~ Masking) + L437 (never below 1): a big net against Masking 2
    can only take it to 1, and the enemy Detection Factor is recomputed off the new Masking."""
    # attack: 6 dice vs Orange TN 4 -> all 6 = 6 succ; resist: 2 dice all 1 -> 0 succ.
    scripted([6, 6, 6, 6, 6, 6, 1, 1])
    enemy = {"masking": 2, "utilities": {"sleaze": 4}, "detection_factor": 99}
    state = {"condition_monitor": {}}
    res = mr._resolve_attribute_attack(
        state, attacker_pool=6, resist_tn=6, target_attr_rating=2, attr="masking",
        sec_code="Orange", target_status="intruding", target_kind="enemy", enemy=enemy)
    assert res["reduction"] == 3 and res["applied"] == 1 and res["new_value"] == 1
    # Ledger model: the enemy base Masking is untouched; the damage lives in its condition monitor
    # and the stored Detection Factor is recomputed off the new EFFECTIVE Masking (2 - 1 = 1).
    assert enemy["masking"] == 2                                          # base untouched
    assert enemy["condition_monitor"]["persona_damage"]["masking"] == 1
    assert mr._enemy_effective_attr(enemy, "masking") == 1                # effective floored at 1
    assert enemy["detection_factor"] == eng.detection_factor(1, 4)


# =============================================================================
# Edge: multi-hit accumulation (the bug the unification fixed)
# =============================================================================

def test_resolver_pc_multi_hit_accumulates_and_floors(scripted):
    """Two successive crippler hits on the SAME attribute must ACCUMULATE (not reset). The old
    per-site cap keyed off the CURRENT effective attribute, so a second hit could LOWER the
    stored damage; the unified resolver caps the INCREMENT (applied = min(net//2, eff - 1))."""
    state = _pc_state()
    pd = state["condition_monitor"]["persona_damage"]

    # Hit 1: Bod eff 6, net 4 -> reduction 2 -> pd 2, eff 4.
    scripted([6, 6, 6, 6, 1, 1, 1, 1, 1, 1])
    r1 = mr._resolve_attribute_attack(
        state, attacker_pool=4, resist_tn=6, target_attr_rating=6, attr="bod",
        sec_code="Orange", target_status="intruding", target_kind="pc", causing_rating=6)
    assert r1["applied"] == 2 and pd["bod"] == 2

    # Hit 2: Bod eff now 4, net 4 -> reduction 2 -> pd 4, eff 2 (accumulated, NOT reset).
    scripted([6, 6, 6, 6, 1, 1, 1, 1])
    r2 = mr._resolve_attribute_attack(
        state, attacker_pool=4, resist_tn=6, target_attr_rating=4, attr="bod",
        sec_code="Orange", target_status="intruding", target_kind="pc", causing_rating=6)
    assert r2["applied"] == 2 and r2["new_value"] == 2 and pd["bod"] == 4

    # Hit 3: Bod eff now 2, net 4 -> reduction 2 but only 1 point of room -> floor at 1.
    scripted([6, 6, 6, 6, 1, 1])
    r3 = mr._resolve_attribute_attack(
        state, attacker_pool=4, resist_tn=6, target_attr_rating=2, attr="bod",
        sec_code="Orange", target_status="intruding", target_kind="pc", causing_rating=6)
    assert r3["applied"] == 1 and r3["new_value"] == 1 and pd["bod"] == 5


# =============================================================================
# Ripper rider (PC direction) -- permanent chip damage
# =============================================================================

def test_resolver_pc_ripper_applies_permanent_chip(scripted):
    """vr2 L525: a ripper also runs a Ripper Test (IC rating dice vs MPCP+Hardening) and reduces
    the persona chip by 1 per success, PERMANENTLY (recorded in persona_chip_damage)."""
    # attack: 2 dice vs Orange TN 4 -> [6,6] 2 succ; resist: 6 dice all 1 -> 0 succ -> net 2,
    #   reduction 1. Ripper Test: ic_rating 3 dice vs MPCP 6 -> [6,6,1] -> 2 succ -> chip 2.
    scripted([6, 6, 1, 1, 1, 1, 1, 1, 6, 6, 1])
    state = _pc_state()
    res = mr._resolve_attribute_attack(
        state, attacker_pool=2, resist_tn=3, target_attr_rating=6, attr="bod",
        sec_code="Orange", target_status="intruding", target_kind="pc", causing_rating=3,
        is_ripper=True, mpcp_rating=6)
    assert res["applied"] == 1 and res["chip_applied"] == 2 and res["new_value"] == 3
    cm = state["condition_monitor"]
    assert cm["persona_damage"]["bod"] == 3          # 1 crippler + 2 chip (same slot)
    assert cm["persona_chip_damage"]["bod"] == 2     # permanent portion Restore won't repair
