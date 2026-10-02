"""rename_spells_to_book_names

The spell catalog was re-transcribed from the books. Three entries change name, and a known spell
is matched to the catalog by name, so rename them on every character (and in the saved chargen
wizard state) to keep their stats and reference popup:

- "Gecko Grip" is "Gecko Crawl" in Awakenings.
- "Alleviate Allergy" / "Cause Allergy" are four spells each, one per allergy severity. The old
  single entries carried the Light drain of the Nuisance version, so they become that one.

Revision ID: b4e7a1c93d26
Revises: a7d2e5c9b130
Create Date: 2026-10-02 00:00:00.000000
"""
import json
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "b4e7a1c93d26"
down_revision: Union[str, None] = "a7d2e5c9b130"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

RENAMES = {
    "Gecko Grip": "Gecko Crawl",
    "Alleviate Allergy": "Alleviate Nuisance Allergy",
    "Cause Allergy": "Cause Nuisance Allergy",
}


def _rename(spells, names) -> bool:
    changed = False
    for spell in spells if isinstance(spells, list) else []:
        if isinstance(spell, dict) and spell.get("name") in names:
            spell["name"] = names[spell["name"]]
            changed = True
    return changed


def _apply(names) -> None:
    bind = op.get_bind()
    columns = {c["name"] for c in sa.inspect(bind).get_columns("characters")}
    has_state = "chargen_state" in columns
    rows = bind.execute(sa.text(
        f"SELECT id, spells, {'chargen_state' if has_state else 'NULL'} FROM characters"
    )).fetchall()
    for char_id, spells_raw, state_raw in rows:
        try:
            spells = json.loads(spells_raw) if isinstance(spells_raw, str) else spells_raw
            state = json.loads(state_raw) if isinstance(state_raw, str) else state_raw
        except ValueError:
            continue
        if _rename(spells, names):
            bind.execute(sa.text("UPDATE characters SET spells = :v WHERE id = :id"),
                         {"v": json.dumps(spells), "id": char_id})
        if isinstance(state, dict) and _rename(state.get("spells"), names):
            bind.execute(sa.text("UPDATE characters SET chargen_state = :v WHERE id = :id"),
                         {"v": json.dumps(state), "id": char_id})


def upgrade() -> None:
    _apply(RENAMES)


def downgrade() -> None:
    _apply({new: old for old, new in RENAMES.items()})
