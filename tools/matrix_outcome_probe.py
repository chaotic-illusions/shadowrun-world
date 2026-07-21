"""In-process probe: force deterministic Success / Failure / Tie outcomes for live
Matrix-run actions and capture the REAL event_log dicts + state deltas the UI renders.

Why this approach (justification -- see docs/_matrix_catalog_live_feasibility.md):

  * Determinism lever: we monkeypatch ``matrix_engine.roll_dice`` to pop a scripted
    SUCCESS COUNT per call (in call order) instead of seeding an RNG. ``roll_dice`` is
    the single opposed-test primitive every resolver funnels through, so controlling its
    successes directly forces the decker-vs-host / attacker-vs-defender outcome regardless
    of pool size, target number, or the rule-of-6 explosion. Seeding a Random would still
    leave the outcome a function of pool/TN arithmetic (brittle); scripting successes is
    exact. We also pin ``matrix_engine.random`` and ``matrix_runs.random`` to a fixed RNG
    so any residual non-roll_dice randomness (enemy nerve/spawn/choice) is stable.

  * Execution layer: we call the REAL async endpoint bodies (``mr.perform_action`` /
    ``mr.attack_ic``) and the REAL app-as-GM driver (``mr._advance_npc_pass``) in-process
    -- NOT via HTTP -- with a fake run object + a no-op AsyncSession, and monkeypatch
    ``_get_run_or_404`` / ``_serialize_run`` so no DB or auth is touched. The event_log
    dicts produced are byte-for-byte what a real POST would persist and the UI would render.

No DB writes: state is built in memory (``_initial_state`` on a SimpleNamespace host) and
mutated in dicts only. The already-running uvicorn server is never touched.

Run:  .\.venv\Scripts\python tools\matrix_outcome_probe.py
"""

from __future__ import annotations

import asyncio
import copy
import json
import os
import sys
import types

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.routers import matrix_runs as mr
from app.services import matrix_engine as eng
from app.schemas.matrix_run import RunActionInput, RunAttackInput


# --------------------------------------------------------------------------- RNG

class ScriptedRollDice:
    """Drop-in for ``eng.roll_dice``: pops the next scripted success count in call order.

    Returns a coherent roll dict (pool honoured, a plausible dice list, ones=0 so a
    data-bomb 'all ones' detonation is never triggered by accident)."""

    def __init__(self) -> None:
        self.queue: list[int] = []
        self.default = 0
        self.calls: list[dict] = []

    def script(self, *successes: int) -> None:
        self.queue = list(successes)

    def __call__(self, pool: int, tn: int = 4) -> dict:
        pool = max(1, pool)
        succ = self.queue.pop(0) if self.queue else self.default
        succ = max(0, min(pool, succ))
        hit = max(tn, 6)
        dice = [hit] * succ + [min(tn - 1, 2) if tn > 2 else 1] * (pool - succ)
        result = {"pool": pool, "tn": tn, "dice": dice, "successes": succ, "ones": 0}
        self.calls.append({"pool": pool, "tn": tn, "successes": succ})
        return result


class FixedRandom:
    """Deterministic stand-in for any residual module ``random`` use (not roll_dice)."""

    def randint(self, a, b):
        return a

    def choice(self, seq):
        return seq[0]

    def random(self):
        return 0.99  # high -> low-probability enemy spawns / nerve-flees stay dormant

    def shuffle(self, seq):
        return None

    def sample(self, seq, k):
        return list(seq)[:k]

    def seed(self, *a, **k):
        pass

    def getstate(self):
        return None

    def setstate(self, s):
        pass


ROLL = ScriptedRollDice()
eng.roll_dice = ROLL
eng.random = FixedRandom()
mr.random = FixedRandom()


# --------------------------------------------------------------------- fake I/O

class FakeDB:
    async def execute(self, *a, **k):
        raise AssertionError("DB should not be queried (patched _get_run_or_404)")

    async def commit(self):
        pass

    async def refresh(self, obj):
        pass


class FakeRun:
    def __init__(self, state: dict, decker: dict) -> None:
        self.id = 1
        self.status = "active"
        self.state_json = state
        self.decker_json = decker
        self.owner_token_hash = None
        self.version = 1


AUTH = {"is_admin": True, "is_user": True, "user_token": None, "view_as_player": False}


def _install_run(run: FakeRun) -> None:
    async def _fake_get(db, run_id):
        return run

    mr._get_run_or_404 = _fake_get
    mr._assert_run_access = lambda run, auth: None
    mr._serialize_run = lambda run, auth: run.state_json


# ------------------------------------------------------------------ base state

def build_decker() -> dict:
    return {
        "handle": "ProbeRunner",
        "mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
        "intelligence": 6, "quickness": 6, "willpower": 6,
        "computer_skill": 6, "hacking_skill": 6,
        "deck_mode": "hot", "persona_mode": "none",
        "utilities": {"attack": 6, "sleaze": 0, "shield": 0, "medic": 0},
        "program_options": {},
        "storage_free_mp": -1,
    }


def build_host():
    cfg = {
        "security_code": "Red",
        "security_value": 8,
        "acifs": [8, 8, 8, 8, 8],
        "sheaf": [],
        "paydata": [{"name": "payfile", "density": 3, "is_key": False, "defense": 0}],
    }
    return types.SimpleNamespace(config_json=cfg, ltg_address=None, trap_doors_json=None)


def base_state(decker: dict) -> dict:
    host = build_host()
    st = mr._initial_state(decker, host)
    # Make the player's action economy generous + mark logged on so ops resolve.
    st["logon_complete"] = True
    st["decker_initiative"] = 30
    st["initiative_passes"] = 3
    st["current_pass"] = 1
    st["current_turn"] = 1
    st["npc_combat_maneuvers"] = False   # keep NPC path a straight attack, not a maneuver
    return st


def killer_ic() -> dict:
    return {
        "id": "ic_killer", "type": "Killer", "rating": 8, "status": "active",
        "boxes": 0, "initiative": 24, "detection_level": 3,
    }


def enemy_roster_state(decker: dict) -> dict:
    """A combat state populated with EACH enemy-type category the engine recognises."""
    st = base_state(decker)
    st["active_ic"] = [
        killer_ic(),                                                     # proactive gray IC
        {"id": "ic_construct", "type": "Construct", "rating": 6,        # Construct-type active IC
         "status": "active", "boxes": 0, "initiative": 14, "detection_level": 3},
        {"id": "ic_party_a", "type": "Killer", "rating": 6, "status": "active",
         "boxes": 0, "initiative": 12, "detection_level": 3, "cluster_id": "party1"},
        {"id": "ic_party_b", "type": "Killer", "rating": 6, "status": "active",
         "boxes": 0, "initiative": 12, "detection_level": 3, "cluster_id": "party1"},
    ]
    st["lurking_ic"] = [
        {"id": "lc_worm", "type": "Worm", "variant": "deathworm", "rating": 6,
         "subsystem": "files", "status": "lurking"},
    ]
    st["enemy_deckers"] = [
        {"id": "ed1", "handle": "BlackHat", "computer_skill": 6, "attack": 6,
         "bod": 6, "evasion": 6, "masking": 6, "sensor": 6, "mpcp": 6,
         "initiative": 18, "persona_boxes": 0, "status": "active", "detected": True},
    ]
    return st


# ------------------------------------------------------------------- reporting

def dump(label: str, before: dict, after: dict, watch: list[str]) -> None:
    new_events = after.get("event_log", [])[len(before.get("event_log", [])):]
    print(f"\n    --- {label} ---")
    print("    NEW event_log entries:")
    if not new_events:
        print("      (none)")
    for e in new_events:
        print("      " + json.dumps(e, default=str))
    print("    state deltas:")
    for key in watch:
        b = _dig(before, key)
        a = _dig(after, key)
        if b != a:
            print(f"      {key}: {b!r} -> {a!r}")


def _dig(state: dict, dotted: str):
    cur = state
    for part in dotted.split("."):
        if isinstance(cur, list):
            try:
                cur = cur[int(part)]
            except (ValueError, IndexError):
                return None
        elif isinstance(cur, dict):
            cur = cur.get(part)
        else:
            return None
    return cur


# ---------------------------------------------------------------- scenarios

async def scenario_attack_ic(script, decker) -> None:
    """Decker attacks a Killer IC (cybercombat). roll_dice order: [attack, resist]."""
    st = base_state(decker)
    st["active_ic"] = [killer_ic()]
    run = FakeRun(copy.deepcopy(st), decker)
    _install_run(run)
    ROLL.script(*script)
    before = copy.deepcopy(run.state_json)
    body = RunAttackInput(target_ic_id="ic_killer", attack_pool=8, hacking_pool_dice=0)
    await mr.attack_ic(1, body, AUTH, FakeDB())
    dump("attack_ic", before, run.state_json,
         ["security_tally", "active_ic.0.boxes", "active_ic.0.status"])


async def scenario_system_test(script, decker) -> None:
    """Decker runs a System Test op (analyze_host). system_test order: [decker, host]."""
    st = base_state(decker)
    st["active_ic"] = []  # isolate the op's own event from any NPC reaction
    run = FakeRun(copy.deepcopy(st), decker)
    _install_run(run)
    ROLL.script(*script)
    before = copy.deepcopy(run.state_json)
    body = RunActionInput(action_type="analyze_host", subsystem="access",
                          utility_rating=0, hacking_pool_dice=0)
    await mr.perform_action(1, body, AUTH, FakeDB())
    dump("system_test (analyze_host)", before, run.state_json,
         ["security_tally", "alert_status", "host_ratings_revealed"])


def scenario_enemy_attack(script, decker) -> None:
    """App-as-GM drives a proactive Killer IC against the decker. order: [attack, resist]."""
    st = enemy_roster_state(decker)
    # Keep only the single Killer active so the forced roll maps to one clean exchange,
    # and drop the enemy decker for this scenario (its AI turn is a separate driver path).
    st["active_ic"] = [killer_ic()]
    st["enemy_deckers"] = []
    run = FakeRun(st, decker)
    ROLL.script(*script)
    before = copy.deepcopy(run.state_json)
    eff = mr._get_decker_effective(decker, st)
    st["_acting_init"] = None
    mr._advance_npc_pass(
        st, decker, run,
        eff=eff, sec_code=st["host_security_code"],
        sec_value=st["host_security_value"], det_factor=st["detection_factor"],
    )
    dump("enemy proactive attack (Killer IC -> decker)", before, run.state_json,
         ["condition_monitor.persona_boxes", "condition_monitor.physical_boxes",
          "condition_monitor.stun_boxes", "icon_crashed", "run_ended"])


# ------------------------------------------------------------------------ main

def main() -> None:
    decker = build_decker()

    print("=" * 78)
    print("MATRIX OUTCOME PROBE -- live in-process S/F/T demonstration")
    print("=" * 78)

    print("\n[ ENEMY ROSTER CONSTRUCTED IN STATE ]")
    roster = enemy_roster_state(decker)
    print("  active_ic types :", [ic["type"] for ic in roster["active_ic"]])
    print("  party cluster   :", [ic["id"] for ic in roster["active_ic"] if ic.get("cluster_id")])
    print("  lurking_ic      :", [(w["type"], w.get("variant")) for w in roster["lurking_ic"]])
    print("  enemy_deckers   :", [d["handle"] for d in roster["enemy_deckers"]])

    # ---- ACTION 1: attack_ic ------------------------------------------------
    print("\n\n#############  ACTION 1: attack_ic (decker -> Killer IC)  #############")
    #  SUCCESS: attack scores, IC fails to resist -> damage boxes land
    asyncio.run(scenario_attack_ic([4, 0], decker))
    #  FAILURE: attack whiffs -> no successes -> no boxes
    asyncio.run(scenario_attack_ic([0, 4], decker))
    #  TIE   : equal successes -> net 0 -> staged to no damage (cybercombat is net-successes,
    #          there is no discrete 'tie' branch; net<=0 simply deals nothing)
    asyncio.run(scenario_attack_ic([2, 2], decker))

    # ---- ACTION 2: system-test op ------------------------------------------
    print("\n\n#############  ACTION 2: system_test op (analyze_host, Access)  #############")
    #  SUCCESS: decker net +2, decker successes > 0
    asyncio.run(scenario_system_test([2, 0], decker))
    #  FAILURE: decker 0 successes -> fail
    asyncio.run(scenario_system_test([0, 2], decker))
    #  TIE (house rule -> decker): net 0 with decker successes > 0 SUCCEEDS
    asyncio.run(scenario_system_test([2, 2], decker))
    #  TIE (mutual whiff 0-vs-0): the one tie that FAILS
    asyncio.run(scenario_system_test([0, 0], decker))

    # ---- ACTION 3: enemy proactive attack ----------------------------------
    print("\n\n#############  ACTION 3: enemy proactive attack (Killer IC -> decker)  #############")
    #  SUCCESS (for the IC): it hits, decker fails to resist -> decker takes boxes
    scenario_enemy_attack([4, 0], decker)
    #  FAILURE (for the IC): it whiffs -> decker unharmed
    scenario_enemy_attack([0, 4], decker)
    #  TIE: equal successes -> net 0 -> no boxes
    scenario_enemy_attack([2, 2], decker)

    print("\n" + "=" * 78)
    print("PROBE COMPLETE")
    print("=" * 78)


if __name__ == "__main__":
    main()
