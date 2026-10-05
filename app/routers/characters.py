import io
import math
import os
import re
import uuid

import aiofiles
from fastapi import APIRouter, Depends, HTTPException, Query, Response, UploadFile, File
from PIL import Image, UnidentifiedImageError
from sqlalchemy import select, update as sql_update, func, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.dependencies import get_db, get_or_404, apply_update
from app.models.auth import UserToken
from app.models.character import Character
from app.models.contact import Contact
from app.models.organization import Organization
from app.models.reputation import Reputation
from app.schemas.character import (
    CharacterCreate, CharacterUpdate, CharacterRead, CharacterSummary, DossierCommit, ChargenStateRead,
    CharacterOwnerAssign, KarmaAward, KarmaDonation,
)
from app.routers.contacts import contact_type_for_loyalty, serialize_contact, visible_contacts
from app.schemas.contact import ContactRead
from app.schemas.deck_builder_state import DeckBuilderStateRead, DeckBuilderStateUpdate
from app.schemas.reputation import ReputationRead
from app.auth.core import hash_token
from app.auth.dependencies import get_admin_token, get_any_token
from app.models.campaign import CampaignState
from app.services.campaign import current_tick, get_campaign_state

router = APIRouter()

# Identity-only fields: safe for a bare POST /characters/ (a brand-new character with no chargen
# history yet, nothing to spend points on). Career/gameplay fields are deliberately excluded here --
# see _PLAYER_WRITABLE_FIELDS below -- a plain create must never be able to hand a fresh PC max
# nuyen/essence/attributes/Delta-grade gear the way an existing character's post-chargen PATCH can.
_PLAYER_IDENTITY_FIELDS = {
    "name", "archetype", "title", "race", "nationality", "gender",
    "age", "description", "background", "notes", "is_active",
}

_PLAYER_WRITABLE_FIELDS = _PLAYER_IDENTITY_FIELDS | {
    # Career fields: post-chargen play-sheet edits (karma spend, purchases, condition
    # tracking). Trust-the-player, same philosophy as the chargen dossier commit --
    # the GM reviews the sheet rather than the server enforcing a points budget. PATCH-only:
    # a character must already exist (created via /characters/ or committed via /characters/dossier)
    # before any of these become writable -- see _character_create_data, which uses
    # _PLAYER_IDENTITY_FIELDS instead of this full set.
    # karma_pool is not here: it moves only by Karma awards and donations (their own endpoints
    # below), and otherwise only a GM sets it.
    "nuyen", "good_karma", "skills", "gear", "spells",
    "body", "quickness", "strength", "charisma", "intelligence", "willpower",
    "essence", "body_index", "magic_rating", "lifestyle_level", "lifestyle_permanent",
    "physical_damage", "stun_damage", "physical_overflow",
    # Play-sheet karma-raise commits patch chargen_state.base (the true pre-augmentation
    # attribute ratings) alongside the recomputed aggregate above -- see play-sheet.html's
    # commitModal() 'attrs' branch.
    "chargen_state",
}

# Fields on the chargen dossier schema that only a GM may set: cyber-grade approvals, affiliation,
# reveal flags and provenance. A player's dossier commit never writes them -- a new PC gets the
# column default and an existing one keeps its stored value.
_DOSSIER_GM_FIELDS = {
    "beta_grade_approved", "delta_grade_approved", "organization_id", "is_independent",
    "portrait_url", "show_background", "source_adventure", "catalog_scope", "contact_skills",
}


# Essence/Body Index are the two post-chargen limits that are hard-enforced rather than
# trust-the-player (unlike nuyen, see _PLAYER_WRITABLE_FIELDS above) -- this mirrors just enough of
# frontend/shared.js's cyberBaseEss/gradedCyberEssence and play-sheet.html's ownedBioIndex to
# recompute both totals from a submitted gear blob, without a client round-trip. Grade multipliers
# must stay in sync with play-sheet.html's ESS_GRADE_MULT if a new grade is ever added there.
_ESS_GRADE_MULT = {"Standard": 1.0, "Alpha": 0.8, "Beta": 0.6, "Delta": 0.5}

# Cyber grade -> the Character boolean column a GM must have set before a player's gear PATCH may
# introduce that grade. Beta/Delta are never offered at chargen (see _assert_chargen_grades_allowed)
# and stay GM-gated post-chargen too -- a player can spend nuyen/karma freely (_PLAYER_WRITABLE_FIELDS
# trusts them there) but not unlock a narratively-restricted grade by hand-editing a gear PATCH.
_GRADE_APPROVAL_COLUMN = {"Beta": "beta_grade_approved", "Delta": "delta_grade_approved"}
_STARTING_ESSENCE = 6.0


def _clamped_rating(g: dict) -> int:
    lo = int(g.get("minRating") or 1)
    hi = max(lo, int(g.get("maxRating") or lo))
    return max(lo, min(int(g.get("rating") or lo), hi))


def _rated_ess_lookup(g: dict) -> float:
    lo = int(g.get("minRating") or 1)
    r = _clamped_rating(g)
    ess_tbl = g.get("essTbl")
    idx = r - lo
    if isinstance(ess_tbl, list) and 0 <= idx < len(ess_tbl) and ess_tbl[idx] is not None:
        return float(ess_tbl[idx] or 0)
    return float(g.get("essUnit") or 0) * r


def _grade_essence_cost(base_ess: float, mult: float) -> float:
    if base_ess <= 0:
        return 0.0
    v = math.ceil(base_ess * mult * 100 - 1e-9) / 100
    return max(0.05, v)


def _essence_used(gear: dict) -> float:
    total = 0.0
    for g in (gear or {}).get("cyber") or []:
        base = float(g.get("baseEss") or 0) if not g.get("rated") else _rated_ess_lookup(g)
        base += sum(float(o.get("ess") or 0) for o in (g.get("options") or []))
        if g.get("noGrade"):
            total += base
        else:
            total += _grade_essence_cost(base, _ESS_GRADE_MULT.get(g.get("grade") or "Standard", 1.0))
    return total


def _body_index_used(gear: dict) -> float:
    total = 0.0
    for g in (gear or {}).get("bio") or []:
        total += float(g.get("ess") or 0) if not g.get("rated") else _rated_ess_lookup(g)
    return total


def _validate_hard_gear_caps(char: Character, submitted: dict) -> None:
    """Reject a PATCH whose (post-update) gear would push Essence or Body Index past its cap --
    closes the gap where a direct PATCH with a hand-picked gear+essence pair could bypass the
    client-side purchase-flow check entirely.
    """
    gear = submitted.get("gear", char.gear) or {}
    ess_used = _essence_used(gear)
    if ess_used > _STARTING_ESSENCE + 1e-6:
        raise HTTPException(
            status_code=422,
            detail=f"Gear implies {ess_used:.2f} Essence used, exceeding the {_STARTING_ESSENCE:.0f} available.",
        )
    # Body Index is capped at the karma-base (pre-augmentation) Body rating, which only survives in
    # chargen_state.base -- a record still missing that snapshot skips this half of the check rather
    # than cap against the wrong (augmented) number.
    chargen_state = submitted.get("chargen_state", char.chargen_state) or {}
    base_body = (chargen_state.get("base") or {}).get("body")
    if base_body is not None:
        body_used = _body_index_used(gear)
        if body_used > float(base_body) + 1e-6:
            raise HTTPException(
                status_code=422,
                detail=f"Gear implies {body_used:.2f} Body Index used, exceeding Body {base_body}.",
            )


def _assert_gear_grades_allowed(char: Character, submitted: dict) -> None:
    """Reject a non-admin's gear PATCH that introduces a GM-gated cyber grade (Beta/Delta) the
    character hasn't been approved for. Defense-in-depth behind the play-sheet gear picker, which
    already greys out ungranted grades -- see openManageBuyGear's gradeBooks in play-sheet.html.
    """
    gear = submitted.get("gear") or {}
    for line in gear.get("cyber") or []:
        grade = line.get("grade") if isinstance(line, dict) else None
        column = _GRADE_APPROVAL_COLUMN.get(grade)
        if column and not getattr(char, column):
            raise HTTPException(
                status_code=403,
                detail=f"{grade}-grade cyberware requires GM approval for this character",
            )


def _is_privileged_view(ctx: dict) -> bool:
    """True only for a real admin NOT previewing runner view -- the full-data audience.

    Players and admins previewing runner view (X-Runner-View) get the redacted payload.
    """
    return bool(ctx.get("is_admin")) and not ctx.get("view_as_player")


def _owns(char: Character, ctx: dict) -> bool:
    """True when the caller's token owns this character (admins included -- no admin bypass)."""
    return bool(char.owner_token and ctx.get("user_token")
                and char.owner_token == hash_token(ctx["user_token"]))


async def _caller_pc_ids(db: AsyncSession, ctx: dict) -> set[int]:
    """IDs of the PCs the caller's token owns (empty for a token that owns none)."""
    if not ctx.get("user_token"):
        return set()
    rows = await db.execute(select(Character.id).where(Character.owner_token == hash_token(ctx["user_token"])))
    return {row[0] for row in rows.all()}


async def _owns_contact_npc(db: AsyncSession, char: Character, ctx: dict) -> bool:
    """True when ``char`` is a chargen-made contact NPC of a runner the caller owns -- that player
    may edit the contact's profile (_PLAYER_CONTACT_FIELDS) and sees its background."""
    if char.is_pc or not char.origin_pc_id:
        return False
    return char.origin_pc_id in await _caller_pc_ids(db, ctx)


# What a player may change on a contact NPC they own: its profile and affiliation. Connection,
# runner links, activity, source adventure, stats and GM notes stay admin-only.
_PLAYER_CONTACT_FIELDS = {
    "name", "title", "archetype", "race", "nationality", "gender", "age",
    "description", "background", "contact_skills", "organization_id", "is_independent",
}


def _serialize_character(char: Character, ctx: dict, contact_owner: bool = False) -> dict:
    """``contact_owner``: the caller owns this contact NPC (_owns_contact_npc), so they see the
    background they write. Its GM notes stay hidden either way."""
    data = CharacterRead.model_validate(char, from_attributes=True).model_dump()
    if _is_privileged_view(ctx):
        return data
    # A PC's notes belong to its player: the owner sees them. NPC notes and other players' PC
    # notes are GM-only.
    pc_owner = char.is_pc and _owns(char, ctx)
    if not pc_owner:
        data["notes"] = None
    # Same for the background a player writes for their own PC -- hiding it from them made the
    # edit form reload empty, and the next save wrote that blank back over the stored text.
    if not data.get("show_background") and not contact_owner and not pc_owner:
        data["background"] = None
    # An inactive org is GM-concealed: don't name it through a member's affiliation.
    if char.organization is not None and char.organization.is_active is False:
        data["organization_id"] = None
        data["organization_name"] = None
        data["is_independent"] = False
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


def _assert_character_access(char: Character, ctx: dict) -> None:
    """Owner-or-admin gate. A hidden draft the caller doesn't own returns 404 so its existence
    stays private; a committed character the caller doesn't own returns 403."""
    if _is_owner_or_admin(char, ctx):
        return
    if char.is_draft:
        raise HTTPException(status_code=404, detail="Character not found")
    raise HTTPException(status_code=403, detail="Admin or character owner required")


def _character_create_data(body: CharacterCreate, ctx: dict) -> dict:
    if ctx["is_admin"]:
        data = body.model_dump()
        data.pop("owner_token", None)
        if data.get("is_pc"):
            data["catalog_scope"] = "core"
        return data

    data = body.model_dump(include=_PLAYER_IDENTITY_FIELDS)
    data["is_pc"] = True
    data["is_independent"] = True  # runners default to Independent (no org) unless a GM sets otherwise
    data["catalog_scope"] = "core"
    data["owner_token"] = hash_token(ctx["user_token"])
    return data


def _strip_gm_dossier_fields(data: dict, ctx: dict) -> dict:
    if not ctx["is_admin"]:
        for key in _DOSSIER_GM_FIELDS:
            data.pop(key, None)
    return data


async def _assert_org_exists(db: AsyncSession, data: dict) -> None:
    """A dangling organization_id would fail the FK on commit (500); reject it up front."""
    org_id = data.get("organization_id")
    if org_id is not None and await db.get(Organization, org_id) is None:
        raise HTTPException(status_code=422, detail=f"Organization {org_id} not found")


def _dossier_create_data(body: CharacterCreate, ctx: dict) -> dict:
    """Chargen commit accepts the full sheet from either an admin or a player.

    Unlike the lightweight create path, a player building their own dossier may set
    every gameplay field (attributes, essence, skills, gear, ...) -- but not the GM-owned
    fields in _DOSSIER_GM_FIELDS, which keep their defaults. The result is a PC owned by
    the committing token (an admin's token counts). Chargen is a trust-the-player tool --
    the GM reviews finished sheets rather than the server enforcing a points budget.
    """
    data = _strip_gm_dossier_fields(body.model_dump(exclude={"contacts"}), ctx)
    data.pop("owner_token", None)
    data["is_pc"] = True
    data["is_independent"] = True  # runners default to Independent (no org) unless a GM sets otherwise
    data["catalog_scope"] = "core"
    # Claim the new PC to the committing token (an admin's token counts) so the builder owns it
    # immediately -- no manual world-state claim needed. Matches claim_character's token semantics.
    if ctx.get("user_token"):
        data["owner_token"] = hash_token(ctx["user_token"])
    return data


# SHIP setting. Chargen contacts are promoted to NPC "persons of interest" (Known Persons).
# When True, those POI keep standing in the registry when the PC that named them is deleted
# (a live world remembers people); set False only for scratch/test cleanup where the POI should
# be removed along with the PC.
_KEEP_CHARGEN_POI_ON_DELETE = True


# Contact types that name an individual (a specific archetype) and so are promoted to an NPC
# "person of interest" in the Known Persons registry. Gangs/Tribes name a group, not a person,
# so they stay contacts on the runner but never spawn an NPC dossier.
_POI_PROMOTED_CONTACT_TYPES = {None, "", "Contact", "Buddy", "Follower"}


async def _create_dossier_contacts(db: AsyncSession, char: Character, contacts) -> None:
    """Create the runner's chargen contacts as Contact rows. Individual contacts (Contact/Buddy/
    Follower) are each linked (npc_id) to a freshly created NPC "person of interest" so they appear
    in the Known Persons registry; Gang/Tribe contacts stay unlinked (npc_id=None) group contacts.

    TESTING vs SHIP: see _KEEP_CHARGEN_POI_ON_DELETE and delete_character. The POI are currently
    removed with the PC (easy cleanup while testing) and will persist independently on ship.
    """
    for c in contacts:
        ctype = getattr(c, "contact_type", None)
        npc_id = None
        if ctype in _POI_PROMOTED_CONTACT_TYPES:
            poi = Character(name=c.name, is_pc=False, archetype=c.profession, connection=c.connection,
                            origin_pc_id=char.id)
            db.add(poi)
            await db.flush()  # assign poi.id for the npc link
            npc_id = poi.id
        db.add(Contact(
            owner_id=char.id, npc_id=npc_id, name=c.name, profession=c.profession,
            contact_type=ctype, connection=c.connection, loyalty=c.loyalty,
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



def _assert_chargen_skills(skills: list | None) -> None:
    """Reject a finished chargen sheet whose skill breaks the SR2 starting-skill rules.

    Skills arrive already split (frontend/shared.js skillParts shape), so the general rating
    must be at least 1 for every skill -- a Concentration needs 2 Skill Points and a
    Specialization 3. A starting skill has at most one of each (SR2 pp.45, 70); more can only
    be bought with Good Karma after chargen.
    """
    bad = []
    for s in skills or []:
        if not isinstance(s, dict):
            continue
        try:
            rating = int(s.get("rating") or 0)
        except (TypeError, ValueError):
            rating = 0
        if rating < 1 or len(s.get("concs") or []) > 1 or len(s.get("specs") or []) > 1:
            bad.append(str(s.get("name") or "?"))
    if bad:
        raise HTTPException(
            status_code=422,
            detail=(
                "Every skill needs a general rating of at least 1 after its Concentration or "
                "Specialization (2 Skill Points to concentrate, 3 to specialize), with at most one "
                "of each at character creation: " + ", ".join(bad)
            ),
        )


_FREE_CHARGEN_CONTACTS = 2
_MAX_CHARGEN_FOLLOWERS = 5


def _assert_chargen_contacts(contacts: list) -> None:
    """Reject a finished chargen sheet that breaks the starting-contact rules (SR2 pp.43-44).

    Every runner starts with two contacts, each with a name and a profession (the builder's
    archetype); one of them may be upgraded to a Buddy, and only one Buddy can be taken at
    creation. More Contacts and Gang/Tribe ties can be bought freely; Followers are capped at
    five, each from a different archetype.
    """
    contacts = contacts or []
    if sum(c.contact_type == "Buddy" for c in contacts) > 1:
        raise HTTPException(status_code=422, detail="Only one Buddy can be taken at character creation")
    followers = [c for c in contacts if c.contact_type == "Follower"]
    if len(followers) > _MAX_CHARGEN_FOLLOWERS:
        raise HTTPException(status_code=422,
                            detail=f"At most {_MAX_CHARGEN_FOLLOWERS} Followers can be taken at character creation")
    archetypes = [(c.profession or "").strip() for c in followers]
    if not all(archetypes) or len(set(archetypes)) < len(archetypes):
        raise HTTPException(status_code=422, detail="Each Follower needs its own archetype -- no two the same")
    picked = sum((c.contact_type or "Contact") in ("Contact", "Buddy") and bool(c.name.strip())
                 and bool((c.profession or "").strip()) for c in contacts)
    if picked < _FREE_CHARGEN_CONTACTS:
        raise HTTPException(
            status_code=422,
            detail=f"Pick your {_FREE_CHARGEN_CONTACTS} contacts, each with a name and archetype -- "
                   "one can be upgraded to a Buddy",
        )

async def _ensure_pc_reputation(db: AsyncSession, char: Character) -> None:
    """Give a live PC the reputation row the run tools assume exists.

    Street cred, notoriety, public awareness and heat are only tracked for runners in play,
    so a draft or an NPC gets nothing. Idempotent, and safe to call on every write path that
    can turn a row into a live PC. Without it a PC created through the API or the builder had
    no row at all, and a reviewed run change against them was reported as an error instead of
    being applied.
    """
    if not char.is_pc or char.is_draft:
        return
    exists = await db.scalar(select(Reputation.id).where(Reputation.character_id == char.id))
    if exists is None:
        db.add(Reputation(character_id=char.id))


async def _apply_dossier(
    db: AsyncSession, char: Character, body: CharacterCreate, ctx: dict, *, keep_draft: bool,
) -> None:
    """Write a chargen sheet onto an existing owned character row.

    Shared by the draft-update, finalize and convert paths. Only the fields the builder sent
    are written, so anything it doesn't carry (portrait, GM approvals, affiliation, ...) keeps
    its stored value; a player can't write _DOSSIER_GM_FIELDS at all. Ownership is never
    reassigned here; ``keep_draft`` controls whether the row stays a draft or becomes real.
    """
    _assert_chargen_grades_allowed(body.gear, ctx["is_admin"])
    data = _strip_gm_dossier_fields(
        body.model_dump(exclude={"contacts", "owner_token"}, exclude_unset=True), ctx)
    await _assert_org_exists(db, data)
    data["is_pc"] = True
    data["catalog_scope"] = "core"
    data["is_draft"] = keep_draft
    for key, value in data.items():
        setattr(char, key, value)

@router.get("/mine")
async def my_character_ids(
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Return IDs of characters owned by the caller's token (``ids``), plus the contact NPCs their
    runners' chargen made (``contact_ids``), which the caller may also edit."""
    ids = await _caller_pc_ids(db, ctx)
    contact_ids = []
    if ids:
        rows = await db.execute(
            select(Character.id).where(Character.is_pc == False, Character.origin_pc_id.in_(ids))  # noqa: E712
        )
        contact_ids = sorted(row[0] for row in rows.all())
    return {"ids": sorted(ids), "contact_ids": contact_ids}


@router.get("/drafts", response_model=list[CharacterRead])
async def my_draft_characters(
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Return the caller's in-progress chargen drafts (admins in admin view see all drafts).

    Drafts are hidden from the normal character list; this is how the builder and the
    Characters page surface a runner's unfinished dossiers so they can be resumed. An admin
    previewing runner view gets only their own, exactly as a player would.
    """
    q = select(Character).options(selectinload(Character.organization)).where(
        Character.is_draft == True  # noqa: E712 -- SQL boolean comparison
    )
    if not _is_privileged_view(ctx):
        q = q.where(Character.owner_token == hash_token(ctx["user_token"]))
    result = await db.execute(q.order_by(Character.updated_at.desc()))
    chars = result.scalars().all()
    drafts = [_serialize_character(char, ctx) for char in chars]
    if _is_privileged_view(ctx):
        # Tell the GM which token owns each draft so orphans can be spotted and reassigned.
        token_ids = dict((await db.execute(select(UserToken.token_hash, UserToken.id))).all())
        for draft, char in zip(drafts, chars):
            draft["owner_token_id"] = token_ids.get(char.owner_token)
    return drafts


@router.get("/{character_id}/chargen-state", response_model=ChargenStateRead)
async def get_chargen_state(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Raw wizard state for resuming a chargen draft losslessly. Owner-or-admin only."""
    char = await _load_character(db, character_id)
    if not _is_owner_or_admin(char, ctx):
        raise HTTPException(status_code=404, detail="Character not found")
    return ChargenStateRead(state=char.chargen_state or {})


@router.get("/{character_id}/deck-builder-state", response_model=DeckBuilderStateRead)
async def get_deck_builder_state(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    char = await _load_character(db, character_id)
    if not char.is_pc:
        raise HTTPException(status_code=400, detail="Deck builder state is only available for PCs")
    _assert_character_access(char, ctx)
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
    _assert_character_access(char, ctx)
    char.deck_builder_state = body.state or {}
    await db.commit()
    await db.refresh(char)
    return DeckBuilderStateRead(state=char.deck_builder_state or {})


@router.get("/", response_model=list[CharacterRead])
async def list_characters(
    is_pc: bool | None = Query(None, description="Filter by PC (true) or NPC (false)"),
    is_active: bool | None = Query(None),
    source_adventure: str | None = Query(None, description="Filter by published-adventure source"),
    ctx: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    q = select(Character).options(selectinload(Character.organization))
    # Chargen drafts are hidden everywhere until the wizard finalizes them.
    q = q.where(Character.is_draft == False)  # noqa: E712 -- SQL boolean comparison
    if not _is_privileged_view(ctx):
        # Inactive NPCs are GM-concealed (e.g. a kidnapped contact); never ship them to players.
        # Inactive PCs stay visible -- players see greyed-out teammates on world-state.
        q = q.where(or_(Character.is_pc == True, Character.is_active == True))  # noqa: E712
    if is_pc is not None:
        q = q.where(Character.is_pc == is_pc)
    if is_active is not None:
        q = q.where(Character.is_active == is_active)
    if source_adventure:
        q = q.where(Character.source_adventure == source_adventure)
    result = await db.execute(q.order_by(Character.name))
    my_pcs = set() if _is_privileged_view(ctx) else await _caller_pc_ids(db, ctx)
    return [_serialize_character(char, ctx, contact_owner=bool(not char.is_pc and char.origin_pc_id in my_pcs))
            for char in result.scalars().all()]


@router.post("/", response_model=CharacterRead, status_code=201)
async def create_character(
    body: CharacterCreate,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    char = Character(**_character_create_data(body, ctx))
    db.add(char)
    await db.flush()
    await _ensure_pc_reputation(db, char)
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
    data = _dossier_create_data(body, ctx)
    if not data.get("is_draft"):
        _assert_chargen_skills(body.skills)
        _assert_chargen_contacts(body.contacts)
    await _assert_org_exists(db, data)
    char = Character(**data)
    if not char.is_draft:
        await _stamp_lifestyle_start(db, char)
    db.add(char)
    await db.flush()
    await _ensure_pc_reputation(db, char)
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
    await _apply_dossier(db, char, body, ctx, keep_draft=True)
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
    _assert_chargen_skills(body.skills)
    _assert_chargen_contacts(body.contacts)
    await _apply_dossier(db, char, body, ctx, keep_draft=False)
    await _stamp_lifestyle_start(db, char)
    await _ensure_pc_reputation(db, char)
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
    _assert_chargen_skills(body.skills)
    _assert_chargen_contacts(body.contacts)
    await _apply_dossier(db, char, body, ctx, keep_draft=False)
    await _stamp_lifestyle_start(db, char)
    await _ensure_pc_reputation(db, char)
    if body.contacts:
        existing = await db.scalar(
            select(func.count()).select_from(Contact).where(Contact.owner_id == char.id)
        )
        if not existing:
            await _create_dossier_contacts(db, char, body.contacts)
    await db.commit()
    await db.refresh(char, attribute_names=["organization"])
    return _serialize_character(char, ctx)


@router.get("/{character_id}", response_model=CharacterRead)
async def get_character(
    character_id: int,
    ctx: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    char = await _load_character(db, character_id)
    # Hidden drafts must not leak (existence or content) to anyone but the owner/admin.
    if char.is_draft and not _is_owner_or_admin(char, ctx):
        raise HTTPException(status_code=404, detail="Character not found")
    # Inactive NPCs are GM-concealed -- hide existence from players (404, not 403).
    if not char.is_pc and char.is_active is False and not _is_privileged_view(ctx):
        raise HTTPException(status_code=404, detail="Character not found")
    return _serialize_character(char, ctx, contact_owner=await _owns_contact_npc(db, char, ctx))


@router.get("/{character_id}/sheet.pdf")
async def character_sheet_pdf(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Generate and download the filled SR2 character sheet PDF for a completed, owned PC.

    Owner-or-admin only; drafts (still in the builder) 404 -- they haven't been published yet.
    """
    char = await _load_character(db, character_id)
    if not char.is_pc:
        raise HTTPException(status_code=400, detail="Character sheets are generated for PCs only")
    if char.is_draft:
        raise HTTPException(status_code=404, detail="Character not found")
    _assert_character_access(char, ctx)

    char_dict = {col.name: getattr(char, col.name) for col in Character.__table__.columns}
    rows = (await db.execute(
        select(Contact).where(Contact.owner_id == char.id, Contact.is_active == True)  # noqa: E712
    )).scalars().all()
    contacts = [
        (c.name, c.profession or "", c.contact_type or contact_type_for_loyalty(c.loyalty or 1))
        for c in rows
    ]
    try:
        from app.services.sheet_pdf import render_character_sheet
        pdf_bytes = render_character_sheet(char_dict, contacts)
    except ImportError:
        raise HTTPException(status_code=503, detail="PDF generation is unavailable on this server")

    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", char.name or "").strip("_") or f"character_{char.id}"
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{safe}_SR2.pdf"'},
    )


_PORTRAIT_CONTENT_TYPES = {"image/png": "png", "image/jpeg": "jpg", "image/webp": "webp"}
_PORTRAIT_MAX_BYTES = 5 * 1024 * 1024  # 5 MB
_PORTRAIT_CHUNK_BYTES = 256 * 1024  # read size for the streamed size-cap check below
_PORTRAIT_PIL_FORMATS = {"png": "PNG", "jpg": "JPEG", "webp": "WEBP"}


@router.post("/{character_id}/portrait", response_model=CharacterRead)
async def upload_character_portrait(
    character_id: int,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Upload/replace a character's portrait image. Owner-or-admin only. Stored on local disk
    under data/uploads/portraits (served via the /uploads static mount in app/main.py)."""
    char = await _load_character(db, character_id)
    _assert_character_access(char, ctx)

    ext = _PORTRAIT_CONTENT_TYPES.get(file.content_type)
    if not ext:
        raise HTTPException(status_code=400, detail="Portrait must be a PNG, JPEG, or WEBP image")

    # Read in bounded chunks so an oversized upload is rejected as soon as the cap is crossed,
    # instead of buffering the entire body first just to measure it.
    chunks = []
    total = 0
    while True:
        chunk = await file.read(_PORTRAIT_CHUNK_BYTES)
        if not chunk:
            break
        total += len(chunk)
        if total > _PORTRAIT_MAX_BYTES:
            raise HTTPException(status_code=400, detail="Portrait image is too large (limit 5MB)")
        chunks.append(chunk)
    data = b"".join(chunks)
    if not data:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")

    # The Content-Type header above is entirely client-supplied and trivially spoofed -- verify
    # the bytes actually decode as an image, and as the SPECIFIC type claimed, before trusting it.
    try:
        img = Image.open(io.BytesIO(data))
        detected_format = img.format
        img.verify()
    except (UnidentifiedImageError, OSError):
        raise HTTPException(status_code=400, detail="File is not a valid image")
    if detected_format != _PORTRAIT_PIL_FORMATS.get(ext):
        raise HTTPException(status_code=400, detail="Image content doesn't match its declared type")

    filename = f"{uuid.uuid4().hex}.{ext}"
    path = os.path.join("data", "uploads", "portraits", filename)
    async with aiofiles.open(path, "wb") as f:
        await f.write(data)

    old_url = char.portrait_url
    char.portrait_url = f"/uploads/portraits/{filename}"
    await db.commit()
    await db.refresh(char)
    await _remove_replaced_portrait(db, old_url)
    return _serialize_character(char, ctx)


# Only files this endpoint wrote (uuid4 hex names) are ever deleted -- portrait_url is otherwise
# free text a GM can set, so it must never be turned into an arbitrary filesystem path.
_UPLOADED_PORTRAIT_RE = re.compile(r"^/uploads/portraits/([0-9a-f]{32}\.(?:png|jpg|webp))$")


async def _remove_replaced_portrait(db: AsyncSession, old_url: str | None) -> None:
    """Delete a replaced portrait file so repeated uploads don't fill the disk, unless another
    character still points at it."""
    match = _UPLOADED_PORTRAIT_RE.match(old_url or "")
    if not match:
        return
    still_used = await db.scalar(
        select(func.count()).select_from(Character).where(Character.portrait_url == old_url)
    )
    if still_used:
        return
    try:
        os.remove(os.path.join("data", "uploads", "portraits", match.group(1)))
    except FileNotFoundError:
        pass


@router.patch("/{character_id}", response_model=CharacterRead)
async def update_character(
    character_id: int,
    body: CharacterUpdate,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    char = await _load_character(db, character_id)
    is_admin = ctx["is_admin"]
    contact_owner = False
    if not _is_owner_or_admin(char, ctx):
        # A hidden draft the caller doesn't own returns 404 so its existence stays private.
        if char.is_draft:
            raise HTTPException(status_code=404, detail="Character not found")
        contact_owner = await _owns_contact_npc(db, char, ctx)
        # A GM-concealed (inactive) contact stays hidden from its owner too, same as on GET.
        if contact_owner and char.is_active is False:
            raise HTTPException(status_code=404, detail="Character not found")
        if not contact_owner:
            raise HTTPException(status_code=403, detail="Admin or character owner required")

    if contact_owner:
        submitted = body.model_dump(exclude_unset=True)
        forbidden = set(submitted.keys()) - _PLAYER_CONTACT_FIELDS
        if forbidden:
            raise HTTPException(status_code=403, detail=f"Players cannot modify: {', '.join(sorted(forbidden))}")
        # Only an org the player can see: a GM-concealed (inactive) one reads as not found.
        org_id = submitted.get("organization_id")
        if org_id is not None:
            org = await db.get(Organization, org_id)
            if org is None or org.is_active is False:
                raise HTTPException(status_code=422, detail=f"Organization {org_id} not found")
    # Non-admins may only update a limited set of fields on their own PC
    elif not is_admin:
        submitted = body.model_dump(exclude_unset=True)
        forbidden = set(submitted.keys()) - _PLAYER_WRITABLE_FIELDS
        if forbidden:
            raise HTTPException(status_code=403, detail=f"Players cannot modify: {', '.join(sorted(forbidden))}")
        if "gear" in submitted or "chargen_state" in submitted:
            _validate_hard_gear_caps(char, submitted)
        if "gear" in submitted:
            _assert_gear_grades_allowed(char, submitted)
    else:
        # The GM grants (or, with null, revokes) a player's right to edit a contact NPC.
        origin_id = body.model_dump(exclude_unset=True).get("origin_pc_id")
        if origin_id is not None:
            origin = await db.get(Character, origin_id)
            if char.is_pc or origin is None or not origin.is_pc:
                raise HTTPException(status_code=422, detail="origin_pc_id must name a runner, on an NPC")

    await apply_update(db, char, body, exclude={"owner_token"}, commit=False)
    # A contact row copies its NPC's name and archetype (as profession) when the link is made --
    # carry a rename/re-archetype through so runners' contact lists don't go stale.
    changed = body.model_dump(exclude_unset=True)
    if not char.is_pc and ({"name", "archetype"} & changed.keys()):
        values = {}
        if "name" in changed:
            values["name"] = char.name
        if "archetype" in changed:
            values["profession"] = char.archetype
        await db.execute(sql_update(Contact).where(Contact.npc_id == char.id).values(**values))
    await _ensure_pc_reputation(db, char)
    await db.commit()
    await db.refresh(char)
    return _serialize_character(char, ctx, contact_owner=contact_owner)


@router.post("/{character_id}/award-karma", response_model=CharacterRead)
async def award_karma(
    character_id: int,
    body: KarmaAward,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Award Karma (SR2 p.190): 1 point in every 10 earned goes to the Karma Pool and the rest to
    Good Karma. Counting against the running total rounds in favor of Good Karma and keeps small
    awards from losing their Pool share. A negative award takes Karma back (a correction): the
    total drops and the Pool loses any point it no longer reaches. Spending Good Karma on skills,
    attributes or spells is a plain good_karma PATCH and never touches the total. Owner-or-admin."""
    char = await _load_character(db, character_id)
    _assert_character_access(char, ctx)
    earned = char.karma_earned or 0
    total = earned + body.karma
    pool_change = total // 10 - earned // 10
    good_change = body.karma - pool_change
    if total < 0 or (char.good_karma or 0) + good_change < 0:
        raise HTTPException(status_code=422, detail="Only unspent awarded Karma can be taken back")
    # Guarded on the total this split was computed from, so two awards at once can't both count it.
    result = await db.execute(
        sql_update(Character).where(Character.id == char.id, Character.karma_earned == earned).values(
            karma_earned=total,
            # A Pool point already donated can't be taken back; the Pool stops at 0.
            karma_pool=func.max(Character.karma_pool + pool_change, 0),
            good_karma=Character.good_karma + good_change,
            version=Character.version + 1,  # keep the optimistic lock honest for concurrent PATCHes
        )
    )
    if result.rowcount != 1:
        raise HTTPException(status_code=409, detail="Karma changed at the same time -- reload and try again")
    await db.commit()
    await db.refresh(char)
    return _serialize_character(char, ctx)


@router.post("/{character_id}/donate-karma", response_model=CharacterRead)
async def donate_karma(
    character_id: int,
    body: KarmaDonation,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Permanently move Karma Pool points to the Team Karma Pool (SR2 p.191). Owner-or-admin;
    at most what the character's Karma Pool holds."""
    char = await _load_character(db, character_id)
    _assert_character_access(char, ctx)
    await get_campaign_state(db)
    result = await db.execute(
        sql_update(Character)
        .where(Character.id == char.id, Character.karma_pool >= body.points)
        .values(karma_pool=Character.karma_pool - body.points, version=Character.version + 1)
    )
    if result.rowcount != 1:
        raise HTTPException(status_code=422, detail="Cannot donate more than the Karma Pool holds")
    await db.execute(
        sql_update(CampaignState).where(CampaignState.id == 1)
        .values(team_karma=CampaignState.team_karma + body.points)
    )
    await db.commit()
    await db.refresh(char)
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
        owns = _is_owner_or_admin(char, ctx)
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
    # Contact NPCs this runner's player could edit go back to GM-only -- SQLite may hand this id to
    # the next character created, whose player must not inherit them.
    await db.execute(
        sql_update(Character).where(Character.origin_pc_id == character_id).values(origin_pc_id=None)
    )
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
async def get_character_contacts(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    result = await db.execute(
        select(Character).options(selectinload(Character.contacts)).where(Character.id == character_id)
    )
    char = result.scalars().first()
    if not char:
        raise HTTPException(status_code=404, detail="Character not found")
    # Hidden drafts must not leak (existence or content) to anyone but the owner/admin -- same gate
    # as get_character.
    if char.is_draft and not _is_owner_or_admin(char, ctx):
        raise HTTPException(status_code=404, detail="Character not found")
    # Inactive NPCs are GM-concealed -- hide existence from players (404, not 403).
    if not char.is_pc and char.is_active is False and not _is_privileged_view(ctx):
        raise HTTPException(status_code=404, detail="Character not found")
    # Same concealment and GM-note redaction as GET /contacts/.
    return [serialize_contact(c, ctx) for c in await visible_contacts(db, char.contacts, ctx)]


@router.get("/{character_id}/reputation", response_model=ReputationRead | None)
async def get_character_reputation(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    char = await get_or_404(db, Character, character_id)
    if char.is_draft and not _is_owner_or_admin(char, ctx):
        raise HTTPException(status_code=404, detail="Character not found")
    if not char.is_pc and char.is_active is False and not _is_privileged_view(ctx):
        raise HTTPException(status_code=404, detail="Character not found")
    result = await db.execute(select(Reputation).where(Reputation.character_id == character_id))
    rep = result.scalars().first()
    if rep is None:
        return None
    data = ReputationRead.model_validate(rep).model_dump()
    if not _is_privileged_view(ctx):
        data["notes"] = None
    return data


# -- Claim / unclaim -----------------------------------------------------------

@router.post("/{character_id}/claim", response_model=CharacterRead)
async def claim_character(
    character_id: int,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    """Player or admin claims a PC by writing their token hash onto it.

    An unfinished chargen draft can't be claimed (even an unowned one) -- it stays private to
    its owner, and a GM moves it with assign-owner instead.
    """
    claim_hash = hash_token(ctx["user_token"])

    result = await db.execute(
        sql_update(Character)
        .where(
            Character.id == character_id,
            Character.is_pc.is_(True),
            (Character.owner_token.is_(None)) | (Character.owner_token == claim_hash),
            (Character.is_draft.is_(False)) | (Character.owner_token == claim_hash),
        )
        .values(owner_token=claim_hash)
    )
    if result.rowcount != 1:
        char = await _load_character(db, character_id)
        if char.is_draft:
            raise HTTPException(status_code=404, detail="Character not found")
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
    """Admin or the owning player can unclaim a committed character.

    A chargen draft can't be unclaimed: an unowned draft can't be claimed back (see
    claim_character), so the player would lose it. A GM moves drafts with assign-owner.
    """
    char = await _load_character(db, character_id)
    if char.is_draft:
        if not _is_owner_or_admin(char, ctx):
            raise HTTPException(status_code=404, detail="Character not found")
        raise HTTPException(status_code=400, detail="A draft can't be unclaimed; a GM can reassign it")
    if not _is_owner_or_admin(char, ctx):
        raise HTTPException(status_code=403, detail="Only the owning player or an admin can unclaim")

    char.owner_token = None
    await db.commit()
    await db.refresh(char, attribute_names=["organization"])
    return _serialize_character(char, ctx)


@router.post("/{character_id}/assign-owner", response_model=CharacterRead)
async def assign_character_owner(
    character_id: int,
    body: CharacterOwnerAssign,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    """GM hands a PC (typically an orphaned chargen draft) to a player token, or unowns it
    when ``token_id`` is null."""
    char = await _load_character(db, character_id)
    if not char.is_pc:
        raise HTTPException(status_code=400, detail="Only PC characters can be assigned")
    if body.token_id is None:
        char.owner_token = None
    else:
        ut = (await db.execute(select(UserToken).where(UserToken.id == body.token_id))).scalars().first()
        if not ut:
            raise HTTPException(status_code=404, detail="Token not found")
        char.owner_token = ut.token_hash
    await db.commit()
    await db.refresh(char, attribute_names=["organization"])
    data = _serialize_character(char, {"is_admin": True})
    data["owner_token_id"] = body.token_id
    return data
