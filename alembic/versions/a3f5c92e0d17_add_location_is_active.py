"""add_location_is_active

Revision ID: a3f5c92e0d17
Revises: 8c1e3f7a2b95
Create Date: 2026-08-30 12:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3f5c92e0d17'
down_revision: Union[str, None] = '8c1e3f7a2b95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Existing locations were always visible to players; default them active so this
    # column addition doesn't hide anything that was already discovered.
    op.add_column('locations', sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.true()))


def downgrade() -> None:
    op.drop_column('locations', 'is_active')
