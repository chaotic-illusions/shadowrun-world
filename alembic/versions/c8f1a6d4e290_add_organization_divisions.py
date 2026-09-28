"""add_organization_divisions

Add an embedded, ordered registry for corporate divisions and other sub-organizations.

Revision ID: c8f1a6d4e290
Revises: b7d2e4f60a91
Create Date: 2026-09-20 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "c8f1a6d4e290"
down_revision: Union[str, None] = "b7d2e4f60a91"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "organizations",
        sa.Column("divisions", sa.JSON(), nullable=False, server_default=sa.text("'[]'")),
    )


def downgrade() -> None:
    with op.batch_alter_table("organizations") as batch_op:
        batch_op.drop_column("divisions")