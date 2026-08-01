"""Headless-browser DOM suite for the SR2 Matrix run console (Playwright).

Where the state-layer harness (tests/test_matrix_visibility_*.py) proves the *data* the UI renders
from is correct, this suite proves the **rendered DOM** is correct: it loads the real
frontend/matrix-run.html in a headless browser, injects a real serialized run via ``showRunView()``,
and asserts what actually appears -- the Known IC pane, the paydata pane, the available actions --
as the PLAYER and as the ADMIN. That closes the last gap: whether the JS actually draws the right
buttons/cards/badges for a given state (and hides GM-only ones from the player).

Design: docs/matrix-e2e-visibility-harness.md (Phase 3). It reuses the headless engine to build
states (fast, no gameplay), then renders each ONCE per role -- so it stays quick even though a real
browser is involved (no clicking through a run to reach a state).

Skipped cleanly when Playwright or a system Chromium (Edge/Chrome) is unavailable, so CI / Docker
without a browser stays green. Locally: ``pip install pytest-playwright`` (the bundled-Chromium
download is not required -- this uses the system Edge/Chrome via ``channel=``).
"""

from __future__ import annotations

import functools
import http.server
import json
import os
import random
import socketserver
import threading

import pytest

import app.services.matrix_engine as eng
from app.routers import matrix_runs as mr
from app.schemas.matrix_run import RunActionInput
from tests import matrix_visibility_invariants as inv
from tests.test_matrix_visibility_fuzz import (
    _FakeDB, _HostNS, _StubRun, _call, _capable_decker, _random_host, _random_step,
)

try:
    from playwright.sync_api import sync_playwright
except Exception:  # noqa: BLE001 -- playwright optional
    sync_playwright = None

pytestmark = pytest.mark.skipif(sync_playwright is None, reason="playwright not installed")

# API path fragments the page hits on load -- all stubbed so bootstrapAuth completes and no real
# backend is needed. Everything else (html/js/css/fonts) is served from disk by the static server.
_API = ("/auth/", "/matrix-runs2", "/matrix-hosts", "/characters", "/runs", "/rtgs",
        "/organizations", "/locations", "/contacts")

# Uncaught JS errors captured per page (keyed by id) so a render that throws fails its test.
_ERRS: dict[int, list[str]] = {}


# =============================================================================
# Browser + static-server fixtures (session-scoped: one browser, two long-lived pages).
# =============================================================================
@pytest.fixture(scope="module")
def _frontend_port():
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory="frontend")
    # Silence the per-request logging to stderr.
    handler_cls = type("_QuietHandler", (handler.func,), {"log_message": lambda *a, **k: None})
    srv = socketserver.TCPServer(("127.0.0.1", 0), functools.partial(handler_cls, directory="frontend"))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    try:
        yield srv.server_address[1]
    finally:
        srv.shutdown()


@pytest.fixture(scope="module")
def _browser():
    with sync_playwright() as p:
        channel = None
        browser = None
        for candidate in ("msedge", "chrome"):
            try:
                browser = p.chromium.launch(channel=candidate, headless=True)
                channel = candidate
                break
            except Exception:  # noqa: BLE001 -- try the next system browser
                continue
        if browser is None:
            pytest.skip("no system Chromium (Edge/Chrome) available for Playwright")
        try:
            yield browser
        finally:
            browser.close()


def _make_page(browser, port, is_admin):
    ctx = browser.new_context()
    token_key = "sr_admin_token" if is_admin else "sr_user_token"
    ctx.add_init_script(f"localStorage.setItem('{token_key}', 'tok'); sessionStorage.clear();")
    page = ctx.new_page()
    _ERRS[id(page)] = []
    page.on("pageerror", lambda exc, _p=page: _ERRS[id(_p)].append(str(exc)))

    def handler(route):
        url = route.request.url
        if any(marker in url for marker in _API):
            if "/auth/verify" in url:
                route.fulfill(json={"is_admin": is_admin, "is_user": not is_admin,
                                    "is_default_password": False})
            else:
                route.fulfill(json=[])
        else:
            route.continue_()

    page.route("**/*", handler)
    page.goto(f"http://127.0.0.1:{port}/matrix-run.html")
    page.wait_for_function("typeof showRunView === 'function'", timeout=15000)
    return page


@pytest.fixture(scope="module")
def player_page(_browser, _frontend_port):
    """The run console loaded as a non-admin (bootstrapAuth injects `.gm-only { display:none }`)."""
    return _make_page(_browser, _frontend_port, is_admin=False)


@pytest.fixture(scope="module")
def admin_page(_browser, _frontend_port):
    return _make_page(_browser, _frontend_port, is_admin=True)


def _render(page, run):
    """Inject a serialized run and render the whole console from it (no gameplay). Returns the list
    of uncaught JS errors raised during the render (empty == clean)."""
    _ERRS[id(page)] = []
    page.evaluate("(r) => showRunView(r)", run)
    page.wait_for_timeout(120)
    return list(_ERRS[id(page)])


def _action_values(page):
    """Every value in the #actionType dropdown (including disabled / unaffordable options), or [] when
    the console shows no dropdown at all (pre-logon / icon crashed / run ended)."""
    if page.query_selector("#actionType") is None:
        return []
    return page.eval_on_selector_all("#actionType option", "els => els.map(e => e.value)")


def _ic_card_names(page):
    """The type-name text of every rendered Known-IC card (active + lurking), in DOM order."""
    return page.eval_on_selector_all(
        "#run-ic-list .ic-card .ic-type-name", "els => els.map(e => e.innerText.trim())")


# =============================================================================
# State builders -- reuse the headless engine to produce real serialized runs.
# =============================================================================
def _serialized(mutate, decker_mutate=None):
    """Build a run, apply ``mutate(state)`` (and optional ``decker_mutate(decker)``), and return
    (player_run, admin_run) as JSON-safe dicts. Saves/restores the global RNG so seeding here never
    perturbs the deterministic scenario tests."""
    _saved_rng = random.getstate()
    try:
        random.seed(1)
        mr.random.seed(1)
        eng.random.seed(1)
        cfg = {"security_code": "Orange", "security_value": 6, "acifs": [6, 6, 6, 6, 6], "sheaf": [],
               "paydata": [], "scrambles": [], "data_bombs": [], "slave_pieces": ["camera"]}
        host = _HostNS(cfg)
        decker = _capable_decker()
        if decker_mutate:
            decker_mutate(decker)
        state = mr._initial_state(decker, host)
        mutate(state)
        run = _StubRun(decker, state)
        player = json.loads(json.dumps(mr._serialize_run(run, inv.AUTH_PLAYER), default=str))
        admin = json.loads(json.dumps(mr._serialize_run(run, inv.AUTH_ADMIN), default=str))
        return player, admin
    finally:
        random.setstate(_saved_rng)


def _add_killer_ic(state):
    state["logon_complete"] = True
    mr._activate_sheaf_step(
        state, {"trigger": 0, "events": [{"type": "ic", "ic_type": "Killer", "rating": 6}]}, "Orange")


def _add_located_file(state, *, analyzed, encrypted, discovered=False):
    state["logon_complete"] = True
    state["paydata"] = [{"id": "pd0", "name": "Payroll DB", "density": 80, "is_key": True,
                         "located": True, "analyzed": analyzed}]
    if encrypted:
        sc = {"target_key": "files::file::Payroll DB", "rating": 5, "variant": "poison"}
        if discovered:
            sc["discovered"] = True
            sc["variant_revealed"] = True
        state["scrambles"] = [sc]


# =============================================================================
# DOM assertions -- the actual rendered console, per role.
# =============================================================================
def test_unidentified_ic_identity_is_redacted_in_the_dom(player_page, admin_page):
    """A Killer IC the decker has not identified renders as 'Unknown IC' in the player's Known IC
    pane (never 'Killer'), but the admin sees the real type -- redaction proven at the pixel level."""
    player, admin = _serialized(_add_killer_ic)

    _render(player_page, player)
    ic = player_page.inner_text("#run-ic-list")
    assert "Unknown IC" in ic, f"player Known IC pane did not render the IC: {ic!r}"
    assert "Killer" not in ic, f"player Known IC pane LEAKED the IC identity: {ic!r}"

    _render(admin_page, admin)
    ic_admin = admin_page.inner_text("#run-ic-list")
    assert "Killer" in ic_admin, f"admin Known IC pane did not reveal the identified type: {ic_admin!r}"


def test_analyzed_file_shows_size_and_offers_download(player_page):
    """An analyzed, non-encrypted located file shows its real size in the paydata pane and IS a
    Download target."""
    player, _ = _serialized(lambda s: _add_located_file(s, analyzed=True, encrypted=False))
    _render(player_page, player)

    downloads = player_page.inner_text("#run-downloads-body")
    assert "Payroll DB" in downloads, f"located file missing from paydata pane: {downloads!r}"
    assert "80 Mp" in downloads, f"analyzed file did not show its real size: {downloads!r}"

    actions = player_page.eval_on_selector_all("#actionType option", "els => els.map(e => e.value)")
    assert "download_data" in actions, f"Download not offered for a plain located file: {actions}"


def test_undiscovered_encrypted_file_looks_plain_and_offers_a_blind_download(player_page):
    """A file whose covering Scramble the decker has NOT discovered looks plain: its size stays
    hidden until analyzed, no ENCRYPTED badge, and Download IS offered -- the blind attempt is
    itself how the decker discovers the lock (and trips an Exploding Scramble's bomb)."""
    player, _ = _serialized(lambda s: _add_located_file(s, analyzed=False, encrypted=True, discovered=False))
    _render(player_page, player)

    downloads = player_page.inner_text("#run-downloads-body")
    assert "Payroll DB" in downloads, f"located file missing from files pane: {downloads!r}"
    assert "??? Mp" in downloads, f"unanalyzed file leaked its size: {downloads!r}"
    assert "ENCRYPTED" not in downloads, f"encryption leaked before it was discovered: {downloads!r}"

    actions = player_page.eval_on_selector_all("#actionType option", "els => els.map(e => e.value)")
    assert "download_data" in actions, f"blind Download not offered on an undiscovered-scramble file: {actions}"


def test_discovered_encrypted_file_shows_encrypted_and_offers_decrypt(player_page):
    """Once the covering Scramble is DISCOVERED, the file's card reads ENCRYPTED and offers Decrypt
    in place -- the encryption is now known, so a blind Download is off the action menu."""
    player, _ = _serialized(lambda s: _add_located_file(s, analyzed=True, encrypted=True, discovered=True))
    _render(player_page, player)

    downloads = player_page.inner_text("#run-downloads-body")
    assert "Payroll DB" in downloads, f"located file missing from files pane: {downloads!r}"
    assert "ENCRYPTED" in downloads, f"discovered encryption not shown on the file card: {downloads!r}"
    assert "Decrypt" in downloads, f"file card offers no Decrypt control: {downloads!r}"

    actions = player_page.eval_on_selector_all("#actionType option", "els => els.map(e => e.value)")
    assert "download_data" not in actions, f"blind Download wrongly offered for a known-encrypted file: {actions}"


def test_admin_sees_hidden_scramble_but_can_still_blind_download(admin_page):
    """Runner/admin 'sees more' -- a still-undiscovered Scramble shows a GM marker -- but keeps the
    SAME action set as the player: it can blind-download the file (which is how the lock is found)."""
    _, admin = _serialized(lambda s: _add_located_file(s, analyzed=False, encrypted=True, discovered=False))
    _render(admin_page, admin)
    files = admin_page.inner_text("#run-downloads-body")
    assert "GM: SCRAMBLED" in files, f"admin GM scramble marker missing: {files!r}"
    assert ">> DOWNLOAD" in files, f"admin cannot blind-download a still-locked file: {files!r}"
    assert ">> DECRYPT" not in files, f"admin jumped to Decrypt instead of a blind Download: {files!r}"


def test_decrypt_prompt_caps_hacking_pool_at_the_remaining_pool(player_page):
    """The Decrypt hacking-pool prompt is capped at the remaining Hacking Pool, like the rest of the
    app (the shared prompt input carries the max)."""
    def mut(s):
        s["logon_complete"] = True
        s["hackingPool_remaining"] = 3
        s["paydata"] = [{"id": "pd0", "name": "Ledger", "density": 40, "located": True, "analyzed": True}]
        s["scrambles"] = [{"target_key": "files::file::Ledger", "rating": 6, "variant": "poison",
                           "discovered": True, "variant_revealed": True}]
    player, _ = _serialized(mut)
    _render(player_page, player)
    cap = player_page.evaluate("""() => {
        const f = (_run.state_json.located_paydata || []).find(p => p.scramble_ref);
        if (!f) return 'no-scramble-file';
        decryptScramble(f.scramble_ref);
        const input = document.getElementById('_sharedPromptInput');
        return input ? input.getAttribute('max') : 'no-input';
    }""")
    assert cap == "3", f"Decrypt prompt not capped at the remaining Hacking Pool: max={cap!r}"


def test_crashed_icon_offers_only_jack_out(player_page):
    """When Black IC has crashed the icon, the action console collapses to a single Jack Out control
    -- no action dropdown, no Perform button (vr2 L612)."""
    def mut(state):
        state["logon_complete"] = True
        state["icon_crashed"] = True
    player, _ = _serialized(mut)
    _render(player_page, player)

    action_area = player_page.inner_text("#action-area")
    assert "jack out" in action_area.lower(), f"crashed icon did not offer Jack Out: {action_area!r}"
    assert player_page.query_selector("#actionType") is None, "action dropdown shown while icon crashed"
    assert player_page.query_selector("#actPerformBtn") is None, "Perform button shown while icon crashed"


# =============================================================================
# Per-action availability oracle -- the "exercise every action type" layer. For each action in the
# catalog we build a PLAYER state that SHOULD offer it (game precondition met) and, for gated
# actions, one that should NOT (precondition violated), then assert the rendered #actionType dropdown
# agrees. The precondition is asserted HERE (independently of the catalog's own valid() predicate),
# so a predicate that offers/hides an action in the wrong state is caught -- this is the "actions
# available are correct" check, and running one state per action exercises every action branch.
# =============================================================================
def _logged_on(state):
    """Bare post-logon state: the console renders its full dropdown and no game-state precondition is
    met, so only the always-available actions appear."""
    state["logon_complete"] = True


def _ic(ic_type, **extra):
    """A fully-IDENTIFIED active IC (detection_level 3) so it survives player redaction with its real
    type -- the availability predicates key off ic.type, and an unidentified ('Unknown IC') copy would
    wrongly hide every type-specific action (Slow / Disinfect / Steamroller / Relocate)."""
    ic = {"id": extra.pop("id", "ic1"), "type": ic_type, "rating": 6, "status": "active",
          "detection_level": 3, "category": "proactive", "boxes": 0}
    ic.update(extra)
    return ic


def _b_located(state):
    _add_located_file(state, analyzed=True, encrypted=False)


def _b_located_unanalyzed(state):
    _add_located_file(state, analyzed=False, encrypted=False)


def _b_worm(state):
    # A worm displays to the player only when its variant is known (a variant-less worm redacts to
    # 'Unknown IC'); 'Deathworm' still matches the /worm/i gate on Disinfect.
    _logged_on(state)
    state["active_ic"] = [_ic("Worm", variant="deathworm")]


def _b_tar(state):
    _logged_on(state)
    state["active_ic"] = [_ic("Tar Baby")]


def _b_proactive_ic(state):
    # A Killer is proactive + identified: eligible for Slow and a valid combat-maneuver target.
    _logged_on(state)
    state["active_ic"] = [_ic("Killer")]


def _b_trace_locate(state):
    _logged_on(state)
    state["active_ic"] = [_ic("Trace", trace_phase="locate", trace_locate_remaining=2)]


def _b_persona_hurt(state):
    _logged_on(state)
    state.setdefault("condition_monitor", {})["persona_boxes"] = 3


def _b_attr_hurt(state):
    _logged_on(state)
    state.setdefault("condition_monitor", {})["persona_damage"] = {"bod": 1}


def _b_legitimate(state):
    _logged_on(state)
    state["has_legitimate_status"] = True


def _b_redirected(state):
    _logged_on(state)
    state["redirects_placed"] = 1


def _b_hog(state):
    _logged_on(state)
    state["hog_infections"] = [{"id": "h1", "rating": 4, "target_id": "pc"}]


def _b_squeezed_program(state):
    _logged_on(state)
    state["squeezed_active"] = [{"name": "attack", "rating": 6, "size": 6}]


def _dinab_decker(decker):
    # DINAB is gated on the loadout carrying a DINAB rating for a loaded program (attack is loaded).
    decker["program_options"] = {"attack": {"dinab": 4}}


# (action, present_state_build, present_decker_build, absent_state_build). A None present-decker means
# the default capable decker; a None absent-build means the action is always available (offered in any
# bare post-logon state, so there is no state that legitimately hides it).
_ACTION_CASES = [
    # -- Always available (no game-state gate): offered in a bare post-logon state --
    ("analyze_host",      _logged_on, None, None),
    ("analyze_security",  _logged_on, None, None),
    ("analyze_subsystem", _logged_on, None, None),
    ("locate_paydata",    _logged_on, None, None),
    ("locate_file",       _logged_on, None, None),
    ("locate_ic",         _logged_on, None, None),
    ("locate_decker",     _logged_on, None, None),
    ("crash_host",        _logged_on, None, None),
    ("null_operation",    _logged_on, None, None),
    ("decoy",             _logged_on, None, None),
    ("invalidate_passcode", _logged_on, None, None),
    ("unload_program",    _logged_on, None, None),
    # -- Gated: present when the precondition holds, hidden when it does not --
    ("download_data",     _b_located,            None, _logged_on),
    ("edit_file",         _b_located,            None, _logged_on),
    ("analyze_icon",      _b_located_unanalyzed, None, _b_located),
    ("disinfect",         _b_worm,               None, _logged_on),
    ("steamroller",       _b_tar,                None, _logged_on),
    ("slow",              _b_proactive_ic,       None, _logged_on),
    ("relocate",          _b_trace_locate,       None, _logged_on),
    ("evade_detection",   _b_proactive_ic,       None, _logged_on),
    ("parry_attack",      _b_proactive_ic,       None, _logged_on),
    ("position_attack",   _b_proactive_ic,       None, _logged_on),
    ("medic",             _b_persona_hurt,       None, _logged_on),
    ("restore",           _b_attr_hurt,          None, _logged_on),
    ("validate_passcode", _logged_on,            None, _b_legitimate),
    ("redirect_datatrail", _logged_on,           None, _b_redirected),
    ("purge_hog",         _b_hog,                None, _logged_on),
    ("decompress_file",   _b_squeezed_program,   None, _logged_on),
    ("swap_memory",       _logged_on,            None, None),
    ("dinab",             _logged_on,            _dinab_decker, _logged_on),
]


@pytest.mark.parametrize("action,present_build,present_decker,absent_build", _ACTION_CASES,
                         ids=[c[0] for c in _ACTION_CASES])
def test_action_availability_matches_game_state(player_page, action, present_build, present_decker,
                                                absent_build):
    """Each action must be OFFERED exactly when its game-state precondition is met, and HIDDEN when it
    is not -- proven against the real rendered dropdown, as the player sees it."""
    player, _ = _serialized(present_build, present_decker)
    _render(player_page, player)
    assert action in _action_values(player_page), (
        f"{action} should be OFFERED when its precondition is met (dropdown: "
        f"{sorted(set(_action_values(player_page)))})")

    if absent_build is not None:
        player, _ = _serialized(absent_build)
        _render(player_page, player)
        assert action not in _action_values(player_page), (
            f"{action} should be HIDDEN when its precondition is not met")


# =============================================================================
# Federated Bank playtest regressions -- BEHAVIORAL. Each reproduces a bug found in live play and
# asserts the FIXED behavior in the REAL rendered DOM, so reintroducing the bug fails the exact test.
# (Always-on static backups that also run without a browser live in tests/test_matrix_visibility_e2e.py.)
# =============================================================================
def test_fedbank_program_tooltips_are_in_app_with_descriptions(player_page):
    """Bug: program tooltips used the OS `title` and showed only a size, not a description. The in-app
    tooltip builders must carry the real program DESCRIPTION (Defuse -> disarms data bombs) in a
    data-tip, never a native title."""
    info = player_page.evaluate("""() => ({
        desc: (MatrixPrograms.get('defuse') || {}).description || '',
        pt: progTip('defuse', 24),
        chip: progChip('defuse', 6, 24, 0),
        lao: laoCardTip('Defuse-6', 'defuse', 24, 'Drag onto Active or Storage.'),
    })""")
    assert "data bomb" in info["desc"].lower(), f"defuse has no real description: {info['desc']!r}"
    assert "data bomb" in info["pt"].lower(), f"progTip dropped the description: {info['pt']!r}"
    assert "Mp" in info["pt"], f"progTip dropped the size: {info['pt']!r}"
    assert "data-tip=" in info["chip"] and "title=" not in info["chip"], (
        f"program chip is not an in-app data-tip tooltip: {info['chip']!r}")
    assert "data bomb" in info["lao"].lower(), f"loadout card tip dropped the description: {info['lao']!r}"


def test_fedbank_admin_sees_and_can_analyze_located_files(admin_page):
    """Bug: a file the player located did NOT appear in the admin view, and the admin could not run
    Analyze Icon on it. The admin must see the file and be offered Analyze Icon."""
    _, admin = _serialized(lambda s: _add_located_file(s, analyzed=False, encrypted=False))
    _render(admin_page, admin)
    body = admin_page.inner_text("#run-downloads-body")
    assert "Payroll DB" in body, f"admin cannot see the player-located file: {body!r}"
    assert "analyze_icon" in _action_values(admin_page), (
        "admin is not offered Analyze Icon for a located file")


def test_fedbank_invalidate_offers_entire_system_with_no_ic(player_page):
    """Bug: Invalidate Passcode could target the whole system ONLY when Active IC was visible, and the
    dropdown listed only the IC. It must always offer 'Entire system passcode table' -- it flips every
    icon on the host, active or not."""
    player, _ = _serialized(_logged_on)   # logged on, NO active IC
    _render(player_page, player)
    opts = player_page.evaluate("""() => {
        const sel = document.getElementById('actionType');
        sel.value = 'invalidate_passcode';
        onActionTypeChange();
        const t = document.getElementById('actionTargetSelect');
        return t ? Array.prototype.slice.call(t.querySelectorAll('option')).map(o => ({ v: o.value, l: o.innerText })) : [];
    }""")
    vals = [o["v"] for o in opts]
    assert "__all__" in vals, f"Invalidate has no whole-system option with no IC present: {opts}"
    label = next(o["l"] for o in opts if o["v"] == "__all__")
    assert "entire system" in label.lower(), f"whole-system option mislabeled: {label!r}"


def test_fedbank_discovered_file_scramble_rides_its_file_card(player_page):
    """A per-file Scramble the decker has discovered rides its file's card in the Files pane (with a
    Decrypt control) -- NOT the IC pane. All file actions live in one place."""
    def mut(s):
        s["logon_complete"] = True
        s["paydata"] = [{"id": "pd0", "name": "Ledger", "density": 40, "located": True, "analyzed": True}]
        s["scrambles"] = [{"target_key": "files::file::Ledger", "rating": 6, "variant": "poison",
                           "discovered": True, "variant_revealed": True}]
    player, _ = _serialized(mut)
    _render(player_page, player)
    files = player_page.inner_text("#run-downloads-body")
    assert "ENCRYPTED" in files, f"discovered file scramble not shown on its file card: {files!r}"
    assert "Decrypt" in files, f"file card offers no Decrypt control: {files!r}"
    # ...and the per-file scramble is NOT duplicated in the Known IC pane.
    ic = player_page.inner_text("#run-ic-list")
    assert "Decrypt" not in ic, f"per-file scramble leaked into the IC pane: {ic!r}"


def test_fedbank_analyzed_file_removed_from_analyze_targets(player_page):
    """Bug: an already-analyzed file stayed in the Analyze Icon target list -- a wasted action. Once
    analyzed, a file must drop out of the target dropdown; unanalyzed files remain."""
    def mut(s):
        s["logon_complete"] = True
        s["paydata"] = [
            {"id": "pd0", "name": "FreshFile", "density": 40, "located": True, "analyzed": False},
            {"id": "pd1", "name": "ScannedFile", "density": 40, "located": True, "analyzed": True},
        ]
    player, _ = _serialized(mut)
    _render(player_page, player)
    opts = player_page.evaluate("""() => {
        const sel = document.getElementById('actionType');
        sel.value = 'analyze_icon';
        onActionTypeChange();
        const t = document.getElementById('actionTargetSelect');
        return t ? Array.prototype.slice.call(t.querySelectorAll('option')).map(o => o.innerText) : [];
    }""")
    joined = " | ".join(opts)
    assert "FreshFile" in joined, f"unanalyzed file missing from Analyze Icon targets: {opts}"
    assert "ScannedFile" not in joined, (
        f"already-analyzed file still offered as an Analyze Icon target: {opts}")


def test_fedbank_event_log_autoscrolls_to_newest(player_page):
    """Bug: the running log did not scroll as new entries arrived. When events stream in and the feed
    overflows, it must pin to the newest line (scrollTop at the bottom)."""
    def mut(s):
        s["logon_complete"] = True
        s["event_log"] = [{"type": "system", "description": f"boot {i}"} for i in range(3)]
    player, _ = _serialized(mut)
    _render(player_page, player)
    metrics = player_page.evaluate("""() => {
        const f = document.getElementById('mr-stream-feed');
        f.style.height = '80px'; f.style.overflowY = 'auto';   // force a bounded, scrollable feed
        const many = [];
        for (let i = 0; i < 60; i++) many.push({ type: 'system', description: 'log line ' + i });
        _run.state_json.event_log = many;
        renderStage(_run.state_json, _run.decker_json);        // streams new events + auto-scrolls
        return { top: f.scrollTop, ch: f.clientHeight, sh: f.scrollHeight };
    }""")
    assert metrics["sh"] > metrics["ch"], f"feed did not overflow, cannot test auto-scroll: {metrics}"
    assert metrics["top"] + metrics["ch"] >= metrics["sh"] - 4, (
        f"event log did not auto-scroll to the newest entry: {metrics}")


# =============================================================================
# MANY-HOST render sweep -- the breadth layer. Drive several random hosts a few steps each, capture
# the player-serialized state at every step, and assert the rendered console never throws a JS error
# and never shows a visible GM-only element. This exercises the render across a wide spread of
# engine-produced states (the "multitude of hosts" requirement), catching render crashes for any
# state the engine can reach.
# =============================================================================
def _capture_states(n_hosts=int(os.environ.get("MATRIX_DOM_HOSTS", "8")),
                    steps=int(os.environ.get("MATRIX_DOM_STEPS", "7"))):
    """Drive random hosts through logon + a random script, capturing (label, player_run, admin_run)
    per step -- BOTH serializations of the same engine state, so admin-vs-player parity can be proven
    at the DOM. The breadth (host count x steps) is env-tunable (MATRIX_DOM_HOSTS / MATRIX_DOM_STEPS)
    for a deeper local sweep without slowing the default CI run."""
    out: list[tuple[str, dict, dict]] = []
    if sync_playwright is None:
        return out
    # Save/restore the GLOBAL RNG + the patched run lookups: this runs at import (collection), so it
    # must leave the process exactly as it found it or it perturbs the deterministic scenario tests.
    _saved_rng = random.getstate()
    saved = (mr._get_run_or_404, mr._get_host_or_404, mr._assert_run_access)
    try:
        for h in range(n_hosts):
            random.seed(2000 + h)
            mr.random.seed(2000 + h)
            eng.random.seed(2000 + h)
            rng = random.Random(7000 + h)
            decker = _capable_decker()
            host = _random_host(rng)
            state = mr._initial_state(decker, host)
            run = _StubRun(decker, state)

            async def _gr(db, run_id, _r=run):
                return _r

            async def _gh(db, host_id, _h=host):
                return _h

            mr._get_run_or_404 = _gr
            mr._get_host_or_404 = _gh
            mr._assert_run_access = lambda r, a: None
            _call(mr.perform_action(run_id=1, body=RunActionInput(
                action_type="logon_to_host", subsystem="access", utility_rating=6, hacking_pool_dice=2),
                auth=inv.AUTH_ADMIN, db=_FakeDB()))
            for i in range(steps):
                if run.status != "active" or run.state_json.get("run_ended"):
                    break
                _random_step(rng, run)
                out.append((f"host{h}-step{i}",
                            json.loads(json.dumps(mr._serialize_run(run, inv.AUTH_PLAYER), default=str)),
                            json.loads(json.dumps(mr._serialize_run(run, inv.AUTH_ADMIN), default=str))))
    finally:
        mr._get_run_or_404, mr._get_host_or_404, mr._assert_run_access = saved
        random.setstate(_saved_rng)
    return out


_RAW_CORPUS = _capture_states()
# Player-only view (unchanged shape for the existing corpus tests) + an admin lookup by label, so the
# admin-superset test can render the SAME state from both roles.
_CORPUS = [(label, player_run) for label, player_run, _admin in _RAW_CORPUS]
_CORPUS_ADMIN = {label: admin_run for label, _player, admin_run in _RAW_CORPUS}


@pytest.mark.skipif(not _CORPUS, reason="no captured states (playwright unavailable)")
@pytest.mark.parametrize("label,player_run", _CORPUS, ids=[c[0] for c in _CORPUS])
def test_player_dom_never_leaks_or_crashes(player_page, label, player_run):
    """Across many random-host states, the player console must render WITHOUT a JS error and show NO
    visible .gm-only element (the client-side GM redaction). A render crash or a visible GM-only node
    fails the exact state -- so every engine-reachable state is proven to render safely for a player."""
    errors = _render(player_page, player_run)
    assert not errors, f"[{label}] render raised JS error(s): {errors[:2]}"
    visible_gm = player_page.eval_on_selector_all(
        ".gm-only", "els => els.filter(e => e.offsetParent !== null).length")
    assert visible_gm == 0, f"[{label}] {visible_gm} GM-only element(s) visible to the player"


# =============================================================================
# CONSISTENCY layer -- for every captured state, the rendered #actionType dropdown must contain
# EXACTLY the actions the catalog marks valid for that state (nothing dropped by the optgroup
# grouping, nothing invalid leaking), each option disabled iff unaffordable, and no duplicates. This
# ties the visible control set to the declared game-state validity across the whole corpus.
# =============================================================================
_CONSISTENCY_JS = """
() => {
  if (typeof ACTION_CATALOG === 'undefined' || typeof _run === 'undefined' || !_run) {
    return { noDropdown: true };
  }
  const sel = document.getElementById('actionType');
  if (!sel) return { noDropdown: true };
  const s = _run.state_json || {};
  const expected = ACTION_CATALOG.filter(function (a) { return !a.valid || a.valid(s); })
    .map(function (a) { return a.v; });
  const opts = Array.prototype.slice.call(sel.querySelectorAll('option')).map(function (o) {
    const meta = _ACTION_BY_V[o.value] || {};
    return {
      v: o.value,
      disabled: !!o.disabled,
      afford: (typeof _canAffordCost === 'function') ? !!_canAffordCost(s, meta.cost) : true
    };
  });
  return { expected: expected, rendered: opts.map(function (o) { return o.v; }), opts: opts };
}
"""


@pytest.mark.skipif(not _CORPUS, reason="no captured states (playwright unavailable)")
@pytest.mark.parametrize("label,player_run", _CORPUS, ids=[c[0] for c in _CORPUS])
def test_action_dropdown_is_consistent_with_catalog(player_page, label, player_run):
    """The rendered action dropdown must equal the catalog's valid-action set for the state, each
    option disabled iff unaffordable, with no duplicates. A missing dropdown is allowed only when the
    console is genuinely action-locked (pre-logon / icon crashed / run ended)."""
    _render(player_page, player_run)
    data = player_page.evaluate(_CONSISTENCY_JS)
    st = player_run.get("state_json", {})
    if data.get("noDropdown"):
        assert st.get("run_ended") or st.get("icon_crashed") or not st.get("logon_complete"), (
            f"[{label}] action dropdown missing but the run is live and actionable")
        return
    exp, ren = set(data["expected"]), set(data["rendered"])
    assert exp == ren, f"[{label}] dropdown != catalog validity: missing {exp - ren}, extra {ren - exp}"
    assert len(data["rendered"]) == len(ren), f"[{label}] duplicate options: {data['rendered']}"
    for o in data["opts"]:
        assert o["disabled"] == (not o["afford"]), (
            f"[{label}] option {o['v']}: disabled={o['disabled']} but affordable={o['afford']}")


# =============================================================================
# PANE-CORRECTNESS layer -- for every captured state, the Known IC pane and the paydata panel must
# mirror exactly what the (redacted) player state carries: one IC card per visible IC, no invented or
# leaked identity, and the paydata panel shown iff there is paydata to show.
# =============================================================================
@pytest.mark.skipif(not _CORPUS, reason="no captured states (playwright unavailable)")
@pytest.mark.parametrize("label,player_run", _CORPUS, ids=[c[0] for c in _CORPUS])
def test_panes_reflect_state(player_page, label, player_run):
    """Known IC pane: one card per visible (non-suppressed) active IC plus each revealed lurking IC,
    every card's identity backed by the state (no leak). Paydata panel: visible iff there is content."""
    _render(player_page, player_run)
    st = player_run.get("state_json", {})

    active = [ic for ic in (st.get("active_ic") or [])
              if not (ic.get("suppressed") and not ic.get("suppression_released"))]
    lurking = list(st.get("lurking_ic") or []) + list(st.get("revealed_lurking_ic") or [])
    expected_types = ([str(ic.get("type") or "") for ic in active]
                      + [str(ic.get("type") or "") for ic in lurking])

    cards = player_page.eval_on_selector_all(
        "#run-ic-list .ic-card .ic-type-name", "els => els.map(e => e.innerText.trim())")
    assert len(cards) == len(expected_types), (
        f"[{label}] Known IC pane rendered {len(cards)} card(s), state has {len(expected_types)}")
    for name in cards:
        assert any(name.startswith(t) for t in expected_types if t), (
            f"[{label}] IC card '{name}' matches no state IC {expected_types}")
    if expected_types:
        assert "No security identified" not in player_page.inner_text("#run-ic-list"), (
            f"[{label}] Known IC pane shows the empty message despite {len(expected_types)} IC")

    has_pay = bool(st.get("located_paydata") or st.get("downloaded_files")
                   or st.get("active_download") or st.get("paydata_secured"))
    panel_visible = bool(player_page.eval_on_selector(
        "#run-downloads-panel", "el => el && el.offsetParent !== null"))
    assert panel_visible == has_pay, (
        f"[{label}] paydata panel visible={panel_visible} but has_content={has_pay}")


# =============================================================================
# ADMIN-SUPERSET layer -- the admin is a strict superset of the player: everything the player can see
# or do, the admin can too (plus more). This is the DOM proof of the located-files regression (players
# located files the admin could neither see nor act on): render the SAME engine state as both roles
# and assert the admin console never offers FEWER actions, shows FEWER IC, or hides a file the player
# has found. The admin legitimately shows MORE (lurking IC, unredacted identities) -- never fewer.
# =============================================================================
@pytest.mark.skipif(not _CORPUS, reason="no captured states (playwright unavailable)")
@pytest.mark.parametrize("label,player_run", _CORPUS, ids=[c[0] for c in _CORPUS])
def test_admin_dom_is_a_superset_of_player(player_page, admin_page, label, player_run):
    """For the same run, the admin DOM must be a superset of the player DOM: player actions subset of
    admin actions, every player-located file visible in the admin paydata pane, and admin IC card
    count >= player IC card count."""
    admin_run = _CORPUS_ADMIN[label]
    _render(player_page, player_run)
    _render(admin_page, admin_run)

    # 1) Available actions: the player can never do something the admin cannot.
    p_actions, a_actions = set(_action_values(player_page)), set(_action_values(admin_page))
    assert p_actions <= a_actions, (
        f"[{label}] player is offered actions the admin is not (admin must be a superset): "
        f"{sorted(p_actions - a_actions)}")

    # 2) Located files: every file the player has found must be visible in the admin's paydata pane
    #    (the exact 'players located files, admin could not see them' regression, at the DOM).
    p_files = [str(p.get("name")) for p in (player_run.get("state_json", {}).get("located_paydata") or [])
               if isinstance(p, dict) and p.get("name")]
    if p_files:
        admin_body = (admin_page.inner_text("#run-downloads-body")
                      if admin_page.query_selector("#run-downloads-body") else "")
        for name in p_files:
            assert name in admin_body, (
                f"[{label}] admin paydata pane does not show player-located file {name!r}")

    # 3) Known IC: the admin sees at least as many IC as the player (usually more -- lurking IC).
    assert len(_ic_card_names(admin_page)) >= len(_ic_card_names(player_page)), (
        f"[{label}] admin Known IC pane shows fewer cards than the player's")


# =============================================================================
# COVERAGE guard -- the per-action table must cover EVERY action the catalog can offer, so a newly
# added action cannot ship without an availability test (enforces "exercise every action type").
# =============================================================================
def test_every_catalog_action_has_an_availability_case(player_page):
    """_ACTION_CASES must name exactly the catalog's action set -- nothing missing, nothing stale."""
    catalog = set(player_page.evaluate("() => ACTION_CATALOG.map(a => a.v)"))
    tested = {c[0] for c in _ACTION_CASES}
    missing = catalog - tested
    assert not missing, f"catalog actions with no availability case: {sorted(missing)}"
    stale = tested - catalog
    assert not stale, f"_ACTION_CASES references non-catalog actions: {sorted(stale)}"


# =============================================================================
# BRANCH-COVERAGE layer -- the "every branch" proof. Using Chromium V8 precise (block-level) coverage
# via CDP, drive the whole random corpus (both roles) + every action-availability state + a set of
# render-branch variant states (crashed / party / construct / trap IC, enemy deckers, active download,
# crash countdown, decoy, terminated run, ...) + every catalog target-builder closure, then report the
# fraction of matrix-run.html blocks executed and the functions never entered. Random-seeded hosts
# supply the breadth; the variant states + target sweep close the branches randomness rarely hits.
# =============================================================================
def _cv_unidentified_ic(state):
    state["logon_complete"] = True
    state["active_ic"] = [_ic("Killer", id="u1", detection_level=1, category=None, rating=None)]


def _cv_crashed_ic(state):
    state["logon_complete"] = True
    state["active_ic"] = [_ic("Killer", id="c1", status="crashed", boxes=10)]


def _cv_party_cluster(state):
    state["logon_complete"] = True
    state["active_ic"] = [_ic("Killer", id="p1", cluster_id="cl1"),
                          _ic("Acid", id="p2", cluster_id="cl1")]


def _cv_construct_ic(state):
    state["logon_complete"] = True
    state["active_ic"] = [_ic("Construct", id="k1",
                              construct_components=[{"type": "Killer", "rating": 5},
                                                    {"type": "Tar Baby", "rating": 4}])]


def _cv_option_ic(state):
    state["logon_complete"] = True
    state["active_ic"] = [_ic("Killer", id="o1", expert={"type": "offense", "value": 2},
                              shield=True, shift=True, cascading=True, options=["Armor"])]


def _cv_suppressed_ic(state):
    state["logon_complete"] = True
    state["active_ic"] = [_ic("Killer", id="s1", status="crashed", suppressed=True, boxes=10)]


def _cv_enemy_decker(state):
    state["logon_complete"] = True
    state["enemy_deckers"] = [{"id": "ed1", "name": "Ghost", "status": "active", "revealed": True,
                               "boxes": 0, "intruding": False}]


def _cv_active_download(state):
    state["logon_complete"] = True
    _add_located_file(state, analyzed=True, encrypted=False)
    state["active_download"] = {"file": "Payroll DB", "turns_left": 2, "turns_total": 4,
                                "compressed": True}


def _cv_crash_countdown(state):
    state["logon_complete"] = True
    state["crash_host_countdown"] = {"turns_remaining": 3}


def _cv_decoy_legit(state):
    state["logon_complete"] = True
    state["has_legitimate_status"] = True
    state["decoy_successes"] = 2
    state["decoy_hp"] = 8


def _cv_security_known(state):
    state["logon_complete"] = True
    state["security_known"] = {"tally": 4, "alert": "passive", "turn": 2}
    state["host_ratings_revealed"] = {"access": 5, "control": 4, "index": 6, "files": 7, "slave": 3}


def _cv_terminated(state):
    state["logon_complete"] = True
    state["run_ended"] = True
    state["end_reason"] = "jacked_out"


def _cv_prelogon(state):
    pass  # the bare initial state -- exercises the pre-logon action area + blank host panel


def _cv_kitchen_sink(state):
    """A single state that makes the widest set of actions available at once, so selecting each option
    exercises its target(state) closure in the catalog (Download / Edit / Disinfect / Steamroller /
    Slow / Relocate / Analyze Icon / Purge Hog / Decompress / Invalidate / maneuvers / ...)."""
    _add_located_file(state, analyzed=False, encrypted=False)
    state["active_ic"] = [
        _ic("Killer", id="k1"),
        _ic("Tar Baby", id="t1"),
        _ic("Worm", id="w1", variant="deathworm"),
        _ic("Trace", id="tr1", trace_phase="locate", trace_locate_remaining=2),
    ]
    state["enemy_deckers"] = [{"id": "ed1", "name": "Ghost", "status": "active", "revealed": True,
                               "boxes": 0, "intruding": False}]
    state["hog_infections"] = [{"id": "h1", "rating": 4, "target_id": "pc"}]
    state["downloaded_files"] = [{"name": "loot", "compressed": True}]
    state["squeezed_active"] = [{"name": "attack", "rating": 6, "size": 6}]
    state["condition_monitor"] = {"persona_boxes": 3, "persona_damage": {"bod": 1}}
    # A discovered Scramble + Data Bomb on the located file so the Decrypt / Crash / Defuse card
    # handlers have real refs to fire against (their branches, and the defense-card render, execute).
    state["scrambles"] = [{"target_key": "files::file::Payroll DB", "rating": 6, "variant": "poison",
                          "discovered": True, "variant_revealed": True}]
    state["data_bombs"] = [{"target": "files::file::Payroll DB", "rating": 5, "discovered": True}]


_COVERAGE_VARIANTS = [
    _cv_unidentified_ic, _cv_crashed_ic, _cv_party_cluster, _cv_construct_ic, _cv_option_ic,
    _cv_suppressed_ic, _cv_enemy_decker, _cv_active_download, _cv_crash_countdown, _cv_decoy_legit,
    _cv_security_known, _cv_terminated, _cv_prelogon,
]


def _raw_run(state):
    """A run dict fed straight to showRunView, bypassing the serializer -- lets the coverage sweep hit
    exact render branches (file lifecycle, active alert, mixed IC board) without redaction filtering
    fields out. Correctness of redaction is proven elsewhere; here we only want the code paths run."""
    st = dict(state)
    st.setdefault("logon_complete", True)
    return {"id": 1, "status": "active", "decker_json": _capable_decker(), "state_json": st}


# Hand-crafted states for render branches the random corpus rarely produces all at once.
_COVERAGE_RAW_STATES = [
    {   # paydata lifecycle: located / downloaded / destroyed / tampered + secured + storage meter
        "located_paydata": [
            {"id": "d1", "name": "f-down", "size_mp": 40, "analyzed": True, "downloaded": True, "is_key": False},
            {"id": "d2", "name": "f-dead", "size_mp": 40, "analyzed": True, "destroyed": True, "is_key": False},
            {"id": "d3", "name": "f-mod", "size_mp": 40, "analyzed": True, "tampered": True, "is_key": True},
        ],
        "downloaded_files": [{"name": "f-down", "compressed": False, "size_mp": 40}],
        "storage_used_mp": 40, "storage_free_mp": 600,
        "paydata_secured": {"count": 1, "total_mp": 40},
    },
    {   # active alert + heavy damage + suppression + bandwidth mod (status/deck-stat branches)
        "security_known": {"tally": 8, "alert": "active", "turn": 3},
        "host_security_code": "Red", "host_security_value": 9, "host_security_revealed": True,
        "condition_monitor": {"persona_boxes": 6, "stun_boxes": 3, "physical_boxes": 2,
                              "mpcp_damage": 2, "persona_damage": {"masking": 1, "sensor": 1}},
        "suppression_count": 2, "bandwidth_modifier": 3,
        "host_ratings_revealed": {"access": 5, "control": 4, "index": 6, "files": 7, "slave": 3},
    },
    {   # mixed IC board: party cluster + construct + trap + lurking + decoy + legitimate badge
        "active_ic": [
            {"id": "p1", "type": "Killer", "rating": 6, "status": "active", "detection_level": 3,
             "category": "proactive", "cluster_id": "cl1", "boxes": 2},
            {"id": "p2", "type": "Acid", "rating": 5, "status": "active", "detection_level": 3,
             "category": "proactive", "cluster_id": "cl1", "boxes": 0},
            {"id": "cst", "type": "Construct", "rating": 6, "status": "active", "detection_level": 3,
             "category": "proactive", "construct_components": [{"type": "Killer", "rating": 5}]},
            {"id": "tp", "type": "Probe", "rating": 4, "status": "active", "detection_level": 3,
             "category": "reactive", "trap_hidden": True},
        ],
        "revealed_lurking_ic": [{"id": "lk", "type": "Tar Baby", "rating": 5, "detection_level": 2}],
        "has_legitimate_status": True, "decoy_successes": 2, "decoy_hp": 8,
    },
]


def _safe_render(page, run):
    """Drive one render for coverage, swallowing a JS throw so one bad state cannot abort collection
    (render CORRECTNESS is proven by the other tests; here we only want the code paths executed)."""
    try:
        page.evaluate("(r) => showRunView(r)", run)
    except Exception:  # noqa: BLE001 -- coverage drive must be resilient
        pass


def _drive_for_coverage(page):
    for _label, player_run, admin_run in _RAW_CORPUS:
        _safe_render(page, player_run)
        _safe_render(page, admin_run)
    for _action, present_build, present_decker, absent_build in _ACTION_CASES:
        player, admin = _serialized(present_build, present_decker)
        _safe_render(page, player)
        _safe_render(page, admin)
        if absent_build is not None:
            player, _admin = _serialized(absent_build)
            _safe_render(page, player)
    for mut in _COVERAGE_VARIANTS:
        player, admin = _serialized(mut)
        _safe_render(page, player)
        _safe_render(page, admin)
    for raw_state in _COVERAGE_RAW_STATES:
        _safe_render(page, _raw_run(raw_state))
    # DINAB needs a loadout that carries a DINAB rating -- render it so that branch is exercised too.
    player, _admin = _serialized(_logged_on, _dinab_decker)
    _safe_render(page, player)
    # -- "Exercise the whole program" pass: on a rich state, run every action's target(state) closure,
    #    fire the interaction handlers (modals + per-card actions), then submit performAction for every
    #    action so the request-building branches execute too -- not just the render paths. Everything
    #    is wrapped + modals dismissed; a handler that opens a modal or hits the stubbed API must not
    #    abort collection.
    rich_player, _admin = _serialized(_cv_kitchen_sink)
    _safe_render(page, rich_player)
    # (A) every catalog target(state) closure -- select each offered action (does not replace _run).
    page.evaluate("""() => {
        const sel = document.getElementById('actionType');
        if (!sel) return;
        const vals = Array.prototype.slice.call(sel.querySelectorAll('option')).map(o => o.value);
        for (const v of vals) { sel.value = v; try { onActionTypeChange(); } catch (e) {} }
    }""")
    # (B) the per-card / modal interaction handlers, against the intact _run.
    page.evaluate("""() => {
        const dismiss = () => {
            try { document.querySelectorAll('.open').forEach(m => m.classList.remove('open')); } catch (e) {}
            try { document.querySelectorAll('.mr-prompt').forEach(m => m.remove()); } catch (e) {}
        };
        const st = (_run && _run.state_json) || {};
        const scr = (st.discovered_scrambles || [])[0] || {};
        const bomb = (st.discovered_data_bombs || [])[0] || {};
        const calls = [
            () => openLogoffModal(), () => window.closeLogoffModal && closeLogoffModal(),
            () => openAttackModal('k1', 'Killer', 6), () => window.closeAttackModal && closeAttackModal(),
            () => analyzeIC('k1'), () => slowIC('k1', 'Killer', 6),
            () => relocateFromCard('tr1'), () => steamrollTar('t1', 'Tar Baby', 4),
            () => window.openEnemyAttackModal && openEnemyAttackModal('ed1', 'Ghost'),
            () => window.scanEnemyDecker && scanEnemyDecker('ed1'),
            () => window.strikeEnemyDecker && strikeEnemyDecker('ed1'),
            () => scr.scramble_ref && decryptScramble(scr.scramble_ref),
            () => scr.scramble_ref && crashScramble(scr.scramble_ref),
            () => bomb.target && defuseBomb(bomb.target),
            () => { const f = (st.located_paydata || [])[0]; return f && downloadFile(f.id || f.name); },
            () => { const f = (st.located_paydata || [])[0]; return f && analyzeFileIcon(f.id || f.name); },
            () => { const f = (st.located_paydata || [])[0]; return f && editFile(f.id || f.name, 'erase'); },
            () => toggleSuppress('k1', false), () => toggleSuppress('k1', true),
            () => doEndTurn(),
        ];
        for (const c of calls) { try { c(); } catch (e) {} dismiss(); }
    }""")
    # (C) submit every action (performAction builds + posts each request; may replace _run, so last).
    _safe_render(page, rich_player)
    page.evaluate("""() => {
        const dismiss = () => {
            try { document.querySelectorAll('.open').forEach(m => m.classList.remove('open')); } catch (e) {}
            try { document.querySelectorAll('.mr-prompt').forEach(m => m.remove()); } catch (e) {}
        };
        const sel = document.getElementById('actionType');
        if (!sel) return;
        const vals = Array.prototype.slice.call(sel.querySelectorAll('option')).map(o => o.value);
        for (const v of vals) { sel.value = v; try { onActionTypeChange(); } catch (e) {} try { performAction(); } catch (e) {} dismiss(); }
    }""")
    # (D) the inline hard-stop defense prompt (_renderStreamPrompt) + its Resist button / HP steppers,
    #     plus dice-bearing events so the roll-stream renderer (pushRoll) runs.
    _safe_render(page, _raw_run({
        "logon_complete": True,
        "pending_defense": {"attacker_label": "Black IC", "attack_successes": 3, "power": 6,
                            "hp_available": 4, "to_hit_roll": {"dice": [5, 5, 8]}},
        "event_log": [
            {"type": "ic_attack", "description": "Black IC strikes.", "ic_type": "Black IC",
             "defense_roll": {"dice": [3, 5, 6], "successes": 1}},
            {"type": "action_result", "description": "Attack resolved.",
             "roll": {"dice": [2, 4, 6, 6], "successes": 2}},
        ],
    }))
    page.evaluate("""() => {
        try {
            const feed = document.getElementById('mr-stream-feed');
            if (feed) {
                feed.querySelectorAll('button[data-a]').forEach(b => { try { b.click(); } catch (e) {} });
                const go = document.getElementById('mr-def-go');
                if (go) { try { go.click(); } catch (e) {} }
            }
        } catch (e) {}
    }""")
    # (E) the Suppress-decision modal + its confirm buttons (yes/no.onclick). Call checkSuppressionModal
    #     directly with DF headroom (base 5) so it takes the "Suppress or Accept tally" branch and both
    #     buttons are live, then invoke each -- robust against the streaming state left by (D).
    page.evaluate("""() => {
        try { _streaming = false; } catch (e) {}
        const state = {
            logon_complete: true, base_detection_factor: 5, detection_factor: 5, suppression_count: 0,
            active_ic: [{ id: 'sd1', type: 'Killer', rating: 6, status: 'crashed',
                          detection_level: 3, category: 'proactive', boxes: 10 }],
            condition_monitor: {},
        };
        try { _run = { id: 1, status: 'active', decker_json: {}, state_json: state }; } catch (e) {}
        try { checkSuppressionModal(state, {}); } catch (e) {}
        const yes = document.getElementById('suppressModalYes');
        const no = document.getElementById('suppressModalNo');
        try { if (yes && yes.onclick) yes.onclick(); } catch (e) {}
        try { if (no && no.onclick) no.onclick(); } catch (e) {}
    }""")
    page.wait_for_timeout(150)   # flush async handler continuations before coverage is captured


# Floors chosen from the measured coverage with margin. The STRONG gate is `uncovered_fns` empty:
# every NAMED function in the run console must be exercised by the sweep (stable run-to-run, unlike
# the block %, which shifts slightly with V8 JIT). The percentage floors are the secondary signal --
# a drop means a whole slice of the UI stopped being reached; raise them as coverage grows.
#
# Block coverage plateaus near ~63%: the remaining branches are defensive null-guards and rare
# state combinations that neither more random seeds (measured: 56 -> 240 states moved it <2 points)
# nor injected API failures reach. Function coverage (0 named gaps) is the meaningful "every function
# runs" guarantee; the invariant battery + admin-superset + Fed Bank regressions are what actually
# assert CORRECTNESS on every seeded system.
_FUNCTION_FLOOR_PCT = 88.0
_COVERAGE_FLOOR_PCT = 58.0


@pytest.mark.skipif(not _RAW_CORPUS, reason="no captured states (playwright unavailable)")
def test_frontend_branch_coverage(_browser, _frontend_port, capsys):
    """Report matrix-run.html V8 block coverage across the whole seeded sweep and assert it stays above
    the floor. The printed 'functions never entered' list is the actionable gap -- add a state that
    reaches them to push coverage up."""
    page = _make_page(_browser, _frontend_port, is_admin=True)
    try:
        cdp = page.context.new_cdp_session(page)
        cdp.send("Profiler.enable")
        cdp.send("Profiler.startPreciseCoverage", {"callCount": True, "detailed": True})
    except Exception as exc:  # noqa: BLE001 -- coverage is Chromium-only
        pytest.skip(f"V8 precise coverage unavailable: {exc}")

    try:
        _drive_for_coverage(page)
        raw = cdp.send("Profiler.takePreciseCoverage")
    finally:
        try:
            cdp.send("Profiler.stopPreciseCoverage")
        except Exception:  # noqa: BLE001
            pass

    total = covered = 0
    total_fns = covered_fns = 0
    uncovered_fns = []
    for script in raw.get("result", []):
        if "matrix-run.html" not in script.get("url", ""):
            continue
        for fn in script.get("functions", []):
            ranges = fn.get("ranges", [])
            if not ranges:
                continue
            total += len(ranges)
            covered += sum(1 for r in ranges if (r.get("count", 0) or 0) > 0)
            entered = (ranges[0].get("count", 0) or 0) > 0
            total_fns += 1
            covered_fns += 1 if entered else 0
            if not entered and fn.get("functionName"):
                uncovered_fns.append(fn["functionName"])

    assert total > 0, "no V8 coverage captured for matrix-run.html (inline script url not matched)"
    pct = 100.0 * covered / total
    fn_pct = 100.0 * covered_fns / total_fns if total_fns else 0.0
    report = (
        f"\nmatrix-run.html V8 coverage:  functions {fn_pct:.1f}% ({covered_fns}/{total_fns})  |  "
        f"blocks {pct:.1f}% ({covered}/{total})\n"
        f"functions never entered ({len(sorted(set(uncovered_fns)))}): "
        f"{sorted(set(uncovered_fns))}\n")
    with capsys.disabled():
        print(report)

    named_gaps = sorted(set(uncovered_fns))
    assert not named_gaps, (
        f"named run-console function(s) never exercised by the seeded sweep -- add a state or "
        f"interaction that reaches them (this is the 'exercise the whole program' gate): {named_gaps}"
        f"{report}")
    assert fn_pct >= _FUNCTION_FLOOR_PCT, (
        f"matrix-run.html function coverage {fn_pct:.1f}% fell below floor {_FUNCTION_FLOOR_PCT}% -- "
        f"a whole function stopped being reached by the seeded sweep.{report}")
    assert pct >= _COVERAGE_FLOOR_PCT, (
        f"matrix-run.html block coverage {pct:.1f}% fell below floor {_COVERAGE_FLOOR_PCT}% -- a UI "
        f"branch stopped being reached by the seeded sweep.{report}")
