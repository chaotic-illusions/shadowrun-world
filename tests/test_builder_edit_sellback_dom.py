"""Headless-browser test of selling starting gear back in the builder's re-edit (?edit=<id>).

The Oversight case: a runner with Priority A Resources mostly spent on a car adds a 200,000 nuyen
Follower in a re-edit, which puts Resources over budget. Selling the car back (still on the sheet)
fixes it and the save goes through. Starting gear that's no longer on the sheet (one of two
ammo boxes used up) is hidden, and cyberware stays locked. API stubbed; same Playwright setup as
tests/test_character_builder_dom.py.
"""
from __future__ import annotations

import pytest

from tests.test_character_builder_dom import _browser, _frontend_port, _route, sync_playwright  # noqa: F401 -- fixtures

pytestmark = pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")

_CYBER = {"n": "Datajack", "sub": "headware", "grade": "Standard", "baseEss": 0.2, "baseCost": 1000}
_BUILD = {
    "prio": {"race": "D", "magic": "E", "attributes": "B", "skills": "C", "resources": "A"},
    "metatype": "Human", "magicType": "Mundane",
    "base": {"body": 4, "quickness": 4, "strength": 4, "charisma": 4, "intelligence": 4, "willpower": 4},
    "skills": [],
    "gear": {"weapons": [{"n": "Regular Ammo", "cost": 20}, {"n": "Regular Ammo", "cost": 20}],
             "armor": [], "cyber": [_CYBER], "bio": [], "gear": [], "matrix": [],
             "vehicles": [{"n": "Car X", "sub": "Car", "cost": 899000, "body": 2}]},
    "contacts": [],
    "identity": {"handle": "Oversight", "lifestyle": "Low", "lifestylePermanent": False},
    "advancement": {"karma": {}, "attrs": {}},
}
_CHAR = {
    "id": 7, "name": "Oversight", "is_pc": True, "is_draft": False, "is_claimed": True, "version": 4,
    "race": "Human", "body": 4, "quickness": 4, "strength": 4, "charisma": 4, "intelligence": 4,
    "willpower": 4, "essence": 5.8, "good_karma": 0, "nuyen": 9996, "skills": [], "spells": [],
    "adept_powers": [],
    # One ammo box used up on the Dossier, which also added its own fields to the lines.
    "gear": {"weapons": [{"n": "Regular Ammo", "cost": 20, "rounds": 4}],
             "cyber": [_CYBER], "vehicles": [{"n": "Car X", "sub": "Car", "cost": 899000, "body": 2, "primary": True}]},
    "created_at": "2026-01-01T00:00:00Z", "updated_at": "2026-01-01T00:00:00Z",
}
_CONTACTS = [{"id": 1, "name": "Fixer Joe", "profession": "Fixer", "contact_type": "Contact", "loyalty": 1},
             {"id": 2, "name": "Doc", "profession": "Street Doc", "contact_type": "Contact", "loyalty": 1}]


def _edit_route(posts):
    def route(r):
        req, path = r.request, r.request.url.split("?")[0]
        if path.endswith((".js", ".css", ".html")) or "/fonts/" in path:
            r.continue_()
        elif path.endswith("/characters/7/rebuild-dossier"):
            posts.append(req.post_data_json)
            r.fulfill(json={"id": 7, "name": "Oversight", "karma_refunded": 0, "good_karma": 0, "nuyen": 79996})
        elif path.endswith("/characters/7/chargen-state"):
            r.fulfill(json={"state": _BUILD})
        elif path.endswith("/characters/7/contacts"):
            r.fulfill(json=_CONTACTS)
        elif path.endswith("/characters/7"):
            r.fulfill(json=_CHAR)
        else:
            _route(r)
    return route


def _step(pg, n):
    pg.locator(f'.wstep-dot[data-step="{n}"]').click()
    pg.wait_for_timeout(120)


def test_reedit_sells_starting_gear_back_to_fund_a_follower(_browser, _frontend_port):
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    posts: list[dict] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _edit_route(posts))
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html?edit=7")
    pg.wait_for_selector("#cbxModeBanner:has-text('Editing')", timeout=15000)

    # Loadout: the car and ONE ammo box (the other was used up) are listed; the car can be sold,
    # the Datajack can't.
    _step(pg, 5)
    loadout = pg.inner_text(".cbx-owned-wrap")
    assert "Car X" in loadout and loadout.count("Regular Ammo") == 1
    assert "1 starting item isn't on the sheet any more" in loadout
    assert pg.locator('[data-delgear="vehicles:0"]').is_enabled()
    assert pg.locator('[data-delgear="cyber:0"]').is_disabled()

    # A 200,000 Follower puts Resources over budget: the save is blocked.
    _step(pg, 6)
    pg.locator("#cbxAddContact").click()
    pg.wait_for_timeout(50)
    pg.select_option('[data-ctype="2"]', "Follower")
    pg.wait_for_timeout(50)
    pg.select_option('[data-carch="2"]', "Bodyguard")
    pg.fill('[data-cname="2"]', "Big Mike")
    _step(pg, 7)
    pg.locator("#cbxSubmit").click()
    pg.wait_for_timeout(300)
    assert "Resources" in pg.inner_text("#cbxSubmitStatus")

    # Sell the car back; now it saves, naming the sold line and the cash its Resources free up.
    _step(pg, 5)
    pg.locator('[data-delgear="vehicles:0"]').click()
    pg.wait_for_timeout(100)
    assert "Car X" not in pg.inner_text(".cbx-owned-wrap")
    _step(pg, 7)
    pg.locator("#cbxSubmit").click()
    pg.wait_for_selector("#cbxEditConfirm", timeout=5000)
    review = pg.inner_text("#cbxEditReview")
    assert "Sold back" in review and "Car X" in review and "899,000" in review
    pg.locator("#cbxEditConfirm").click()
    pg.wait_for_timeout(400)

    assert len(posts) == 1, pg.inner_text("#cbxSubmitStatus")
    sent = posts[0]
    assert sent["gear_sold"] == [{"bucket": "vehicles", "index": 0}]
    assert sent["expected_version"] == 4
    assert [c["name"] for c in sent["contacts"]] == ["Big Mike"]
    # Spent 900,040 of 1,000,000 before (car + ammo + the 1,000 Datajack: cash 9,996); 201,040
    # after (ammo + Datajack + Follower: cash 79,896).
    assert sent["nuyen_delta"] == 79896 - 9996
    assert "Saved" in pg.inner_text("#cbxSubmitStatus")
    assert errors == [], f"JS errors during the re-edit: {errors}"
    ctx.close()
