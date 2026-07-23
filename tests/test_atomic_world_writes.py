import asyncio
from contextlib import asynccontextmanager
from datetime import date

import pytest
from fastapi import HTTPException
from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.auth.core import hash_token
from app.db.base import Base
from app.models.adventure_log import AdventureLog, AdventureRunCounter
from app.models.campaign import CampaignState
from app.models.character import Character
from app.routers.adventure_logs import create_log, update_log
from app.routers.characters import claim_character
from app.schemas.adventure_log import AdventureLogCreate, AdventureLogUpdate
from app.services.campaign import advance_clock, get_campaign_state
import app.main as main


@asynccontextmanager
async def _database(path):
    engine = create_async_engine(
        f"sqlite+aiosqlite:///{path.as_posix()}",
        connect_args={"timeout": 5},
    )
    sessions = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as connection:
        await connection.exec_driver_sql("PRAGMA journal_mode=WAL")
        await connection.run_sync(Base.metadata.create_all)
    try:
        yield engine, sessions
    finally:
        await engine.dispose()


def test_character_claim_is_atomic(tmp_path):
    async def scenario():
        async with _database(tmp_path / "claim.db") as (_, sessions):
            async with sessions() as db:
                db.add(Character(name="Claimable", is_pc=True))
                await db.commit()

            barrier = asyncio.Barrier(2)

            async def claim(token):
                async with sessions() as db:
                    await db.execute(select(func.count()).select_from(Character))
                    await barrier.wait()
                    try:
                        result = await claim_character(
                            1,
                            db=db,
                            ctx={"user_token": token, "is_admin": False},
                        )
                        return result["is_claimed"]
                    except HTTPException as exc:
                        return exc.status_code

            outcomes = await asyncio.gather(claim("alpha"), claim("bravo"))
            assert sorted(outcomes, key=str) == [409, True]

            async with sessions() as db:
                owner = await db.scalar(select(Character.owner_token).where(Character.id == 1))
            assert owner in {hash_token("alpha"), hash_token("bravo")}

    asyncio.run(scenario())


def test_campaign_singleton_and_clock_increment_are_atomic(tmp_path):
    async def scenario():
        async with _database(tmp_path / "campaign.db") as (_, sessions):
            async def create_state():
                async with sessions() as db:
                    return (await get_campaign_state(db)).current_tick

            assert await asyncio.gather(*(create_state() for _ in range(4))) == [0, 0, 0, 0]

            async def increment():
                async with sessions() as db:
                    return await advance_clock(db, 1)

            results = await asyncio.gather(*(increment() for _ in range(12)))
            assert sorted(results) == list(range(1, 13))
            async with sessions() as db:
                assert await db.scalar(select(CampaignState.current_tick)) == 12
                assert await db.scalar(select(func.count()).select_from(CampaignState)) == 1

    asyncio.run(scenario())


def test_adventure_run_numbers_are_unique_under_concurrency(tmp_path):
    async def scenario():
        async with _database(tmp_path / "runs.db") as (_, sessions):
            body = AdventureLogCreate(
                title="Concurrent run",
                session_date=date(2053, 1, 1),
                objective="Test allocation",
                result="Logged",
            )

            async def create_one():
                async with sessions() as db:
                    log = await create_log(body, db=db, _="admin")
                    return log.run_number

            run_numbers = await asyncio.gather(*(create_one() for _ in range(8)))
            assert sorted(run_numbers) == list(range(1, 9))
            async with sessions() as db:
                assert await db.scalar(select(AdventureRunCounter.last_run_number)) == 8
                assert await db.scalar(select(func.count()).select_from(AdventureLog)) == 8

                existing = await db.get(AdventureLog, 1)
                existing.run_number = 50
                await db.commit()

            async with sessions() as db:
                next_log = await create_log(body, db=db, _="admin")
                assert next_log.run_number == 51

            async with sessions() as db:
                with pytest.raises(HTTPException) as conflict:
                    await update_log(
                        next_log.id,
                        AdventureLogUpdate(run_number=50),
                        db=db,
                        _="admin",
                    )
                assert conflict.value.status_code == 409

    asyncio.run(scenario())


def test_schema_guard_accepts_verified_concurrent_success(monkeypatch):
    class Result:
        def __init__(self, columns):
            self.columns = columns

        def fetchall(self):
            return [(0, column) for column in self.columns]

    class Connection:
        def __init__(self):
            self.columns = []

        async def exec_driver_sql(self, statement):
            if statement.startswith("PRAGMA"):
                return Result(self.columns)
            self.columns.append("new_column")
            raise RuntimeError("duplicate column name")

    connection = Connection()

    class Engine:
        @asynccontextmanager
        async def begin(self):
            yield connection

    monkeypatch.setattr(main, "engine", Engine())
    assert asyncio.run(main._ensure_sqlite_column("sample", "new_column", "INTEGER")) is True


def test_schema_guard_fails_when_postcondition_is_absent(monkeypatch):
    class Result:
        def fetchall(self):
            return []

    class Connection:
        async def exec_driver_sql(self, statement):
            if statement.startswith("ALTER"):
                raise RuntimeError("disk I/O error")
            return Result()

    class Engine:
        @asynccontextmanager
        async def begin(self):
            yield Connection()

    monkeypatch.setattr(main, "engine", Engine())
    with pytest.raises(RuntimeError, match="disk I/O error"):
        asyncio.run(main._ensure_sqlite_column("sample", "missing", "INTEGER"))


def test_legacy_run_number_guard_establishes_postconditions(tmp_path, monkeypatch):
    async def scenario():
        database = tmp_path / "legacy-runs.db"
        engine = create_async_engine(f"sqlite+aiosqlite:///{database.as_posix()}")
        async with engine.begin() as connection:
            await connection.exec_driver_sql(
                "CREATE TABLE adventure_logs (id INTEGER PRIMARY KEY, run_number INTEGER)"
            )
            await connection.exec_driver_sql(
                "CREATE TABLE adventure_run_counter "
                "(id INTEGER PRIMARY KEY, last_run_number INTEGER NOT NULL)"
            )
            await connection.exec_driver_sql(
                "INSERT INTO adventure_logs (id, run_number) VALUES (1, 7), (2, 7), (3, NULL)"
            )

        monkeypatch.setattr(main, "engine", engine)
        await main._ensure_adventure_run_number_schema()

        async with engine.connect() as connection:
            rows = await connection.exec_driver_sql(
                "SELECT run_number FROM adventure_logs ORDER BY id"
            )
            assert [row[0] for row in rows.fetchall()] == [7, 8, None]
            indexes = await connection.exec_driver_sql("PRAGMA index_list(adventure_logs)")
            assert any(row[1] == "ux_adventure_logs_run_number" and row[2] for row in indexes)
            counter = await connection.exec_driver_sql(
                "SELECT last_run_number FROM adventure_run_counter WHERE id = 1"
            )
            assert counter.scalar_one() == 8
        await engine.dispose()

    asyncio.run(scenario())