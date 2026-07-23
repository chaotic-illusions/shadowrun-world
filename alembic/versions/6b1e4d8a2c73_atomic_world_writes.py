"""atomic_world_writes

Add the persisted adventure-run allocator and enforce unique run numbers.
Existing duplicate non-null run numbers are retained on their oldest row and
reassigned above the current maximum in stable id order.

Revision ID: 6b1e4d8a2c73
Revises: d5f2a3c81b47
Create Date: 2026-07-23 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "6b1e4d8a2c73"
down_revision: Union[str, None] = "d5f2a3c81b47"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "adventure_run_counter",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("last_run_number", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.execute(
        """
        WITH duplicate_rows AS (
            SELECT id,
                   ROW_NUMBER() OVER (ORDER BY run_number, id) AS offset
              FROM adventure_logs
             WHERE id NOT IN (
                       SELECT MIN(id)
                         FROM adventure_logs
                        WHERE run_number IS NOT NULL
                        GROUP BY run_number
                   )
               AND run_number IS NOT NULL
        ), maximum AS (
            SELECT COALESCE(MAX(run_number), 0) AS value FROM adventure_logs
        )
        UPDATE adventure_logs
           SET run_number = (SELECT value FROM maximum)
                            + (SELECT offset FROM duplicate_rows WHERE duplicate_rows.id = adventure_logs.id)
         WHERE id IN (SELECT id FROM duplicate_rows)
        """
    )
    op.create_index(
        "ux_adventure_logs_run_number",
        "adventure_logs",
        ["run_number"],
        unique=True,
    )
    op.execute(
        "INSERT INTO adventure_run_counter (id, last_run_number) "
        "SELECT 1, COALESCE(MAX(run_number), 0) FROM adventure_logs"
    )


def downgrade() -> None:
    op.drop_index("ux_adventure_logs_run_number", table_name="adventure_logs")
    op.drop_table("adventure_run_counter")