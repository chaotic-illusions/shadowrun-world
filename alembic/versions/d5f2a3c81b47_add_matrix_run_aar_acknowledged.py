"""add matrix_runs.aar_acknowledged

Revision ID: d5f2a3c81b47
Revises: c4e7a1b9f200
Create Date: 2026-07-20

Gate: once a run ends, the GM must acknowledge its after-action report before the same decker may
start another run. This boolean tracks that acknowledgement (False until the GM reviews it).
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "d5f2a3c81b47"
down_revision: Union[str, None] = "c4e7a1b9f200"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "matrix_runs",
        sa.Column("aar_acknowledged", sa.Boolean(), nullable=False, server_default=sa.text("0")),
    )


def downgrade() -> None:
    op.drop_column("matrix_runs", "aar_acknowledged")
