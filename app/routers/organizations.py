from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_or_404, apply_update
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationUpdate, OrganizationRead, OrganizationSummary
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


@router.delete("/{org_id}", status_code=204)
async def delete_organization(
    org_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    org = await get_or_404(db, Organization, org_id)
    await db.delete(org)
    await db.commit()
