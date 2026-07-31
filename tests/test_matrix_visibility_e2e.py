"""End-to-end visibility & redaction invariant harness for the SR2 Matrix run engine.

Design: docs/matrix-e2e-visibility-harness.md

This module drives the REAL run endpoints (``app.routers.matrix_runs``) and the REAL
serializer, then asserts a battery of admin-vs-player visibility invariants after every
step. It encodes the Federated Bank playtest bugs (B/C/D/E/F) as permanent regressions:

  B  admin serialization must carry located_paydata (admin Analyze Icon needs targets)
  C  a located file's size + ENCRYPTED status stay hidden from the player until Analyze Icon
  D  Invalidate Passcode (entire system) is offerable whenever logged on
  E  a discovered Scramble is visible to the player the instant its ``discovered`` flag flips
  F  an analyzed file is dropped from the Analyze Icon target set

Two styles, on purpose (see the design doc): DIRECT-STATE tests hand-build a state and call
the real ``_serialize_run`` (deterministic, zero dice, pins the redaction logic); the DRIVEN
test calls the real ``perform_action`` endpoints under a fixed seed (integration proof).
"""

from __future__ import annotations

import asyncio
import datetime
import random
from pathlib import Path

from fastapi import HTTPException

from app.routers import matrix_runs as mr
from app.services import matrix_engine as eng
from app.schemas.matrix_run import DeckerStats, RunActionInput

from tests import matrix_visibility_invariants as inv

SEED = 20260730

ROOT = Path(__file__).resolve().parents[1]
RUN_UI = (ROOT / "frontend" / "matrix-run.html").read_text(encoding="utf-8")

AUTH_ADMIN = {"is_admin": True, "is_user": False, "user_token": None}
AUTH_PLAYER = {"is_admin": False, "is_user": True, "user_token": "harness"}

ENCRYPTED_FILE = "Encrypted Ledger"
BOMB_FILE = "Booby File"
PLAIN_FILE = "Memo"


# =============================================================================
# Fixtures: a reveal-bearing synthetic host + an overwhelmingly capable decker.
# =============================================================================
class _Host:
    """Minimal MatrixHost stand-in accepted by _initial_state / _build_trap_doors."""

    def __init__(self):
        self.id = 9001
        self.name = "Harness Vault"
        self.ltg_address = "LTG://harness/vault"
        self.trap_doors_json = None
        self.config_json = {
            "security_code": "Green",
            "security_value": 4,
            # Trivial subsystem ratings -> low TNs so the seeded drive reliably succeeds.
            "acifs": [2, 2, 2, 2, 2],
            # No scripted sheaf steps: keeps IC spawns out of the deterministic drive.
            "sheaf": [],
            "paydata": [
                {"id": "pd_locked", "name": ENCRYPTED_FILE, "density": 90, "is_key": True, "defense": 0},
                {"id": "pd_bomb", "name": BOMB_FILE, "density": 40, "is_key": False, "defense": 0},
                {"id": "pd_plain", "name": PLAIN_FILE, "density": 20, "is_key": False, "defense": 0},
            ],
            # A Poison Scramble encrypts the key file (the C/E reveal path).
            "scrambles": [
                {"target_key": f"files::file::{ENCRYPTED_FILE}", "rating": 6, "variant": "poison"},
            ],
            "data_bombs": [
                {"target": f"files::file::{BOMB_FILE}", "rating": 5},
            ],
        }


def _build_decker() -> dict:
    # rating, active-size (size is irrelevant here -- memory is not the constraint under test)
    active = {
        "attack": (6, 96), "deception": (6, 24), "analyze": (6, 36), "browse": (6, 36),
        "evaluate": (6, 36), "read_write": (6, 36), "decrypt": (6, 18), "defuse": (6, 24),
        "sleaze": (6, 108),
    }
    utilities = {k: r for k, (r, _s) in active.items()}
    program_sizes = {k: s for k, (_r, s) in active.items()}
    stats = DeckerStats(
        name="Prober", character_id=2, deck_name="Harness Deck",
        mpcp=10, bod=6, evasion=6, masking=6, sensor=6,
        computer_skill=12, intelligence=6, quickness=4, willpower=5, body=4,
        deck_mode="hot", iccm=False, hardening=6, response_increase=3,
        active_memory=800, io_speed=800,
        trace_factor=0, base_bandwidth=100, access_modifier=2,
        reaction_modifier=-2, physical_trace_immune=True,
        storage_free_mp=2000,
        utilities=utilities,
        storage_programs=[],
        program_sizes=program_sizes,
        program_options={},
    )
    return stats.model_dump()


class _FakeDB:
    async def commit(self):
        return None

    async def refresh(self, obj):
        return None

    async def get(self, *a, **k):
        return None

    async def execute(self, *a, **k):
        class _Empty:
            def scalars(self_):
                return self_

            def first(self_):
                return None

            def all(self_):
                return []

        return _Empty()


class _StubRun:
    def __init__(self, decker, state):
        now = datetime.datetime.now(datetime.timezone.utc)
        self.id = 1
        self.host_id = 9001
        self.status = "active"
        self.owner_token_hash = None
        self.decker_json = decker
        self.state_json = state
        self.created_at = now
        self.updated_at = now
        self.version = 1
        self.aar_acknowledged = False


def _new_run(monkeypatch) -> _StubRun:
    """Seed the three RNG surfaces, build the run, and patch the run lookup / access guard.

    ``monkeypatch`` auto-restores the patched module attributes after the test, so this cannot
    contaminate the rest of the suite.
    """
    random.seed(SEED)
    eng.random.seed(SEED)
    mr.random.seed(SEED)
    host = _Host()
    decker = _build_decker()
    state = mr._initial_state(decker, host)
    run = _StubRun(decker, state)

    async def _get_run_or_404(db, run_id):
        return run

    monkeypatch.setattr(mr, "_get_run_or_404", _get_run_or_404)
    monkeypatch.setattr(mr, "_assert_run_access", lambda r, a: None)
    return run


# =============================================================================
# Dual-view capture + the invariant library (see design doc, section 3).
# =============================================================================
# Dual-view capture + the invariant battery come from the shared canonical module
# (tests/matrix_visibility_invariants.py) so these targeted regressions and the generative fuzzer
# (tests/test_matrix_visibility_fuzz.py) enforce the IDENTICAL admin-vs-player rules.
# =============================================================================
def dual_view(run):
    admin = mr._serialize_run(run, AUTH_ADMIN).get("state_json", {})
    player = mr._serialize_run(run, AUTH_PLAYER).get("state_json", {})
    return admin, player


def assert_invariants(run, label=""):
    """Delegate to the shared canonical battery so a new invariant added there is enforced here too."""
    return inv.check_all(run, label)


def _file(view_list, name):
    return next((p for p in (view_list or []) if p.get("name") == name), None)


# =============================================================================
# DIRECT-STATE tests -- deterministic, exercise the real _serialize_run redaction.
# =============================================================================
def test_progressive_disclosure_and_redaction_direct(monkeypatch):
    """B/C/E + secrecy: a located-but-unanalyzed encrypted file hides its size from the player,
    the admin sees it fully, the discovered scramble shows immediately, and no GM-only key leaks.
    Then Analyze Icon reveals the size to the player."""
    run = _new_run(monkeypatch)
    st = run.state_json
    st["logon_complete"] = True
    # Locate File found the key file; Analyze Subsystem discovered its scramble.
    for p in st["paydata"]:
        if p["name"] == ENCRYPTED_FILE:
            p["located"] = True
    for sc in st["scrambles"]:
        sc["discovered"] = True

    admin, player = assert_invariants(run, "located-not-analyzed")

    # B: admin sees the located file with its real size.
    a_locked = _file(admin["located_paydata"], ENCRYPTED_FILE)
    assert a_locked is not None and a_locked["size_mp"] == 90

    # C: player sees the file by name, but size hidden and not yet analyzed.
    p_locked = _file(player["located_paydata"], ENCRYPTED_FILE)
    assert p_locked is not None
    assert p_locked["size_mp"] is None
    assert p_locked["analyzed"] is False
    assert p_locked["encrypted"] is True  # truthful in payload for the Download gate

    # E: the discovered scramble is surfaced to the player immediately (no IC dependency).
    assert player.get("discovered_scrambles"), "discovered scramble not surfaced to the player"

    # ...Analyze Icon on the file now reveals its size to the player.
    for p in st["paydata"]:
        if p["name"] == ENCRYPTED_FILE:
            p["analyzed"] = True
    _, player2 = assert_invariants(run, "analyzed")
    p_locked2 = _file(player2["located_paydata"], ENCRYPTED_FILE)
    assert p_locked2["size_mp"] == 90 and p_locked2["analyzed"] is True


def test_analyzed_file_dropped_from_analyze_targets_direct(monkeypatch):
    """F: the server marks a scanned file ``analyzed``; the run-UI ``_analyzeIconTargets`` filter
    (``!p.analyzed``) then drops it. We pin the server half of that contract here."""
    run = _new_run(monkeypatch)
    st = run.state_json
    st["logon_complete"] = True
    for p in st["paydata"]:
        if p["name"] == ENCRYPTED_FILE:
            p["located"] = True

    _, player = dual_view(run)
    p_locked = _file(player["located_paydata"], ENCRYPTED_FILE)
    assert p_locked["analyzed"] is False  # still a valid Analyze Icon target

    # The real Analyze Icon application flips the flag the UI filters on.
    mr._apply_analyze_icon(st, target_file=ENCRYPTED_FILE)
    _, player2 = dual_view(run)
    p_locked2 = _file(player2["located_paydata"], ENCRYPTED_FILE)
    assert p_locked2["analyzed"] is True  # now excluded from _analyzeIconTargets


# =============================================================================
# DRIVEN test -- real endpoints, seeded. Proves the invariants on ENGINE-produced state.
# =============================================================================
def test_driven_logon_locate_analyze_real_endpoints(monkeypatch):
    """Drive the real perform_action stack (logon -> locate file -> analyze icon) under a fixed
    seed. The redaction battery must hold after EVERY step; once the drive reaches an analyzed
    file, the player reveal invariants are proven on engine-produced state."""
    run = _new_run(monkeypatch)
    loop = asyncio.new_event_loop()

    def call(coro):
        return loop.run_until_complete(coro)

    def end_turn():
        try:
            call(mr.new_turn(1, AUTH_PLAYER, _FakeDB()))
        except HTTPException:
            pass

    def do(action, subsystem, **kw):
        """Perform an action, advancing the initiative economy when the pass can't afford it."""
        for _ in range(12):
            if run.state_json.get("run_ended"):
                return False
            body = RunActionInput(action_type=action, subsystem=subsystem, **kw)
            try:
                call(mr.perform_action(1, body, AUTH_PLAYER, _FakeDB()))
                return True
            except HTTPException as exc:
                detail = str(exc.detail)
                if any(m in detail for m in ("action point", "Free action", "Not enough", "turn(s)")):
                    end_turn()
                    continue
                return False
        return False

    # Redaction holds from the very first serialization (pre-logon).
    assert_invariants(run, "pre-logon")

    assert do("logon_to_host", "access", utility_rating=6, hacking_pool_dice=2), "logon failed"
    assert run.state_json.get("logon_complete") is True
    assert_invariants(run, "post-logon")

    # Locate the encrypted target file (real Index/Browse test), then Analyze its icon.
    do("locate_file", "index", target_file=ENCRYPTED_FILE, utility_rating=6, hacking_pool_dice=2)
    assert_invariants(run, "post-locate")

    do("analyze_icon", "control", target_file=ENCRYPTED_FILE)
    admin, player = assert_invariants(run, "post-analyze")

    # The seeded drive reaches the analyzed reveal, so prove the reveal invariants end-to-end on
    # engine-produced state (seed makes the dice deterministic -- reproducible, not flaky).
    p_locked = _file(player["located_paydata"], ENCRYPTED_FILE)
    assert p_locked is not None and p_locked.get("analyzed"), (
        "seeded drive did not reach an analyzed file -- retune SEED / decker before asserting reveal")
    assert p_locked["size_mp"] == 90, "analyzed file did not reveal its size to the player"
    assert player.get("discovered_scrambles"), "analyzed encrypted file did not surface its scramble"
    a_locked = _file(admin["located_paydata"], ENCRYPTED_FILE)
    assert a_locked is not None and a_locked["size_mp"] == 90  # admin parity on live state


# =============================================================================
# STATIC frontend contract -- pins the run-UI half of the C/D/F/A fixes (literal-token search of
# matrix-run.html, same style as tests/test_matrix_reconciliation.py). A headless state check
# cannot see the dropdown/tooltip render, so these tokens are the regression guard for it.
# =============================================================================
def test_frontend_visibility_contracts_static():
    # C: the paydata panel gates size + ENCRYPTED badge on "size known", not on raw encryption.
    assert "const known   = p.size_mp !== null && p.size_mp !== undefined;" in RUN_UI
    assert "const showEnc = known && p.encrypted;" in RUN_UI
    assert "p.encrypted ? '??? Mp'" not in RUN_UI  # the old leak-prone gate is gone

    # D: Invalidate Passcode always offers the whole-system option and drops the visible-IC gate.
    assert "const opts = [{ value: '__all__', label: 'Entire system passcode table (+4 TN)' }];" in RUN_UI
    assert "if (single.length >= 2) opts.push({ value: '__all__'" not in RUN_UI

    # F: an analyzed file is filtered out of the Analyze Icon target list.
    assert "(s.located_paydata || []).filter(p => !p.destroyed && !p.analyzed)" in RUN_UI

    # A: the deck adjust-loadout program cards use the in-app tooltip with real descriptions.
    assert "function laoCardTip(label, utilName, sizeMp, hint)" in RUN_UI
    assert 'data-tip="${esc(laoCardTip(' in RUN_UI
    assert 'title="Drag between Active and Storage; drag out to remove"' not in RUN_UI
