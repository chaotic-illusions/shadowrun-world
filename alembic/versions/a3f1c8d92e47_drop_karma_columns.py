"""drop_karma_columns

Revision ID: a3f1c8d92e47
Revises: d516fa2eeebe
Create Date: 2026-04-08 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3f1c8d92e47'
down_revision: Union[str, None] = 'd516fa2eeebe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('characters') as batch_op:
        batch_op.drop_column('karma_total')
        batch_op.drop_column('karma_current')


def downgrade() -> None:
    with op.batch_alter_table('characters') as batch_op:
        batch_op.add_column(sa.Column('karma_current', sa.Integer(), nullable=False, server_default='0'))
        batch_op.add_column(sa.Column('karma_total', sa.Integer(), nullable=False, server_default='0'))
