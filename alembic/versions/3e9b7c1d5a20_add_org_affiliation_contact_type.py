"""add_org_affiliation_contact_type

Lets specific organizations (gangs/tribes) be flagged as runner-affiliable. When
organizations.affiliation_contact_type is "Gang" or "Tribe", a runner can be linked to the org
(spawning a contact of that type + a faction-standing tie that weights rep changes 2x). NULL (the
default) means the org is not a gang/tribe and the runner-affiliation link is unavailable.

Revision ID: 3e9b7c1d5a20
Revises: 7d2f1a6c8e94
Create Date: 2026-08-26 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "3e9b7c1d5a20"
down_revision: Union[str, None] = "7d2f1a6c8e94"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "organizations",
        sa.Column("affiliation_contact_type", sa.String(length=20), nullable=True),
    )


def downgrade() -> None:
    with op.batch_alter_table("organizations") as batch_op:
        batch_op.drop_column("affiliation_contact_type")
