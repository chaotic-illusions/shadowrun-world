"""add_matrix_host_id_code

Revision ID: f8a3c1d05e92
Revises: e7c2a9d4f180
Create Date: 2026-06-10 09:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8a3c1d05e92'
down_revision: Union[str, None] = 'e7c2a9d4f180'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('matrix_hosts', sa.Column('id_code', sa.String(length=20), nullable=True))


def downgrade() -> None:
    op.drop_column('matrix_hosts', 'id_code')
