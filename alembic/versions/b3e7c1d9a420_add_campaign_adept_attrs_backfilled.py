"""add_campaign_adept_attrs_backfilled

One-time marker for the startup backfill that adds Improved Physical Attributes levels to existing
adepts' stored attributes (app/main.py _backfill_adept_attrs_once).

Revision ID: b3e7c1d9a420
Revises: a8f3d61c2b47
Create Date: 2026-11-22 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "b3e7c1d9a420"
down_revision: Union[str, None] = "a8f3d61c2b47"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def _columns(table: str) -> set[str]:
    return {c["name"] for c in sa.inspect(op.get_bind()).get_columns(table)}


def upgrade() -> None:
    if "adept_attrs_backfilled" not in _columns("campaign_state"):
        op.add_column(
            "campaign_state",
            sa.Column("adept_attrs_backfilled", sa.Boolean(), nullable=False, server_default=sa.false()),
        )


def downgrade() -> None:
    with op.batch_alter_table("campaign_state") as batch_op:
        batch_op.drop_column("adept_attrs_backfilled")
