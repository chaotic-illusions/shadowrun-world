"""Rebuilding a finished runner from the character builder (POST /characters/{id}/rebuild-dossier).

The builder sends the whole new sheet. The server writes it, adds the builder's Karma refund to
Good Karma and its starting-cash change to nuyen, keeps the Karma Pool and notes, edits contacts
in place, lets an existing GM-approved Beta/Delta implant stay (but not a new one), and refuses a
stale save. Throwaway aiosqlite DB, router functions called directly (same pattern as
tests/test_dossier_gm_fields.py).
"""
import asyncio

import pytest
from fastapi import HTTPException
from sqlalchemy import select

from app.auth.core import hash_token
from app.models.character import Character
from app.models.contact import Contact
from app.routers.characters import rebuild_character_dossier
from app.schemas.character import CharacterRead, DossierRebuild
from tests.test_dossier_gm_fields import ADMIN, OTHER, PLAYER, _database

BUILD = {
    "prio": {"race": "E", "magic": "E", "attributes": "B", "skills": "A", "resources": "C"},
    "metatype": "Human", "magicType": "Mundane",
    "base": {"body": 4, "quickness": 4, "strength": 3, "charisma": 3, "intelligence": 5, "willpower": 5},
    "skills": [{"name": "Etiquette", "attr": "Charisma", "group": "social", "rating": 1, "conc": "Street", "spec": ""}],
    "gear": {"weapons": [{"n": "Ares Predator"}]},
    "identity": {"handle": "Wraith", "lifestyle": "Low", "lifestylePermanent": False},
    "magic_rating_base": 0,
    "advancement": {"karma": {"skill:Etiquette": 2}, "attrs": {"body": 1}},
}
SHEET_GEAR = {"weapons": [{"n": "Ares Predator", "id": "w1", "equipped": True}],
              "cyber": [{"n": "Wired Reflexes", "grade": "Delta", "baseEss": 2, "baseCost": 55000}],
              "foci": [], "programs": [], "odd_bucket": [{"n": "Kept as-is"}]}


def _body(**over):
    """A rebuild payload: the new sheet as the builder's commitPayload() sends it."""
    b = {"name": "Wraith", "is_pc": True, "body": 5, "quickness": 4, "strength": 3, "charisma": 3,
         "intelligence": 5, "willpower": 5, "essence": 6.0, "magic_rating": 0,
         "skills": [{"name": "Etiquette", "rating": 1, "concs": [], "specs": []}],
         "spells": [], "gear": {"weapons": [{"n": "Ares Predator", "id": "w1", "equipped": True}],
                                "cyber": [{"n": "Wired Reflexes", "grade": "Delta", "baseEss": 2, "baseCost": 55000}],
                                "foci": [], "programs": []},
         # Never taken from the payload: these are adjusted / kept server-side.
         "good_karma": 0, "nuyen": 5, "karma_pool": 1, "notes": "builder notes",
         "chargen_state": {**BUILD, "advancement": {"karma": {}, "attrs": {}}},
         "contacts": []}
    b.update(over)
    return b


def _setup(db):
    db.add(Character(id=10, name="Wraith", is_pc=True, owner_token=hash_token("runner"), good_karma=3,
                     nuyen=1000, karma_pool=4, notes="table notes", body=5, magic_rating=0,
                     chargen_state=BUILD, gear=SHEET_GEAR))
    db.add(Character(id=20, name="Fixer Joe", is_pc=False, archetype="Fixer", origin_pc_id=10))
    db.add(Character(id=21, name="Mr. Q (real name)", is_pc=False, archetype="Doc", origin_pc_id=10))
    db.add(Contact(id=1, owner_id=10, npc_id=20, name="Fixer Joe", profession="Fixer", contact_type="Contact", loyalty=2))
    db.add(Contact(id=2, owner_id=10, npc_id=21, name="Doc", profession="Street Doc", contact_type="Buddy", loyalty=3))
    db.add(Contact(id=3, owner_id=10, name="Red Hot Nukes", contact_type="Gang", loyalty=1))
    db.add(Contact(id=4, owner_id=10, name="GM secret", profession="Mole", contact_type="Contact",
                   loyalty=1, is_active=False))


def _run(tmp_path, body, ctx=PLAYER, db_name="t.db", setup=_setup):
    async def scenario():
        async with _database(tmp_path / db_name) as sessions:
            async with sessions() as db:
                setup(db)
                await db.commit()
            async with sessions() as db:
                out = await rebuild_character_dossier(10, DossierRebuild(**body), db=db, ctx=ctx)
            async with sessions() as db:
                row = await db.get(Character, 10)
                contacts = {c.id: c for c in (await db.execute(select(Contact).where(Contact.owner_id == 10))).scalars()}
                npcs = {c.id: c for c in (await db.execute(select(Character).where(Character.is_pc == False))).scalars()}  # noqa: E712
                return out, row, contacts, npcs
    return asyncio.run(scenario())


_SAME_CONTACTS = [{"id": 1, "name": "Fixer Joe", "profession": "Fixer", "contact_type": "Contact"},
                  {"id": 2, "name": "Doc", "profession": "Street Doc", "contact_type": "Buddy"},
                  {"id": 3, "name": "Red Hot Nukes", "contact_type": "Gang"}]


def test_rebuild_writes_the_sheet_and_adjusts_karma_and_nuyen(tmp_path):
    body = _body(skills=[{"name": "Etiquette", "rating": 3, "concs": [], "specs": []}],
                 karma_refund=12, nuyen_delta=-300, contacts=_SAME_CONTACTS)
    out, row, _, _ = _run(tmp_path, body)
    assert out["karma_refunded"] == 12
    assert row.skills[0]["rating"] == 3
    assert row.good_karma == 3 + 12                     # current + refund, not the payload's 0
    assert row.nuyen == 1000 - 300                      # current + delta, not the payload's 5
    assert row.karma_pool == 4 and row.notes == "table notes"
    assert row.gear["odd_bucket"] == [{"n": "Kept as-is"}]   # a bucket the builder doesn't carry
    assert row.gear["weapons"] == [{"n": "Ares Predator", "id": "w1", "equipped": True}]
    # The new build is the baseline: nothing left to refund, magic ceiling restarts.
    assert row.chargen_state["advancement"] == {} and row.chargen_state["magic_rating_base"] == 0
    assert row.chargen_state["editId"] is None


def test_respent_resources_must_be_covered_by_cash_on_hand(tmp_path):
    # The runner has 1,000 cash. Re-spending 50,000 of leftover starting Resources takes back the
    # 5,000 cash it became, which isn't there: refused, nothing written.
    with pytest.raises(HTTPException) as e:
        _run(tmp_path, _body(nuyen_delta=-5000, contacts=_SAME_CONTACTS))
    assert e.value.status_code == 422 and "Not enough cash" in e.value.detail
    # Exactly what's on hand is fine (down to 0), and freeing Resources adds cash.
    _, row, _, _ = _run(tmp_path, _body(nuyen_delta=-1000, contacts=_SAME_CONTACTS), db_name="all.db")
    assert row.nuyen == 0
    _, row, _, _ = _run(tmp_path, _body(nuyen_delta=2500, contacts=_SAME_CONTACTS), db_name="up.db")
    assert row.nuyen == 3500


def test_contacts_are_edited_in_place(tmp_path):
    contacts = [
        {"id": 1, "name": "Fixer Joey", "profession": "Fence", "contact_type": "Buddy"},   # rename + Contact->Buddy
        {"id": 2, "name": "Doc", "profession": "Street Doc", "contact_type": "Gang"},     # person -> Gang
        {"id": 3, "name": "Red Hot Nukes", "profession": "Talismonger", "contact_type": "Contact"},  # Gang -> person
        {"name": "Big Mike", "profession": "Bodyguard", "contact_type": "Follower", "loyalty": 6},  # new
    ]
    _, _, rows, npcs = _run(tmp_path, _body(contacts=contacts))
    joe = rows[1]
    assert (joe.name, joe.profession, joe.contact_type) == ("Fixer Joey", "Fence", "Buddy")
    assert joe.loyalty == 3 + 1                         # Buddy's 3, plus the 1 point raised in play
    assert (npcs[20].name, npcs[20].archetype) == ("Fixer Joey", "Fence")   # NPC followed the rename
    assert rows[2].npc_id is None and 21 in npcs        # unlinked, but the NPC stays a Person of Interest
    assert rows[3].npc_id is not None and npcs[rows[3].npc_id].name == "Red Hot Nukes"
    assert any(c.name == "Big Mike" and c.npc_id for c in rows.values())
    assert 4 in rows                                    # the GM-hidden contact is never touched


def test_npc_the_gm_renamed_keeps_its_name(tmp_path):
    contacts = [{"id": 1, "name": "Fixer Joe", "profession": "Fixer", "contact_type": "Contact"},
                {"id": 2, "name": "Doc Holliday", "profession": "Street Doc", "contact_type": "Buddy"},
                {"id": 3, "name": "Red Hot Nukes", "contact_type": "Gang"}]
    _, _, rows, npcs = _run(tmp_path, _body(contacts=contacts))
    assert rows[2].name == "Doc Holliday"
    assert npcs[21].name == "Mr. Q (real name)"         # the GM's name for the NPC wins
    assert rows[2].loyalty == 3                          # same type: loyalty unchanged


def test_contact_left_out_is_deleted_and_its_npc_kept(tmp_path):
    _, _, rows, npcs = _run(tmp_path, _body(contacts=_SAME_CONTACTS[1:]))
    assert 1 not in rows and 20 in npcs
    assert 4 in rows                                    # hidden from the player, so not "left out"


@pytest.mark.parametrize("contacts", [
    [{"id": 99, "name": "Stranger", "contact_type": "Contact"}],                    # not this runner's
    [{"id": 4, "name": "GM secret", "contact_type": "Contact"}],                    # hidden from the player
    [{"id": 1, "name": "A", "contact_type": "Contact"}, {"id": 1, "name": "B", "contact_type": "Contact"}],
])
def test_bad_contact_ids_are_refused(tmp_path, contacts):
    with pytest.raises(HTTPException) as e:
        _run(tmp_path, _body(contacts=contacts))
    assert e.value.status_code == 422


def test_existing_delta_implant_may_stay_but_a_new_one_is_refused(tmp_path):
    _run(tmp_path, _body(contacts=_SAME_CONTACTS))                 # the sheet's Delta Wired Reflexes: fine
    gear = {"cyber": [{"n": "Wired Reflexes", "grade": "Delta", "baseEss": 2, "baseCost": 55000},
                      {"n": "Datajack", "grade": "Delta", "baseEss": 0.2, "baseCost": 1000}]}
    with pytest.raises(HTTPException) as e:
        _run(tmp_path, _body(gear=gear, contacts=_SAME_CONTACTS), db_name="new.db")
    assert e.value.status_code == 400 and "Delta" in e.value.detail
    _run(tmp_path, _body(gear=gear, contacts=_SAME_CONTACTS), ctx=ADMIN, db_name="gm.db")   # a GM may


def test_owner_or_gm_only(tmp_path):
    with pytest.raises(HTTPException) as e:
        _run(tmp_path, _body(), ctx=OTHER)
    assert e.value.status_code == 404
    out, _, _, _ = _run(tmp_path, _body(contacts=_SAME_CONTACTS), ctx=ADMIN, db_name="gm.db")
    assert out["id"] == 10


def test_pre_wizard_runner_must_convert(tmp_path):
    def setup(db):
        db.add(Character(id=10, name="Old", is_pc=True, owner_token=hash_token("runner"), chargen_state={}))
    with pytest.raises(HTTPException) as e:
        _run(tmp_path, _body(), setup=setup)
    assert e.value.status_code == 400


def test_stale_save_is_refused_and_a_current_one_goes_through(tmp_path):
    async def scenario(pick, name):
        async with _database(tmp_path / name) as sessions:
            async with sessions() as db:
                _setup(db)
                await db.commit()
            async with sessions() as db:          # e.g. Karma spent on the Dossier in another tab
                row = await db.get(Character, 10)
                row.nuyen = 900
                await db.commit()
                now = row.version
            async with sessions() as db:
                body = _body(contacts=_SAME_CONTACTS, karma_refund=2, expected_version=pick(now))
                await rebuild_character_dossier(10, DossierRebuild(**body), db=db, ctx=PLAYER)
            async with sessions() as db:
                return await db.get(Character, 10)
    with pytest.raises(HTTPException) as e:
        asyncio.run(scenario(lambda now: now - 1, "stale.db"))
    assert e.value.status_code == 409
    row = asyncio.run(scenario(lambda now: now, "current.db"))
    assert row.good_karma == 5


def test_character_read_exposes_version_for_the_review():
    assert "version" in CharacterRead.model_fields


def _setup_untyped(db):
    """A runner whose contacts' types were never stored: loyalty raised in play makes one look
    like a Buddy (4) and one like a Follower (6). The GM's notes etc. sit on the records."""
    db.add(Character(id=10, name="Wraith", is_pc=True, owner_token=hash_token("runner"), good_karma=3,
                     nuyen=1000, chargen_state=BUILD, gear=SHEET_GEAR))
    db.add(Contact(id=1, owner_id=10, name="Joe", profession="Fence", contact_type=None, loyalty=4,
                   connection=3, notes="GM: owes the runner", description="Pawn shop on 5th"))
    db.add(Contact(id=2, owner_id=10, name="Rook", profession="Bodyguard", contact_type=None, loyalty=6))
    db.add(Contact(id=3, owner_id=10, name="Doc", profession="Street Doc", contact_type="Buddy", loyalty=3))


@pytest.mark.parametrize("contact_id,new_type,loyalty", [
    (1, "Contact", 4),    # untyped loyalty 4 (shown as Buddy): all 3 points above 1 were raised in play
    (1, "Follower", 6),   # 6 + 3 raised, capped at 6
    (2, "Buddy", 6),      # untyped loyalty 6 (shown as Follower) -> Buddy: 3 + 5 raised, capped
    (3, "Contact", 1),    # a stored Buddy at its creation loyalty becomes a plain Contact
])
def test_type_change_keeps_loyalty_raised_in_play(tmp_path, contact_id, new_type, loyalty):
    contacts = [{"id": 1, "name": "Joe", "profession": "Fence", "contact_type": "Buddy"},
                {"id": 2, "name": "Rook", "profession": "Bodyguard", "contact_type": "Follower"},
                {"id": 3, "name": "Doc", "profession": "Street Doc", "contact_type": "Buddy"}]
    for c in contacts:
        if c["id"] == contact_id:
            c["contact_type"] = new_type
    _, _, rows, _ = _run(tmp_path, _body(contacts=contacts), setup=_setup_untyped)
    assert rows[contact_id].loyalty == loyalty and rows[contact_id].contact_type == new_type


def test_unchanged_untyped_contacts_keep_their_loyalty(tmp_path):
    contacts = [{"id": 1, "name": "Joe", "profession": "Fence", "contact_type": "Buddy"},
                {"id": 2, "name": "Rook", "profession": "Bodyguard", "contact_type": "Follower"},
                {"id": 3, "name": "Doc", "profession": "Street Doc", "contact_type": "Buddy"}]
    _, _, rows, _ = _run(tmp_path, _body(contacts=contacts), setup=_setup_untyped)
    assert (rows[1].loyalty, rows[2].loyalty, rows[3].loyalty) == (4, 6, 3)


def test_editing_a_contact_keeps_everything_else_on_the_record(tmp_path):
    # A Fence renamed and turned into a Data Broker: same record, same relationship.
    contacts = [{"id": 1, "name": "Joey Two-Times", "profession": "Data Broker", "contact_type": "Buddy"},
                {"id": 2, "name": "Rook", "profession": "Bodyguard", "contact_type": "Follower"},
                {"id": 3, "name": "Doc", "profession": "Street Doc", "contact_type": "Buddy"}]
    _, _, rows, _ = _run(tmp_path, _body(contacts=contacts), setup=_setup_untyped)
    joe = rows[1]
    assert (joe.name, joe.profession) == ("Joey Two-Times", "Data Broker")
    assert (joe.loyalty, joe.connection) == (4, 3)
    assert joe.notes == "GM: owes the runner" and joe.description == "Pawn shop on 5th"
