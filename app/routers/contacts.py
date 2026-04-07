from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_or_404, apply_update
from app.models.contact import Contact
from app.schemas.contact import ContactCreate, ContactUpdate, ContactRead
from app.auth.dependencies import get_admin_token

router = APIRouter()


@router.get("/", response_model=list[ContactRead])
async def list_contacts(
    owner_id: int | None = Query(None, description="Filter by owning character ID"),
    organization_id: int | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    q = select(Contact)
    if owner_id is not None:
        q = q.where(Contact.owner_id == owner_id)
    if organization_id is not None:
        q = q.where(Contact.organization_id == organization_id)
    result = await db.execute(q.order_by(Contact.name))
    return result.scalars().all()


@router.post("/", response_model=ContactRead, status_code=201)
async def create_contact(
    body: ContactCreate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    contact = Contact(**body.model_dump())
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact


@router.get("/{contact_id}", response_model=ContactRead)
async def get_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    return await get_or_404(db, Contact, contact_id)


@router.patch("/{contact_id}", response_model=ContactRead)
async def update_contact(
    contact_id: int,
    body: ContactUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    contact = await get_or_404(db, Contact, contact_id)
    await apply_update(db, contact, body)
    return contact


@router.delete("/{contact_id}", status_code=204)
async def delete_contact(
    contact_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    contact = await get_or_404(db, Contact, contact_id)
    await db.delete(contact)
    await db.commit()
