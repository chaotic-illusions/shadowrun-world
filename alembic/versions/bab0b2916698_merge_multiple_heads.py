"""Merge multiple heads

Revision ID: bab0b2916698
Revises: 7ab3c2f9d1a4, a3f1c8d92e47, c1d4a9b3e708
Create Date: 2026-05-26 21:58:16.191906
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bab0b2916698'
down_revision: Union[str, None] = ('7ab3c2f9d1a4', 'a3f1c8d92e47', 'c1d4a9b3e708')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
