"""add_matrix_run_owner_token_hash

Revision ID: f5b2c8a17d33
Revises: e3a9f1b72c04
Create Date: 2026-05-19 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'f5b2c8a17d33'
down_revision: Union[str, None] = 'e3a9f1b72c04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('matrix_runs', sa.Column('owner_token_hash', sa.String(length=64), nullable=True))
    op.create_index('ix_matrix_runs_owner_token_hash', 'matrix_runs', ['owner_token_hash'], unique=False)


def downgrade() -> None:
    op.drop_index('ix_matrix_runs_owner_token_hash', table_name='matrix_runs')
    op.drop_column('matrix_runs', 'owner_token_hash')
