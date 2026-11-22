"""Every PC archetype picker offers the one shared list (frontend/shared.js RUNNER_ARCHETYPES) plus
"Custom...": the GM's Characters editor builds its options from it, and World State's archetype
editor takes its labels (and card colour classes) from it. Stubbed API; same Playwright setup as
tests/test_character_builder_dom.py.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from tests.test_character_builder_dom import _browser, _frontend_port, _route, sync_playwright  # noqa: F401 -- fixtures

pytestmark = pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")

_OFFICIAL = ["Street Samurai", "Decker", "Rigger", "Mage", "Shaman", "Adept"]


_SHARED_JS = Path(__file__).resolve().parents[1] / "frontend" / "shared.js"
_LIST = "const RUNNER_ARCHETYPES = ['Street Samurai', 'Decker', 'Rigger', 'Mage', 'Shaman', 'Adept'];"


def _page(_browser, url, extra_archetype=None):
    """Open a page with the API stubbed. With `extra_archetype`, shared.js is served with one more
    official archetype -- a page that reads the shared list shows it; a hand-typed copy doesn't."""
    ctx = _browser.new_context()
    ctx.add_init_script("localStorage.clear(); sessionStorage.clear(); localStorage.setItem('sr_admin_token','tok');")
    pg = ctx.new_page()
    errors: list[str] = []
    pg.on("pageerror", lambda exc: errors.append(str(exc)))
    pg.route("**/*", _route)
    if extra_archetype:
        src = _SHARED_JS.read_text(encoding="utf-8")
        assert src.count(_LIST) == 1
        patched = src.replace(_LIST, _LIST.replace("'Adept'", f"'Adept', '{extra_archetype}'"))
        pg.route("**/shared.js", lambda r: r.fulfill(body=patched, content_type="application/javascript"))
    pg.goto(url)
    pg.wait_for_load_state("networkidle")
    return ctx, pg, errors


def test_shared_list_is_the_official_archetypes(_browser, _frontend_port):
    ctx, pg, errors = _page(_browser, f"http://127.0.0.1:{_frontend_port}/manage-characters.html")
    assert pg.evaluate("RUNNER_ARCHETYPES") == _OFFICIAL
    ctx.close()


def test_gm_characters_editor_offers_the_shared_list_plus_custom(_browser, _frontend_port):
    ctx, pg, errors = _page(_browser, f"http://127.0.0.1:{_frontend_port}/manage-characters.html")
    values = pg.eval_on_selector("#f-archetype-pc", "el => Array.from(el.options).map(o => o.value)")
    labels = pg.eval_on_selector("#f-archetype-pc", "el => Array.from(el.options).map(o => o.textContent)")
    assert values == _OFFICIAL + ["Custom"]
    assert labels[-1] == "Custom..."
    assert errors == [], f"JS errors on the Characters page: {errors}"
    ctx.close()
    # An archetype added to the shared list shows up here without touching this page.
    ctx, pg, errors = _page(_browser, f"http://127.0.0.1:{_frontend_port}/manage-characters.html", "Face")
    values = pg.eval_on_selector("#f-archetype-pc", "el => Array.from(el.options).map(o => o.value)")
    assert values == _OFFICIAL + ["Face", "Custom"]
    ctx.close()


def test_world_state_archetype_editor_uses_the_shared_list(_browser, _frontend_port):
    ctx, pg, errors = _page(_browser, f"http://127.0.0.1:{_frontend_port}/world-state.html")
    arch = pg.evaluate("ARCHETYPES")
    assert [a["label"] for a in arch] == _OFFICIAL + ["Custom"]
    assert [a["cls"] for a in arch] == ["arch-samurai", "arch-decker", "arch-rigger", "arch-mage",
                                       "arch-shaman", "arch-adept", "arch-custom"]
    assert errors == [], f"JS errors on World State: {errors}"
    ctx.close()
    ctx, pg, errors = _page(_browser, f"http://127.0.0.1:{_frontend_port}/world-state.html", "Face")
    assert [a["label"] for a in pg.evaluate("ARCHETYPES")] == _OFFICIAL + ["Face", "Custom"]
    ctx.close()
