import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

from alembic.config import Config
from alembic.script import ScriptDirectory


# Derived from the actual migration graph rather than hardcoded -- a hardcoded revision ID here
# went stale (and both tests failed) every time a new migration landed without this file being
# updated to match. CURRENT_HEAD is whatever `alembic heads` reports right now; FORMER_HEAD is its
# immediate parent, so "upgrade from FORMER_HEAD to head" always exercises exactly the most recent
# migration step, whatever that happens to be.
_REPO_ROOT = Path(__file__).resolve().parent.parent
_ALEMBIC_CFG = Config(str(_REPO_ROOT / "alembic.ini"))
# alembic.ini's script_location is a bare relative path ("alembic"), resolved against the process's
# cwd rather than the ini file's own directory -- pin it absolute so this works regardless of where
# pytest is invoked from.
_ALEMBIC_CFG.set_main_option("script_location", str(_REPO_ROOT / "alembic"))
_SCRIPTS = ScriptDirectory.from_config(_ALEMBIC_CFG)
CURRENT_HEAD = _SCRIPTS.get_current_head()
FORMER_HEAD = _SCRIPTS.get_revision(CURRENT_HEAD).down_revision


def _alembic(database_path, *arguments):
    env = os.environ.copy()
    env["DATABASE_URL"] = f"sqlite+aiosqlite:///{database_path.as_posix()}"
    return subprocess.run(
        [sys.executable, "-m", "alembic", *arguments],
        check=True,
        capture_output=True,
        text=True,
        env=env,
    )


def test_empty_database_upgrades_to_head(tmp_path):
    database = tmp_path / "empty.db"
    _alembic(database, "upgrade", "head")
    current = _alembic(database, "current")
    assert f"{CURRENT_HEAD} (head)" in current.stdout

    with sqlite3.connect(database) as db:
        organization_columns = {
            row[1]: row for row in db.execute("PRAGMA table_info(organizations)")
        }
        location_columns = {row[1]: row for row in db.execute("PRAGMA table_info(locations)")}
        character_columns = {row[1]: row for row in db.execute("PRAGMA table_info(characters)")}
    assert organization_columns["divisions"][3] == 1
    assert organization_columns["divisions"][4] == "'[]'"
    for columns in (organization_columns, location_columns, character_columns):
        assert columns["catalog_scope"][3] == 1
        assert columns["catalog_scope"][4] == "'reference'"


def test_former_head_database_upgrades_without_replaying_baseline(tmp_path):
    database = tmp_path / "former-head.db"
    _alembic(database, "upgrade", FORMER_HEAD)

    upgraded = _alembic(database, "upgrade", "head")
    assert f"Running upgrade {FORMER_HEAD} -> {CURRENT_HEAD}" in upgraded.stderr
    assert "pre_matrix_baseline" not in upgraded.stderr

    current = _alembic(database, "current")
    assert f"{CURRENT_HEAD} (head)" in current.stdout


def test_migrated_schema_matches_models(tmp_path):
    """After upgrade head the DB has exactly the models' tables, columns and nullability -- no
    orphan tables (e.g. a dropped model's) and no drift a later autogenerate would pick up."""
    from alembic.autogenerate import compare_metadata
    from alembic.migration import MigrationContext
    from sqlalchemy import create_engine

    import app.models  # noqa: F401 -- registers every model on Base.metadata
    from app.db.base import Base

    database = tmp_path / "compare.db"
    _alembic(database, "upgrade", "head")
    engine = create_engine(f"sqlite:///{database.as_posix()}")
    try:
        with engine.connect() as connection:
            diff = compare_metadata(MigrationContext.configure(connection), Base.metadata)
    finally:
        engine.dispose()
    assert diff == []


def test_matrix_runs_with_null_columns_upgrade_to_not_null(tmp_path):
    # Pinned to the migration under test (e9b4d2a7c615 tightens matrix_runs), not FORMER_HEAD,
    # which moves on as later migrations land.
    database = tmp_path / "nulls.db"
    _alembic(database, "upgrade", "d4a7c9e2f160")
    with sqlite3.connect(database) as db:
        db.execute(
            "INSERT INTO matrix_runs (id, status, version, aar_acknowledged) VALUES (1, 'active', 0, 0)"
        )
    _alembic(database, "upgrade", "e9b4d2a7c615")
    with sqlite3.connect(database) as db:
        row = db.execute(
            "SELECT decker_json, state_json, created_at IS NOT NULL, updated_at IS NOT NULL "
            "FROM matrix_runs WHERE id = 1"
        ).fetchone()
        tables = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    assert row == ("{}", "{}", 1, 1)
    assert "house_rules" not in tables



def test_fan_content_toggle_stripped_from_enabled_books(tmp_path):
    database = tmp_path / "fan.db"
    _alembic(database, "upgrade", "e9b4d2a7c615")
    with sqlite3.connect(database) as db:
        # The campaign_state singleton row is created by its own migration.
        db.execute("UPDATE campaign_state SET enabled_books = '[\"SSC\", \"FAN\", \"RIG2\"]' WHERE id = 1")
    _alembic(database, "upgrade", "a3f6c1e8d924")
    with sqlite3.connect(database) as db:
        books = db.execute("SELECT enabled_books FROM campaign_state WHERE id = 1").fetchone()[0]
    assert json.loads(books) == ["SSC", "RIG2"]


def test_origin_pc_id_backfills_runner_contacts(tmp_path):
    database = tmp_path / "origin.db"
    _alembic(database, "upgrade", "a3f6c1e8d924")
    with sqlite3.connect(database) as db:
        cols = "name, is_pc, race, show_background, contact_skills, connection, is_active, created_at, updated_at"
        vals = "'Human', 0, '[]', 1, 1, '2026-10-01', '2026-10-01'"
        db.execute(f"INSERT INTO characters (id, {cols}) VALUES (1, 'Leadbelly', 1, {vals})")
        for npc_id, name in ((10, "Chopper"), (11, "Patch"), (12, "Johnson")):
            db.execute(f"INSERT INTO characters (id, {cols}) VALUES (?, ?, 0, {vals})", (npc_id, name))
        contact_cols = "owner_id, npc_id, name, contact_type, loyalty, connection, is_active"
        db.execute(f"INSERT INTO contacts ({contact_cols}) VALUES (1, 10, 'Chopper', 'Contact', 1, 1, 1)")
        db.execute(f"INSERT INTO contacts ({contact_cols}) VALUES (1, 11, 'Patch', NULL, 3, 1, 1)")
        db.execute(f"INSERT INTO contacts ({contact_cols}) VALUES (1, 12, 'Johnson', 'Gang', 1, 1, 1)")
        db.execute(f"INSERT INTO contacts ({contact_cols}) VALUES (1, NULL, 'Crew', 'Follower', 1, 1, 1)")
    _alembic(database, "upgrade", "a7d2e5c9b130")
    with sqlite3.connect(database) as db:
        origins = dict(db.execute("SELECT id, origin_pc_id FROM characters WHERE is_pc = 0").fetchall())
        types = dict(db.execute("SELECT name, contact_type || ':' || loyalty FROM contacts").fetchall())
    # Individual contacts (chargen-typed or hand-linked) belong to the runner; a Gang tie doesn't.
    assert origins == {10: 1, 11: 1, 12: None}
    # The hand-linked one takes its type from Loyalty; Followers move to Loyalty 6.
    assert types == {"Chopper": "Contact:1", "Patch": "Buddy:3", "Johnson": "Gang:1", "Crew": "Follower:6"}


def test_spells_renamed_to_book_names(tmp_path):
    database = tmp_path / "spells.db"
    _alembic(database, "upgrade", "a7d2e5c9b130")
    owned = [{"name": "Gecko Grip", "force": 3}, {"name": "Heal", "force": 4}, {"name": "Cause Allergy", "force": 2}]
    with sqlite3.connect(database) as db:
        cols = "name, is_pc, race, show_background, contact_skills, connection, is_active, created_at, updated_at"
        vals = "'Human', 1, '[]', 1, 1, '2026-10-02', '2026-10-02'"
        db.execute(
            f"INSERT INTO characters (id, {cols}, spells, chargen_state) VALUES (1, 'Night Shift', 1, {vals}, ?, ?)",
            (json.dumps(owned), json.dumps({"spells": [{"name": "Alleviate Allergy", "force": 1}]})),
        )
    _alembic(database, "upgrade", "b4e7a1c93d26")
    with sqlite3.connect(database) as db:
        spells, state = db.execute("SELECT spells, chargen_state FROM characters WHERE id = 1").fetchone()
    assert [s["name"] for s in json.loads(spells)] == ["Gecko Crawl", "Heal", "Cause Nuisance Allergy"]
    assert json.loads(spells)[1] == {"name": "Heal", "force": 4}
    assert json.loads(state)["spells"] == [{"name": "Alleviate Nuisance Allergy", "force": 1}]
