"""Restore -- actor parity (Layer 2).

Proves the "same mechanic, same math, whoever runs it" guarantee for Restore, the defensive utility
that repairs TEMPORARY crippler damage to a persona's attributes (Bod/Evasion/Masking/Sensor). Both
a PC decker and an enemy (security) decker now resolve it through ONE shared, actor-agnostic core --
``mr._restore_repair_core`` -- that takes no "who is acting" flag, so the PC and enemy wrappers
cannot drift onto different dice / repair / TN math.

This is the capstone of the enemy attribute-damage re-architecture: an enemy's cripple damage now
lives in the SAME condition-monitor ledger the PC uses (``persona_damage`` + ``crippler_rating`` +
``persona_chip_damage``; the base attribute in ``enemy[attr]`` is never mutated, and effective =
base - damage via ``mr._enemy_effective_attr``). Because both actors share that ledger, the ONE
Restore core repairs either persona identically. The ONLY differences are display + PC-only riders:

  * event -- the PC wrapper emits a player-visible ``restore_repair``; the enemy wrapper emits a
    GM-only ``enemy_decker``(restore) event (the player never sees the defender's exact program).
  * riders -- DINAB ``pool_override``, One-Shot spend, and the undamaged/offline info events are
    PC-only (enemy loadouts model none of them).

vr2_rules.md: Restore repairs the temporary attribute reductions from crippler programs; Restore
Test TN = the causing crippler's rating, every 2 successes repairs 1 point, and (unlike Shield /
Medic) Restore does NOT lose a Rating Point per use. Layer 1 (``TestRestoreRepair`` in
test_matrix_engine.py) pins the primitive numbers; this file pins that both actors feed the shared
core identical inputs and apply the result identically -- so no actor can silently drift onto a
different resolution.
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


def _ledger(bod_damage: int, causing: int) -> dict:
    """A condition monitor with ``bod_damage`` temporary Bod cripple points caused by a crippler of
    rating ``causing`` (no permanent Persona-chip damage). Shape is identical for a PC and an
    enemy -- the whole point is that the Restore core cannot tell them apart."""
    return {
        "persona_damage": {"bod": bod_damage, "evasion": 0, "masking": 0, "sensor": 0},
        "crippler_rating": {"bod": causing, "evasion": 0, "masking": 0, "sensor": 0},
    }


# =============================================================================
# RESTORE
# =============================================================================

class TestRestoreCoreActorAgnostic:
    """Layer 2a -- the shared ``_restore_repair_core`` repairs identically for a PC-shaped and an
    enemy-shaped condition monitor given the SAME ledger + Restore rating. The core takes no actor
    parameter (and no wear owner -- Restore does not self-degrade), so it cannot branch on who acts."""

    def test_core_result_depends_only_on_cm_and_rating(self, scripted):
        # 5 Restore dice at TN 6 (the causing crippler rating); the 5-value script cycles so both
        # calls see the identical roll -> 4 successes -> 2 points repaired (successes // 2).
        scripted([6, 6, 6, 6, 1])
        cm_pc = _ledger(bod_damage=4, causing=6)
        cm_en = _ledger(bod_damage=4, causing=6)
        res_pc, attr_pc, pts_pc, floor_pc = mr._restore_repair_core(cm_pc, rating=5)
        res_en, attr_en, pts_en, floor_en = mr._restore_repair_core(cm_en, rating=5)
        assert (attr_pc, pts_pc, floor_pc) == (attr_en, pts_en, floor_en) == ("bod", 2, 0)
        assert res_pc["tn"] == res_en["tn"] == 6                      # TN = causing crippler rating
        assert res_pc["roll"]["dice"] == res_en["roll"]["dice"] == [6, 6, 6, 6, 1]
        assert res_pc["successes"] == res_en["successes"] == 4
        # Same repair applied to each OWN ledger: Bod temp damage 4 -> 2 (never below the 0 chip floor).
        assert cm_pc["persona_damage"]["bod"] == cm_en["persona_damage"]["bod"] == 2
        # Temp damage remains -> the causing rating is kept (needed if Restore runs again next pass).
        assert cm_pc["crippler_rating"]["bod"] == cm_en["crippler_rating"]["bod"] == 6

    def test_core_clears_causing_rating_when_temp_damage_fully_repaired(self, scripted):
        # 2 temp points, 4 successes -> repairs both; once temp damage is gone the causing rating is
        # cleared (moot) -- and identically for either actor.
        scripted([6, 6, 6, 6, 1])
        cm_pc = _ledger(bod_damage=2, causing=6)
        cm_en = _ledger(bod_damage=2, causing=6)
        _, _, pts_pc, _ = mr._restore_repair_core(cm_pc, rating=5)
        _, _, pts_en, _ = mr._restore_repair_core(cm_en, rating=5)
        assert pts_pc == pts_en == 2
        assert cm_pc["persona_damage"]["bod"] == cm_en["persona_damage"]["bod"] == 0
        assert cm_pc["crippler_rating"]["bod"] == cm_en["crippler_rating"]["bod"] == 0


class TestRestoreWrapperParity:
    """Layer 2b -- the PC (``_apply_restore``) and enemy (``_enemy_restore_repair``) wrappers both
    feed ``eng.restore_repair`` the SAME (restore_rating, causing_rating, damage_points) for an
    identical ledger + loadout, repair the same points into each actor's OWN ledger, and accrue NO
    wear -- differing only in event visibility."""

    def test_both_wrappers_feed_primitive_identical_args(self, monkeypatch):
        calls: list[tuple[int, int, int]] = []

        def _spy(*, restore_rating, causing_rating, damage_points):
            calls.append((restore_rating, causing_rating, damage_points))
            tn = max(2, causing_rating)
            return {"roll": {"dice": [6, 6, 6, 6], "successes": 4, "tn": tn}, "tn": tn,
                    "restore_rating": restore_rating, "causing_rating": causing_rating,
                    "successes": 4, "points_repaired": 2}

        monkeypatch.setattr(eng, "restore_repair", _spy)

        # PC decker Restores its own crippled Bod (4 temp damage from a rating-6 crippler).
        state: dict = {"event_log": [], "condition_monitor": _ledger(bod_damage=4, causing=6)}
        decker = {"bod": 6, "utilities": {"restore": 5}}
        mr._apply_restore(state, decker)

        # Enemy security decker Restores the SAME damage with the SAME Restore rating.
        en_state: dict = {"event_log": []}
        enemy = {"id": "e1", "name": "Icebreaker", "bod": 6, "utilities": {"restore": 5},
                 "condition_monitor": _ledger(bod_damage=4, causing=6)}
        mr._enemy_restore_repair(en_state, enemy)

        # Same (restore_rating, causing_rating, damage_points) fed to the one primitive.
        assert calls == [(5, 6, 4), (5, 6, 4)]
        # Same points repaired, applied to each actor's OWN ledger (Bod temp damage 4 -> 2).
        assert state["condition_monitor"]["persona_damage"]["bod"] == 2
        assert enemy["condition_monitor"]["persona_damage"]["bod"] == 2
        # Restore does NOT self-degrade: neither actor accrues program_damage['restore'].
        assert "program_damage" not in state
        assert (enemy.get("program_damage") or {}).get("restore", 0) == 0
        # Display differs: PC player-visible restore_repair, enemy player-visible enemy_decker(restore).
        pc_ev = state["event_log"][-1]
        en_ev = en_state["event_log"][-1]
        assert pc_ev["type"] == "restore_repair" and not pc_ev.get("gm_only")
        assert pc_ev["attribute"] == "bod" and pc_ev["repaired"] == 2
        assert en_ev["type"] == "enemy_decker" and en_ev["outcome"] == "restore"
        assert not en_ev.get("gm_only")
        assert "repairs damage to their BOD" in en_ev["description"]
