"""drop_lifestyle_upkeep_and_standing_decay

The lifestyle upkeep engine is gone (players track their own nuyen), and org standings no
longer decay, so their clock stamps are dead: drop `characters.lifestyle_paid_tick` and
`org_standings.standings_stamped_tick`.

Revision ID: a8f3d61c2b47
Revises: 05052cb8d641
Create Date: 2026-10-08 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "a8f3d61c2b47"
down_revision: Union[str, None] = "05052cb8d641"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def _columns(table: str) -> set[str]:
    return {c["name"] for c in sa.inspect(op.get_bind()).get_columns(table)}


def upgrade() -> None:
    if "lifestyle_paid_tick" in _columns("characters"):
        with op.batch_alter_table("characters") as batch_op:
            batch_op.drop_column("lifestyle_paid_tick")
    if "standings_stamped_tick" in _columns("org_standings"):
        with op.batch_alter_table("org_standings") as batch_op:
            batch_op.drop_column("standings_stamped_tick")


def downgrade() -> None:
    op.add_column("org_standings", sa.Column("standings_stamped_tick", sa.Integer(), nullable=True, server_default="0"))
    op.add_column("characters", sa.Column("lifestyle_paid_tick", sa.Integer(), nullable=True))
