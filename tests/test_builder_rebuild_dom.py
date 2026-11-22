"""Headless-browser test of rebuilding a finished runner in the builder (?edit=<id>).

The runner loads as it is now: attributes and skills at their creation values (the Karma spent
raising them is refunded), the sheet's inventory -- including a second car and a Delta Datajack
bought in play -- counted as creation picks, and its real contacts. It loads over its Resources
budget; that overrun is the baseline, so saving is allowed until an edit makes it worse. API
stubbed; same Playwright setup as tests/test_character_builder_dom.py.
"""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from app.schemas.character import DossierRebuild
from tests.test_character_builder_dom import _browser, _frontend_port, _route, sync_playwright  # noqa: F401 -- fixtures

_FRONTEND = Path(__file__).resolve().parents[1] / "frontend"

_DATAJACK = {"n": "Datajack", "sub": "headware", "grade": "Delta", "baseEss": 0.2, "baseCost": 1000}
_CAR_X = {"n": "Car X", "sub": "Car", "cost": 899000, "body": 2}
_BUILD = {
    "prio": {"race": "D", "magic": "E", "attributes": "B", "skills": "C", "resources": "A"},
    "metatype": "Human", "magicType": "Mundane",
    "base": {"body": 4, "quickness": 4, "strength": 4, "charisma": 4, "intelligence": 4, "willpower": 4},
    "skills": [{"name": "Firearms", "attr": "quickness", "group": "combat", "rating": 3, "conc": "", "spec": ""}],
    "gear": {"weapons": [], "armor": [], "cyber": [], "bio": [], "gear": [], "matrix": [], "vehicles": [_CAR_X]},
    "contacts": [],
    "identity": {"handle": "Oversight", "lifestyle": "Low", "lifestylePermanent": False},
    # Body 4 -> 5 bought on the Dossier and recorded (at the old placeholder price, 10).
    "advancement": {"karma": {"attr:body": 10}, "attrs": {"body": 1}},
}
_CHAR = {
    "id": 7, "name": "Oversight", "is_pc": True, "is_draft": False, "is_claimed": True, "version": 4,
    "race": "Human", "body": 5, "quickness": 4, "strength": 4, "charisma": 4, "intelligence": 4,
    "willpower": 4, "essence": 5.9, "good_karma": 2, "nuyen": 500, "karma_pool": 3, "lifestyle_level": 2,
    "archetype": "Bounty Hunter",   # typed on the Dossier after creation (free text)
    # Firearms 3 -> 5 raised in play before Karma was recorded: 2x4 + 2x5 = 18 to refund.
    "skills": [{"name": "Firearms", "attr": "quickness", "group": "combat", "rating": 5, "concs": [], "specs": []}],
    "spells": [], "adept_powers": [],
    "gear": {"vehicles": [{**_CAR_X, "primary": True}, {"n": "Car Y", "sub": "Car", "cost": 200000, "body": 2}],
             "cyber": [_DATAJACK]},
    "created_at": "2026-01-01T00:00:00Z", "updated_at": "2026-01-01T00:00:00Z",
}
_CONTACTS = [{"id": 1, "name": "Fixer Joe", "profession": "Fixer", "contact_type": "Contact", "loyalty": 1},
             {"id": 2, "name": "Doc", "profession": "Street Doc", "contact_type": "Contact", "loyalty": 1}]


def _rebuild_route(posts, contacts=_CONTACTS):
    def route(r):
        req, path = r.request, r.request.url.split("?")[0]
        if path.endswith((".js", ".css", ".html")) or "/fonts/" in path:
            r.continue_()
        elif path.endswith("/characters/7/rebuild-dossier"):
            posts.append(req.post_data_json)
            r.fulfill(json={"id": 7, "name": "Oversight", "karma_refunded": 28, "good_karma": 30, "nuyen": 500})
        elif path.endswith("/characters/7/chargen-state"):
            r.fulfill(json={"state": _BUILD})
        elif path.endswith("/characters/7/contacts"):
            r.fulfill(json=contacts)
        elif path.endswith("/characters/7"):
            r.fulfill(json=_CHAR)
        else:
            _route(r)
    return route


def _step(pg, n):
    pg.locator(f'.wstep-dot[data-step="{n}"]').click()
    pg.wait_for_timeout(120)


def _submit(pg):
    _step(pg, 7)
    pg.locator("#cbxSubmit").click()
    pg.wait_for_timeout(400)


@pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")
def test_rebuild_loads_current_runner_refunds_raises_and_keeps_the_baseline(_browser, _frontend_port):
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    posts: list[dict] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _rebuild_route(posts))
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html?edit=7")
    pg.wait_for_selector("#cbxModeBanner:has-text('Rebuilding')", timeout=15000)

    # Inventory is the sheet's, play purchases included; nothing is locked; the Delta implant stays.
    _step(pg, 5)
    loadout = pg.inner_text(".cbx-owned-wrap")
    assert "Car X" in loadout and "Car Y" in loadout and "Datajack" in loadout
    assert pg.locator('[data-delgear="vehicles:1"]').is_enabled()
    assert pg.locator('[data-delgear="cyber:0"]').is_enabled()
    assert pg.eval_on_selector('[data-cybergrade="0"]', "el => el.value") == "Delta"

    # Loaded 109,000 over Resources (both cars + the Delta Datajack): that baseline doesn't block.
    _submit(pg)
    assert pg.locator("#cbxEditConfirm").count() == 1, pg.inner_text("#cbxSubmitStatus")

    # A 200,000 Follower makes the overrun worse: blocked.
    _step(pg, 6)
    pg.locator("#cbxAddContact").click()
    pg.wait_for_timeout(50)
    pg.select_option('[data-ctype="2"]', "Follower")
    pg.wait_for_timeout(50)
    pg.select_option('[data-carch="2"]', "Bodyguard")
    pg.fill('[data-cname="2"]', "Big Mike")
    pg.fill('[data-cname="1"]', "Doc Holliday")            # an existing contact, renamed in place
    _submit(pg)
    assert "Resources" in pg.inner_text("#cbxSubmitStatus") and pg.locator("#cbxEditConfirm").count() == 0

    # Removing the car bought in play pays for the Follower: back to the baseline, so it saves.
    _step(pg, 5)
    pg.locator('[data-delgear="vehicles:1"]').click()
    pg.wait_for_timeout(100)
    _submit(pg)
    review = pg.inner_text("#cbxEditReview")
    assert "+10" in review and "+18" in review                # Body (recorded), Firearms (priced)
    assert "Car Y" in review and "Doc Holliday" in review and "Big Mike" in review
    assert "30" in review                                     # Good Karma 2 -> 30
    pg.locator("#cbxEditConfirm").click()
    pg.wait_for_timeout(500)

    assert len(posts) == 1, pg.inner_text("#cbxSubmitStatus")
    sent = posts[0]
    DossierRebuild(**sent)                                    # what the builder sends, the server accepts
    assert sent["karma_refund"] == 28 and sent["expected_version"] == 4
    assert sent["body"] == 4                                  # creation value; the raise is refunded
    assert [s["rating"] for s in sent["skills"] if s["name"] == "Firearms"] == [3]
    assert [v["n"] for v in sent["gear"]["vehicles"]] == ["Car X"]
    assert sent["gear"]["vehicles"][0].get("primary") is True  # the sheet's own fields ride along
    assert sent["gear"]["cyber"][0]["grade"] == "Delta"
    assert [(c.get("id"), c["name"]) for c in sent["contacts"]] == [(1, "Fixer Joe"), (2, "Doc Holliday"), (None, "Big Mike")]
    for kept_server_side in ("good_karma", "nuyen", "karma_pool", "notes"):
        assert kept_server_side not in sent
    assert sent["archetype"] == "Bounty Hunter"               # the Dossier's edit isn't reverted
    assert sent["nuyen_delta"] == 0                           # over budget before and after: no starting cash either way
    assert "Saved" in pg.inner_text("#cbxSubmitStatus")

    assert errors == [], f"JS errors during the rebuild: {errors}"
    ctx.close()


@pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")
def test_rebuild_allows_the_buddies_the_runner_already_had(_browser, _frontend_port):
    """Two Buddies at load (a stored one, and one whose loyalty was raised to 4 in play): the rebuild
    can be saved as is, but a third can't be added."""
    contacts = [{"id": 1, "name": "Fixer Joe", "profession": "Fixer", "contact_type": "Contact", "loyalty": 1},
                {"id": 2, "name": "Doc", "profession": "Street Doc", "contact_type": "Buddy", "loyalty": 3},
                {"id": 3, "name": "Rita", "profession": "Fence", "contact_type": None, "loyalty": 4}]
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    posts: list[dict] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _rebuild_route(posts, contacts))
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html?edit=7")
    pg.wait_for_selector("#cbxModeBanner:has-text('Rebuilding')", timeout=15000)

    _step(pg, 6)
    assert pg.eval_on_selector('[data-ctype="2"]', "el => el.value") == "Buddy"     # loyalty 4 -> shown as Buddy
    assert pg.locator('[data-ctype="0"] option[value="Buddy"]').is_disabled()      # no third Buddy
    _submit(pg)
    assert pg.locator("#cbxEditConfirm").count() == 1, pg.inner_text("#cbxSubmitStatus")
    pg.locator("#cbxEditConfirm").click()
    pg.wait_for_timeout(400)
    assert [c["contact_type"] for c in posts[0]["contacts"]] == ["Contact", "Buddy", "Buddy"]
    assert errors == [], f"JS errors during the rebuild: {errors}"
    ctx.close()


@pytest.mark.skipif(shutil.which("node") is None, reason="Node.js is required")
def test_refund_pricing_matches_the_advancement_rules():
    """General 2x, Concentration 1.5x rounded up, Specialization 1x, language 1x the new rating;
    attributes the new rating. A Concentration/Specialization bought in play is priced from what
    it builds on now. Runs the real functions (builder + shared.js) under Node."""
    shared = (_FRONTEND / "shared.js").read_text(encoding="utf-8")
    builder = (_FRONTEND / "character-builder.html").read_text(encoding="utf-8")
    costs = shared[shared.index("function attrKarmaCost("):shared.index("function newConcRating(")]
    pricing = builder[builder.index("function priceSteps("):builder.index("// [{key, label, karma}] for every attribute")]
    script = costs + pricing + """
console.log(JSON.stringify({
  concSpec: skillRaiseKarma({ rating: 3, concs: [], specs: [] },
    { group: 'combat', rating: 3, concs: [{ name: 'Pistols', rating: 5 }], specs: [{ name: 'Ares', rating: 6, conc: 'Pistols' }] }),
  raisedConc: skillRaiseKarma({ rating: 3, concs: [{ name: 'Pistols', rating: 4 }], specs: [] },
    { group: 'combat', rating: 3, concs: [{ name: 'Pistols', rating: 6 }], specs: [] }),
  language: skillRaiseKarma({ rating: 2 }, { group: 'language', rating: 4, concs: [], specs: [] }),
  newSkill: skillRaiseKarma(undefined, { group: 'combat', rating: 2, concs: [], specs: [] }),
  lowered: skillRaiseKarma({ rating: 4 }, { group: 'combat', rating: 3, concs: [], specs: [] }),
  attr: priceSteps(4, 6, attrKarmaCost),
}));
"""
    out = subprocess.run(["node", "-e", script], check=True, capture_output=True, text=True, timeout=30).stdout
    assert json.loads(out) == {"concSpec": 6 + 8 + 6, "raisedConc": 8 + 9, "language": 3 + 4,
                               "newSkill": 2 + 4, "lowered": 0, "attr": 5 + 6}
