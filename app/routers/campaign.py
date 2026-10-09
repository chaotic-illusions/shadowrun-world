from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.auth.dependencies import get_admin_token
from app.schemas.campaign import ClockRead, AdvanceClockRequest, AdvanceClockResult, TeamKarma
from app.services.campaign import current_tick, advance_clock, get_campaign_state, set_team_karma

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

    This is the single control that moves world time forward -- heat and public
    awareness decay are computed from the elapsed ticks.
    """
    new_tick = await advance_clock(db, body.days)
    return AdvanceClockResult(current_tick=new_tick, days_advanced=body.days)


@router.get("/team-karma", response_model=TeamKarma)
async def get_team_karma(db: AsyncSession = Depends(get_db)):
    """Return the team's Karma Pool (SR2 p.191)."""
    return TeamKarma(team_karma=(await get_campaign_state(db)).team_karma)


@router.put("/team-karma", response_model=TeamKarma)
async def put_team_karma(
    body: TeamKarma,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    """Set the team's Karma Pool (admin only)."""
    return TeamKarma(team_karma=await set_team_karma(db, body.team_karma))
