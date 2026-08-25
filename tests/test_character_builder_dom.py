"""Headless-browser smoke test for the SR2 character builder (Playwright).

Loads frontend/character-builder.html with /catalog/* stubbed from the real catalog
data and asserts the wizard boots, walks every step, buys gear, and commits -- with
zero uncaught JS errors. Skipped cleanly when Playwright or a system Chromium
(Edge/Chrome) is unavailable, so CI/Docker without a browser stays green.
"""
from __future__ import annotations

import functools
import http.server
import re
import socketserver
import threading

import pytest

from app.data import catalog as cat

try:
    from playwright.sync_api import sync_playwright
except Exception:  # noqa: BLE001 -- playwright optional
    sync_playwright = None

pytestmark = pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")


@pytest.fixture(scope="module")
def _frontend_port():
    handler_cls = type(
        "_QuietHandler",
        (http.server.SimpleHTTPRequestHandler,),
        {"log_message": lambda *a, **k: None},
    )
    srv = socketserver.TCPServer(
        ("127.0.0.1", 0), functools.partial(handler_cls, directory="frontend")
    )
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    try:
        yield srv.server_address[1]
    finally:
        srv.shutdown()


@pytest.fixture(scope="module")
def _browser():
    with sync_playwright() as p:
        browser = None
        for candidate in ("msedge", "chrome"):
            try:
                browser = p.chromium.launch(channel=candidate, headless=True)
                break
            except Exception:  # noqa: BLE001 -- try the next system browser
                continue
        if browser is None:
            pytest.skip("no system Chromium (Edge/Chrome) available for Playwright")
        try:
            yield browser
        finally:
            browser.close()


def _route(route):
    url = route.request.url
    path = url.split("?")[0]
    # Never intercept static assets (matrix-programs.js etc. would otherwise match "/matrix").
    if path.endswith((".js", ".css", ".html")) or "/fonts/" in path:
        route.continue_()
        return
    if "/auth/verify" in url:
        route.fulfill(json={"is_admin": True, "is_user": False, "is_default_password": False})
    elif "/catalog/rules" in url:
        route.fulfill(json=cat.get_rules())
    elif "/catalog/books" in url:
        if route.request.method == "PUT":
            enabled = (route.request.post_data_json or {}).get("enabled", [])
        else:
            enabled = ["SSC", "CYB"]
        official = [
            {"code": "SSC", "name": "Street Samurai Catalog", "enabled": "SSC" in enabled},
            {"code": "SHADOW", "name": "Shadowtech", "enabled": "SHADOW" in enabled},
            {"code": "CYB", "name": "Cybertechnology", "enabled": "CYB" in enabled},
            {"code": "RIG2", "name": "Rigger 2", "enabled": "RIG2" in enabled},
        ]
        route.fulfill(json={"enabled": enabled,
                            "core": {"code": "SR2", "name": "Shadowrun, Second Edition"},
                            "official": official,
                            # includes: real /catalog/books responses always carry this (schema
                            # default []) -- manage-sourcebooks.html does an unconditional
                            # fan.includes.join(...), which throws against a stub missing it.
                            "fan": {"code": "FAN", "name": "Fan Content", "enabled": "FAN" in enabled,
                                    "includes": ["BSW", "RG"]}})
    elif "/catalog/skill-specs" in url:
        if route.request.method == "PUT":
            specs = (route.request.post_data_json or {}).get("specs", {})
            route.fulfill(json={"specs": specs})
        else:
            skills = [
                {"n": s.get("n"), "attr": s.get("attr"), "group": s.get("group"), "conc": s.get("conc", [])}
                for s in cat.get_rules().get("skills", [])
            ]
            route.fulfill(json={"skills": skills, "specs": {}})
    elif "/catalog/" in url:
        name = url.split("/catalog/")[1].split("?")[0].strip("/")
        items = cat.get_catalog(name) if name in cat.ITEM_CATALOGS else []
        route.fulfill(json={"catalog": name, "count": len(items), "items": items})
    elif "deck-builder-state" in url:
        route.fulfill(json={"state": {"chargen": {"spent": 50000}}})
    elif "finalize-dossier" in url or "dossier-draft" in url:
        body = route.request.post_data_json or {}
        route.fulfill(json={
            "id": 5, "name": body.get("name", "Draftrunner"), "is_pc": True, "is_claimed": True,
            "organization_name": None,
            "created_at": "2026-01-01T00:00:00Z", "updated_at": "2026-01-01T00:00:00Z",
        })
    elif "/characters/dossier" in url:
        body = route.request.post_data_json or {}
        route.fulfill(
            status=201,
            json={
                "id": 1, "name": body.get("name", "Runner"), "is_pc": True, "is_claimed": True,
                "organization_name": None,
                "created_at": "2026-01-01T00:00:00Z", "updated_at": "2026-01-01T00:00:00Z",
            },
        )
    elif any(m in url for m in ("/characters", "/runs", "/matrix", "/rtgs",
                                "/organizations", "/locations", "/contacts", "/reputation")):
        route.fulfill(json=[])
    else:
        route.continue_()


@pytest.fixture(scope="module")
def page_and_errors(_browser, _frontend_port):
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.setItem('sr_admin_token','tok'); localStorage.removeItem('sr2_dossier_v1'); sessionStorage.clear();")
    pg = ctx.new_page()
    errors: list[str] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _route)
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html")
    pg.wait_for_selector("#cbxNewRunner", timeout=15000)   # landing page
    pg.locator("#cbxNewRunner").click()                     # enter the wizard
    pg.wait_for_selector(".cbx-priogrid", timeout=15000)
    return pg, errors


def test_builder_boots_without_errors(page_and_errors):
    page, errors = page_and_errors
    assert errors == [], f"JS errors on boot: {errors}"
    assert page.locator(".wstep-dot").count() == 7


def test_builder_walks_all_steps_buys_gear_and_commits(page_and_errors):
    page, errors = page_and_errors

    # Apply the first quick-start kit -> fills priorities/attributes/skills/gear in one shot.
    page.locator("[data-kit]").first.click()
    page.wait_for_timeout(80)

    # Walk every step via the rail; each must render a non-empty body.
    for i in range(7):
        page.locator(f'.wstep-dot[data-step="{i}"]').click()
        page.wait_for_timeout(60)
        assert page.locator("#cbxStepBody").inner_text().strip() != ""

    # Add a Computer skill (exercises the skill picker; a common decker prerequisite).
    page.locator('.wstep-dot[data-step="4"]').click()
    page.wait_for_timeout(60)
    add_comp = page.locator('[data-addskill="Computer"]').first
    if add_comp.count():
        add_comp.click()
        page.wait_for_timeout(60)

    # Required-concentration skills (e.g. Etiquette from the kit) now start with NO concentration
    # and flag the row red, blocking commit until chosen. Pick the first real option for each.
    for _ in range(6):
        row = page.locator('.cbx-skillrow--needs').first
        if row.count() == 0:
            break
        sel = row.locator('[data-conc]').first
        val = sel.evaluate("el => (Array.from(el.options).find(o => o.value) || {}).value || ''")
        if not val:
            break
        sel.select_option(val)
        page.wait_for_timeout(50)

    # A kit lands exactly at the skill budget, so trim one point to fit the added Computer skill
    # (commit now blocks over-budget builds).
    dec = page.locator('[data-skill="0"][data-d="-1"]').first
    if dec.count():
        dec.click()
        page.wait_for_timeout(60)

    # Asset Manifest: weapons/armor/cyber/bio/gear/matrix/vehicles now buy through the shared
    # gear-picker.js component (#cbxGearPicker) -- same one play-sheet.html's Buy Gear modal uses.
    # The deckware Programs picker isn't a catalog item, so it still renders as its own panel below.
    page.locator('.wstep-dot[data-step="5"]').click()
    page.wait_for_timeout(60)
    page.wait_for_selector("#cbxGearPicker .gc-grid", timeout=15000)

    # Expand a program row (Sleaze) and add it to the loadout, then confirm the loadout row appears.
    page.locator('[data-proginspect="sleaze"]').click()
    page.wait_for_timeout(60)
    page.locator('[data-progadd="sleaze"]').click()
    page.wait_for_timeout(60)
    assert page.locator("[data-progdel]").count() >= 1

    picker = page.locator("#cbxGearPicker")
    picker.locator('[data-cat="bioware"]').click()
    page.wait_for_timeout(60)
    bio_row = picker.locator("#gcList [data-pick]").first
    if bio_row.count():
        bio_row.click()
        page.wait_for_timeout(60)
        buy = picker.locator("#gcBuy")
        if buy.count():
            buy.click()
            page.wait_for_timeout(60)

    # Cyberware: buy an item, then confirm the owned line's grade selector (Loadout column) still
    # lets you switch it to Alpha post-purchase (SSC is enabled in the stub).
    picker.locator('[data-cat="cyberware"]').click()
    page.wait_for_timeout(60)
    cyber_row = picker.locator("#gcList [data-pick]").first
    if cyber_row.count():
        cyber_row.click()
        page.wait_for_timeout(60)
        cyber_buy = picker.locator("#gcBuy")
        if cyber_buy.count():
            cyber_buy.click()
            page.wait_for_timeout(60)
            grade_sel = page.locator(".cbx-owned-wrap [data-cybergrade]").first
            assert grade_sel.count() == 1
            grade_sel.select_option("Alpha")
            page.wait_for_timeout(60)

    # Finish + commit (stubbed 201).
    page.locator('.wstep-dot[data-step="6"]').click()
    page.wait_for_timeout(60)
    page.fill('[data-id="handle"]', "Testrunner")
    page.locator("#cbxSubmit").click()
    page.wait_for_timeout(150)

    assert "Committed" in page.locator("#cbxSubmitStatus").inner_text()
    assert errors == [], f"JS errors during walkthrough: {errors}"


# An existing PC returned by GET /characters/{id} for the convert path.
_CONVERT_CHAR = {
    "id": 7, "name": "Old Runner", "is_pc": True, "race": "Elf",
    "body": 3, "quickness": 5, "strength": 2, "charisma": 6, "intelligence": 6, "willpower": 5,
    "essence": 6.0, "body_index": 0.0, "magic_rating": 0, "magic_type": None,
    "priorities": {"race": "A", "magic": "E", "attributes": "B", "skills": "C", "resources": "D"},
    "skills": [{"name": "Firearms", "attr": "quickness", "group": "active", "rating": 4, "conc": "", "spec": ""}],
    "spells": [], "adept_powers": [], "gear": {},
    "lifestyle_level": 2, "lifestyle_permanent": False,
    "gender": "M", "age": 30, "description": "Veteran shadowrunner.",
}


def _convert_route(route):
    url = route.request.url
    path = url.split("?")[0]
    if "/auth/verify" in url:
        route.fulfill(json={"is_admin": True, "is_user": False, "is_default_password": False})
    elif "/catalog/rules" in url:
        route.fulfill(json=cat.get_rules())
    elif "/catalog/books" in url:
        route.fulfill(json={"enabled": ["SSC", "CYB"], "core": {"code": "SR2", "name": "SR2"},
                            "official": [], "fan": {"code": "FAN", "name": "Fan"}})
    elif "/catalog/" in url:
        name = url.split("/catalog/")[1].split("?")[0].strip("/")
        items = cat.get_catalog(name) if name in cat.ITEM_CATALOGS else []
        route.fulfill(json={"catalog": name, "count": len(items), "items": items})
    elif "/characters/drafts" in url:
        route.fulfill(json=[])
    elif "deck-builder-state" in url:
        route.fulfill(json={"state": {}})
    elif "convert-dossier" in url:
        body = route.request.post_data_json or {}
        route.fulfill(json={"id": 7, "name": body.get("name", "Old Runner"), "is_pc": True, "is_claimed": True,
                            "organization_name": None,
                            "created_at": "2026-01-01T00:00:00Z", "updated_at": "2026-01-01T00:00:00Z"})
    elif "/contacts" in url:
        route.fulfill(json=[])
    elif re.search(r"/characters/\d+$", path):
        route.fulfill(json=_CONVERT_CHAR)
    elif "/characters" in url:
        route.fulfill(json=[])
    else:
        route.continue_()


def test_builder_convert_hydrates_and_posts_convert_dossier(_browser, _frontend_port):
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    posts: list[str] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.on("request", lambda r: posts.append(r.url) if r.method == "POST" else None)
    pg.route("**/*", _convert_route)

    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html?convert=7")
    pg.wait_for_selector(".cbx-priogrid", timeout=15000)
    pg.wait_for_timeout(200)

    # Convert mode banner is shown, and the char's priorities hydrated (all five set -> committable).
    assert "Converting" in pg.inner_text("#cbxModeBanner")
    # Commit -> should POST to the convert-dossier endpoint and report "Converted".
    pg.locator('.wstep-dot[data-step="6"]').click()
    pg.wait_for_timeout(80)
    pg.locator("#cbxSubmit").click()
    pg.wait_for_timeout(200)

    assert any("/characters/7/convert-dossier" in u for u in posts), posts
    assert "Converted" in pg.locator("#cbxSubmitStatus").inner_text()
    assert errors == [], f"JS errors during convert: {errors}"
    ctx.close()


def test_builder_skills_grouping_required_conc_and_na_spec(_browser, _frontend_port):
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _route)
    pg.goto(f"http://127.0.0.1:{_frontend_port}/character-builder.html")
    pg.wait_for_selector("#cbxNewRunner", timeout=15000)
    pg.locator("#cbxNewRunner").click()
    pg.wait_for_selector(".cbx-priogrid", timeout=15000)

    # Skills step: the picker is group cards, including a Build/Repair card.
    pg.locator('.wstep-dot[data-step="4"]').click()
    pg.wait_for_timeout(100)
    assert pg.locator(".cbx-skillcard__h", has_text="Build/Repair").count() >= 1
    assert pg.locator('[data-addskill="Computer B/R"]').count() == 1

    # Etiquette: required concentration with NO default -- the player must choose. It shows a
    # "-- choose --" placeholder, starts empty, and flags the row red until a pick is made.
    pg.locator('[data-addskill="Etiquette"]').first.click()
    pg.wait_for_timeout(80)
    assert pg.locator(".cbx-skillrow").count() >= 1  # chosen skill renders on one row
    has_placeholder = pg.eval_on_selector('[data-conc="0"]', "el => Array.from(el.options).some(o => o.value === '')")
    assert has_placeholder is True                    # required + unset -> placeholder option present
    conc_val = pg.eval_on_selector('[data-conc="0"]', "el => el.value")
    assert conc_val == ""                             # no auto-default; awaiting a choice
    assert pg.locator(".cbx-skillrow--needs").count() >= 1   # row flagged red
    assert pg.locator(".cbx-narrowsel:disabled").count() >= 1  # specialization N/A disabled
    # Pick a concentration -> the red flag clears.
    first_conc = pg.eval_on_selector('[data-conc="0"]', "el => (Array.from(el.options).find(o => o.value) || {}).value")
    pg.select_option('[data-conc="0"]', first_conc)
    pg.wait_for_timeout(80)
    assert pg.locator(".cbx-skillrow--needs").count() == 0   # choice made -> no longer red

    # Firearms: optional concentration (has "(none)"); specialization is gated behind a concentration.
    pg.locator('[data-addskill="Firearms"]').first.click()
    pg.wait_for_timeout(80)
    fire_none = pg.eval_on_selector('[data-conc="1"]', "el => Array.from(el.options).some(o => o.value === '')")
    assert fire_none is True
    assert pg.locator('[data-spec="1"]').count() == 0   # no spec dropdown until a concentration is picked
    pg.select_option('[data-conc="1"]', "Pistols")
    pg.wait_for_timeout(80)
    assert pg.locator('[data-spec="1"]').count() == 1   # weapon specialization dropdown now present

    assert errors == [], f"JS errors on skills step: {errors}"
    ctx.close()


def test_sourcebooks_page_toggles_books(_browser, _frontend_port):
    """The GM sourcebook toggle lives on manage-sourcebooks.html (moved off the character
    builder, gated admin-only, and reachable from the Admin Control nav dropdown)."""
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    puts: list[str] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.on("request", lambda r: puts.append(r.url) if r.method == "PUT" else None)
    pg.route("**/*", _route)
    pg.goto(f"http://127.0.0.1:{_frontend_port}/manage-sourcebooks.html")
    pg.wait_for_selector("#sbMain", state="visible", timeout=15000)

    # A Shadowtech toggle is present (off in the stub).
    shadow = pg.locator('[data-book="SHADOW"]')
    assert shadow.count() == 1
    assert shadow.is_checked() is False

    # Enabling it PUTs the new book set (unlocking bioware / that book's gear).
    shadow.check()
    pg.wait_for_timeout(250)
    assert any(u.endswith("/catalog/books") for u in puts), puts
    assert errors == [], f"JS errors toggling sources: {errors}"
    ctx.close()


def test_admin_control_nav_group_gates_downtime_and_sourcebooks(_browser, _frontend_port):
    """The Admin Control dropdown is visible to everyone; Downtime/Sourcebooks inside it are
    gm-only, Tokens is not."""
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_user_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))

    def _player_route(route):
        url = route.request.url
        if "/auth/verify" in url:
            route.fulfill(json={"is_admin": False, "is_user": True, "is_default_password": False})
        else:
            _route(route)

    pg.route("**/*", _player_route)
    pg.goto(f"http://127.0.0.1:{_frontend_port}/manage-sourcebooks.html")
    pg.wait_for_selector(".nav-group--admin", timeout=15000)
    pg.wait_for_selector("#sbNotGm", state="visible", timeout=15000)  # confirms bootstrapAuth finished

    group = pg.locator(".nav-group--admin")
    assert group.count() == 1
    # .nav-group-menu is display:none except on :hover/:focus-within/.open (style.css) -- open it
    # first, otherwise every link is invisible regardless of the gm-only gate and the "should be
    # visible" assertion below can never actually catch a regression.
    group.hover()
    assert group.locator('a[href="manage-tokens.html"]').is_visible()
    assert not group.locator('a[href="manage-downtime.html"]').is_visible()
    assert not group.locator('a[href="manage-sourcebooks.html"]').is_visible()
    assert errors == [], f"JS errors on Admin Control nav gate check: {errors}"
    ctx.close()

