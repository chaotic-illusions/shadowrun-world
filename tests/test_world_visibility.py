"""Server-side concealment of inactive NPCs and contacts (world-state reveal control).

Marking an NPC or a contact inactive (e.g. a kidnapped fixer whose services are offline) must
remove it from the shared API payload for players AND for an admin previewing runner view --
concealment cannot be client-side only, or a player reads it straight out of DevTools. Admins in
their own (non-preview) view still see the full roster so they can toggle relevance at any time.

Same throwaway-DB pattern as tests/test_character_permissions.py: the real router functions are
called directly (FastAPI dependency injection is just Python here).
"""

import asyncio
from contextlib import asynccontextmanager

import pytest
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.db.base import Base
from app.models.character import Character
from app.models.contact import Contact
from app.routers.characters import list_characters, get_character
from app.routers.contacts import list_contacts


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


_ADMIN = {"is_admin": True, "is_user": True, "user_token": "admin", "view_as_player": False}
_ADMIN_PREVIEW = {"is_admin": True, "is_user": True, "user_token": "admin", "view_as_player": True}
_PLAYER = {"is_admin": False, "is_user": True, "user_token": "runner", "view_as_player": False}


def _names(rows):
    return {r["name"] for r in rows}


def test_inactive_npc_hidden_from_players_and_preview_but_visible_to_admin(tmp_path):
    async def scenario():
        async with _database(tmp_path / "npc_vis.db") as sessions:
            async with sessions() as db:
                db.add_all([
                    Character(name="Active NPC", is_pc=False, is_active=True),
                    Character(name="Kidnapped NPC", is_pc=False, is_active=False),
                    Character(name="Benched PC", is_pc=True, is_active=False),
                ])
                await db.commit()

            async with sessions() as db:
                admin = _names(await list_characters(None, None, _ADMIN, db))
            async with sessions() as db:
                player = _names(await list_characters(None, None, _PLAYER, db))
            async with sessions() as db:
                preview = _names(await list_characters(None, None, _ADMIN_PREVIEW, db))
            return admin, player, preview

    admin, player, preview = asyncio.run(scenario())

    # Admin sees the whole roster.
    assert {"Active NPC", "Kidnapped NPC", "Benched PC"} <= admin
    # Player: inactive NPC concealed, but an inactive PC (greyed-out teammate) still shows.
    assert "Kidnapped NPC" not in player
    assert {"Active NPC", "Benched PC"} <= player
    # Admin previewing runner view sees exactly what the player sees.
    assert "Kidnapped NPC" not in preview
    assert {"Active NPC", "Benched PC"} <= preview


def test_get_inactive_npc_returns_404_for_player(tmp_path):
    async def scenario():
        async with _database(tmp_path / "npc_get.db") as sessions:
            async with sessions() as db:
                npc = Character(name="Kidnapped NPC", is_pc=False, is_active=False)
                db.add(npc)
                await db.commit()
                npc_id = npc.id

            async with sessions() as db:
                admin_row = await get_character(npc_id, _ADMIN, db)
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await get_character(npc_id, _PLAYER, db)
            return admin_row["name"], exc.value.status_code

    name, status = asyncio.run(scenario())
    assert name == "Kidnapped NPC"
    assert status == 404  # hide existence, not 403


def test_inactive_contacts_hidden_from_players(tmp_path):
    async def scenario():
        async with _database(tmp_path / "contact_vis.db") as sessions:
            async with sessions() as db:
                owner = Character(name="Runner", is_pc=True, is_active=True)
                active_npc = Character(name="Active Fixer NPC", is_pc=False, is_active=True)
                inactive_npc = Character(name="Kidnapped Fixer NPC", is_pc=False, is_active=False)
                db.add_all([owner, active_npc, inactive_npc])
                await db.commit()
                db.add_all([
                    Contact(name="Active Standalone", owner_id=owner.id, is_active=True),
                    Contact(name="Inactive Standalone", owner_id=owner.id, is_active=False),
                    Contact(name="Via Active NPC", owner_id=owner.id, npc_id=active_npc.id, is_active=True),
                    # Contact row is active, but the linked NPC is inactive -> still concealed.
                    Contact(name="Via Kidnapped NPC", owner_id=owner.id, npc_id=inactive_npc.id, is_active=True),
                ])
                await db.commit()

            async with sessions() as db:
                admin = _names(await list_contacts(None, None, _ADMIN, db))
            async with sessions() as db:
                player = _names(await list_contacts(None, None, _PLAYER, db))
            return admin, player

    admin, player = asyncio.run(scenario())

    assert {"Active Standalone", "Inactive Standalone", "Via Active NPC", "Via Kidnapped NPC"} <= admin
    assert {"Active Standalone", "Via Active NPC"} <= player
    assert "Inactive Standalone" not in player   # contact row inactive
    assert "Via Kidnapped NPC" not in player     # linked NPC inactive
