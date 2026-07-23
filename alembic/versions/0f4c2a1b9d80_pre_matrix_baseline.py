"""pre_matrix_baseline

Core schema snapshot immediately before the first matrix migration. This makes
the Alembic history self-contained for empty databases while preserving every
previously published revision identifier.

Revision ID: 0f4c2a1b9d80
Revises:
Create Date: 2026-07-23 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0f4c2a1b9d80"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "organizations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("org_type", sa.String(length=100), nullable=True),
        sa.Column("tier", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("headquarters", sa.String(length=200), nullable=True),
        sa.Column("leadership", sa.JSON(), nullable=False),
        sa.Column("ltgs", sa.JSON(), nullable=False),
        sa.Column("ally_ids", sa.JSON(), nullable=False),
        sa.Column("enemy_ids", sa.JSON(), nullable=False),
        sa.Column("revealed_ally_ids", sa.JSON(), nullable=False),
        sa.Column("revealed_enemy_ids", sa.JSON(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_organizations_id"), "organizations", ["id"], unique=False)
    op.create_index(op.f("ix_organizations_name"), "organizations", ["name"], unique=False)

    op.create_table(
        "auth_user_tokens",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("token_hash", sa.String(length=64), nullable=False),
        sa.Column("label", sa.String(length=200), nullable=True),
        sa.Column("is_admin", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_auth_user_tokens_id"), "auth_user_tokens", ["id"], unique=False)
    op.create_index(
        op.f("ix_auth_user_tokens_token_hash"),
        "auth_user_tokens",
        ["token_hash"],
        unique=True,
    )

    op.create_table(
        "house_rules",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=300), nullable=False),
        sa.Column("category", sa.String(length=100), nullable=True),
        sa.Column("source_reference", sa.String(length=200), nullable=True),
        sa.Column("original_rule", sa.Text(), nullable=True),
        sa.Column("modification", sa.Text(), nullable=False),
        sa.Column("reason", sa.Text(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_house_rules_id"), "house_rules", ["id"], unique=False)

    op.create_table(
        "rtgs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("code", sa.String(length=50), nullable=False),
        sa.Column("region", sa.String(length=200), nullable=False),
        sa.Column("political_entity", sa.String(length=200), nullable=True),
        sa.Column("continent", sa.String(length=100), nullable=True),
        sa.Column("rtg_security_rating", sa.String(length=20), nullable=True),
        sa.Column("canonical", sa.Boolean(), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_rtgs_code"), "rtgs", ["code"], unique=True)
    op.create_index(op.f("ix_rtgs_id"), "rtgs", ["id"], unique=False)

    op.create_table(
        "characters",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("is_pc", sa.Boolean(), nullable=False),
        sa.Column("archetype", sa.String(length=100), nullable=True),
        sa.Column("title", sa.String(length=200), nullable=True),
        sa.Column("race", sa.String(length=50), nullable=False),
        sa.Column("nationality", sa.String(length=100), nullable=True),
        sa.Column("gender", sa.String(length=50), nullable=True),
        sa.Column("age", sa.Integer(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("background", sa.Text(), nullable=True),
        sa.Column("show_background", sa.Boolean(), nullable=False),
        sa.Column("contact_skills", sa.JSON(), nullable=False),
        sa.Column("connection", sa.Integer(), nullable=False),
        sa.Column("organization_id", sa.Integer(), nullable=True),
        sa.Column("karma_total", sa.Integer(), nullable=False),
        sa.Column("karma_current", sa.Integer(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("owner_token", sa.String(length=64), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_characters_id"), "characters", ["id"], unique=False)
    op.create_index(op.f("ix_characters_name"), "characters", ["name"], unique=False)
    op.create_index(op.f("ix_characters_owner_token"), "characters", ["owner_token"], unique=False)

    op.create_table(
        "locations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("location_type", sa.String(length=100), nullable=True),
        sa.Column("city", sa.String(length=100), nullable=True),
        sa.Column("district", sa.String(length=100), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("security_level", sa.String(length=50), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("controlling_org_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["controlling_org_id"], ["organizations.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_locations_id"), "locations", ["id"], unique=False)
    op.create_index(op.f("ix_locations_name"), "locations", ["name"], unique=False)

    op.create_table(
        "adventure_logs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=300), nullable=False),
        sa.Column("session_date", sa.Date(), nullable=False),
        sa.Column("run_number", sa.Integer(), nullable=True),
        sa.Column("objective", sa.Text(), nullable=False),
        sa.Column("result", sa.Text(), nullable=False),
        sa.Column("outcome", sa.String(length=50), nullable=True),
        sa.Column("payout", sa.String(length=300), nullable=True),
        sa.Column("casualties", sa.Text(), nullable=True),
        sa.Column("outcome_tags", sa.JSON(), nullable=False),
        sa.Column("consequences_suggested", sa.JSON(), nullable=False),
        sa.Column("consequences_active", sa.JSON(), nullable=False),
        sa.Column("heat", sa.Integer(), nullable=False),
        sa.Column("tick_count", sa.Integer(), nullable=False),
        sa.Column("employer", sa.String(length=200), nullable=True),
        sa.Column("changes_applied", sa.JSON(), nullable=False),
        sa.Column("changes_excluded", sa.JSON(), nullable=False),
        sa.Column("gm_notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_adventure_logs_id"), "adventure_logs", ["id"], unique=False)

    op.create_table(
        "contacts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("profession", sa.String(length=100), nullable=True),
        sa.Column("race", sa.String(length=50), nullable=True),
        sa.Column("loyalty", sa.Integer(), nullable=False),
        sa.Column("connection", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=False),
        sa.Column("npc_id", sa.Integer(), nullable=True),
        sa.Column("location_id", sa.Integer(), nullable=True),
        sa.Column("organization_id", sa.Integer(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.CheckConstraint("connection >= 1 AND connection <= 6", name="ck_contact_connection"),
        sa.CheckConstraint("loyalty >= 1 AND loyalty <= 6", name="ck_contact_loyalty"),
        sa.ForeignKeyConstraint(["location_id"], ["locations.id"]),
        sa.ForeignKeyConstraint(["npc_id"], ["characters.id"]),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.ForeignKeyConstraint(["owner_id"], ["characters.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_contacts_id"), "contacts", ["id"], unique=False)
    op.create_index(op.f("ix_contacts_name"), "contacts", ["name"], unique=False)

    op.create_table(
        "reputations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("character_id", sa.Integer(), nullable=False),
        sa.Column("street_cred", sa.Integer(), nullable=False),
        sa.Column("notoriety", sa.Integer(), nullable=False),
        sa.Column("public_awareness", sa.Integer(), nullable=False),
        sa.Column("pa_updated_at", sa.Date(), nullable=True),
        sa.Column("heat", sa.Integer(), nullable=False),
        sa.Column("heat_updated_at", sa.Date(), nullable=True),
        sa.Column("heat_stamped_tick", sa.Integer(), nullable=False),
        sa.Column("pa_stamped_tick", sa.Integer(), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["character_id"], ["characters.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("character_id"),
    )
    op.create_index(op.f("ix_reputations_id"), "reputations", ["id"], unique=False)

    op.create_table(
        "org_standings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("character_id", sa.Integer(), nullable=False),
        sa.Column("organization_id", sa.Integer(), nullable=False),
        sa.Column("standing", sa.Integer(), nullable=False),
        sa.Column("standings_updated_at", sa.Date(), nullable=True),
        sa.Column("standings_stamped_tick", sa.Integer(), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["character_id"], ["characters.id"]),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("character_id", "organization_id", name="uq_org_standing_char_org"),
    )
    op.create_index(op.f("ix_org_standings_id"), "org_standings", ["id"], unique=False)

    op.create_table(
        "log_characters",
        sa.Column("log_id", sa.Integer(), nullable=False),
        sa.Column("character_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["character_id"], ["characters.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["log_id"], ["adventure_logs.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("log_id", "character_id"),
    )
    op.create_table(
        "log_locations",
        sa.Column("log_id", sa.Integer(), nullable=False),
        sa.Column("location_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["location_id"], ["locations.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["log_id"], ["adventure_logs.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("log_id", "location_id"),
    )
    op.create_table(
        "log_organizations",
        sa.Column("log_id", sa.Integer(), nullable=False),
        sa.Column("organization_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["log_id"], ["adventure_logs.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("log_id", "organization_id"),
    )


def downgrade() -> None:
    op.drop_table("log_organizations")
    op.drop_table("log_locations")
    op.drop_table("log_characters")
    op.drop_index(op.f("ix_org_standings_id"), table_name="org_standings")
    op.drop_table("org_standings")
    op.drop_index(op.f("ix_reputations_id"), table_name="reputations")
    op.drop_table("reputations")
    op.drop_index(op.f("ix_contacts_name"), table_name="contacts")
    op.drop_index(op.f("ix_contacts_id"), table_name="contacts")
    op.drop_table("contacts")
    op.drop_index(op.f("ix_adventure_logs_id"), table_name="adventure_logs")
    op.drop_table("adventure_logs")
    op.drop_index(op.f("ix_locations_name"), table_name="locations")
    op.drop_index(op.f("ix_locations_id"), table_name="locations")
    op.drop_table("locations")
    op.drop_index(op.f("ix_characters_owner_token"), table_name="characters")
    op.drop_index(op.f("ix_characters_name"), table_name="characters")
    op.drop_index(op.f("ix_characters_id"), table_name="characters")
    op.drop_table("characters")
    op.drop_index(op.f("ix_rtgs_id"), table_name="rtgs")
    op.drop_index(op.f("ix_rtgs_code"), table_name="rtgs")
    op.drop_table("rtgs")
    op.drop_index(op.f("ix_house_rules_id"), table_name="house_rules")
    op.drop_table("house_rules")
    op.drop_index(op.f("ix_auth_user_tokens_token_hash"), table_name="auth_user_tokens")
    op.drop_index(op.f("ix_auth_user_tokens_id"), table_name="auth_user_tokens")
    op.drop_table("auth_user_tokens")
    op.drop_index(op.f("ix_organizations_name"), table_name="organizations")
    op.drop_index(op.f("ix_organizations_id"), table_name="organizations")
    op.drop_table("organizations")