"""add_character_sheet_fields

Promote the full SR2 character sheet onto real columns: the remaining two
attributes (strength, charisma), essence/body index, magic (rating/type/
tradition/totem), economy (nuyen), karma (pool + good karma), and the ordinal
lifestyle tier. Catalog-heavy chargen lists stay JSON (priorities, skills,
spells, adept_powers, gear).

Revision ID: d7e4b2a9c150
Revises: c9f1a3b6e2d7
Create Date: 2026-08-12 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "d7e4b2a9c150"
down_revision: Union[str, None] = "c9f1a3b6e2d7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("characters", sa.Column("strength", sa.Integer(), nullable=False, server_default="0"))
    op.add_column("characters", sa.Column("charisma", sa.Integer(), nullable=False, server_default="0"))
    op.add_column("characters", sa.Column("essence", sa.Float(), nullable=False, server_default="6.0"))
    op.add_column("characters", sa.Column("body_index", sa.Float(), nullable=False, server_default="0.0"))
    op.add_column("characters", sa.Column("magic_rating", sa.Integer(), nullable=False, server_default="0"))
    op.add_column("characters", sa.Column("magic_type", sa.String(length=50), nullable=True))
    op.add_column("characters", sa.Column("tradition", sa.String(length=50), nullable=True))
    op.add_column("characters", sa.Column("totem", sa.String(length=50), nullable=True))
    op.add_column("characters", sa.Column("nuyen", sa.Integer(), nullable=False, server_default="0"))
    op.add_column("characters", sa.Column("karma_pool", sa.Integer(), nullable=False, server_default="1"))
    op.add_column("characters", sa.Column("good_karma", sa.Integer(), nullable=False, server_default="0"))
    op.add_column("characters", sa.Column("lifestyle_level", sa.Integer(), nullable=True))
    op.add_column("characters", sa.Column("priorities", sa.JSON(), nullable=False, server_default=sa.text("'{}'")))
    op.add_column("characters", sa.Column("skills", sa.JSON(), nullable=False, server_default=sa.text("'[]'")))
    op.add_column("characters", sa.Column("spells", sa.JSON(), nullable=False, server_default=sa.text("'[]'")))
    op.add_column("characters", sa.Column("adept_powers", sa.JSON(), nullable=False, server_default=sa.text("'[]'")))
    op.add_column("characters", sa.Column("gear", sa.JSON(), nullable=False, server_default=sa.text("'{}'")))


def downgrade() -> None:
    for column in (
        "gear",
        "adept_powers",
        "spells",
        "skills",
        "priorities",
        "lifestyle_level",
        "good_karma",
        "karma_pool",
        "nuyen",
        "totem",
        "tradition",
        "magic_type",
        "magic_rating",
        "body_index",
        "essence",
        "charisma",
        "strength",
    ):
        op.drop_column("characters", column)
