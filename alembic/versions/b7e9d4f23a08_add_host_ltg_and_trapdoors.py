"""add_host_ltg_and_trapdoors

Revision ID: b7e9d4f23a08
Revises: f5b2c8a17d33
Create Date: 2026-05-19 00:00:01.000000

Adds ltg_address (String) and trap_doors_json (JSON) to matrix_hosts.
Replaces the ad-hoc ALTER TABLE migration that previously lived in app/main.py.
Uses batch_alter_table so SQLite (which can't ADD COLUMN with non-trivial types
in some cases) recreates the table cleanly.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'b7e9d4f23a08'
down_revision: Union[str, None] = 'f5b2c8a17d33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Inspect first so re-running on an instance where the ad-hoc migration already
    # added these columns is a no-op rather than an error.
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing = {col["name"] for col in inspector.get_columns("matrix_hosts")}

    with op.batch_alter_table("matrix_hosts") as batch:
        if "ltg_address" not in existing:
            batch.add_column(sa.Column("ltg_address", sa.String(length=100), nullable=True))
        if "trap_doors_json" not in existing:
            batch.add_column(sa.Column("trap_doors_json", sa.JSON(), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table("matrix_hosts") as batch:
        batch.drop_column("trap_doors_json")
        batch.drop_column("ltg_address")
