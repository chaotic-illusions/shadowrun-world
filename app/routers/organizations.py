from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, update as sql_update
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_or_404, apply_update
from app.models.organization import Organization
from app.models.character import Character
from app.models.contact import Contact
from app.models.location import Location
from app.schemas.organization import OrganizationCreate, OrganizationUpdate, OrganizationRead, OrganizationSummary, LtgSecurityUpdate
from app.auth.dependencies import get_admin_token

router = APIRouter()


@router.get("/", response_model=list[OrganizationRead])
async def list_organizations(
    org_type: str | None = Query(None),
    is_active: bool | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    q = select(Organization)
    if org_type:
        q = q.where(Organization.org_type == org_type)
    if is_active is not None:
        q = q.where(Organization.is_active == is_active)
    result = await db.execute(q.order_by(Organization.tier.desc(), Organization.name))
    return result.scalars().all()


@router.post("/", response_model=OrganizationRead, status_code=201)
async def create_organization(
    body: OrganizationCreate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    org = Organization(**body.model_dump())
    db.add(org)
    await db.commit()
    await db.refresh(org)
    return org


@router.get("/{org_id}", response_model=OrganizationRead)
async def get_organization(org_id: int, db: AsyncSession = Depends(get_db)):
    return await get_or_404(db, Organization, org_id)


@router.patch("/{org_id}", response_model=OrganizationRead)
async def update_organization(
    org_id: int,
    body: OrganizationUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    org = await get_or_404(db, Organization, org_id)
    await apply_update(db, org, body)
    return org


@router.patch("/{org_id}/ltg-security")
async def update_ltg_security(
    org_id: int,
    body: LtgSecurityUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    """Update san_access_rating for one LTG entry, identified by rtg+ltg keys."""
    org = await get_or_404(db, Organization, org_id)
    updated = []
    changed = False
    for entry in (org.ltgs or []):
        e = dict(entry)
        if e.get("rtg") == body.rtg and e.get("ltg") == body.ltg:
            e["san_access_rating"] = body.san_access_rating
            changed = True
        updated.append(e)
    if not changed:
        raise HTTPException(
            status_code=404,
            detail=f"No LTG entry with rtg='{body.rtg}' ltg='{body.ltg}' in org {org_id}",
        )
    org.ltgs = updated
    await db.commit()
    return {"updated": True, "org_id": org_id, "new_rating": body.san_access_rating}


@router.delete("/{org_id}", status_code=204)
async def delete_organization(
    org_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    org = await get_or_404(db, Organization, org_id)
    # These FKs have no DB-level ondelete rule; with foreign_keys=ON a plain delete would
    # be blocked, so null the references first (SET NULL semantics). org_standings are
    # removed by the ORM cascade; matrix_host.owner_org_id is SET NULL at the DB level.
    await db.execute(sql_update(Character).where(Character.organization_id == org_id).values(organization_id=None))
    await db.execute(sql_update(Contact).where(Contact.organization_id == org_id).values(organization_id=None))
    await db.execute(sql_update(Location).where(Location.controlling_org_id == org_id).values(controlling_org_id=None))
    await db.delete(org)
    await db.commit()
