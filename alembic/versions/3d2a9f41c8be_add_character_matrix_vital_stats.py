"""add_character_matrix_vital_stats

Revision ID: 3d2a9f41c8be
Revises: bab0b2916698
Create Date: 2026-05-28 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '3d2a9f41c8be'
down_revision: Union[str, None] = 'bab0b2916698'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('characters', sa.Column('intelligence', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('characters', sa.Column('quickness', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('characters', sa.Column('willpower', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('characters', sa.Column('body', sa.Integer(), nullable=False, server_default='0'))


def downgrade() -> None:
    op.drop_column('characters', 'body')
    op.drop_column('characters', 'willpower')
    op.drop_column('characters', 'quickness')
    op.drop_column('characters', 'intelligence')
