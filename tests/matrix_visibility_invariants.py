"""Canonical admin-vs-player VISIBILITY invariants for the SR2 Matrix run engine.

These are the GENERAL truths that must hold in EVERY serialized state of EVERY run -- for any
host and any action sequence. They are the machine-checked definition of "the UI can only reveal
what the rules permit, when they permit it," and they are the bug-detector both harnesses share:

  * tests/test_matrix_visibility_e2e.py  -- targeted regressions (the known playtest bugs)
  * tests/test_matrix_visibility_fuzz.py -- generative DISCOVERY (randomized hosts + actions)

Design: docs/matrix-e2e-visibility-harness.md. Each ``check_*`` is a pure function that raises
AssertionError with a reproducible message on violation. ``check_all`` serializes both views once
and runs the whole battery; it is the single call both harnesses use, so a new invariant added
here is instantly enforced across every scenario and every fuzz seed.

This module has no ``test_`` functions, so pytest does not collect it directly.
"""

from __future__ import annotations

from app.routers import matrix_runs as mr

AUTH_ADMIN = {"is_admin": True, "is_user": False, "user_token": None}
AUTH_PLAYER = {"is_admin": False, "is_user": True, "user_token": "harness"}


def serialize(run, auth) -> dict:
    """The real player/admin serialization of a run's state (what the browser would receive)."""
    return mr._serialize_run(run, auth).get("state_json", {}) or {}


# --------------------------------------------------------------------------- secrecy
def check_no_gm_key_leak(admin: dict, player: dict, ctx: str = "") -> None:
    """(1) No GM-only state key may ever reach the player payload (mr._GM_ONLY_STATE_KEYS)."""
    leaked = mr._GM_ONLY_STATE_KEYS & set(player)
    assert not leaked, f"GM-only keys leaked to player: {sorted(leaked)} {ctx}"


def check_security_hidden(admin: dict, player: dict, ctx: str = "") -> None:
    """(1) Raw tally/alert are never sent; host Security code/value hide until Analyze Host."""
    assert "security_tally" not in player, f"raw security tally leaked to player {ctx}"
    assert "alert_status" not in player, f"raw alert status leaked to player {ctx}"
    if not player.get("host_security_revealed"):
        assert "host_security_code" not in player, f"host security code leaked pre-analyze {ctx}"
        assert "host_security_value" not in player, f"host security value leaked pre-analyze {ctx}"


def check_trap_ic_redaction(admin: dict, player: dict, ctx: str = "") -> None:
    """(1) A concealed (trap) IC in the player view is a bare ``True`` marker -- never its
    hidden type/rating (which would leak what the [TRAP] badge is hiding)."""
    for ic in (player.get("active_ic") or []):
        if isinstance(ic, dict) and "trap_hidden" in ic:
            assert ic["trap_hidden"] is True, (
                f"trap_hidden leaked details to player: {ic.get('trap_hidden')!r} {ctx}")


# --------------------------------------------------------------------------- disclosure
def check_progressive_disclosure(admin: dict, player: dict, ctx: str = "") -> None:
    """(2) A located file's size stays hidden from the player until it is analyzed; once analyzed
    the size is present. (Bug C.)"""
    for p in (player.get("located_paydata") or []):
        if not isinstance(p, dict):
            continue
        if p.get("analyzed"):
            assert p.get("size_mp") is not None, (
                f"analyzed file {p.get('name')!r} hides its size from the player {ctx}")
        else:
            assert p.get("size_mp") is None, (
                f"unanalyzed file {p.get('name')!r} leaked its size to the player {ctx}")


# --------------------------------------------------------------------------- parity
def check_admin_parity(admin: dict, player: dict, ctx: str = "") -> None:
    """(3) The admin never knows FEWER located files than the player, and always with a real size
    (admin Analyze Icon needs those targets -- Bug B)."""
    a_ids = {(p.get("id") or p.get("name")) for p in (admin.get("located_paydata") or [])
             if isinstance(p, dict)}
    p_ids = {(p.get("id") or p.get("name")) for p in (player.get("located_paydata") or [])
             if isinstance(p, dict)}
    missing = {i for i in (p_ids - a_ids) if i is not None}
    assert not missing, f"admin located_paydata missing files the player sees: {missing} {ctx}"
    for p in (admin.get("located_paydata") or []):
        if isinstance(p, dict):
            assert p.get("size_mp") is not None, (
                f"admin size_mp hidden for {p.get('name')!r} {ctx}")


# --------------------------------------------------------------------------- well-formedness
def check_state_well_formed(admin: dict, player: dict, ctx: str = "") -> None:
    """(0) Engine state stays sane: condition monitors in 0..10, no negative tally/pool. A
    violation here is usually an engine-state-corruption bug surfaced by the serialization."""
    cm = admin.get("condition_monitor") or {}
    for k in ("persona_boxes", "stun_boxes", "physical_boxes"):
        v = cm.get(k, 0) or 0
        assert 0 <= v <= 10, f"{k}={v} out of 0..10 {ctx}"
    assert (admin.get("security_tally", 0) or 0) >= 0, f"negative security tally {ctx}"
    assert (admin.get("hackingPool_remaining", 0) or 0) >= 0, f"negative Hacking Pool {ctx}"


BATTERY = (
    check_no_gm_key_leak,
    check_security_hidden,
    check_trap_ic_redaction,
    check_progressive_disclosure,
    check_admin_parity,
    check_state_well_formed,
)


def check_all(run, ctx: str = "") -> tuple[dict, dict]:
    """Serialize both views once and run the whole battery. Both serializations must also SUCCEED
    (a redaction bug that throws is itself a finding). Returns (admin_state, player_state)."""
    try:
        admin = serialize(run, AUTH_ADMIN)
        player = serialize(run, AUTH_PLAYER)
    except Exception as exc:  # noqa: BLE001 -- a serialization crash is a reportable bug
        raise AssertionError(f"_serialize_run raised {type(exc).__name__}: {exc} {ctx}") from exc
    for check in BATTERY:
        check(admin, player, ctx)
    return admin, player
