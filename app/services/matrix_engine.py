"""
Shadowrun 2nd Edition Matrix rules engine.
Dice rolling, cybercombat resolution, security sheaf generation.
"""

from __future__ import annotations

import math
import random
from typing import Any

from app.services.matrix_rules import (
    DAMAGE_LEVELS, DAMAGE_BOXES, IC_DAMAGE_LEVEL,
    DUMP_SHOCK_LEVEL, COMBAT_TN, SIMSENSE_OVERLOAD_TN,
    IC_INITIATIVE_DICE, SHEAF_INTERVALS,
    IC_RATINGS_TABLE,
    SHEAF_ALERT_TABLE, SHEAF_REACTIVE_WHITE_TABLE, SHEAF_PROACTIVE_WHITE_TABLE,
    SHEAF_REACTIVE_GRAY_TABLE, SHEAF_PROACTIVE_GRAY_TABLE, SHEAF_BLACK_TABLE,
    SHEAF_TRAP_IC_TABLE, SHEAF_CRIPPLER_RIPPER_TARGET_TABLE,
    IC_CATALOG,
)


# -- Dice engine ----------------------------------------------------------------

def roll_dice(pool: int, tn: int = 4) -> dict[str, Any]:
    """Roll a SR2 dice pool against a target number.

    When TN > 6, any die showing 6 is re-rolled and the result added (open-ended
    sixes): e.g. vs TN 8, a 6 becomes 6+reroll; if the reroll is also a 6 the
    process repeats.  Ones are counted from the initial rolls before any rerolls.
    """
    pool = max(1, pool)
    raw = [random.randint(1, 6) for _ in range(pool)]
    ones = sum(1 for d in raw if d == 1)

    if tn <= 6:
        dice = raw
    else:
        dice = []
        for r in raw:
            total = r
            while total % 6 == 0:  # last sub-roll was a 6 -- keep adding
                total += random.randint(1, 6)
            dice.append(total)

    successes = sum(1 for d in dice if d >= tn)
    return {"pool": pool, "tn": tn, "dice": dice, "successes": successes, "ones": ones}


def hacking_pool(intelligence: int, mpcp: int) -> int:
    """Hacking Pool = (Intelligence + MPCP) // 3."""
    return (intelligence + mpcp) // 3


def detection_factor(masking: int, sleaze_rating: int = 0) -> int:
    """Detection Factor = ceil((masking + sleaze) / 2) if sleaze > 0, else ceil(masking / 2)."""
    if sleaze_rating > 0:
        return math.ceil((masking + sleaze_rating) / 2)
    return math.ceil(masking / 2)


# -- System test (decker action + host security response) ----------------------

def system_test(
    *,
    decker_pool: int,
    subsystem_rating: int,
    security_value: int,
    det_factor: int,
    extra_tn_modifier: int = 0,
) -> dict[str, Any]:
    """
    Run one System Test:
    - Decker rolls decker_pool vs. subsystem_rating (+ modifier)
    - Host rolls security_value vs. det_factor
    Returns both rolls and the security tally increase (host successes).
    """
    decker_tn = max(2, subsystem_rating + extra_tn_modifier)
    decker_roll = roll_dice(decker_pool, decker_tn)
    host_roll = roll_dice(security_value, det_factor)

    decker_net = decker_roll["successes"] - host_roll["successes"]
    success = decker_net > 0

    return {
        "success": success,
        "decker_roll": decker_roll,
        "host_roll": host_roll,
        "decker_net_successes": decker_net,
        "tally_increase": host_roll["successes"],
    }


# -- Damage handling -----------------------------------------------------------

def stage_damage(base_level: str, net_successes: int, direction: int = 1) -> str:
    """
    Stage damage up (direction=1) or down (direction=-1) by net_successes // 2.
    Clamped to valid damage levels.
    """
    steps = net_successes // 2
    idx = DAMAGE_LEVELS.index(base_level)
    idx = max(0, min(len(DAMAGE_LEVELS) - 1, idx + direction * steps))
    return DAMAGE_LEVELS[idx]


def damage_resistance(
    *,
    bod: int,
    power: int,
    armor_rating: int = 0,
    base_damage_level: str,
    attacker_successes: int = 0,
) -> dict[str, Any]:
    """
    Resolve a damage resistance roll.
    - Effective power = power - armor_rating (min 1)
    - Resistance roll: bod dice vs. effective_power
    - Stage down 1 level per 2 resistance successes
    Returns effective power, resistance roll, and final damage level.
    """
    effective_power = max(1, power - armor_rating)
    # First stage up from attacker successes
    staged_up = stage_damage(base_damage_level, attacker_successes, 1)
    # Defender resists
    resist_roll = roll_dice(bod, effective_power)
    final = stage_damage(staged_up, resist_roll["successes"], -1)
    return {
        "effective_power": effective_power,
        "staged_up_level": staged_up,
        "resist_roll": resist_roll,
        "final_damage_level": final,
        "boxes": DAMAGE_BOXES[final],
    }


# -- Cybercombat ---------------------------------------------------------------

def cybercombat_attack(
    *,
    attacker_pool: int,
    security_code: str,
    target_status: str = "intruding",
    target_bod: int,
    armor_rating: int = 0,
    ic_rating: int,
    attacker_is_ic: bool = True,
    tn_modifier: int = 0,
) -> dict[str, Any]:
    """
    Resolve a single cybercombat attack exchange.
    - attacker_pool: attacker's dice pool (Security Value for IC; attack utility + hacking pool for decker)
    - security_code: host security code string
    - target_status: "intruding" or "legitimate"
    - target_bod: defender Bod rating (for resistance)
    - armor_rating: Armor utility rating (reduces Power)
    - ic_rating: IC's rating (determines Power and base damage level)
    - attacker_is_ic: if True, IC attacks decker; if False, decker attacks IC
    - tn_modifier: additional TN adjustment (e.g. Party IC cluster penalty)
    """
    tn = max(2, COMBAT_TN[security_code][target_status] + tn_modifier)
    base_damage = IC_DAMAGE_LEVEL[security_code]

    attack_roll = roll_dice(attacker_pool, tn)

    resist = damage_resistance(
        bod=target_bod,
        power=ic_rating,
        armor_rating=armor_rating,
        base_damage_level=base_damage,
        attacker_successes=attack_roll["successes"],
    )

    return {
        "attack_roll": attack_roll,
        "attack_tn": tn,
        "base_damage_level": base_damage,
        "resistance": resist,
    }


def ic_initiative_roll(ic_rating: int, security_code: str) -> int:
    """Roll IC initiative: ic_rating + Nd6 where N = IC_INITIATIVE_DICE[security_code]."""
    n_dice = IC_INITIATIVE_DICE.get(security_code, 1)
    roll = sum(random.randint(1, 6) for _ in range(n_dice))
    return ic_rating + roll


def decker_initiative_roll(
    reaction: int,
    response_increase: int = 0,
    has_hot_dnl: bool = False,
    has_reality_filter: bool = False,
) -> int:
    """
    Decker initiative: Reaction + 1D6 base + bonuses.
    +1D6 and +2 Reaction per Response Increase level (max 3).
    +1D6 if hot DNI, +1D6 if Reality Filter.
    """
    ri = min(3, response_increase)
    effective_reaction = reaction + ri * 2
    dice_count = 1 + ri + (1 if has_hot_dnl else 0) + (1 if has_reality_filter else 0)
    roll = sum(random.randint(1, 6) for _ in range(dice_count))
    return effective_reaction + roll


def dump_shock_roll(
    *,
    security_code: str,
    security_value: int,
    body: int,
    is_cool_deck: bool = False,
    has_iccm: bool = False,
    is_tortoise: bool = False,
) -> dict[str, Any]:
    """
    Resolve dump shock. Tortoise is immune.
    Power = security_value. Cool deck -2 power / -1 damage level. ICCM same.
    Resistance: Body dice vs. Power.
    """
    if is_tortoise:
        return {"immune": True, "reason": "Tortoise deck"}

    base_level = DUMP_SHOCK_LEVEL[security_code]
    power = security_value

    modifiers: list[str] = []
    if is_cool_deck:
        power = max(1, power - 2)
        base_level = stage_damage(base_level, 2, -1)
        modifiers.append("Cool deck: -2 Power, -1 Damage Level")
    if has_iccm:
        power = max(1, power - 2)
        base_level = stage_damage(base_level, 2, -1)
        modifiers.append("ICCM: -2 Power, -1 Damage Level")

    resist_roll = roll_dice(body, power)
    final = stage_damage(base_level, resist_roll["successes"], -1)

    return {
        "immune": False,
        "power": power,
        "base_level": base_level,
        "resist_roll": resist_roll,
        "final_level": final,
        "boxes": DAMAGE_BOXES[final],
        "modifiers": modifiers,
    }


def simsense_check(
    *,
    damage_level: str,
    willpower: int,
    hot_dnil_only: bool = False,
    has_iccm: bool = False,
    deck_mode: str = "hot",
) -> dict[str, Any]:
    """
    Simsense overload check (hot deck + white/gray IC only).
    Cool decks and tortoises are immune.
    Returns willpower test result and whether Stun damage is taken.
    """
    if deck_mode in ("cool", "tortoise"):
        return {"immune": True, "reason": f"{deck_mode} deck"}
    if damage_level not in SIMSENSE_OVERLOAD_TN:
        return {"immune": True, "reason": "Damage level not subject to simsense overload"}

    tn = SIMSENSE_OVERLOAD_TN[damage_level]
    if hot_dnil_only:
        tn += 2
    if has_iccm:
        tn -= 2
    tn = max(2, tn)

    roll = roll_dice(willpower, tn)
    stun_taken = roll["successes"] == 0

    return {
        "immune": False,
        "tn": tn,
        "roll": roll,
        "stun_taken": stun_taken,
    }


# -- Sheaf generator -----------------------------------------------------------

def _roll_d6() -> int:
    return random.randint(1, 6)


def _roll_2d6() -> int:
    return _roll_d6() + _roll_d6()


def _pick_unique_components(options: list[str], count: int) -> list[str]:
    pool = list(options)
    picked: list[str] = []
    for _ in range(count):
        if not pool:
            pool = list(options)
        choice = random.choice(pool)
        picked.append(choice)
        if choice in pool:
            pool.remove(choice)
    return picked


def _proactive_ic_types() -> list[str]:
    return [ic for ic, meta in IC_CATALOG.items() if meta.get("ic_type") == "proactive"]


def _table_pick(table: list[tuple[tuple[int, int], Any]], roll: int) -> Any:
    for (lo, hi), value in table:
        if lo <= roll <= hi:
            return value
    return table[-1][1]


def _roll_alert_family(zone: str) -> str:
    return _table_pick(SHEAF_ALERT_TABLE[zone], _roll_2d6())


def _build_trap_ic_event(surface_type: str, security_value: int) -> dict:
    hidden_type = _table_pick(SHEAF_TRAP_IC_TABLE, _roll_2d6())

    rating = _ic_rating(security_value)
    return {
        "type": "trap_ic",
        "surface_ic_type": surface_type,
        "surface_ic_rating": rating,
        "hidden_ic_type": hidden_type,
        "hidden_ic_rating": rating,
    }


def _build_construct_or_party_event(security_value: int) -> dict:
    components_allowed = _proactive_ic_types()

    kind = random.choice(["construct", "party_ic"])
    component_count = 2 if kind == "construct" else random.choice([2, 3])
    rating = _ic_rating(security_value)
    components = [{"type": ic_type, "rating": rating} for ic_type in _pick_unique_components(components_allowed, component_count)]

    if kind == "construct":
        threat_rating = max(1, min(4, rating // 3))
        return {
            "type": "construct",
            "threat_rating": threat_rating,
            "components": components,
            "defenses": [],
        }

    return {
        "type": "party_ic",
        "components": components,
    }


def _build_ic_event(family: str, security_value: int) -> dict | None:
    rating = _ic_rating(security_value)

    if family == "reactive_white":
        ic_type = _table_pick(SHEAF_REACTIVE_WHITE_TABLE, _roll_d6())
        return {"type": "ic", "ic_type": ic_type, "rating": rating}

    if family == "proactive_white":
        result = _table_pick(SHEAF_PROACTIVE_WHITE_TABLE, _roll_2d6())
        if result == "Crippler":
            attr = _table_pick(SHEAF_CRIPPLER_RIPPER_TARGET_TABLE, _roll_d6())
            ic_type = {"Bod": "Acid", "Evasion": "Binder", "Masking": "Marker", "Sensor": "Jammer"}[attr]
            return {"type": "ic", "ic_type": ic_type, "rating": rating}
        if result == "Killer":
            return {"type": "ic", "ic_type": "Killer", "rating": rating}
        if result == "Trap Trace":
            return _build_trap_ic_event("Trace", security_value)
        if result == "Trap Probe":
            return _build_trap_ic_event("Probe", security_value)
        if result == "Construct/Party IC":
            return _build_construct_or_party_event(security_value)
        return None

    if family == "reactive_gray":
        result = _table_pick(SHEAF_REACTIVE_GRAY_TABLE, _roll_d6())
        if result == "Trap Probe":
            return _build_trap_ic_event("Probe", security_value)
        if result == "Trap Trace":
            return _build_trap_ic_event("Trace", security_value)
        if result == "Tar Pit":
            return {"type": "ic", "ic_type": "Tar Pit", "rating": rating}
        return None

    if family == "proactive_gray":
        result = _table_pick(SHEAF_PROACTIVE_GRAY_TABLE, _roll_2d6())
        if result == "Rippers":
            attr = _table_pick(SHEAF_CRIPPLER_RIPPER_TARGET_TABLE, _roll_d6())
            ic_type = {"Bod": "Acid-rip", "Evasion": "Bind-rip", "Masking": "Mark-rip", "Sensor": "Jam-rip"}[attr]
            return {"type": "ic", "ic_type": ic_type, "rating": rating}
        if result in {"Blaster", "Sparky"}:
            return {"type": "ic", "ic_type": result, "rating": rating}
        if result == "Construct/Party IC":
            return _build_construct_or_party_event(security_value)
        return None

    if family == "black_ic":
        result = _table_pick(SHEAF_BLACK_TABLE, _roll_2d6())
        if result == "Lethal":
            return {"type": "ic", "ic_type": "Black IC", "rating": rating, "mode": "lethal"}
        if result == "Non-Lethal":
            return {"type": "ic", "ic_type": "Black IC", "rating": rating, "mode": "non_lethal"}
        if result == "Construct/Party IC":
            return _build_construct_or_party_event(security_value)
        return None

    return None


def _ic_rating(security_value: int) -> int:
    """Roll 2D6 and look up the IC rating from the IC Ratings Table (vr2_rules.md)."""
    roll = random.randint(1, 6) + random.randint(1, 6)
    if security_value <= 4:
        col = 0
    elif security_value <= 7:
        col = 1
    elif security_value <= 10:
        col = 2
    else:
        col = 3
    for (lo, hi), ratings in IC_RATINGS_TABLE:
        if lo <= roll <= hi:
            return ratings[col]
    return IC_RATINGS_TABLE[-1][1][col]


def generate_sheaf(
    *,
    security_code: str,
    security_value: int,
    step_count: int | None = None,
    seed: int | None = None,
) -> list[dict]:
    """
    Auto-generate a security sheaf for a Matrix host.

    Returns a list of sheaf steps:
      [{"trigger": int, "events": [{"type": "ic"/"passive_alert"/"active_alert"/"shutdown", ...}]}]

    Rules:
    - Trigger thresholds increase by random intervals per SHEAF_INTERVALS
    - IC families are rolled from the VR2 alert/allocation tables
    - Results follow VR2 allocation tables directly (manual curation expected)
    - Passive Alert appears in mid-section, Active Alert in late section
    - Shutdown is always the last step
    """
    if seed is None:
        return _generate_sheaf_impl(security_code, security_value, step_count)
    # Confine the seed to this call: save/restore the global RNG so a seeded
    # preview doesn't make every subsequent dice roll in the process predictable.
    # generate_sheaf has no awaits, so save/restore is safe under the async loop.
    saved = random.getstate()
    random.seed(seed)
    try:
        return _generate_sheaf_impl(security_code, security_value, step_count)
    finally:
        random.setstate(saved)


def _generate_sheaf_impl(
    security_code: str,
    security_value: int,
    step_count: int | None,
) -> list[dict]:
    """Core sheaf builder. RNG seeding/confinement is handled by generate_sheaf."""
    intervals = SHEAF_INTERVALS[security_code]
    first_min, first_max = intervals["first_range"]
    iv_min, iv_max = intervals["interval_range"]
    # Default step count based on security code
    if step_count is None:
        defaults = {"Blue": 5, "Green": 6, "Orange": 7, "Red": 8, "Black": 9}
        step_count = defaults[security_code]

    # Build trigger thresholds
    trigger = random.randint(first_min, first_max)
    triggers: list[int] = [trigger]
    for _ in range(step_count - 1):
        trigger += random.randint(iv_min, iv_max)
        triggers.append(trigger)

    passive_alert_step = step_count // 3
    active_alert_step = (step_count * 2) // 3
    shutdown_step = step_count - 1

    sheaf: list[dict] = []
    for i, trig in enumerate(triggers):
        events: list[dict] = []

        if i == shutdown_step:
            events.append({"type": "shutdown"})
            sheaf.append({"trigger": trig, "events": events})
            continue

        if i < passive_alert_step:
            zone = "none"
        elif i < active_alert_step:
            zone = "passive"
        else:
            zone = "active"

        candidate: dict | None = None
        for _ in range(64):
            family = _roll_alert_family(zone)
            if family in {"passive_alert", "active_alert", "shutdown"}:
                continue
            candidate = _build_ic_event(family, security_value)
            if candidate:
                break

        if candidate:
            events.append(candidate)

        if i == passive_alert_step:
            events.append({"type": "passive_alert"})
        elif i == active_alert_step:
            events.append({"type": "active_alert"})

        sheaf.append({"trigger": trig, "events": events})

    return sheaf


# -- Probe IC test -------------------------------------------------------------

def probe_test(ic_rating: int, det_factor: int) -> dict[str, Any]:
    """
    Probe IC test: ic_rating dice vs. detection_factor.
    Successes add to security tally.
    """
    roll = roll_dice(ic_rating, det_factor)
    return {
        "ic_rating": ic_rating,
        "detection_factor": det_factor,
        "roll": roll,
        "tally_increase": roll["successes"],
    }


# -- Trace IC hunt cycle -------------------------------------------------------

def trace_hunt_cycle_attack(
    security_value: int,
    trace_factor: int,
) -> dict[str, Any]:
    """
    One hunt cycle attack: security_value dice vs. trace_factor.
    Hunt cycle ends when trace IC gets any success.
    """
    roll = roll_dice(security_value, trace_factor)
    hit = roll["successes"] > 0
    return {"roll": roll, "hit": hit}


# -- Crippler / Ripper attack --------------------------------------------------

def crippler_attack(
    *,
    security_value: int,
    security_code: str,
    target_status: str = "intruding",
    target_attribute_rating: int,
    ic_rating: int,
    is_ripper: bool = False,
    mpcp_rating: int = 0,
    hardening: int = 0,
) -> dict[str, Any]:
    """
    Crippler/Ripper opposed attack sequence.
    - Attack: security_value dice vs COMBAT_TN[security_code][target_status]
    - Defense: target_attribute_rating dice vs ic_rating (decker uses targeted attr as dice pool)
    - Reduction = max(0, net_successes) // 2 (persists until logoff for cripplers)
    - Ripper: on any damage, also makes ic_rating dice vs (mpcp_rating + hardening)
      -> reduces the targeted attribute chip by 1 per success (permanent)
    """
    attack_tn = COMBAT_TN[security_code][target_status]
    attack_roll = roll_dice(security_value, attack_tn)
    defense_roll = roll_dice(target_attribute_rating, ic_rating)
    net = max(0, attack_roll["successes"] - defense_roll["successes"])
    reduction = net // 2

    result: dict[str, Any] = {
        "attack_roll": attack_roll,
        "defense_roll": defense_roll,
        "net_successes": net,
        "attribute_reduction": reduction,
        "is_ripper": is_ripper,
    }

    if is_ripper and net > 0 and mpcp_rating > 0:
        ripper_tn = mpcp_rating + hardening
        ripper_roll = roll_dice(ic_rating, ripper_tn)
        result["ripper_roll"] = ripper_roll
        result["chip_damage"] = ripper_roll["successes"]

    return result


# -- Tar Baby / Tar Pit test ---------------------------------------------------

def tar_baby_test(
    *,
    ic_rating: int,
    utility_rating: int,
    is_tar_pit: bool = False,
    mpcp_rating: int = 0,
    hardening: int = 0,
) -> dict[str, Any]:
    """
    Tar Baby: ic_rating dice vs. utility_rating TN vs. utility_rating dice vs. ic_rating TN.
    If IC wins: both crash. If utility wins: utility survives.
    Tar Pit additionally tests vs. MPCP to corrupt all copies.
    """
    ic_roll = roll_dice(ic_rating, utility_rating)
    util_roll = roll_dice(utility_rating, ic_rating)

    ic_wins = ic_roll["successes"] >= util_roll["successes"]
    result: dict[str, Any] = {
        "ic_roll": ic_roll,
        "util_roll": util_roll,
        "ic_wins": ic_wins,
        "utility_crashed": ic_wins,
        "ic_crashed": ic_wins,
    }

    if is_tar_pit and ic_wins and mpcp_rating > 0:
        pit_tn = mpcp_rating + hardening
        pit_roll = roll_dice(ic_rating, pit_tn)
        result["tar_pit_roll"] = pit_roll
        result["all_copies_corrupted"] = pit_roll["successes"] > 0

    return result
