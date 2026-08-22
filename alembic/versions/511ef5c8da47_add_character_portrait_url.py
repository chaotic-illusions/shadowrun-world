"""add_character_portrait_url

Revision ID: 511ef5c8da47
Revises: b7e4f291a6c8
Create Date: 2026-08-20 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '511ef5c8da47'
down_revision: Union[str, None] = 'b7e4f291a6c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('characters', sa.Column('portrait_url', sa.String(length=500), nullable=True))


def downgrade() -> None:
    op.drop_column('characters', 'portrait_url')
