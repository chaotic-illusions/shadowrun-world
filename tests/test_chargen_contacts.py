"""A finished chargen sheet needs its two starting contacts (SR2 p.43), one of which may be upgraded
to a Buddy -- but only one Buddy -- and at most five Followers from different archetypes (p.44),
whatever the builder page did. More Contacts and Gang/Tribe ties can be added freely but don't
stand in for the two. Drafts aren't checked: they are saved mid-wizard.

Throwaway aiosqlite DB, router functions called directly (same pattern as
tests/test_dossier_gm_fields.py).
"""
import asyncio

import pytest
from fastapi import HTTPException

from app.models.character import Character
from app.routers.characters import convert_character_dossier, create_character_dossier, finalize_character_dossier
from app.schemas.character import DossierCommit
from tests.test_dossier_gm_fields import ADMIN, _database

# The minimum a finished sheet carries; other chargen tests reuse it.
STARTING_CONTACTS = [
    {"name": "Fixer Joe", "profession": "Fixer", "contact_type": "Contact"},
    {"name": "Doc Wagon", "profession": "Street Doc", "contact_type": "Contact"},
]
BUDDY = {**STARTING_CONTACTS[1], "contact_type": "Buddy", "loyalty": 3}
FOLLOWERS = [{"name": f"Follower {a}", "profession": a, "contact_type": "Follower", "loyalty": 6}
             for a in ("Bodyguard", "Mercenary", "Street Mage", "Street Decker", "Medic", "Fence")]

BAD = {
    "none": [],
    "only one": STARTING_CONTACTS[:1],
    "no archetype": [STARTING_CONTACTS[0], {"name": "Somebody", "contact_type": "Contact"}],
    "two Buddies": [{**c, "contact_type": "Buddy"} for c in STARTING_CONTACTS],
    "a gang isn't one of the two": [STARTING_CONTACTS[0], {"name": "Ancients", "contact_type": "Gang"}],
    "a follower isn't one of the two": [STARTING_CONTACTS[0], FOLLOWERS[0]],
    "six Followers": STARTING_CONTACTS + FOLLOWERS,
    "Followers sharing an archetype": STARTING_CONTACTS + [FOLLOWERS[0], {**FOLLOWERS[0], "name": "Twin"}],
    "Follower without an archetype": STARTING_CONTACTS + [{**FOLLOWERS[0], "profession": None}],
}


def _create(tmp_path, contacts, **extra):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            async with sessions() as db:
                return await create_character_dossier(
                    body=DossierCommit(name="Chancer", contacts=contacts, **extra), db=db, ctx=ADMIN)
    return asyncio.run(scenario())


@pytest.mark.parametrize("contacts", [STARTING_CONTACTS, [STARTING_CONTACTS[0], BUDDY]], ids=["two Contacts", "one upgraded"])
def test_two_contacts_commit_with_or_without_a_buddy(tmp_path, contacts):
    assert _create(tmp_path, contacts)["is_draft"] is False


def test_extras_on_top(tmp_path):
    more = [{"name": "Wanda", "profession": "Bartender", "contact_type": "Contact"},
            {"name": "Ancients", "contact_type": "Gang"}, {"name": "Sinsearach", "contact_type": "Tribe"}]
    assert _create(tmp_path, [STARTING_CONTACTS[0], BUDDY] + more + FOLLOWERS[:5])["is_draft"] is False


@pytest.mark.parametrize("case", list(BAD))
def test_missing_contacts_are_rejected(tmp_path, case):
    with pytest.raises(HTTPException) as exc:
        _create(tmp_path, BAD[case])
    assert exc.value.status_code == 422


def test_draft_is_not_checked(tmp_path):
    assert _create(tmp_path, [], is_draft=True)["is_draft"] is True


@pytest.mark.parametrize("route", ["finalize", "convert"])
def test_finalize_and_convert_are_checked(tmp_path, route):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            async with sessions() as db:
                db.add(Character(id=5, name="Runner", is_pc=True, is_draft=route == "finalize"))
                await db.commit()
            endpoint = finalize_character_dossier if route == "finalize" else convert_character_dossier
            async with sessions() as db:
                await endpoint(character_id=5, body=DossierCommit(name="Runner"), db=db, ctx=ADMIN)
    with pytest.raises(HTTPException) as exc:
        asyncio.run(scenario())
    assert exc.value.status_code == 422
