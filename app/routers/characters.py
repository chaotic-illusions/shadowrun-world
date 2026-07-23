from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, update as sql_update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.dependencies import get_db, get_or_404, apply_update
from app.models.character import Character
from app.models.contact import Contact
from app.models.reputation import Reputation
from app.schemas.character import CharacterCreate, CharacterUpdate, CharacterRead, CharacterSummary
from app.schemas.contact import ContactRead
from app.schemas.deck_builder_state import DeckBuilderStateRead, DeckBuilderStateUpdate
from app.schemas.reputation import ReputationRead
from app.auth.core import hash_token
from app.auth.dependencies import get_admin_token, get_any_token

router = APIRouter()

_PLAYER_WRITABLE_FIELDS = {
    "name", "archetype", "title", "race", "nationality", "gender",
    "age", "description", "background", "notes", "is_active",
}


def _serialize_character(char: Character, ctx: dict) -> dict:
    data = CharacterRead.model_validate(char, from_attributes=True).model_dump()
    if ctx.get("is_admin") and not ctx.get("view_as_player"):
        return data
    data["notes"] = None
    if not data.get("show_background"):
        data["background"] = None
    return data


async def _load_character(db: AsyncSession, character_id: int) -> Character:
    """Load a character with its organization eagerly loaded (needed for organization_name)."""
    result = await db.execute(
        select(Character).options(selectinload(Character.organization)).where(Character.id == character_id)
    )
    char = result.scalars().first()
    if not char:
        raise HTTPException(status_code=404, detail="Character not found")
    return char


def _is_owner_or_admin(char: Character, ctx: dict) -> bool:
    if ctx["is_admin"]:
        return True
    caller_hash = hash_token(ctx["user_token"])
    return bool(char.owner_token and char.owner_token == caller_hash)


def _character_create_data(body: CharacterCreate, ctx: dict) -> dict:
    if ctx["is_admin"]:
        data = body.model_dump()
        data.pop("owner_token", None)
        return data

    data = body.model_dump(include=_PLAYER_WRITABLE_FIELDS)
    data["is_pc"] = True
    data["owner_token"] = hash_token(ctx["user_token"])
    return data


@router.get("/mine")
async def my_character_ids(
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Return IDs of characters owned by the caller's token."""
    caller_hash = hash_token(ctx["user_token"])
    result = await db.execute(
        select(Character.id).where(Character.owner_token == caller_hash)
    )
    return {"ids": [row[0] for row in result.all()]}


@router.get("/{character_id}/deck-builder-state", response_model=DeckBuilderStateRead)
async def get_deck_builder_state(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    char = await _load_character(db, character_id)
    if not char.is_pc:
        raise HTTPException(status_code=400, detail="Deck builder state is only available for PCs")
    if not _is_owner_or_admin(char, ctx):
        raise HTTPException(status_code=403, detail="Admin or character owner required")
    return DeckBuilderStateRead(state=char.deck_builder_state or {})


@router.put("/{character_id}/deck-builder-state", response_model=DeckBuilderStateRead)
async def update_deck_builder_state(
    character_id: int,
    body: DeckBuilderStateUpdate,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    char = await _load_character(db, character_id)
    if not char.is_pc:
        raise HTTPException(status_code=400, detail="Deck builder state is only available for PCs")
    if not _is_owner_or_admin(char, ctx):
        raise HTTPException(status_code=403, detail="Admin or character owner required")
    char.deck_builder_state = body.state or {}
    await db.commit()
    await db.refresh(char)
    return DeckBuilderStateRead(state=char.deck_builder_state or {})


@router.get("/", response_model=list[CharacterRead])
async def list_characters(
    is_pc: bool | None = Query(None, description="Filter by PC (true) or NPC (false)"),
    is_active: bool | None = Query(None),
    ctx: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    q = select(Character).options(selectinload(Character.organization))
    if is_pc is not None:
        q = q.where(Character.is_pc == is_pc)
    if is_active is not None:
        q = q.where(Character.is_active == is_active)
    result = await db.execute(q.order_by(Character.name))
    return [_serialize_character(char, ctx) for char in result.scalars().all()]


@router.post("/", response_model=CharacterRead, status_code=201)
async def create_character(
    body: CharacterCreate,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    char = Character(**_character_create_data(body, ctx))
    db.add(char)
    await db.commit()
    await db.refresh(char, attribute_names=["organization"])
    return _serialize_character(char, ctx)


@router.get("/{character_id}", response_model=CharacterRead)
async def get_character(
    character_id: int,
    ctx: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    return _serialize_character(await _load_character(db, character_id), ctx)


@router.patch("/{character_id}", response_model=CharacterRead)
async def update_character(
    character_id: int,
    body: CharacterUpdate,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    char = await _load_character(db, character_id)
    is_admin = ctx["is_admin"]
    caller_hash = hash_token(ctx["user_token"])
    is_owner = bool(char.owner_token and char.owner_token == caller_hash)

    if not is_admin and not is_owner:
        raise HTTPException(status_code=403, detail="Admin or character owner required")

    # Non-admins may only update a limited set of fields on their own PC
    if not is_admin:
        submitted = body.model_dump(exclude_unset=True)
        forbidden = set(submitted.keys()) - _PLAYER_WRITABLE_FIELDS
        if forbidden:
            raise HTTPException(status_code=403, detail=f"Players cannot modify: {', '.join(sorted(forbidden))}")

    await apply_update(db, char, body, exclude={"owner_token"})
    return _serialize_character(char, ctx)


@router.delete("/{character_id}", status_code=204)
async def delete_character(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    char = await get_or_404(db, Character, character_id)
    # Contacts that reference this character as their NPC have no DB ondelete rule; null
    # them so foreign_keys=ON does not block the delete. (Owned contacts, reputation, and
    # standings are removed by the ORM cascade on Character.)
    await db.execute(sql_update(Contact).where(Contact.npc_id == character_id).values(npc_id=None))
    await db.delete(char)
    await db.commit()


@router.get("/{character_id}/contacts", response_model=list[ContactRead])
async def get_character_contacts(character_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Character).options(selectinload(Character.contacts)).where(Character.id == character_id)
    )
    char = result.scalars().first()
    if not char:
        raise HTTPException(status_code=404, detail="Character not found")
    return char.contacts


@router.get("/{character_id}/reputation", response_model=ReputationRead | None)
async def get_character_reputation(character_id: int, db: AsyncSession = Depends(get_db)):
    await get_or_404(db, Character, character_id)
    result = await db.execute(select(Reputation).where(Reputation.character_id == character_id))
    return result.scalars().first()


# -- Claim / unclaim -----------------------------------------------------------

@router.post("/{character_id}/claim", response_model=CharacterRead)
async def claim_character(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Player or admin claims a PC by writing their token hash onto it."""
    claim_hash = hash_token(ctx["user_token"])

    result = await db.execute(
        sql_update(Character)
        .where(
            Character.id == character_id,
            Character.is_pc.is_(True),
            (Character.owner_token.is_(None)) | (Character.owner_token == claim_hash),
        )
        .values(owner_token=claim_hash)
    )
    if result.rowcount != 1:
        char = await _load_character(db, character_id)
        if not char.is_pc:
            raise HTTPException(status_code=400, detail="Only PC characters can be claimed")
        raise HTTPException(status_code=409, detail="Character is already claimed by another player")

    await db.commit()
    return _serialize_character(await _load_character(db, character_id), ctx)


@router.post("/{character_id}/unclaim", response_model=CharacterRead)
async def unclaim_character(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Admin or the owning player can unclaim a character."""
    char = await _load_character(db, character_id)
    is_admin = ctx["is_admin"]
    caller_hash = hash_token(ctx["user_token"])
    is_owner = bool(char.owner_token and char.owner_token == caller_hash)

    if not is_admin and not is_owner:
        raise HTTPException(status_code=403, detail="Only the owning player or an admin can unclaim")

    char.owner_token = None
    await db.commit()
    await db.refresh(char, attribute_names=["organization"])
    return _serialize_character(char, ctx)
