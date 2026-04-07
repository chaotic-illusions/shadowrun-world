"""Shared campaign utilities."""
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.adventure_log import AdventureLog


async def current_tick(db: AsyncSession) -> int:
    """Return the global campaign tick total (sum of all log tick_counts)."""
    result = await db.execute(select(func.sum(AdventureLog.tick_count)))
    return result.scalar() or 0
