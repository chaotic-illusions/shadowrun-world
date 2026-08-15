from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, update as sql_update, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.dependencies import get_db, get_or_404, apply_update
from app.models.character import Character, LIFESTYLE_UPKEEP_TICKS
from app.models.contact import Contact
from app.models.reputation import Reputation
from app.schemas.character import CharacterCreate, CharacterUpdate, CharacterRead, CharacterSummary, DossierCommit, LifestylePurchase
from app.schemas.contact import ContactRead
from app.schemas.deck_builder_state import DeckBuilderStateRead, DeckBuilderStateUpdate
from app.schemas.reputation import ReputationRead
from app.auth.core import hash_token
from app.auth.dependencies import get_admin_token, get_any_token
from app.services.campaign import current_tick
from app.services.lifestyle import monthly_cost, permanent_cost

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


def _dossier_create_data(body: CharacterCreate, ctx: dict) -> dict:
    """Chargen commit accepts the FULL sheet from either an admin or a player.

    Unlike the lightweight create path, a player building their own dossier may set
    every gameplay field (attributes, essence, skills, gear, ...). The result is a
    PC owned by the committing token (an admin's token counts). Chargen is a
    trust-the-player tool -- the GM reviews finished sheets rather than the server
    enforcing a points budget.
    """
    data = body.model_dump(exclude={"contacts"})
    data.pop("owner_token", None)
    data["is_pc"] = True
    # Claim the new PC to the committing token (an admin's token counts) so the builder owns it
    # immediately -- no manual world-state claim needed. Matches claim_character's token semantics.
    if ctx.get("user_token"):
        data["owner_token"] = hash_token(ctx["user_token"])
    return data


# TESTING TOGGLE -- set True before shipping. Chargen contacts are promoted to NPC "persons of
# interest" (Known Persons). While False, those POI are deleted along with the PC that named them
# so scratch characters clean up fully; True keeps them standing in the registry for a live world.
_KEEP_CHARGEN_POI_ON_DELETE = False


async def _create_dossier_contacts(db: AsyncSession, char: Character, contacts) -> None:
    """Create the runner's chargen contacts as Contact rows, each linked (npc_id) to a freshly
    created NPC "person of interest" so it appears in the Known Persons registry.

    TESTING vs SHIP: see _KEEP_CHARGEN_POI_ON_DELETE and delete_character. The POI are currently
    removed with the PC (easy cleanup while testing) and will persist independently on ship.
    """
    for c in contacts:
        poi = Character(name=c.name, is_pc=False, archetype=c.profession, connection=c.connection)
        db.add(poi)
        await db.flush()  # assign poi.id for the npc link
        db.add(Contact(
            owner_id=char.id, npc_id=poi.id, name=c.name, profession=c.profession,
            connection=c.connection, loyalty=c.loyalty,
        ))


async def _stamp_lifestyle_start(db: AsyncSession, char: Character) -> None:
    """Start the lifestyle upkeep clock for a PC that just became real.

    Stamps ``lifestyle_paid_tick`` to the current campaign tick so the runner is
    charged rent from commit-time forward (never billed back-rent). No-op for
    characters without a lifestyle.
    """
    if char.lifestyle_level is not None and char.lifestyle_paid_tick is None:
        char.lifestyle_paid_tick = await current_tick(db)


# Cyberware grades a player may commit at character creation. Betaware is a post-chargen
# career purchase and Deltaware is GM-authorized only, so both are blocked for non-admins.
_CHARGEN_GRADES_ALLOWED = {None, "", "Standard", "Alpha"}


def _assert_chargen_grades_allowed(gear: dict | None, is_admin: bool) -> None:
    """Reject GM-gated cyber grades (Beta/Delta) in a non-admin chargen submission.

    Defense-in-depth behind the wizard UI, which already hides these options. Admins
    (GMs) may commit any grade -- that is how Delta gets applied to a character.
    """
    if is_admin:
        return
    for line in ((gear or {}).get("cyber") or []):
        grade = line.get("grade") if isinstance(line, dict) else None
        if grade not in _CHARGEN_GRADES_ALLOWED:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Cyberware grade '{grade}' requires GM authorization and "
                    "cannot be selected at character creation"
                ),
            )


def _apply_dossier(char: Character, body: CharacterCreate, ctx: dict, *, keep_draft: bool) -> None:
    """Write a full chargen sheet onto an existing owned character row.

    Shared by the draft-update and finalize paths. Ownership is never reassigned here;
    ``keep_draft`` controls whether the row stays a draft (mid-build) or becomes real.
    """
    _assert_chargen_grades_allowed(body.gear, ctx["is_admin"])
    data = _dossier_create_data(body, ctx)
    data.pop("owner_token", None)  # never reassign ownership on an existing row
    data["is_draft"] = keep_draft
    for key, value in data.items():
        setattr(char, key, value)

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


@router.get("/drafts", response_model=list[CharacterRead])
async def my_draft_characters(
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Return the caller's in-progress chargen drafts (admins see all drafts).

    Drafts are hidden from the normal character list; this is how the builder and the
    Characters page surface a runner's unfinished dossiers so they can be resumed.
    """
    q = select(Character).options(selectinload(Character.organization)).where(
        Character.is_draft == True  # noqa: E712 -- SQL boolean comparison
    )
    if not ctx["is_admin"]:
        q = q.where(Character.owner_token == hash_token(ctx["user_token"]))
    result = await db.execute(q.order_by(Character.updated_at.desc()))
    return [_serialize_character(char, ctx) for char in result.scalars().all()]


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
    # Chargen drafts are hidden everywhere until the wizard finalizes them.
    q = q.where(Character.is_draft == False)  # noqa: E712 -- SQL boolean comparison
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


@router.post("/dossier", response_model=CharacterRead, status_code=201)
async def create_character_dossier(
    body: DossierCommit,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Commit a full chargen dossier (character builder) as a new PC.

    Claimed to the committing token (user or admin) so the builder owns it right away.
    """
    _assert_chargen_grades_allowed(body.gear, ctx["is_admin"])
    char = Character(**_dossier_create_data(body, ctx))
    if not char.is_draft:
        await _stamp_lifestyle_start(db, char)
    db.add(char)
    await db.commit()
    await db.refresh(char, attribute_names=["organization"])
    if body.contacts and not char.is_draft:
        await _create_dossier_contacts(db, char, body.contacts)
        await db.commit()
    return _serialize_character(char, ctx)


@router.post("/{character_id}/dossier-draft", response_model=CharacterRead)
async def update_character_draft(
    character_id: int,
    body: DossierCommit,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Refresh an in-progress chargen draft with the wizard's current sheet.

    Keeps the draft flag set (and preserves the deck the player is building against it),
    so the Deck Workshop derives caps from up-to-date skills. Owner-or-admin only.
    """
    char = await _load_character(db, character_id)
    if not _is_owner_or_admin(char, ctx):
        raise HTTPException(status_code=404, detail="Character not found")
    if not char.is_draft:
        raise HTTPException(status_code=400, detail="Only a draft character can be updated as a draft")
    _apply_dossier(char, body, ctx, keep_draft=True)
    await db.commit()
    await db.refresh(char, attribute_names=["organization"])
    return _serialize_character(char, ctx)


@router.post("/{character_id}/finalize-dossier", response_model=CharacterRead)
async def finalize_character_dossier(
    character_id: int,
    body: DossierCommit,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Finalize a chargen draft PC into a real character (character builder).

    Writes the full sheet onto an existing draft the caller owns and clears the draft
    flag, preserving the deck the player built against it during chargen. Only a draft
    may be finalized; non-admins get the same grade/Delta gating as the create path.
    """
    char = await _load_character(db, character_id)
    if not _is_owner_or_admin(char, ctx):
        raise HTTPException(status_code=404, detail="Character not found")
    if not char.is_draft:
        raise HTTPException(status_code=400, detail="Only a draft character can be finalized")
    _apply_dossier(char, body, ctx, keep_draft=False)
    await _stamp_lifestyle_start(db, char)
    if body.contacts:
        await _create_dossier_contacts(db, char, body.contacts)
    await db.commit()
    await db.refresh(char, attribute_names=["organization"])
    return _serialize_character(char, ctx)


@router.post("/{character_id}/convert-dossier", response_model=CharacterRead)
async def convert_character_dossier(
    character_id: int,
    body: DossierCommit,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Overwrite an existing (non-draft) character in place with a full chargen sheet.

    The conversion path for pre-wizard PCs: open the character in the builder, fill in
    the sheet, and commit back onto the same record. Owner-or-admin only. Contacts are
    created only when the character has none yet, so re-converting never duplicates them.
    """
    char = await _load_character(db, character_id)
    if not _is_owner_or_admin(char, ctx):
        raise HTTPException(status_code=404, detail="Character not found")
    if char.is_draft:
        raise HTTPException(status_code=400, detail="Use finalize-dossier for a draft character")
    _apply_dossier(char, body, ctx, keep_draft=False)
    await _stamp_lifestyle_start(db, char)
    if body.contacts:
        existing = await db.scalar(
            select(func.count()).select_from(Contact).where(Contact.owner_id == char.id)
        )
        if not existing:
            await _create_dossier_contacts(db, char, body.contacts)
    await db.commit()
    await db.refresh(char, attribute_names=["organization"])
    return _serialize_character(char, ctx)


@router.post("/{character_id}/lifestyle", response_model=CharacterRead)
async def purchase_lifestyle(
    character_id: int,
    body: LifestylePurchase,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Buy or change a lifestyle after chargen, paid from the character's nuyen.

    Owner-or-admin only. Prepays ``months`` of upkeep up front (advancing the settle
    clock so upkeep is not double-charged), or buys the tier outright when
    ``permanent`` is set (100 months). Fails with 400 if the character can't afford it.
    """
    char = await _load_character(db, character_id)
    if not char.is_pc:
        raise HTTPException(status_code=400, detail="Lifestyle applies only to PCs")
    if not _is_owner_or_admin(char, ctx):
        raise HTTPException(status_code=404, detail="Character not found")

    total = permanent_cost(body.level) if body.permanent else monthly_cost(body.level) * body.months
    if total > char.nuyen:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient nuyen: need {total}, have {char.nuyen}",
        )

    tick = await current_tick(db)
    char.nuyen -= total
    char.lifestyle_level = body.level
    char.lifestyle_permanent = body.permanent
    # Prepaid through now + months (permanent never accrues, so just stamp to now).
    char.lifestyle_paid_tick = tick if body.permanent else tick + body.months * LIFESTYLE_UPKEEP_TICKS
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
    ctx: dict = Depends(get_any_token),
):
    """Delete a character.

    A GM (admin) may delete any character. A player may delete only their OWN
    in-progress draft; once a dossier is committed to the world it takes a GM to
    remove it. A non-owner's hidden draft returns 404 so its existence stays private.
    """
    char = await get_or_404(db, Character, character_id)
    if not ctx["is_admin"]:
        owns = bool(char.owner_token and char.owner_token == hash_token(ctx["user_token"]))
        if char.is_draft and owns:
            pass  # a player discarding their own unfinished dossier
        elif char.is_draft:
            raise HTTPException(status_code=404, detail="Character not found")
        else:
            raise HTTPException(status_code=403, detail="Only a GM can delete a committed character")
    # Persons of interest this PC created from its chargen contacts (Contact.npc_id links). TESTING:
    # gather them so they are removed with the PC; SHIP (_KEEP_CHARGEN_POI_ON_DELETE=True): keep them.
    poi_ids: list[int] = []
    if not _KEEP_CHARGEN_POI_ON_DELETE:
        poi_ids = list((await db.execute(
            select(Contact.npc_id).where(Contact.owner_id == character_id, Contact.npc_id.isnot(None))
        )).scalars().all())
    # Contacts that reference this character as their NPC have no DB ondelete rule; null them so
    # foreign_keys=ON does not block the delete. (Owned contacts, reputation, and standings are
    # removed by the ORM cascade on Character during the awaited flush.)
    await db.execute(sql_update(Contact).where(Contact.npc_id == character_id).values(npc_id=None))
    await db.delete(char)
    await db.flush()  # emit the cascade (owned-contact deletes) before removing the POI they referenced
    for pid in poi_ids:
        npc = await db.get(Character, pid)
        if npc is None or npc.is_pc:
            continue  # only remove NPC persons of interest, never a real PC
        await db.execute(sql_update(Contact).where(Contact.npc_id == pid).values(npc_id=None))
        await db.delete(npc)
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
