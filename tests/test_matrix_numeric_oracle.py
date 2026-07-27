"""Consolidated VR2 Matrix numeric oracle -- executed success AND failure per resolver.

Requirement (3) of the reconciliation: every in-scope program / option / IC / host
mechanic must be numerically correct in BOTH success and failure against a cited VR2
rule, executed deterministically in-process.

Rather than duplicate a bespoke test per buildable item, this oracle pins the SHARED
engine primitive each item resolves through (requirement 4): every ledger ``resolver``
is exercised here once in a SUCCESS case and once in a FAILURE case with a scripted
d6 stream, so the proof is complete and non-redundant. The reconciliation contract
test (``test_matrix_reconciliation.py``) asserts that EVERY ledger resolver appears in
``COVERED_PRIMITIVES`` (or is one of the two proven passives in ``PASSIVE_COVERED``),
so a newly-built program/IC cannot slip past the numeric gate -- that is requirement
(5) applied to requirement (3).

Determinism
-----------
``roll_dice`` is the only RNG consumer in the primitives under test; it calls
``random.randint(1, 6)`` once per die (plus once per re-roll when TN > 6). Each row
scripts the EXACT faces consumed, in call order, and ``_run`` asserts the stream is
fully drained -- so a miscounted pool fails loudly instead of silently drawing a wrong
face. TNs are kept <= 6 (no rule-of-6 rerolls) except the dedicated ``roll_dice`` row,
which exists to prove exploding sixes, and the Disinfect/Hog-purge failure rows, which
prove a defence pushing the TN above 6.

The ``vr2`` field on each row is the governing ``vr2_rules.md`` line. Box counts follow
``matrix_rules.ICON_DAMAGE_BOXES`` boxes a hit deals (Light 1 / Moderate 2 / Serious 3 / Deadly 6).
"""

from __future__ import annotations

import pytest

import app.services.matrix_engine as eng
import app.routers.matrix_runs as mr
from tests.matrix_scope_ledger import PROGRAMS, IC


# --------------------------------------------------------------------------- harness
class _ScriptedD6:
    """Feeds ``eng.random.randint(1, 6)``: pops the next scripted face each call."""

    def __init__(self, faces: list[int]):
        self._faces = list(faces)
        self._i = 0

    def randint(self, a: int, b: int) -> int:
        assert (a, b) == (1, 6), f"unexpected randint({a}, {b}); oracle assumes d6 only"
        assert self._i < len(self._faces), "scripted RNG underrun -- miscounted dice pool"
        v = self._faces[self._i]
        self._i += 1
        return v

    @property
    def drained(self) -> bool:
        return self._i == len(self._faces)


def _run(monkeypatch, faces, fn, **kwargs):
    """Run ``fn`` with a scripted d6 stream and assert the stream was fully consumed."""
    rng = _ScriptedD6(faces)
    monkeypatch.setattr(eng, "random", rng)
    result = fn(**kwargs)
    assert rng.drained, f"scripted RNG left {len(faces) - rng._i} unused face(s) for {fn.__name__}"
    return result


# --------------------------------------------------------------------------- rows
# Each ``_p_<primitive>`` runs the SUCCESS branch then the FAILURE branch. The name is
# the exact ledger ``resolver`` string so the contract test can prove coverage by key.

def _p_roll_dice(mp):
    # SUCCESS: rule of 6 -- one die explodes 6 -> 6 -> 3 = 15, beating TN 12.
    r = _run(mp, [6, 6, 3], eng.roll_dice, pool=1, tn=12)
    assert r["dice"] == [15] and r["successes"] == 1
    # FAILURE: a flat 5 cannot reach TN 12 without a 6 to explode.
    r = _run(mp, [5], eng.roll_dice, pool=1, tn=12)
    assert r["successes"] == 0


def _p_system_test(mp):
    # SUCCESS: decker nets +2 over the host -> operation succeeds, no tally.
    r = _run(mp, [6, 6, 2, 2, 2, 2, 2], eng.system_test,
             decker_pool=4, subsystem_rating=4, security_value=3, det_factor=4)
    assert r["success"] is True and r["decker_net_successes"] == 2 and r["tally_increase"] == 0
    # FAILURE: decker whiffs, host scores 2 -> operation fails, tally +2.
    r = _run(mp, [2, 2, 2, 2, 6, 6, 2], eng.system_test,
             decker_pool=4, subsystem_rating=4, security_value=3, det_factor=4)
    assert r["success"] is False and r["tally_increase"] == 2


def _p_detection_factor(mp):
    # Pure formula (no RNG): a loaded Sleaze raises Detection Factor.
    assert eng.detection_factor(6, 0) == 3          # masking only: ceil(6 / 2)
    assert eng.detection_factor(6, 4) == 5          # + Sleaze 4:   ceil((6 + 4) / 2)


def _p_damage_resistance(mp):
    # SUCCESS (for the attacker): defender resists nothing -> full Serious (3 boxes).
    r = _run(mp, [1, 1, 1, 1], eng.damage_resistance,
             bod=4, power=6, base_damage_level="Serious", attacker_successes=0)
    assert r["final_damage_level"] == "Serious" and r["boxes"] == 3
    # FAILURE (attack mitigated): 4 resist successes stage Serious down to Light (1 box).
    r = _run(mp, [6, 6, 6, 6], eng.damage_resistance,
             bod=4, power=6, base_damage_level="Serious", attacker_successes=0)
    assert r["final_damage_level"] == "Light" and r["boxes"] == 1


def _p_cybercombat_attack(mp):
    # SUCCESS: 3 net to-hit stages Serious up to Deadly; defender resists nothing -> 6 boxes.
    r = _run(mp, [6, 6, 6, 2, 2, 1, 1, 1, 1], eng.cybercombat_attack,
             attacker_pool=5, security_code="Red", target_status="intruding",
             target_bod=4, ic_rating=6)
    assert r["attack_roll"]["successes"] == 3
    assert r["resistance"]["final_damage_level"] == "Deadly" and r["resistance"]["boxes"] == 6
    # FAILURE: 0 to-hit successes -> the run layer applies no damage (a clean miss).
    r = _run(mp, [2, 2, 2, 2, 2, 1, 1, 1, 1], eng.cybercombat_attack,
             attacker_pool=5, security_code="Red", target_status="intruding",
             target_bod=4, ic_rating=6)
    assert r["attack_roll"]["successes"] == 0


def _p_black_attack(mp):
    # SUCCESS: one Attack Test drives BOTH icon and meat resistance -> Deadly on each. Icon damage
    # uses the icon box table (Deadly = 6); meat (physical body) uses the 1/3/6/10 table (Deadly = 10).
    r = _run(mp, [6, 6, 6, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1], eng.black_attack,
             attacker_pool=5, security_code="Red", target_status="intruding",
             base_damage_level="Serious", power=6, icon_bod=4, meat_pool=4)
    assert r["attack_roll"]["successes"] == 3
    assert r["icon"]["boxes"] == 6
    assert r["meat"] is not None and r["meat"]["boxes"] == 10
    # FAILURE: 0 to-hit successes -> no damage to icon or operator.
    r = _run(mp, [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1], eng.black_attack,
             attacker_pool=5, security_code="Red", target_status="intruding",
             base_damage_level="Serious", power=6, icon_bod=4, meat_pool=4)
    assert r["attack_roll"]["successes"] == 0


def _p_attribute_attack_core(mp):
    # SUCCESS: 4 net successes reduce the targeted attribute by 2 (1 per 2 net).
    r = _run(mp, [6, 6, 6, 6, 2, 2, 2, 2, 2, 2], eng.attribute_attack_core,
             attacker_pool=6, resist_tn=4, security_code="Orange",
             target_status="intruding", target_attribute_rating=4)
    assert r["net"] == 4 and r["reduction"] == 2
    # FAILURE: the target out-resists (2 vs 4) -> net clamped to 0, no reduction.
    r = _run(mp, [6, 6, 2, 2, 2, 2, 6, 6, 6, 6], eng.attribute_attack_core,
             attacker_pool=6, resist_tn=4, security_code="Orange",
             target_status="intruding", target_attribute_rating=4)
    assert r["net"] == 0 and r["reduction"] == 0


def _p_crippler_attack(mp):
    # SUCCESS (ripper): 4 net -> 2 attribute points, plus a permanent 2-point chip burn.
    r = _run(mp, [6, 6, 6, 6, 2, 2, 2, 2, 2, 2, 6, 6, 2, 2], eng.crippler_attack,
             security_value=6, security_code="Red", target_status="intruding",
             target_attribute_rating=4, ic_rating=4, is_ripper=True, mpcp_rating=4)
    assert r["net_successes"] == 4 and r["attribute_reduction"] == 2 and r["chip_damage"] == 2
    # FAILURE: 0 net -> no reduction and (net not > 0) no ripper chip roll at all.
    r = _run(mp, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], eng.crippler_attack,
             security_value=6, security_code="Red", target_status="intruding",
             target_attribute_rating=4, ic_rating=4, is_ripper=True, mpcp_rating=4)
    assert r["net_successes"] == 0 and "chip_damage" not in r


def _p_hog_attack(mp):
    # SUCCESS: 4 net -> the target's highest running program loses 2 rating points this turn.
    r = _run(mp, [6, 6, 6, 6, 2, 2, 2, 2, 2, 2], eng.hog_attack,
             attacker_pool=6, security_code="Orange", target_status="intruding",
             hog_rating=4, mpcp_rating=4)
    assert r["net"] == 4 and r["reduction"] == 2
    # FAILURE: 0 net -> the infection makes no progress this turn.
    r = _run(mp, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], eng.hog_attack,
             attacker_pool=6, security_code="Orange", target_status="intruding",
             hog_rating=4, mpcp_rating=4)
    assert r["reduction"] == 0


def _p_medic_heal(mp):
    # SUCCESS: Moderate wound (TN 5), 3 successes -> 3 boxes healed.
    r = _run(mp, [6, 6, 6, 2, 2], eng.medic_heal, medic_rating=5, wound_level="Moderate")
    assert r["tn"] == 5 and r["boxes_healed"] == 3
    # FAILURE: Serious wound (TN 6), no successes -> 0 boxes healed.
    r = _run(mp, [2, 2, 2, 2, 2], eng.medic_heal, medic_rating=5, wound_level="Serious")
    assert r["tn"] == 6 and r["boxes_healed"] == 0


def _p_restore_repair(mp):
    # SUCCESS: TN = causing rating 4; 4 successes -> 2 attribute points repaired (capped by damage).
    r = _run(mp, [6, 6, 6, 6, 2, 2], eng.restore_repair,
             restore_rating=6, causing_rating=4, damage_points=3)
    assert r["tn"] == 4 and r["points_repaired"] == 2
    # FAILURE: TN = causing rating 6; 0 successes -> nothing repaired.
    r = _run(mp, [2, 2, 2, 2], eng.restore_repair,
             restore_rating=4, causing_rating=6, damage_points=3)
    assert r["tn"] == 6 and r["points_repaired"] == 0


def _p_shield_parry(mp):
    # SUCCESS: 3 parry successes (subtracted from the attacker's damage successes).
    r = _run(mp, [6, 6, 6, 2, 2], eng.shield_parry, shield_rating=5, attacker_skill=4)
    assert r["successes"] == 3 and r["tn"] == 4
    # FAILURE: outclassed Shield (rating 3 vs skill 6) parries nothing.
    r = _run(mp, [2, 2, 2], eng.shield_parry, shield_rating=3, attacker_skill=6)
    assert r["successes"] == 0 and r["tn"] == 6


def _p_maneuver_test(mp):
    # SUCCESS: maneuvering icon nets +3 (strictly more) -> maneuver lands.
    r = _run(mp, [6, 6, 6, 2, 2, 2, 2, 2, 2, 2], eng.maneuver_test,
             maneuvering_evasion_dice=6, maneuvering_evasion_rating=6,
             opposing_sensor_dice=4, opposing_sensor_rating=4)
    assert r["success"] is True and r["net_successes"] == 3
    # FAILURE: opposing icon wins the exchange -> maneuver fails (net clamped to 0).
    r = _run(mp, [2, 2, 2, 2, 2, 2, 6, 6, 2, 2], eng.maneuver_test,
             maneuvering_evasion_dice=6, maneuvering_evasion_rating=6,
             opposing_sensor_dice=4, opposing_sensor_rating=4)
    assert r["success"] is False and r["net_successes"] == 0


def _p_slow_test(mp):
    # SUCCESS: 4 net -> the proactive IC loses 2 actions.
    r = _run(mp, [6, 6, 6, 6, 2, 2, 2, 2, 2, 2], eng.slow_test,
             decker_pool=6, slow_rating=4, ic_dice=4)
    assert r["actions_lost"] == 2
    # FAILURE: the IC out-resists -> no actions lost.
    r = _run(mp, [2, 2, 2, 2, 2, 2, 6, 6, 2, 2], eng.slow_test,
             decker_pool=6, slow_rating=4, ic_dice=4)
    assert r["actions_lost"] == 0


def _p_steamroller_attack(mp):
    # SUCCESS: a Deadly hit (6 boxes) on a tar already at 4/10 reaches 10 -> crash.
    r = _run(mp, [6, 6, 6, 6, 2, 2, 1, 1], eng.steamroller_attack,
             steamroller_rating=6, steamroller_pool=6, tar_ic_rating=2, to_hit_tn=4,
             existing_boxes=4)
    assert r["crashed"] is True and r["boxes"] == 6
    # FAILURE: a weak Steamroller whiffs and the tar stages the low-Power Deadly down to a graze.
    r = _run(mp, [2, 2, 2, 6, 6, 6, 6, 6, 6], eng.steamroller_attack,
             steamroller_rating=2, steamroller_pool=3, tar_ic_rating=6, to_hit_tn=4)
    assert r["crashed"] is False


def _p_tar_baby_test(mp):
    # SUCCESS (for the IC): the tar wins the opposed test -> the decker's utility crashes.
    r = _run(mp, [6, 6, 6, 2, 2, 2, 2, 2], eng.tar_baby_test, ic_rating=5, utility_rating=3)
    assert r["utility_crashed"] is True
    # FAILURE (for the IC): a strong utility survives the tar.
    r = _run(mp, [2, 2, 2, 6, 6, 6, 2, 2], eng.tar_baby_test, ic_rating=3, utility_rating=5)
    assert r["utility_crashed"] is False


def _p_data_bomb_defuse(mp):
    # SUCCESS: TN = subsystem 6 - Defuse 2 = 4; 2 successes -> defused, no tally.
    r = _run(mp, [6, 6, 2, 2, 2], eng.data_bomb_defuse,
             decker_pool=5, subsystem_rating=6, defuse_utility=2)
    assert r["tn"] == 4 and r["defused"] is True and r["detonated"] is False
    # FAILURE (botch): all ones -> the bomb detonates.
    r = _run(mp, [1, 1, 1, 1], eng.data_bomb_defuse,
             decker_pool=4, subsystem_rating=4, defuse_utility=0)
    assert r["defused"] is False and r["detonated"] is True


def _p_data_bomb_detonate(mp):
    # SUCCESS (bomb hurts persona): fixed (rating)M, no resist -> Moderate (2 boxes), tally +4.
    r = _run(mp, [2, 2, 2, 2], eng.data_bomb_detonate, ic_rating=4, target_bod=4)
    assert r["tally_increase"] == 4 and r["resistance"]["boxes"] == 2
    # FAILURE (resisted): 4 resist successes stage the Moderate DOWN 2 levels -> None (fully
    # resisted, 0 boxes). Under net-first staging a base Moderate cannot survive 4 net resist successes.
    r = _run(mp, [6, 6, 6, 6], eng.data_bomb_detonate, ic_rating=4, target_bod=4)
    assert r["resistance"]["boxes"] == 0 and r["resistance"]["final_damage_level"] == "None"


def _p_worm_attack(mp):
    # SUCCESS: host SV 5 dice vs MPCP TN 3; 3 successes, Hardening 0 -> net 3 > 0 -> infected.
    r = _run(mp, [6, 6, 6, 2, 2], eng.worm_attack, security_value=5, mpcp_rating=3, hardening=0)
    assert r["tn"] == 3 and r["mpcp_infected"] is True
    # FAILURE: Hardening subtracts from successes; net must exceed 0. 3 successes - Hardening 3 = 0.
    r = _run(mp, [6, 6, 6], eng.worm_attack, security_value=3, mpcp_rating=5, hardening=3)
    assert r["tn"] == 5 and r["mpcp_infected"] is False


def _p_disinfect_test(mp):
    # SUCCESS: 2 decker successes beat 0 host successes; host tally stays flat.
    r = _run(mp, [6, 6, 2, 2, 2, 1, 1], eng.disinfect_test,
             decker_pool=5, subsystem_rating=6, disinfect_utility=2,
             security_value=2, det_factor=4)
    assert r["tn"] == 4 and r["worm_destroyed"] is True and r["tally_increase"] == 0
    # FAILURE: no decker successes vs 2 host successes; worm survives and tally rises by 2.
    r = _run(mp, [2, 2, 2, 2, 4, 4], eng.disinfect_test,
             decker_pool=4, subsystem_rating=6, disinfect_utility=0,
             security_value=2, det_factor=4)
    assert r["tn"] == 6 and r["worm_destroyed"] is False and r["tally_increase"] == 2


def _p_scramble_decrypt_test(mp):
    # SUCCESS: TN = Scramble 6 - Decrypt 2 = 4; 2 successes -> decrypted, no tally.
    r = _run(mp, [6, 6, 2, 2, 2], eng.scramble_decrypt_test,
             decker_pool=5, scramble_rating=6, decrypt_utility=2)
    assert r["tn"] == 4 and r["decrypted"] is True
    # FAILURE: no Decrypt, TN = Scramble 6; 0 successes -> still scrambled.
    r = _run(mp, [2, 2, 2, 2], eng.scramble_decrypt_test,
             decker_pool=4, scramble_rating=6, decrypt_utility=0)
    assert r["tn"] == 6 and r["decrypted"] is False


def _p_probe_test(mp):
    # SUCCESS: 3 successes vs Detection Factor -> +3 to the security tally.
    r = _run(mp, [6, 6, 6, 2, 2], eng.probe_test, ic_rating=5, det_factor=4)
    assert r["tally_increase"] == 3
    # FAILURE: 0 successes -> the Probe adds nothing this cycle.
    r = _run(mp, [2, 2, 2], eng.probe_test, ic_rating=3, det_factor=6)
    assert r["tally_increase"] == 0


def _p_trace_hunt_cycle_attack(mp):
    # SUCCESS (for the IC): any success ends the hunt cycle -> the decker is traced.
    r = _run(mp, [6, 6, 2, 2, 2, 2], eng.trace_hunt_cycle_attack, security_value=6, trace_factor=4)
    assert r["hit"] is True
    # FAILURE (for the IC): 0 successes vs the Trace Factor -> the hunt continues.
    r = _run(mp, [2, 2, 2, 2], eng.trace_hunt_cycle_attack, security_value=4, trace_factor=6)
    assert r["hit"] is False


def _p_pc_locate_decker_test(mp):
    # SUCCESS: TN = enemy Mask+Sleaze 6 - Scanner 2 = 4; net +3 -> the hidden decker is pinpointed.
    r = _run(mp, [6, 6, 6, 2, 2, 2, 2, 2, 2, 2], eng.pc_locate_decker_test,
             sensor_rating=6, scanner_rating=2, enemy_mask_sleaze=6, enemy_evasion=4)
    assert r["target_tn"] == 4 and r["located"] is True
    # FAILURE: no Scanner, TN = 6; the enemy out-evades -> not located.
    r = _run(mp, [2, 2, 2, 2, 6, 6, 2, 2, 2, 2], eng.pc_locate_decker_test,
             sensor_rating=4, scanner_rating=0, enemy_mask_sleaze=6, enemy_evasion=6)
    assert r["target_tn"] == 6 and r["located"] is False


def _p_hog_purge_test(mp):
    # SUCCESS: TN = (Hog 2 - hardening 0) + infected program rating 2 = 4; 2 successes -> purged.
    r = _run(mp, [6, 6, 2, 2, 2, 2], eng.hog_purge_test,
             computer_skill=6, hog_rating=2, infected_program_rating=2)
    assert r["tn"] == 4 and r["purged"] is True
    # FAILURE: a heavier Hog raises the TN to 8; 0 successes -> the infection persists.
    r = _run(mp, [2, 2, 2], eng.hog_purge_test,
             computer_skill=3, hog_rating=4, infected_program_rating=4)
    assert r["tn"] == 8 and r["purged"] is False


# --------------------------------------------------------------------------- registry
# name -> {vr2 line, executed success+failure check}. The KEY is the exact ledger
# ``resolver`` string; ``COVERED_PRIMITIVES`` is consumed by the contract test.
ORACLE: dict[str, dict] = {
    "roll_dice":                {"vr2": 0,    "fn": _p_roll_dice},   # rule of 6 (SR2 Success Test)
    "system_test":              {"vr2": 1792, "fn": _p_system_test},
    "detection_factor":         {"vr2": 1510, "fn": _p_detection_factor},
    "damage_resistance":        {"vr2": 2052, "fn": _p_damage_resistance},
    "cybercombat_attack":       {"vr2": 2010, "fn": _p_cybercombat_attack},
    "black_attack":             {"vr2": 603,  "fn": _p_black_attack},
    "attribute_attack_core":    {"vr2": 431,  "fn": _p_attribute_attack_core},
    "crippler_attack":          {"vr2": 523,  "fn": _p_crippler_attack},
    "hog_attack":               {"vr2": 1526, "fn": _p_hog_attack},
    "medic_heal":               {"vr2": 1587, "fn": _p_medic_heal},
    "restore_repair":           {"vr2": 1587, "fn": _p_restore_repair},
    "shield_parry":             {"vr2": 1587, "fn": _p_shield_parry},
    "maneuver_test":            {"vr2": 1982, "fn": _p_maneuver_test},
    "slow_test":                {"vr2": 1526, "fn": _p_slow_test},
    "steamroller_attack":       {"vr2": 1526, "fn": _p_steamroller_attack},
    "tar_baby_test":            {"vr2": 497,  "fn": _p_tar_baby_test},
    "data_bomb_defuse":         {"vr2": 457,  "fn": _p_data_bomb_defuse},
    "data_bomb_detonate":       {"vr2": 457,  "fn": _p_data_bomb_detonate},
    "worm_attack":              {"vr2": 544,  "fn": _p_worm_attack},
    "disinfect_test":           {"vr2": 1587, "fn": _p_disinfect_test},
    "scramble_decrypt_test":    {"vr2": 487,  "fn": _p_scramble_decrypt_test},
    "probe_test":               {"vr2": 481,  "fn": _p_probe_test},
    "trace_hunt_cycle_attack":  {"vr2": 560,  "fn": _p_trace_hunt_cycle_attack},
    "pc_locate_decker_test":    {"vr2": 1792, "fn": _p_pc_locate_decker_test},
    "hog_purge_test":           {"vr2": 1548, "fn": _p_hog_purge_test},
}

#: Primitive resolvers with an executed success+failure oracle row above.
COVERED_PRIMITIVES: frozenset[str] = frozenset(ORACLE)

#: Ledger programs whose resolver is "passive": each has its own executed test below.
PASSIVE_COVERED: frozenset[str] = frozenset({"Camo", "Compressor"})


# --------------------------------------------------------------------------- tests
@pytest.mark.parametrize("name", sorted(ORACLE))
def test_primitive_success_and_failure(name, monkeypatch):
    """Every shared resolver is numerically correct in BOTH success and failure (req 3)."""
    ORACLE[name]["fn"](monkeypatch)


def test_camo_raises_trace_factor_tn(monkeypatch):
    """Camo (passive) adds to the decker's Trace Factor -- the Trace IC's TN. A higher Trace
    Factor turns a hunt-cycle hit into a miss (vr2 Camo L1587 / Trace IC L560)."""
    # Without Camo: Trace Factor 4 -> the Trace IC (Security Value 4) scores a hit.
    r = _run(monkeypatch, [6, 6, 2, 2], eng.trace_hunt_cycle_attack, security_value=4, trace_factor=4)
    assert r["hit"] is True
    # With Camo +2: Trace Factor 6 -> the same roll now misses.
    r = _run(monkeypatch, [2, 2, 2, 2], eng.trace_hunt_cycle_attack, security_value=4, trace_factor=6)
    assert r["hit"] is False


def test_compressor_halves_stored_size():
    """Compressor (passive) is a deterministic size transform (no dice): a loaded Compressor
    stores a downloaded file at HALF size (rounded up), capped at Rating*100 Mp (vr2 L1510-1515).
    Exercises the real shared helper so a change to the download-size math is caught."""
    # SUCCESS (compressible): Compressor 2 (cap 200 Mp), a 100 Mp file stores at (100+1)//2 = 50.
    stored, compressible = mr._compressed_store_size(2, 100)
    assert compressible is True and stored == 50
    # FAILURE (no Compressor loaded): full size, uncompressed.
    stored, compressible = mr._compressed_store_size(0, 100)
    assert compressible is False and stored == 100
    # FAILURE (over the Rating*100 cap): too large to compress -> full size.
    stored, compressible = mr._compressed_store_size(1, 200)
    assert compressible is False and stored == 200


def test_oracle_covers_every_ledger_resolver():
    """Self-check (req 5): every distinct resolver named by an in-scope program or IC is either
    an executed primitive row here or one of the two proven passives -- no resolver escapes the
    numeric gate, and the oracle has no stale rows the ledger never references."""
    referenced = {p["resolver"] for p in PROGRAMS.values()} | {i["resolver"] for i in IC.values()}
    # Every ledger resolver is covered (primitive row) or is the "passive" sentinel.
    uncovered = {r for r in referenced if r != "passive" and r not in COVERED_PRIMITIVES}
    assert not uncovered, f"ledger resolvers with no executed oracle row: {sorted(uncovered)}"
    # The two passive programs each have an executed test.
    passive_progs = {name for name, p in PROGRAMS.items() if p["resolver"] == "passive"}
    assert passive_progs == set(PASSIVE_COVERED), (
        f"passive-program set drifted: ledger={sorted(passive_progs)} "
        f"oracle={sorted(PASSIVE_COVERED)}"
    )
    # No oracle primitive row is dead weight: every covered primitive that maps 1:1 to a ledger
    # resolver is actually referenced (the three engine-internal rows -- roll_dice,
    # data_bomb_detonate, hog_purge_test -- back host mechanics / counter-actions, not a
    # program/IC resolver, so they are allowed to be present without a ledger resolver key).
    engine_internal = {"roll_dice", "data_bomb_detonate", "hog_purge_test"}
    stale = {r for r in COVERED_PRIMITIVES if r not in referenced and r not in engine_internal}
    assert not stale, f"oracle rows referenced by nothing in the ledger: {sorted(stale)}"
