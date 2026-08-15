"""add_character_is_draft

Chargen draft flag: an in-progress character-builder PC that is hidden from every
character list until the wizard finalizes it. Defaults False so no existing row is
treated as a draft.

Revision ID: a1c9e7b3f52d
Revises: f3a8d0c21e64
Create Date: 2026-08-12 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "a1c9e7b3f52d"
down_revision: Union[str, None] = "f3a8d0c21e64"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "characters",
        sa.Column("is_draft", sa.Boolean(), nullable=False, server_default=sa.false()),
    )


def downgrade() -> None:
    op.drop_column("characters", "is_draft")
