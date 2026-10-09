from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_or_404, apply_update
from app.models.character import Character
from app.models.organization import Organization
from app.models.reputation import Reputation, OrgStanding
from app.schemas.reputation import (
    ReputationCreate, ReputationUpdate, ReputationRead,
    OrgStandingCreate, OrgStandingUpdate, OrgStandingRead,
)
from app.services.campaign import current_tick
from app.services.heat_calculator import current_heat, current_pa
from app.auth.dependencies import get_admin_token, get_any_token

router = APIRouter()


def _is_privileged_view(ctx: dict) -> bool:
    """True only for a real admin NOT previewing runner view -- the full-data audience."""
    return bool(ctx.get("is_admin")) and not ctx.get("view_as_player")


def _inactive_npc_ids_query():
    return select(Character.id).where(
        Character.is_pc == False,  # noqa: E712
        Character.is_active == False,  # noqa: E712
    )


# --- Reputation (Street Cred / Notoriety / Public Awareness) ---

@router.get("/", response_model=list[ReputationRead])
async def list_reputations(
    character_id: int | None = Query(None),
    ctx: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    q = select(Reputation, Character.is_active).join(Character, Character.id == Reputation.character_id)
    if character_id is not None:
        q = q.where(Reputation.character_id == character_id)
    privileged = _is_privileged_view(ctx)
    if not privileged:
        # Inactive NPCs are GM-concealed.
        q = q.where(Reputation.character_id.not_in(_inactive_npc_ids_query()))
    result = await db.execute(q)
    tick = await current_tick(db)
    rows = []
    # Heat and PA are reported as they stand now (decayed), so an editor that saves
    # them back unchanged doesn't resurrect the pre-decay value.
    for rep, active in result.all():
        row = ReputationRead.model_validate(rep).model_dump()
        row["heat"] = current_heat(rep.heat, rep.heat_stamped_tick, tick, active)
        row["public_awareness"] = current_pa(rep.public_awareness, rep.pa_stamped_tick, tick, active)
        rows.append(row)
    if not privileged:
        for row in rows:
            row["notes"] = None
    return rows


@router.post("/", response_model=ReputationRead, status_code=201)
async def create_reputation(
    body: ReputationCreate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    result = await db.execute(
        select(Reputation).where(Reputation.character_id == body.character_id)
    )
    if result.scalars().first():
        raise HTTPException(status_code=409, detail="Reputation record already exists for this character")
    rep = Reputation(**body.model_dump())
    db.add(rep)
    await db.commit()
    await db.refresh(rep)
    return rep


@router.patch("/{rep_id}", response_model=ReputationRead)
async def update_reputation(
    rep_id: int,
    body: ReputationUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    rep = await get_or_404(db, Reputation, rep_id)
    tick = await current_tick(db)
    active = await db.scalar(select(Character.is_active).where(Character.id == rep.character_id))
    # A heat/PA equal to its current decayed value is an unchanged field echoed back by
    # the editor -- leave it decaying instead of re-stamping the stored value.
    skip = set()
    if body.heat == current_heat(rep.heat, rep.heat_stamped_tick, tick, active):
        skip.add("heat")
    if body.public_awareness == current_pa(rep.public_awareness, rep.pa_stamped_tick, tick, active):
        skip.add("public_awareness")
    # apply_update without committing -- we need to stamp ticks first
    await apply_update(db, rep, body, exclude=skip, commit=False)

    if body.public_awareness is not None and "public_awareness" not in skip and body.pa_updated_at is None:
        rep.pa_updated_at = date.today()
        rep.pa_stamped_tick = tick
    if body.heat is not None and "heat" not in skip and body.heat_updated_at is None:
        rep.heat_updated_at = date.today()
        rep.heat_stamped_tick = tick

    await db.commit()
    await db.refresh(rep)
    return rep


@router.delete("/{rep_id}", status_code=204)
async def delete_reputation(
    rep_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    rep = await get_or_404(db, Reputation, rep_id)
    await db.delete(rep)
    await db.commit()


# --- Org Standings ---

@router.get("/standings", response_model=list[OrgStandingRead])
async def list_org_standings(
    character_id: int | None = Query(None),
    organization_id: int | None = Query(None),
    ctx: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    q = select(OrgStanding)
    if character_id is not None:
        q = q.where(OrgStanding.character_id == character_id)
    if organization_id is not None:
        q = q.where(OrgStanding.organization_id == organization_id)
    privileged = _is_privileged_view(ctx)
    if not privileged:
        # Standings toward inactive orgs, or held by inactive NPCs, would reveal GM-concealed rows.
        q = q.where(
            OrgStanding.organization_id.in_(select(Organization.id).where(Organization.is_active == True)),  # noqa: E712
            OrgStanding.character_id.not_in(_inactive_npc_ids_query()),
        )
    result = await db.execute(q)
    rows = [OrgStandingRead.model_validate(r).model_dump() for r in result.scalars().all()]
    if not privileged:
        for row in rows:
            row["notes"] = None
    return rows


@router.post("/standings", response_model=OrgStandingRead, status_code=201)
async def create_org_standing(
    body: OrgStandingCreate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    result = await db.execute(
        select(OrgStanding).where(
            OrgStanding.character_id == body.character_id,
            OrgStanding.organization_id == body.organization_id,
        )
    )
    if result.scalars().first():
        raise HTTPException(status_code=409, detail="Standing already exists for this character/org pair")
    standing = OrgStanding(**body.model_dump())
    db.add(standing)
    await db.commit()
    await db.refresh(standing)
    return standing


@router.patch("/standings/{standing_id}", response_model=OrgStandingRead)
async def update_org_standing(
    standing_id: int,
    body: OrgStandingUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    standing = await get_or_404(db, OrgStanding, standing_id)
    await apply_update(db, standing, body, commit=False)

    if body.standing is not None:
        standing.standings_updated_at = date.today()

    await db.commit()
    await db.refresh(standing)
    return standing


@router.delete("/standings/{standing_id}", status_code=204)
async def delete_org_standing(
    standing_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    standing = await get_or_404(db, OrgStanding, standing_id)
    await db.delete(standing)
    await db.commit()


# --- Admin Utilities ---

@router.post("/reset-pc-data", status_code=200)
async def reset_all_pc_data(
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    """Reset all PC heat, reputation, and org standings to baseline (for testing)."""
    result = await db.execute(
        select(Character.id).where(Character.is_pc == True)  # noqa: E712
    )
    pc_ids = [row[0] for row in result.all()]

    if pc_ids:
        rep_result = await db.execute(
            select(Reputation).where(Reputation.character_id.in_(pc_ids))
        )
        for rep in rep_result.scalars().all():
            rep.street_cred = 0
            rep.notoriety = 0
            rep.public_awareness = 0
            rep.pa_updated_at = None
            rep.heat = 0
            rep.heat_updated_at = None

        standing_result = await db.execute(
            select(OrgStanding).where(OrgStanding.character_id.in_(pc_ids))
        )
        for standing in standing_result.scalars().all():
            await db.delete(standing)

    await db.commit()
    return {"reset": len(pc_ids), "message": f"Reset reputation data for {len(pc_ids)} PCs"}
