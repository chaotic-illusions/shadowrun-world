"""add_character_programming_skills

Revision ID: 7ab3c2f9d1a4
Revises: f5b2c8a17d33
Create Date: 2026-05-26 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '7ab3c2f9d1a4'
down_revision: Union[str, None] = 'f5b2c8a17d33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('characters', sa.Column('computer_skill_enabled', sa.Boolean(), nullable=False, server_default=sa.false()))
    op.add_column('characters', sa.Column('computer_skill_rating', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('characters', sa.Column('software_skill_enabled', sa.Boolean(), nullable=False, server_default=sa.false()))
    op.add_column('characters', sa.Column('software_skill_rating', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('characters', sa.Column('matrix_skill_enabled', sa.Boolean(), nullable=False, server_default=sa.false()))
    op.add_column('characters', sa.Column('matrix_skill_rating', sa.Integer(), nullable=False, server_default='0'))


def downgrade() -> None:
    op.drop_column('characters', 'matrix_skill_rating')
    op.drop_column('characters', 'matrix_skill_enabled')
    op.drop_column('characters', 'software_skill_rating')
    op.drop_column('characters', 'software_skill_enabled')
    op.drop_column('characters', 'computer_skill_rating')
    op.drop_column('characters', 'computer_skill_enabled')
