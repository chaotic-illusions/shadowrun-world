"""Attribute-crippling family -- actor parity (Layer 2).

Proves the "same mechanic, same math, whoever fires it" guarantee: the crippler IC
(``eng.crippler_attack``) and the shared ``eng.attribute_attack_core`` resolve identical
dice to identical net/reduction because the IC wrapper delegates to that core; the live
decker programs (Poison/Restrict/Reveal) route through the SAME core via ``eng.crippler_attack``
in the router seam ``mr._resolve_attribute_attack``, which reduces a PC persona and an enemy
attribute by the same amount for the same roll.
Also asserts the single source-of-truth table covers every persona attribute so no
actor can silently lack an option the others have.

vr2_rules.md: L437 (crippler math) + L1557-1570 ("Poison ... like Acid", etc.) establish
that the decker programs and the matching crippler IC are the same test.
"""
from __future__ import annotations

import pytest

from app.services import matrix_engine as eng
from app.routers import matrix_runs as mr


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
    return {"condition_monitor": {
        "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
        "persona_chip_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
        "crippler_rating": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
    }}


# =============================================================================
# Engine parity -- crippler_attack (IC) == attribute_attack_core (shared core)
# =============================================================================

@pytest.mark.parametrize("seq, exp_net, exp_reduction", [
    ([6, 6, 6, 6, 1, 1, 1, 1], 4, 2),     # attack 4 succ, resist 0 -> net 4 -> 2
    ([6, 6, 6, 1, 1, 1, 1, 1], 3, 1),     # attack 3 succ, resist 0 -> net 3 -> 1 (round down)
    ([6, 6, 5, 1, 6, 1, 1, 1], 2, 1),     # attack 3 succ, resist 1 -> net 2 -> 1
])
def test_crippler_wrapper_matches_shared_core(scripted, seq, exp_net, exp_reduction):
    """Given identical dice and inputs, the IC crippler wrapper (eng.crippler_attack) and the
    shared eng.attribute_attack_core produce the same attack roll, resist roll, net and reduction
    -- the wrapper adds only a ripper rider, so the crippling math lives in one place. The live
    decker programs (Poison/Restrict/Reveal) route through the SAME wrapper in the router seam."""
    # attack: 4 dice vs Orange-intruding TN 4; resist: 4 dice vs rating 6.
    scripted(seq)
    ic = eng.crippler_attack(
        security_value=4, security_code="Orange", target_status="intruding",
        target_attribute_rating=4, ic_rating=6)
    scripted(seq)
    dk = eng.attribute_attack_core(
        attacker_pool=4, resist_tn=6, security_code="Orange", target_status="intruding",
        target_attribute_rating=4)

    assert ic["attack_roll"] == dk["attack_roll"]
    assert ic["defense_roll"] == dk["resist_roll"]      # same roll, wrapper key differs only
    assert ic["net_successes"] == dk["net"] == exp_net
    assert ic["attribute_reduction"] == dk["reduction"] == exp_reduction


# =============================================================================
# Actor parity -- PC-defence and enemy-target reduce identically
# =============================================================================

def test_pc_and_enemy_directions_reduce_identically(scripted):
    """The router seam floors and reduces a PC persona and an enemy attribute the same way for the
    same forced roll (net 4 -> reduction 2 on a starting rating of 6 -> new value 4)."""
    seq = [6, 6, 6, 6, 1, 1, 1, 1, 1, 1]  # attack 4 dice, resist 6 dice (target attr 6)

    scripted(seq)
    pc_state = _pc_state()
    pc = mr._resolve_attribute_attack(
        pc_state, attacker_pool=4, resist_tn=6, target_attr_rating=6, attr="bod",
        sec_code="Orange", target_status="intruding", target_kind="pc", causing_rating=6)

    scripted(seq)
    enemy = {"bod": 6}
    en = mr._resolve_attribute_attack(
        {"condition_monitor": {}}, attacker_pool=4, resist_tn=6, target_attr_rating=6, attr="bod",
        sec_code="Orange", target_status="intruding", target_kind="enemy", enemy=enemy)

    assert pc["reduction"] == en["reduction"] == 2
    assert pc["applied"] == en["applied"] == 2
    assert pc["new_value"] == en["new_value"] == 4
    # Both directions now use the SAME ledger model: the base attribute is never mutated and the
    # damage lives in the target's condition monitor, so a Restore can repair either persona.
    assert enemy["bod"] == 6                                             # base untouched
    assert enemy["condition_monitor"]["persona_damage"]["bod"] == 2      # enemy ledger raised
    assert mr._enemy_effective_attr(enemy, "bod") == 4                   # effective = base - damage
    assert pc_state["condition_monitor"]["persona_damage"]["bod"] == 2   # PC ledger raised


def test_pc_and_enemy_floor_at_one_identically(scripted):
    """Both directions clamp the attribute at 1 for the same overkill roll (net 6 vs rating 2 ->
    only 1 point of reduction is possible)."""
    seq = [6, 6, 6, 6, 6, 6, 1, 1]        # attack 6 dice, resist 2 dice (target attr 2)

    scripted(seq)
    pc = mr._resolve_attribute_attack(
        _pc_state(), attacker_pool=6, resist_tn=6, target_attr_rating=2, attr="evasion",
        sec_code="Orange", target_status="intruding", target_kind="pc", causing_rating=6)

    scripted(seq)
    enemy = {"evasion": 2}
    en = mr._resolve_attribute_attack(
        {"condition_monitor": {}}, attacker_pool=6, resist_tn=6, target_attr_rating=2,
        attr="evasion", sec_code="Orange", target_status="intruding", target_kind="enemy",
        enemy=enemy)

    assert pc["reduction"] == en["reduction"] == 3      # raw net // 2
    assert pc["applied"] == en["applied"] == 1          # floored to a 2 -> 1 drop
    assert pc["new_value"] == en["new_value"] == 1


# =============================================================================
# Table integrity -- every actor has the options the rules give it
# =============================================================================

def test_attribute_attack_table_covers_all_persona_attributes():
    """Single source of truth: every persona attribute has a crippler + ripper IC; only Sensor
    lacks a decker program (Jammer is IC-only). The two lookup maps derive from this table."""
    assert set(mr._ATTRIBUTE_ATTACK) == {"bod", "evasion", "masking", "sensor"}
    for attr, m in mr._ATTRIBUTE_ATTACK.items():
        assert m["ic"] and m["ripper"], f"{attr} missing crippler/ripper IC"
        assert mr._CRIPPLER_TARGET[m["ic"]] == attr
        assert mr._CRIPPLER_TARGET[m["ripper"]] == attr
        if m["program"]:
            assert mr._PROGRAM_ATTR[m["program"]] == attr
    # Exactly the three BEM attributes have a decker program; Sensor is the IC-only asymmetry.
    assert set(mr._PROGRAM_ATTR.values()) == {"bod", "evasion", "masking"}
    assert mr._ATTRIBUTE_ATTACK["sensor"]["program"] is None
