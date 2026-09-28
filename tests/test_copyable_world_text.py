import shutil
import sqlite3
from pathlib import Path

import pytest

from scripts.audit_copyable_world_text import _scan_text, audit_database
from scripts.clean_copyable_world_text import build_changes, clean_text


ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_DB = ROOT / "data" / "prod-snapshot" / "2026-09-15" / "shadowrun_prod.db"

# The production database is a local-only file, never committed.
needs_production_db = pytest.mark.skipif(
    not PRODUCTION_DB.exists(), reason="local production database not present"
)


@needs_production_db
def test_production_copyable_world_text_is_clean() -> None:
    assert audit_database(PRODUCTION_DB) == []


@needs_production_db
def test_production_copyable_world_text_cleanup_is_idempotent() -> None:
    with sqlite3.connect(PRODUCTION_DB) as database:
        database.row_factory = sqlite3.Row
        assert build_changes(database) == []


@needs_production_db
def test_copyable_world_text_tools_ignore_pc_prose(tmp_path: Path) -> None:
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
        changes = build_changes(database)

    assert not any(
        change["table"] == "characters" and change["id"] == pc_id
        for change in changes
    )
    assert audit_database(database_path) == []


def test_cleaner_preserves_valid_prose_and_sentence_boundaries() -> None:
    cases = {
        (
            "He manages an unusually large collection territory, skims little, and "
            "conducts public weekly payment roll calls."
        ): (
            "Andrew Musai manages an unusually large collection territory, skims little, "
            "and conducts public weekly payment roll calls."
        ),
        (
            "Born in San Francisco, a 23-year Seattle resident whose watchwords are safety "
            "and prosperity rather than aggressive expansion; prefers to see things run "
            "smoothly and without problems."
        ): (
            "Born in San Francisco, a 23-year Seattle resident whose watchwords are safety "
            "and prosperity rather than aggressive expansion; prefers to see things run "
            "smoothly and without problems."
        ),
        "'He had said he really wanted to get inside these animals. I guess he got his wish.'": (
            "'He had said he really wanted to get inside these animals. I guess he got his wish.'"
        ),
        "In the 2054 source frame, the airport provides domestic service.": (
            "In 2054, the airport provides domestic service."
        ),
        "Availability: documented in the 2054 source frame; 2050 status is not established.": None,
        "The source's Tir corporation sells computer technology through a Portland office.": (
            "This Tir corporation sells computer technology through a Portland office."
        ),
    }

    assert {source: clean_text(source) for source in cases} == cases


def test_auditor_rejects_known_malformed_prose() -> None:
    malformed = (
        "By 2054,.",
        "published records does not establish it.",
        "Harlech Castle is a alternate name.",
        "The U.S. Of A. remains unchanged.",
        "One sentence.By 2056, another begins.",
        "These hidden facts is not publicly known.",
    )

    for text in malformed:
        findings = list(_scan_text("test", 1, "test", "notes", text))
        assert any("malformed_prose" in finding.patterns for finding in findings), text