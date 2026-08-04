"""add_character_math_spu

Revision ID: c9f1a3b6e2d7
Revises: 6b1e4d8a2c73
Create Date: 2026-08-04 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'c9f1a3b6e2d7'
down_revision: Union[str, None] = '6b1e4d8a2c73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('characters', sa.Column('math_spu_enabled', sa.Boolean(), nullable=False, server_default=sa.false()))
    op.add_column('characters', sa.Column('math_spu_rating', sa.Integer(), nullable=False, server_default='0'))


def downgrade() -> None:
    op.drop_column('characters', 'math_spu_rating')
    op.drop_column('characters', 'math_spu_enabled')
