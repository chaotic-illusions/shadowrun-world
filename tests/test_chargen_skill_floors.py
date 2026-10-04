"""A finished chargen sheet can't carry a skill below general 1, or more than one Concentration or
Specialization on a skill (SR2 pp.45, 70) -- whatever the builder page did. Drafts aren't checked:
they are saved mid-wizard.

Throwaway aiosqlite DB, router functions called directly (same pattern as
tests/test_dossier_gm_fields.py).
"""
import asyncio

import pytest
from fastapi import HTTPException

from app.models.character import Character
from app.routers.characters import convert_character_dossier, create_character_dossier, finalize_character_dossier
from app.schemas.character import DossierCommit
from tests.test_chargen_contacts import STARTING_CONTACTS
from tests.test_dossier_gm_fields import ADMIN, _database

GOOD = [
    {"name": "Firearms", "rating": 1, "concs": [{"name": "Pistols", "rating": 3}],
     "specs": [{"name": "Ares Predator", "rating": 5, "conc": "Pistols"}]},
    {"name": "Etiquette", "rating": 1, "concs": [{"name": "Street", "rating": 3}], "specs": []},
    {"name": "Stealth", "rating": 1, "concs": [], "specs": []},
]
BAD = {
    "general 0 after a Concentration": [{"name": "Etiquette", "rating": 0, "concs": [{"name": "Corporate", "rating": 2}], "specs": []}],
    "general 0": [{"name": "Stealth", "rating": 0, "concs": [], "specs": []}],
    "two Concentrations": [{"name": "Bike", "rating": 2, "concs": [{"name": "Two-wheeler", "rating": 4},
                                                                     {"name": "Racing", "rating": 3}], "specs": []}],
    "two Specializations": [{"name": "Firearms", "rating": 1, "concs": [{"name": "Pistols", "rating": 3}],
                             "specs": [{"name": "Ares Predator", "rating": 5, "conc": "Pistols"},
                                       {"name": "Colt America L36", "rating": 5, "conc": "Pistols"}]}],
}


def _create(tmp_path, skills, **extra):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            async with sessions() as db:
                body = DossierCommit(name="Chancer", skills=skills, contacts=STARTING_CONTACTS, **extra)
                return await create_character_dossier(body=body, db=db, ctx=ADMIN)
    return asyncio.run(scenario())


def test_valid_skills_commit(tmp_path):
    assert _create(tmp_path, GOOD)["skills"] == GOOD


@pytest.mark.parametrize("case", list(BAD))
def test_bad_skill_is_rejected(tmp_path, case):
    with pytest.raises(HTTPException) as exc:
        _create(tmp_path, BAD[case])
    assert exc.value.status_code == 422
    assert BAD[case][0]["name"] in exc.value.detail


def test_draft_is_not_checked(tmp_path):
    assert _create(tmp_path, BAD["general 0"], is_draft=True)["is_draft"] is True


@pytest.mark.parametrize("route", ["finalize", "convert"])
def test_finalize_and_convert_are_checked(tmp_path, route):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            async with sessions() as db:
                db.add(Character(id=5, name="Runner", is_pc=True, is_draft=route == "finalize"))
                await db.commit()
            endpoint = finalize_character_dossier if route == "finalize" else convert_character_dossier
            async with sessions() as db:
                body = DossierCommit(name="Runner", skills=BAD["general 0"], contacts=STARTING_CONTACTS)
                await endpoint(character_id=5, body=body, db=db, ctx=ADMIN)
    with pytest.raises(HTTPException) as exc:
        asyncio.run(scenario())
    assert exc.value.status_code == 422
