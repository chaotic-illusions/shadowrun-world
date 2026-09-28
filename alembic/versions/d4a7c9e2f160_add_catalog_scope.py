"""add_catalog_scope

Revision ID: d4a7c9e2f160
Revises: c8f1a6d4e290
Create Date: 2026-09-23 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "d4a7c9e2f160"
down_revision: Union[str, None] = "c8f1a6d4e290"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    for table in ("organizations", "locations", "characters"):
        op.add_column(
            table,
            sa.Column(
                "catalog_scope",
                sa.String(length=20),
                nullable=False,
                server_default="reference",
            ),
        )


def downgrade() -> None:
    for table in ("characters", "locations", "organizations"):
        with op.batch_alter_table(table) as batch_op:
            batch_op.drop_column("catalog_scope")