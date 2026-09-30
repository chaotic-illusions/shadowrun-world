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
