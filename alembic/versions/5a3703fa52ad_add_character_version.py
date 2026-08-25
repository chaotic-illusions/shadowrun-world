"""add_character_version

Optimistic-lock counter for characters (version_id_col). Prevents lost updates
when concurrent PATCHes replace the whole `gear`/`chargen_state` JSON blob at once
(e.g. two browser tabs buying gear before either response lands).

Revision ID: 5a3703fa52ad
Revises: 511ef5c8da47
Create Date: 2026-08-25 00:28:31.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '5a3703fa52ad'
down_revision: Union[str, None] = '511ef5c8da47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'characters',
        sa.Column('version', sa.Integer(), nullable=False, server_default=sa.text('0')),
    )


def downgrade() -> None:
    op.drop_column('characters', 'version')
