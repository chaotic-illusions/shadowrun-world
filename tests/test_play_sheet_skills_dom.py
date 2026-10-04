"""Headless-browser test of the play sheet's Manage Skills (SR2 p.190 karma improvement).

Loads frontend/play-sheet.html with the API stubbed, buys a second Concentration and a
Specialization, raises the general skill and a language, commits, and checks what was PATCHed:
new parts start one above what they build on, the general skill is never lowered, and the karma
spent matches the book. Same Playwright setup as tests/test_character_builder_dom.py.
"""
from __future__ import annotations

import json

import pytest

from app.data import catalog as cat
from tests.test_character_builder_dom import _browser, _frontend_port, sync_playwright  # noqa: F401 -- fixtures

pytestmark = pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")

_CHAR = {
    "id": 7, "name": "Night Shift", "is_pc": True, "is_claimed": True, "race": "Human",
    "body": 3, "quickness": 4, "strength": 3, "charisma": 4, "intelligence": 5, "willpower": 5,
    "reaction": 4, "essence": 6.0, "magic_rating": 0, "good_karma": 30, "karma_pool": 1, "nuyen": 100,
    "skills": [
        {"name": "Firearms", "attr": "quickness", "group": "combat", "rating": 2,
         "concs": [{"name": "Pistols", "rating": 4}], "specs": []},
        {"name": "Spanish", "attr": "intelligence", "group": "language", "rating": 2, "concs": [], "specs": []},
    ],
    "gear": {"weapons": [{"n": "Ares Predator"}, {"n": "Defiance T-250"}]},
    "spells": [], "adept_powers": [], "priorities": {},
    "created_at": "2026-01-01T00:00:00Z", "updated_at": "2026-01-01T00:00:00Z",
}


def _route_for(patches):
    def _route(route):
        req, url = route.request, route.request.url
        path = url.split("?")[0]
        if path.endswith((".js", ".css", ".html")) or "/fonts/" in path:
            route.continue_()
        elif "/auth/verify" in url:
            route.fulfill(json={"is_admin": True, "is_user": False, "is_default_password": False})
        elif "/catalog/skill-specs" in url:
            skills = [{"n": s.get("n"), "attr": s.get("attr"), "group": s.get("group"), "conc": s.get("conc", [])}
                      for s in cat.get_rules().get("skills", [])]
            route.fulfill(json={"skills": skills, "specs": cat.get_skill_specs()})
        elif "/catalog/vehicle-classes" in url:
            route.fulfill(json={"classes": cat.get_vehicle_classes()})
        elif "/catalog/rules" in url:
            route.fulfill(json=cat.get_rules())
        elif "/catalog/books" in url:
            route.fulfill(json={"enabled": [], "core": {"code": "SR2", "name": "SR2"}, "official": []})
        elif "/catalog/" in url:
            name = path.split("/catalog/")[1].strip("/")
            items = cat.get_catalog(name) if name in cat.ITEM_CATALOGS else []
            route.fulfill(json={"catalog": name, "count": len(items), "items": items})
        elif path.endswith("/characters/mine"):
            route.fulfill(json={"ids": [7]})
        elif path.endswith("/characters/7") and req.method == "PATCH":
            patches.append(req.post_data_json)
            route.fulfill(json={**_CHAR, **req.post_data_json})
        elif path.endswith("/characters/7"):
            route.fulfill(json=_CHAR)
        elif "chargen-state" in url or "deck-builder-state" in url:
            route.fulfill(json={"state": {}})
        elif any(m in url for m in ("/characters", "/contacts", "/runs", "/organizations", "/locations")):
            route.fulfill(json=[])
        else:
            route.continue_()
    return _route


def test_manage_skills_buys_concentrations_and_specializations_with_karma(_browser, _frontend_port):
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    patches: list[dict] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _route_for(patches))
    pg.goto(f"http://127.0.0.1:{_frontend_port}/play-sheet.html?id=7")
    pg.wait_for_selector("#skillList .sk-row", timeout=15000)
    pg.locator("#manageSkillsBtn").click()
    pg.wait_for_selector('[data-addconc="0"]', timeout=5000)

    # Concentrations offered: the web's, less Pistols; priced at general+1 = 3 for ceil(4.5) = 5.
    conc_opts = pg.eval_on_selector('[data-addconc="0"]', "el => Array.from(el.options).map(o => o.value)")
    assert "Pistols" not in conc_opts and "Shotguns" in conc_opts
    assert "New Concentration at 3" in pg.inner_text("#modalBody") and "5 karma" in pg.inner_text("#modalBody")
    pg.select_option('[data-addconc="0"]', "Shotguns")

    # Specializations: only the character's own weapons, each under its own Concentration. The
    # Ares Predator builds on Pistols 4 -> 5 for 5 karma.
    groups = pg.eval_on_selector('[data-addspec="0"]', """el => Object.fromEntries(Array.from(el.querySelectorAll('optgroup'))
        .map(g => [g.label, Array.from(g.querySelectorAll('option')).map(o => o.textContent)]))""")
    assert groups["Pistols"] == ["Ares Predator at 5 — 5 karma"]
    assert groups["Shotguns"] == ["Defiance T-250 at 4 — 4 karma"]   # Shotguns 3 (just bought) + 1
    assert "Rifles" not in groups
    pg.select_option('[data-addspec="0"]', json.dumps(["Pistols", "Ares Predator"], separators=(",", ":")))

    # Raise Firearms 2 -> 3 (6 karma) and Spanish 2 -> 3 (a language: 3 karma).
    pg.locator('[data-raise-skill="0"][data-raise-tier="general"]').click()
    pg.locator('[data-raise-skill="1"][data-raise-tier="general"]').click()
    pg.locator("#modalCommitBtn").click()
    pg.wait_for_timeout(300)

    sent = next(p for p in patches if "skills" in p)
    firearms, spanish = sent["skills"]
    assert firearms["rating"] == 3                                     # raised, never lowered
    assert firearms["concs"] == [{"name": "Pistols", "rating": 4}, {"name": "Shotguns", "rating": 3}]
    assert firearms["specs"] == [{"name": "Ares Predator", "rating": 5, "conc": "Pistols"}]
    assert spanish["rating"] == 3
    assert sent["good_karma"] == 30 - 5 - 5 - 6 - 3
    row = pg.inner_text("#skillList")
    assert "Shotguns" in row and "Ares Predator" in row
    assert errors == [], f"JS errors on the play sheet: {errors}"
    ctx.close()
