"""Generative VISIBILITY fuzzer -- the bug-DISCOVERY layer of the E2E harness.

Where tests/test_matrix_visibility_e2e.py pins the KNOWN playtest bugs, this harness hunts for
the ones nobody has found yet. It does that the only way a finite team can cover an infinite
state space: property-based fuzzing. For each seed it

  1. builds a RANDOM host (random security code / ACIFS / paydata mix / scramble variants / data
     bombs / slave pieces / IC spread) and a capable decker,
  2. logs on for real, then drives a long RANDOM sequence of real endpoint calls, and
  3. after EVERY step runs the full admin-vs-player invariant battery
     (tests/matrix_visibility_invariants.check_all).

Any invariant violation -- a GM secret reaching the player, an admin seeing fewer files than the
player, a size leaking before Analyze Icon, a serialization crash, corrupt state -- fails the test
with the exact ``seed`` + ``step`` so it reproduces deterministically. The RNG is a per-seed
random.Random monkeypatched over mr.random / eng.random, so a red run is a recipe, not a fluke.

Design + roadmap: docs/matrix-e2e-visibility-harness.md.
"""

from __future__ import annotations

import asyncio
import datetime
import os
import random
import typing

import pytest
from fastapi import HTTPException

from app.routers import matrix_runs as mr
from app.schemas.matrix_run import (
    ActionType, DeckerUtilities, RunActionInput, RunAreaAttackInput, RunAttackInput,
    RunEnemyAttackInput, RunEnemyScanInput,
)

from tests import matrix_visibility_invariants as inv

# One seed = one full random run. Broad rather than deep; each seed is a distinct host + script.
# Default 128 seeds sweeps a wide space each CI run; for a deeper hunt set MATRIX_FUZZ_SEEDS
# (e.g. 1000) -- every added seed is a brand-new host + action stream.
FUZZ_SEEDS = list(range(1, int(os.environ.get("MATRIX_FUZZ_SEEDS", "80")) + 1))

SECURITY_CODES = ["Blue", "Green", "Orange", "Red"]
SUBSYSTEMS = ["access", "files", "slave", "index", "control"]
SCRAMBLE_VARIANTS = [None, "poison", "exploding"]
SLAVE_PIECES = ["camera", "maglock", "sensor", "turnstile", "elevator"]
IC_TYPES = ["Probe", "Killer", "Acid", "Marker", "Tar Baby", "Trace", "Worm", "Black IC"]
WORM_VARIANTS = ["deathworm", "tapeworm"]
# Offensive programs the PC can hand-fire at an enemy decker (mirrors RunEnemyAttackInput).
STRIKE_PROGRAMS = ["attack", "poison", "restrict", "reveal", "hog", "black_hammer", "killjoy"]

# Actions driven through /action. Reveal-heavy on purpose: those are the paths that gate disclosure.
DISCLOSURE_ACTIONS = [
    "analyze_host", "analyze_security", "analyze_subsystem", "locate_paydata", "locate_file",
    "locate_ic", "locate_decker", "analyze_icon", "decrypt_file", "download_data", "edit_file",
    "defuse_data_bomb", "decompress_file", "validate_passcode", "invalidate_passcode",
    "crash_host", "redirect_datatrail", "relocate", "decoy", "null_operation",
]
_SUBSYS_FOR = {
    "logon_to_host": "access", "analyze_security": "access", "validate_passcode": "access",
    "locate_paydata": "index", "locate_file": "index", "locate_ic": "index",
    "locate_decker": "index", "download_data": "files", "edit_file": "files",
    "decrypt_file": "files", "decompress_file": "files", "defuse_data_bomb": "files",
    "crash_host": "control", "redirect_datatrail": "control", "relocate": "control",
    "decoy": "control",
}
_VALID_ACTIONS = set(typing.get_args(ActionType))


# --------------------------------------------------------------------------- fakes
class _FakeDB:
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
        self.aar_acknowledged = False


class _HostNS:
    def __init__(self, cfg: dict, trap_doors=None):
        self.id = 1
        self.name = "Fuzz Vault"
        self.config_json = cfg
        self.ltg_address = "LTG-FUZZ"
        self.is_visible_to_players = True
        self.trap_doors_json = trap_doors


# --------------------------------------------------------------------------- generators
def _capable_decker() -> dict:
    util_keys = list(DeckerUtilities.model_fields.keys())
    utilities = {k: 6 for k in util_keys}
    return {
        "name": "Visibility Fuzz", "mpcp": 10, "bod": 8, "evasion": 8, "masking": 8, "sensor": 8,
        "computer_skill": 12, "intelligence": 6, "quickness": 5, "willpower": 6, "body": 6,
        "deck_mode": "hot", "iccm": False, "hardening": 4, "response_increase": 3,
        "active_memory": 6000, "io_speed": 200,
        "trace_factor": 0, "base_bandwidth": 100, "access_modifier": 0,
        "reaction_modifier": 0, "physical_trace_immune": False,
        "storage_free_mp": 6000, "linked_passcode": True,
        "utilities": utilities, "program_sizes": {k: 6 for k in util_keys},
        "program_options": {}, "storage_programs": [
            {"name": "sleaze", "rating": 6, "size": 6},
            {"name": "analyze", "rating": 6, "size": 6},
        ],
    }


def _random_sheaf(rng: random.Random) -> list[dict]:
    """A representative host defense sheaf: 0-4 steps at rising security-tally triggers, each firing
    a real event type seen in shipped hosts -- a straight IC spawn, a Trap IC (surface + concealed),
    or a Passive Alert. These fire dynamically on new_turn as the tally climbs, so the fuzz exercises
    the trigger machinery and trap/alert redaction, not just pre-placed IC."""
    steps: list[dict] = []
    trigger = 0
    for _ in range(rng.randint(0, 4)):
        trigger += rng.randint(3, 6)
        kind = rng.choice(["ic", "ic", "trap_ic", "passive_alert"])
        if kind == "ic":
            event = {"type": "ic", "ic_type": rng.choice(IC_TYPES), "rating": rng.randint(3, 8)}
        elif kind == "trap_ic":
            event = {"type": "trap_ic",
                     "surface_ic_type": rng.choice(["Trace", "Probe", "Killer"]),
                     "surface_ic_rating": rng.randint(3, 8),
                     "hidden_ic_type": rng.choice(["Killer", "Black IC", "Tar Baby"]),
                     "hidden_ic_rating": rng.randint(3, 8)}
        else:
            event = {"type": "passive_alert"}
        steps.append({"trigger": trigger, "events": [event]})
    return steps


def _random_host(rng: random.Random) -> _HostNS:
    paydata, scrambles, data_bombs = [], [], []
    for i in range(rng.randint(1, 6)):
        name = f"file{i}"
        paydata.append({"id": f"pd{i}", "name": name,
                        "density": rng.choice([20, 40, 60, 80, 120, 200]),
                        "is_key": rng.random() < 0.4, "defense": 0})
        if rng.random() < 0.5:  # encrypt some files (Scramble IC)
            sc = {"target_key": f"files::file::{name}", "rating": rng.randint(3, 8)}
            variant = rng.choice(SCRAMBLE_VARIANTS)
            if variant:
                sc["variant"] = variant
            scrambles.append(sc)
        if rng.random() < 0.35:  # booby-trap some files (Data Bomb)
            data_bombs.append({"target": f"files::file::{name}", "rating": rng.randint(3, 8)})
    slaves = rng.sample(SLAVE_PIECES, rng.randint(0, 3))
    # Occasionally a subsystem-wide Scramble (Files or a Slave device), not just per-file.
    if rng.random() < 0.2:
        scrambles.append({"target_key": "files::entire", "rating": rng.randint(3, 8),
                          "variant": rng.choice(["poison", "exploding"])})
    if slaves and rng.random() < 0.2:
        scrambles.append({"target_key": f"slave::piece::{slaves[0]}", "rating": rng.randint(3, 8)})
    cfg = {
        "security_code": rng.choice(SECURITY_CODES),
        "security_value": rng.randint(3, 12),
        # Cover low-to-high-security hosts (shipped hosts reach the low-to-mid teens).
        "acifs": [rng.randint(3, 15) for _ in range(5)],
        "sheaf": _random_sheaf(rng),
        "paydata": paydata,
        "scrambles": scrambles,
        "data_bombs": data_bombs,
        "slave_pieces": slaves,
    }
    if rng.random() < 0.3:  # booby-trap a subsystem with a persistent Worm
        cfg["worms"] = [{"variant": rng.choice(WORM_VARIANTS), "rating": rng.randint(3, 7),
                        "target": rng.choice(["access", "control", "index", "files", "slave"])}]
    trap_doors = None
    if slaves and rng.random() < 0.4:
        trap_doors = [{"id": "td1", "source_piece": slaves[0], "subsystem": "slave",
                       "destination_host_id": None, "destination_ltg": "", "destination_label": "??"}]
    return _HostNS(cfg, trap_doors)


# --------------------------------------------------------------------------- driving
# One persistent event loop for the whole module. asyncio.run() creates AND tears down a fresh loop
# on every call, and on Windows (ProactorEventLoop) tens of thousands of those leak OS handles and
# progressively stall -- which is what made a long sweep hang partway through. Reusing a single loop
# (the pattern tools/sim_static_run.py already uses) keeps every driven action O(1).
_LOOP = asyncio.new_event_loop()


def _call(coro) -> None:
    """Drive one endpoint on the shared loop. A 4xx HTTPException is a legal "you can't do that right
    now" rejection and is tolerated; a 5xx (server error) or ANY non-HTTP exception is a real bug and
    propagates -- so a 500 / unhandled crash from any random host fails the seed with a reproducible
    trace (full 404/500 coverage)."""
    try:
        _LOOP.run_until_complete(coro)
    except HTTPException as exc:
        if exc.status_code >= 500:
            raise


def _pick_file(rng: random.Random, state: dict) -> str:
    files = [p.get("name") for p in (state.get("paydata") or [])
             if isinstance(p, dict) and p.get("name")]
    return rng.choice(files) if files else ""


def _pick_ic(rng: random.Random, state: dict) -> str:
    ics = [ic.get("id") for ic in (state.get("active_ic") or [])
           if isinstance(ic, dict) and ic.get("status") == "active" and ic.get("id")]
    return rng.choice(ics) if ics else ""


def _pick_enemy(rng: random.Random, state: dict) -> str:
    es = [e.get("id") for e in (state.get("enemy_deckers") or [])
          if isinstance(e, dict) and e.get("status") == "active" and e.get("revealed") and e.get("id")]
    return rng.choice(es) if es else ""


def _area_targets(state: dict, limit: int = 3) -> list[str]:
    ids = [ic.get("id") for ic in (state.get("active_ic") or [])
           if isinstance(ic, dict) and ic.get("status") == "active" and ic.get("id")]
    return ids[:limit]


def _action_body(rng: random.Random, action: str, state: dict) -> RunActionInput:
    ic = _pick_ic(rng, state)
    target_file = _pick_file(rng, state)
    if action == "invalidate_passcode" and rng.random() < 0.6:
        ic = "__all__"  # exercise the whole-system invalidate branch (Bug D)
    subsystem = rng.choice(SUBSYSTEMS) if action == "analyze_subsystem" else _SUBSYS_FOR.get(action, "files")
    return RunActionInput(
        action_type=action, subsystem=subsystem,
        utility_rating=6, hacking_pool_dice=rng.randint(0, 2),
        target_ic_id=ic, target_file=target_file,
        target_program=rng.choice(["sleaze", "analyze", ""]),
        maneuver_target=ic, position_choice="tn",
    )


def _random_step(rng: random.Random, run: _StubRun) -> None:
    state = run.state_json
    roll = rng.random()
    if roll < 0.55:
        action = rng.choice(DISCLOSURE_ACTIONS)
        if action in _VALID_ACTIONS:
            _call(mr.perform_action(run_id=1, body=_action_body(rng, action, state),
                                    auth=inv.AUTH_ADMIN, db=_FakeDB()))
    elif roll < 0.68:
        ic = _pick_ic(rng, state)
        if ic:
            _call(mr.attack_ic(run_id=1, body=RunAttackInput(
                target_ic_id=ic, attack_pool=8, hacking_pool_dice=1, armor_utility=6),
                auth=inv.AUTH_ADMIN, db=_FakeDB()))
    elif roll < 0.80:
        enemy = _pick_enemy(rng, state)
        if enemy:
            _call(mr.attack_enemy_decker(run_id=1, body=RunEnemyAttackInput(
                enemy_id=enemy, attack_pool=8, hacking_pool_dice=1,
                program=rng.choice(STRIKE_PROGRAMS)), auth=inv.AUTH_ADMIN, db=_FakeDB()))
    elif roll < 0.87:
        enemy = _pick_enemy(rng, state)
        if enemy:
            _call(mr.scan_enemy_decker(run_id=1, body=RunEnemyScanInput(
                enemy_id=enemy, hacking_pool_dice=1), auth=inv.AUTH_ADMIN, db=_FakeDB()))
    elif roll < 0.93:
        tids = _area_targets(state)
        if tids:
            _call(mr.area_attack(run_id=1, body=RunAreaAttackInput(
                target_ids=tids, attack_pool=10, hacking_pool_dice=1),
                auth=inv.AUTH_ADMIN, db=_FakeDB()))
    else:
        _call(mr.new_turn(run_id=1, auth=inv.AUTH_ADMIN, db=_FakeDB()))


# --------------------------------------------------------------------------- the fuzz test
@pytest.mark.parametrize("seed", FUZZ_SEEDS)
def test_random_hosts_preserve_visibility_invariants(monkeypatch, seed):
    """One random host + a long random script per seed; the admin-vs-player battery must hold after
    every step. A failure prints the seed + step so it reproduces exactly."""
    # Determinism without rebinding the module: the engine draws from the GLOBAL random stream
    # (mr.random / eng.random are that module) -- seed it so rolls are reproducible AND production
    # code that legitimately calls ``random.Random(local_seed)`` still works. The driver picks from
    # its OWN independent, decorrelated stream. Save/restore the global state so this fuzz run does
    # not perturb other tests that depend on the process RNG history.
    _saved_rng = random.getstate()
    try:
        random.seed(seed)
        rng = random.Random(seed ^ 0x9E3779B9)

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

        inv.check_all(run, f"seed={seed} step=boot")

        # Log on for real, then seed a random IC spread so trap/lurking/active redaction is exercised.
        _call(mr.perform_action(run_id=1, body=RunActionInput(
            action_type="logon_to_host", subsystem="access", utility_rating=6, hacking_pool_dice=2),
            auth=inv.AUTH_ADMIN, db=_FakeDB()))
        inv.check_all(run, f"seed={seed} step=logon")

        sec = state.get("host_security_code", "Green")
        for _ in range(rng.randint(0, 3)):
            step = {"trigger": 0, "events": [{"type": "ic",
                    "ic_type": rng.choice(IC_TYPES), "rating": rng.randint(3, 8)}]}
            mr._activate_sheaf_step(state, step, sec)
        # Sometimes dispatch a security decker (revealed or still hidden) so enemy-icon redaction is
        # exercised alongside IC.
        if rng.random() < 0.5:
            enemy = mr._spawn_enemy_decker(state, sec)
            if isinstance(enemy, dict) and rng.random() < 0.6:
                enemy["revealed"] = True
        _, prev_player = inv.check_all(run, f"seed={seed} step=ic-spread")
        inv.check_serialization_pure(run, f"seed={seed} step=ic-spread")

        for i in range(55):
            if run.status != "active" or run.state_json.get("run_ended"):
                break
            _random_step(rng, run)
            _, cur_player = inv.check_all(run, f"seed={seed} step={i}")
            inv.check_monotonic_disclosure(prev_player, cur_player, f"seed={seed} step={i}")
            prev_player = cur_player
    finally:
        random.setstate(_saved_rng)
