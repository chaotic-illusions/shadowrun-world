"""Draft ownership survives token churn: revoke-with-transfer, GM assign-owner, and drafts
can't be claimed out from under their owner.

Throwaway aiosqlite DB, router functions called directly (same pattern as
tests/test_character_lifestyle_flow.py).
"""
import asyncio
from contextlib import asynccontextmanager

import pytest
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.auth.core import hash_token
from app.db.base import Base
from app.models.auth import UserToken
from app.models.character import Character
from app.models.matrix_run import MatrixRun
from app.routers.auth import revoke_token
from app.routers.characters import (
    assign_character_owner, claim_character, my_draft_characters, unclaim_character,
)
from app.schemas.character import CharacterOwnerAssign


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


OLD, NEW = "old-token", "new-token"


async def _seed(sessions):
    """Two player tokens; OLD owns a draft, a finished PC and a matrix run."""
    async with sessions() as db:
        db.add_all([
            UserToken(id=1, token_hash=hash_token(OLD), label="Sam (old)"),
            UserToken(id=2, token_hash=hash_token(NEW), label="Sam (new)"),
            Character(id=10, name="Draft", is_pc=True, is_draft=True, owner_token=hash_token(OLD)),
            Character(id=11, name="Final", is_pc=True, owner_token=hash_token(OLD)),
            MatrixRun(id=20, owner_token_hash=hash_token(OLD)),
        ])
        await db.commit()


def test_revoke_with_transfer_moves_drafts_characters_and_runs(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                await revoke_token(token_id=1, transfer_to=2, db=db, _="admin")
            async with sessions() as db:
                chars = (await db.execute(select(Character))).scalars().all()
                assert {c.owner_token for c in chars} == {hash_token(NEW)}
                run = await db.get(MatrixRun, 20)
                assert run.owner_token_hash == hash_token(NEW)
                assert await db.get(UserToken, 1) is None
                mine = await my_draft_characters(db=db, ctx={"is_admin": False, "user_token": NEW})
                assert [d["name"] for d in mine] == ["Draft"]

    asyncio.run(scenario())


def test_revoke_without_transfer_still_unclaims(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                await revoke_token(token_id=1, transfer_to=None, db=db, _="admin")
            async with sessions() as db:
                chars = (await db.execute(select(Character))).scalars().all()
                assert all(c.owner_token is None for c in chars)
                # Runs are unowned too -- none stay keyed to the dead hash.
                assert (await db.get(MatrixRun, 20)).owner_token_hash is None
                assert await db.get(UserToken, 1) is None

    asyncio.run(scenario())


@pytest.mark.parametrize("target,status", [(1, 400), (99, 404)])
def test_revoke_rejects_bad_transfer_target(tmp_path, target, status):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await revoke_token(token_id=1, transfer_to=target, db=db, _="admin")
                assert exc.value.status_code == status
            async with sessions() as db:
                assert await db.get(UserToken, 1) is not None  # nothing revoked

    asyncio.run(scenario())


def test_assign_owner_hands_draft_to_token_and_can_unown(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                out = await assign_character_owner(10, CharacterOwnerAssign(token_id=2), db=db, _="admin")
                assert out["owner_token_id"] == 2
            async with sessions() as db:
                assert (await db.get(Character, 10)).owner_token == hash_token(NEW)
                admin_view = await my_draft_characters(db=db, ctx={"is_admin": True, "user_token": "gm"})
                assert admin_view[0]["owner_token_id"] == 2
                player_view = await my_draft_characters(db=db, ctx={"is_admin": False, "user_token": NEW})
                assert player_view[0]["owner_token_id"] is None  # owner ids are GM-only
            async with sessions() as db:
                await assign_character_owner(10, CharacterOwnerAssign(token_id=None), db=db, _="admin")
            async with sessions() as db:
                assert (await db.get(Character, 10)).owner_token is None
                with pytest.raises(HTTPException) as exc:
                    await assign_character_owner(10, CharacterOwnerAssign(token_id=99), db=db, _="admin")
                assert exc.value.status_code == 404

    asyncio.run(scenario())


def test_admin_in_runner_view_sees_only_own_drafts(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            async with sessions() as db:
                db.add_all([
                    Character(name="GM Draft", is_pc=True, is_draft=True, owner_token=hash_token("gm")),
                    Character(name="Player Draft", is_pc=True, is_draft=True, owner_token=hash_token(NEW)),
                ])
                await db.commit()
            async with sessions() as db:
                runner = await my_draft_characters(
                    db=db, ctx={"is_admin": True, "user_token": "gm", "view_as_player": True})
                assert [d["name"] for d in runner] == ["GM Draft"]
                assert runner[0]["owner_token_id"] is None
                admin = await my_draft_characters(db=db, ctx={"is_admin": True, "user_token": "gm"})
                assert {d["name"] for d in admin} == {"GM Draft", "Player Draft"}

    asyncio.run(scenario())


def test_orphaned_draft_cannot_be_claimed_by_a_player(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            async with sessions() as db:
                db.add_all([
                    Character(id=10, name="Orphan", is_pc=True, is_draft=True, owner_token=None),
                    Character(id=11, name="Mine", is_pc=True, is_draft=True, owner_token=hash_token(NEW)),
                    Character(id=12, name="Open", is_pc=True, owner_token=None),
                ])
                await db.commit()
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await claim_character(10, db=db, ctx={"is_admin": False, "user_token": NEW})
                assert exc.value.status_code == 404
            async with sessions() as db:
                assert (await db.get(Character, 10)).owner_token is None
                # Re-claiming your own draft and claiming a finished unowned PC still work.
                await claim_character(11, db=db, ctx={"is_admin": False, "user_token": NEW})
                await claim_character(12, db=db, ctx={"is_admin": False, "user_token": NEW})
            async with sessions() as db:
                assert (await db.get(Character, 12)).owner_token == hash_token(NEW)

    asyncio.run(scenario())


def test_drafts_cannot_be_unclaimed(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await unclaim_character(10, db=db, ctx={"is_admin": False, "user_token": NEW})
                assert exc.value.status_code == 404  # not the owner: existence stays private
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await unclaim_character(10, db=db, ctx={"is_admin": False, "user_token": OLD})
                assert exc.value.status_code == 400  # owner: refused, so the draft isn't lost
            async with sessions() as db:
                assert (await db.get(Character, 10)).owner_token == hash_token(OLD)
                # A committed PC can still be unclaimed by its owner.
                await unclaim_character(11, db=db, ctx={"is_admin": False, "user_token": OLD})
            async with sessions() as db:
                assert (await db.get(Character, 11)).owner_token is None

    asyncio.run(scenario())
