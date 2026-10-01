"""add_character_origin_pc_id

Contact NPCs remember the runner whose chargen made them (characters.origin_pc_id), so that
runner's player can edit the contact's profile. Backfills existing data:

- Every NPC linked as an individual contact (not Gang/Tribe) of a PC gets that PC as its origin
  -- the first such link wins if an NPC is somehow linked to several runners. That includes
  contacts the GM linked by hand after chargen, which are treated as chargen contacts.
- Those hand-linked contacts carry no contact_type; it's set from Loyalty the same way the play
  sheet already labels them (3+ Buddy, else Contact), so nothing visibly changes.
- Contact type now sets Loyalty (Contact 1, Buddy 3, Follower 6); chargen used to give Followers
  Loyalty 1, so any still at 1 move to 6.

Revision ID: a7d2e5c9b130
Revises: a3f6c1e8d924
Create Date: 2026-10-01 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "a7d2e5c9b130"
down_revision: Union[str, None] = "a3f6c1e8d924"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    # The app's startup guard (_ensure_character_origin_pc_id_column) may have added it already.
    columns = {c["name"] for c in sa.inspect(bind).get_columns("characters")}
    if "origin_pc_id" not in columns:
        op.add_column("characters", sa.Column("origin_pc_id", sa.Integer(), nullable=True))

    links = bind.execute(sa.text(
        "SELECT ct.npc_id, ct.owner_id FROM contacts ct "
        "JOIN characters pc ON pc.id = ct.owner_id JOIN characters npc ON npc.id = ct.npc_id "
        "WHERE pc.is_pc = 1 AND npc.is_pc = 0 AND COALESCE(ct.contact_type, '') NOT IN ('Gang', 'Tribe') "
        "ORDER BY ct.id"
    )).fetchall()
    for npc_id, pc_id in links:
        bind.execute(
            sa.text("UPDATE characters SET origin_pc_id = :pc WHERE id = :npc AND origin_pc_id IS NULL"),
            {"pc": pc_id, "npc": npc_id},
        )

    bind.execute(sa.text(
        "UPDATE contacts SET contact_type = CASE WHEN loyalty >= 3 THEN 'Buddy' ELSE 'Contact' END "
        "WHERE contact_type IS NULL AND npc_id IS NOT NULL "
        "AND owner_id IN (SELECT id FROM characters WHERE is_pc = 1)"
    ))
    bind.execute(sa.text("UPDATE contacts SET loyalty = 6 WHERE contact_type = 'Follower' AND loyalty = 1"))


def downgrade() -> None:
    # The contact_type/loyalty backfill isn't reversed: the old values aren't recorded, and the new
    # ones match what the play sheet already showed.
    op.drop_column("characters", "origin_pc_id")
