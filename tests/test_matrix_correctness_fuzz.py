"""Generative CORRECTNESS fuzz: play a random host like a decker and, after EVERY action, assert the
engine produced the result the SR2 rules demand ("I did X -> per the rules I should see Y").

This is the sibling of ``test_matrix_visibility_fuzz`` (which checks redaction). Here, after each real
endpoint call, ``matrix_correctness_oracle.check_transition`` re-derives the expected outcome from the
rules + the recorded dice and compares it to the engine's state -- so a wrong success count, a broken
rule of 6, a mis-charged Hacking Pool, a bad Detection Factor, a "located but invisible" file, or an
un-analyzed reversion FAILS the exact seed/step. A 4xx rejection is a legal "you can't do that now"
and is skipped (no post-condition); a 5xx or unhandled crash is always a bug.

Depth is env-tunable: ``MATRIX_ORACLE_SEEDS`` (default 80). Each seed is a fresh random host + a
long random action script under a fixed RNG, so a failure reproduces exactly.
"""

from __future__ import annotations

import copy
import os
import random

import pytest
from fastapi import HTTPException

from app.routers import matrix_runs as mr
from app.services import matrix_engine as eng
from app.schemas.matrix_run import (
    RunActionInput, RunAttackInput, RunEnemyAttackInput, RunEnemyScanInput, RunAreaAttackInput,
)

from tests import matrix_correctness_oracle as oracle
from tests.test_matrix_visibility_fuzz import (
    _FakeDB, _StubRun, _capable_decker, _random_host, _call,
    _pick_file, _pick_ic, _pick_enemy, _area_targets,
    DISCLOSURE_ACTIONS, STRIKE_PROGRAMS, SUBSYSTEMS, _SUBSYS_FOR, _VALID_ACTIONS,
)

AUTH_ADMIN = {"is_admin": True, "is_user": False, "user_token": None}

# One seed = one full random run, checked for RULE CORRECTNESS after every step.
FUZZ_SEEDS = list(range(1, int(os.environ.get("MATRIX_ORACLE_SEEDS", "80")) + 1))


def _run_and_check(run, action_type: str, hp: int, coro, ctx: str) -> None:
    """Snapshot the raw state, drive one endpoint, and run the correctness battery on the transition.
    A 4xx is a legal rejection (nothing to assert); a 5xx / unhandled exception propagates as a bug."""
    before = copy.deepcopy(run.state_json)
    ev_before = len(run.state_json.get("event_log") or [])
    try:
        _call(coro)
    except HTTPException as exc:
        if exc.status_code >= 500:
            raise
        return
    after = copy.deepcopy(run.state_json)
    new_events = (after.get("event_log") or [])[ev_before:]
    admin_state = mr._serialize_run(run, AUTH_ADMIN).get("state_json", {})
    oracle.check_transition(before, after, admin_state, new_events,
                            {"type": action_type}, hp, f"{ctx} action={action_type}")


def _drive_one(rng: random.Random, run, ctx: str) -> None:
    """Pick + drive one random action (with a KNOWN Hacking Pool spend the oracle can verify)."""
    state = run.state_json
    hp = rng.randint(0, 3)
    roll = rng.random()

    if roll < 0.60:
        action = rng.choice(DISCLOSURE_ACTIONS)
        if action not in _VALID_ACTIONS:
            return
        ic = _pick_ic(rng, state)
        target_file = _pick_file(rng, state)
        if action == "invalidate_passcode" and rng.random() < 0.5:
            ic = "__all__"
        subsystem = (rng.choice(SUBSYSTEMS) if action == "analyze_subsystem"
                     else _SUBSYS_FOR.get(action, "files"))
        body = RunActionInput(
            action_type=action, subsystem=subsystem, utility_rating=6, hacking_pool_dice=hp,
            target_ic_id=ic, target_file=target_file,
            target_program=rng.choice(["sleaze", "analyze", ""]),
            maneuver_target=ic, position_choice="tn")
        _run_and_check(run, action, hp,
                       mr.perform_action(run_id=1, body=body, auth=AUTH_ADMIN, db=_FakeDB()), ctx)
    elif roll < 0.72:
        ic = _pick_ic(rng, state)
        if ic:
            _run_and_check(run, "attack_ic", hp, mr.attack_ic(
                run_id=1, body=RunAttackInput(target_ic_id=ic, attack_pool=8, hacking_pool_dice=hp,
                                              armor_utility=6), auth=AUTH_ADMIN, db=_FakeDB()), ctx)
    elif roll < 0.82:
        enemy = _pick_enemy(rng, state)
        if enemy:
            _run_and_check(run, "attack_enemy_decker", hp, mr.attack_enemy_decker(
                run_id=1, body=RunEnemyAttackInput(enemy_id=enemy, attack_pool=8, hacking_pool_dice=hp,
                                                   program=rng.choice(STRIKE_PROGRAMS)),
                auth=AUTH_ADMIN, db=_FakeDB()), ctx)
    elif roll < 0.90:
        enemy = _pick_enemy(rng, state)
        if enemy:
            _run_and_check(run, "scan_enemy_decker", hp, mr.scan_enemy_decker(
                run_id=1, body=RunEnemyScanInput(enemy_id=enemy, hacking_pool_dice=hp),
                auth=AUTH_ADMIN, db=_FakeDB()), ctx)
    elif roll < 0.95:
        tids = _area_targets(state)
        if tids:
            _run_and_check(run, "area_attack", hp, mr.area_attack(
                run_id=1, body=RunAreaAttackInput(target_ids=tids, attack_pool=10, hacking_pool_dice=hp),
                auth=AUTH_ADMIN, db=_FakeDB()), ctx)
    else:
        _run_and_check(run, "new_turn", 0,
                       mr.new_turn(run_id=1, auth=AUTH_ADMIN, db=_FakeDB()), ctx)


@pytest.mark.parametrize("seed", FUZZ_SEEDS)
def test_engine_computes_rules_correctly(monkeypatch, seed):
    """One random host + a long random action script; after EVERY step the engine's result must match
    what the SR2 rules demand. A failure prints the seed + step for exact reproduction."""
    _saved_rng = random.getstate()
    try:
        random.seed(seed)
        mr.random.seed(seed)
        eng.random.seed(seed)
        rng = random.Random((seed * 2654435761) & 0xFFFFFFFF)

        decker = _capable_decker()
        host = _random_host(rng)
        state = mr._initial_state(decker, host)
        run = _StubRun(decker, state)

        async def _get(db, run_id):
            return run

        async def _get_host(db, host_id):
            return host

        monkeypatch.setattr(mr, "_get_run_or_404", _get)
        monkeypatch.setattr(mr, "_get_host_or_404", _get_host)
        monkeypatch.setattr(mr, "_assert_run_access", lambda r, a: None)

        _run_and_check(run, "logon_to_host", 2, mr.perform_action(
            run_id=1, body=RunActionInput(action_type="logon_to_host", subsystem="access",
                                          utility_rating=6, hacking_pool_dice=2),
            auth=AUTH_ADMIN, db=_FakeDB()), f"seed={seed} logon")

        for i in range(45):
            if run.status != "active" or run.state_json.get("run_ended"):
                break
            _drive_one(rng, run, f"seed={seed} step={i}")
    finally:
        random.setstate(_saved_rng)
