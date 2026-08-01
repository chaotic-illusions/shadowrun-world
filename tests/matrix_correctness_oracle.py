"""SR2 Matrix engine CORRECTNESS oracle -- "I did X, so per the rules I should see Y. Do I?"

Where ``matrix_visibility_invariants`` asserts the UI can only REVEAL what the rules permit, this
module asserts the engine COMPUTES the rules correctly. Each check derives the expected result
INDEPENDENTLY from the SR2 rules (vr2_rules.md) -- from the recorded dice, the before/after state,
and the action the player took -- and compares it to what the engine actually produced. A mismatch
is a game-LOGIC bug (the class the Federated Bank playtest surfaced), not a redaction bug.

Dice are random, so every check is either:
  (a) a dice-AGNOSTIC rule relationship that must hold no matter what was rolled, or
  (b) a re-derivation FROM the recorded roll -- e.g. the rule of 6: the number of successes MUST
      equal the number of dice that met the target number. Copying the engine would be circular,
      so the checks apply the RULE arithmetic, never the engine's helpers.

Each ``check_*`` is a pure function raising AssertionError with a reproducible message.
``check_transition`` runs the whole battery on one (before -> after) action step. This module has no
``test_`` functions, so pytest does not collect it directly.
"""

from __future__ import annotations

import math

# A "roll" as produced by matrix_engine.roll_dice: {pool, tn, dice, successes, ones}. `dice` holds
# the per-die POST-explosion totals when tn > 6 (rule of 6), so `d >= tn` is an honest hit.
_ROLL_KEYS = {"pool", "tn", "dice", "successes"}


def _is_roll(v) -> bool:
    return isinstance(v, dict) and _ROLL_KEYS <= set(v)


def _iter_condition_monitors(state: dict):
    """Yield (label, condition_monitor) for the decker and every enemy decker."""
    cm = state.get("condition_monitor")
    if isinstance(cm, dict):
        yield "decker", cm
    for e in (state.get("enemy_deckers") or []):
        if isinstance(e, dict) and isinstance(e.get("condition_monitor"), dict):
            yield f"enemy {e.get('id')}", e["condition_monitor"]


# --------------------------------------------------------------------------- dice / test math
def check_dice_rolls(new_events: list, ctx: str = "") -> None:
    """(RULE OF 6) Every recorded roll must be internally honest: the success count equals the number
    of dice that met the TN, and the die count equals the pool. This is THE check that a broken dice
    evaluator (e.g. exploding-6 dropped, so every TN>6 test silently yields ~0 successes) can never
    pass. NOTE: this app deliberately floors DF -- and DF-based / damage-resistance TNs -- at 1 (not
    the universal Rule of 2, which it applies only to subsystem/skill tests), so a TN of 1 is legal
    here; only TN < 1 is an outright bug."""
    for ev in new_events:
        if not isinstance(ev, dict):
            continue
        for key, val in ev.items():
            if _is_roll(val):
                _check_one_roll(val, f"{ctx} event={ev.get('type')} field={key}")


def _check_one_roll(roll: dict, ctx: str) -> None:
    tn = int(roll["tn"])
    pool = int(roll["pool"])
    successes = int(roll["successes"])
    dice = [int(d) for d in (roll.get("dice") or [])]
    assert tn >= 1, f"roll TN {tn} < 1 (a target number is never below 1) -- {ctx}"
    assert len(dice) == max(1, pool), (
        f"roll produced {len(dice)} dice for a pool of {pool} (pool floors at 1) -- {ctx}")
    expected = sum(1 for d in dice if d >= tn)
    assert successes == expected, (
        f"DICE MISCOUNT (rule of 6?): engine reports {successes} successes but {expected} of the "
        f"{len(dice)} dice met TN {tn} -- dice={dice} -- {ctx}")
    # `ones` is counted from the RAW rolls; only when tn<=6 are `dice` the raw rolls, so it is
    # re-derivable then (for tn>6 the entries are post-explosion totals).
    if tn <= 6 and "ones" in roll:
        expected_ones = sum(1 for d in dice if d == 1)
        assert int(roll["ones"]) == expected_ones, (
            f"roll reports {roll['ones']} ones but {expected_ones} dice show 1 -- dice={dice} -- {ctx}")


def check_no_success_without_a_hit(new_events: list, ctx: str = "") -> None:
    """A System Test can never SUCCEED with zero decker successes. The exact tie/net rule is
    ACTION-SPECIFIC (ordinary tests succeed on a nonzero tie; Locate Paydata / combat maneuvers /
    Slow / cripplers / Hog are effect-gated and need POSITIVE net; Analyze/Crash Host use raw decker
    successes), so only this one universally-true direction is asserted -- but a success reported on a
    roll of zero decker successes is impossible under every one of those variants and is a real bug."""
    for ev in new_events:
        if not isinstance(ev, dict):
            continue
        dr = ev.get("decker_roll")
        if _is_roll(dr) and ev.get("success") is True:
            assert int(dr["successes"]) > 0, (
                f"action reports SUCCESS with 0 decker successes (impossible in SR2) -- {ctx} "
                f"event={ev.get('type')}/{ev.get('action')}")


# --------------------------------------------------------------------------- detection factor
def check_detection_factor(admin_state: dict, ctx: str = "") -> None:
    """(vr2 Detection Factor) The live DF is exactly max(1, base - suppressions): each held-down
    suppression costs 1 DF and it floors at 1. A DF that forgot the floor, the subtraction, or the
    suppression feed is caught here."""
    df = admin_state.get("detection_factor")
    base = admin_state.get("base_detection_factor")
    supp = admin_state.get("suppression_count")
    if df is None or base is None or supp is None:
        return
    assert df == max(1, base - supp), (
        f"Detection Factor {df} != max(1, base {base} - suppressions {supp}) = {max(1, base - supp)} "
        f"-- {ctx}")


def check_suppression_count(admin_state: dict, ctx: str = "") -> None:
    """(vr2 Suppression) The suppression count that DF is charged for must equal the number of icons
    actually held down (suppressed active IC + suppressed ledger entries)."""
    supp = admin_state.get("suppression_count")
    if supp is None:
        return
    actual = (sum(1 for ic in (admin_state.get("active_ic") or [])
                  if isinstance(ic, dict) and ic.get("suppressed"))
              + sum(1 for s in (admin_state.get("suppressions") or [])
                    if isinstance(s, dict) and s.get("suppressed")))
    assert supp == actual, (
        f"suppression_count {supp} != icons actually suppressed {actual} -- {ctx}")


# --------------------------------------------------------------------------- hacking pool economy
def check_hacking_pool(before: dict, after: dict, hp_provided: int, ctx: str = "") -> None:
    """(SR2 RAW Hacking Pool) The pool depletes as spent and is NEVER topped back up mid-pass; it
    refreshes ONLY at a pass/turn boundary. Within a single action that did not cross such a boundary,
    the pool may only go DOWN, never below 0, and never by more dice than the player actually spent."""
    b, a = before.get("hackingPool_remaining"), after.get("hackingPool_remaining")
    if b is None or a is None:
        return
    if before.get("current_pass") != after.get("current_pass"):
        return  # a pass boundary legitimately refreshes the pool
    if before.get("current_turn") != after.get("current_turn") or after.get("run_ended"):
        return
    assert a >= 0, f"hackingPool_remaining {a} < 0 -- {ctx}"
    assert a <= b, (
        f"hackingPool_remaining ROSE {b} -> {a} within a pass (RAW: no mid-pass refill) -- {ctx}")
    assert b - a <= hp_provided, (
        f"spent {b - a} Hacking Pool dice but only {hp_provided} were provided this action -- {ctx}")


# --------------------------------------------------------------------------- condition monitors
def check_condition_monitors(after: dict, ctx: str = "") -> None:
    """(SR2 Condition Monitor = 10 boxes) Every persona/stun/physical track stays within 0..10 for the
    decker AND every enemy decker. Overflow ("12/10") is an un-capped damage-add bug."""
    for label, cm in _iter_condition_monitors(after):
        for track in ("persona_boxes", "stun_boxes", "physical_boxes"):
            v = int(cm.get(track, 0) or 0)
            assert 0 <= v <= 10, f"{label} {track}={v} out of 0..10 -- {ctx}"


# --------------------------------------------------------------------------- security tally
def check_tally_non_negative(after: dict, ctx: str = "") -> None:
    """The security tally never goes negative (refunds floor at 0)."""
    t = after.get("security_tally")
    if t is not None:
        assert int(t) >= 0, f"security_tally {t} < 0 -- {ctx}"


# --------------------------------------------------------------------------- paydata state changes
def _paydata_by_id(state: dict) -> dict:
    out = {}
    for p in (state.get("paydata") or []):
        if isinstance(p, dict):
            out[p.get("id") or p.get("name")] = p
    return out


def check_locate_marks_located(after: dict, new_events: list, ctx: str = "") -> None:
    """(Locate File / Locate Paydata) If a locate event NAMES the files it found, those files must be
    flagged ``located`` in the resulting state -- otherwise the decker was told a file was found but
    the download/analyze machinery can never see it (the Federated Bank 'located but invisible' class)."""
    named = set()
    for ev in new_events:
        if isinstance(ev, dict) and ev.get("type") in ("file_located", "paydata_located"):
            for f in (ev.get("files") or []):
                if isinstance(f, dict) and f.get("name"):
                    named.add(str(f["name"]))
    if not named:
        return
    located = {str(p.get("name")) for p in (after.get("paydata") or [])
               if isinstance(p, dict) and p.get("located")}
    missing = named - located
    assert not missing, (
        f"locate reported {sorted(named)} found, but not marked located in state: {sorted(missing)} "
        f"-- {ctx}")


def check_analyzed_never_reverts(before: dict, after: dict, ctx: str = "") -> None:
    """(Progressive disclosure) A file that has been Analyze-Icon'd stays analyzed for as long as it is
    on the host; only a destroyed/erased file may leave the list."""
    before_pd = _paydata_by_id(before)
    after_pd = _paydata_by_id(after)
    for fid, p in before_pd.items():
        if not (p.get("located") and p.get("analyzed")):
            continue
        a = after_pd.get(fid)
        if a is None:
            continue  # file left the board (destroyed) -- not a reversion
        assert a.get("analyzed"), f"file {fid!r} un-analyzed after having been analyzed -- {ctx}"


def check_validate_passcode(before: dict, after: dict, action: dict, test_success, ctx: str = "") -> None:
    """(vr2 Validate Passcode L1899) A successful Validate flips ``has_legitimate_status`` to True and
    nothing else; a failure leaves it unchanged. Validate must never CLEAR the flag."""
    if action.get("type") != "validate_passcode":
        return
    if test_success is True:
        assert after.get("has_legitimate_status") is True, (
            f"validate_passcode succeeded but has_legitimate_status is "
            f"{after.get('has_legitimate_status')!r}, not True -- {ctx}")
    # Validate itself never clears the flag (that is alert/logoff/host-gone, not this action).
    if before.get("has_legitimate_status") is True:
        assert after.get("has_legitimate_status") is True, (
            f"validate_passcode CLEARED has_legitimate_status (it must only set it) -- {ctx}")


# --------------------------------------------------------------------------- the battery
def _action_test_success(new_events: list):
    """The success flag of the action's own System Test (the event carrying a decker_roll), or None."""
    for ev in new_events:
        if isinstance(ev, dict) and _is_roll(ev.get("decker_roll")) and isinstance(ev.get("success"), bool):
            return ev["success"]
    return None


def check_transition(before: dict, after: dict, admin_state: dict, new_events: list,
                     action: dict, hp_provided: int, ctx: str = "") -> None:
    """Run the whole correctness battery on one action step. ``before``/``after`` are the raw engine
    state (deep-copied) around the action; ``admin_state`` is the admin serialization of ``after``;
    ``new_events`` are the events this action appended; ``action`` = {type, ...}; ``hp_provided`` is
    the Hacking Pool dice the driver told the action to spend."""
    test_success = _action_test_success(new_events)
    check_dice_rolls(new_events, ctx)
    check_no_success_without_a_hit(new_events, ctx)
    check_detection_factor(admin_state, ctx)
    check_suppression_count(admin_state, ctx)
    check_hacking_pool(before, after, hp_provided, ctx)
    check_condition_monitors(after, ctx)
    check_tally_non_negative(after, ctx)
    check_locate_marks_located(after, new_events, ctx)
    check_analyzed_never_reverts(before, after, ctx)
    check_validate_passcode(before, after, action, test_success, ctx)
