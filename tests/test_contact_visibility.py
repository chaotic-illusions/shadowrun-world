"""Every contact read path hides GM notes and GM-concealed contacts from players the same way
GET /contacts/ does: /characters/{id}/contacts and /contacts/{id} included.
"""
import asyncio
from contextlib import asynccontextmanager

import pytest
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.auth.core import hash_token
from app.db.base import Base
from app.models.character import Character
from app.models.contact import Contact
from app.routers.characters import get_character_contacts
from app.routers.contacts import get_contact, list_contacts


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


PLAYER = {"is_admin": False, "is_user": True, "user_token": "runner", "view_as_player": False}
ADMIN = {"is_admin": True, "is_user": True, "user_token": "gm", "view_as_player": False}


async def _seed(sessions):
    async with sessions() as db:
        db.add_all([
            Character(id=1, name="Runner", is_pc=True, owner_token=hash_token("runner")),
            Character(id=2, name="Kidnapped Fixer", is_pc=False, is_active=False),
            Character(id=3, name="Hidden Boss", is_pc=False, is_active=False),
            Contact(id=10, owner_id=1, name="Open", notes="GM: is an informant"),
            Contact(id=11, owner_id=1, name="Retired", is_active=False),
            Contact(id=12, owner_id=1, name="Fixer", npc_id=2),
            Contact(id=13, owner_id=3, name="Boss's man"),
        ])
        await db.commit()


def test_character_contacts_match_list_contacts_for_players(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                via_char = await get_character_contacts(character_id=1, db=db, ctx=PLAYER)
            async with sessions() as db:
                via_list = await list_contacts(owner_id=1, organization_id=None, ctx=PLAYER, db=db)
            assert [c["id"] for c in via_char] == [10]
            assert via_char == via_list
            assert via_char[0]["notes"] is None
            async with sessions() as db:
                admin = await get_character_contacts(character_id=1, db=db, ctx=ADMIN)
            assert {c["id"] for c in admin} == {10, 11, 12}
            assert next(c for c in admin if c["id"] == 10)["notes"] == "GM: is an informant"

    asyncio.run(scenario())


def test_inactive_npc_contacts_404_for_players(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await get_character_contacts(character_id=3, db=db, ctx=PLAYER)
            assert exc.value.status_code == 404
            async with sessions() as db:
                assert len(await get_character_contacts(character_id=3, db=db, ctx=ADMIN)) == 1

    asyncio.run(scenario())


@pytest.mark.parametrize("contact_id", [11, 12])
def test_get_contact_hides_concealed_contacts(tmp_path, contact_id):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await get_contact(contact_id=contact_id, ctx=PLAYER, db=db)
            assert exc.value.status_code == 404
            async with sessions() as db:
                assert (await get_contact(contact_id=contact_id, ctx=ADMIN, db=db))["id"] == contact_id

    asyncio.run(scenario())
