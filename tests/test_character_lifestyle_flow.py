"""Integration tests for the lifestyle settle flow and the drafts/convert endpoints.

Uses a throwaway aiosqlite DB and calls the router/service functions directly (the
same pattern as tests/test_atomic_world_writes.py) -- no HTTP layer.
"""
import asyncio
from contextlib import asynccontextmanager

import pytest
from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.auth.core import hash_token
from app.db.base import Base
from app.models.character import Character
from app.models.contact import Contact
from app.routers.characters import (
    convert_character_dossier,
    create_character_dossier,
    delete_character,
    my_draft_characters,
)
from app.schemas.character import DossierCommit
from app.services.lifestyle import settle_all_lifestyles


@asynccontextmanager
async def _database(path):
    engine = create_async_engine(
        f"sqlite+aiosqlite:///{path.as_posix()}", connect_args={"timeout": 5}
    )
    sessions = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.exec_driver_sql("PRAGMA journal_mode=WAL")
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield sessions
    finally:
        await engine.dispose()


def test_settle_all_lifestyles_charges_and_evicts(tmp_path):
    async def scenario():
        async with _database(tmp_path / "life.db") as sessions:
            async with sessions() as db:
                db.add(Character(name="Payer", is_pc=True, lifestyle_level=3, nuyen=12000, lifestyle_paid_tick=0))
                db.add(Character(name="Broke", is_pc=True, lifestyle_level=3, nuyen=0, lifestyle_paid_tick=0))
                await db.commit()

            async with sessions() as db:
                assert await settle_all_lifestyles(db, 60) == 2  # two months elapsed

            async with sessions() as db:
                payer = await db.scalar(select(Character).where(Character.name == "Payer"))
                broke = await db.scalar(select(Character).where(Character.name == "Broke"))
                # Payer: Middle 5000/mo x 2 = 10000 charged.
                assert payer.nuyen == 2000 and payer.lifestyle_paid_tick == 60
                # Broke: evicted twice (Middle -> Low -> Squatter), never charged.
                assert broke.lifestyle_level == 1 and broke.nuyen == 0 and broke.lifestyle_paid_tick == 60

    asyncio.run(scenario())


def test_drafts_endpoint_scopes_to_caller(tmp_path):
    async def scenario():
        async with _database(tmp_path / "drafts.db") as sessions:
            tok = "player-1"
            async with sessions() as db:
                db.add(Character(name="MyDraft", is_pc=True, is_draft=True, owner_token=hash_token(tok)))
                db.add(Character(name="MyFinal", is_pc=True, is_draft=False, owner_token=hash_token(tok)))
                db.add(Character(name="OtherDraft", is_pc=True, is_draft=True, owner_token=hash_token("player-2")))
                await db.commit()

            async with sessions() as db:
                mine = await my_draft_characters(db=db, ctx={"is_admin": False, "user_token": tok})
                assert {r["name"] for r in mine} == {"MyDraft"}

            async with sessions() as db:
                all_drafts = await my_draft_characters(db=db, ctx={"is_admin": True, "user_token": "admin"})
                assert {r["name"] for r in all_drafts} == {"MyDraft", "OtherDraft"}

    asyncio.run(scenario())


def test_convert_dossier_overwrites_in_place_and_stamps_lifestyle(tmp_path):
    async def scenario():
        async with _database(tmp_path / "conv.db") as sessions:
            tok = "owner-x"
            async with sessions() as db:
                db.add(Character(name="OldPC", is_pc=True, is_draft=False, owner_token=hash_token(tok), body=1))
                await db.commit()
                cid = await db.scalar(select(Character.id).where(Character.name == "OldPC"))

            body = DossierCommit(
                name="NewSheet", body=5, strength=4, lifestyle_level=2,
                contacts=[{"name": "Fixer Joe", "loyalty": 3}],
            )
            async with sessions() as db:
                res = await convert_character_dossier(cid, body, db=db, ctx={"is_admin": False, "user_token": tok})
                assert res["name"] == "NewSheet"

            async with sessions() as db:
                pc = await db.scalar(select(Character).where(Character.id == cid))
                assert pc.name == "NewSheet" and pc.body == 5 and pc.is_draft is False
                assert pc.lifestyle_level == 2 and pc.lifestyle_paid_tick is not None
                contacts = await db.scalar(
                    select(func.count()).select_from(Contact).where(Contact.owner_id == cid)
                )
                assert contacts == 1

    asyncio.run(scenario())

    async def scenario_no_dupe():
        async with _database(tmp_path / "conv2.db") as sessions:
            tok = "owner-y"
            async with sessions() as db:
                db.add(Character(name="HasContacts", is_pc=True, is_draft=False, owner_token=hash_token(tok)))
                await db.commit()
                cid = await db.scalar(select(Character.id).where(Character.name == "HasContacts"))
                db.add(Contact(owner_id=cid, name="Existing", connection=1, loyalty=1))
                await db.commit()

            body = DossierCommit(name="HasContacts", contacts=[{"name": "New One", "loyalty": 3}])
            async with sessions() as db:
                await convert_character_dossier(cid, body, db=db, ctx={"is_admin": True, "user_token": "admin"})

            async with sessions() as db:
                # A character that already had contacts is not given duplicates on convert.
                contacts = await db.scalar(
                    select(func.count()).select_from(Contact).where(Contact.owner_id == cid)
                )
                assert contacts == 1

    asyncio.run(scenario_no_dupe())


def test_player_can_delete_own_draft_but_not_committed(tmp_path):
    async def scenario():
        async with _database(tmp_path / "del.db") as sessions:
            tok = "p1"
            async with sessions() as db:
                db.add(Character(name="Draft", is_pc=True, is_draft=True, owner_token=hash_token(tok)))
                db.add(Character(name="Committed", is_pc=True, is_draft=False, owner_token=hash_token(tok)))
                db.add(Character(name="OtherDraft", is_pc=True, is_draft=True, owner_token=hash_token("p2")))
                await db.commit()
                draft_id = await db.scalar(select(Character.id).where(Character.name == "Draft"))
                committed_id = await db.scalar(select(Character.id).where(Character.name == "Committed"))
                other_id = await db.scalar(select(Character.id).where(Character.name == "OtherDraft"))

            player = {"is_admin": False, "user_token": tok}

            # Player deletes their own draft -> succeeds.
            async with sessions() as db:
                await delete_character(draft_id, db=db, ctx=player)
            async with sessions() as db:
                assert await db.scalar(select(func.count()).select_from(Character).where(Character.id == draft_id)) == 0

            # Player cannot delete their own committed PC -> 403 (GM required).
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await delete_character(committed_id, db=db, ctx=player)
                assert exc.value.status_code == 403

            # Player cannot delete someone else's hidden draft -> 404 (existence stays private).
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await delete_character(other_id, db=db, ctx=player)
                assert exc.value.status_code == 404

    asyncio.run(scenario())


def test_chargen_contacts_become_poi_and_persist_after_pc_delete(tmp_path):
    async def scenario():
        async with _database(tmp_path / "poi.db") as sessions:
            admin = {"is_admin": True, "user_token": "admin"}
            body = DossierCommit(
                name="Runner",
                contacts=[{"name": "Fixer Joe", "profession": "Fixer", "loyalty": 3}],
            )
            async with sessions() as db:
                res = await create_character_dossier(body, db=db, ctx=admin)
                pid = res["id"]

            async with sessions() as db:
                # The chargen contact became a linked NPC person of interest.
                ct = (await db.execute(select(Contact).where(Contact.owner_id == pid))).scalars().first()
                assert ct is not None and ct.npc_id is not None
                poi = await db.get(Character, ct.npc_id)
                assert poi is not None and poi.is_pc is False and poi.name == "Fixer Joe"
                poi_id = poi.id

            # SHIP behavior (_KEEP_CHARGEN_POI_ON_DELETE=True): deleting the PC removes its own
            # Contact rows but leaves the POI standing in the Known-Persons registry.
            async with sessions() as db:
                await delete_character(pid, db=db, ctx=admin)

            async with sessions() as db:
                assert await db.scalar(select(func.count()).select_from(Character).where(Character.id == pid)) == 0
                assert await db.scalar(select(func.count()).select_from(Character).where(Character.id == poi_id)) == 1
                assert await db.scalar(select(func.count()).select_from(Contact).where(Contact.owner_id == pid)) == 0

    asyncio.run(scenario())


def test_chargen_pc_defaults_to_independent(tmp_path):
    async def scenario():
        async with _database(tmp_path / "indep.db") as sessions:
            admin = {"is_admin": True, "user_token": "admin"}
            async with sessions() as db:
                res = await create_character_dossier(DossierCommit(name="Runner"), db=db, ctx=admin)
                # Runners default to Independent affiliation (not Unknown) at creation.
                assert res["is_independent"] is True

    asyncio.run(scenario())


def test_chargen_gang_tribe_contacts_stay_unlinked(tmp_path):
    async def scenario():
        async with _database(tmp_path / "gang.db") as sessions:
            admin = {"is_admin": True, "user_token": "admin"}
            body = DossierCommit(
                name="Runner",
                contacts=[
                    {"name": "Fixer Joe", "profession": "Fixer", "contact_type": "Contact", "loyalty": 2},
                    {"name": "Ancients", "profession": None, "contact_type": "Gang", "loyalty": 1},
                    {"name": "Sinsearach", "profession": None, "contact_type": "Tribe", "loyalty": 1},
                ],
            )
            async with sessions() as db:
                res = await create_character_dossier(body, db=db, ctx=admin)
                pid = res["id"]

            async with sessions() as db:
                contacts = (await db.execute(
                    select(Contact).where(Contact.owner_id == pid).order_by(Contact.name)
                )).scalars().all()
                by_name = {c.name: c for c in contacts}
                # All three are contacts on the runner...
                assert set(by_name) == {"Ancients", "Fixer Joe", "Sinsearach"}
                # ...but only the individual (Contact) becomes a Known-Persons NPC dossier.
                assert by_name["Fixer Joe"].npc_id is not None
                assert by_name["Ancients"].npc_id is None
                assert by_name["Sinsearach"].npc_id is None
                # No NPC row was spawned for the gang or the tribe.
                npc_names = set((await db.execute(
                    select(Character.name).where(Character.is_pc == False)  # noqa: E712
                )).scalars().all())
                assert "Ancients" not in npc_names and "Sinsearach" not in npc_names
                assert "Fixer Joe" in npc_names

    asyncio.run(scenario())
