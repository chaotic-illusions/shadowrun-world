"""add_campaign_pc_affiliation_backfilled

Runners (PCs) default to "Independent" affiliation. Adds the one-time marker
campaign_state.pc_affiliation_backfilled and, in the same migration, backfills existing PCs to
is_independent=True and flips the marker so the equivalent startup backfill won't re-run (and a
deliberate later "Unknown" on a PC survives restarts). NPCs (default Unknown) are untouched.

Revision ID: 8c1e3f7a2b95
Revises: 3e9b7c1d5a20
Create Date: 2026-08-26 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "8c1e3f7a2b95"
down_revision: Union[str, None] = "3e9b7c1d5a20"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "campaign_state",
        sa.Column("pc_affiliation_backfilled", sa.Boolean(), nullable=False, server_default=sa.false()),
    )
    op.execute("UPDATE characters SET is_independent = 1 WHERE is_pc = 1")
    op.execute("UPDATE campaign_state SET pc_affiliation_backfilled = 1")


def downgrade() -> None:
    with op.batch_alter_table("campaign_state") as batch_op:
        batch_op.drop_column("pc_affiliation_backfilled")
