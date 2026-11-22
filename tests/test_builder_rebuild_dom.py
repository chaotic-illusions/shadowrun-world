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


def _rebuild_route(posts, contacts=_CONTACTS, char=_CHAR, build=_BUILD):
    def route(r):
        req, path = r.request, r.request.url.split("?")[0]
        if path.endswith((".js", ".css", ".html")) or "/fonts/" in path:
            r.continue_()
        elif path.endswith("/characters/7/rebuild-dossier"):
            posts.append(req.post_data_json)
            r.fulfill(json={"id": 7, "name": "Oversight", "karma_refunded": 28, "good_karma": 30, "nuyen": 500})
        elif path.endswith("/characters/7/chargen-state"):
            r.fulfill(json={"state": build})
        elif path.endswith("/characters/7/contacts"):
            r.fulfill(json=contacts)
        elif path.endswith("/characters/7"):
            r.fulfill(json=char)
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


@pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")
@pytest.mark.parametrize("cash,can_save", [(300, False), (600, True)])
def test_respending_leftover_resources_needs_the_cash_they_became(_browser, _frontend_port, cash, can_save):
    """Loaded with 91,000 Resources unspent (starting cash 9,100). A third contact (5,000 Resources)
    takes back 500 cash: refused with 300 on hand, fine with 600."""
    char = {**_CHAR, "nuyen": cash, "gear": {"vehicles": [{**_CAR_X, "primary": True}], "cyber": [_DATAJACK]}}
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    posts: list[dict] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _rebuild_route(posts, char=char))
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html?edit=7")
    pg.wait_for_selector("#cbxModeBanner:has-text('Rebuilding')", timeout=15000)
    _step(pg, 6)
    pg.locator("#cbxAddContact").click()
    pg.wait_for_timeout(50)
    pg.fill('[data-cname="2"]', "Lou")
    pg.select_option('[data-carch="2"]', "Fixer")
    _submit(pg)
    review = pg.inner_text("#cbxEditReview")
    assert ("Not enough cash" in review) is (not can_save)
    assert (pg.locator("#cbxEditConfirm").count() == 1) is can_save
    if not can_save:
        assert "5,000" in review and "500" in review and "300" in review
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


_ADEPT_SKILLS = [{"name": "Firearms", "attr": "quickness", "group": "combat", "rating": 2, "conc": "", "spec": ""},
                 {"name": "Unarmed Combat", "attr": "strength", "group": "combat", "rating": 4, "conc": "", "spec": ""}]
# Improved Ability as the builder saved it before it took a skill: one 0.25 PP rank, not rated.
_OLD_IMPROVED_ABILITY = {"name": "Improved Ability", "ppEach": 0.25, "rated": False, "lvl": 1, "pp": 0.25}


@pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")
def test_improved_ability_is_rated_priced_by_skill_and_capped_by_combat_skill(_browser, _frontend_port):
    """SR2 p.125: Improved Ability buys dice for one skill at that skill's price (Unarmed Combat
    0.5/die, Firearms 1/die), one line per skill, and a Combat Skill caps the dice at its rating.
    An old single-rank line loads as Athletics (the 0.25 it was charged) and can be re-picked."""
    build = {**_BUILD, "prio": {"race": "E", "magic": "B", "attributes": "A", "skills": "C", "resources": "D"},
             "magicType": "Adept", "skills": _ADEPT_SKILLS, "advancement": {},
             "gear": {"weapons": [], "armor": [], "cyber": [], "bio": [], "gear": [], "matrix": [], "vehicles": []}}
    char = {**_CHAR, "essence": 6, "body": 4, "gear": {}, "nuyen": 0,
            "skills": [{**s, "concs": [], "specs": []} for s in _ADEPT_SKILLS],
            "adept_powers": [_OLD_IMPROVED_ABILITY]}
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    posts: list[dict] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _rebuild_route(posts, char=char, build=build))
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html?edit=7")
    pg.wait_for_selector("#cbxModeBanner:has-text('Rebuilding')", timeout=15000)

    cost = lambda i: pg.inner_text(f'.cbx-line:has([data-delpower="{i}"]) .cbx-line__f')
    level = lambda i: pg.inner_text(f'.cbx-line:has([data-delpower="{i}"]) .cbx-attr__base')
    _step(pg, 3)
    assert pg.eval_on_selector('[data-powerpick="0"]', "el => el.value") == "Athletics"
    assert cost(0) == "0.25 PP" and level(0) == "1"

    pg.select_option('[data-powerpick="0"]', "Unarmed Combat")
    assert cost(0) == "0.5 PP"
    for _ in range(6):
        pg.locator('[data-powerlvl="0"][data-d="1"]').click()
    assert level(0) == "4" and cost(0) == "2 PP"              # capped at Unarmed Combat 4

    pg.select_option('[data-powerpick="0"]', "Firearms")       # 1 PP/die, and Firearms is only 2
    assert level(0) == "2" and cost(0) == "2 PP"

    pg.locator('[data-inspect="Improved Ability"]').click()
    pg.locator('[data-addpower="Improved Ability"]').click()   # goes to the best-rated free skill
    assert pg.eval_on_selector('[data-powerpick="1"]', "el => el.value") == "Unarmed Combat"
    assert pg.locator('[data-powerpick="1"] option[value="Firearms"]').is_disabled()

    # Firearms dropped below the dice bought: warned and the save is refused.
    _step(pg, 4)
    pg.locator('[data-skill="0"][data-d="-1"]').click()
    _step(pg, 3)
    assert "Firearms is only rated 1" in pg.inner_text("#cbxStepBody")
    _submit(pg)
    assert "Firearms is only rated 1" in pg.inner_text("#cbxSubmitStatus")
    assert pg.locator("#cbxEditConfirm").count() == 0

    _step(pg, 3)
    pg.locator('[data-powerlvl="0"][data-d="-1"]').click()
    _submit(pg)
    assert pg.locator("#cbxEditConfirm").count() == 1, pg.inner_text("#cbxSubmitStatus")
    pg.locator("#cbxEditConfirm").click()
    pg.wait_for_timeout(400)
    sent = posts[0]
    DossierRebuild(**sent)
    assert [(p["skill"], p["lvl"], p["rated"], p["pp"]) for p in sent["adept_powers"]] == [
        ("Firearms", 1, True, 1), ("Unarmed Combat", 1, True, 0.5)]
    assert errors == [], f"JS errors during the rebuild: {errors}"
    ctx.close()


@pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")
def test_adept_power_picks_doubling_and_chargen_limits(_browser, _frontend_port):
    """Quick Draw is one line per weapon type (Firearms / Melee Weapons), never twice the same;
    Attribute Boost and Improved Physical Senses each take a pick; Killing Hands + Distance Strike
    doubles the second; Enhanced Centering isn't offered; Pain Resistance goes to 9; Mystic Armor
    stops at the Magic Rating."""
    build = {**_BUILD, "prio": {"race": "E", "magic": "B", "attributes": "A", "skills": "C", "resources": "D"},
             "magicType": "Adept", "skills": _ADEPT_SKILLS, "advancement": {},
             "gear": {"weapons": [], "armor": [], "cyber": [], "bio": [], "gear": [], "matrix": [], "vehicles": []}}
    # A Delta Datajack (0.1 Essence) leaves Essence 5.9: Magic Rating 5.
    char = {**_CHAR, "essence": 5.9, "body": 4, "gear": {"cyber": [_DATAJACK]}, "nuyen": 0,
            "skills": [{**s, "concs": [], "specs": []} for s in _ADEPT_SKILLS], "adept_powers": []}
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    posts: list[dict] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    inner = _rebuild_route(posts, char=char, build=build)

    def route(r):                                              # Grimoire + Awakenings switched on
        if r.request.url.split("?")[0].endswith("/catalog/books") and r.request.method == "GET":
            r.fulfill(json={"enabled": ["GRIM", "AWK"], "core": {"code": "SR2", "name": "Shadowrun, Second Edition"},
                            "official": [{"code": "GRIM", "name": "Grimoire", "enabled": True},
                                         {"code": "AWK", "name": "Awakenings", "enabled": True}]})
        else:
            inner(r)
    pg.route("**/*", route)
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html?edit=7")
    pg.wait_for_selector("#cbxModeBanner:has-text('Rebuilding')", timeout=15000)
    _step(pg, 3)
    assert pg.locator('[data-inspect="Body Control"]').count() == 1   # a Grimoire power is offered

    def add(name):                                             # opens the shop row unless it's open
        if pg.locator(f'[data-inspect="{name}"][aria-expanded="true"]').count() == 0:
            pg.locator(f'[data-inspect="{name}"]').click()
        pg.locator(f'[data-addpower="{name}"]').click()

    cost = lambda i: pg.inner_text(f'.cbx-line:has([data-delpower="{i}"]) .cbx-line__f')
    pick = lambda i: pg.eval_on_selector(f'[data-powerpick="{i}"]', "el => el.value")

    assert pg.locator('[data-inspect="Enhanced Centering"]').count() == 0

    add("Quick Draw")                                          # 0: Firearms
    add("Quick Draw")                                          # 1: Melee Weapons
    assert (pick(0), pick(1)) == ("Firearms", "Melee Weapons")
    assert pg.locator('[data-powerpick="1"] option[value="Firearms"]').is_disabled()
    assert pg.locator('.cbx-shopitem.is-open button:has-text("Added")').is_disabled()   # both taken
    # A forced duplicate (the option re-enabled by hand) is refused.
    pg.eval_on_selector('[data-powerpick="1"]', "el => { el.options[0].disabled = false; }")
    pg.select_option('[data-powerpick="1"]', "Firearms")
    assert pick(1) == "Melee Weapons"
    pg.locator('[data-delpower="1"]').click()
    pg.locator('[data-delpower="0"]').click()

    add("Attribute Boost")                                     # 0
    add("Attribute Boost")                                     # 1
    assert (pick(0), pick(1)) == ("body", "strength")
    assert pg.locator('[data-powerlvl="1"]').count() == 2      # bought in levels
    pg.locator('[data-delpower="1"]').click()
    pg.locator('[data-delpower="0"]').click()

    add("Improved Physical Senses")                            # 0
    add("Improved Physical Senses")                            # 1
    assert (pick(0), pick(1)) == ("Low-Light Vision", "Thermographic Vision")
    assert pg.locator('[data-powerlvl="0"]').count() == 0      # one sense per line, no levels
    assert cost(0) == "0.25 PP" and cost(1) == "0.25 PP"
    pg.locator('[data-delpower="1"]').click()
    pg.locator('[data-delpower="0"]').click()

    add("Killing Hands")                                       # 0: 0.5
    add("Distance Strike")                                     # 1: bought second, 2 x 2
    assert cost(0) == "0.5 PP" and cost(1) == "4 PP"
    pg.locator('[data-delpower="0"]').click()                  # Distance Strike alone: normal price
    assert cost(0) == "2 PP"
    add("Killing Hands")                                       # now Killing Hands is second: 0.5 x 2
    assert cost(1) == "1 PP"
    pg.locator('[data-delpower="0"]').click()
    pg.locator('[data-delpower="0"]').click()

    add("Pain Resistance")
    for _ in range(12):
        pg.locator('[data-powerlvl="0"][data-d="1"]').click()
    assert pg.inner_text('.cbx-line:has([data-delpower="0"]) .cbx-attr__base') == "9"
    pg.locator('[data-delpower="0"]').click()

    add("Mystic Armor")                                        # no more levels than Magic Rating 5
    for _ in range(8):
        pg.locator('[data-powerlvl="0"][data-d="1"]').click()
    assert pg.inner_text('.cbx-line:has([data-delpower="0"]) .cbx-attr__base') == "5"
    assert errors == [], f"JS errors on the magic step: {errors}"
    ctx.close()



@pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")
def test_adept_powers_feed_the_committed_attributes_reaction_and_initiative(_browser, _frontend_port):
    """Improved Physical Attributes is part of the committed attribute (attribute points still buy
    only the base); Increased Reaction / Increased Reflexes show in the summary's Reaction and
    Initiative."""
    build = {**_BUILD, "prio": {"race": "E", "magic": "B", "attributes": "A", "skills": "C", "resources": "D"},
             "magicType": "Adept", "skills": _ADEPT_SKILLS, "advancement": {},
             "gear": {"weapons": [], "armor": [], "cyber": [], "bio": [], "gear": [], "matrix": [], "vehicles": []}}
    powers = [{"name": "Improved Physical Attributes", "attr": "strength", "rated": True, "lvl": 2, "ppEach": 0.5},
              {"name": "Increased Reaction", "rated": True, "lvl": 1, "ppEach": 0.5},
              {"name": "Increased Reflexes", "rated": True, "lvl": 1, "ppEach": 1}]
    char = {**_CHAR, "essence": 6, "body": 4, "strength": 6, "gear": {}, "nuyen": 0,
            "skills": [{**s, "concs": [], "specs": []} for s in _ADEPT_SKILLS], "adept_powers": powers}
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    posts: list[dict] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _rebuild_route(posts, char=char, build=build))
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html?edit=7")
    pg.wait_for_selector("#cbxModeBanner:has-text('Rebuilding')", timeout=15000)

    _step(pg, 7)
    cell = lambda k: pg.inner_text(f'.rev-cell:has(.k:text-is("{k}")) .v')
    assert cell("Strength") == "6"                               # base 4 + Improved Physical Attributes 2
    assert cell("Reaction") == "5"                               # (4+4)/2 + Increased Reaction 1
    assert cell("Initiative") == "2D6"                           # 1 + Increased Reflexes 1
    # The stored Strength 6 already includes the power: loading it changes nothing.
    _submit(pg)
    assert "Nothing has changed" in pg.inner_text("#cbxSubmitStatus")

    _step(pg, 3)
    pg.locator('[data-powerlvl="0"][data-d="1"]').click()       # Improved Physical Attributes 3
    _submit(pg)
    assert pg.locator("#cbxEditConfirm").count() == 1, pg.inner_text("#cbxSubmitStatus")
    pg.locator("#cbxEditConfirm").click()
    pg.wait_for_timeout(400)
    sent = posts[0]
    assert sent["strength"] == 7
    assert sent["chargen_state"]["base"]["strength"] == 4       # attribute points bought only the base
    assert errors == [], f"JS errors during the rebuild: {errors}"
    ctx.close()


@pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")
def test_builder_spell_fetish_toggle_and_foci_bind_to_real_picks(_browser, _frontend_port):
    """A spell can be marked as needing a fetish; a spell focus binds to a real spell category from a
    list (no free text), and an unbound one blocks the save."""
    spells = [{"name": "Stunbolt", "cat": "combat", "force": 3}, {"name": "Heal", "cat": "health", "force": 3}]
    # Resources B (400,000) so a 75,000 focus fits; Attributes C (20 points) for six 3s.
    build = {**_BUILD, "prio": {"race": "E", "magic": "A", "attributes": "C", "skills": "D", "resources": "B"},
             "base": {a: 3 for a in ("body", "quickness", "strength", "charisma", "intelligence", "willpower")},
             "magicType": "Full Mage", "tradition": "Hermetic", "spells": spells, "advancement": {},
             "gear": {"weapons": [], "armor": [], "cyber": [], "bio": [], "gear": [], "matrix": [], "vehicles": []}}
    char = {**_CHAR, "essence": 6, "gear": {}, "nuyen": 100000, "magic_type": "Full Mage", "tradition": "Hermetic",
            "spells": spells, **{a: 3 for a in ("body", "quickness", "strength", "charisma", "intelligence", "willpower")}}
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    posts: list[dict] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _rebuild_route(posts, char=char, build=build))
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html?edit=7")
    pg.wait_for_selector("#cbxModeBanner:has-text('Rebuilding')", timeout=15000)

    _step(pg, 3)
    pg.locator('[data-spellfetish="1"]').check()                  # Heal needs a fetish
    pg.locator('[data-addfocus]', has_text="Spell Category Focus").first.click()
    pg.wait_for_timeout(100)
    sel = '.cbx-skill:has-text("Spell Category Focus") select[data-focusapplies]'
    assert pg.locator(sel).count() == 1                            # a list, not a text box
    assert pg.eval_on_selector(sel, "el => el.value") == ""
    _submit(pg)
    assert "Pick what each focus is bound to" in pg.inner_text("#cbxSubmitStatus")

    _step(pg, 3)
    pg.select_option(sel, "health")
    _submit(pg)
    assert pg.locator("#cbxEditConfirm").count() == 1, pg.inner_text("#cbxEditReview")
    pg.locator("#cbxEditConfirm").click()
    pg.wait_for_timeout(400)
    sent = posts[0]
    assert [s.get("fetish", False) for s in sent["spells"]] == [False, True]
    assert sent["gear"]["foci"][0]["applies"] == "health"
    assert errors == [], f"JS errors during the rebuild: {errors}"
    ctx.close()


@pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")
def test_improved_ability_cap_is_the_general_rating(_browser, _frontend_port):
    """Firearms with a Pistols Concentration commits as Firearms 3 / Pistols 5: Improved Ability for
    Firearms stops at 3 dice, the general rating, not the line's 4."""
    skills = [{"name": "Firearms", "attr": "quickness", "group": "combat", "rating": 4, "conc": "Pistols", "spec": ""}]
    build = {**_BUILD, "prio": {"race": "E", "magic": "B", "attributes": "A", "skills": "C", "resources": "D"},
             "magicType": "Adept", "skills": skills, "advancement": {},
             "gear": {"weapons": [], "armor": [], "cyber": [], "bio": [], "gear": [], "matrix": [], "vehicles": []}}
    char = {**_CHAR, "essence": 6, "body": 4, "gear": {}, "nuyen": 0, "adept_powers": [],
            "skills": [{"name": "Firearms", "attr": "quickness", "group": "combat", "rating": 3,
                        "concs": [{"name": "Pistols", "rating": 5}], "specs": []}]}
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _rebuild_route([], char=char, build=build))
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html?edit=7")
    pg.wait_for_selector("#cbxModeBanner:has-text('Rebuilding')", timeout=15000)
    _step(pg, 3)
    pg.locator('[data-inspect="Improved Ability"]').click()
    pg.locator('[data-addpower="Improved Ability"]').click()
    pg.select_option('[data-powerpick="0"]', "Firearms")
    for _ in range(6):
        pg.locator('[data-powerlvl="0"][data-d="1"]').click()
    assert pg.inner_text('.cbx-line:has([data-delpower="0"]) .cbx-attr__base') == "3"
    assert errors == [], f"JS errors: {errors}"
    ctx.close()


@pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")
def test_spell_focus_needs_a_spell_to_bind_to(_browser, _frontend_port):
    """A Specific Spell Focus can't be committed when the runner knows no spell to bind it to."""
    build = {**_BUILD, "prio": {"race": "E", "magic": "A", "attributes": "C", "skills": "D", "resources": "B"},
             "base": {a: 3 for a in ("body", "quickness", "strength", "charisma", "intelligence", "willpower")},
             "magicType": "Full Mage", "tradition": "Hermetic", "spells": [], "advancement": {},
             "gear": {"weapons": [], "armor": [], "cyber": [], "bio": [], "gear": [], "matrix": [], "vehicles": []}}
    char = {**_CHAR, "essence": 6, "gear": {}, "nuyen": 100000, "magic_type": "Full Mage", "tradition": "Hermetic",
            "spells": [], **{a: 3 for a in ("body", "quickness", "strength", "charisma", "intelligence", "willpower")}}
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _rebuild_route([], char=char, build=build))
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html?edit=7")
    pg.wait_for_selector("#cbxModeBanner:has-text('Rebuilding')", timeout=15000)
    _step(pg, 3)
    pg.locator('[data-addfocus]', has_text="Specific Spell Focus").first.click()
    _submit(pg)
    assert "Specific Spell Focus (learn a spell first)" in pg.inner_text("#cbxSubmitStatus")
    assert errors == [], f"JS errors: {errors}"
    ctx.close()


@pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")
def test_rigging_gets_only_the_vcr_bonus(_browser, _frontend_port):
    """Rigging Reaction / Initiative are the base (Q+I)/2 plus only the VCR (+2 Reaction, +1D6 per
    level): Wired Reflexes counts for the physical line only."""
    build = {**_BUILD, "base": {"body": 4, "quickness": 4, "strength": 4, "charisma": 4, "intelligence": 4, "willpower": 4},
             "advancement": {},
             "gear": {"weapons": [], "armor": [], "bio": [], "gear": [], "matrix": [], "vehicles": [],
                      "cyber": [{"n": "Vehicle Control Rig", "sub": "headware", "grade": "Standard", "rated": True, "rating": 1,
                                 "maxRating": 3, "baseEss": 2, "baseCost": 12000, "modsPer": {"reaction": 2, "initDice": 1}},
                                {"n": "Wired Reflexes", "sub": "bodyware", "grade": "Standard", "rated": True, "rating": 1,
                                 "maxRating": 3, "baseEss": 2, "baseCost": 55000, "modsPer": {"reaction": 2, "initDice": 1}}]}}
    char = {**_CHAR, "essence": 2, "gear": {"cyber": build["gear"]["cyber"]}}
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _rebuild_route([], char=char, build=build))
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html?edit=7")
    pg.wait_for_selector("#cbxModeBanner:has-text('Rebuilding')", timeout=15000)
    _step(pg, 7)
    cell = lambda k: pg.inner_text(f'.rev-cell:has(.k:text-is("{k}")) .v')
    assert cell("Reaction") == "6 / 6"                          # physical 4 + Wired 2; rigging 4 + VCR 2
    assert cell("Initiative") == "2D6 / 2D6"                    # physical 1 + Wired 1; rigging 1 + VCR 1
    assert errors == [], f"JS errors: {errors}"
    ctx.close()
