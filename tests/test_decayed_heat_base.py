"""New heat/PA lands on the decayed value, and an echoed save doesn't undo decay.

Heat 3 decays to 1 over 14 days; +2 on the next run must put the runner at 3, not 5. And the
GM character editor saves heat/PA back on every save, so an unchanged value must leave the
decay running instead of re-stamping the stored pre-decay value. Org standings don't decay.

Direct router-call style against a throwaway aiosqlite DB, same as
tests/test_pc_reputation_row.py -- no HTTP layer.
"""
import asyncio
from contextlib import asynccontextmanager

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.db.base import Base
from app.models.campaign import CampaignState
from app.models.character import Character
from app.models.organization import Organization
from app.models.reputation import OrgStanding, Reputation
from app.routers.adventure_logs import ApplyChangesRequest, apply_world_changes, party_stats
from app.routers.reputation import list_reputations, update_reputation
from app.schemas.reputation import ReputationUpdate

ADMIN = {"is_admin": True}


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


async def _seed(sessions, *, tick: int) -> int:
    """Leadbelly with heat 3 / PA 2 stamped at tick 1, the clock at `tick`."""
    async with sessions() as db:
        db.add(CampaignState(id=1, current_tick=tick))
        pc = Character(name="Leadbelly", is_pc=True, is_active=True)
        db.add(pc)
        await db.flush()
        db.add(Reputation(character_id=pc.id, heat=3, heat_stamped_tick=1,
                          public_awareness=2, pa_stamped_tick=1))
        await db.commit()
        return pc.id


async def _rep(sessions, pc_id):
    async with sessions() as db:
        return await db.scalar(select(Reputation).where(Reputation.character_id == pc_id))


def test_new_heat_adds_to_decayed_value(tmp_path):
    async def scenario():
        async with _database(tmp_path / "add.db") as sessions:
            pc_id = await _seed(sessions, tick=15)  # 14 days on: heat 3 -> 1.14 -> 1, PA 2 -> 0.76 -> 1

            body = ApplyChangesRequest(changes=[
                {"type": "heat", "character_id": pc_id, "delta": 2},
                {"type": "public_awareness", "character_id": pc_id, "delta": 1},
            ])
            async with sessions() as db:
                result = await apply_world_changes(body, db=db, _="admin")
            assert result["errors"] == []

            rep = await _rep(sessions, pc_id)
            assert (rep.heat, rep.heat_stamped_tick) == (3, 15)  # 1 + 2, not 3 + 2
            assert (rep.public_awareness, rep.pa_stamped_tick) == (2, 15)  # 1 + 1

    asyncio.run(scenario())


def test_list_reports_decayed_values(tmp_path):
    async def scenario():
        async with _database(tmp_path / "list.db") as sessions:
            pc_id = await _seed(sessions, tick=15)
            async with sessions() as db:
                rows = await list_reputations(character_id=pc_id, ctx=ADMIN, db=db)
            assert (rows[0]["heat"], rows[0]["public_awareness"]) == (1, 1)

    asyncio.run(scenario())


def test_echoed_editor_save_keeps_decaying(tmp_path):
    async def scenario():
        async with _database(tmp_path / "echo.db") as sessions:
            pc_id = await _seed(sessions, tick=15)
            rep_id = (await _rep(sessions, pc_id)).id

            # The editor loads the decayed values (1, 1) and saves them straight back.
            async with sessions() as db:
                await update_reputation(rep_id, ReputationUpdate(heat=1, public_awareness=1, street_cred=2),
                                        db=db, _="admin")
            rep = await _rep(sessions, pc_id)
            assert (rep.heat, rep.heat_stamped_tick) == (3, 1)  # untouched, still decaying
            assert (rep.public_awareness, rep.pa_stamped_tick) == (2, 1)
            assert rep.street_cred == 2

            # A real edit sets the value and restarts decay from now.
            async with sessions() as db:
                await update_reputation(rep_id, ReputationUpdate(heat=4), db=db, _="admin")
            rep = await _rep(sessions, pc_id)
            assert (rep.heat, rep.heat_stamped_tick) == (4, 15)

    asyncio.run(scenario())


def test_org_standings_do_not_decay(tmp_path):
    async def scenario():
        async with _database(tmp_path / "standing.db") as sessions:
            async with sessions() as db:
                db.add(CampaignState(id=1, current_tick=500))
                pc = Character(name="Gambit", is_pc=True, is_active=False)
                org = Organization(name="Ancients")
                db.add_all([pc, org])
                await db.flush()
                db.add(OrgStanding(character_id=pc.id, organization_id=org.id, standing=5))
                await db.commit()
                pc_id = pc.id

            async with sessions() as db:
                data = await party_stats(auth=ADMIN, db=db)
            assert data["char_rep"][pc_id]["standings"][0]["standing"] == 5

    asyncio.run(scenario())
