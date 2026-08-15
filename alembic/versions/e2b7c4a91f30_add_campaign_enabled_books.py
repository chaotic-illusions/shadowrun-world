"""add_campaign_enabled_books

Add the per-campaign sourcebook toggle list to the campaign_state singleton.
Empty means SR2 core only (SR2 is always implicitly enabled).

Revision ID: e2b7c4a91f30
Revises: d7e4b2a9c150
Create Date: 2026-08-12 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "e2b7c4a91f30"
down_revision: Union[str, None] = "d7e4b2a9c150"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "campaign_state",
        sa.Column("enabled_books", sa.JSON(), nullable=False, server_default=sa.text("'[]'")),
    )


def downgrade() -> None:
    op.drop_column("campaign_state", "enabled_books")
