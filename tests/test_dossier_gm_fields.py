"""Chargen dossier commits can't write GM-only fields, and converting keeps what the builder
doesn't send. Also: a PC's notes are visible to its owner, and a hidden org isn't named through
a member's affiliation.

Throwaway aiosqlite DB, router functions called directly (same pattern as
tests/test_draft_ownership.py).
"""
import asyncio
from contextlib import asynccontextmanager

import pytest
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.auth.core import hash_token
from app.db.base import Base
from app.models.character import Character
from app.models.organization import Organization
from app.routers.characters import (
    convert_character_dossier,
    create_character_dossier,
    get_character,
    list_characters,
)
from app.schemas.character import DossierCommit


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


# A finished sheet needs its starting Contact and Buddy (tests/test_chargen_contacts.py, which imports from here).
_STARTING_CONTACTS = [{"name": "Fixer Joe", "profession": "Fixer"},
                      {"name": "Doc Wagon", "profession": "Street Doc", "contact_type": "Buddy", "loyalty": 3}]

PLAYER = {"is_admin": False, "is_user": True, "user_token": "runner", "view_as_player": False}
OTHER = {"is_admin": False, "is_user": True, "user_token": "someone-else", "view_as_player": False}
ADMIN = {"is_admin": True, "is_user": True, "user_token": "gm", "view_as_player": False}


async def _seed(sessions):
    async with sessions() as db:
        db.add_all([
            Organization(id=1, name="Open Corp", is_active=True),
            Organization(id=2, name="Secret Cabal", is_active=False),
            Character(
                id=10, name="Wraith", is_pc=True, owner_token=hash_token("runner"),
                organization_id=1, portrait_url="/uploads/portraits/w.png", show_background=True,
                delta_grade_approved=True, source_adventure="Queen Euphoria", notes="Next mods: smartlink",
                math_spu_enabled=True, math_spu_rating=2,
            ),
            Character(id=11, name="Mole", is_pc=False, organization_id=2, notes="GM secret"),
        ])
        await db.commit()


def test_player_dossier_cannot_set_gm_fields(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            body = DossierCommit(
                name="Chancer", beta_grade_approved=True, delta_grade_approved=True,
                organization_id=2, show_background=True, portrait_url="/x.png",
                source_adventure="Mercurial", contact_skills=["Etiquette"], contacts=_STARTING_CONTACTS,
            )
            async with sessions() as db:
                out = await create_character_dossier(body=body, db=db, ctx=PLAYER)
            assert out["organization_name"] is None  # no hidden-org name comes back
            async with sessions() as db:
                char = await db.get(Character, out["id"])
                assert char.beta_grade_approved is False
                assert char.delta_grade_approved is False
                assert char.organization_id is None
                assert char.show_background is False
                assert char.portrait_url is None
                assert char.source_adventure is None
                assert char.contact_skills == []

    asyncio.run(scenario())


def test_player_convert_keeps_gm_fields_and_unsent_values(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            # What the builder sends: sheet fields, no GM fields, no Math SPU columns.
            body = DossierCommit(name="Wraith II", strength=5, notes="Next mods: smartlink",
                                 delta_grade_approved=False, organization_id=None, contacts=_STARTING_CONTACTS)
            async with sessions() as db:
                await convert_character_dossier(character_id=10, body=body, db=db, ctx=PLAYER)
            async with sessions() as db:
                char = await db.get(Character, 10)
                assert char.name == "Wraith II" and char.strength == 5
                assert char.delta_grade_approved is True      # player can't revoke/grant approvals
                assert char.organization_id == 1              # affiliation untouched
                assert char.portrait_url == "/uploads/portraits/w.png"
                assert char.show_background is True
                assert char.source_adventure == "Queen Euphoria"
                assert char.math_spu_enabled is True and char.math_spu_rating == 2  # not sent -> kept

    asyncio.run(scenario())


def test_dossier_rejects_missing_org_for_admin(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await create_character_dossier(
                        body=DossierCommit(name="Ghost", organization_id=999), db=db, ctx=ADMIN)
            assert exc.value.status_code == 422

    asyncio.run(scenario())


def test_pc_notes_visible_to_owner_only(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                assert (await get_character(character_id=10, ctx=PLAYER, db=db))["notes"] == "Next mods: smartlink"
            async with sessions() as db:
                assert (await get_character(character_id=10, ctx=OTHER, db=db))["notes"] is None
            async with sessions() as db:
                assert (await get_character(character_id=10, ctx=ADMIN, db=db))["notes"] == "Next mods: smartlink"

    asyncio.run(scenario())


def test_hidden_org_not_named_through_member(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                rows = await list_characters(is_pc=None, is_active=None, source_adventure=None, ctx=PLAYER, db=db)
            mole = next(r for r in rows if r["id"] == 11)
            assert mole["organization_id"] is None and mole["organization_name"] is None
            assert mole["notes"] is None
            wraith = next(r for r in rows if r["id"] == 10)
            assert wraith["organization_name"] == "Open Corp"
            async with sessions() as db:
                rows = await list_characters(is_pc=None, is_active=None, source_adventure=None, ctx=ADMIN, db=db)
            assert next(r for r in rows if r["id"] == 11)["organization_name"] == "Secret Cabal"

    asyncio.run(scenario())
