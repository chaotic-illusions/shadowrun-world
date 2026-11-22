"""Startup guards: leftover division ``headquarters`` keys are stripped (they'd fail every org
read), and a create_all-built DB is stamped so a later ``alembic upgrade head`` works.
"""
import asyncio
import os
import subprocess
import sys

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

import app.main as main
from app.db.base import Base
from app.models.organization import Organization
from app.routers.organizations import list_organizations

DIVISION = {"id": "6f1c6f2e-4a55-4b8e-9a8e-0d6f7b8c9a01", "name": "Ops", "kind": "division",
            "headquarters": "Seattle"}
ADMIN = {"is_admin": True, "is_user": True, "user_token": "gm", "view_as_player": False}


def _use_database(path, monkeypatch):
    engine = create_async_engine(f"sqlite+aiosqlite:///{path.as_posix()}")
    monkeypatch.setattr(main, "engine", engine)
    monkeypatch.setattr(main, "async_session", async_sessionmaker(engine, expire_on_commit=False))
    return engine


def test_division_headquarters_stripped_and_orgs_readable(tmp_path, monkeypatch):
    async def scenario():
        engine = _use_database(tmp_path / "t.db", monkeypatch)
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            async with main.async_session() as db:
                db.add(Organization(id=1, name="Corp", divisions=[DIVISION]))
                await db.commit()
            await main._strip_division_headquarters()
            await main._strip_division_headquarters()  # idempotent
            async with main.async_session() as db:
                orgs = await list_organizations(
                    org_type=None, is_active=None, source_adventure=None, auth=ADMIN, db=db)
            assert orgs[0]["divisions"][0]["name"] == "Ops"
            assert "headquarters" not in orgs[0]["divisions"][0]
        finally:
            await engine.dispose()

    asyncio.run(scenario())


def test_create_all_database_is_stamped_for_alembic(tmp_path, monkeypatch):
    database = tmp_path / "fresh.db"

    async def scenario():
        engine = _use_database(database, monkeypatch)
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            await main._stamp_unversioned_db()
            await main._stamp_unversioned_db()  # already stamped: no-op
        finally:
            await engine.dispose()

    asyncio.run(scenario())
    env = os.environ.copy()
    env["DATABASE_URL"] = f"sqlite+aiosqlite:///{database.as_posix()}"
    out = subprocess.run([sys.executable, "-m", "alembic", "upgrade", "head"],
                         capture_output=True, text=True, env=env)
    assert out.returncode == 0, out.stderr
    current = subprocess.run([sys.executable, "-m", "alembic", "current"],
                             capture_output=True, text=True, env=env, check=True)
    assert f"{main._alembic_head()} (head)" in current.stdout


def test_adept_attrs_backfilled_once(tmp_path, monkeypatch):
    """Adepts stored before attributes included Improved Physical Attributes get their levels added
    once; Attribute Boost (temporary) and other characters are untouched; a restart adds nothing."""
    from sqlalchemy import select
    from app.models.character import Character

    powers = [
        {"name": "Improved Physical Attributes", "attr": "strength", "rated": True, "lvl": 2},
        {"name": "Improved Physical Attributes", "rated": True, "lvl": 1},      # no pick: Body
        {"name": "Attribute Boost", "attr": "quickness", "rated": True, "lvl": 3},
        {"name": "Improved Physical Attributes", "attr": "quickness", "rated": True, "lvl": "3a"},  # garbled: skipped
        {"name": "Improved Physical Attributes", "attr": "quickness", "rated": True, "lvl": 9999},  # absurd: skipped
    ]

    async def scenario():
        engine = _use_database(tmp_path / "t.db", monkeypatch)
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            async with main.async_session() as db:
                db.add(Character(id=1, name="Adept", body=4, strength=4, quickness=5, adept_powers=powers))
                db.add(Character(id=2, name="Sam", body=4, strength=4, quickness=5, adept_powers=[]))
                await db.commit()
            await main._backfill_adept_attrs_once()
            await main._backfill_adept_attrs_once()  # guarded: no second add
            async with main.async_session() as db:
                rows = {c.id: c for c in (await db.execute(select(Character))).scalars()}
            assert (rows[1].body, rows[1].strength, rows[1].quickness) == (5, 6, 5)
            assert rows[1].version == rows[2].version + 1     # through the ORM: optimistic lock bumped once
            assert (rows[2].body, rows[2].strength, rows[2].quickness) == (4, 4, 5)
        finally:
            await engine.dispose()

    asyncio.run(scenario())
