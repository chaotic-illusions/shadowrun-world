"""add_character_karma_earned

Running total of Karma awarded to a character (SR2 p.190), which decides how much of each award
goes to the Karma Pool. Every character starts the count at 0: no Karma has been awarded on the
sheet before this.

Revision ID: 05052cb8d641
Revises: cfb8c0b1605b
Create Date: 2026-10-04 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "05052cb8d641"
down_revision: Union[str, None] = "cfb8c0b1605b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # The app's startup guard (_ensure_character_sheet_columns) may have added it already.
    columns = {c["name"] for c in sa.inspect(op.get_bind()).get_columns("characters")}
    if "karma_earned" in columns:
        return
    op.add_column("characters", sa.Column("karma_earned", sa.Integer(), nullable=False, server_default="0"))


def downgrade() -> None:
    with op.batch_alter_table("characters") as batch_op:
        batch_op.drop_column("karma_earned")
