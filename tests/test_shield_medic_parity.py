"""Shield / Medic -- actor parity (Layer 2).

Proves the "same mechanic, same math, whoever runs it" guarantee for the two defensive utilities
that BOTH a PC decker and an enemy (security) decker carry. Each now resolves through ONE shared,
actor-agnostic core -- ``mr._shield_parry_core`` / ``mr._medic_heal_core`` -- that takes no "who is
acting" flag, so the PC and enemy wrappers cannot drift onto different dice / wear / heal math. The
ONLY differences are display + PC-only riders:

  * event -- the PC wrapper emits a player-visible ``shield_parry`` / ``medic_heal``; the enemy
    wrapper emits a GM-only ``enemy_shield_parry`` / ``enemy_decker``(medic) event (the player never
    sees the defender's exact program).
  * wear slot -- the PC's Shield/Medic wear lives in the run ``state['program_damage']``; the
    enemy's on its OWN dict (each security decker tracks its own program damage).
  * One-Shot / DINAB -- PC-only features layered in the PC wrapper (enemy decks model neither).

vr2_rules.md: Shield "loses 1 Rating Point every time it is used" (parry the effective rating vs the
attacker's skill); Medic "loses 1 Rating Point each time it is used" (heal, TN by the icon's current
wound level). Layer 1 (``TestShieldDefense`` / ``TestMedicHeal`` in test_matrix_engine.py) pins the
primitive numbers; this file pins that both actors feed the shared core identical inputs and apply
the result identically -- so no actor can silently drift onto a different resolution.
"""
from __future__ import annotations

import pytest

from app.services import matrix_engine as eng
from app.routers import matrix_runs as mr


# -- Deterministic dice helper (mirrors the oracle's _ScriptedRandom) -----------

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
# SHIELD
# =============================================================================

class TestShieldCoreActorAgnostic:
    """Layer 2a -- the shared ``_shield_parry_core`` resolves identically for a PC-shaped and an
    enemy-shaped wear_owner given the SAME (rating, attacker_skill), and wears each owner's own slot
    by exactly 1 (never the other actor's). The core has no actor parameter, so it cannot branch."""

    def test_core_result_depends_only_on_rating_and_skill(self, scripted):
        # 3 dice per call; the 3-value script cycles so both calls see the identical roll.
        scripted([6, 5, 1])                         # TN 5 (no explosion): 6,5 hit -> 2 successes
        pc_owner: dict = {}
        enemy_owner: dict = {}
        res_pc, succ_pc, rem_pc = mr._shield_parry_core(pc_owner, rating=3, attacker_skill=5)
        res_en, succ_en, rem_en = mr._shield_parry_core(enemy_owner, rating=3, attacker_skill=5)
        assert (succ_pc, rem_pc) == (succ_en, rem_en) == (2, 2)
        assert res_pc["roll"]["dice"] == res_en["roll"]["dice"] == [6, 5, 1]
        assert res_pc["tn"] == res_en["tn"] == 5
        # each owner wears ONLY its own Shield slot, by exactly 1 Rating Point
        assert pc_owner["program_damage"]["shield"] == 1
        assert enemy_owner["program_damage"]["shield"] == 1


class TestShieldWrapperParity:
    """Layer 2b -- the PC (``_shield_parry``) and enemy (``_enemy_shield_parry``) wrappers both feed
    ``eng.shield_parry`` the SAME (shield_rating, attacker_skill) for identical loadouts, return the
    same successes, and wear their OWN slot -- differing only in event visibility."""

    def test_both_wrappers_feed_primitive_identical_args(self, monkeypatch):
        calls: list[tuple[int, int]] = []

        def _spy(*, shield_rating, attacker_skill):
            calls.append((shield_rating, attacker_skill))
            tn = max(2, attacker_skill)
            return {"roll": {"dice": [6, 6], "successes": 2, "tn": tn},
                    "successes": 2, "shield_rating": shield_rating, "tn": tn}

        monkeypatch.setattr(eng, "shield_parry", _spy)

        # PC decker parries an IC hit (host Security Value 6).
        state: dict = {"event_log": []}
        decker = {"utilities": {"shield": 4}}
        pc_succ = mr._shield_parry(state, decker, attacker_skill=6, context="Killer")

        # Enemy security decker parries the PC's Strike Back with the SAME loadout + attacker skill.
        en_state: dict = {"event_log": []}
        enemy = {"id": "e1", "name": "Icebreaker", "utilities": {"shield": 4}}
        en_succ = mr._enemy_shield_parry(en_state, enemy, attacker_skill=6, context="strike back")

        # Same rating + skill fed to the one primitive; same successes back.
        assert calls == [(4, 6), (4, 6)]
        assert pc_succ == en_succ == 2
        # Wear lands on each actor's OWN slot, by exactly 1.
        assert state["program_damage"]["shield"] == 1
        assert enemy["program_damage"]["shield"] == 1
        assert "program_damage" not in en_state          # enemy wear is NOT on the run state
        # Display differs: PC player-visible, enemy GM-only.
        pc_ev = state["event_log"][-1]
        en_ev = en_state["event_log"][-1]
        assert pc_ev["type"] == "shield_parry" and not pc_ev.get("gm_only")
        assert en_ev["type"] == "enemy_shield_parry" and en_ev["gm_only"] is True


# =============================================================================
# MEDIC
# =============================================================================

class TestMedicCoreActorAgnostic:
    """Layer 2a -- the shared ``_medic_heal_core`` heals identically for a PC-shaped and an
    enemy-shaped condition monitor given the SAME rating + current damage, and wears each owner's
    own Medic slot by exactly 1. No actor parameter -> no actor branch."""

    def test_core_result_depends_only_on_cm_and_rating(self, scripted):
        # Serious wound (6 boxes) -> TN 6 (no explosion); 3 dice per call, script cycles.
        scripted([6, 6, 1])                         # two 6s hit -> heal 2 boxes
        cm_pc = {"persona_boxes": 6}
        cm_en = {"persona_boxes": 6}
        pc_owner: dict = {}
        en_owner: dict = {}
        res_pc, wound_pc, healed_pc = mr._medic_heal_core(cm_pc, pc_owner, rating=3)
        res_en, wound_en, healed_en = mr._medic_heal_core(cm_en, en_owner, rating=3)
        assert (wound_pc, healed_pc) == (wound_en, healed_en) == ("Serious", 2)
        assert res_pc["tn"] == res_en["tn"] == 6
        assert cm_pc["persona_boxes"] == cm_en["persona_boxes"] == 4   # 6 - 2 healed
        assert pc_owner["program_damage"]["medic"] == 1
        assert en_owner["program_damage"]["medic"] == 1


class TestMedicWrapperParity:
    """Layer 2b -- the PC (``_apply_medic``) and enemy (``_enemy_medic_heal``) wrappers both feed
    ``eng.medic_heal`` the SAME (medic_rating, wound_level) for identical damage + loadout, heal the
    same boxes, and wear their OWN slot -- differing only in event visibility."""

    def test_both_wrappers_feed_primitive_identical_args(self, monkeypatch):
        calls: list[tuple[int, str]] = []

        def _spy(*, medic_rating, wound_level):
            calls.append((medic_rating, wound_level))
            return {"roll": {"dice": [6, 6, 1], "successes": 2, "tn": 6}, "tn": 6,
                    "wound_level": wound_level, "medic_rating": medic_rating, "boxes_healed": 2}

        monkeypatch.setattr(eng, "medic_heal", _spy)

        # PC decker self-heals a Serious icon wound (6 boxes).
        state: dict = {"event_log": [], "condition_monitor": {"persona_boxes": 6}}
        decker = {"utilities": {"medic": 5}}
        mr._apply_medic(state, decker)

        # Enemy security decker self-heals the SAME wound with the SAME Medic rating.
        en_state: dict = {"event_log": []}
        enemy = {"id": "e1", "name": "Icebreaker", "utilities": {"medic": 5},
                 "condition_monitor": {"persona_boxes": 6}}
        mr._enemy_medic_heal(en_state, enemy)

        # Same rating + wound-level TN column fed to the one primitive.
        assert calls == [(5, "Serious"), (5, "Serious")]
        # Same boxes healed, applied to each actor's OWN condition monitor.
        assert state["condition_monitor"]["persona_boxes"] == 4
        assert enemy["condition_monitor"]["persona_boxes"] == 4
        # Wear on each actor's OWN slot, by exactly 1.
        assert state["program_damage"]["medic"] == 1
        assert enemy["program_damage"]["medic"] == 1
        assert "program_damage" not in en_state          # enemy wear is NOT on the run state
        # Display differs: PC player-visible medic_heal, enemy player-visible enemy_decker(medic).
        pc_ev = state["event_log"][-1]
        en_ev = en_state["event_log"][-1]
        assert pc_ev["type"] == "medic_heal" and not pc_ev.get("gm_only")
        assert en_ev["type"] == "enemy_decker" and en_ev["outcome"] == "medic"
        assert not en_ev.get("gm_only")
        assert "repairs damage to their icon" in en_ev["description"]
