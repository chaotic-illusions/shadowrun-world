"""add_character_computer_br_skill

Revision ID: 9f2d1b7c4e66
Revises: 3d2a9f41c8be
Create Date: 2026-05-29 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '9f2d1b7c4e66'
down_revision: Union[str, None] = '3d2a9f41c8be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('characters', sa.Column('computer_br_skill_enabled', sa.Boolean(), nullable=False, server_default=sa.false()))
    op.add_column('characters', sa.Column('computer_br_skill_rating', sa.Integer(), nullable=False, server_default='0'))


def downgrade() -> None:
    op.drop_column('characters', 'computer_br_skill_rating')
    op.drop_column('characters', 'computer_br_skill_enabled')
