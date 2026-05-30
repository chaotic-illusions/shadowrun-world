"""index matrix_runs.host_id

Revision ID: c1d4a9b3e708
Revises: b7e9d4f23a08
Create Date: 2026-05-24 00:00:00.000000

The original matrix_runs migration created the table without an index on
host_id. Add one now so per-host run lookups don't table-scan as runs accumulate.
Idempotent against deployments where the index was created out-of-band.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'c1d4a9b3e708'
down_revision: Union[str, None] = 'b7e9d4f23a08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing = {ix["name"] for ix in inspector.get_indexes("matrix_runs")}
    if "ix_matrix_runs_host_id" not in existing:
        op.create_index('ix_matrix_runs_host_id', 'matrix_runs', ['host_id'], unique=False)


def downgrade() -> None:
    op.drop_index('ix_matrix_runs_host_id', table_name='matrix_runs')
