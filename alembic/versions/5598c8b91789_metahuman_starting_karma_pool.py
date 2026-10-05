"""metahuman_starting_karma_pool

SR2 p.47: metahumans begin with 2 points in their Karma Pool, humans with 1 (the More
Metahumans optional rule, which this campaign doesn't use, would drop metahumans to 1).
Chargen gave everyone 1, so every finished metahuman PC gets the missing point here. It's
added rather than set, so any pool already earned through Karma is kept.

Revision ID: 5598c8b91789
Revises: d8a3f0b6c215
Create Date: 2026-10-04 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op


revision: str = "5598c8b91789"
down_revision: Union[str, None] = "d8a3f0b6c215"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

_METAHUMAN_PCS = "is_pc = 1 AND is_draft = 0 AND race IS NOT NULL AND race != 'Human'"


def upgrade() -> None:
    op.execute(f"UPDATE characters SET karma_pool = karma_pool + 1 WHERE {_METAHUMAN_PCS}")


def downgrade() -> None:
    op.execute(f"UPDATE characters SET karma_pool = MAX(karma_pool - 1, 0) WHERE {_METAHUMAN_PCS}")
