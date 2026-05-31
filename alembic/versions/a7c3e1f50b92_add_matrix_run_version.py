"""add_matrix_run_version

Optimistic-lock counter for matrix_runs (version_id_col). Prevents lost updates
to state_json when concurrent requests mutate the same run.

Revision ID: a7c3e1f50b92
Revises: 4b8f6e2a1d11
Create Date: 2026-05-30 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'a7c3e1f50b92'
down_revision: Union[str, None] = '4b8f6e2a1d11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'matrix_runs',
        sa.Column('version', sa.Integer(), nullable=False, server_default=sa.text('0')),
    )


def downgrade() -> None:
    op.drop_column('matrix_runs', 'version')
