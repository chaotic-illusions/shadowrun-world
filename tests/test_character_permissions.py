"""Focused character create/update permission tests."""

import pytest
from fastapi import HTTPException

from app.auth.core import hash_token
from app.models.character import Character
from app.routers.characters import (
    _assert_chargen_grades_allowed,
    _character_create_data,
    _dossier_create_data,
)
from app.schemas.character import CharacterCreate, DossierCommit


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


def test_admin_create_includes_sheet_fields():
    body = CharacterCreate(
        name="Ripper",
        strength=6,
        charisma=2,
        essence=4.5,
        body_index=1.2,
        nuyen=25000,
        good_karma=3,
        lifestyle_level=2,
        priorities={"race": "A", "resources": "B"},
        skills=[{"name": "Firearms", "rating": 6}],
        gear={"weapons": ["Ares Predator"]},
    )

    data = _character_create_data(body, {"is_admin": True, "user_token": None})

    assert data["strength"] == 6
    assert data["essence"] == 4.5
    assert data["nuyen"] == 25000
    assert data["karma_pool"] == 1  # RAW chargen default
    assert data["lifestyle_level"] == 2
    assert data["skills"] == [{"name": "Firearms", "rating": 6}]
    assert data["gear"] == {"weapons": ["Ares Predator"]}


def test_player_create_excludes_sheet_fields():
    body = CharacterCreate(
        name="Switch",
        strength=6,
        essence=3.0,
        nuyen=1000000,
        skills=[{"name": "Firearms", "rating": 6}],
        gear={"weapons": ["Ares Predator"]},
    )

    data = _character_create_data(body, {"is_admin": False, "user_token": "runner-token"})

    for field in ("strength", "essence", "nuyen", "skills", "gear"):
        assert field not in data


def test_lifestyle_name_property_maps_ordinal_to_label():
    char = Character(name="Handle")
    assert char.lifestyle_name is None  # unset
    char.lifestyle_level = 0
    assert char.lifestyle_name == "Street"
    char.lifestyle_level = 3
    assert char.lifestyle_name == "Middle"
    char.lifestyle_level = 5
    assert char.lifestyle_name == "Luxury"


def test_dossier_player_gets_full_sheet_and_ownership():
    body = CharacterCreate(
        name="Wraith",
        strength=6,
        intelligence=6,
        essence=3.5,
        nuyen=25000,
        skills=[{"name": "Firearms", "rating": 6}],
        gear={"weapons": ["Ares Predator"]},
    )

    data = _dossier_create_data(body, {"is_admin": False, "user_token": "runner-token"})

    assert data["is_pc"] is True
    assert data["owner_token"] == hash_token("runner-token")
    assert data["strength"] == 6
    assert data["essence"] == 3.5
    assert data["nuyen"] == 25000
    assert data["skills"] == [{"name": "Firearms", "rating": 6}]
    assert data["gear"] == {"weapons": ["Ares Predator"]}


def test_dossier_admin_claims_full_sheet_to_admin_token():
    body = CharacterCreate(name="NPC Runner", strength=5, nuyen=1000)

    data = _dossier_create_data(body, {"is_admin": True, "user_token": "admin-token"})

    assert data["is_pc"] is True
    assert data["owner_token"] == hash_token("admin-token")
    assert data["strength"] == 5


def test_chargen_grade_gating_blocks_beta_and_delta_for_players():
    # Standard / Alpha are fine for a player.
    _assert_chargen_grades_allowed(
        {"cyber": [{"n": "Datajack", "grade": "Standard"}, {"n": "Smartlink", "grade": "Alpha"}]},
        is_admin=False,
    )
    for gated in ("Beta", "Delta"):
        with pytest.raises(HTTPException) as exc:
            _assert_chargen_grades_allowed({"cyber": [{"n": "Wired Reflexes", "grade": gated}]}, is_admin=False)
        assert exc.value.status_code == 400
    # An admin (GM) may commit any grade -- that is how Delta is applied.
    _assert_chargen_grades_allowed({"cyber": [{"n": "Wired Reflexes", "grade": "Delta"}]}, is_admin=True)


def test_dossier_preserves_draft_flag_for_player():
    body = CharacterCreate(name="Draft Runner", is_draft=True, strength=6)

    data = _dossier_create_data(body, {"is_admin": False, "user_token": "runner-token"})

    assert data["is_draft"] is True
    assert data["owner_token"] == hash_token("runner-token")
    assert data["strength"] == 6


def test_dossier_commit_carries_contacts_but_char_build_excludes_them():
    body = DossierCommit(
        name="Runner",
        strength=5,
        contacts=[{"name": "Fixer Joe", "profession": "Fixer", "loyalty": 3}],
    )

    data = _dossier_create_data(body, {"is_admin": False, "user_token": "t"})

    # Contacts are not Character columns -- they must not leak into the Character build.
    assert "contacts" not in data
    assert data["strength"] == 5
    assert len(body.contacts) == 1
    assert body.contacts[0].name == "Fixer Joe"
    assert body.contacts[0].profession == "Fixer"
    assert body.contacts[0].loyalty == 3
    assert body.contacts[0].connection == 1  # schema default