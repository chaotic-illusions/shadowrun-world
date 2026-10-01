"""drop_fan_content_book_toggle

The fan-made sourcebooks (Blackhand's Street Weapons 2057, Running Gear) and their "FAN" toggle
were removed from the catalog. Strip "FAN" from campaign_state.enabled_books so the stored setting
matches what the app can offer. A no-op when the toggle was never switched on.

Revision ID: a3f6c1e8d924
Revises: e9b4d2a7c615
Create Date: 2026-10-01 00:00:00.000000
"""
import json
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "a3f6c1e8d924"
down_revision: Union[str, None] = "e9b4d2a7c615"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    rows = bind.execute(sa.text("SELECT id, enabled_books FROM campaign_state")).fetchall()
    for row_id, raw in rows:
        books = json.loads(raw) if isinstance(raw, str) else (raw or [])
        if "FAN" in books:
            bind.execute(
                sa.text("UPDATE campaign_state SET enabled_books = :books WHERE id = :id"),
                {"books": json.dumps([b for b in books if b != "FAN"]), "id": row_id},
            )


def downgrade() -> None:
    # Whether FAN was on before is not recorded; the fan catalogs are gone either way.
    pass
