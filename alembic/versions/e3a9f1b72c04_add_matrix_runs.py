"""add_matrix_runs

Revision ID: e3a9f1b72c04
Revises: d516fa2eeebe
Create Date: 2026-05-14 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'e3a9f1b72c04'
down_revision: Union[str, None] = 'd516fa2eeebe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'matrix_runs',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('host_id', sa.Integer(),
                  sa.ForeignKey('matrix_hosts.id', ondelete='SET NULL'), nullable=True),
        sa.Column('decker_json', sa.JSON(), nullable=True),
        sa.Column('state_json',  sa.JSON(), nullable=True),
        sa.Column('status', sa.String(20), nullable=False, server_default='active'),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )
    op.create_index('ix_matrix_runs_id', 'matrix_runs', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index('ix_matrix_runs_id', table_name='matrix_runs')
    op.drop_table('matrix_runs')
