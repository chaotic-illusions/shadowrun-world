"""Inactive (GM-concealed) orgs, locations and NPCs aren't named to players through run logs,
party stats, or standings -- and standing/reputation GM notes are redacted.
"""
import asyncio
from contextlib import asynccontextmanager
from datetime import date

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.auth.core import hash_token
from app.db.base import Base
from app.models.adventure_log import AdventureLog
from app.models.character import Character
from app.models.location import Location
from app.models.organization import Organization
from app.models.reputation import OrgStanding, Reputation
from app.routers.adventure_logs import get_log, party_stats
from app.routers.reputation import list_org_standings, list_reputations


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
SECRET = "Secret Cabal"


async def _seed(sessions):
    async with sessions() as db:
        open_org = Organization(id=1, name="Open Corp", is_active=True)
        secret_org = Organization(id=2, name=SECRET, is_active=False)
        pc = Character(id=1, name="Runner", is_pc=True, owner_token=hash_token("runner"))
        mole = Character(id=2, name="Mole", is_pc=False, is_active=False)
        log = AdventureLog(id=1, title="Run", session_date=date(2026, 1, 1), objective="o", result="r")
        log.orgs_involved = [open_org, secret_org]
        log.locations_involved = [
            Location(id=1, name="Open Bar", is_active=True),
            Location(id=2, name="Hidden Lab", is_active=False),
        ]
        log.participants = [pc, mole]
        db.add_all([open_org, secret_org, pc, mole, log])
        db.add_all([
            OrgStanding(character_id=1, organization_id=1, standing=2, notes="GM: they owe us"),
            OrgStanding(character_id=1, organization_id=2, standing=-3),
            OrgStanding(character_id=2, organization_id=1, standing=1),
            Reputation(character_id=1, notes="GM rep note"),
            Reputation(character_id=2),
        ])
        await db.commit()


def test_run_log_hides_inactive_orgs_locations_npcs(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                data = await get_log(log_id=1, auth=PLAYER, db=db)
            assert [o["name"] for o in data["orgs_involved"]] == ["Open Corp"]
            assert [loc["name"] for loc in data["locations_involved"]] == ["Open Bar"]
            assert [p["name"] for p in data["participants"]] == ["Runner"]
            async with sessions() as db:
                data = await get_log(log_id=1, auth=ADMIN, db=db)
            assert len(data["orgs_involved"]) == 2 and len(data["participants"]) == 2

    asyncio.run(scenario())


def test_party_stats_drops_inactive_org_standings_for_players(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                data = await party_stats(auth=PLAYER, db=db)
            names = [s["org_name"] for s in data["char_rep"][1]["standings"]]
            assert names == ["Open Corp"]
            async with sessions() as db:
                data = await party_stats(auth=ADMIN, db=db)
            assert SECRET in [s["org_name"] for s in data["char_rep"][1]["standings"]]

    asyncio.run(scenario())


def test_standings_and_reputation_lists_redact_for_players(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            await _seed(sessions)
            async with sessions() as db:
                rows = await list_org_standings(character_id=None, organization_id=None, ctx=PLAYER, db=db)
            assert [(r["character_id"], r["organization_id"]) for r in rows] == [(1, 1)]
            assert rows[0]["notes"] is None
            async with sessions() as db:
                reps = await list_reputations(character_id=None, ctx=PLAYER, db=db)
            assert [r["character_id"] for r in reps] == [1] and reps[0]["notes"] is None
            async with sessions() as db:
                rows = await list_org_standings(character_id=None, organization_id=None, ctx=ADMIN, db=db)
            assert len(rows) == 3
            async with sessions() as db:
                reps = await list_reputations(character_id=None, ctx=ADMIN, db=db)
            assert len(reps) == 2 and reps[0]["notes"] == "GM rep note"

    asyncio.run(scenario())
