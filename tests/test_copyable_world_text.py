"""The copyable-world-text auditor, on synthetic input only.

Auditing the real world data is a manual step against a local DB copy:
``python scripts/audit_copyable_world_text.py --db <db>``. Tests never read production data.
"""
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.db.base import Base
from app.models.character import Character
from scripts.audit_copyable_world_text import _scan_text, audit_database

FLAGGED = "NEEDS HUMAN TOUCH: keep this player-authored text."


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


def test_copyable_world_text_audit_ignores_pc_prose(tmp_path: Path) -> None:
    database_path = tmp_path / "world.db"
    engine = create_engine(f"sqlite:///{database_path.as_posix()}")
    Base.metadata.create_all(engine)
    with Session(engine) as db:
        db.add_all([
            Character(id=1, name="Runner", is_pc=True, notes=FLAGGED),
            Character(id=2, name="Fixer", is_pc=False, notes=FLAGGED),
        ])
        db.commit()
    engine.dispose()

    findings = audit_database(database_path)

    assert findings, "the NPC's flagged note should be reported"
    assert {(f.kind, f.row_id) for f in findings} == {("character", 2)}
