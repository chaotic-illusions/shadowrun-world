import shutil
import sqlite3
from pathlib import Path

import pytest

from scripts.audit_copyable_world_text import audit_database


ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_DB = ROOT / "data" / "shadowrun_prod.db"

# The production database is a local-only file, never committed.
needs_production_db = pytest.mark.skipif(
    not PRODUCTION_DB.exists(), reason="local production database not present"
)


@needs_production_db
def test_production_copyable_world_text_is_clean() -> None:
    assert audit_database(PRODUCTION_DB) == []


@needs_production_db
def test_copyable_world_text_audit_ignores_pc_prose(tmp_path: Path) -> None:
    database_path = tmp_path / "world.db"
    shutil.copy2(PRODUCTION_DB, database_path)

    with sqlite3.connect(database_path) as database:
        database.row_factory = sqlite3.Row
        pc_id = database.execute(
            "SELECT id FROM characters WHERE is_pc = 1 ORDER BY id LIMIT 1"
        ).fetchone()["id"]
        database.execute(
            "UPDATE characters SET notes = ? WHERE id = ?",
            ("NEEDS HUMAN TOUCH: keep this player-authored text.", pc_id),
        )
        database.commit()

    assert audit_database(database_path) == []

