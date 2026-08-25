"""Focused character create/update permission tests."""

import asyncio
from contextlib import asynccontextmanager

import pytest
from fastapi import HTTPException
from sqlalchemy.orm.exc import StaleDataError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.auth.core import hash_token
from app.db.base import Base
from app.models.character import Character
from app.routers.characters import (
    _assert_chargen_grades_allowed,
    _assert_gear_grades_allowed,
    _character_create_data,
    _dossier_create_data,
    _validate_hard_gear_caps,
    update_character,
)
from app.schemas.character import CharacterCreate, CharacterUpdate, DossierCommit


# Same throwaway-DB pattern as tests/test_character_lifestyle_flow.py -- calls the real router
# function directly (no HTTP layer needed; FastAPI's dependency injection is just Python here).
@asynccontextmanager
async def _database(path):
    engine = create_async_engine(f"sqlite+aiosqlite:///{path.as_posix()}", connect_args={"timeout": 5})
    sessions = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield sessions
    finally:
        await engine.dispose()


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


def test_validate_hard_gear_caps_allows_gear_within_essence():
    char = Character(name="Chrome", gear={}, chargen_state={})
    # Standard Vehicle Control Rig: baseEss 2.0, grade multiplier 1.0 -- well under 6.0 Essence.
    submitted = {"gear": {"cyber": [{"n": "Vehicle Control Rig", "baseEss": 2.0, "grade": "Standard"}]}}
    _validate_hard_gear_caps(char, submitted)  # must not raise


def test_validate_hard_gear_caps_blocks_essence_over_cap():
    char = Character(name="Chrome", gear={}, chargen_state={})
    submitted = {"gear": {"cyber": [
        {"n": "Wired Reflexes", "baseEss": 4.0, "grade": "Standard"},
        {"n": "Vehicle Control Rig", "baseEss": 3.0, "grade": "Standard"},
    ]}}
    with pytest.raises(HTTPException) as exc:
        _validate_hard_gear_caps(char, submitted)
    assert exc.value.status_code == 422
    assert "Essence" in exc.value.detail


def test_validate_hard_gear_caps_blocks_body_index_over_karma_base_body():
    char = Character(name="Chrome", gear={}, chargen_state={"base": {"body": 3}})
    submitted = {"gear": {"bio": [{"n": "Bone Lacing", "ess": 4.0}]}}
    with pytest.raises(HTTPException) as exc:
        _validate_hard_gear_caps(char, submitted)
    assert exc.value.status_code == 422
    assert "Body Index" in exc.value.detail


def test_validate_hard_gear_caps_skips_body_index_without_stored_base():
    # Older records without a chargen_state.base snapshot skip the Body Index half of the check
    # rather than cap against the wrong (augmented) number -- see _validate_hard_gear_caps.
    char = Character(name="Chrome", gear={}, chargen_state={})
    submitted = {"gear": {"bio": [{"n": "Bone Lacing", "ess": 4.0}]}}
    _validate_hard_gear_caps(char, submitted)  # must not raise


# -- End-to-end coverage for the real PATCH /characters/{id} handler (not just the pure functions
# above) -- calls update_character() directly against a throwaway DB, same pattern
# tests/test_character_lifestyle_flow.py uses.

_OVER_CAP_CYBER_GEAR = {"gear": {"cyber": [
    {"n": "Wired Reflexes", "baseEss": 4.0, "grade": "Standard"},
    {"n": "Vehicle Control Rig", "baseEss": 3.0, "grade": "Standard"},
]}}


def test_patch_character_blocks_essence_over_cap_for_player(tmp_path):
    async def scenario():
        async with _database(tmp_path / "essence_patch.db") as sessions:
            async with sessions() as db:
                char = Character(name="Chrome", is_pc=True, owner_token=hash_token("runner-token"), essence=6.0)
                db.add(char)
                await db.commit()
                char_id = char.id

            async with sessions() as db:
                ctx = {"is_admin": False, "is_user": True, "user_token": "runner-token", "view_as_player": False}
                body = CharacterUpdate(**_OVER_CAP_CYBER_GEAR)
                with pytest.raises(HTTPException) as exc:
                    await update_character(char_id, body, db, ctx)
                assert exc.value.status_code == 422

    asyncio.run(scenario())


def test_patch_character_allows_admin_to_bypass_essence_cap(tmp_path):
    # Enforcement is intentionally scoped to non-admin requests (see update_character) -- a GM can
    # still deliberately hand out over-cap gear for narrative reasons.
    async def scenario():
        async with _database(tmp_path / "essence_admin_patch.db") as sessions:
            async with sessions() as db:
                char = Character(name="Chrome", is_pc=True, owner_token=hash_token("runner-token"), essence=6.0)
                db.add(char)
                await db.commit()
                char_id = char.id

            async with sessions() as db:
                ctx = {"is_admin": True, "is_user": True, "user_token": "admin-token", "view_as_player": False}
                body = CharacterUpdate(**_OVER_CAP_CYBER_GEAR)
                result = await update_character(char_id, body, db, ctx)
                assert result["gear"]["cyber"]

    asyncio.run(scenario())


def test_patch_character_optimistic_lock_rejects_stale_concurrent_write(tmp_path):
    # Two overlapping PATCHes (e.g. two browser tabs) each load the character BEFORE either
    # commits -- the realistic race. The second commit must raise StaleDataError instead of
    # silently clobbering the first write's gear -- see Character.version / __mapper_args__.
    async def scenario():
        async with _database(tmp_path / "optimistic_lock.db") as sessions:
            async with sessions() as db:
                char = Character(name="Chrome", is_pc=True, owner_token=hash_token("runner-token"))
                db.add(char)
                await db.commit()
                char_id = char.id

            async with sessions() as db_a, sessions() as db_b:
                char_a = await db_a.get(Character, char_id)
                char_b = await db_b.get(Character, char_id)  # both tabs see version=0

                char_a.nuyen = 100
                await db_a.commit()  # bumps version to 1

                char_b.nuyen = 200
                with pytest.raises(StaleDataError):
                    await db_b.commit()  # still targets WHERE version=0 -- no row matches

    asyncio.run(scenario())


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


def test_gear_grade_gating_blocks_unapproved_beta_and_delta():
    char = Character(name="Chrome", beta_grade_approved=False, delta_grade_approved=False)
    for gated in ("Beta", "Delta"):
        with pytest.raises(HTTPException) as exc:
            _assert_gear_grades_allowed(char, {"gear": {"cyber": [{"n": "Wired Reflexes", "grade": gated}]}})
        assert exc.value.status_code == 403


def test_gear_grade_gating_allows_approved_grade_only():
    char = Character(name="Chrome", beta_grade_approved=True, delta_grade_approved=False)
    _assert_gear_grades_allowed(char, {"gear": {"cyber": [{"n": "Wired Reflexes", "grade": "Beta"}]}})  # must not raise
    with pytest.raises(HTTPException) as exc:
        _assert_gear_grades_allowed(char, {"gear": {"cyber": [{"n": "Boosted Reflexes", "grade": "Delta"}]}})
    assert exc.value.status_code == 403


def test_gear_grade_gating_ignores_standard_and_alpha():
    char = Character(name="Chrome")  # both approval flags default False
    _assert_gear_grades_allowed(char, {"gear": {"cyber": [
        {"n": "Datajack", "grade": "Standard"}, {"n": "Smartlink", "grade": "Alpha"},
    ]}})  # must not raise


def test_patch_character_blocks_player_from_setting_grade_approval_flags(tmp_path):
    async def scenario():
        async with _database(tmp_path / "grade_approval_flag.db") as sessions:
            async with sessions() as db:
                char = Character(name="Chrome", is_pc=True, owner_token=hash_token("runner-token"))
                db.add(char)
                await db.commit()
                char_id = char.id

            async with sessions() as db:
                ctx = {"is_admin": False, "is_user": True, "user_token": "runner-token", "view_as_player": False}
                body = CharacterUpdate(delta_grade_approved=True)
                with pytest.raises(HTTPException) as exc:
                    await update_character(char_id, body, db, ctx)
                assert exc.value.status_code == 403

    asyncio.run(scenario())


def test_patch_character_blocks_player_gear_patch_with_unapproved_grade(tmp_path):
    async def scenario():
        async with _database(tmp_path / "grade_gear_patch.db") as sessions:
            async with sessions() as db:
                char = Character(name="Chrome", is_pc=True, owner_token=hash_token("runner-token"), essence=6.0)
                db.add(char)
                await db.commit()
                char_id = char.id

            async with sessions() as db:
                ctx = {"is_admin": False, "is_user": True, "user_token": "runner-token", "view_as_player": False}
                body = CharacterUpdate(gear={"cyber": [{"n": "Wired Reflexes", "baseEss": 4.0, "grade": "Beta"}]})
                with pytest.raises(HTTPException) as exc:
                    await update_character(char_id, body, db, ctx)
                assert exc.value.status_code == 403

    asyncio.run(scenario())


def test_patch_character_allows_player_gear_patch_once_gm_approves_grade(tmp_path):
    async def scenario():
        async with _database(tmp_path / "grade_gear_approved.db") as sessions:
            async with sessions() as db:
                char = Character(
                    name="Chrome", is_pc=True, owner_token=hash_token("runner-token"),
                    essence=6.0, beta_grade_approved=True,
                )
                db.add(char)
                await db.commit()
                char_id = char.id

            async with sessions() as db:
                ctx = {"is_admin": False, "is_user": True, "user_token": "runner-token", "view_as_player": False}
                body = CharacterUpdate(gear={"cyber": [{"n": "Wired Reflexes", "baseEss": 4.0, "grade": "Beta"}]})
                result = await update_character(char_id, body, db, ctx)
                assert result["gear"]["cyber"][0]["grade"] == "Beta"

    asyncio.run(scenario())


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