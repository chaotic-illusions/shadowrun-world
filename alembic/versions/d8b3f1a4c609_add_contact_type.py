"""add_contact_type

Revision ID: d8b3f1a4c609
Revises: c7e2f9a4b1d3
Create Date: 2026-08-15 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'd8b3f1a4c609'
down_revision: Union[str, None] = 'c7e2f9a4b1d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('contacts', sa.Column('contact_type', sa.String(length=20), nullable=True))


def downgrade() -> None:
    op.drop_column('contacts', 'contact_type')
