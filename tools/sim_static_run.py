"""Ad-hoc blind playthrough driver: decker "Static" (Fuchi Cyber-6) vs the Test host (id 3).

Drives the REAL run engine (app.routers.matrix_runs) against the live Test host config, the
same way the scenario-fuzz tests do (stub run + fake DB + monkeypatched _get_run_or_404).
The "player" makes decisions off the PLAYER-redacted serialization only (blind play); the GM
log + AAR are pulled from the admin serialization at the end.

NOT a test. Run:  python tools/sim_static_run.py [seed]
"""
from __future__ import annotations

import asyncio
import copy
import datetime
import json
import random
import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import HTTPException

from app.routers import matrix_runs as mr
from app.services import matrix_engine as eng
from app.schemas.matrix_run import (
    DeckerStats, RunActionInput, RunAttackInput, RunLogoffInput, RunTrapDoorInput,
)

_ARGS = sys.argv[1:]
_PERSIST = "--persist" in _ARGS
_POS = [a for a in _ARGS if not a.startswith("--")]
SEED = int(_POS[0]) if _POS else 4242


_ADMIN = {"is_admin": True, "is_user": False, "user_token": None}
_PLAYER = {"is_admin": False, "is_user": True, "user_token": "static"}


# ---------------------------------------------------------------------------
# Load the real Test host (id 3) into a lightweight stand-in object.
# ---------------------------------------------------------------------------
class _Host:
    pass


def load_host(host_id: int = 3) -> _Host:
    c = sqlite3.connect("data/shadowrun.db")
    row = list(c.execute(
        "select id, name, config_json, ltg_address, trap_doors_json from matrix_hosts where id=?",
        (host_id,)))[0]
    c.close()
    h = _Host()
    h.id = row[0]
    h.name = row[1]
    h.config_json = json.loads(row[2]) if row[2] else {}
    h.ltg_address = row[3]
    h.trap_doors_json = json.loads(row[4]) if row[4] else None
    return h


# ---------------------------------------------------------------------------
# Build Static's decker payload (Fuchi Cyber-6 + character 2 attributes).
# ---------------------------------------------------------------------------
def build_static() -> dict:
    # Active loadout (rating, active-size)
    active = {
        "attack": (6, 96), "armor": (5, 38), "shield": (4, 32), "deception": (4, 16),
        "read_write": (5, 25), "compressor": (3, 18), "defuse": (4, 16), "camo": (4, 24),
        "decrypt": (4, 8), "sleaze": (6, 108),
    }
    storage = {"analyze": (4, 24), "medic": (6, 72), "relocate": (5, 50), "restore": (6, 54)}

    utilities = {k: r for k, (r, _s) in active.items()}
    program_sizes = {k: s for k, (_r, s) in {**active, **storage}.items()}
    storage_programs = [{"name": k, "rating": r, "size": s} for k, (r, s) in storage.items()]

    stats = DeckerStats(
        name="Static", character_id=2, deck_name="Fuchi Cyber-6",
        mpcp=8, bod=6, evasion=6, masking=6, sensor=6,
        computer_skill=10, intelligence=5, quickness=3, willpower=4, body=3,
        deck_mode="hot", iccm=False, hardening=4, response_increase=2,
        active_memory=400, io_speed=400,
        # Satellite uplink jackpoint: Access +2, Reaction -2, physical trace immune, base BW 50.
        trace_factor=0, base_bandwidth=50, access_modifier=2,
        reaction_modifier=-2, physical_trace_immune=True,
        storage_free_mp=1000,
        utilities=utilities,
        storage_programs=storage_programs,
        program_sizes=program_sizes,
        program_options={"attack": {"skulk": 2}},
    )
    return stats.model_dump()


# ---------------------------------------------------------------------------
# Stub run + fake DB, mirroring tests/test_scenario_fuzz.py.
# ---------------------------------------------------------------------------
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
    def __init__(self, decker: dict, state: dict):
        now = datetime.datetime.now(datetime.timezone.utc)
        self.id = 1
        self.host_id = 3
        self.status = "active"
        self.owner_token_hash = None
        self.decker_json = decker
        self.state_json = state
        self.created_at = now
        self.updated_at = now
        self.version = 1
        self.aar_acknowledged = False


RUN: _StubRun  # set in main


def _patch():
    async def _get_run_or_404(db, run_id):
        return RUN
    mr._get_run_or_404 = _get_run_or_404
    # No owner hash -> access assertion passes for our tokens.
    mr._assert_run_access = lambda run, auth: None


# ---------------------------------------------------------------------------
# Action helpers (call the real async endpoints).
# ---------------------------------------------------------------------------
_LOOP = asyncio.new_event_loop()


def _run(coro):
    return _LOOP.run_until_complete(coro)


NARR: list[str] = []


def note(msg: str):
    NARR.append(msg)
    print(msg)


def act(action_type, subsystem, **kw):
    body = RunActionInput(action_type=action_type, subsystem=subsystem, **kw)
    try:
        _run(mr.perform_action(1, body, _PLAYER, _FakeDB()))
        return True, None
    except HTTPException as e:
        return False, e.detail


def attack(ic_id, pool, hp=0):
    body = RunAttackInput(target_ic_id=ic_id, attack_pool=pool, hacking_pool_dice=hp)
    try:
        _run(mr.attack_ic(1, body, _PLAYER, _FakeDB()))
        return True, None
    except HTTPException as e:
        return False, e.detail


def logoff(hp=0, deception=4):
    body = RunLogoffInput(hacking_pool_dice=hp, deception_utility=deception)
    try:
        _run(mr.graceful_logoff(1, body, _PLAYER, _FakeDB()))
        return True, None
    except HTTPException as e:
        return False, e.detail


def end_turn():
    try:
        _run(mr.new_turn(1, _PLAYER, _FakeDB()))
        return True, None
    except HTTPException as e:
        return False, e.detail


def hp_left():
    return RUN.state_json.get("hackingPool_remaining", 0)


def last_events(n=1):
    log = RUN.state_json.get("event_log", [])
    return log[-n:]


def print_last(prefix="  "):
    for ev in last_events(1):
        desc = ev.get("description", ev.get("type", ""))
        print(f"{prefix}{desc}")


def st():
    return RUN.state_json


def ended():
    return st().get("run_ended") or RUN.status != "active"


_TURN_BUDGET = {"n": 0}
_MAX_TURNS = 120  # hard cap on total End Turn/Round advances for the whole run


def _advance():
    """End the current pass/turn/round so the action budget + Hacking Pool refresh and any
    hostiles on the closing pass get to act. Returns False if capped or the run ended."""
    if _TURN_BUDGET["n"] >= _MAX_TURNS or ended():
        return False
    _TURN_BUDGET["n"] += 1
    end_turn()
    return not ended()


_BUDGET_MARKERS = (
    "action point", "End Turn", "End Round", "Free action",
    "turn(s) are spent", "Not enough action",
)


def do(action, subsystem, label, **kw):
    """Perform an action, transparently advancing the initiative economy when the current
    pass/turn/round can't afford it. Non-budget failures are reported and skipped."""
    for _ in range(10):
        if ended():
            return False
        ok, err = act(action, subsystem, **kw)
        if ok:
            print_last()
            return True
        e = str(err)
        if any(m in e for m in _BUDGET_MARKERS):
            if not _advance():
                note(f"  [{label}: could not free budget]")
                return False
            note(f"  [advance -> Round {st().get('current_turn')} "
                 f"pass {st().get('current_pass')}/{st().get('initiative_passes')}]")
            continue
        note(f"  [{label} blocked: {err}]")
        return False
    note(f"  [{label}: exhausted retries]")
    return False


def pview():
    """Player-redacted serialization -- what Static actually knows (blind play reads from here)."""
    return mr._serialize_run(RUN, _PLAYER).get("state_json", {})


def player_paydata():
    return pview().get("located_paydata", [])


def player_bombs():
    return pview().get("discovered_data_bombs", [])


def player_trapdoors():
    return pview().get("discovered_trap_doors", [])


def shield_wear():
    """Rating points Static's Shield has lost to parries (state['program_damage']['shield']).
    Static knows his own program condition, so consulting this is legitimate player knowledge."""
    return int((st().get("program_damage") or {}).get("shield", 0) or 0)


def maybe_reload_shield(threshold=2):
    """Reload the Shield from its storage copy (Swap Memory, Simple action) once it has worn by
    ``threshold`` rating points, so it stays effective against the next Crippler/attack. No-op if
    it hasn't worn enough yet or the run ended."""
    if ended() or shield_wear() < threshold:
        return
    note(f"  [Shield worn {shield_wear()} pts -- reloading fresh copy]")
    do("swap_memory", "control", "reload shield", target_program="shield")


def paydata_by_name(name):
    for p in st().get("paydata") or []:
        if str(p.get("name", "")).strip().lower() == str(name).strip().lower():
            return p
    return None


def storage_room_for(name):
    """Free deck storage vs the compressor-effective footprint of file ``name`` (player knows his
    own deck memory). Returns True if it fits (or storage is untracked)."""
    free = st().get("storage_free_mp", -1)
    if free is None or free < 0:
        return True
    pd = paydata_by_name(name)
    if pd is None:
        return True
    comp = mr._effective_compressor(RUN.decker_json)
    stored, _ = mr._compressed_store_size(comp, pd.get("density", 0))
    remaining = max(0, free - st().get("storage_used_mp", 0))
    return stored <= remaining


def is_downloaded(name):
    pd = paydata_by_name(name)
    return bool(pd and pd.get("downloaded"))


def play():
    note(f"=== BLIND RUN: Static (Fuchi Cyber-6) vs host '{load_host(3).name}' | seed {SEED} ===")
    note(f"Static: Computer 10, MPCP 8, persona 6/6/6/6, DF start {st().get('detection_factor')}, "
         f"HP {st().get('hackingPool_total')}, satlink (physical-trace immune).")
    note(f"Active kit: Attack-6(Skulk2), Armor-5, Shield-4, Sleaze-6, Camo-4, Deception-4, "
         f"Read/Write-5, Decrypt-4, Defuse-4, Compressor-3.")
    note(f"Storage (swap as needed): Analyze-4, Medic-6, Relocate-5, Restore-6.")
    note("")

    # 1) LOGON -------------------------------------------------------------
    note("-- Logon --")
    tries = 0
    while not st().get("logon_complete") and not ended() and tries < 8:
        do("logon_to_host", "access", "logon", utility_rating=4, hacking_pool_dice=2)
        tries += 1
    if not st().get("logon_complete"):
        note("Could not log on; aborting."); return
    note(f"  [inside the host. DF {st().get('detection_factor')}]")
    note("")

    # 2) SWAP ANALYZE IN (recon + bomb detection need it) ------------------
    # Swap out Camo (not Compressor) so downloads still compress on the deck.
    note("-- Load Analyze (swap out Camo to make room; keep Compressor) --")
    do("unload_program", "control", "unload camo", target_program="camo")
    do("swap_memory", "control", "load analyze", target_program="analyze")
    note("")

    # 3) QUICK RECON: one security read + one host probe (stay quiet) ------
    note("-- Recon --")
    do("analyze_security", "access", "analyze security", utility_rating=4, hacking_pool_dice=1)
    do("analyze_host", "control", "analyze host", utility_rating=4, hacking_pool_dice=2)
    note("")

    # 4) FIND PAYDATA ------------------------------------------------------
    note("-- Locate paydata --")
    for _ in range(3):
        if ended():
            break
        do("locate_paydata", "index", "locate paydata", utility_rating=0, hacking_pool_dice=2)
        if len(player_paydata()) >= 4:
            break
    found = player_paydata()
    note(f"  [located {len(found)} paydata file(s): "
         f"{', '.join(p.get('name','?') for p in found)}]")
    note("")

    # 5) WORK EACH FILE: analyze icon (bomb) -> defuse -> decrypt -> download
    note("-- Extract paydata (grab the fattest files first) --")
    haul_order = sorted(player_paydata(), key=lambda p: -(p.get("density") or p.get("size_mp") or 0))
    for pd in haul_order:
        if ended():
            break
        name = pd.get("name", "?")
        note(f"  * {name} ({pd.get('density') or pd.get('size_mp') or '?'} Mp"
             f"{', KEY' if pd.get('is_key') else ''})")
        maybe_reload_shield()
        do("analyze_icon", "control", "analyze icon", target_file=name)
        for b in player_bombs():
            bn = b.get("name") or b.get("target")
            if bn and str(bn).endswith(name):
                note(f"    [bomb detected on {name} -- defusing]")
                do("defuse_data_bomb", "files", "defuse", target_file=name,
                   utility_rating=4, hacking_pool_dice=3)
        # decrypt if scrambled (harmless attempt otherwise)
        do("decrypt_file", "files", "decrypt", target_file=name,
           utility_rating=4, hacking_pool_dice=2)
        # Download -- retry a lost opposed roll while the file still fits on the deck.
        dl_tries = 0
        while (not ended() and not is_downloaded(name) and dl_tries < 3
               and storage_room_for(name)):
            maybe_reload_shield()
            do("download_data", "files", "download", target_file=name,
               utility_rating=5, hacking_pool_dice=2)
            dl_tries += 1
        if not is_downloaded(name) and not storage_room_for(name):
            note(f"    [no deck storage left for {name} -- leaving it]")
        elif not is_downloaded(name):
            note(f"    [could not pull {name} in {dl_tries} attempt(s)]")
    note("")

    # 6) HUNT THE TRAP DOOR (analyze slave subsystem; do NOT enter) --------
    note("-- Hunt for the trap door (Analyze Subsystem; will NOT follow it) --")
    # Retry the probe: a single Analyze Subsystem may not net enough successes to surface a
    # concealed trap door, so keep probing (advancing the initiative economy) until one is found
    # or we run out of patience. Slave first (where the Test host hides it), then Access/Index.
    attempts = 0
    while not ended() and not player_trapdoors() and attempts < 10:
        for sub in ("slave", "access", "index"):
            if ended() or player_trapdoors():
                break
            do("analyze_subsystem", sub, f"analyze {sub}", utility_rating=4, hacking_pool_dice=2)
        attempts += 1
    tds = player_trapdoors()
    if tds:
        note(f"  [FOUND trap door on subsystem '{tds[0].get('subsystem')}' "
             f"-- NOT following it per orders]")
    else:
        note("  [no trap door surfaced from the subsystems probed]")
    note("")

    # 7) ESCAPE CLEANLY ----------------------------------------------------
    note("-- Graceful logoff (clean escape) --")
    tries = 0
    while not ended() and tries < 12:
        ok, err = logoff(hp=min(4, hp_left()), deception=4)
        if ok:
            print_last()
            break
        e = str(err)
        if any(m in e for m in _BUDGET_MARKERS):
            if not _advance():
                note("  [logoff: could not free budget]"); break
        else:
            note(f"  [logoff blocked: {err}]")
            if not _advance():
                break
        tries += 1
    if not ended() and RUN.status == "active":
        note("  [clean logoff kept failing -- emergency jack-out (accept dump shock)]")
        try:
            _run(mr.jack_out(1, _PLAYER, _FakeDB()))
            print_last()
        except HTTPException as exc:
            note(f"  [jack-out blocked: {exc.detail}]")
    note("")
    note(f"=== RUN END: status={RUN.status} end_reason={st().get('end_reason')} ===")


if __name__ == "__main__":
    host = load_host(3)
    decker = build_static()
    RUN = _StubRun(decker, mr._initial_state(decker, host))
    _patch()

    random.seed(SEED)
    eng.random.seed(SEED)
    mr.random.seed(SEED)

    play()

    # ---- Reports -----------------------------------------------------------
    log = RUN.state_json.get("event_log", [])
    pv = mr._serialize_run(RUN, _PLAYER).get("state_json", {})
    player_log = pv.get("event_log", [])

    print("\n\n########## PLAYER EVENT LOG (what Static sees) ##########")
    for i, ev in enumerate(player_log, 1):
        print(f"{i:3}. {ev.get('description', ev.get('type',''))}")

    print("\n\n########## GM EVENT LOG (full, unredacted) ##########")
    for i, ev in enumerate(log, 1):
        gmflag = " [GM]" if ev.get("gm_only") else ""
        print(f"{i:3}.{gmflag} {ev.get('description', ev.get('type',''))}")

    print("\n\n########## GM AAR ##########")
    stf = RUN.state_json
    print(f"Final status      : {RUN.status}  (end_reason={stf.get('end_reason')})")
    print(f"Security tally    : {stf.get('security_tally')}  alert={stf.get('alert_status')}")
    print(f"Sheaf steps fired : {stf.get('sheaf_steps_triggered')}")
    print(f"Active IC at end  : {[ic.get('type') for ic in stf.get('active_ic', [])]}")
    cm = stf.get('condition_monitor', {})
    print(f"Static condition  : persona {cm.get('persona_boxes')}/10  stun {cm.get('stun_boxes')}/10  "
          f"phys {cm.get('physical_boxes')}/10  mpcp_dmg {cm.get('mpcp_damage')}")
    print(f"Detection Factor  : {stf.get('detection_factor')}")
    haul = stf.get("paydata_secured") or {}
    print(f"Paydata secured   : {haul.get('count', 0)} file(s), {haul.get('total_mp', 0)} Mp, "
          f"{haul.get('key_count', 0)} key file(s)")
    if haul.get("files"):
        for f in haul["files"]:
            print(f"    - {f}")
    print(f"Downloaded ledger : {[d.get('name') for d in stf.get('downloaded_files', [])]}")
    tds = stf.get("trap_doors", [])
    for td in tds:
        print(f"Trap door         : discovered={td.get('discovered')} filed={td.get('filed')} "
              f"subsystem={td.get('subsystem')} -> dest '{td.get('destination_label')}' "
              f"(followed={td.get('entered', False)})")
    # GM-only AAR event if present
    for ev in log:
        if ev.get("type") == "paydata_aar":
            print(f"AAR detail        : {ev.get('description')}")

    # ---- Structured GM AAR (what the /matrix-runs2 review page renders) -----
    print("\n\n########## STRUCTURED GM AAR (review-page payload) ##########")
    aar = mr._build_run_aar(RUN)
    print(json.dumps(aar, indent=2, default=str))

    # ---- Optionally persist the finished run so a real AAR exists in the DB -
    if _PERSIST:
        from app.db.session import async_session
        from app.models.matrix_run import MatrixRun
        from app.auth.core import hash_token

        async def _persist():
            async with async_session() as db:
                row = MatrixRun(
                    host_id=RUN.host_id,
                    decker_json=RUN.decker_json,
                    state_json=RUN.state_json,
                    status=RUN.status,
                    owner_token_hash=hash_token(_PLAYER["user_token"]),
                    aar_acknowledged=False,
                )
                db.add(row)
                await db.commit()
                await db.refresh(row)
                return row.id

        new_id = _run(_persist())
        print(f"\n[persist] Saved run #{new_id} to data/shadowrun.db "
              f"(status={RUN.status}) -- available in the GM Run Reports queue.")


