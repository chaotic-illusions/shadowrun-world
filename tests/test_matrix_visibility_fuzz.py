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
import random
import typing

import pytest
from fastapi import HTTPException

from app.routers import matrix_runs as mr
from app.schemas.matrix_run import ActionType, DeckerUtilities, RunActionInput, RunAttackInput

from tests import matrix_visibility_invariants as inv

# One seed = one full random run. Broad rather than deep; each seed is a distinct host + script.
FUZZ_SEEDS = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

SECURITY_CODES = ["Blue", "Green", "Orange", "Red"]
SUBSYSTEMS = ["access", "files", "slave", "index", "control"]
SCRAMBLE_VARIANTS = [None, "poison", "exploding"]
SLAVE_PIECES = ["camera", "maglock", "sensor", "turnstile", "elevator"]
IC_TYPES = ["Probe", "Killer", "Acid", "Marker", "Tar Baby", "Trace", "Worm", "Black IC"]

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


def _random_host(rng: random.Random) -> _HostNS:
    paydata, scrambles, data_bombs = [], [], []
    for i in range(rng.randint(1, 4)):
        name = f"file{i}"
        paydata.append({"id": f"pd{i}", "name": name,
                        "density": rng.choice([20, 40, 60, 80, 120]),
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
    cfg = {
        "security_code": rng.choice(SECURITY_CODES),
        "security_value": rng.randint(3, 9),
        "acifs": [rng.randint(2, 10) for _ in range(5)],
        "sheaf": [],
        "paydata": paydata,
        "scrambles": scrambles,
        "data_bombs": data_bombs,
        "slave_pieces": slaves,
    }
    trap_doors = None
    if slaves and rng.random() < 0.4:
        trap_doors = [{"id": "td1", "source_piece": slaves[0], "subsystem": "slave",
                       "destination_host_id": None, "destination_ltg": "", "destination_label": "??"}]
    return _HostNS(cfg, trap_doors)


# --------------------------------------------------------------------------- driving
def _call(coro) -> None:
    """Drive one endpoint. A controlled HTTPException (illegal-in-context action) is fine; any
    other exception propagates as a real bug (the harness never swallows unexpected failures)."""
    try:
        asyncio.run(coro)
    except HTTPException:
        pass


def _pick_file(rng: random.Random, state: dict) -> str:
    files = [p.get("name") for p in (state.get("paydata") or [])
             if isinstance(p, dict) and p.get("name")]
    return rng.choice(files) if files else ""


def _pick_ic(rng: random.Random, state: dict) -> str:
    ics = [ic.get("id") for ic in (state.get("active_ic") or [])
           if isinstance(ic, dict) and ic.get("status") == "active" and ic.get("id")]
    return rng.choice(ics) if ics else ""


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
    if roll < 0.72:
        action = rng.choice(DISCLOSURE_ACTIONS)
        if action in _VALID_ACTIONS:
            _call(mr.perform_action(run_id=1, body=_action_body(rng, action, state),
                                    auth=inv.AUTH_ADMIN, db=_FakeDB()))
    elif roll < 0.85:
        ic = _pick_ic(rng, state)
        if ic:
            _call(mr.attack_ic(run_id=1, body=RunAttackInput(
                target_ic_id=ic, attack_pool=8, hacking_pool_dice=1, armor_utility=6),
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
        monkeypatch.setattr(mr, "_get_run_or_404", _get)
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
        inv.check_all(run, f"seed={seed} step=ic-spread")

        for i in range(45):
            if run.status != "active" or run.state_json.get("run_ended"):
                break
            _random_step(rng, run)
            inv.check_all(run, f"seed={seed} step={i}")
    finally:
        random.setstate(_saved_rng)
