"""add_campaign_team_karma

The shadowrunning team's Karma Pool (SR2 p.191). A new team starts with 2 (p.47); only a GM
changes it, from the world-state page.

Revision ID: cfb8c0b1605b
Revises: 5598c8b91789
Create Date: 2026-10-04 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "cfb8c0b1605b"
down_revision: Union[str, None] = "5598c8b91789"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # The app's startup guard (_ensure_campaign_team_karma_column) may have added it already.
    columns = {c["name"] for c in sa.inspect(op.get_bind()).get_columns("campaign_state")}
    if "team_karma" in columns:
        return
    op.add_column(
        "campaign_state",
        sa.Column("team_karma", sa.Integer(), nullable=False, server_default="2"),
    )


def downgrade() -> None:
    with op.batch_alter_table("campaign_state") as batch_op:
        batch_op.drop_column("team_karma")
