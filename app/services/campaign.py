"""Shared campaign utilities."""
from sqlalchemy import func, select, update
from sqlalchemy.dialects.sqlite import insert as sqlite_insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.adventure_log import AdventureLog
from app.models.campaign import CampaignState


async def _legacy_tick_total(db: AsyncSession) -> int:
    """Pre-clock campaign total: the sum of every log's tick_count.

    Used once to seed the persistent clock so the timeline stays continuous for
    campaigns that predate the CampaignState row (older decay stamps are relative
    to this running total).
    """
    result = await db.execute(select(func.sum(AdventureLog.tick_count)))
    return result.scalar() or 0


async def get_campaign_state(db: AsyncSession) -> CampaignState:
    """Return the single CampaignState row, creating + seeding it if absent."""
    legacy_total = await _legacy_tick_total(db)
    result = await db.execute(
        sqlite_insert(CampaignState)
        .values(id=1, current_tick=legacy_total)
        .on_conflict_do_nothing(index_elements=[CampaignState.id])
    )
    if result.rowcount == 1:
        await db.commit()
    state = await db.get(CampaignState, 1)
    if state is None:
        raise RuntimeError("campaign_state singleton was not created")
    return state


async def current_tick(db: AsyncSession) -> int:
    """Return the absolute campaign clock (in ticks; 1 tick = 1 day).

    Only the Downtime control advances this; logging a run no longer moves time.
    """
    state = await get_campaign_state(db)
    return state.current_tick


async def advance_clock(db: AsyncSession, days: int) -> int:
    """Advance the campaign clock by `days` ticks and return the new total."""
    await get_campaign_state(db)
    result = await db.execute(
        update(CampaignState)
        .where(CampaignState.id == 1)
        .values(current_tick=CampaignState.current_tick + max(0, int(days)))
        .returning(CampaignState.current_tick)
    )
    new_tick = result.scalar_one_or_none()
    if new_tick is None:
        await db.rollback()
        raise RuntimeError("campaign_state singleton disappeared during clock advance")
    await db.commit()
    return new_tick
