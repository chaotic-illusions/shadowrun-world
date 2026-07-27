"""Scenario fuzz harness -- Layer 3 of the rules-coverage program.

Where the coverage contract (tests/test_coverage_matrix.py) proves each mechanic is
*registered* and that Hog is *modelled once* for both directions, this harness proves the
whole surface actually *runs*: it drives the REAL run endpoints in app.routers.matrix_runs
against a MAXIMAL decker (every utility, Hog included, DINAB / One-Shot / Area options
spread across the programs that allow them) on a MAXIMAL host (every subsystem, a spread of
IC, paydata + a key file, a scramble, a data bomb, a trap door, plus a dispatched enemy
decker) with a seeded, reproducible RNG.

After every single step it asserts a set of structural + rules invariants:
  * every ActionType dispatches cleanly -- a success or a controlled HTTPException, never an
    unhandled Python crash;
  * persona / stun / physical condition monitors stay within 0..10;
  * Hacking Pool, program-damage ledger, and enemy ratings never go negative;
  * every Hog infection is well-formed;
  * a PLAYER serialization never leaks a GM-only state key.

Failures reproduce exactly from the printed seed. The suite is intentionally broad rather
than deep: it is the "would this actually work in a run" forcing function the project was
missing.
"""
from __future__ import annotations

import asyncio
import datetime
import random
import typing

import pytest
from fastapi import HTTPException

from app.routers import matrix_runs as mr
from app.services import matrix_engine as eng
from app.schemas.matrix_run import (
    ActionType,
    DeckerUtilities,
    RunActionInput,
    RunAreaAttackInput,
    RunAttackInput,
    RunEnemyAttackInput,
    RunEnemyScanInput,
    RunSuppressInput,
)

ACTIONS = list(typing.get_args(ActionType))
# Offensive programs the PC can hand-fire at an enemy decker (mirrors RunEnemyAttackInput).
STRIKE_PROGRAMS = ["attack", "poison", "restrict", "reveal", "hog", "black_hammer", "killjoy"]
# Utilities that may carry DINAB (mirrors the coverage RAW_DINAB_CAPABLE set).
DINAB_CAPABLE = ["attack", "hog", "poison", "restrict", "reveal", "slow",
                 "steamroller", "medic", "restore"]
SEEDS = [1, 7, 13, 42, 99, 777, 2024, 31337]

_ADMIN = {"is_admin": True, "is_user": False, "user_token": None}
_PLAYER = {"is_admin": False, "is_user": True, "user_token": "player"}

# Subsystem each action is exercised against (handlers that ignore it are unaffected).
_SUBSYS_FOR = {
    "logon_to_host": "access",
    "analyze_security": "access", "validate_passcode": "access",
    "locate_paydata": "index", "locate_ic": "index", "locate_decker": "index",
    "download_data": "files", "edit_file": "files", "decrypt_file": "files",
    "decompress_file": "files", "defuse_data_bomb": "files", "crash_host": "control",
    "redirect_datatrail": "control", "relocate": "control", "decoy": "control",
}


# -- Fakes / stub run ----------------------------------------------------------

class _FakeDB:
    """Async DB stand-in: the run is served by a monkeypatched _get_run_or_404, so no real
    query ever runs. commit / refresh are no-ops; execute returns an empty result set as a
    defensive default rather than raising."""

    async def commit(self):
        return None

    async def refresh(self, obj):
        return None

    async def execute(self, *a, **k):
        class _Empty:
            def scalars(self):
                return self

            def first(self):
                return None

            def all(self):
                return []
        return _Empty()


class _StubRun:
    """Carries exactly the attributes MatrixRunRead.model_validate reads, so the REAL
    _serialize_run (used for the GM-redaction invariant) works unmodified."""

    def __init__(self, decker: dict, state: dict):
        now = datetime.datetime.now(datetime.timezone.utc)
        self.id = 1
        self.host_id = 1
        self.status = "active"
        self.owner_token_hash = None
        self.decker_json = decker
        self.state_json = state
        self.created_at = now
        self.updated_at = now
        self.version = 1


# -- Maximal decker + host -----------------------------------------------------

def _maximal_decker() -> dict:
    util_keys = list(DeckerUtilities.model_fields.keys())
    utilities = {k: 6 for k in util_keys}
    program_options: dict[str, dict] = {}
    for k in DINAB_CAPABLE:
        program_options[k] = {"dinab": 4, "targeting": True}
    # Attack also carries Area + Penetration so the /area-attack burst path is reachable.
    program_options["attack"] = {"dinab": 4, "targeting": True, "area": 3, "penetration": True}
    # Poison is One-Shot so the one-shot spend/block path gets exercised.
    program_options["poison"] = {"dinab": 4, "one_shot": True}
    program_sizes = {k: 6 for k in util_keys}
    return {
        "name": "Fuzz Ghost",
        "mpcp": 12, "bod": 12, "evasion": 12, "masking": 12, "sensor": 12,
        "computer_skill": 12, "intelligence": 6, "quickness": 6, "willpower": 6, "body": 6,
        "deck_mode": "hot", "iccm": True, "hardening": 3, "response_increase": 3,
        "active_memory": 5000, "io_speed": 200,
        "trace_factor": 0, "bandwidth_modifier": 0, "base_bandwidth": 100,
        "access_modifier": 0, "console_access": False,
        "reaction_modifier": 0, "physical_trace_immune": False,
        "storage_free_mp": 5000, "linked_passcode": True,
        "utilities": utilities,
        "program_sizes": program_sizes,
        "program_options": program_options,
        "storage_programs": [
            {"name": "sleaze", "rating": 6, "size": 6},
            {"name": "analyze", "rating": 6, "size": 6},
        ],
    }


def _maximal_host():
    cfg = {
        "security_code": "Red",
        "security_value": 9,
        "acifs": [10, 10, 10, 10, 10],
        "sheaf": [],
        "paydata": [
            {"name": "payroll.db", "density": 40, "is_key": False, "defense": 0, "located": True},
            {"name": "black_files", "density": 80, "is_key": True, "defense": 0, "located": True},
        ],
        "scrambles": [
            {"target_key": "files::black_files", "rating": 6, "variant": "poison",
             "discovered": True},
        ],
        "data_bombs": [
            {"target": "files::black_files", "rating": 6, "discovered": True},
        ],
        "slave_pieces": ["maglock", "camera"],
    }
    return typing.cast(mr.MatrixHost, _HostNS(cfg))


class _HostNS:
    def __init__(self, cfg: dict):
        self.id = 1
        self.name = "Fuzz Host"
        self.config_json = cfg
        self.ltg_address = "LTG-1-800-FUZZ"
        self.is_visible_to_players = True
        self.trap_doors_json = [
            {"id": "td1", "source_piece": "maglock", "subsystem": "slave",
             "destination_host_id": None, "destination_ltg": "", "destination_label": "??"},
        ]


def _fresh_run() -> _StubRun:
    """Boot a maximal run mid-engagement: logged on, a spread of IC placed, one enemy decker
    dispatched and revealed. Assumes the caller has already pointed mr.random / eng.random at a
    seeded Random so the whole boot is reproducible."""
    decker = _maximal_decker()
    host = _maximal_host()
    state = mr._initial_state(decker, host)
    sec = state["host_security_code"]
    state["logon_complete"] = True
    # Place a spread of IC so IC-attack / crippler-Restore / tar-Steamroller / Trace all resolve.
    for ic_type in ("Killer", "Acid", "Tar Baby", "Worm", "Trace", "Black IC"):
        step = {"trigger": 0, "events": [{"type": "ic", "ic_type": ic_type, "rating": 6}]}
        mr._activate_sheaf_step(state, step, sec)
    # Dispatch and reveal a security decker so Strike Back / Hog have a live target.
    enemy = mr._spawn_enemy_decker(state, sec)
    enemy["revealed"] = True
    return _StubRun(decker, state)


# -- Target pickers ------------------------------------------------------------

def _first_active_ic(state: dict) -> str:
    for ic in state.get("active_ic", []):
        if isinstance(ic, dict) and ic.get("status") == "active" and ic.get("id"):
            return str(ic["id"])
    return ""


def _first_revealed_enemy(state: dict) -> str:
    for e in state.get("enemy_deckers", []):
        if isinstance(e, dict) and e.get("status") == "active" and e.get("revealed") and e.get("id"):
            return str(e["id"])
    return ""


def _area_targets(state: dict, limit: int = 3) -> list[str]:
    ids = [str(ic["id"]) for ic in state.get("active_ic", [])
           if isinstance(ic, dict) and ic.get("status") == "active" and ic.get("id")]
    return ids[:limit]


def _action_input(action: str, state: dict) -> RunActionInput:
    ic = _first_active_ic(state)
    enemy = _first_revealed_enemy(state)
    target_file = ""
    if action == "decrypt_file":
        target_file = "files::black_files"
    elif action in ("download_data", "edit_file", "decompress_file"):
        target_file = "payroll.db"
    elif action == "defuse_data_bomb":
        target_file = "black_files"
    target_program = ""
    if action == "swap_memory":
        target_program = "sleaze"
    elif action == "unload_program":
        target_program = "analyze"
    elif action == "purge_hog":
        target_program = "analyze"
    elif action == "restore":
        target_program = "bod"
    return RunActionInput(
        action_type=action,
        subsystem=_SUBSYS_FOR.get(action, "files"),
        utility_rating=6,
        hacking_pool_dice=1,
        target_ic_id=ic,
        target_file=target_file,
        target_program=target_program,
        maneuver_target=(ic or enemy),
        position_choice="tn",
    )


# -- Invariants ----------------------------------------------------------------

def _assert_invariants(run: _StubRun, seed) -> None:
    state = run.state_json
    ctx = f"(seed={seed})"
    assert isinstance(state, dict), ctx
    assert isinstance(state.get("event_log"), list), ctx
    cm = state.get("condition_monitor") or {}
    for k in ("persona_boxes", "stun_boxes", "physical_boxes"):
        v = cm.get(k, 0) or 0
        assert 0 <= v <= 10, f"{k}={v} out of 0..10 {ctx}"
    assert (state.get("hackingPool_remaining", 0) or 0) >= 0, ctx
    for k, v in (state.get("program_damage") or {}).items():
        assert (v or 0) >= 0, f"program_damage[{k}]={v} {ctx}"
    for e in state.get("enemy_deckers", []):
        for attr in ("bod", "evasion", "masking", "sensor", "mpcp"):
            if attr in e:
                assert (e[attr] or 0) >= 0, f"enemy {attr}={e.get(attr)} {ctx}"
        for uk, uv in (e.get("utilities") or {}).items():
            assert (uv or 0) >= 0, f"enemy util {uk}={uv} {ctx}"
    for inf in (state.get("hog_infections") or []):
        assert {"id", "attacker_id", "target_id", "rating", "drain"} <= set(inf), \
            f"malformed hog infection {inf} {ctx}"
        assert (inf.get("drain", 0) or 0) >= 0, ctx
    # GM redaction: a player serialization must leak no GM-only state key.
    view = mr._serialize_run(run, _PLAYER)
    pstate = view.get("state_json") or {}
    leaked = mr._GM_ONLY_STATE_KEYS & set(pstate)
    assert not leaked, f"GM-only keys leaked to player: {leaked} {ctx}"


def _call(coro) -> bool:
    """Drive one endpoint coroutine. A controlled HTTPException (illegal-in-context action) is
    an acceptable outcome; anything else propagates as a real bug."""
    try:
        asyncio.run(coro)
        return True
    except HTTPException:
        return False


# -- Tests ---------------------------------------------------------------------

def test_every_action_dispatches_cleanly(monkeypatch):
    """Every ActionType, fired once against a fresh maximal run, either succeeds or raises a
    controlled HTTPException -- it must never raise an unhandled exception -- and leaves the run
    state satisfying every invariant."""
    for i, action in enumerate(ACTIONS):
        rng = random.Random(1000 + i)
        monkeypatch.setattr(mr, "random", rng)
        monkeypatch.setattr(eng, "random", rng)
        run = _fresh_run()

        async def _get(db, run_id, _r=run):
            return _r
        monkeypatch.setattr(mr, "_get_run_or_404", _get)

        _call(mr.perform_action(run_id=1, body=_action_input(action, run.state_json),
                                auth=_ADMIN, db=_FakeDB()))
        _assert_invariants(run, f"action={action}")


@pytest.mark.parametrize("seed", SEEDS)
def test_random_run_sequences_preserve_invariants(monkeypatch, seed):
    """A long randomized sequence of mixed endpoint calls (system ops, IC cybercombat, enemy-
    decker Strike Back incl. Hog, Area bursts, end-of-pass) keeps every invariant true after
    every step, for each seed."""
    rng = random.Random(seed)
    monkeypatch.setattr(mr, "random", rng)
    monkeypatch.setattr(eng, "random", rng)
    run = _fresh_run()

    async def _get(db, run_id):
        return run
    monkeypatch.setattr(mr, "_get_run_or_404", _get)

    _assert_invariants(run, seed)
    for _ in range(80):
        if run.status != "active" or run.state_json.get("run_ended"):
            break
        roll = rng.random()
        if roll < 0.50:
            body = _action_input(rng.choice(ACTIONS), run.state_json)
            _call(mr.perform_action(run_id=1, body=body, auth=_ADMIN, db=_FakeDB()))
        elif roll < 0.62:
            ic = _first_active_ic(run.state_json)
            if ic:
                _call(mr.attack_ic(run_id=1, body=RunAttackInput(
                    target_ic_id=ic, attack_pool=8, hacking_pool_dice=1, armor_utility=6),
                    auth=_ADMIN, db=_FakeDB()))
        elif roll < 0.74:
            e = _first_revealed_enemy(run.state_json)
            if e:
                _call(mr.attack_enemy_decker(run_id=1, body=RunEnemyAttackInput(
                    enemy_id=e, attack_pool=8, hacking_pool_dice=1,
                    program=rng.choice(STRIKE_PROGRAMS)), auth=_ADMIN, db=_FakeDB()))
        elif roll < 0.80:
            e = _first_revealed_enemy(run.state_json)
            if e:
                _call(mr.scan_enemy_decker(run_id=1, body=RunEnemyScanInput(
                    enemy_id=e, hacking_pool_dice=1), auth=_ADMIN, db=_FakeDB()))
        elif roll < 0.88:
            tids = _area_targets(run.state_json)
            if tids:
                _call(mr.area_attack(run_id=1, body=RunAreaAttackInput(
                    target_ids=tids, attack_pool=10, hacking_pool_dice=1),
                    auth=_ADMIN, db=_FakeDB()))
        else:
            _call(mr.new_turn(run_id=1, auth=_ADMIN, db=_FakeDB()))
        _assert_invariants(run, seed)


def test_manual_hog_strike_seeds_enemy_infection(monkeypatch):
    """The PC's manual Hog Strike Back seeds a persistent infection ON THE ENEMY (attacker=pc),
    proving Hog is reachable in the PC->enemy direction through the same resolver the enemy uses
    against the PC."""
    rng = random.Random(4)
    monkeypatch.setattr(mr, "random", rng)
    monkeypatch.setattr(eng, "random", rng)
    # Force a deterministic hit so the branch resolves regardless of dice.
    monkeypatch.setattr(mr.eng, "hog_attack", lambda **kw: {
        "attack_roll": {"successes": 3, "ones": 0}, "resist_roll": {"successes": 0},
        "net": 4, "reduction": 2})
    run = _fresh_run()
    enemy_id = _first_revealed_enemy(run.state_json)
    assert enemy_id, "harness failed to dispatch a revealed enemy decker"

    async def _get(db, run_id):
        return run
    monkeypatch.setattr(mr, "_get_run_or_404", _get)

    body = RunEnemyAttackInput(enemy_id=enemy_id, attack_pool=8, hacking_pool_dice=0, program="hog")
    asyncio.run(mr.attack_enemy_decker(run_id=1, body=body, auth=_ADMIN, db=_FakeDB()))

    infections = [i for i in run.state_json.get("hog_infections", [])
                  if i.get("target_id") == enemy_id]
    assert infections, "manual Hog strike did not seed an infection on the enemy"
    assert infections[0]["attacker_id"] == "pc"
    assert infections[0]["drain"] == 2
    _assert_invariants(run, "manual-hog")


def test_hacking_pool_not_refilled_out_of_combat(monkeypatch):
    """Strict SR2 RAW regression: spending Hacking Pool dice on an action does NOT top the pool
    back up, even with no IC present -- it refreshes only at pass/turn boundaries
    (_reset_pass_budget). Guards the removed 'out-of-combat HP is free' auto-refill block."""
    # Leave the process-wide random stream exactly as found: a couple of downstream scenario tests
    # depend on the un-reseeded global RNG history, so this test must not consume from it.
    _global_rng = random.getstate()
    try:
        rng = random.Random(4242)
        monkeypatch.setattr(mr, "random", rng)
        monkeypatch.setattr(eng, "random", rng)

        decker = _maximal_decker()
        host = _maximal_host()
        state = mr._initial_state(decker, host)
        state["logon_complete"] = True
        # The old auto-refill fired precisely when no IC (active or lurking) remained.
        state["active_ic"] = []
        state["lurking_ic"] = []
        state["hackingPool_total"] = 6
        state["hackingPool_remaining"] = 6
        run = _StubRun(decker, state)

        async def _get(db, run_id):
            return run
        monkeypatch.setattr(mr, "_get_run_or_404", _get)

        # analyze_security spends 1 Hacking Pool die and never re-queries the host from the DB, so
        # it drives the full perform_action path (write-back included) against the stub run.
        _call(mr.perform_action(run_id=1, body=_action_input("analyze_security", state),
                                auth=_ADMIN, db=_FakeDB()))
        # Spent 1 of 6; strict RAW leaves 5 -- the pool must NOT be topped back up to 6.
        assert run.state_json["hackingPool_remaining"] == 5
    finally:
        random.setstate(_global_rng)
def _probe_run(monkeypatch, *, active_ic, sheaf, action_tally, probe_tally, seed):
    """Drive one analyze_security action through the REAL perform_action with system_test and
    probe_test stubbed to fixed outcomes, so a Probe Test's tally contribution is unmistakable.
    Returns the post-action state_json. Isolates the global RNG (a couple of downstream scenario
    tests depend on the un-reseeded stream) and disables enemy-decker spawns for a clean tally."""
    rng = random.Random(seed)
    monkeypatch.setattr(mr, "random", rng)
    monkeypatch.setattr(eng, "random", rng)
    decker = _maximal_decker()
    host = _maximal_host()
    state = mr._initial_state(decker, host)
    state["logon_complete"] = True
    state["security_tally"] = 0
    state["enemy_decker_cap"] = 0            # no probabilistic enemy-decker spawns muddying the tally
    state["active_ic"] = active_ic
    state["sheaf"] = sheaf
    state["sheaf_steps_triggered"] = []
    run = _StubRun(decker, state)
    monkeypatch.setattr(eng, "system_test", lambda **kw: {
        "success": False, "decker_net_successes": 0, "tally_increase": action_tally,
        "decker_roll": {"successes": 0, "ones": 0}, "host_roll": {"successes": action_tally, "ones": 0}})
    monkeypatch.setattr(eng, "probe_test", lambda ic_rating, det_factor: {
        "tally_increase": probe_tally, "roll": {"successes": probe_tally, "ones": 0}})

    async def _get(db, run_id):
        return run
    monkeypatch.setattr(mr, "_get_run_or_404", _get)

    _call(mr.perform_action(run_id=1, body=_action_input("analyze_security", state),
                            auth=_ADMIN, db=_FakeDB()))
    return run.state_json


def test_probe_ic_does_not_test_the_action_that_spawns_it(monkeypatch):
    """vr2_rules.md L485: a Probe IC makes a Probe Test for every System Test the decker makes, but
    only one it was ALREADY watching. A Probe that first activates as a consequence of THIS action
    (its tally bump crossing a sheaf step) must NOT test the very action that spawned it -- it starts
    probing next action. Regression for the 'Probe fires on activation' bug that double-counted the
    triggering action's tally."""
    _global_rng = random.getstate()
    try:
        st = _probe_run(
            monkeypatch,
            active_ic=[],                                   # no Probe watching when the test is made
            sheaf=[{"trigger": 2, "events": [{"type": "ic", "ic_type": "Probe", "rating": 6}]}],
            action_tally=2,                                 # the action itself crosses the sheaf at 2
            probe_tally=5,                                  # a very loud probe, so the bug can't hide
            seed=2027,
        )
        # The Probe DID activate this action...
        assert any(ic.get("type") == "Probe" for ic in st["active_ic"])
        # ...but it did NOT test this action: tally rose by the action's 2 only, not 2 + probe 5,
        # and no probe_ic event fired.
        assert st["security_tally"] == 2
        assert not [e for e in st["event_log"] if e.get("type") == "probe_ic"]
    finally:
        random.setstate(_global_rng)


def test_active_probe_ic_tests_each_system_test(monkeypatch):
    """Baseline direction of the timing fix: a Probe IC that is ALREADY active when the decker makes
    a System Test DOES make its Probe Test and adds the successes to the security tally."""
    _global_rng = random.getstate()
    try:
        st = _probe_run(
            monkeypatch,
            active_ic=[{"id": "probe_pre", "type": "Probe", "rating": 6, "category": "white",
                        "status": "active", "suppressed": False, "initiative": 5,
                        "detection_level": 3, "analyzed": True}],
            sheaf=[],
            action_tally=0,                                 # the action itself adds nothing
            probe_tally=3,                                  # the pre-existing probe adds 3
            seed=2029,
        )
        assert [e for e in st["event_log"] if e.get("type") == "probe_ic"]
        assert st["security_tally"] == 3                    # action +0, pre-existing probe +3
    finally:
        random.setstate(_global_rng)


def test_sheaf_spawned_ic_does_not_act_on_the_spawning_action(monkeypatch):
    """vr2 initiative: an IC that first activates as a consequence of the decker's action (its tally
    bump crossing a sheaf step) has not yet reached its own initiative segment, so it must not act in
    the same action it spawned. A lower, still-upcoming count is marked pending until End Turn;
    a count that already passed waits until the next round."""
    _global_rng = random.getstate()
    try:
        rng = random.Random(3131)
        monkeypatch.setattr(mr, "random", rng)
        monkeypatch.setattr(eng, "random", rng)
        decker = _maximal_decker()
        host = _maximal_host()
        state = mr._initial_state(decker, host)
        state["logon_complete"] = True
        state["security_tally"] = 0
        state["enemy_decker_cap"] = 0            # no enemy-decker spawns muddying the pass
        state["active_ic"] = []
        state["current_pass"] = 1
        # A sheaf step that spawns a proactive Killer IC the moment the tally reaches 2.
        state["sheaf"] = [{"trigger": 2, "events": [{"type": "ic", "ic_type": "Killer", "rating": 6}]}]
        state["sheaf_steps_triggered"] = []
        run = _StubRun(decker, state)
        # The action fails and bumps the tally by 2 -> crosses the sheaf -> spawns the Killer.
        monkeypatch.setattr(eng, "system_test", lambda **kw: {
            "success": False, "decker_net_successes": 0, "tally_increase": 2,
            "decker_roll": {"successes": 0, "ones": 0}, "host_roll": {"successes": 2, "ones": 0}})

        async def _get(db, run_id):
            return run
        monkeypatch.setattr(mr, "_get_run_or_404", _get)

        _call(mr.perform_action(run_id=1, body=_action_input("analyze_security", state),
                                auth=_ADMIN, db=_FakeDB()))
        st = run.state_json
        killers = [ic for ic in st["active_ic"] if ic["type"] == "Killer"]
        assert killers, "the sheaf step should have spawned the Killer IC"
        # Held back from the spawning action; because its count is lower than the decker's, End
        # Turn may release it later in this same pass.
        assert killers[0].get("spawn_pending_pass") == st.get("current_pass", 1)
        # ...and it launched no cybercombat on the action that spawned it.
        assert not [e for e in st["event_log"]
                    if e.get("type") == "ic_attack" and e.get("ic_type") == "Killer"]
    finally:
        random.setstate(_global_rng)


def test_spawn_holdback_uses_current_initiative_count():
    state = {
        "current_pass": 1,
        "decker_initiative": 23,
        "active_ic": [
            {"id": "upcoming", "initiative": 12, "status": "active"},
            {"id": "missed", "initiative": 24, "status": "active"},
        ],
        "enemy_deckers": [],
    }

    mr._hold_back_new_hostiles(state, set(), set())

    upcoming, missed = state["active_ic"]
    assert upcoming["spawn_pending_pass"] == 1
    assert "acted_pass" not in upcoming
    assert missed["acted_pass"] == 1
    assert missed["actions_taken_turn"] == 1        # missed i24
    assert missed["spawn_pending_pass"] == 1        # but i14 is still upcoming

    mr._release_spawned_hostiles_for_pass(state, 1)

    assert "spawn_pending_pass" not in upcoming
    assert "spawn_pending_pass" not in missed
    assert missed["acted_pass"] == 1


def test_logon_starts_first_round_on_shared_initiative_clock(monkeypatch):
    decker = _maximal_decker()
    state = mr._initial_state(decker, _maximal_host())
    state.update({
        "logon_complete": False,
        "decker_initiative": 20,
        "initiative_passes": 2,
        "current_pass": 1,
        "sheaf": [],
        "active_ic": [
            {"id": "fast", "type": "Trace", "rating": 5, "status": "active",
             "initiative": 24, "boxes": 0, "trace_phase": "hunt", "analyzed": True},
            {"id": "slow", "type": "Trace", "rating": 5, "status": "active",
             "initiative": 13, "boxes": 0, "trace_phase": "hunt", "analyzed": True},
        ],
        "enemy_deckers": [],
        "event_log": [],
    })
    state["condition_monitor"]["persona_boxes"] = 1     # effective player initiative 19
    run = _StubRun(decker, state)

    async def _get(db, run_id):
        return run

    monkeypatch.setattr(mr, "_get_run_or_404", _get)
    monkeypatch.setattr(eng, "system_test", lambda **kwargs: {
        "success": True, "decker_net_successes": 1, "tally_increase": 0,
        "decker_roll": {"successes": 1, "ones": 0},
        "host_roll": {"successes": 0, "ones": 0},
    })
    monkeypatch.setattr(eng, "trace_hunt_cycle_attack", lambda *args, **kwargs: {
        "hit": False, "roll": {"successes": 0, "ones": 0},
    })

    asyncio.run(mr.perform_action(
        run_id=1,
        body=RunActionInput(
            action_type="logon_to_host", subsystem="access", utility_rating=6,
            hacking_pool_dice=0,
        ),
        auth=_ADMIN,
        db=_FakeDB(),
    ))

    attacks = [event for event in run.state_json["event_log"] if event.get("type") == "ic_attack"]
    assert [(event["ic_id"], event["init"]) for event in attacks] == [("fast", 24)]
    active = {ic["id"]: ic for ic in run.state_json["active_ic"]}
    assert active["fast"]["actions_taken_turn"] == 1
    assert "actions_taken_turn" not in active["slow"]
    assert run.state_json["logon_complete"] is True
    assert run.state_json["pass_action_points"] == 2


def test_relocate_suppress_pauses_trace_in_place_and_release_resumes(monkeypatch):
    """vr2 L588: a won Relocate lets the decker SUPPRESS the trace IC. When suppress_trace=True the
    trace is paused IN PLACE (its trace_phase / location-cycle remaining are untouched -- NOT reset
    to hunt), costs 1 Detection Factor, and takes no further action while suppressed. Releasing it
    resumes the trace exactly where it left off (no tally, re-suppressible -- not the one-way crash
    mode)."""
    _global_rng = random.getstate()
    try:
        rng = random.Random(4242)
        monkeypatch.setattr(mr, "random", rng)
        monkeypatch.setattr(eng, "random", rng)
        decker = _maximal_decker()
        host = _maximal_host()
        state = mr._initial_state(decker, host)
        state["logon_complete"] = True
        state["security_tally"] = 0
        state["enemy_decker_cap"] = 0
        state["current_pass"] = 1
        # An active Trace IC mid location-cycle -- exactly what Relocate is used to shake.
        state["active_ic"] = [{
            "id": "trace_1", "type": "Trace", "rating": 5, "category": "white",
            "status": "active", "suppressed": False, "initiative": 10, "acted_pass": 1,
            "analyzed": True, "trace_phase": "locate", "trace_locate_remaining": 3,
        }]
        run = _StubRun(decker, state)
        df_before = mr._effective_detection_factor(state, decker)
        # Force the Relocate's opposed Control test to WIN.
        monkeypatch.setattr(eng, "system_test", lambda **kw: {
            "success": True, "decker_net_successes": 3, "tally_increase": 0,
            "decker_roll": {"successes": 3, "ones": 0}, "host_roll": {"successes": 0, "ones": 0}})

        async def _get(db, run_id):
            return run
        monkeypatch.setattr(mr, "_get_run_or_404", _get)

        body = _action_input("relocate", state)
        body = body.model_copy(update={"suppress_trace": True})
        _call(mr.perform_action(run_id=1, body=body, auth=_ADMIN, db=_FakeDB()))
        st = run.state_json
        trace = next(ic for ic in st["active_ic"] if ic["id"] == "trace_1")
        # Suppressed in place: paused, mode=trace, phase and location-cycle remaining untouched.
        assert trace.get("suppressed") is True
        assert trace.get("suppress_mode") == "trace"
        assert trace.get("trace_phase") == "locate"          # NOT reset to hunt
        assert trace.get("trace_locate_remaining") == 3
        assert not trace.get("suppression_released")         # re-suppressible, not one-way
        # 1 Detection Factor cost while suppressed.
        assert mr._effective_detection_factor(st, decker) == df_before - 1

        # Release it: resumes in place, no tally change, no one-way lock.
        _call(mr.suppress_ic(run_id=1, body=RunSuppressInput(ic_id="trace_1", release=True),
                             auth=_ADMIN, db=_FakeDB()))
        st = run.state_json
        trace = next(ic for ic in st["active_ic"] if ic["id"] == "trace_1")
        assert trace.get("suppressed") is False
        assert "suppress_mode" not in trace
        assert not trace.get("suppression_released")         # still re-suppressible
        assert trace.get("trace_phase") == "locate"          # resumed exactly where it left off
        assert mr._effective_detection_factor(st, decker) == df_before
    finally:
        random.setstate(_global_rng)


def test_relocate_df_floor_falls_back_to_spoof(monkeypatch):
    """A Relocate SUPPRESS costs 1 Detection Factor and DF cannot be spent below its floor of 1.
    When the won Relocate test asks to suppress but the decker is already at the DF floor, the trace
    must NOT be suppressed for free -- the won test instead falls back to the no-DF-cost spoof-for-
    this-turn outcome and tells the decker to release a suppression first."""
    _global_rng = random.getstate()
    try:
        rng = random.Random(9191)
        monkeypatch.setattr(mr, "random", rng)
        monkeypatch.setattr(eng, "random", rng)
        decker = _maximal_decker()
        host = _maximal_host()
        state = mr._initial_state(decker, host)
        state["logon_complete"] = True
        state["security_tally"] = 0
        state["enemy_decker_cap"] = 0
        state["current_pass"] = 1
        state["current_turn"] = 2
        state["active_ic"] = [{
            "id": "trace_1", "type": "Trace", "rating": 5, "category": "white",
            "status": "active", "suppressed": False, "initiative": 10, "acted_pass": 1,
            "analyzed": True, "trace_phase": "locate", "trace_locate_remaining": 3,
        }]
        run = _StubRun(decker, state)
        # Force DF to already be at its floor -- no point left to spend on a suppression.
        monkeypatch.setattr(mr, "_base_detection_factor", lambda s, d: 1)
        monkeypatch.setattr(eng, "system_test", lambda **kw: {
            "success": True, "decker_net_successes": 3, "tally_increase": 0,
            "decker_roll": {"successes": 3, "ones": 0}, "host_roll": {"successes": 0, "ones": 0}})

        async def _get(db, run_id):
            return run
        monkeypatch.setattr(mr, "_get_run_or_404", _get)

        body = _action_input("relocate", state)
        body = body.model_copy(update={"suppress_trace": True})
        _call(mr.perform_action(run_id=1, body=body, auth=_ADMIN, db=_FakeDB()))
        st = run.state_json
        trace = next(ic for ic in st["active_ic"] if ic["id"] == "trace_1")
        # Not suppressed (no DF to spend); spoofed for this turn AND the suppress offer is HELD open
        # (surfaced in the SUPPRESSIONS panel) so the decker can free a DF point and take it later.
        assert not trace.get("suppressed")
        assert "suppress_mode" not in trace
        assert trace.get("trace_spoofed_turn") == 2
        assert trace.get("relocate_suppress_pending") is True
    finally:
        random.setstate(_global_rng)


def test_relocate_held_suppress_offer_taken_after_freeing_df(monkeypatch):
    """The held Relocate suppress offer (relocate_suppress_pending) can be TAKEN once the decker frees
    a DF point: releasing another suppression restores 1 DF, then Suppress on the held trace converts
    it into a real trace-pause (suppress_mode='trace', spoof upgraded to a full pause)."""
    _global_rng = random.getstate()
    try:
        rng = random.Random(9292)
        monkeypatch.setattr(mr, "random", rng)
        monkeypatch.setattr(eng, "random", rng)
        decker = _maximal_decker()
        host = _maximal_host()
        state = mr._initial_state(decker, host)
        state["logon_complete"] = True
        state["security_tally"] = 0
        state["enemy_decker_cap"] = 0
        state["current_pass"] = 1
        state["current_turn"] = 2
        # A crashed IC already suppressed (occupying the DF), plus a locating trace with the HELD
        # Relocate suppress offer. DF is at the floor until the crashed IC is released.
        state["active_ic"] = [
            {"id": "crash_1", "type": "Killer", "rating": 4, "category": "black",
             "status": "crashed", "suppressed": True, "crash_tally": 4},
            {"id": "trace_1", "type": "Trace", "rating": 5, "category": "white",
             "status": "active", "suppressed": False, "trace_phase": "locate",
             "trace_locate_remaining": 3, "trace_spoofed_turn": 2, "relocate_suppress_pending": True},
        ]
        run = _StubRun(decker, state)

        async def _get(db, run_id):
            return run
        monkeypatch.setattr(mr, "_get_run_or_404", _get)
        # Force a low base DF so one suppressed IC sits at the floor (DF 2 - 1 suppressed = 1).
        monkeypatch.setattr(mr, "_base_detection_factor", lambda s, d: 2)

        # Suppressing the held trace while still at the floor must be rejected.
        with pytest.raises(HTTPException):
            mr._toggle_ic_suppression(state, decker, ic_id="trace_1", release=False)

        # Release the crashed IC -> frees 1 DF.
        mr._toggle_ic_suppression(state, decker, ic_id="crash_1", release=True)
        # Now the held trace offer can be taken.
        mr._toggle_ic_suppression(state, decker, ic_id="trace_1", release=False)
        trace = next(ic for ic in state["active_ic"] if ic["id"] == "trace_1")
        assert trace.get("suppressed") is True
        assert trace.get("suppress_mode") == "trace"
        assert not trace.get("relocate_suppress_pending")
        assert "trace_spoofed_turn" not in trace   # upgraded from per-turn spoof to a full pause
    finally:
        random.setstate(_global_rng)


def test_relocate_spoofs_one_trace_for_the_turn_without_resetting_it(monkeypatch):
    """vr2 L588 + Relocate utility: a won Relocate (without suppress_trace) SPOOFS one trace IC in its
    location cycle FOR THAT TURN ONLY -- it makes no location-cycle progress this turn but is NOT reset
    to its hunt cycle, and it targets a SINGLE trace even when several are hunting. Regression for the
    old (incorrect) 'reset every locating trace back to Hunt' behavior."""
    _global_rng = random.getstate()
    try:
        rng = random.Random(4343)
        monkeypatch.setattr(mr, "random", rng)
        monkeypatch.setattr(eng, "random", rng)
        decker = _maximal_decker()
        host = _maximal_host()
        state = mr._initial_state(decker, host)
        state["logon_complete"] = True
        state["security_tally"] = 0
        state["enemy_decker_cap"] = 0
        state["current_pass"] = 1
        state["current_turn"] = 4
        # TWO traces mid location-cycle; Relocate should touch only the targeted one.
        state["active_ic"] = [
            {"id": "trace_a", "type": "Trace", "rating": 5, "category": "white",
             "status": "active", "suppressed": False, "initiative": 10, "acted_pass": 1,
             "analyzed": True, "trace_phase": "locate", "trace_locate_remaining": 3},
            {"id": "trace_b", "type": "Trace", "rating": 6, "category": "white",
             "status": "active", "suppressed": False, "initiative": 9, "acted_pass": 1,
             "analyzed": True, "trace_phase": "locate", "trace_locate_remaining": 2},
        ]
        run = _StubRun(decker, state)
        monkeypatch.setattr(eng, "system_test", lambda **kw: {
            "success": True, "decker_net_successes": 3, "tally_increase": 0,
            "decker_roll": {"successes": 3, "ones": 0}, "host_roll": {"successes": 0, "ones": 0}})

        async def _get(db, run_id):
            return run
        monkeypatch.setattr(mr, "_get_run_or_404", _get)

        body = _action_input("relocate", state)
        body = body.model_copy(update={"target_ic_id": "trace_a"})
        _call(mr.perform_action(run_id=1, body=body, auth=_ADMIN, db=_FakeDB()))
        st = run.state_json
        ta = next(ic for ic in st["active_ic"] if ic["id"] == "trace_a")
        tb = next(ic for ic in st["active_ic"] if ic["id"] == "trace_b")
        # Targeted trace: spoofed for THIS turn, still in its location cycle, countdown untouched.
        assert ta.get("trace_spoofed_turn") == st.get("current_turn")
        assert ta.get("trace_phase") == "locate"             # NOT reset to hunt
        assert ta.get("trace_locate_remaining") == 3
        assert not ta.get("suppressed")
        # The OTHER trace is entirely unaffected (single-target).
        assert tb.get("trace_spoofed_turn") is None
        assert tb.get("trace_phase") == "locate"
        assert tb.get("trace_locate_remaining") == 2
    finally:
        random.setstate(_global_rng)
