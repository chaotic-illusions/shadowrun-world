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


def test_removed_cyberware_is_refunded(tmp_path):
    database = tmp_path / "cyber.db"
    _alembic(database, "upgrade", "b4e7a1c93d26")
    smartlink = {"n": "Smartlink", "grade": "Standard", "baseEss": 0.5, "baseCost": 7000}
    gear = {"cyber": [smartlink,
                      {"n": "Display Link", "grade": "Standard", "baseEss": 0.1, "baseCost": 1000},
                      {"n": "Chipjack", "grade": "Alpha", "baseEss": 0.2, "baseCost": 1000}],
            "weapons": [{"n": "Ares Predator"}]}
    state = {"gear": {"cyber": [smartlink, {"n": "Display Link", "grade": "Standard", "baseEss": 0.1}]}}
    with sqlite3.connect(database) as db:
        cols = ("name, is_pc, race, show_background, contact_skills, connection, is_active, created_at, updated_at, "
                "gear, chargen_state, essence, nuyen, is_draft")
        vals = "'Human', 0, '[]', 1, 1, '2026-10-02', '2026-10-02', ?, ?, ?, ?, ?"
        for char_id, name, is_draft in ((1, "Hatchetman", 0), (2, "Unfinished", 1)):
            db.execute(f"INSERT INTO characters (id, {cols}) VALUES (?, ?, 1, {vals})",
                       (char_id, name, json.dumps(gear), json.dumps(state), 5.24, 500, is_draft))
        db.execute(f"INSERT INTO characters (id, {cols}) VALUES (3, 'Clean', 1, {vals})",
                   (json.dumps({"cyber": [smartlink]}), "{}", 5.5, 100, 0))
    _alembic(database, "upgrade", "c5f8b2d04e37")
    with sqlite3.connect(database) as db:
        rows = {r[0]: r[1:] for r in db.execute("SELECT id, gear, chargen_state, essence, nuyen FROM characters")}
    for char_id in (1, 2):
        kept = json.loads(rows[char_id][0])
        assert kept == {"cyber": [smartlink], "weapons": [{"n": "Ares Predator"}]}
        assert json.loads(rows[char_id][1]) == {"gear": {"cyber": [smartlink]}}
    # Display Link 0.1 + Alpha Chipjack 0.16 Essence; 1,000 + 3,000 nuyen.
    assert rows[1][2:] == (5.5, 4500)
    assert rows[2][2:] == (5.24, 500)     # a draft's totals are recomputed by the builder
    assert rows[3][2:] == (5.5, 100)      # untouched


def test_skills_move_to_concentration_lists(tmp_path):
    database = tmp_path / "skills.db"
    _alembic(database, "upgrade", "c5f8b2d04e37")
    skills = [
        # Fresh from chargen, never opened on the play sheet: 3 points + Pistols, not yet split.
        {"name": "Firearms", "attr": "quickness", "group": "combat", "rating": 3, "conc": "Pistols", "spec": ""},
        # 4 points + Two-wheeler + Honda Viking, not yet split.
        {"name": "Bike", "rating": 4, "conc": "Two-wheeler", "spec": "Honda Viking"},
        # Split by the play sheet, then the Concentration raised with karma.
        {"name": "Sorcery", "rating": 4, "conc": "Spellcasting", "concRating": 7, "spec": "Combat", "specRating": 8},
        {"name": "Etiquette", "rating": 0, "conc": "Street", "concRating": 2, "spec": "", "specRating": None},
        {"name": "Stealth", "rating": 2, "conc": "", "spec": ""},
        {"name": "Spanish", "group": "language", "rating": 2, "conc": "", "spec": "", "free": False},
    ]
    state = {"skills": [{"name": "Firearms", "rating": 3, "conc": "Pistols", "spec": ""}]}
    with sqlite3.connect(database) as db:
        cols = ("name, is_pc, race, show_background, contact_skills, connection, is_active, created_at, updated_at, "
                "skills, chargen_state")
        vals = "'Human', 1, '[]', 1, 1, '2026-10-04', '2026-10-04', ?, ?"
        db.execute(f"INSERT INTO characters (id, {cols}) VALUES (1, 'Runner', 1, {vals})",
                   (json.dumps(skills), json.dumps(state)))
        db.execute(f"INSERT INTO characters (id, {cols}) VALUES (2, 'Contact', 0, {vals})", ("[]", "{}"))
    _alembic(database, "upgrade", "d8a3f0b6c215")
    with sqlite3.connect(database) as db:
        got, got_state = db.execute("SELECT skills, chargen_state FROM characters WHERE id = 1").fetchone()
        assert db.execute("SELECT skills FROM characters WHERE id = 2").fetchone()[0] == "[]"
    assert json.loads(got) == [
        {"name": "Firearms", "attr": "quickness", "group": "combat", "rating": 2,
         "concs": [{"name": "Pistols", "rating": 4}], "specs": []},
        {"name": "Bike", "rating": 2, "concs": [{"name": "Two-wheeler", "rating": 4}],
         "specs": [{"name": "Honda Viking", "rating": 6, "conc": "Two-wheeler"}]},
        {"name": "Sorcery", "rating": 4, "concs": [{"name": "Spellcasting", "rating": 7}],
         "specs": [{"name": "Combat", "rating": 8, "conc": "Spellcasting"}]},
        {"name": "Etiquette", "rating": 0, "concs": [{"name": "Street", "rating": 2}], "specs": []},
        {"name": "Stealth", "rating": 2, "concs": [], "specs": []},
        {"name": "Spanish", "group": "language", "rating": 2, "free": False, "concs": [], "specs": []},
    ]
    assert json.loads(got_state) == state   # the wizard keeps its own single conc/spec shape
