"""add_matrix_host_trap_dest

Revision ID: c4e7a1b9f200
Revises: f8a3c1d05e92
Create Date: 2026-06-26 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4e7a1b9f200'
down_revision: Union[str, None] = 'f8a3c1d05e92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'matrix_hosts',
        sa.Column('is_trap_door_dest', sa.Boolean(), nullable=False, server_default=sa.text('0')),
    )


def downgrade() -> None:
    op.drop_column('matrix_hosts', 'is_trap_door_dest')
