"""Focused character create/update permission tests."""

from app.auth.core import hash_token
from app.routers.characters import _character_create_data
from app.schemas.character import CharacterCreate


def test_player_create_forces_pc_and_ignores_gm_only_fields():
    body = CharacterCreate(
        name="Switch",
        is_pc=False,
        organization_id=42,
        show_background=True,
        connection=6,
        computer_skill_enabled=True,
        computer_skill_rating=12,
        intelligence=9,
        notes="player note",
    )

    data = _character_create_data(
        body,
        {"is_admin": False, "user_token": "runner-token"},
    )

    assert data["is_pc"] is True
    assert data["owner_token"] == hash_token("runner-token")
    assert data["notes"] == "player note"
    assert "organization_id" not in data
    assert "show_background" not in data
    assert "connection" not in data
    assert "computer_skill_enabled" not in data
    assert "computer_skill_rating" not in data
    assert "intelligence" not in data


def test_admin_create_preserves_gm_fields_but_not_submitted_owner_token():
    body = CharacterCreate(
        name="Mr. Johnson",
        is_pc=False,
        organization_id=42,
        owner_token="not-a-server-derived-owner",
    )

    data = _character_create_data(body, {"is_admin": True, "user_token": None})

    assert data["is_pc"] is False
    assert data["organization_id"] == 42
    assert "owner_token" not in data