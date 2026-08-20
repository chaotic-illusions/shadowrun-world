"""add_character_condition_monitor

Revision ID: b7e4f291a6c8
Revises: e4a1c7d90b52
Create Date: 2026-08-20 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7e4f291a6c8'
down_revision: Union[str, None] = 'e4a1c7d90b52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('characters') as batch_op:
        batch_op.add_column(sa.Column('physical_damage', sa.Integer(), nullable=False, server_default='0'))
        batch_op.add_column(sa.Column('stun_damage', sa.Integer(), nullable=False, server_default='0'))
        batch_op.add_column(sa.Column('physical_overflow', sa.Integer(), nullable=False, server_default='0'))


def downgrade() -> None:
    with op.batch_alter_table('characters') as batch_op:
        batch_op.drop_column('physical_overflow')
        batch_op.drop_column('stun_damage')
        batch_op.drop_column('physical_damage')
