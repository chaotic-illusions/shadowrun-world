"""add_character_is_independent

Splits the single "Independent / Unknown" affiliation choice into two distinct states for
NPCs. When characters.organization_id is null, is_independent=True means deliberately
unaffiliated ("Independent") while False (the default) means ties are unknown ("Unknown").
Default False so every existing NPC keeps its current "Unknown" display.

Revision ID: 7d2f1a6c8e94
Revises: a1c4e7f209b6
Create Date: 2026-08-25 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "7d2f1a6c8e94"
down_revision: Union[str, None] = "a1c4e7f209b6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "characters",
        sa.Column("is_independent", sa.Boolean(), nullable=False, server_default=sa.false()),
    )


def downgrade() -> None:
    with op.batch_alter_table("characters") as batch_op:
        batch_op.drop_column("is_independent")
