from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_or_404, apply_update
from app.models.character import Character
from app.models.contact import Contact
from app.schemas.contact import ContactCreate, ContactUpdate, ContactRead
from app.auth.dependencies import get_admin_token, get_any_token

router = APIRouter()


def _is_privileged_view(ctx: dict) -> bool:
    """True only for a real admin NOT previewing runner view -- the full-data audience."""
    return bool(ctx.get("is_admin")) and not ctx.get("view_as_player")


def serialize_contact(contact: Contact, ctx: dict) -> dict:
    data = ContactRead.model_validate(contact, from_attributes=True).model_dump()
    if not _is_privileged_view(ctx):
        data["notes"] = None
    return data


async def visible_contacts(db: AsyncSession, contacts, ctx: dict) -> list[Contact]:
    """Drop GM-concealed contacts for non-privileged callers: inactive contacts, and contacts whose
    linked NPC is inactive (kidnapped/unavailable). Admin (non-preview) sees the full roster."""
    contacts = list(contacts)
    if _is_privileged_view(ctx):
        return contacts
    inactive_npc_ids = set(
        (
            await db.execute(
                select(Character.id).where(
                    Character.is_pc == False,  # noqa: E712
                    Character.is_active == False,  # noqa: E712
                )
            )
        ).scalars().all()
    )
    return [
        c for c in contacts
        if c.is_active and (c.npc_id is None or c.npc_id not in inactive_npc_ids)
    ]


@router.get("/", response_model=list[ContactRead])
async def list_contacts(
    owner_id: int | None = Query(None, description="Filter by owning character ID"),
    organization_id: int | None = Query(None),
    ctx: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    # Contacts are a shared world roster: every authenticated user sees the whole active-runner
    # contact network (GM notes are still redacted from non-admins in serialize_contact).
    q = select(Contact)
    if owner_id is not None:
        q = q.where(Contact.owner_id == owner_id)
    if organization_id is not None:
        q = q.where(Contact.organization_id == organization_id)
    result = await db.execute(q.order_by(Contact.name))
    contacts = await visible_contacts(db, result.scalars().all(), ctx)
    return [serialize_contact(contact, ctx) for contact in contacts]


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
async def get_contact(
    contact_id: int,
    ctx: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    contact = await get_or_404(db, Contact, contact_id)
    if not await visible_contacts(db, [contact], ctx):
        raise HTTPException(status_code=404, detail="Contact not found")
    return serialize_contact(contact, ctx)


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
