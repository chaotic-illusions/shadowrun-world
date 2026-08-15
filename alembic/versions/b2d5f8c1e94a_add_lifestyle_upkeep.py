"""add_lifestyle_upkeep

Lifestyle upkeep engine columns: `lifestyle_permanent` (a lifestyle bought outright
is never charged monthly rent) and `lifestyle_paid_tick` (the campaign tick through
which upkeep has been settled). Both default to "no upkeep owed yet" so existing rows
are never billed back-rent. See app/services/lifestyle.py.

Revision ID: b2d5f8c1e94a
Revises: a1c9e7b3f52d
Create Date: 2026-08-12 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "b2d5f8c1e94a"
down_revision: Union[str, None] = "a1c9e7b3f52d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "characters",
        sa.Column("lifestyle_permanent", sa.Boolean(), nullable=False, server_default=sa.false()),
    )
    op.add_column(
        "characters",
        sa.Column("lifestyle_paid_tick", sa.Integer(), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("characters", "lifestyle_paid_tick")
    op.drop_column("characters", "lifestyle_permanent")
