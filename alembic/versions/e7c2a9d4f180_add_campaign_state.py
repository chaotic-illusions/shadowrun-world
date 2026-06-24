"""add_campaign_state

Single-row campaign clock store. The campaign tick (1 tick = 1 day) becomes the
single source of truth for time passing in the world; heat / public-awareness /
org-standing decay are computed from elapsed ticks. Seeds the row from the legacy
per-log tick total so existing decay stamps stay continuous.

Revision ID: e7c2a9d4f180
Revises: a7c3e1f50b92
Create Date: 2026-06-12 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'e7c2a9d4f180'
down_revision: Union[str, None] = 'a7c3e1f50b92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'campaign_state',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('current_tick', sa.Integer(), nullable=False, server_default=sa.text('0')),
        sa.PrimaryKeyConstraint('id'),
    )
    # Seed the single row, carrying forward the legacy tick total for continuity.
    op.execute(
        "INSERT INTO campaign_state (id, current_tick) "
        "SELECT 1, COALESCE(SUM(tick_count), 0) FROM adventure_logs"
    )


def downgrade() -> None:
    op.drop_table('campaign_state')
