from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.auth.dependencies import get_admin_token
from app.schemas.campaign import ClockRead, AdvanceClockRequest, AdvanceClockResult
from app.services.campaign import current_tick, advance_clock

router = APIRouter()


@router.get("/clock", response_model=ClockRead)
async def get_clock(db: AsyncSession = Depends(get_db)):
    """Return the current campaign clock (absolute tick total)."""
    return ClockRead(current_tick=await current_tick(db))


@router.post("/advance", response_model=AdvanceClockResult)
async def advance_campaign_clock(
    body: AdvanceClockRequest,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    """Advance the campaign clock by N days (admin only).

    This is the single control that moves world time forward -- heat, public
    awareness, and org-standing decay are all computed from the elapsed ticks.
    """
    new_tick = await advance_clock(db, body.days)
    return AdvanceClockResult(current_tick=new_tick, days_advanced=body.days)
