"""
Heat and faction standing calculator for completed runs.

Heat (0-10) represents the team's exposure after a run -- attention drawn from
corps, law enforcement, and the shadows.  It is a party-level value stored on
the AdventureLog and is computed deterministically from run parameters.

Heat scale:
  0        = Neutral   (baseline, no exposure)
  1-2      = Noticed   (low heat, half-life 3 days)
  3-4      = Flagged   (moderate, half-life 7 days)
  5-6      = Wanted    (high, half-life 14 days)
  7-8      = Hot       (very high, half-life 21 days)
  9-10     = Nova Hot  (extreme, half-life 30 days)

Faction ripple: a standing change with org X propagates (at reduced magnitude)
to X's documented allies and enemies.
"""
from __future__ import annotations
import math
from datetime import date

# -- Heat inputs --------------------------------------------------------------

OUTCOME_HEAT: dict[str, int] = {
    "success":          2,
    "partial_success":  2,
    "failure":          1,   # failed run = lower profile
    "critical_failure": 3,   # something went very wrong publicly
    "abandoned":        1,
}

TAG_HEAT: dict[str, int] = {
    "witnesses":         1,
    "collateral_damage": 2,
    "public_scene":      2,
    "media_attention":   3,
    "casualties":        1,
    "wetwork":           1,
    "assassination":     1,
    "magic_use":         1,
    "vehicle_chase":     1,
    "data_theft":        0,
    "extraction":        0,
    "bribery":           0,
    "false_flag":        0,
}

ORG_TYPE_HEAT: dict[str, int] = {
    "megacorp":             1,
    "government":           1,
    "nation-state":         1,
    "political organization": 1,
    "security contractor":  0,
    "syndicate":            0,
    "corporation":          0,
    "gang":                 0,
    "fixer_network":        0,
    "cult":                 0,
    "other":                0,
}

# -- Threshold tables ---------------------------------------------------------

# (lo, hi, label) -- inclusive bounds
HEAT_THRESHOLDS: list[tuple[int, int, str]] = [
    (0,  0, "Neutral"),
    (1,  2, "Noticed"),
    (3,  4, "Flagged"),
    (5,  6, "Wanted"),
    (7,  8, "Hot"),
    (9, 10, "Nova Hot"),
]

# Half-life in days per heat tier (used for decay)
HEAT_HALF_LIVES: list[tuple[int, int, float]] = [
    (0,  0, float('inf')),  # Neutral never decays (already 0)
    (1,  2, 3.0),            # Noticed
    (3,  4, 7.0),            # Flagged
    (5,  6, 14.0),           # Wanted
    (7,  8, 21.0),           # Hot
    (9, 10, 30.0),           # Nova Hot
]

STANDING_TIERS: list[tuple[int, int, str]] = [
    (-10, -7, "hostile"),
    ( -6, -3, "unfriendly"),
    ( -2,  2, "neutral"),
    (  3,  6, "friendly"),
    (  7, 10, "allied"),
]

# -- Reputation tier tables ----------------------------------------------------
# Net rep = 20 + street_cred - notoriety, clamped 0-40.  20 = neutral baseline.

PC_REP_TIERS: list[tuple[int, int, str]] = [
    ( 0,  0, "Infamous"),
    ( 1,  1, "Pariah"),
    ( 2,  4, "Feared"),
    ( 5,  7, "Dangerous"),
    ( 8, 11, "Dirty"),
    (12, 15, "Shady"),
    (16, 19, "Questionable"),
    (20, 20, "Nobody"),
    (21, 23, "Tested"),
    (24, 26, "Proven"),
    (27, 30, "Seasoned"),
    (31, 33, "Dependable"),
    (34, 36, "Professional"),
    (37, 39, "Trusted"),
    (40, 40, "Legend"),
]

TEAM_REP_TIERS: list[tuple[int, int, str]] = [
    ( 0,  1, "Blacklisted"),
    ( 2,  4, "Feared"),
    ( 5,  7, "Dangerous"),
    ( 8, 11, "Dirty"),
    (12, 15, "Shady"),
    (16, 19, "Questionable"),
    (20, 20, "Unknown"),
    (21, 23, "Amateur"),
    (24, 26, "Proven"),
    (27, 30, "Experienced"),
    (31, 33, "Dependable"),
    (34, 36, "Professional"),
    (37, 39, "Trusted"),
]

PA_TIERS: list[tuple[int, int, str]] = [
    ( 0,  0, "Shadow"),
    ( 1,  3, "Seen"),
    ( 4,  7, "Recognized"),
    ( 8, 12, "In the Spotlight"),
    (13, 99, "Burned"),
]

# Half-life in days per PA tier -- media and public attention fades over time
PA_HALF_LIVES: list[tuple[int, int, float]] = [
    ( 0,  0, float('inf')),  # Shadow -- nothing to decay
    ( 1,  3, 7.0),            # Seen -- news cycle moves on quickly
    ( 4,  7, 14.0),           # Recognized
    ( 8, 12, 21.0),           # In the Spotlight
    (13, 99, 30.0),           # Burned -- hard to shake but fades eventually
]

# -- Ripple parameters --------------------------------------------------------

RIPPLE_FACTOR = 0.4   # fraction of original delta applied to adjacent orgs
RIPPLE_CAP    = 2     # maximum ripple magnitude in either direction

# Inactive PCs who are "lying low" decay heat/PA/standings twice as fast.
LYING_LOW_DECAY_ACCEL = 2.0


# -- Public API ---------------------------------------------------------------

def heat_label(heat: int) -> str:
    for lo, hi, label in HEAT_THRESHOLDS:
        if lo <= heat <= hi:
            return label
    return "Nova Hot"


def standing_label(standing: int) -> str:
    for lo, hi, label in STANDING_TIERS:
        if lo <= standing <= hi:
            return label
    return "neutral"


def pc_rep_label(net_rep: int) -> str:
    net_rep = max(0, min(40, net_rep))
    for lo, hi, label in PC_REP_TIERS:
        if lo <= net_rep <= hi:
            return label
    return "Nobody"


def team_rep_label(score: int) -> str:
    score = max(0, min(39, score))
    for lo, hi, label in TEAM_REP_TIERS:
        if lo <= score <= hi:
            return label
    return "Unknown"


def pa_label(pa: int) -> str:
    for lo, hi, label in PA_TIERS:
        if lo <= pa <= hi:
            return label
    return "Burned"


def _pa_half_life(pa: int) -> float:
    """Return the decay half-life in days for a given PA value."""
    for lo, hi, hl in PA_HALF_LIVES:
        if lo <= pa <= hi:
            return hl
    return 30.0


def decay_pa(pa: int, elapsed: int, accel: float = 1.0) -> float:
    """
    Return the decayed public awareness value (float).
    elapsed  : ticks since PA was last changed (use current_tick - pa_stamped_tick).
    accel > 1.0 compresses the half-life (faster decay, e.g. lying-low runners).
    """
    if pa <= 0 or elapsed <= 0:
        return max(0.0, float(pa))
    hl = _pa_half_life(pa) / max(accel, 1.0)
    if math.isinf(hl):
        return float(pa)
    return pa * math.exp(-math.log(2) * elapsed / hl)


def _half_life(heat: int) -> float:
    """Return the decay half-life in days for a given heat value."""
    for lo, hi, hl in HEAT_HALF_LIVES:
        if lo <= heat <= hi:
            return hl
    return 30.0


def decay_heat(heat: int, days_ago: int, accel: float = 1.0) -> float:
    """
    Return the decayed heat value (float).
    elapsed  : ticks since heat was last changed (use current_tick - heat_stamped_tick).
    accel > 1.0 compresses the half-life (faster decay, e.g. lying-low runners).
    """
    if heat <= 0 or days_ago <= 0:
        return max(0.0, float(heat))
    hl = _half_life(heat) / max(accel, 1.0)
    if math.isinf(hl):
        return float(heat)
    return heat * math.exp(-math.log(2) * days_ago / hl)


# Half-lives in days for org standings decay.
# Negative standings (hostility) fade faster; positive (loyalty) take 2x longer.
# Magnitude of standing drives tier -- both tables are keyed on abs(standing).
STANDING_HALF_LIVES_NEG: list[tuple[int, int, float]] = [
    (0,  0, float('inf')),  # neutral -- never decays
    (1,  3, 4.0),            # unfriendly low   (pos 6.0 / 1.5)
    (4,  6, 8.0),            # unfriendly high  (pos 12.0 / 1.5)
    (7,  9, 13.0),           # hostile low-mid  (pos 20.0 / 1.5)
    (10, 10, 19.0),          # hostile max      (pos 28.0 / 1.5)
]
STANDING_HALF_LIVES_POS: list[tuple[int, int, float]] = [
    (0,  0, float('inf')),
    (1,  3, 6.0),
    (4,  6, 12.0),
    (7,  9, 20.0),
    (10, 10, 28.0),
]


def _standing_half_life(standing: int) -> float:
    """Return the decay half-life for a standing value (uses abs magnitude)."""
    mag   = abs(standing)
    table = STANDING_HALF_LIVES_POS if standing > 0 else STANDING_HALF_LIVES_NEG
    for lo, hi, hl in table:
        if lo <= mag <= hi:
            return hl
    return 14.0


def decay_standing(standing: int, elapsed: int, accel: float = 1.0) -> float:
    """
    Return the effective standing (float) after exponential decay toward 0.
    elapsed  : ticks since standing was last changed.
    Positive standings decay toward 0 from above; negative from below.
    Neutral (0) is never modified.  Pass elapsed=0 to skip decay.
    accel > 1.0 compresses the half-life (faster decay, e.g. lying-low runners).
    """
    if standing == 0 or elapsed <= 0:
        return float(standing)
    hl = _standing_half_life(standing) / max(accel, 1.0)
    if math.isinf(hl):
        return float(standing)
    decayed = standing * math.exp(-math.log(2) * elapsed / hl)
    # preserve sign; clamp so magnitude never exceeds original
    if standing > 0:
        return max(0.0, decayed)
    return min(0.0, decayed)


def compute_heat(
    outcome: str | None,
    outcome_tags: list[str] | None,
    employer_tier: int | None = None,
    employer_org_type: str | None = None,
) -> int:
    """
    Compute a heat value (0-10) for a completed run.

    Parameters
    ----------
    outcome        : SR outcome string (success / partial_success / etc.)
    outcome_tags   : list of consequence tags from the log
    employer_tier  : org tier of the hiring party (1-6), if known
    employer_org_type : org_type string of the hiring party, if known
    """
    base = OUTCOME_HEAT.get(outcome or "", 2)
    tag_bonus = sum(TAG_HEAT.get(t, 0) for t in (outcome_tags or []))

    tier_bonus = 0
    if employer_tier:
        if employer_tier >= 6:
            tier_bonus = 3
        elif employer_tier >= 5:
            tier_bonus = 2
        elif employer_tier >= 3:
            tier_bonus = 1

    type_bonus = ORG_TYPE_HEAT.get(employer_org_type or "", 0)

    return min(10, max(0, base + tag_bonus + tier_bonus + type_bonus))


def compute_ripple(
    org_id: int,
    delta: int,
    org_map: dict[int, dict],
) -> list[dict]:
    """
    Given an org_id and a standing delta for some character, return proposed
    ripple changes to that org's allies and enemies.

    org_map : {org_id: {"name": str, "ally_ids": [...], "enemy_ids": [...]}}

    Returns a list of dicts compatible with the ChangeItem schema:
        {type, character_id, character_name, delta, org_id, org_name, reason, ripple}
    The caller must fill in character_id / character_name before returning to client.
    """
    org = org_map.get(org_id)
    if not org or delta == 0:
        return []

    ripple_mag = min(RIPPLE_CAP, max(1, round(abs(delta) * RIPPLE_FACTOR)))
    items = []

    for ally_id in (org.get("ally_ids") or []):
        ally = org_map.get(ally_id)
        items.append({
            "type":     "org_standing",
            "delta":    ripple_mag if delta > 0 else -ripple_mag,
            "org_id":   ally_id,
            "org_name": ally["name"] if ally else str(ally_id),
            "reason":   (
                f"Faction ripple: {org['name']} ally "
                f"(standing changed by {delta:+})"
            ),
            "ripple":   True,
        })

    for enemy_id in (org.get("enemy_ids") or []):
        enemy = org_map.get(enemy_id)
        items.append({
            "type":     "org_standing",
            "delta":    -ripple_mag if delta > 0 else ripple_mag,
            "org_id":   enemy_id,
            "org_name": enemy["name"] if enemy else str(enemy_id),
            "reason":   (
                f"Faction ripple: {org['name']} rival "
                f"(standing changed by {delta:+})"
            ),
            "ripple":   True,
        })

    return items
