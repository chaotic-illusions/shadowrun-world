"""add_character_deck_builder_state

Revision ID: 4b8f6e2a1d11
Revises: 9f2d1b7c4e66
Create Date: 2026-05-30 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '4b8f6e2a1d11'
down_revision: Union[str, None] = '9f2d1b7c4e66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'characters',
        sa.Column('deck_builder_state', sa.JSON(), nullable=False, server_default=sa.text("'{}'")),
    )


def downgrade() -> None:
    op.drop_column('characters', 'deck_builder_state')
