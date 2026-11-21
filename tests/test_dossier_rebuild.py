"""Re-editing a finished runner in the character builder (POST /characters/{id}/rebuild-dossier).

The edit can't touch the locked parts of the build (priorities, metatype, magic choices, gear,
lifestyle, existing contacts), refunds exactly the Good Karma recorded against the items it
changed, and can only cost cash. Throwaway aiosqlite DB, router functions called directly (same
pattern as tests/test_dossier_gm_fields.py).
"""
import asyncio

import pytest
from fastapi import HTTPException
from sqlalchemy import select

from app.auth.core import hash_token
from app.models.character import Character
from app.models.contact import Contact
from app.routers.characters import rebuild_character_dossier
from app.schemas.character import DossierRebuild
from tests.test_dossier_gm_fields import ADMIN, OTHER, PLAYER, _database

BUILD = {
    "prio": {"race": "E", "magic": "E", "attributes": "B", "skills": "A", "resources": "C"},
    "metatype": "Human",
    "magicType": "Mundane",
    "base": {"body": 4, "quickness": 4, "strength": 3, "charisma": 3, "intelligence": 5, "willpower": 5},
    "skills": [{"name": "Etiquette", "attr": "Charisma", "group": "social", "rating": 1, "conc": "Street", "spec": ""}],
    "gear": {"weapons": [{"n": "Ares Predator"}]},
    "contacts": [{"name": "Fixer Joe", "archetype": "Fixer", "type": "Contact"},
                 {"name": "", "archetype": "", "type": "Contact"}],
    "identity": {"handle": "Wraith", "lifestyle": "Low", "lifestylePermanent": False},
    "magic_rating_base": 0,
    "advancement": {"karma": {"skill:Etiquette": 2, "attr:body": 10}, "attrs": {"body": 1}},
}


def _run(tmp_path, body, ctx=PLAYER, db_name="t.db", **char):
    async def scenario():
        async with _database(tmp_path / db_name) as sessions:
            async with sessions() as db:
                db.add(Character(id=10, name="Wraith", is_pc=True, owner_token=hash_token("runner"),
                                 good_karma=3, nuyen=1000, body=5, chargen_state=BUILD, **char))
                await db.commit()
            async with sessions() as db:
                out = await rebuild_character_dossier(10, DossierRebuild(**body), db=db, ctx=ctx)
            async with sessions() as db:
                row = await db.get(Character, 10)
                contacts = (await db.execute(select(Contact).where(Contact.owner_id == 10))).scalars().all()
                return out, row, contacts
    return asyncio.run(scenario())


def _edited(**changes):
    return {**BUILD, **changes}


def test_refunds_exactly_the_dropped_entries(tmp_path):
    adv = {"karma": {"attr:body": 10}, "attrs": {"body": 1}}   # Etiquette changed -> its 2 karma back
    skills = [{"name": "Etiquette", "rating": 2, "concs": [], "specs": []}]
    out, row, _ = _run(tmp_path, {"chargen_state": _edited(advancement=adv), "skills": skills})
    assert out["karma_refunded"] == 2
    assert row.good_karma == 5
    assert row.skills == skills
    assert row.chargen_state["advancement"] == adv


def test_unchanged_edit_refunds_nothing(tmp_path):
    out, row, _ = _run(tmp_path, {"chargen_state": BUILD})
    assert out["karma_refunded"] == 0 and row.good_karma == 3


@pytest.mark.parametrize("adv", [
    {"karma": {"skill:Etiquette": 1, "attr:body": 10}},              # altered amount
    {"karma": {"skill:Etiquette": 2, "attr:body": 10, "x": 5}},      # invented entry
    {"karma": {"skill:Etiquette": 2, "attr:body": 10}, "attrs": {"body": 2}},
], ids=["altered", "invented", "attr raise altered"])
def test_advancement_can_only_lose_entries(tmp_path, adv):
    with pytest.raises(HTTPException) as e:
        _run(tmp_path, {"chargen_state": _edited(advancement=adv)})
    assert e.value.status_code == 422


def test_locked_keys_restored(tmp_path):
    tampered = _edited(prio={**BUILD["prio"], "resources": "A"}, metatype="Troll", magicType="Full Mage",
                       gear={"weapons": []}, magic_rating_base=6,
                       identity={**BUILD["identity"], "handle": "Ghost", "lifestyle": "Luxury"})
    _, row, _ = _run(tmp_path, {"chargen_state": tampered})
    cs = row.chargen_state
    for key in ("prio", "metatype", "magicType", "gear", "magic_rating_base"):
        assert cs[key] == BUILD[key], key
    assert cs["identity"]["lifestyle"] == "Low"
    assert cs["identity"]["handle"] == "Ghost"   # identity text stays editable


def test_new_contacts_are_created_and_cost_cash(tmp_path):
    contacts = [BUILD["contacts"][0], {"name": "Doc Wagon", "archetype": "Street Doc", "type": "Contact"}]
    new = [{"name": "Doc Wagon", "profession": "Street Doc", "contact_type": "Contact"}]
    _, row, rows = _run(tmp_path, {"chargen_state": _edited(contacts=contacts), "contacts": new, "nuyen_delta": -500})
    assert [c.name for c in rows] == ["Doc Wagon"]
    assert row.nuyen == 500
    # The saved builder list mirrors the real Contact rows, not whatever the client sent.
    assert row.chargen_state["contacts"] == [{"name": "Doc Wagon", "archetype": "Street Doc", "type": "Contact"}]


def test_edit_never_adds_cash(tmp_path):
    _, row, _ = _run(tmp_path, {"chargen_state": BUILD, "nuyen_delta": 50000})
    assert row.nuyen == 1000


def test_owner_or_gm_only(tmp_path):
    with pytest.raises(HTTPException) as e:
        _run(tmp_path, {"chargen_state": BUILD}, ctx=OTHER)
    assert e.value.status_code == 404
    out, _, _ = _run(tmp_path, {"chargen_state": BUILD}, ctx=ADMIN, db_name="gm.db")
    assert out["id"] == 10


def test_pre_wizard_runner_must_convert(tmp_path):
    async def scenario():
        async with _database(tmp_path / "t.db") as sessions:
            async with sessions() as db:
                db.add(Character(id=10, name="Old", is_pc=True, owner_token=hash_token("runner"), chargen_state={}))
                await db.commit()
            async with sessions() as db:
                await rebuild_character_dossier(10, DossierRebuild(chargen_state={}), db=db, ctx=PLAYER)
    with pytest.raises(HTTPException) as e:
        asyncio.run(scenario())
    assert e.value.status_code == 400
