"""
Shadowrun 2nd Edition Matrix rules engine.
Dice rolling, cybercombat resolution, security sheaf generation.
"""

from __future__ import annotations

import math
import random
from typing import Any, Callable

from app.services.matrix_rules import (
    DAMAGE_LEVELS, DAMAGE_BOXES, ICON_DAMAGE_BOXES, STAGE_SCALE, IC_DAMAGE_LEVEL,
    DUMP_SHOCK_LEVEL, COMBAT_TN, SIMSENSE_OVERLOAD_TN,
    MEDIC_TN,
    IC_INITIATIVE_DICE, SHEAF_INTERVALS,
    IC_RATINGS_TABLE,
    SHEAF_ALERT_TABLE, SHEAF_REACTIVE_WHITE_TABLE, SHEAF_PROACTIVE_WHITE_TABLE,
    SHEAF_REACTIVE_GRAY_TABLE, SHEAF_PROACTIVE_GRAY_TABLE, SHEAF_BLACK_TABLE,
    SHEAF_TRAP_IC_TABLE, SHEAF_CRIPPLER_RIPPER_TARGET_TABLE,
    IC_OPTIONS_TABLE, IC_DEFENSE_TABLE,
    IC_CATALOG,
)
from app.services.run_trace import trace


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
    trace(
        f"roll {pool}d6 vs TN {tn} -> {successes} success(es)"
        + (f", {ones} one(s)" if ones else "")
        + (f" [rule of 6, per-die totals {dice}]" if tn > 6 else "")
    )
    return {"pool": pool, "tn": tn, "dice": dice, "successes": successes, "ones": ones}


def hacking_pool(intelligence: int, mpcp: int) -> int:
    """Hacking Pool = (Intelligence + MPCP) // 3."""
    return (intelligence + mpcp) // 3


def detection_factor(masking: int, sleaze_rating: int = 0) -> int:
    """Detection Factor = ceil((masking + sleaze) / 2) if sleaze > 0, else ceil(masking / 2)."""
    if sleaze_rating > 0:
        df = math.ceil((masking + sleaze_rating) / 2)
        trace(f"detection factor: ceil((masking {masking} + sleaze {sleaze_rating}) / 2) = {df}")
        return df
    df = math.ceil(masking / 2)
    trace(f"detection factor: ceil(masking {masking} / 2) = {df}")
    return df


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
    # A nonzero tie goes to the decker; a 0-vs-0 tie is a mutual whiff, so the decker must
    # score at least one success for the task to succeed.
    success = decker_net >= 0 and decker_roll["successes"] > 0

    trace(
        f"system test: decker {decker_pool}d6 vs subsystem TN {subsystem_rating}"
        + (f" {extra_tn_modifier:+d} mod" if extra_tn_modifier else "")
        + f" = TN {decker_tn} -> {decker_roll['successes']} succ; "
        f"host {security_value}d6 vs DF {det_factor} -> {host_roll['successes']} succ; "
        f"net {decker_net} => {'SUCCESS' if success else 'FAIL'}, tally +{host_roll['successes']}"
    )
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
    Stage damage up (direction=1) or down (direction=-1) by net_successes // 2 on the full staging
    scale (``STAGE_SCALE`` = None, Light, Moderate, Serious, Deadly). ``net_successes`` may be
    negative (a net-successes-first resolution can hand this a negative value with direction=1);
    division truncates toward zero so 2 full successes are always needed to move one level in either
    sense. A hit can be staged DOWN to ``None`` (fully resisted -- no damage) but never UP past
    ``Deadly``.
    """
    steps = int(net_successes / 2)
    idx = STAGE_SCALE.index(base_level)
    idx = max(0, min(len(STAGE_SCALE) - 1, idx + direction * steps))
    result = STAGE_SCALE[idx]
    if steps:
        trace(
            f"stage {base_level} {'up' if direction > 0 else 'down'} by {steps} "
            f"(net {net_successes} succ / 2) -> {result}"
        )
    return result


def damage_resistance(
    *,
    bod: int,
    power: int,
    armor_rating: int = 0,
    base_damage_level: str,
    attacker_successes: int = 0,
    shield_successes: int = 0,
    body_damage: bool = False,
    defender_bonus_dice: int = 0,
) -> dict[str, Any]:
    """
    Resolve a damage resistance roll.
    - Effective power = power - armor_rating (min 1)
    - Shield parry: net Shield Test successes cancel attacker damage successes 1:1 BEFORE
      staging, clamped at 0 (a parry can blunt a hit but never reverse it). Armor (a Power
      reduction) is a SEPARATE defence and stacks with Shield (a successes reduction).
    - Resistance roll: (bod + defender_bonus_dice) dice vs. effective_power. ``defender_bonus_dice``
      is Hacking Pool the defender chose to spend on THIS resist (vr2: HP may be added to defense
      tests -- but NOT to Body/Willpower tests vs gray/black IC; that gate is the caller's).
    - NET-SUCCESSES-FIRST staging: the defender resists, then the damage level is staged ONCE
      from the base by (attacker net successes - resistance successes) // 2. This preserves
      excess attacker successes above Deadly through the resist step instead of capping the hit
      at Deadly before the defender rolls (a Deadly-capped hit that is then resisted would lose
      the excess and drop too far). Damage is still clamped at Deadly -- no over-Deadly overflow.
    - ``body_damage``: select the box table. Icon/persona damage uses ICON_DAMAGE_BOXES
      (1/2/3/6); physical/stun damage to the operator's meat body uses DAMAGE_BOXES (1/3/6/10).
    Returns effective power, resistance roll, and final damage level.
    """
    effective_power = max(1, power - armor_rating)
    shield_successes = max(0, shield_successes)
    net_attacker = max(0, attacker_successes - shield_successes)
    # Informational: where the hit would land on attacker successes alone (pre-resist).
    staged_up = stage_damage(base_damage_level, net_attacker, 1)
    # Defender resists, THEN stage once from the base by the combined net successes.
    resist_roll = roll_dice(bod + max(0, defender_bonus_dice), effective_power)
    net = net_attacker - resist_roll["successes"]
    final = stage_damage(base_damage_level, net, 1)
    box_table = DAMAGE_BOXES if body_damage else ICON_DAMAGE_BOXES
    trace(
        f"damage resist: power {power} - armor {armor_rating} = {effective_power}; "
        f"attacker succ {attacker_successes} - shield {shield_successes} = {net_attacker}; "
        f"resist {bod + max(0, defender_bonus_dice)}d6 vs {effective_power} -> {resist_roll['successes']} succ; "
        f"net {net} from base {base_damage_level} -> final {final} ({box_table[final]} boxes)"
    )
    return {
        "effective_power": effective_power,
        "attacker_successes": net_attacker,
        "shield_successes": shield_successes,
        "staged_up_level": staged_up,
        "resist_roll": resist_roll,
        "final_damage_level": final,
        "boxes": box_table[final],
    }


def shield_parry(*, shield_rating: int, attacker_skill: int) -> dict[str, Any]:
    """Defensive Shield utility parry (vr2): roll the Shield's effective rating in dice against
    the attacker's skill (Computer Skill for a decker, Security Value for IC). The resulting
    successes are subtracted from the attacker's damage successes (for damage attacks) or added
    to the decker's side of an opposed test (for crippler/ripper attribute attacks).

    Pure roll only -- the caller degrades the Shield by 1 Rating Point per use (regardless of
    outcome) and reloads a fresh copy via the Swap Memory operation.
    """
    rating = max(1, shield_rating)
    roll = roll_dice(rating, max(2, attacker_skill))
    trace(f"shield parry: {rating}d6 vs attacker skill {roll['tn']} -> {roll['successes']} succ")
    return {"roll": roll, "successes": roll["successes"], "shield_rating": rating, "tn": roll["tn"]}


def medic_heal(*, medic_rating: int, wound_level: str) -> dict[str, Any]:
    """Defensive Medic utility heal (vr2): roll the Medic's effective rating in dice against a
    target number set by the icon's current wound level (Light 4 / Moderate 5 / Serious 6). Each
    success heals 1 box of the persona/icon Condition Monitor.

    Pure roll only -- the caller subtracts ``boxes_healed`` from the filled condition-monitor
    boxes (floored at 0, capped by the current damage), degrades the Medic by 1 Rating Point per
    use (regardless of outcome), and reloads a fresh copy via the Swap Memory operation.
    """
    rating = max(1, medic_rating)
    tn = MEDIC_TN[wound_level]
    roll = roll_dice(rating, tn)
    trace(f"medic heal: {rating}d6 vs {wound_level} TN {tn} -> heal {roll['successes']} box(es)")
    return {
        "roll": roll,
        "tn": tn,
        "wound_level": wound_level,
        "medic_rating": rating,
        "boxes_healed": roll["successes"],
    }


def restore_repair(*, restore_rating: int, causing_rating: int, damage_points: int) -> dict[str, Any]:
    """Defensive Restore utility (vr2): repair damage to the online icon's persona attributes
    (Bod/Evasion/Masking/Sensor) caused by cripplers. Roll the Restore's effective rating in dice
    against a target number equal to the rating of the program that caused the damage (the highest
    rating when several programs are involved). Every 2 successes repairs 1 point of attribute
    damage, capped by the damage currently present.

    Pure roll only. Unlike Medic, Restore does NOT lose a Rating Point per use (the rule has no
    degradation clause), and it CANNOT repair permanent Persona-chip damage from gray/black IC
    (Rippers) -- the caller passes only the temporary, repairable damage in ``damage_points``.
    """
    rating = max(1, restore_rating)
    tn = max(2, causing_rating)
    roll = roll_dice(rating, tn)
    points = min(max(0, damage_points), roll["successes"] // 2)
    trace(
        f"restore: {rating}d6 vs causing rating {tn} -> {roll['successes']} succ "
        f"-> repair {points} attribute point(s)"
    )
    return {
        "roll": roll,
        "tn": tn,
        "restore_rating": rating,
        "causing_rating": causing_rating,
        "successes": roll["successes"],
        "points_repaired": points,
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
    shield_successes: int = 0,
    base_damage_level: str | None = None,
    shield_parry: Callable[[], int] | None = None,
    defender_bonus_dice: int = 0,
    precomputed_attack_roll: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Resolve a single cybercombat attack exchange.
    - attacker_pool: attacker's dice pool (Security Value for IC; attack utility + hacking pool for decker)
    - security_code: host security code string
    - target_status: "intruding" or "legitimate" -- the TARGET icon's status (vr2: valid-passcode
      icons are Legitimate, all others Intruding), which selects the to-hit column
    - target_bod: defender Bod rating (for resistance)
    - armor_rating: Armor utility rating (reduces Power)
    - ic_rating: IC's rating (determines Power and, for IC, the base damage level)
    - attacker_is_ic: if True, IC attacks decker; if False, decker attacks IC
    - tn_modifier: additional TN adjustment (e.g. Party IC cluster penalty)
    - shield_successes: defender's Shield parry successes, subtracted from the attack's damage
      successes before staging (a hit on the decker's persona; see damage_resistance)
    - base_damage_level: override the base Damage Level. IC read their severity from the host
      Security Code (``IC_DAMAGE_LEVEL[security_code]``), so IC callers leave this None; a decker's
      Attack utility carries its OWN level (Attack-6L/-6M/-6S/-6D) and passes it here. Only the
      damage SEVERITY follows the program -- the to-hit still uses the host COMBAT_TN.
    - shield_parry: optional deferred Shield callback (vr2). The persona is only "affected" -- and
      the defender only rolls (and wears) a Shield -- when the attack actually lands, so the caller
      passes a callback that rolls+wears the Shield; it is invoked ONLY when the attack scores >= 1
      success, and its return value overrides ``shield_successes``. A clean miss rolls no Shield.
    """
    tn = max(2, COMBAT_TN[security_code][target_status] + tn_modifier)
    base_damage = base_damage_level if base_damage_level in DAMAGE_LEVELS else IC_DAMAGE_LEVEL[security_code]

    trace(
        f"cybercombat {'IC->decker' if attacker_is_ic else 'decker->IC'}: "
        f"{attacker_pool}d6 vs TN {tn} ({security_code}/{target_status}"
        + (f", {tn_modifier:+d} mod" if tn_modifier else "") + f"), base damage {base_damage}"
    )
    # ``precomputed_attack_roll``: reuse a to-hit already rolled by the caller (the interactive
    # per-attack defense flow rolls the to-hit first so the player sees it, THEN resolves the resist
    # with the Hacking Pool dice they chose). Backward-compatible -- callers that omit it roll now.
    attack_roll = precomputed_attack_roll if precomputed_attack_roll is not None else roll_dice(attacker_pool, tn)

    # Shield only fires when the attack lands (the persona is affected); a clean miss rolls no Shield.
    if shield_parry is not None and attack_roll["successes"] > 0:
        shield_successes = shield_parry()

    resist = damage_resistance(
        bod=target_bod,
        power=ic_rating,
        armor_rating=armor_rating,
        base_damage_level=base_damage,
        attacker_successes=attack_roll["successes"],
        shield_successes=shield_successes,
        defender_bonus_dice=defender_bonus_dice,
    )

    return {
        "attack_roll": attack_roll,
        "attack_tn": tn,
        "base_damage_level": base_damage,
        "resistance": resist,
    }


def black_attack(
    *,
    attacker_pool: int,
    security_code: str,
    target_status: str = "intruding",
    base_damage_level: str,
    power: int,
    hardening: int = 0,
    icon_bod: int,
    icon_armor: int = 0,
    tn_modifier: int = 0,
    shield_successes: int = 0,
    meat_pool: int | None = None,
    meat_is_stun: bool = False,
    shield_parry: Callable[[], int] | None = None,
) -> dict[str, Any]:
    """Resolve one Black-family strike (Black IC / Black Hammer / Killjoy).

    Shared by every actor that can fire one -- enemy Black IC, an enemy decker's Black Hammer /
    Killjoy, and the PC's own Black Hammer / Killjoy -- so the mechanic resolves identically no
    matter who pulls the trigger. A SINGLE Attack Test drives BOTH resistance tests off the same
    successes (vr2: black IC / Black Hammer "damage the icon AND the operator" from one strike):

    - icon: ``icon_bod`` dice vs Power. Hardening reduces Power; Armor reduces it further.
    - meat: ``meat_pool`` dice vs Power. Hardening reduces Power; Armor does NOT protect the
      operator. ``meat_pool`` is the operator's Body (lethal) or Willpower (non-lethal / Killjoy);
      pass ``None`` when the target is an NPC whose flesh is not simulated (PC -> enemy decker),
      which yields an icon-only result.

    ``base_damage_level`` is supplied by the caller: the host Security Code table
    (``IC_DAMAGE_LEVEL[sec]``) for black IC, or a fixed level for the Black Hammer / Killjoy
    programs. The to-hit still uses the host's ``COMBAT_TN`` -- only the damage SEVERITY follows the
    program. Both resistance tests share one ``power`` (Position-Power maneuver bonuses fold into
    it), so a combat maneuver shifts the whole strike, not just one half of it.

    Returns the attack roll plus an ``icon`` (always) and ``meat`` (or ``None``) ``damage_resistance``
    result. The caller applies boxes to the correct condition monitor, composes the event, and
    resolves crash / MPCP-burn / jack-out consequences per actor.
    """
    tn = max(2, COMBAT_TN[security_code][target_status] + tn_modifier)
    attack_roll = roll_dice(attacker_pool, tn)
    # One deferred Shield parry blunts BOTH resistance tests -- but only when the strike lands
    # (persona affected). A clean miss (0 attack successes) rolls no Shield and wears nothing.
    if shield_parry is not None and attack_roll["successes"] > 0:
        shield_successes = shield_parry()
    resist_power = power - hardening  # floored by damage_resistance via max(1, power - armor)
    icon = damage_resistance(
        bod=icon_bod,
        power=resist_power,
        armor_rating=icon_armor,
        base_damage_level=base_damage_level,
        attacker_successes=attack_roll["successes"],
        shield_successes=shield_successes,
    )
    meat = None
    if meat_pool is not None:
        meat = damage_resistance(
            bod=meat_pool,
            power=resist_power,
            armor_rating=0,
            base_damage_level=base_damage_level,
            attacker_successes=attack_roll["successes"],
            shield_successes=shield_successes,
            body_damage=True,
        )
    trace(
        f"black_attack {security_code}/{target_status}: {attacker_pool}d6 vs TN {tn} "
        f"-> {attack_roll['successes']} succ; base {base_damage_level}; "
        f"icon {icon['final_damage_level']} ({icon['boxes']})"
        + (
            f"; meat {'stun' if meat_is_stun else 'phys'} "
            f"{meat['final_damage_level']} ({meat['boxes']})"
            if meat
            else "; icon-only"
        )
    )
    return {
        "attack_roll": attack_roll,
        "attack_tn": tn,
        "base_damage_level": base_damage_level,
        "icon": icon,
        "meat": meat,
        "meat_is_stun": meat_is_stun,
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
    deck_mode: str = "hot",
) -> int:
    """
    Decker initiative (vr2 L1913-1923): Reaction + 1D6 base + bonuses.
    +1D6 and +2 Reaction per Response Increase level (max 3).
    +1D6 if hot DNI, +1D6 if Reality Filter.
    Cool deck: -1D6 Initiative (running cool with manual controls).
    Tortoise: no ASIST -- half Reaction (min 1) and only 1D6 regardless of Response
    Increase / other bonuses.
    Always rolls at least 1 initiative die (SR2 core minimum).
    """
    mode = (deck_mode or "hot").lower()
    if mode == "tortoise":
        effective_reaction = max(1, reaction // 2)
        dice_count = 1                       # single die, no RI/RF/hot bonus
    else:
        ri = min(3, response_increase)
        effective_reaction = reaction + ri * 2
        dice_count = 1 + ri + (1 if has_hot_dnl else 0) + (1 if has_reality_filter else 0)
        if mode == "cool":
            dice_count -= 1                  # -1D6 running cool with manual controls
        dice_count = max(1, dice_count)      # SR2: always at least 1 initiative die
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


def _roll_alert_family(zone: str, steps_passed: int = 0) -> str:
    """Roll on the Alert Table (vr2_rules.md L857-873) for one trigger step. RAW: roll **1D6** and
    **add the number of trigger steps already passed in the CURRENT alert level** (the counter
    resets to 0 on every escalation). This ramp applies to all three levels -- No Alert, Passive
    Alert, and Active Alert -- so each level eventually rolls the 8+ escalation row
    (No->Passive->Active->Shutdown); the lower rows name an IC family to activate. Escalation is
    impossible in the first couple of steps of a level and steadily more likely as its tally
    climbs -- deckers get poking-around time early, urgency late."""
    return _table_pick(SHEAF_ALERT_TABLE[zone], _roll_d6() + steps_passed)


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


def _build_construct_or_party_event(security_value: int, security_code: str = "Black") -> dict:
    components_allowed = _proactive_ic_types()

    kind = random.choice(["construct", "party_ic"])
    capacity = max(2, security_value * 2)
    max_rating = max(1, math.ceil(security_value * 2 / 3))
    max_party_count = max(1, security_value // 2)
    component_count = 2 if kind == "construct" else min(random.choice([2, 3]), max_party_count)
    rating = min(_ic_rating(security_value), max_rating)

    picked = _pick_unique_components(components_allowed, component_count)
    components = []
    remaining = capacity
    for ic_type in picked:
        surcharge = 2 if IC_CATALOG.get(ic_type, {}).get("category") == "black" else (
            1 if IC_CATALOG.get(ic_type, {}).get("category") == "gray" else 0
        )
        component_rating = min(rating, max(1, remaining - surcharge))
        if component_rating + surcharge > remaining:
            break
        components.append({"type": ic_type, "rating": component_rating})
        remaining -= component_rating + surcharge

    if kind == "construct":
        max_threat = {"Blue": 0, "Green": 1, "Orange": 2, "Red": 3, "Black": 4}.get(
            security_code, 4,
        )
        threat_rating = min(max_threat, max(0, rating // 3))
        # Roll the IC Defenses Table for the construct's single combined icon (vr2).
        defense = _table_pick(IC_DEFENSE_TABLE, _roll_2d6())
        defenses = [d for d in ("Armor", "Shifting", "Shielding") if d in defense]
        while defenses and len(defenses) * 2 > remaining:
            defenses.pop()
        return {
            "type": "construct",
            "threat_rating": threat_rating,
            "components": components,
            "defenses": defenses,
        }

    # Party IC: each component is its own combat icon -- roll Options + Defenses for each.
    for component in components:
        extras = _roll_ic_extras()
        options = list(extras.get("options") or [])
        while options and len(options) > remaining:
            options.pop()
        if options:
            extras["options"] = options
            remaining -= len(options)
        else:
            extras.pop("options", None)
        component.update(extras)
    return {
        "type": "party_ic",
        "components": components,
    }


def _roll_ic_extras() -> dict[str, Any]:
    """Roll the IC Options + IC Defenses tables (vr2) for a generated combat IC.

    Returns event fields to merge into the IC dict: ``options`` (Armor/Shielding/Shifting),
    ``cascading``, and/or ``expert`` ({type: offense|defense, value: 1D3}). Shield/Shift
    flow into the decker's to-hit TN; Armor/Cascading/Expert are carried for the GM/UI.
    """
    extras: dict[str, Any] = {}
    opt = _table_pick(IC_OPTIONS_TABLE, _roll_2d6())
    if opt == "Cascading":
        extras["cascading"] = True
    elif opt == "Expert Offense":
        extras["expert"] = {"type": "offense", "value": random.randint(1, 3)}
    elif opt == "Expert Defense":
        extras["expert"] = {"type": "defense", "value": random.randint(1, 3)}
    defense = _table_pick(IC_DEFENSE_TABLE, _roll_2d6())
    opts = [d for d in ("Armor", "Shifting", "Shielding") if d in defense]
    if opts:
        extras["options"] = opts
    return extras


def _build_ic_event(family: str, security_value: int, security_code: str = "Black") -> dict | None:
    rating = _ic_rating(security_value)

    if family == "reactive_white":
        ic_type = _table_pick(SHEAF_REACTIVE_WHITE_TABLE, _roll_d6())
        return {"type": "ic", "ic_type": ic_type, "rating": rating}

    if family == "proactive_white":
        result = _table_pick(SHEAF_PROACTIVE_WHITE_TABLE, _roll_2d6())
        if result == "Crippler":
            attr = _table_pick(SHEAF_CRIPPLER_RIPPER_TARGET_TABLE, _roll_d6())
            ic_type = {"Bod": "Acid", "Evasion": "Binder", "Masking": "Marker", "Sensor": "Jammer"}[attr]
            return {"type": "ic", "ic_type": ic_type, "rating": rating, **_roll_ic_extras()}
        if result == "Killer":
            return {"type": "ic", "ic_type": "Killer", "rating": rating, **_roll_ic_extras()}
        if result == "Trap Trace":
            return _build_trap_ic_event("Trace", security_value)
        if result == "Trap Probe":
            return _build_trap_ic_event("Probe", security_value)
        if result == "Construct/Party IC":
            return _build_construct_or_party_event(security_value, security_code)
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
            return {"type": "ic", "ic_type": ic_type, "rating": rating, **_roll_ic_extras()}
        if result in {"Blaster", "Sparky"}:
            return {"type": "ic", "ic_type": result, "rating": rating, **_roll_ic_extras()}
        if result == "Construct/Party IC":
            return _build_construct_or_party_event(security_value, security_code)
        return None

    if family == "black_ic":
        result = _table_pick(SHEAF_BLACK_TABLE, _roll_2d6())
        if result == "Lethal":
            return {"type": "ic", "ic_type": "Black IC", "rating": rating, "mode": "lethal", **_roll_ic_extras()}
        if result == "Non-Lethal":
            return {"type": "ic", "ic_type": "Black IC", "rating": rating, "mode": "non_lethal", **_roll_ic_extras()}
        if result == "Construct/Party IC":
            return _build_construct_or_party_event(security_value, security_code)
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
    - Alert state EMERGES from the per-step 1D6+ramp roll (vr2 L857-873): No -> Passive -> Active
      -> Shutdown, each escalating only when its step rolls the 8+ row. Early steps effectively
      cannot escalate (the ramp is small); late steps almost certainly do.
    - Shutdown is not guaranteed and is not forced onto the last step (it is operator-initiated).
    """
    if step_count is not None and not 1 <= step_count <= 64:
        raise ValueError("step_count must be between 1 and 64")
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

    # Walk the steps in order, carrying the live alert state. Each step rolls 1D6 + (steps already
    # passed IN THE CURRENT alert level -- the counter resets on every escalation) against that
    # level's Alert Table (vr2 L857-873): an 8+ result escalates the level (No->Passive->Active->
    # Shutdown) and is that step's event; any other result activates the named IC family.
    sheaf: list[dict] = []
    zone = "none"
    level_steps = 0
    for trig in triggers:
        events: list[dict] = []
        outcome = _roll_alert_family(zone, level_steps)
        if outcome == "passive_alert":
            zone = "passive"
            level_steps = 0
            events.append({"type": "passive_alert"})
        elif outcome == "active_alert":
            zone = "active"
            level_steps = 0
            events.append({"type": "active_alert"})
        elif outcome == "shutdown":
            level_steps = 0
            events.append({"type": "shutdown"})
        else:
            level_steps += 1
            candidate = _build_ic_event(outcome, security_value, security_code)
            if candidate:
                events.append(candidate)
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

def attribute_attack_core(
    *,
    attacker_pool: int,
    resist_tn: int,
    security_code: str,
    target_status: str,
    target_attribute_rating: int,
    shield_successes: int = 0,
    tn_modifier: int = 0,
    shield_parry: Callable[[], int] | None = None,
) -> dict[str, Any]:
    """Shared attribute-crippling core for BOTH the IC cripplers (Acid / Binder / Marker /
    Jammer) and the decker programs (Poison / Restrict / Reveal) -- the rules explicitly say the
    decker programs work "like" the matching crippler IC, so the dice math is modelled ONCE here
    and the public entry point crippler_attack delegates to it; the router's _resolve_attribute_attack
    routes BOTH the IC cripplers and the decker programs (Poison / Restrict / Reveal) through it.

    - Attack: ``attacker_pool`` dice vs COMBAT_TN[security_code][target_status] (+ tn_modifier).
    - Resist: ``target_attribute_rating`` dice vs ``resist_tn`` (the attacker's program/IC rating).
    - Shield: net defender Shield Test successes ADD to the resist side (vr2).
    - Reduction = max(0, net) // 2  (1 attribute point per 2 net successes).

    ``shield_parry`` is an optional deferred Shield callback: the persona is only "affected" when
    the crippler's attack scores hits, so the Shield is rolled (and worn) ONLY when the attack
    roll lands >= 1 success -- a resisted/whiffed crippler rolls no Shield. Its return overrides
    ``shield_successes``.

    Returns neutral keys (attack_roll / resist_roll / net / reduction / shield_successes); the
    two public wrappers re-label these to preserve their historical return contracts."""
    attack_tn = max(2, COMBAT_TN[security_code][target_status] + tn_modifier)
    attack_roll = roll_dice(attacker_pool, attack_tn)
    resist_roll = roll_dice(target_attribute_rating, resist_tn)
    if shield_parry is not None and attack_roll["successes"] > 0:
        shield_successes = shield_parry()
    shield_successes = max(0, shield_successes)
    net = max(0, attack_roll["successes"] - resist_roll["successes"] - shield_successes)
    return {"attack_roll": attack_roll, "resist_roll": resist_roll, "net": net,
            "reduction": net // 2, "shield_successes": shield_successes}


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
    shield_successes: int = 0,
    tn_modifier: int = 0,
    shield_parry: Callable[[], int] | None = None,
) -> dict[str, Any]:
    """
    Crippler/Ripper opposed attack sequence (IC side of attribute_attack_core).
    - Attack: security_value dice vs COMBAT_TN[security_code][target_status]
    - Defense: target_attribute_rating dice vs ic_rating (decker uses targeted attr as dice pool)
    - Shield: net Shield Test successes ADD to the decker's defence side (vr2)
    - Reduction = max(0, net_successes) // 2 (persists until logoff for cripplers)
    - Ripper: on any damage, also makes ic_rating dice vs (mpcp_rating + hardening)
      -> reduces the targeted attribute chip by 1 per success (permanent)
    - tn_modifier: combat-maneuver adjustment to the attack TN (Parry raises it, Position
      lowers it); defaults to 0 so existing callers are unaffected.
    - shield_parry: optional deferred Shield callback -- rolled/worn ONLY when the crippler's
      attack lands (>= 1 success); overrides ``shield_successes``.
    """
    core = attribute_attack_core(
        attacker_pool=security_value, resist_tn=ic_rating, security_code=security_code,
        target_status=target_status, target_attribute_rating=target_attribute_rating,
        shield_successes=shield_successes, tn_modifier=tn_modifier, shield_parry=shield_parry)
    net = core["net"]
    result: dict[str, Any] = {
        "attack_roll": core["attack_roll"],
        "defense_roll": core["resist_roll"],
        "shield_successes": core["shield_successes"],
        "net_successes": net,
        "attribute_reduction": core["reduction"],
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

    # Ties favor the decker's utility. Tar must score strictly more successes to crash it.
    ic_wins = ic_roll["successes"] > util_roll["successes"]
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


# -- Steamroller (anti-tar utility) --------------------------------------------

# A Tar Baby / Tar Pit IC uses the SAME 10-box condition monitor as any other IC (user ruling
# 2026-07-17): tar programs are not special-cased into a shallow track. Steamroller simply takes
# one down FASTER because it lands full (Rating)D hits (6 icon boxes each), so a solid two-strike
# Steamroller crashes it while chip damage or a badly under-rated Steamroller takes longer.
TAR_IC_CONDITION_BOXES = 10


def steamroller_attack(
    *,
    steamroller_rating: int,
    steamroller_pool: int,
    tar_ic_rating: int,
    to_hit_tn: int = 4,
    existing_boxes: int = 0,
) -> dict[str, Any]:
    """Resolve a Steamroller utility strike against a Tar Baby / Tar Pit IC
    (vr2_rules.md L1581-1585: "Inflicts (Rating)D damage to tar IC programs ... Immune to the
    destructive effect of tar programs -- tar IC cannot crash the Steamroller utility").

    Steamroller is a *one-way* weapon: it does NOT run the tar program's opposed crash test
    (that immunity is enforced by the caller never invoking ``tar_baby_test``). Instead it
    resolves like a normal IC-damage hit so the existing staging math decides the outcome:

    - To-hit: ``steamroller_pool`` dice (decker Computer skill + hacking pool) vs ``to_hit_tn``.
    - Damage: a Deadly-level attack with Power = the Steamroller's effective ``steamroller_rating``.
      The tar IC resists with ``tar_ic_rating`` dice vs that Power, staging the Deadly hit DOWN.
      This is why a high-rating Steamroller reliably crashes (the tar can't stage a high-Power
      Deadly far enough down) while a very low rating can fail (low Power -> low resist TN ->
      the tar stages it down to a Light graze).
    - The resolved damage fills the tar's condition monitor; it crashes once the accumulated boxes
      reach ``TAR_IC_CONDITION_BOXES`` (a full 10-box IC monitor). A clean (Rating)D lands 6 icon
      boxes, so a solid two-strike Steamroller crashes it -- faster than chipping it with plain
      attacks, but no longer a one-shot.

    Returns the to-hit roll, the resistance result, the boxes inflicted this strike, the running
    total against the tar's monitor, and whether it crashed.
    """
    to_hit = roll_dice(max(1, steamroller_pool), max(2, to_hit_tn))
    resist = damage_resistance(
        bod=max(1, tar_ic_rating),
        power=max(1, steamroller_rating),
        base_damage_level="Deadly",
        attacker_successes=to_hit["successes"],
    )
    boxes = resist["boxes"]
    total_boxes = max(0, existing_boxes) + boxes
    crashed = total_boxes >= TAR_IC_CONDITION_BOXES
    return {
        "to_hit_roll": to_hit,
        "resist": resist,
        "damage_level": resist["final_damage_level"],
        "boxes": boxes,
        "total_boxes": total_boxes,
        "tar_cm": TAR_IC_CONDITION_BOXES,
        "crashed": crashed,
    }


# -- Slow (anti-proactive-IC utility) ------------------------------------------

def slow_test(
    *,
    decker_pool: int,
    slow_rating: int,
    ic_dice: int,
) -> dict[str, Any]:
    """Resolve the opposed Resistance (Slow Rating) Test for the Slow utility
    (vr2_rules.md L1572-1578): after a Slow attack hits a proactive IC, the IC makes an opposed
    Resistance Test and -- if the attacker wins -- loses execution speed.

    Modelled as a symmetric SR2 opposed test (mirrors ``tar_baby_test``):
    - The decker (the Slow program) rolls ``decker_pool`` dice -- the Slow Rating -- vs the IC's
      rating as TN (``ic_dice``).
    - The IC resists with ``ic_dice`` dice (its rating) vs the Slow Rating as TN.
    - ``net_successes`` = decker successes - IC successes. With the attacker ahead, the IC loses
      one action per 2 net successes (``actions_lost`` = net // 2 -- a PURE floor; the caller
      applies the "at least one action lost on a win" and the hang/resume rules).

    Uses the rule-of-6 dice via ``roll_dice`` (TNs floored at 2, the SR2 minimum). Pure and
    side-effect free -- the run layer decides how the lost actions translate into skipped passes.
    """
    decker_roll = roll_dice(max(1, decker_pool), max(2, ic_dice))
    ic_roll = roll_dice(max(1, ic_dice), max(2, slow_rating))
    net = decker_roll["successes"] - ic_roll["successes"]
    actions_lost = max(0, net) // 2
    return {
        "decker_roll": decker_roll,
        "ic_roll": ic_roll,
        "slow_rating": slow_rating,
        "net_successes": net,
        "actions_lost": actions_lost,
    }


# -- Data Bomb -----------------------------------------------------------------

def data_bomb_defuse(
    *,
    decker_pool: int,
    subsystem_rating: int,
    defuse_utility: int = 0,
) -> dict[str, Any]:
    """Defuse a Data Bomb (vr2_rules.md L463-471): a Computer Test against the controlling
    subsystem rating reduced by the carried Defuse utility -- TN = (Files Rating for a file bomb,
    or Slave Rating for a device bomb) - Defuse Rating, floored at 2. Uses the rule-of-6 dice via
    roll_dice.

    - ``defused`` (>=1 success): the bomb is disarmed. A successful defuse does NOT count as
      crashing, so the caller adds NO security tally (the bomb's rating is never added on success).
    - ``detonated``: the decker rolled ALL 1s (every die a 1 -- a botch), which sets the bomb off.
    - Any other failure leaves the bomb primed; the decker may try again.
    """
    tn = max(2, subsystem_rating - defuse_utility)
    roll = roll_dice(decker_pool, tn)
    defused = roll["successes"] > 0
    detonated = (not defused) and roll["ones"] == roll["pool"]
    return {"roll": roll, "tn": tn, "defused": defused, "detonated": detonated}


def data_bomb_detonate(
    *,
    ic_rating: int,
    target_bod: int,
    armor_rating: int = 0,
    shield_successes: int = 0,
) -> dict[str, Any]:
    """Data Bomb explodes when a protected target is accessed undefused (vr2).

    Inflicts a fixed (IC rating)M against the persona (Bod resists, Armor reduces
    Power) and adds the IC rating to the security tally.

    A Shield parry has no attack-staging successes to cancel here (the (rating)M is
    automatic), so its net successes instead stage the resolved damage DOWN (2 successes =
    one level) -- the only sensible reading of "reduce the attacker's damage" for a fixed hit.
    """
    resist = damage_resistance(
        bod=target_bod,
        power=ic_rating,
        armor_rating=armor_rating,
        base_damage_level="Moderate",
        attacker_successes=0,  # fixed (rating)M -- no attack-success staging
    )
    shield_successes = max(0, shield_successes)
    if shield_successes > 0:
        lowered = stage_damage(resist["final_damage_level"], shield_successes, -1)
        resist["final_damage_level"] = lowered
        resist["boxes"] = ICON_DAMAGE_BOXES[lowered]
        resist["shield_successes"] = shield_successes
    return {"damage_level": "Moderate", "tally_increase": ic_rating, "resistance": resist}


# -- Worm ----------------------------------------------------------------------

def worm_attack(
    *,
    security_value: int,
    mpcp_rating: int,
    hardening: int = 0,
) -> dict[str, Any]:
    """Worm Infection Test (vr2_rules.md L548-550 + user ruling 2026-07-10).

    The HOST rolls its Security Value dice against a target number equal to the deck's MPCP
    rating. Subtract the deck's Hardening from the worm's successes; a net GREATER THAN ZERO
    (i.e. successes exceed Hardening) infects the MPCP -- a permanent corruption that requires
    replacing the chip. A worm carries no IC rating, so this test never touches the security
    tally (the caller adds none).
    """
    tn = max(2, mpcp_rating)
    roll = roll_dice(security_value, tn)
    net = roll["successes"] - hardening
    infected = net > 0
    return {
        "roll": roll,
        "tn": tn,
        "net_successes": net,
        "mpcp_infected": infected,
        "chip_replacement_required": infected,
    }


def disinfect_test(
    *,
    decker_pool: int,
    subsystem_rating: int,
    disinfect_utility: int = 0,
    security_value: int,
    det_factor: int,
) -> dict[str, Any]:
    """Resolve Disinfect as an opposed host System Test with its utility TN reduction."""
    result = system_test(
        decker_pool=decker_pool,
        subsystem_rating=subsystem_rating,
        security_value=security_value,
        det_factor=det_factor,
        extra_tn_modifier=-disinfect_utility,
    )
    return {
        **result,
        "roll": result["decker_roll"],
        "tn": result["decker_roll"]["tn"],
        "worm_destroyed": result["success"],
    }


# -- Scramble IC (paydata protection) ------------------------------------------

def scramble_decrypt_test(
    *,
    decker_pool: int,
    scramble_rating: int,
    decrypt_utility: int = 0,
) -> dict[str, Any]:
    """Attempt to Decrypt a Scramble IC (vr2): Computer Test vs the Scramble rating,
    reduced by the Decrypt utility. Success defeats the Scramble with NO tally increase.
    """
    tn = max(2, scramble_rating - decrypt_utility)
    roll = roll_dice(decker_pool, tn)
    return {"roll": roll, "tn": tn, "decrypted": roll["successes"] > 0}


def scramble_failure_consequence(
    *, variant: str, is_key: bool, scramble_rating: int = 6, decker_computer_skill: int = 6
) -> dict[str, Any]:
    """Consequence of a FAILED Decrypt against a Scramble IC (vr2_rules.md L487-495).

    - Poison: on a failed decrypt the IC makes a Poison Test -- it rolls its own rating dice
      against a target number equal to the decker's Computer skill. Only a SUCCESS destroys the
      protected data; if the Poison Test FAILS the data is safe (the poison is suppressed for
      this attempt). Key data lost this way is permanent and mission-critical.
    - Exploding: linked to a data bomb that detonates (data not wiped by the Scramble).
    """
    if variant not in {"exploding", "poison"}:
        raise ValueError(f"Unsupported Scramble variant: {variant!r}")
    if variant == "poison":
        poison_tn = max(2, decker_computer_skill)
        poison_roll = roll_dice(scramble_rating, poison_tn)
        destroyed = poison_roll["successes"] > 0
        if not destroyed:
            return {
                "data_destroyed": False,
                "key_data_lost": False,
                "poison_roll": poison_roll,
                "poison_tn": poison_tn,
                "message": (
                    "Decrypt failed, but the Poison Scramble's test missed (IC "
                    f"{scramble_rating}d6 vs TN {poison_tn} = your Computer skill) -- "
                    "the protected data survives. Try the decrypt again."
                ),
            }
        return {
            "data_destroyed": True,
            "key_data_lost": bool(is_key),
            "poison_roll": poison_roll,
            "poison_tn": poison_tn,
            "message": (
                "KEY DATA DESTROYED -- the Poison Scramble's test succeeded (IC "
                f"{scramble_rating}d6 vs TN {poison_tn}) and wiped the protected file. "
                "It cannot be recovered."
                if is_key else
                "Protected data destroyed -- the Poison Scramble's test succeeded (IC "
                f"{scramble_rating}d6 vs TN {poison_tn}) on the failed decrypt."
            ),
        }
    return {
        "data_destroyed": False,
        "detonate_data_bomb": True,
        "message": "Exploding Scramble triggered -- its linked data bomb detonates.",
    }


# -- Enemy decker (security decker antagonist) ---------------------------------

# Auto-generation rubric keyed to the host security code. Stats are tier CAPS; the
# actual values also scale with security_value but never exceed the tier (so a Blue
# host never fields a Computer-12 decker).
#
# An enemy decker hunts you the only way a decker can: LOCATE you (Locate Decker /
# Scanner -- Trace is host IC, not a decker tool), then CRASH YOUR ICON in cybercombat.
# Faithful to vr2_rules "Offensive Utilities": a plain Attack does icon-only damage
# (crash -> dump shock). Permanent deck damage / lethality come ONLY from the lethal
# decker programs -- Black Hammer (Physical) / Killjoy (Stun) -- which "function like
# Black IC but from a decker" and reduce MPCP on an icon crash at DOUBLE the program
# rating. Per the rules those are carried only on deadly-force systems (Red/Black).
#   intent: dump = crash the icon (Attack); kill = lethal biofeedback (Black Hammer/Killjoy).
#   extra: the non-Attack offensive programs this decker carries (every decker has Attack).
#     Hog (crash running programs), Poison/Restrict/Reveal (decker cripplers -> Bod/Evasion/
#     Masking), Black Hammer (lethal Physical) / Killjoy (lethal Stun, deadly-force hosts only).
_ENEMY_DECKER_TIERS: dict[str, dict[str, Any]] = {
    # Per-instance generation rolls each stat/program as a CENTERED 1D3-style spread
    # (center-1 .. center+1) clamped to [1, cap]. Centers are TIER-ONLY -- the host's numeric
    # security value never scales a decker (a skilled decker can watch a soft host). SURVIVE is
    # additive up the tiers: Armor (Green) -> +Shield (Orange) -> +Medic (Red/Black). ``kill`` /
    # ``survive`` map a utility key -> its center rating; all program ratings live in the returned
    # ``utilities`` dict. ``hardening`` / ``bravery`` use explicit (min, max) bands (NOT centered).
    # ri/quickness/intelligence scale the enemy's Matrix INITIATIVE with host difficulty; RI is
    # additionally clamped to MPCP/4 (vr2). Black is in a league of its own (Int center 8, RI 3).
    "Blue":   {"mpcp": 4,  "skill": 4,  "persona": 3, "attack": 3,  "intent": "dump",
               "ri": 0, "quickness": 3, "intelligence": 4, "hardening": (0, 0), "bravery": (0, 1),
               "kill": {}, "survive": {}},
    "Green":  {"mpcp": 6,  "skill": 5,  "persona": 4, "attack": 5,  "intent": "dump",
               "ri": 1, "quickness": 4, "intelligence": 5, "hardening": (0, 0), "bravery": (0, 2),
               "kill": {"hog": 4}, "survive": {"armor": 3}},
    "Orange": {"mpcp": 7,  "skill": 6,  "persona": 5, "attack": 6,  "intent": "dump",
               "ri": 1, "quickness": 5, "intelligence": 6, "hardening": (0, 0), "bravery": (1, 2),
               "kill": {"hog": 5, "reveal": 5}, "survive": {"armor": 4, "shield": 4}},
    "Red":    {"mpcp": 9,  "skill": 8,  "persona": 6, "attack": 8,  "intent": "dump",
               "ri": 2, "quickness": 6, "intelligence": 6, "hardening": (0, 1), "bravery": (1, 3),
               "kill": {"hog": 6, "reveal": 6, "poison": 6, "black_hammer": 4},
               "survive": {"armor": 5, "shield": 5, "medic": 4, "restore": 4}},
    "Black":  {"mpcp": 12, "skill": 10, "persona": 7, "attack": 10, "intent": "kill",
               "ri": 3, "quickness": 6, "intelligence": 8, "hardening": (1, 2), "bravery": (2, 3),
               "kill": {"hog": 7, "reveal": 7, "poison": 7, "restrict": 7,
                        "black_hammer": 5, "killjoy": 5},
               "survive": {"armor": 6, "shield": 6, "medic": 5, "restore": 5}},
}

_MPCP_MAX = 12  # canonical top-end deck -- a Black roll of 13 folds to 12

# Utility key -> display name for the offensive ``programs`` list (Attack is always first).
_ENEMY_KILL_DISPLAY = {
    "hog": "Hog", "reveal": "Reveal", "poison": "Poison", "restrict": "Restrict",
    "black_hammer": "Black Hammer", "killjoy": "Killjoy",
}

# Count-gated probabilistic spawn: after ANY sheaf step fires, the host rolls ``chance`` to
# dispatch a security decker, capped per run (``cap`` = (min, max), rolled once into
# state["enemy_decker_cap"]). This is the SOLE enemy-decker spawner (no hand-authored path).
_ENEMY_DECKER_SPAWN: dict[str, dict[str, Any]] = {
    "Blue":   {"chance": 0.05, "cap": (1, 1)},
    "Green":  {"chance": 0.10, "cap": (1, 1)},
    "Orange": {"chance": 0.15, "cap": (1, 2)},
    "Red":    {"chance": 0.20, "cap": (1, 2)},
    "Black":  {"chance": 0.25, "cap": (2, 3)},
}

# Cumulative net successes the enemy must score before it has pinpointed the PC.
# DEPRECATED: locate is now a single opposed test (see _locate_opposed) -- any net success
# pinpoints the PC, else the enemy retries next pass. Kept only so any stale reference resolves.
ENEMY_LOCATE_THRESHOLD = 1

# Security-decker street handles, revealed to the PC only once its icon is Analyzed / Scanned
# (until then it shows the generic "Security Decker" identifier). Placeholder pool -- the full
# lore/handle-generator discussion is deferred (see the matrix-run roadmap #4). Kept deliberately
# ASCII-only; a per-run counter disambiguates when the same handle is rolled twice.
_ENEMY_DECKER_HANDLES = (
    "Redline", "Nyx", "Cutter", "Havoc", "Cipher", "Wraith", "Static", "Vantage",
    "Halcyon", "Rook", "Payload", "Torque", "Ferrous", "Mote", "Praxis", "Glitch",
    "Onyx", "Sable", "Vector", "Quorum", "Kestrel", "Dross", "Ember", "Fathom",
    "Cinder", "Talon", "Vellum", "Nought", "Grackle", "Hollow", "Ironsight", "Jitter",
    "Kraken", "Lattice", "Marrow", "Nadir", "Obelisk", "Pallor", "Ratchet", "Snarl",
    "Tremor", "Umbra", "Vagrant", "Warden", "Xenon", "Yarrow", "Zephyr", "Ashfall",
    "Bishop", "Crypt", "Dredge", "Effigy", "Fracture", "Gambit", "Husk", "Ivory",
    "Junction", "Knell", "Lumen", "Mordant", "Needle", "Ordnance", "Pyre", "Quill",
)


def pick_enemy_handle(exclude: set[str] | None = None) -> str:
    """Return a random security-decker street handle from ``_ENEMY_DECKER_HANDLES`` (revealed only
    after the PC Analyzes/Scans the icon). ``exclude`` is a set of handles that are OFF-LIMITS --
    every player-character name plus any handle already taken by another enemy this run -- so an
    NPC never shares a name with a player (case-insensitive). If the whole pool is excluded, fall
    back to a synthesized unique tag rather than reusing a forbidden name. Placeholder generator;
    see roadmap #4."""
    banned = {str(x).strip().lower() for x in (exclude or ()) if str(x).strip()}
    pool = [h for h in _ENEMY_DECKER_HANDLES if h.lower() not in banned]
    if pool:
        return random.choice(pool)
    # Everything is spoken for -- synthesize a handle that is still not on the banned list.
    for _ in range(50):
        candidate = f"Decker-{random.randint(1000, 9999)}"
        if candidate.lower() not in banned:
            return candidate
    return "Decker-0000"


def generate_enemy_decker(
    security_code: str,
    security_value: int,
    *,
    name: str | None = None,
    exclude_handles: set[str] | None = None,
) -> dict[str, Any]:
    """Auto-generate a security decker scaled to the host TIER (vr2-flavoured rubric).

    Every stat and program is rolled per-instance as a centered 1D3-style spread
    (``center - 1 .. center + 1``) clamped to ``[1, cap]`` -- so two same-tier deckers differ.
    The bands are TIER-ONLY: the host's numeric ``security_value`` never scales MPCP/skill/programs
    (it informs only the display name). Program ratings cap at MPCP; the lethal programs
    (Black Hammer / Killjoy) additionally cap at ``ceil(Computer skill / 2)``; MPCP caps at 12.
    Returns a decker dict ready to drop into run state; every dispatched decker is generated
    programmatically (there is no hand-authored path). Spawns are automatic (see the run engine).
    """
    tier = _ENEMY_DECKER_TIERS.get(security_code, _ENEMY_DECKER_TIERS["Green"])

    def _band(center: int, cap: int = 99) -> int:
        """Centered 1D3-style roll, floored at 1 and capped at ``cap``."""
        return max(1, min(cap, center + random.randint(-1, 1)))

    mpcp = _band(tier["mpcp"], _MPCP_MAX)
    skill = _band(tier["skill"])
    persona = _band(tier["persona"])
    sleaze = _band(tier["persona"])       # Sleaze band == persona band, rolled independently
    scanner = _band(tier["persona"])      # Scanner band == persona band (locate other deckers)
    cloak = _band(tier["persona"])        # Cloak band == persona band (evade the PC during maneuvers)
    lock_on = _band(tier["persona"])      # Lock-On band == persona band (hold a sensor lock when the PC evades)
    attack = _band(tier["attack"], mpcp)
    lethal_cap = (skill + 1) // 2         # ceil(Computer skill / 2): the RAW lethal-rating cap
    df = detection_factor(persona, sleaze)  # the PC must beat this to find THEM

    # Roll every carried program into the utilities dict, each clamped to <= MPCP (the lethal
    # programs additionally to <= ceil(skill/2)). SURVIVE (armor/shield/medic) rides alongside.
    utilities: dict[str, int] = {"attack": attack, "sleaze": sleaze, "scanner": scanner,
                                "cloak": cloak, "lock_on": lock_on}
    for key, center in tier["kill"].items():
        cap = lethal_cap if key in ("black_hammer", "killjoy") else mpcp
        utilities[key] = _band(center, cap)
    for key, center in tier["survive"].items():
        utilities[key] = _band(center, mpcp)

    programs = ["Attack"] + [_ENEMY_KILL_DISPLAY[k] for k in tier["kill"] if k in _ENEMY_KILL_DISPLAY]
    # Default lethal program (used by 'kill' intent): Black Hammer if carried, else Killjoy.
    lethal = "Black Hammer" if "black_hammer" in tier["kill"] else (
        "Killjoy" if "killjoy" in tier["kill"] else None)
    lethal_rating = utilities.get("black_hammer") or utilities.get("killjoy") or 0

    # Reaction stats + Response Increase scale the enemy's initiative with host difficulty (all
    # centered per-instance). RI respects MPCP/4 (vr2). Hardening / bravery use explicit bands.
    # Deck mode runs hot more often at higher tiers; a reality filter appears with a tier chance.
    intelligence = _band(tier["intelligence"])
    quickness = _band(tier["quickness"])
    response_increase = max(0, min(mpcp // 4, tier["ri"] + random.randint(-1, 1)))
    hardening = random.randint(*tier["hardening"])
    bravery = random.randint(*tier["bravery"])   # flee resistance (see the run engine's nerve check)
    hot_chance = {"Blue": 0.6, "Green": 0.7, "Orange": 0.8, "Red": 0.9, "Black": 1.0}.get(security_code, 0.8)
    deck_mode = "hot" if random.random() < hot_chance else "cool"
    rf_chance = {"Blue": 0.0, "Green": 0.1, "Orange": 0.25, "Red": 0.5, "Black": 0.75}.get(security_code, 0.25)
    reality_filter = random.random() < rf_chance
    return {
        "name": name or "Security Decker",
        "handle": pick_enemy_handle(exclude_handles),
        "name_revealed": False,
        "mpcp": mpcp,
        "bod": persona, "evasion": persona, "masking": persona, "sensor": persona,
        "computer_skill": skill,
        "intelligence": intelligence,
        "quickness": quickness,
        "response_increase": response_increase,
        "deck_mode": deck_mode,
        "reality_filter": reality_filter,
        "utilities": utilities,
        "programs": programs,
        "intent": tier["intent"],
        "lethal_program": lethal,
        "lethal_rating": lethal_rating,
        "tier": security_code,
        "detection_factor": df,
        "hardening": hardening,
        "bravery": bravery,
        "condition_monitor": {"persona_boxes": 0, "stun_boxes": 0, "physical_boxes": 0, "mpcp_damage": 0},
        "program_damage": {},          # per-enemy Shield/Medic wear (mirrors the PC's slot)
        "nerve_checks_done": [],       # persona-box thresholds already nerve-checked (7/8/9)
        "locate_progress": 0,
        "located": False,
        "revealed": False,
        "status": "active",
    }


def _locate_opposed(
    *,
    locator_dice: int,
    target_hidden_rating: int,
    locator_scanner: int,
    target_evasion_dice: int,
    locator_sensor: int,
    player_is_locator: bool,
) -> dict[str, Any]:
    """Shared opposed locate resolution used by BOTH directions (the PC locating an enemy decker and
    an enemy decker locating the PC). The locator rolls its locate dice vs the target's hidden rating
    (the PC's Detection Factor, or an enemy's full Masking + Sleaze) minus the locator's Scanner
    utility; the target resists with Evasion dice vs the locator's Sensor. A nonzero tie favors
    the player: it locates when the PC is the locator and blocks location when the PC is the target.
    Rolls the locator first so a scripted die sequence is consumed locator-then-target."""
    target_tn = max(2, target_hidden_rating - locator_scanner)
    locator_roll = roll_dice(locator_dice, target_tn)
    target_roll = roll_dice(target_evasion_dice, locator_sensor)
    raw_net = locator_roll["successes"] - target_roll["successes"]
    nonzero_tie = raw_net == 0 and locator_roll["successes"] > 0
    located = raw_net > 0 or (nonzero_tie and player_is_locator)
    return {
        "locator_roll": locator_roll,
        "target_roll": target_roll,
        "target_tn": target_tn,
        "net_successes": max(0, raw_net),
        "located": located,
    }


def enemy_locate_test(
    *,
    computer_skill: int,
    scanner_rating: int,
    sensor_rating: int,
    pc_detection_factor: int,
    pc_evasion: int,
) -> dict[str, Any]:
    """One enemy attempt to locate the PC (vr2: find the intruder's icon). Mirror of
    pc_locate_decker_test via the shared _locate_opposed: the enemy rolls Computer dice vs
    (PC Detection Factor - Scanner utility); the PC resists with Evasion dice vs the enemy's Sensor.
    Any net enemy success pinpoints the PC on THIS attempt -- no cumulative threshold; a miss simply
    means the enemy tries again next pass.
    """
    r = _locate_opposed(
        locator_dice=computer_skill,
        target_hidden_rating=pc_detection_factor,
        locator_scanner=scanner_rating,
        target_evasion_dice=pc_evasion,
        locator_sensor=sensor_rating,
        player_is_locator=False,
    )
    return {
        "enemy_roll": r["locator_roll"],
        "pc_roll": r["target_roll"],
        "enemy_tn": r["target_tn"],
        "net_successes": r["net_successes"],
        "located": r["located"],
    }


def pc_locate_decker_test(
    *,
    sensor_rating: int,
    scanner_rating: int,
    enemy_mask_sleaze: int,
    enemy_evasion: int,
) -> dict[str, Any]:
    """One PC attempt to locate a hidden enemy decker -- the mirror image of enemy_locate_test, via
    the same shared _locate_opposed.

    The PC rolls Sensor dice vs (enemy full Masking + Sleaze - PC Scanner utility); the enemy resists
    with Evasion dice vs the PC's Sensor. Any net PC success pinpoints the enemy (it becomes revealed
    and the PC can Strike Back). The TN is the enemy's FULL Masking + Sleaze (vr2 L1880: Masking plus
    the target's Sleaze rating) -- NOT the halved Detection Factor a decker computes for its own
    persona -- so a sleazier security decker is even harder to find.
    """
    r = _locate_opposed(
        locator_dice=sensor_rating,
        target_hidden_rating=enemy_mask_sleaze,
        locator_scanner=scanner_rating,
        target_evasion_dice=enemy_evasion,
        locator_sensor=sensor_rating,
        player_is_locator=True,
    )
    return {
        "pc_roll": r["locator_roll"],
        "enemy_roll": r["target_roll"],
        "target_tn": r["target_tn"],
        "net_successes": r["net_successes"],
        "located": r["located"],
    }


def maneuver_test(
    *,
    maneuvering_evasion_dice: int,
    maneuvering_evasion_rating: int,
    opposing_sensor_dice: int,
    opposing_sensor_rating: int,
    cloak: int = 0,
    lock_on: int = 0,
) -> dict[str, Any]:
    """SR2/VR2 combat-maneuver opposed test (vr2 L1982) -- shared by Evade Detection,
    Parry Attack and Position Attack.

    The maneuvering icon makes an Evasion Test: Evasion dice vs the opposing icon's Sensor
    Rating (a Cloak utility lowers that TN). The opposing icon makes a Sensor Test: Sensor
    dice vs the maneuvering icon's Evasion Rating (a Lock-On utility lowers that TN). The
    maneuvering icon must roll STRICTLY more successes to succeed; the net successes
    (maneuvering - opposing) are the maneuver's magnitude. A tie or an opposing win is a
    failure (net_successes 0).

    Dice/rating source is the caller's responsibility so the same engine serves every actor:
      - decker (PC or enemy): Evasion dice/Rating = Evasion attribute; Sensor dice/Rating =
        Sensor attribute.
      - IC: rolls Security Value dice for BOTH tests, and uses its rating as BOTH its Evasion
        Rating and its Sensor Rating (the TN an opponent rolls against it).
    Cloak lowers the maneuvering icon's Evasion TN; Lock-On lowers the opposing icon's Sensor
    TN. Both default to 0 (the actor carries neither); IC never carry them.
    """
    maneuvering_tn = max(2, opposing_sensor_rating - cloak)
    opposing_tn = max(2, maneuvering_evasion_rating - lock_on)
    maneuvering_roll = roll_dice(maneuvering_evasion_dice, maneuvering_tn)
    opposing_roll = roll_dice(opposing_sensor_dice, opposing_tn)
    net = maneuvering_roll["successes"] - opposing_roll["successes"]
    return {
        "maneuvering_roll": maneuvering_roll,
        "opposing_roll": opposing_roll,
        "maneuvering_tn": maneuvering_tn,
        "opposing_tn": opposing_tn,
        "net_successes": max(0, net),
        "success": net > 0,
    }


def escalate_enemy_intent(base_intent: str, *, security_tally: int, threshold: int = 12) -> str:
    """A relentless security decker turns lethal as the alarm mounts (vr2 flavour).

    Once the tally is high a 'dump' decker (out to crash your icon) pushes to 'kill'.
    Black-tier deckers already start at 'kill'.
    """
    if security_tally >= threshold and base_intent == "dump":
        return "kill"
    return base_intent


def hog_attack(
    *,
    attacker_pool: int,
    security_code: str,
    target_status: str,
    hog_rating: int,
    mpcp_rating: int,
    hardening: int = 0,
    tn_modifier: int = 0,
) -> dict[str, Any]:
    """Hog virus weapon (vr2): a cybercombat attack that, on a hit, makes the target roll
    MPCP vs the Hog rating; the attacker's net successes // 2 reduce the target's highest
    running program (repeats each turn until that program crashes). ``tn_modifier`` raises the
    attacker's to-hit TN (e.g. the attacker's own wound penalty)."""
    attack_tn = max(2, COMBAT_TN[security_code][target_status] + tn_modifier)
    attack_roll = roll_dice(attacker_pool, attack_tn)
    resist_roll = roll_dice(mpcp_rating, max(2, hog_rating - hardening))
    net = max(0, attack_roll["successes"] - resist_roll["successes"])
    return {"attack_roll": attack_roll, "resist_roll": resist_roll,
            "net": net, "reduction": net // 2}


def hog_purge_test(
    *,
    computer_skill: int,
    hog_rating: int,
    infected_program_rating: int,
    hardening: int = 0,
) -> dict[str, Any]:
    """Purge a Hog virus (vr2 line 1548): Computer Test, TN = (Hog rating - Hardening) +
    the infected program's ORIGINAL rating. A single success wipes both the Hog and the
    infected program from active memory (reload the program afterward via Swap Memory)."""
    tn = max(2, (hog_rating - hardening) + infected_program_rating)
    roll = roll_dice(computer_skill, tn)
    return {"roll": roll, "tn": tn, "purged": roll["successes"] > 0}
