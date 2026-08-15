"""add_character_delta_grade_approved

GM authorization flag for Deltaware cyber (corp-clinic-only, narratively gated).
Admin-set only; defaults False so no existing character is auto-approved.

Revision ID: f3a8d0c21e64
Revises: e2b7c4a91f30
Create Date: 2026-08-12 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "f3a8d0c21e64"
down_revision: Union[str, None] = "e2b7c4a91f30"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "characters",
        sa.Column("delta_grade_approved", sa.Boolean(), nullable=False, server_default=sa.false()),
    )


def downgrade() -> None:
    op.drop_column("characters", "delta_grade_approved")
