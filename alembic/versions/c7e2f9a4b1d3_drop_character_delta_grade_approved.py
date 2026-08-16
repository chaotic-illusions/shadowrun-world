"""drop_character_delta_grade_approved

Removes the unused Deltaware GM-authorization flag. The feature was cut, so the
column and every code reference are gone; this drops the leftover column.

Revision ID: c7e2f9a4b1d3
Revises: b2d5f8c1e94a
Create Date: 2026-08-14 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "c7e2f9a4b1d3"
down_revision: Union[str, None] = "b2d5f8c1e94a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("characters") as batch_op:
        batch_op.drop_column("delta_grade_approved")


def downgrade() -> None:
    with op.batch_alter_table("characters") as batch_op:
        batch_op.add_column(
            sa.Column("delta_grade_approved", sa.Boolean(), nullable=False, server_default=sa.false()),
        )
