"""Lifestyle upkeep engine (SR2 p.245).

Rent is charged lazily off the campaign clock: whenever the world clock advances
(the admin Downtime control is the only thing that moves ticks), every PC with a
lifestyle is "settled" -- charged one month of upkeep for each full 30-tick month
that has elapsed since it was last settled.

If a runner can't make rent for a given month they are evicted one lifestyle tier
for that month (no charge), dropping until they reach Street (free) or can pay
again. A lifestyle bought outright (`lifestyle_permanent`) is never charged.
"""
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.character import (
    Character,
    LIFESTYLE_MONTHLY_COST,
    LIFESTYLE_PERMANENT_MONTHS,
    LIFESTYLE_UPKEEP_TICKS,
)


def monthly_cost(level: int | None) -> int:
    """Monthly upkeep for a lifestyle tier (0 for Street or an unset/out-of-range level)."""
    if level is None or not (0 <= level < len(LIFESTYLE_MONTHLY_COST)):
        return 0
    return LIFESTYLE_MONTHLY_COST[level]


def permanent_cost(level: int | None) -> int:
    """Up-front cost to buy a lifestyle tier outright (100 months of upkeep)."""
    return monthly_cost(level) * LIFESTYLE_PERMANENT_MONTHS


def settle_lifestyle(char: Character, current_tick: int) -> bool:
    """Charge any lifestyle upkeep owed up to ``current_tick``; mutate ``char`` in place.

    Returns True when the character was modified (so the caller can commit). Charges
    one month per full 30-tick period elapsed since ``lifestyle_paid_tick``; a month
    the PC cannot afford evicts them one tier instead (no charge that month).
    """
    if char.lifestyle_level is None:
        return False  # no lifestyle to maintain (NPCs, pre-chargen rows)

    # First time we see this PC: stamp "paid through now" so we never bill back-rent.
    if char.lifestyle_paid_tick is None:
        char.lifestyle_paid_tick = current_tick
        return True

    # A permanent lifestyle is never billed; just keep the stamp current.
    if char.lifestyle_permanent:
        if char.lifestyle_paid_tick < current_tick:
            char.lifestyle_paid_tick = current_tick
            return True
        return False

    elapsed = current_tick - char.lifestyle_paid_tick
    if elapsed < LIFESTYLE_UPKEEP_TICKS:
        return False

    periods = elapsed // LIFESTYLE_UPKEEP_TICKS
    for _ in range(periods):
        cost = monthly_cost(char.lifestyle_level)
        if cost <= 0:
            continue  # Street is free -- nothing to pay, no eviction possible
        if char.nuyen >= cost:
            char.nuyen -= cost
        else:
            # Can't make this month's rent: evicted one tier down (no charge this month).
            char.lifestyle_level = max(0, char.lifestyle_level - 1)
    char.lifestyle_paid_tick += periods * LIFESTYLE_UPKEEP_TICKS
    return True


async def settle_all_lifestyles(db: AsyncSession, current_tick: int) -> int:
    """Settle lifestyle upkeep for every character with a lifestyle; commit if anything changed.

    Returns the number of characters modified. Called when the campaign clock advances.
    """
    result = await db.execute(
        select(Character).where(Character.lifestyle_level.is_not(None))
    )
    changed = 0
    for char in result.scalars().all():
        if settle_lifestyle(char, current_tick):
            changed += 1
    if changed:
        await db.commit()
    return changed
