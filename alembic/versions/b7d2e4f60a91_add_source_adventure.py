"""add_source_adventure

Published-adventure provenance for NPCs (characters), locations, and organizations so the
manage pages can filter the world roster by the adventure an entity was lifted from.

Revision ID: b7d2e4f60a91
Revises: a3f5c92e0d17
Create Date: 2026-09-03 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "b7d2e4f60a91"
down_revision: Union[str, None] = "a3f5c92e0d17"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

_TABLES = ("characters", "locations", "organizations")


def upgrade() -> None:
    for table in _TABLES:
        op.add_column(table, sa.Column("source_adventure", sa.String(length=100), nullable=True))
        op.create_index(f"ix_{table}_source_adventure", table, ["source_adventure"])


def downgrade() -> None:
    for table in _TABLES:
        op.drop_index(f"ix_{table}_source_adventure", table_name=table)
        op.drop_column(table, "source_adventure")
