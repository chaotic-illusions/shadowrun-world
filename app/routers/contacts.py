from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_or_404, apply_update
from app.models.character import Character
from app.models.contact import Contact
from app.schemas.contact import ContactCreate, ContactUpdate, ContactRead
from app.auth.dependencies import get_admin_token, get_any_token

router = APIRouter()


# An individual contact's type and Loyalty are tied: Contact 1, Buddy 3, Follower 6 (chargen gives
# exactly those). Setting Loyalty therefore sets the type -- 6 Follower, 3-5 Buddy, 1-2 Contact --
# so the GM's loyalty dots and the runner's dossier tag can't disagree. Gang/Tribe contacts are an
# organization tie, not a person, and keep their type whatever the Loyalty.
_ORG_TIE_TYPES = {"Gang", "Tribe"}


def contact_type_for_loyalty(loyalty: int) -> str:
    return "Follower" if loyalty >= 6 else "Buddy" if loyalty >= 3 else "Contact"


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
    data = body.model_dump()
    if not data.get("contact_type"):
        data["contact_type"] = contact_type_for_loyalty(data["loyalty"])
    contact = Contact(**data)
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
    changes = body.model_dump(exclude_unset=True)
    await apply_update(db, contact, body, commit=False)
    # A Loyalty change re-derives the type unless the same request set the type itself.
    if "loyalty" in changes and "contact_type" not in changes and contact.contact_type not in _ORG_TIE_TYPES:
        contact.contact_type = contact_type_for_loyalty(contact.loyalty)
    await db.commit()
    await db.refresh(contact)
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
