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

import copy

from app.routers import matrix_runs as mr

AUTH_ADMIN = {"is_admin": True, "is_user": False, "user_token": None}
AUTH_PLAYER = {"is_admin": False, "is_user": True, "user_token": "harness"}


def serialize(run, auth) -> dict:
    """The real player/admin serialization of a run's state (what the browser would receive)."""
    return mr._serialize_run(run, auth).get("state_json", {}) or {}


def check_serialization_pure(run, ctx: str = "") -> None:
    """(0) Redaction is a READ: serializing either view must never mutate the stored run state.
    A serializer that writes back (e.g. leaves computed/redacted keys on the shared dict) can leak
    a redaction from one request into the next, or corrupt persisted state."""
    before = copy.deepcopy(run.state_json)
    serialize(run, AUTH_ADMIN)
    serialize(run, AUTH_PLAYER)
    assert run.state_json == before, (
        f"_serialize_run mutated the stored run state (redaction must be read-only) {ctx}")


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


def check_slave_devices_gated(admin: dict, player: dict, ctx: str = "") -> None:
    """(1) Named Slave devices (host interior topology) reach the player only after a successful
    Analyze Subsystem on Slave -- exposing them earlier leaks the host layout."""
    if player.get("slave_devices"):
        analyzed = player.get("analyzed_subsystems") or []
        assert "slave" in analyzed, (
            f"slave_devices exposed to player before analyzing the Slave subsystem {ctx}")


def check_ltg_hidden(admin: dict, player: dict, ctx: str = "") -> None:
    """(1) A host's LTG-access status AND grid address stay hidden from the player until a
    successful Analyze Subsystem on Access (host_ltg_revealed)."""
    if not player.get("host_ltg_revealed"):
        assert "host_has_ltg" not in player, f"host_has_ltg leaked before LTG reveal {ctx}"
        assert "host_ltg_address" not in player, f"host_ltg_address leaked before LTG reveal {ctx}"


def check_trap_door_destination_hidden(admin: dict, player: dict, ctx: str = "") -> None:
    """(1) A discovered trap door tells the player only that a port exists (id/source/subsystem) --
    never where it leads; the destination stays unknown until the decker actually enters it."""
    for d in (player.get("discovered_trap_doors") or []):
        if not isinstance(d, dict):
            continue
        for leak in ("destination_host_id", "destination_ltg", "destination_label"):
            assert leak not in d, f"trap door leaked {leak!r} to the player {ctx}"


def check_event_log_redaction(admin: dict, player: dict, ctx: str = "") -> None:
    """(1) The player event log never carries a GM-only entry (surreptitious hidden-IC activity the
    decker has not detected)."""
    for e in (player.get("event_log") or []):
        if isinstance(e, dict):
            assert not e.get("gm_only"), f"gm_only event leaked into the player log: {e.get('type')} {ctx}"


_ENEMY_FORBIDDEN = frozenset({
    "mpcp", "bod", "evasion", "masking", "sensor", "utilities", "program_options",
    "program_sizes", "intent", "deck_mode", "computer_skill", "hacking_pool",
})


def check_enemy_decker_redaction(admin: dict, player: dict, ctx: str = "") -> None:
    """(1) A revealed enemy decker shows the player only presence + condition (and, once Scanned,
    the base ratings uncovered in ``scanned``) -- never its raw stats, loadout, or intent."""
    for e in (player.get("enemy_deckers") or []):
        if not isinstance(e, dict):
            continue
        leaked = _ENEMY_FORBIDDEN & set(e)
        assert not leaked, f"enemy decker leaked raw fields to the player: {sorted(leaked)} {ctx}"


def check_ic_identity_redaction(admin: dict, player: dict, ctx: str = "") -> None:
    """(1) Graduated IC reveal (vr2 line 409): an IC the decker has not fully identified must not
    leak its identity. At detection level < 2 the type reads "Unknown IC" and the threat class is
    withheld; the exact rating stays hidden until a full level-3 identification."""
    for ic in (player.get("active_ic") or []):
        if not isinstance(ic, dict):
            continue
        level = ic.get("detection_level")
        if level is None:
            continue
        if level < 2:
            assert ic.get("type") in (None, "Unknown IC"), (
                f"IC type leaked at detection level {level}: {ic.get('type')!r} {ctx}")
            assert ic.get("category") is None, (
                f"IC threat class leaked at detection level {level}: {ic.get('category')!r} {ctx}")
        if level < 3:
            assert ic.get("rating") is None, (
                f"IC rating leaked at detection level {level}: {ic.get('rating')!r} {ctx}")


def check_pending_defense_redaction(admin: dict, player: dict, ctx: str = "") -> None:
    """(1) The interactive-defense prompt the player sees must not carry its internal ``ctx`` (host
    Security code/value + attack modifiers) or the resume bookkeeping -- only /defend needs those."""
    pend = player.get("pending_defense")
    if isinstance(pend, dict):
        for leak in ("ctx", "resume_logon_completed", "resume_count_window",
                     "resume_phase_transition", "acting_init", "acting_count"):
            assert leak not in pend, f"pending_defense leaked {leak!r} to the player {ctx}"


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


# --------------------------------------------------------------------------- cross-view consistency
def check_located_file_parity(admin: dict, player: dict, ctx: str = "") -> None:
    """(3) For every located file the player sees, the admin entry exists and AGREES on every field
    except ``size_mp`` -- which the player alone may mask (None) until the file is analyzed. Catches
    any field that leaks or diverges between the two views (encryption, key, download/destroy state)."""
    a_by_id = {(p.get("id") or p.get("name")): p
               for p in (admin.get("located_paydata") or []) if isinstance(p, dict)}
    for p in (player.get("located_paydata") or []):
        if not isinstance(p, dict):
            continue
        fid = p.get("id") or p.get("name")
        a = a_by_id.get(fid)
        assert a is not None, f"player file {fid!r} absent from admin located_paydata {ctx}"
        for field in ("is_key", "encrypted", "downloaded", "destroyed", "tampered"):
            assert p.get(field) == a.get(field), (
                f"file {fid!r} field {field!r} differs player={p.get(field)!r} "
                f"admin={a.get(field)!r} {ctx}")
        if p.get("size_mp") is not None:
            assert p.get("size_mp") == a.get("size_mp"), (
                f"file {fid!r} revealed size {p.get('size_mp')} != admin {a.get('size_mp')} {ctx}")


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


def check_detection_factor_sane(admin: dict, player: dict, ctx: str = "") -> None:
    """(0) The decker's Detection Factor is always >= 1 and the suppression count is non-negative in
    BOTH views -- a redaction or computation bug that zeros / negates DF would surface here."""
    for label, view in (("admin", admin), ("player", player)):
        df = view.get("detection_factor")
        if df is not None:
            assert df >= 1, f"{label} detection_factor={df} < 1 {ctx}"
        sc = view.get("suppression_count")
        if sc is not None:
            assert sc >= 0, f"{label} suppression_count={sc} < 0 {ctx}"


BATTERY = (
    check_no_gm_key_leak,
    check_security_hidden,
    check_trap_ic_redaction,
    check_slave_devices_gated,
    check_ltg_hidden,
    check_trap_door_destination_hidden,
    check_event_log_redaction,
    check_enemy_decker_redaction,
    check_ic_identity_redaction,
    check_pending_defense_redaction,
    check_progressive_disclosure,
    check_admin_parity,
    check_located_file_parity,
    check_state_well_formed,
    check_detection_factor_sane,
)


# --------------------------------------------------------------------------- cross-STEP (temporal)
def check_monotonic_disclosure(prev_player: dict, cur_player: dict, ctx: str = "") -> None:
    """Disclosure never regresses WITHIN a run: a revealed host ACIFS rating stays revealed, and a
    file that has been analyzed stays analyzed (with its size still shown) for as long as it remains
    on the board. A flicker here is the E-class bug -- a disclosure that appears, then vanishes.

    (host_security_revealed is deliberately NOT asserted here: a Bouncer sheaf event can legitimately
    rotate the security code and re-hide it until re-analyzed. A destroyed/erased file may leave the
    list entirely -- that is not a disclosure regression, so a vanished file is tolerated; only an
    un-analyze or size un-reveal WHILE STILL PRESENT is a violation.)"""
    prev_ratings = set(prev_player.get("host_ratings_revealed") or {})
    cur_ratings = set(cur_player.get("host_ratings_revealed") or {})
    lost = prev_ratings - cur_ratings
    assert not lost, f"host ACIFS ratings un-revealed: {sorted(lost)} {ctx}"

    cur_files = {(p.get("id") or p.get("name")): p
                 for p in (cur_player.get("located_paydata") or []) if isinstance(p, dict)}
    for p in (prev_player.get("located_paydata") or []):
        if not isinstance(p, dict) or not p.get("analyzed"):
            continue
        fid = p.get("id") or p.get("name")
        c = cur_files.get(fid)
        if c is None:
            continue  # file left the board (destroyed / erased) -- not a disclosure regression
        assert c.get("analyzed"), f"file {fid!r} un-analyzed after being analyzed {ctx}"
        assert c.get("size_mp") is not None, f"file {fid!r} size un-revealed after analysis {ctx}"


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

