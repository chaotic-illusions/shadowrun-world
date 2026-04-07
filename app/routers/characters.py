from fastapi import APIRouter, Depends, HTTPException, Query, Header
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.dependencies import get_db, get_or_404, apply_update
from app.models.character import Character
from app.models.reputation import Reputation
from app.schemas.character import CharacterCreate, CharacterUpdate, CharacterRead, CharacterSummary
from app.schemas.contact import ContactRead
from app.schemas.reputation import ReputationRead
from app.auth.core import verify_user_token, verify_admin_token, hash_token
from app.auth.dependencies import get_admin_token, get_any_token

router = APIRouter()


async def _load_character(db: AsyncSession, character_id: int) -> Character:
    """Load a character with its organization eagerly loaded (needed for organization_name)."""
    result = await db.execute(
        select(Character).options(selectinload(Character.organization)).where(Character.id == character_id)
    )
    char = result.scalars().first()
    if not char:
        raise HTTPException(status_code=404, detail="Character not found")
    return char


@router.get("/mine")
async def my_character_ids(
    db: AsyncSession = Depends(get_db),
    x_admin_token: str | None = Header(default=None, alias="X-Admin-Token"),
    x_user_token: str | None = Header(default=None, alias="X-User-Token"),
):
    """Return IDs of characters owned by the caller's token."""
    token = x_user_token or x_admin_token
    if not token:
        return {"ids": []}
    caller_hash = hash_token(token)
    result = await db.execute(
        select(Character.id).where(Character.owner_token == caller_hash)
    )
    return {"ids": [row[0] for row in result.all()]}


@router.get("/", response_model=list[CharacterRead])
async def list_characters(
    is_pc: bool | None = Query(None, description="Filter by PC (true) or NPC (false)"),
    is_active: bool | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    q = select(Character).options(selectinload(Character.organization))
    if is_pc is not None:
        q = q.where(Character.is_pc == is_pc)
    if is_active is not None:
        q = q.where(Character.is_active == is_active)
    result = await db.execute(q.order_by(Character.name))
    return result.scalars().all()


@router.post("/", response_model=CharacterRead, status_code=201)
async def create_character(
    body: CharacterCreate,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    data = body.model_dump()
    # Store the caller's token hash as owner only when a non-admin player creates a PC.
    # Admin-created PCs (including all seeded data) remain unclaimed so players can claim them.
    if data.get("is_pc", True) and not ctx["is_admin"]:
        data["owner_token"] = hash_token(ctx["user_token"])
    else:
        data.pop("owner_token", None)
    char = Character(**data)
    db.add(char)
    await db.commit()
    await db.refresh(char, attribute_names=["organization"])
    return char


@router.get("/{character_id}", response_model=CharacterRead)
async def get_character(character_id: int, db: AsyncSession = Depends(get_db)):
    return await _load_character(db, character_id)


@router.patch("/{character_id}", response_model=CharacterRead)
async def update_character(
    character_id: int,
    body: CharacterUpdate,
    db: AsyncSession = Depends(get_db),
    x_admin_token: str | None = Header(default=None, alias="X-Admin-Token"),
    x_user_token: str | None = Header(default=None, alias="X-User-Token"),
):
    char = await _load_character(db, character_id)
    is_admin = bool(x_admin_token and await verify_admin_token(db, x_admin_token))
    caller_hash = hash_token(x_user_token) if x_user_token else None
    is_owner = bool(caller_hash and char.owner_token == caller_hash)

    if not is_admin and not is_owner:
        raise HTTPException(status_code=403, detail="Admin or character owner required")

    # Non-admins may only update a limited set of fields on their own PC
    if not is_admin:
        allowed = {"name", "archetype", "title", "race", "nationality", "gender",
                    "age", "description", "background", "notes", "is_active"}
        submitted = body.model_dump(exclude_unset=True)
        forbidden = set(submitted.keys()) - allowed
        if forbidden:
            raise HTTPException(status_code=403, detail=f"Players cannot modify: {', '.join(sorted(forbidden))}")

    await apply_update(db, char, body, exclude={"owner_token"})
    return char


@router.delete("/{character_id}", status_code=204)
async def delete_character(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    char = await get_or_404(db, Character, character_id)
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


# ── Claim / unclaim ───────────────────────────────────────────────────────────

@router.post("/{character_id}/claim", response_model=CharacterRead)
async def claim_character(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    x_user_token: str | None = Header(default=None, alias="X-User-Token"),
    x_admin_token: str | None = Header(default=None, alias="X-Admin-Token"),
):
    """Player or admin claims a PC by writing their token hash onto it."""
    if x_user_token and await verify_user_token(db, x_user_token):
        claim_hash = hash_token(x_user_token)
    elif x_admin_token and await verify_admin_token(db, x_admin_token):
        claim_hash = hash_token(x_admin_token)
    else:
        raise HTTPException(status_code=403, detail="Valid user token required to claim a character")

    char = await _load_character(db, character_id)
    if not char.is_pc:
        raise HTTPException(status_code=400, detail="Only PC characters can be claimed")
    if char.owner_token and char.owner_token != claim_hash:
        raise HTTPException(status_code=409, detail="Character is already claimed by another player")

    char.owner_token = claim_hash
    await db.commit()
    await db.refresh(char, attribute_names=["organization"])
    return char


@router.post("/{character_id}/unclaim", response_model=CharacterRead)
async def unclaim_character(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    x_admin_token: str | None = Header(default=None, alias="X-Admin-Token"),
    x_user_token: str | None = Header(default=None, alias="X-User-Token"),
):
    """Admin or the owning player can unclaim a character."""
    char = await _load_character(db, character_id)
    is_admin = bool(x_admin_token and await verify_admin_token(db, x_admin_token))
    caller_hash = hash_token(x_user_token) if x_user_token else None
    is_owner = bool(caller_hash and char.owner_token == caller_hash)

    if not is_admin and not is_owner:
        raise HTTPException(status_code=403, detail="Only the owning player or an admin can unclaim")

    char.owner_token = None
    await db.commit()
    await db.refresh(char, attribute_names=["organization"])
    return char
