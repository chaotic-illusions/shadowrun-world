"""add_character_grade_approval

GM authorization flags for Beta/Delta-grade cyberware (post-chargen career/GM-only
purchases, narratively gated). Admin-set only; default False so no existing character
is auto-approved. Reintroduces the Deltaware half of the flag dropped in
c7e2f9a4b1d3 (that cut feature had no UI to set it; this one does), adding a Betaware
sibling alongside it.

Revision ID: a1c4e7f209b6
Revises: 5a3703fa52ad
Create Date: 2026-08-24 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "a1c4e7f209b6"
down_revision: Union[str, None] = "5a3703fa52ad"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "characters",
        sa.Column("beta_grade_approved", sa.Boolean(), nullable=False, server_default=sa.false()),
    )
    op.add_column(
        "characters",
        sa.Column("delta_grade_approved", sa.Boolean(), nullable=False, server_default=sa.false()),
    )


def downgrade() -> None:
    with op.batch_alter_table("characters") as batch_op:
        batch_op.drop_column("delta_grade_approved")
        batch_op.drop_column("beta_grade_approved")
