"""Players edit the contact NPCs their runners made at chargen (Character.origin_pc_id).

Calls the real router functions against a throwaway DB, same pattern as
tests/test_character_permissions.py.
"""

import asyncio
from contextlib import asynccontextmanager
from types import SimpleNamespace

import pytest
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.auth.core import hash_token
from app.db.base import Base
from app.models.character import Character
from app.models.contact import Contact
from app.models.organization import Organization
from app.routers.contacts import create_contact, update_contact
from app.routers.characters import (
    _create_dossier_contacts,
    get_character,
    list_characters,
    my_character_ids,
    update_character,
)
from app.schemas.character import CharacterUpdate
from app.schemas.contact import ContactCreate, ContactUpdate


@asynccontextmanager
async def _database(path):
    engine = create_async_engine(f"sqlite+aiosqlite:///{path.as_posix()}", connect_args={"timeout": 5})
    sessions = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield sessions
    finally:
        await engine.dispose()


def _ctx(token, admin=False):
    return {"is_admin": admin, "is_user": not admin, "user_token": token, "view_as_player": False}


COLE, OTHER = _ctx("cole-token"), _ctx("other-token")


async def _seed(db):
    """Leadbelly (Cole's runner) made Chopper at chargen; Patch is a GM NPC; Rook is another
    player's runner."""
    leadbelly = Character(name="Leadbelly", is_pc=True, owner_token=hash_token("cole-token"))
    rook = Character(name="Rook", is_pc=True, owner_token=hash_token("other-token"))
    db.add_all([leadbelly, rook])
    await db.flush()
    chopper = Character(name="Chopper", is_pc=False, title="Chop Shop Owner", archetype="Chop Shop Owner",
                        background="Owes the Ancients.", notes="GM: informant for Lone Star.",
                        origin_pc_id=leadbelly.id)
    patch = Character(name="Patch", is_pc=False, title="Street Doc")
    db.add_all([chopper, patch])
    await db.flush()
    db.add(Contact(owner_id=leadbelly.id, npc_id=chopper.id, name="Chopper", profession="Chop Shop Owner",
                   contact_type="Contact", loyalty=1))
    await db.commit()
    return SimpleNamespace(leadbelly=leadbelly.id, rook=rook.id, chopper=chopper.id, patch=patch.id)


def _run(tmp_path, name, scenario):
    async def go():
        async with _database(tmp_path / f"{name}.db") as sessions:
            async with sessions() as db:
                ids = await _seed(db)
            async with sessions() as db:
                await scenario(db, ids)
    asyncio.run(go())


def test_owner_edits_contact_profile_and_rename_reaches_contact_list(tmp_path):
    async def scenario(db, ids):
        body = CharacterUpdate(name="Chopper Reyes", archetype="Fixer", background="Ex-Ancient.",
                               contact_skills=["Fence -- Stolen Vehicles"])
        result = await update_character(ids.chopper, body, db, COLE)
        assert result["name"] == "Chopper Reyes"
        assert result["background"] == "Ex-Ancient."      # owner sees the background they write
        assert result["notes"] is None                      # GM notes stay hidden
        contact = (await db.execute(select(Contact).where(Contact.npc_id == ids.chopper))).scalar_one()
        assert (contact.name, contact.profession) == ("Chopper Reyes", "Fixer")
        npc = await db.get(Character, ids.chopper)
        assert npc.notes == "GM: informant for Lone Star."   # untouched
    _run(tmp_path, "owner_edit", scenario)


@pytest.mark.parametrize("field,value", [
    ("connection", 4), ("is_active", False), ("notes", "x"),
    ("source_adventure", "Silver Angel"), ("is_pc", True), ("body", 6),
])
def test_owner_cannot_touch_gm_fields(tmp_path, field, value):
    async def scenario(db, ids):
        with pytest.raises(HTTPException) as exc:
            await update_character(ids.chopper, CharacterUpdate(**{field: value}), db, COLE)
        assert exc.value.status_code == 403
    _run(tmp_path, f"gm_field_{field}", scenario)


def test_other_players_and_other_npcs_are_off_limits(tmp_path):
    async def scenario(db, ids):
        with pytest.raises(HTTPException) as exc:
            await update_character(ids.chopper, CharacterUpdate(name="Mine now"), db, OTHER)
        assert exc.value.status_code == 403
        with pytest.raises(HTTPException) as exc:
            await update_character(ids.patch, CharacterUpdate(name="Patchy"), db, COLE)
        assert exc.value.status_code == 403
    _run(tmp_path, "off_limits", scenario)


def test_inactive_contact_is_hidden_from_its_owner(tmp_path):
    async def scenario(db, ids):
        npc = await db.get(Character, ids.chopper)
        npc.is_active = False
        await db.commit()
        with pytest.raises(HTTPException) as exc:
            await update_character(ids.chopper, CharacterUpdate(name="x"), db, COLE)
        assert exc.value.status_code == 404
    _run(tmp_path, "inactive", scenario)


def test_admin_keeps_full_control(tmp_path):
    async def scenario(db, ids):
        result = await update_character(ids.chopper, CharacterUpdate(connection=4, notes="new"), db,
                                        _ctx(None, admin=True))
        assert (result["connection"], result["notes"]) == (4, "new")
    _run(tmp_path, "admin", scenario)


def test_mine_lists_contacts_and_reads_show_owner_the_background(tmp_path):
    async def scenario(db, ids):
        assert await my_character_ids(db=db, ctx=COLE) == {"ids": [ids.leadbelly], "contact_ids": [ids.chopper]}
        assert await my_character_ids(db=db, ctx=OTHER) == {"ids": [ids.rook], "contact_ids": []}
        assert (await get_character(ids.chopper, ctx=COLE, db=db))["background"] == "Owes the Ancients."
        assert (await get_character(ids.chopper, ctx=OTHER, db=db))["background"] is None
        listed = {c["id"]: c for c in await list_characters(None, None, None, ctx=COLE, db=db)}
        assert listed[ids.chopper]["background"] == "Owes the Ancients."
        assert listed[ids.chopper]["origin_pc_id"] == ids.leadbelly
    _run(tmp_path, "reads", scenario)


def test_chargen_contacts_record_their_runner(tmp_path):
    async def scenario(db, ids):
        runner = await db.get(Character, ids.rook)
        contacts = [SimpleNamespace(name="Tittle", profession="Bartender", contact_type="Buddy", connection=1, loyalty=3),
                    SimpleNamespace(name="Ancients", profession=None, contact_type="Gang", connection=1, loyalty=1)]
        await _create_dossier_contacts(db, runner, contacts)
        await db.commit()
        npcs = (await db.execute(select(Character).where(Character.name == "Tittle"))).scalars().all()
        assert [n.origin_pc_id for n in npcs] == [ids.rook]
        assert (await db.execute(select(Character).where(Character.name == "Ancients"))).first() is None
    _run(tmp_path, "chargen", scenario)


def test_owner_sets_affiliation_to_a_visible_org_only(tmp_path):
    async def scenario(db, ids):
        ancients = Organization(name="Ancients")
        hidden = Organization(name="Shadow Cabal", is_active=False)
        db.add_all([ancients, hidden])
        await db.commit()
        result = await update_character(ids.chopper, CharacterUpdate(organization_id=ancients.id), db, COLE)
        assert result["organization_id"] == ancients.id
        with pytest.raises(HTTPException) as exc:
            await update_character(ids.chopper, CharacterUpdate(organization_id=hidden.id), db, COLE)
        assert exc.value.status_code == 422
    _run(tmp_path, "affiliation", scenario)


@pytest.mark.parametrize("loyalty,expected", [(1, "Contact"), (2, "Contact"), (3, "Buddy"), (5, "Buddy"), (6, "Follower")])
def test_loyalty_sets_contact_type(tmp_path, loyalty, expected):
    async def scenario(db, ids):
        contact = (await db.execute(select(Contact).where(Contact.npc_id == ids.chopper))).scalar_one()
        updated = await update_contact(contact.id, ContactUpdate(loyalty=loyalty), db, "admin")
        assert updated.contact_type == expected
    _run(tmp_path, f"loyalty_{loyalty}", scenario)


def test_explicit_type_and_org_ties_are_not_rederived(tmp_path):
    async def scenario(db, ids):
        contact = (await db.execute(select(Contact).where(Contact.npc_id == ids.chopper))).scalar_one()
        # A request that sets both (the play sheet's Contact/Buddy toggle) keeps its own type.
        updated = await update_contact(contact.id, ContactUpdate(contact_type="Contact", loyalty=4), db, "admin")
        assert (updated.contact_type, updated.loyalty) == ("Contact", 4)
        gang = Contact(owner_id=ids.rook, name="Ancients", contact_type="Gang", loyalty=1)
        db.add(gang)
        await db.commit()
        assert (await update_contact(gang.id, ContactUpdate(loyalty=6), db, "admin")).contact_type == "Gang"
        # Linking a runner without a type takes it from the Loyalty picked.
        linked = await create_contact(ContactCreate(name="Patch", owner_id=ids.rook, npc_id=ids.patch, loyalty=3), db, "admin")
        assert linked.contact_type == "Buddy"
    _run(tmp_path, "explicit_type", scenario)
