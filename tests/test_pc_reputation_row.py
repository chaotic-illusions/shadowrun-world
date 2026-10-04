"""A live PC always has a reputation row, and apply-changes never drops a change for want of one.

Food Fight (run 1) exposed this: Oversight had no reputation row, so his reviewed heat and
public-awareness changes came back as "No reputation record for character 1860" and were
silently skipped while the other eleven applied.

Direct router-call style against a throwaway aiosqlite DB, same as
tests/test_org_affiliation_weighting.py -- no HTTP layer.
"""
import asyncio
from contextlib import asynccontextmanager

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.db.base import Base
from app.models.character import Character
from app.models.reputation import Reputation
from app.routers.adventure_logs import ApplyChangesRequest, apply_world_changes
from app.routers.characters import _ensure_pc_reputation


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


async def _rep(sessions, pc_id):
    async with sessions() as db:
        return await db.scalar(select(Reputation).where(Reputation.character_id == pc_id))


def test_apply_changes_creates_the_missing_reputation_row(tmp_path):
    """The Food Fight regression: a PC with no row must still receive its changes."""
    async def scenario():
        async with _database(tmp_path / "missing.db") as sessions:
            async with sessions() as db:
                pc = Character(name="Oversight", is_pc=True)
                db.add(pc)
                await db.commit()
                pc_id = pc.id

            assert await _rep(sessions, pc_id) is None  # precondition: no row at all

            body = ApplyChangesRequest(changes=[
                {"type": "heat", "character_id": pc_id, "delta": 2},
                {"type": "public_awareness", "character_id": pc_id, "delta": 1},
                {"type": "street_cred", "character_id": pc_id, "delta": 3},
                {"type": "notoriety", "character_id": pc_id, "delta": 1},
            ])
            async with sessions() as db:
                result = await apply_world_changes(body, db=db, _="admin")

            assert result["errors"] == []
            assert len(result["applied"]) == 4
            rep = await _rep(sessions, pc_id)
            assert rep is not None
            assert (rep.heat, rep.public_awareness, rep.street_cred, rep.notoriety) == (2, 1, 3, 1)

    asyncio.run(scenario())


def test_apply_changes_reuses_an_existing_row(tmp_path):
    """Creating on demand must not clobber a row that is already there."""
    async def scenario():
        async with _database(tmp_path / "existing.db") as sessions:
            async with sessions() as db:
                pc = Character(name="Leadbelly", is_pc=True)
                db.add(pc)
                await db.flush()
                db.add(Reputation(character_id=pc.id, street_cred=4, heat=1))
                await db.commit()
                pc_id = pc.id

            body = ApplyChangesRequest(changes=[
                {"type": "street_cred", "character_id": pc_id, "delta": 1},
                {"type": "heat", "character_id": pc_id, "delta": 2},
            ])
            async with sessions() as db:
                await apply_world_changes(body, db=db, _="admin")

            rep = await _rep(sessions, pc_id)
            assert (rep.street_cred, rep.heat) == (5, 3)  # accumulated, not reset
            async with sessions() as db:
                rows = (await db.execute(
                    select(Reputation).where(Reputation.character_id == pc_id)
                )).scalars().all()
            assert len(rows) == 1  # no duplicate row

    asyncio.run(scenario())


def test_ensure_pc_reputation_only_covers_live_pcs(tmp_path):
    """A live PC gets a row; a draft PC and an NPC get nothing."""
    async def scenario():
        async with _database(tmp_path / "ensure.db") as sessions:
            async with sessions() as db:
                live = Character(name="Runner", is_pc=True)
                draft = Character(name="Half-built", is_pc=True, is_draft=True)
                npc = Character(name="Fixer", is_pc=False)
                db.add_all([live, draft, npc])
                await db.commit()
                live_id, draft_id, npc_id = live.id, draft.id, npc.id

                for char in (live, draft, npc):
                    await _ensure_pc_reputation(db, char)
                await db.commit()

            assert await _rep(sessions, live_id) is not None
            assert await _rep(sessions, draft_id) is None
            assert await _rep(sessions, npc_id) is None

    asyncio.run(scenario())


def test_ensure_pc_reputation_is_idempotent(tmp_path):
    """It is called on every write path that can promote a row, so repeats must be free."""
    async def scenario():
        async with _database(tmp_path / "idem.db") as sessions:
            async with sessions() as db:
                pc = Character(name="Runner", is_pc=True)
                db.add(pc)
                await db.commit()
                pc_id = pc.id

                for _ in range(3):
                    await _ensure_pc_reputation(db, pc)
                    await db.commit()

            async with sessions() as db:
                rows = (await db.execute(
                    select(Reputation).where(Reputation.character_id == pc_id)
                )).scalars().all()
            assert len(rows) == 1

    asyncio.run(scenario())


def test_promoting_a_draft_gives_it_a_row(tmp_path):
    """Clearing is_draft (finalize, convert, or a PATCH) is what makes the PC live."""
    async def scenario():
        async with _database(tmp_path / "promote.db") as sessions:
            async with sessions() as db:
                pc = Character(name="Night Shift", is_pc=True, is_draft=True)
                db.add(pc)
                await db.commit()
                pc_id = pc.id

                await _ensure_pc_reputation(db, pc)
                await db.commit()
            assert await _rep(sessions, pc_id) is None

            async with sessions() as db:
                pc = await db.get(Character, pc_id)
                pc.is_draft = False
                await _ensure_pc_reputation(db, pc)
                await db.commit()
            assert await _rep(sessions, pc_id) is not None

    asyncio.run(scenario())
