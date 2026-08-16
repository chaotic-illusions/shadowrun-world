"""add_character_chargen_state

Revision ID: e4a1c7d90b52
Revises: d8b3f1a4c609
Create Date: 2026-08-15 00:30:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'e4a1c7d90b52'
down_revision: Union[str, None] = 'd8b3f1a4c609'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('characters', sa.Column('chargen_state', sa.JSON(), nullable=False, server_default='{}'))


def downgrade() -> None:
    op.drop_column('characters', 'chargen_state')
