"""drop_house_rules_tighten_matrix_runs

Brings the migrated schema in line with the models: the house_rules table (its model was removed)
is dropped, and matrix_runs' JSON/timestamp columns become NOT NULL as the model declares.

Revision ID: e9b4d2a7c615
Revises: d4a7c9e2f160
Create Date: 2026-09-29 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "e9b4d2a7c615"
down_revision: Union[str, None] = "d4a7c9e2f160"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # IF EXISTS: a DB built by create_all and stamped later never had this table.
    op.execute("DROP INDEX IF EXISTS ix_house_rules_id")
    op.execute("DROP TABLE IF EXISTS house_rules")

    # Fill any NULLs first so the NOT NULL rebuild can't fail on existing rows.
    op.execute("UPDATE matrix_runs SET decker_json = '{}' WHERE decker_json IS NULL")
    op.execute("UPDATE matrix_runs SET state_json = '{}' WHERE state_json IS NULL")
    op.execute("UPDATE matrix_runs SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL")
    op.execute("UPDATE matrix_runs SET updated_at = COALESCE(created_at, CURRENT_TIMESTAMP) WHERE updated_at IS NULL")
    with op.batch_alter_table("matrix_runs") as batch_op:
        batch_op.alter_column("decker_json", existing_type=sa.JSON(), nullable=False)
        batch_op.alter_column("state_json", existing_type=sa.JSON(), nullable=False)
        batch_op.alter_column("created_at", existing_type=sa.DateTime(), nullable=False)
        batch_op.alter_column("updated_at", existing_type=sa.DateTime(), nullable=False)


def downgrade() -> None:
    with op.batch_alter_table("matrix_runs") as batch_op:
        batch_op.alter_column("updated_at", existing_type=sa.DateTime(), nullable=True)
        batch_op.alter_column("created_at", existing_type=sa.DateTime(), nullable=True)
        batch_op.alter_column("state_json", existing_type=sa.JSON(), nullable=True)
        batch_op.alter_column("decker_json", existing_type=sa.JSON(), nullable=True)
    op.create_table(
        "house_rules",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=300), nullable=False),
        sa.Column("category", sa.String(length=100), nullable=True),
        sa.Column("source_reference", sa.String(length=200), nullable=True),
        sa.Column("original_rule", sa.Text(), nullable=True),
        sa.Column("modification", sa.Text(), nullable=False),
        sa.Column("reason", sa.Text(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_house_rules_id"), "house_rules", ["id"], unique=False)
