"""
Matrix Run API -- SR2/VR2.0 rules engine endpoints.
Separate from /matrix-hosts (SR1 topology editor).
"""

from __future__ import annotations

import copy
import random
import re
import uuid
from datetime import datetime, UTC
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.auth.core import hash_token
from app.auth.dependencies import get_admin_token, get_any_token
from app.models.matrix_run import MatrixRun
from app.models.matrix_host import MatrixHost
from app.schemas.matrix_run import (
    MatrixRunCreate, MatrixRunRead, MatrixRunSummary,
    RunActionInput, RunAttackInput, RunLogoffInput, RunReactiveInput,
    RunSuppressInput, RunEnemyAttackInput,
    RunTrapDoorInput, SheaveSaveInput, SheafGenerateInput,
)
from app.services import matrix_engine as eng
from app.services import matrix_rules as rules

router = APIRouter()


# State keys removed entirely from state_json when serving a non-admin.
# (Admin sees the full state.) lurking_ic is GM-only: reactive IC "lurks
# silently" by the rules, so players must not see it exists at all.
_GM_ONLY_STATE_KEYS = {"sheaf", "host_acifs", "lurking_ic", "scrambles", "paydata", "data_bombs", "trap_doors"}

# Maps crippler/ripper IC type names to the decker attribute they attack.
_CRIPPLER_TARGET: dict[str, str] = {
    "Acid": "bod", "Binder": "evasion", "Jammer": "sensor", "Marker": "masking",
    "Acid-rip": "bod", "Bind-rip": "evasion", "Jam-rip": "sensor", "Mark-rip": "masking",
}

# Black Hammer / Killjoy resolve their icon hit at a fixed lethal base level (vr2: these
# "function like black IC" and inflict lethal biofeedback regardless of the host's code).
# Mirrors the enemy->PC lethal-biofeedback base in _enemy_decker_take_turn; strong hits stage
# it up toward Deadly, so the icon takes Serious-Deadly-class damage even on a low-tier host
# where a plain Attack (security-code base) would only be Light/Moderate.
_LETHAL_BASE_LEVEL = "Serious"

# The host designer labels cripplers/rippers as "Crippler (Marker)" / "Ripper (Acid-rip)"
# for the GM, but IC_CATALOG and _CRIPPLER_TARGET are keyed by the bare inner token
# ("Marker", "Acid-rip"). Strip the wrapper before any catalog/target lookup so the IC
# resolves to its rules entry (otherwise it silently no-ops -- never attacks).
_IC_WRAPPER_RE = re.compile(r"^(?:Crippler|Ripper)\s*\((.+)\)\s*$")


def _canonical_ic_type(ic_type: str) -> str:
    """Map a display IC type (e.g. "Crippler (Marker)") to its IC_CATALOG key ("Marker")."""
    if not ic_type:
        return ""
    m = _IC_WRAPPER_RE.match(ic_type)
    return m.group(1).strip() if m else ic_type


def _target_file_name(target: str) -> str:
    """Extract the bare file/piece name from a defense target key.

    Defense targets are stored with inconsistent prefixes across features -- a file-level
    data bomb as "files::<name>", a Files scramble as "files::file::<name>" -- while a
    download addresses the bare "<name>". Compare on the trailing segment so the bomb/
    scramble actually fires on the matching download.
    """
    return target.rsplit("::", 1)[-1].strip() if target else ""


def _build_trap_doors(host: MatrixHost) -> list[dict]:
    """Normalize a host's designer trap doors into GM-only run-state entries.

    A trap door is a concealed comm port to another host, hidden on a subsystem (the designer
    attaches it to a Slave device). Per vr2 it is found via an Analyze Subsystem operation on
    the concealing subsystem -- so each entry starts undiscovered. The destination is redacted
    from players (see _serialize_run) until they ENTER it: filing only records the door, and the
    far host's LTG access can be learned only on the far side (logon + Analyze Access there).
    """
    out: list[dict] = []
    for td in (getattr(host, "trap_doors_json", None) or []):
        if not isinstance(td, dict):
            continue
        out.append({
            "id": str(td.get("id")) if td.get("id") is not None else f"td{len(out) + 1}",
            "source_piece": td.get("source_piece", ""),
            "subsystem": (td.get("subsystem") or "slave"),   # concealing subsystem
            "destination_host_id": td.get("destination_host_id"),
            "destination_ltg": td.get("destination_ltg", ""),
            "destination_label": td.get("destination_label", ""),
            "discovered": False,
            "filed": False,
        })
    return out


# -- Helpers -------------------------------------------------------------------

async def _get_run_or_404(db: AsyncSession, run_id: int) -> MatrixRun:
    result = await db.execute(select(MatrixRun).where(MatrixRun.id == run_id))
    run = result.scalars().first()
    if not run:
        raise HTTPException(404, "Matrix run not found")
    return run


async def _get_host_or_404(db: AsyncSession, host_id: int) -> MatrixHost:
    result = await db.execute(select(MatrixHost).where(MatrixHost.id == host_id))
    host = result.scalars().first()
    if not host:
        raise HTTPException(404, "Matrix host not found")
    return host


def _is_run_owner(run: MatrixRun, auth: dict) -> bool:
    """True if the auth context owns the run (started it via this token)."""
    token = auth.get("user_token")
    if not token or not run.owner_token_hash:
        return False
    return run.owner_token_hash == hash_token(token)


def _assert_run_access(run: MatrixRun, auth: dict) -> None:
    """Admin or owner may read/mutate. Anyone else gets 404 (existence not leaked)."""
    if auth.get("is_admin"):
        return
    if _is_run_owner(run, auth):
        return
    raise HTTPException(404, "Matrix run not found")


# Strip the running security-tally from a player-visible event description. Every tally line in
# the log renders as "[Tt]ally +N -> M" (the running total), which the decker is not supposed to
# know except via Analyze Security -- so remove that clause (and the structured tally fields).
_TALLY_CLAUSE_RE = re.compile(r"\s*[Tt]ally \+\d+ -> \d+\.?")


def _redact_event_tally(e: dict) -> dict:
    """Return a player-safe copy of an event with the running security tally removed."""
    if not isinstance(e, dict):
        return e
    out = dict(e)
    out.pop("tally_increase", None)
    out.pop("tally_total", None)
    desc = out.get("description")
    if isinstance(desc, str):
        scrubbed = _TALLY_CLAUSE_RE.sub("", desc)
        if scrubbed != desc:
            out["description"] = re.sub(r"\s{2,}", " ", scrubbed).strip()
    return out


def _serialize_run(run: MatrixRun, auth: dict) -> dict:
    """Build a MatrixRunRead-shaped dict, redacting GM-only state for non-admins.

    The UI hides these secrets, but the raw JSON would otherwise still carry them,
    so redaction must happen server-side:
      - sheaf / host_acifs / lurking_ic: removed entirely (see _GM_ONLY_STATE_KEYS)
      - active_ic[].trap_hidden: reduced to a bare ``True`` marker so the client can
        still show a generic [TRAP] badge without leaking the concealed IC's
        type/rating.
    """
    data = MatrixRunRead.model_validate(run, from_attributes=True).model_dump()
    if not auth.get("is_admin"):
        state = dict(data.get("state_json") or {})
        # Surface only the paydata the decker has actually LOCATED (name/size/key/downloaded) so
        # the player can make storage decisions; the full GM paydata list is then redacted below.
        located_paydata = [
            {"name": p.get("name"),
             "size_mp": max(0, int(p.get("density", 0) or 0)),
             "is_key": bool(p.get("is_key")),
             "downloaded": bool(p.get("downloaded")),
             "destroyed": bool(p.get("destroyed"))}
            for p in (state.get("paydata") or [])
            if isinstance(p, dict) and p.get("located")
        ]
        # Surface only DISCOVERED trap doors, and even then without the destination -- the player
        # knows a port to "another system" exists, not where it leads. Filing only records it for
        # later (the destination is reachable ONLY through the door); the destination -- and
        # whether it has LTG access -- stays unknown until the decker enters and analyzes it there.
        discovered_trap_doors = [
            {"id": d.get("id"),
             "source_piece": d.get("source_piece", ""),
             "subsystem": d.get("subsystem", "slave"),
             "filed": bool(d.get("filed"))}
            for d in (state.get("trap_doors") or [])
            if isinstance(d, dict) and d.get("discovered")
        ]
        for k in _GM_ONLY_STATE_KEYS:
            state.pop(k, None)
        state["located_paydata"] = located_paydata
        state["discovered_trap_doors"] = discovered_trap_doors
        # The current host's LTG-access status is unknown to the decker until a successful
        # Analyze Subsystem on Access reveals it (host_ltg_revealed). Hide it until then.
        if not state.get("host_ltg_revealed"):
            state.pop("host_has_ltg", None)
        if isinstance(state.get("active_ic"), list):
            redacted = [_redact_ic(ic) for ic in state["active_ic"] if isinstance(ic, dict)]
            state["active_ic"] = [ic for ic in redacted if ic is not None]
        if isinstance(state.get("event_log"), list):
            # Drop GM-only events (e.g. surreptitious reactive-IC activity the decker
            # has not yet detected) so the log never betrays a hidden IC's presence, and
            # scrub the running security tally from the survivors (the decker only learns
            # its tally via Analyze Security -- see _redact_event_tally).
            state["event_log"] = [
                _redact_event_tally(e)
                for e in state["event_log"]
                if not (isinstance(e, dict) and e.get("gm_only"))
            ]
        # Security tally + alert status are GM-only: the decker learns them only by running
        # Analyze Security (which snapshots them into the player-visible security_known).
        state.pop("security_tally", None)
        state.pop("alert_status", None)
        if isinstance(state.get("enemy_deckers"), list):
            # Enemy deckers stay hidden until they reveal themselves (located the PC /
            # attacked). Even then the PC sees only name/tier/intent/condition, not raw stats.
            state["enemy_deckers"] = [
                _redact_enemy_decker(e) for e in state["enemy_deckers"]
                if isinstance(e, dict) and e.get("revealed")
            ]
        data["state_json"] = state

    # Live decker footprint: expose Icon Bandwidth and the Bandwidth Trace Modifier recomputed
    # from the *current* persona ratings and active-memory utilities (they shift as programs
    # crash or the persona takes crippler/MPCP damage), so the UI can show living values.
    decker = run.decker_json or {}
    st = data.get("state_json")
    if isinstance(st, dict):
        st["icon_bandwidth"] = _live_icon_bandwidth(decker, st)
        st["bandwidth_modifier"] = _live_bandwidth_modifier(decker, st)
    return data


def _redact_enemy_decker(e: dict) -> dict:
    """Player view of a revealed enemy decker -- presence + condition, not raw ratings."""
    cm = e.get("condition_monitor", {}) or {}
    return {
        "id": e.get("id"),
        "name": e.get("name"),
        "tier": e.get("tier"),
        "intent": e.get("intent"),
        "status": e.get("status"),
        "located_pc": e.get("located", False),
        "condition_monitor": {"persona_boxes": cm.get("persona_boxes", 0)},
    }


def _ic_detection_level(ic: dict) -> int:
    """Effective detection level the decker currently has on an IC (vr2 line 409).

    Proactive IC betray themselves by attacking -> default level 1 (presence known).
    Reactive IC 'do not betray themselves' -> default level 0 (unaware) until a secret
    Sensor Test or Analyze raises ``detection_level``. ``analyzed`` forces a full reveal.
    """
    level = ic.get("detection_level")
    if level is None:
        is_reactive = rules.IC_CATALOG.get(_canonical_ic_type(ic.get("type", "")), {}).get("ic_type") == "reactive"
        level = 0 if is_reactive else 1
    if ic.get("analyzed"):
        level = 3
    return level


def _redact_ic(ic: dict) -> dict | None:
    """Player view of an active IC. Returns None when the decker is unaware of it.

    Graduated reveal (vr2 reactive-IC detection, line 409, + #9):
      0 -> unaware: hidden entirely (None)        2 -> type known, rating hidden
      1 -> presence known ("Unknown IC")          3 -> type + rating revealed
    Reactive IC running surreptitiously (Probe, Data Bomb, Scramble, Worm, Trace) stay
    invisible until detected, so nothing leaks that they are operating. trap_hidden
    always collapses to a bare marker.
    """
    level = _ic_detection_level(ic)
    if level <= 0:
        return None  # decker is unaware -- do not reveal the IC at all
    out = dict(ic)
    if out.get("trap_hidden"):
        out["trap_hidden"] = True
    if level == 1:
        out["type"] = "Unknown IC"
        out["rating"] = None
    elif level == 2:
        out["rating"] = None  # type known, exact rating still unknown
    # level >= 3: full reveal
    out["detection_level"] = level
    return out


# Action cost (Free/Simple/Complex) per action_type, from the vr2 System Operations table.
# (Action-economy ENFORCEMENT -- 2 Simple OR 1 Complex + 1 Free per pass -- is the next step;
# for now this is surfaced on each action for awareness. See docs GAPS PLAN section D.)
_ACTION_COST = {op["name"].lower().replace(" ", "_"): op["action"] for op in rules.SYSTEM_OPERATIONS}
_ACTION_COST.update({
    "swap_memory": "Simple", "purge_hog": "Complex", "decrypt_file": "Simple",
    "relocate": "Simple", "redirect_datatrail": "Complex", "upload_data": "Simple",
    "analyze_subsystem": "Simple", "logon_to_ltg": "Complex",
    "attack": "Simple",                       # vr2: all cybercombat attacks are Simple Actions
    "medic": "Complex", "restore": "Complex", "disinfect": "Complex",
    "defuse_data_bomb": "Complex", "dump_log": "Complex",
    "steamroller": "Complex", "slow": "Complex", "decompress_file": "Complex",
    "dinab": "Free",                          # DINAB: a Free action runs one program autonomously
})


def _decker_reaction(decker: dict) -> int:
    """VR2 Matrix Reaction = round-up average of Quickness and Intelligence, plus any
    jackpoint Reaction modifier (e.g. SATLINK -2). Clamped to a minimum of 1."""
    base = -(-(decker.get("quickness", 4) + decker.get("intelligence", 4)) // 2)
    return max(1, base + decker.get("reaction_modifier", 0))


def _init_passes(init: int) -> int:
    """VR2 initiative -> number of action passes this Combat Turn. A score acts in decrements of
    10 (22 -> 22/12/2 = 3 passes; 20 -> 20/10 = 2 passes), i.e. ceil(score/10), minimum 1."""
    return max(1, -(-int(init) // 10))


def _roll_decker_initiative(decker: dict) -> tuple[int, int]:
    """Roll the decker's Matrix initiative; return (score, passes). Initiative goes in
    increments of 10 -- a score of 22 acts on counts 22/12/2, i.e. 3 passes this turn."""
    init = eng.decker_initiative_roll(
        _decker_reaction(decker),
        response_increase=decker.get("response_increase", 0),
        has_hot_dnl=decker.get("deck_mode") == "hot",
        has_reality_filter=bool(decker.get("reality_filter")),
    )
    return init, _init_passes(init)


def _initial_state(decker: dict, host: MatrixHost) -> dict:
    """Build the initial run state from decker stats and host config."""
    cfg = host.config_json or {}
    masking = decker.get("masking", 1)
    sleaze = (decker.get("utilities") or {}).get("sleaze", 0)
    det_factor = eng.detection_factor(masking, sleaze)
    hackingPool_total = max(0, (decker.get("intelligence", 1) + decker.get("mpcp", 1)) // 3)
    decker_initiative, initiative_passes = _roll_decker_initiative(decker)

    return {
        "security_tally": 0,
        "alert_status": "none",
        "decker_initiative": decker_initiative,   # Matrix initiative this Combat Turn
        "initiative_passes": initiative_passes,    # action passes (increments of 10)
        "current_pass": 1,
        "actions_this_turn": 0,
        "pass_action_points": 2,   # per-pass: 2 Simple OR 1 Complex
        "pass_free": 1,            # per-pass: 1 Free action
        "condition_monitor": {
            "persona_boxes": 0,
            "physical_boxes": 0,
            "mpcp_damage": 0,
            "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
            # Of the persona_damage above, the portion that is PERMANENT Persona-chip damage
            # (gray/black-IC Rippers). Restore can repair persona_damage down to -- but never
            # below -- this floor. Temporary (Restore-repairable) damage = persona_damage - this.
            "persona_chip_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
            # Highest rating of the crippler program(s) that caused each attribute's CURRENT
            # temporary damage -- the Restore Test target number. Reset to 0 once repaired.
            "crippler_rating": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
        },
        "active_ic": [],
        "lurking_ic": [],
        "current_turn": 1,
        "sheaf_steps_triggered": [],
        "detection_factor": det_factor,
        "host_security_code": cfg.get("security_code", "Green"),
        "host_security_value": cfg.get("security_value", 6),
        "host_acifs": cfg.get("acifs", [10, 10, 10, 10, 10]),
        "sheaf": cfg.get("sheaf", []),
        "paydata": cfg.get("paydata") or [],       # [{name, density, is_key, defense}]
        "scrambles": cfg.get("scrambles") or [],   # [{target_key, rating, variant}]
        "data_bombs": cfg.get("data_bombs") or [], # [{target, rating}]
        "defused_bombs": [],
        # Concealed trap doors (GM-only until discovered via Analyze Subsystem; destinations
        # stay redacted from players until entered or filed -- see _serialize_run).
        "trap_doors": _build_trap_doors(host),
        # This host's own LTG-access status. Unknown to the decker (host_has_ltg redacted) until a
        # successful Analyze Subsystem on Access flips host_ltg_revealed -- the only way to learn
        # whether a host reached through a trap door is also reachable from the regular grid.
        "host_has_ltg": bool(getattr(host, "ltg_address", None)),
        "host_ltg_revealed": False,
        # Host subsystem (ACIFS) ratings are GM-only (host_acifs). Each successful Analyze Host
        # reveals one rating into this player-visible map {subsystem: rating} in ACIFS order
        # (vr2: "each success reveals one piece of info").
        "host_ratings_revealed": {},
        # The decker only KNOWS its security tally + alert status from the last successful Analyze
        # Security (the GM otherwise tracks the tally secretly). None until first scan; then
        # {tally, alert, turn}. The live security_tally/alert_status are redacted for players.
        "security_known": None,
        # Player-visible host access-log summary from the last successful Dump Log (vr2 Validate).
        # None until the decker dumps the log; then a dict (legal users, files accessed, programs
        # run, whether the decker's OWN intrusion is on record, 24h log size). Not GM-only -- it
        # is the decker's own read of the host logs.
        "access_log_dumped": None,
        # Deck storage ledger for downloaded paydata (vr2 Mp). storage_free_mp < 0 = untracked/
        # unlimited; >= 0 = real free capacity at jack-in (downloads consume it).
        "storage_free_mp": decker.get("storage_free_mp", -1),
        "storage_used_mp": 0,
        "downloaded_files": [],   # [{name, size_mp, is_key, turn}] -- player-visible ledger
        # Program memory: storage_programs are carried but NOT active at logon; Swap Memory loads
        # one into active memory (decker.utilities) mid-run, optionally pushing an active program
        # back to storage. program_sizes (util key -> Mp) and active_memory_cap let the engine
        # enforce the active-memory ceiling on a swap-in. Active programs always keep a storage
        # copy, so swapping only shifts *active* usage -- deck storage_free_mp is unaffected.
        "active_memory_cap": int(decker.get("active_memory", 0) or 0),
        "program_sizes": {str(k): int(v) for k, v in (decker.get("program_sizes") or {}).items()},
        "storage_programs": [
            {"name": str(p.get("name", "")), "rating": int(p.get("rating", 0) or 0),
             "size": int(p.get("size", 0) or 0)}
            for p in (decker.get("storage_programs") or [])
            if isinstance(p, dict) and p.get("name")
        ],
        "access_modifier": decker.get("access_modifier", 0),  # jackpoint Access side
        "console_access": decker.get("console_access", False),
        "physical_trace_immune": bool(decker.get("physical_trace_immune", False)),  # SATLINK uplink
        "base_bandwidth": decker.get("base_bandwidth", 0),     # jackpoint base BW for live BW Trace mod
        "linked_passcode": decker.get("linked_passcode", False),
        "enemy_deckers": [],   # security deckers spawned automatically by the sheaf (vr2 #5)
        "logon_complete": False,
        "run_ended": False,
        "end_reason": None,
        "event_log": [],
        "hackingPool_total": hackingPool_total,
        "hackingPool_remaining": hackingPool_total,
        "redirects_placed": 0,
    }


def _spend_hp(state: dict, requested: int) -> None:
    """Deduct Hacking Pool dice; raises 400 if pool is exhausted."""
    if requested <= 0:
        return
    if "hackingPool_remaining" not in state:
        return  # legacy run without HP tracking -- allow freely
    available = state["hackingPool_remaining"]
    if requested > available:
        raise HTTPException(
            400,
            f"Not enough Hacking Pool dice: {requested} requested, {available} remaining"
        )
    state["hackingPool_remaining"] = available - requested


def _append_event(state: dict, event: dict) -> None:
    """Append a timestamped event to the state log."""
    event["turn"] = state.get("current_turn", 1)
    event["ts"] = datetime.now(UTC).isoformat()
    state["event_log"].append(event)


# -- One-Shot program option (vr2_rules.md L1667) --------------------------------------------------
# One-Shot is a build-time program OPTION carried into a run via decker["program_options"][util].
# A one-shot utility executes ONCE then "vanishes from active memory" -- the decker must Swap Memory
# a fresh copy from storage to use it again. A Tar Baby / Tar Pit crash wipes ALL copies of a
# one-shot program on the deck (it can never be reloaded for the rest of the run).
#
# "Spent" is expressed through ``state["program_damage"]``: setting program_damage[util] == its base
# rating drives every ``_effective_<util>`` helper to 0, so a spent one-shot automatically reads as
# "not loaded" (the existing gate) and a Swap Memory reload (Mode 3 sets program_damage[target]=0)
# brings it back -- no per-helper gating is needed.
#
# DELIBERATE SCOPE LIMITS (kept simple on purpose):
#   * Only the NAMED utilities the engine resolves by name are consumed (attack, poison, restrict,
#     reveal, black_hammer, killjoy, medic, restore, disinfect, defuse, steamroller, slow, shield).
#     Operational utilities driven through the generic ``utility_rating`` number (deception, scanner,
#     read_write, validate_pgm, mirrors, relocate, evaluate, analyze, decrypt) are NOT consumed --
#     the request carries only a raw rating for those, not a utility name, and a one-shot Deception
#     is not a meaningful case.
#   * Recovery/defensive utilities (medic, restore, disinfect, defuse, steamroller, slow, shield)
#     have an ``_effective_<util>`` gate, so a spent one-shot is HARD-blocked until reloaded.
#     Offensive utilities (attack, poison, restrict, reveal, black_hammer, killjoy) have no such
#     gate -- consuming them records the spend, emits the player-visible event, shrinks live icon
#     bandwidth and makes Hog skip the slot, but does NOT hard-refuse the next use (a SOFT gate).
#   * Per-COPY counting is not tracked: the in-run cost of a one-shot is simply the Swap Memory
#     action needed to reload it after each use (unless a tar wiped every copy).


def _normalize_util_name(util_name: str) -> str:
    """Canonicalise a utility name: lowercase + spaces->underscores (so "Black Hammer" ->
    "black_hammer") so program_options / utilities lookups always hit the stored key."""
    return str(util_name or "").strip().lower().replace(" ", "_")


def _is_one_shot(decker: dict, util_name: str) -> bool:
    """True iff the named utility was built/loaded with the One-Shot option (carried in
    ``decker["program_options"][util].one_shot``)."""
    key = _normalize_util_name(util_name)
    return bool((decker.get("program_options") or {}).get(key, {}).get("one_shot"))


def _spend_one_shot(state: dict, decker: dict, util_name: str) -> None:
    """Consume a single-use (One-Shot) utility AFTER its effect resolves: mark it spent so it reads
    as "vanished from active memory" until reloaded via Swap Memory. Idempotent no-op for a
    non-one-shot program, one that is not loaded, or one already spent/wiped."""
    key = _normalize_util_name(util_name)
    if not _is_one_shot(decker, key):
        return
    base = int((decker.get("utilities") or {}).get(key, 0) or 0)
    if base <= 0:
        return  # not loaded / already gone from active memory
    if key in (state.get("one_shot_wiped") or []):
        return  # every copy was corrupted by Tar IC -- nothing left to spend
    pd = state.setdefault("program_damage", {})
    if int(pd.get(key, 0) or 0) >= base:
        return  # this copy is already spent -- do not double-emit the event
    pd[key] = base  # effective rating -> 0: "executes ONCE then vanishes from active memory"
    _append_event(state, {
        "type": "one_shot_spent",
        "utility": key,
        "description": (
            f"{key.replace('_', ' ').title()} was a single-use (One-Shot) copy -- spent and gone "
            "from active memory. Swap Memory a fresh copy to use it again."
        ),
    })


def _wipe_one_shot(state: dict, decker: dict, util_name: str) -> None:
    """Tar IC wipe (vr2_rules.md L1667): a Tar Baby / Tar Pit crash destroys EVERY copy of a
    One-Shot program on the deck -- it can never be reloaded this run. Marks it fully spent, flags
    it in ``one_shot_wiped`` (so Swap Memory refuses to reload it) and drops any matching storage
    copy so a Mode-1 load finds nothing. No-op for a non-one-shot program."""
    key = _normalize_util_name(util_name)
    if not _is_one_shot(decker, key):
        return
    base = int((decker.get("utilities") or {}).get(key, 0) or 0)
    pd = state.setdefault("program_damage", {})
    if base > 0:
        pd[key] = base  # the copy in active memory is gone too
    wiped = state.setdefault("one_shot_wiped", [])
    if key not in wiped:
        wiped.append(key)
    storage = state.get("storage_programs")
    if isinstance(storage, list):
        # Remove the storage copies so Swap Memory Mode 1 (load from storage) finds nothing.
        state["storage_programs"] = [
            p for p in storage if _normalize_util_name(p.get("name", "")) != key
        ]
    _append_event(state, {
        "type": "one_shot_wiped",
        "utility": key,
        "description": (
            f"Tar IC corrupted ALL copies of the One-Shot {key.replace('_', ' ').title()} on the "
            "deck -- it cannot be reloaded."
        ),
    })


def _one_shot_block(state: dict, decker: dict, util_name: str) -> None:
    """Hard-refuse an OFFENSIVE strike with a One-Shot utility that is already spent or tar-wiped.

    Recovery/defense utilities (medic, restore, shield, ...) auto-gate through their
    ``_effective_<util>`` helper -- a spent one-shot reads as effective-0 there. The offensive
    endpoints (``attack_ic`` / ``attack_enemy_decker``) read the carried rating directly, so they
    need this explicit check to honour "executes ONCE then vanishes from active memory": once spent,
    the program must be reloaded via Swap Memory before it can fire again. Call it BEFORE spending
    HP / rolling so a blocked strike costs nothing. No-op for a non-one-shot program or one that is
    not loaded / not yet spent."""
    key = _normalize_util_name(util_name)
    if not _is_one_shot(decker, key):
        return
    base = int((decker.get("utilities") or {}).get(key, 0) or 0)
    if base <= 0:
        return  # not loaded -- nothing to spend or block
    pretty = key.replace("_", " ").title()
    if key in (state.get("one_shot_wiped") or []):
        raise HTTPException(
            400,
            f"One-Shot {pretty}: Tar IC corrupted every copy -- it cannot be used again this run.",
        )
    if int((state.get("program_damage") or {}).get(key, 0) or 0) >= base:
        raise HTTPException(
            400,
            f"One-Shot {pretty} is spent and gone from active memory -- "
            "Swap Memory a fresh copy before using it again.",
        )


def _reset_pass_budget(state: dict) -> None:
    """Refresh the current initiative pass's action budget: 2 action points (2 Simple OR
    1 Complex) + 1 Free action (vr2 action economy).

    SR2 core RAW (confirmed by GM, not an assumption): the Hacking Pool refills at the top of
    every Combat Turn AND at the start of EACH of the decker's own initiative passes -- the pool
    is restored every time it becomes the decker's action. So a full pool is available on every
    pass (21/11/1...), shared with defence until that actor's next pass. Refreshed here so both
    pass-advance and New Turn restore it; only refresh when HP tracking exists (legacy runs skip)."""
    state["pass_action_points"] = 2
    state["pass_free"] = 1
    if "hackingPool_total" in state:
        state["hackingPool_remaining"] = state["hackingPool_total"]


def _spend_pass_action(state: dict, action_type: str) -> None:
    """Enforce the per-pass action economy (vr2). Each initiative pass grants 2 action
    points (Simple=1, Complex=2) plus 1 Free action. When the current pass can't afford the
    action, auto-advance to the next initiative pass (refreshing the budget); when ALL passes
    this Combat Turn are spent, raise 400 -- the decker must start a New Turn (re-rolls init).
    Legacy runs without a budget are not enforced."""
    if "pass_action_points" not in state:
        return
    cost = _ACTION_COST.get(action_type, "Complex")
    need_ap = 0 if cost == "Free" else (2 if cost == "Complex" else 1)
    while True:
        if cost == "Free":
            if state.get("pass_free", 0) >= 1:
                state["pass_free"] -= 1
                return
        elif state.get("pass_action_points", 0) >= need_ap:
            state["pass_action_points"] -= need_ap
            return
        cur, total = state.get("current_pass", 1), state.get("initiative_passes", 1)
        if cur >= total:
            raise HTTPException(
                400, f"All {total} initiative pass(es) spent this Combat Turn -- start a "
                     "New Turn (refreshes initiative + actions).")
        state["current_pass"] = cur + 1
        _reset_pass_budget(state)
        _append_event(state, {
            "type": "new_pass",
            "description": f"Initiative pass {cur + 1}/{total} begins -- actions refreshed (2 AP + 1 Free) and Hacking Pool restored.",
        })


def _roll_mpcp_damage(
    state: dict,
    decker: dict,
    ic_rating: int,
    *,
    pool_multiplier: int = 1,
    tn_bonus: int = 0,
) -> tuple[int, dict]:
    """Resolve a post-crash MPCP-damage test (Blaster / Sparky / Black IC).

    Each variant rolls ``ic_rating * pool_multiplier`` dice vs.
    ``mpcp + tn_bonus + hardening`` and deals 1 permanent MPCP damage per 2
    successes. Black IC uses ``pool_multiplier=2``; Sparky adds ``tn_bonus=2``.
    Returns (mpcp_hits, raw_roll). Caller composes the user-facing event.
    """
    hardening = decker.get("hardening", 0)
    tn = max(2, decker.get("mpcp", 1) + tn_bonus + hardening)
    roll = eng.roll_dice(ic_rating * pool_multiplier, tn)
    mpcp_hit = roll["successes"] // 2
    if mpcp_hit > 0:
        state["condition_monitor"]["mpcp_damage"] = (
            state["condition_monitor"].get("mpcp_damage", 0) + mpcp_hit
        )
    return mpcp_hit, roll


def _roll_enemy_mpcp_damage(
    enemy: dict,
    program_rating: int,
    *,
    pool_multiplier: int = 2,
) -> tuple[int, dict]:
    """PC->enemy mirror of ``_roll_mpcp_damage`` (Black Hammer / Killjoy icon-crash burn).

    When the PC's lethal program crashes an enemy decker's icon it "functions like black IC"
    and reduces the target's deck MPCP: roll ``program_rating * pool_multiplier`` dice (vr2:
    blaster-style test at DOUBLE the program rating) vs the enemy's ``MPCP + Hardening`` and
    burn 1 permanent MPCP point per 2 successes. Mutates the enemy's condition monitor
    (``mpcp_damage``) ONLY -- the raw ``mpcp`` is left intact so effective MPCP =
    ``mpcp - mpcp_damage``, exactly as the PC side tracks its own MPCP damage. Returns
    (mpcp_hits, roll); the caller composes the player-facing event.
    """
    hardening = int(enemy.get("hardening", 0) or 0)
    tn = max(2, int(enemy.get("mpcp", 1) or 1) + hardening)
    roll = eng.roll_dice(max(1, program_rating) * pool_multiplier, tn)
    mpcp_hit = roll["successes"] // 2
    if mpcp_hit > 0:
        ecm = enemy.setdefault("condition_monitor", {})
        ecm["mpcp_damage"] = ecm.get("mpcp_damage", 0) + mpcp_hit
    return mpcp_hit, roll


def _apply_dump_shock(state: dict, decker: dict, sec_code: str, sec_value: int) -> dict:
    """Roll dump shock and add any resulting boxes to the physical CM.

    Returns the raw eng.dump_shock_roll result. Callers decide whether to log a
    standalone ``dump_shock`` event or fold the result into another event
    description (trace_dump / jack_out / persona_crash all do this differently).
    """
    ds = eng.dump_shock_roll(
        security_code=sec_code, security_value=sec_value,
        body=decker.get("body", 4),
        is_cool_deck=decker.get("deck_mode") == "cool",
        has_iccm=decker.get("iccm", False),
        is_tortoise=decker.get("deck_mode") == "tortoise",
    )
    if not ds.get("immune"):
        state["condition_monitor"]["physical_boxes"] = (
            state["condition_monitor"].get("physical_boxes", 0) + ds["boxes"]
        )
    return ds


def _check_sheaf_triggers(state: dict) -> list[dict]:
    """
    Check if the current security tally has crossed any sheaf trigger thresholds.
    Returns list of newly triggered steps.
    """
    tally = state["security_tally"]
    sheaf = state.get("sheaf", [])
    already = set(state.get("sheaf_steps_triggered", []))
    newly_triggered = []

    for i, step in enumerate(sheaf):
        if i not in already and tally >= step["trigger"]:
            state["sheaf_steps_triggered"].append(i)
            already.add(i)
            newly_triggered.append(step)

    return newly_triggered


def _check_and_activate_sheaf(state: dict, security_code: str) -> None:
    """Promote any newly-crossed sheaf thresholds and append their events to the log.

    Call after any operation that bumps ``state["security_tally"]`` (action, probe,
    IC crash, failed logoff). Idempotent against already-triggered steps because
    ``_check_sheaf_triggers`` tracks ``sheaf_steps_triggered``.
    """
    for step in _check_sheaf_triggers(state):
        for ev in _activate_sheaf_step(state, step, security_code):
            _append_event(state, ev)


def _cascade_max_increase(security_code: str, base_rating: int) -> int:
    """Cascading IC maximum cumulative increase, by host Security Code (vr2 Cascading IC Table)."""
    if security_code == "Blue":
        return 1
    pct = {"Green": 0.25, "Orange": 0.50, "Red": 0.75, "Black": 1.0}.get(security_code, 0.25)
    flat = {"Green": 2, "Orange": 3, "Red": 4, "Black": 6}.get(security_code, 2)
    return min(int(base_rating * pct), flat)


def _apply_cascade_outcome(ic: dict, security_code: str, *, hit: bool, damage_dealt: bool) -> None:
    """Update a cascading IC's bonuses after one of its attacks (vr2 Cascading IC):
    - MISS (attack didn't connect): +1 to its attack Security Value for subsequent attacks.
    - HIT but the decker resisted ALL damage: +1 to its Rating for subsequent attacks.
    Both are cumulative and capped by the Cascading IC Table (by Security Code)."""
    if not ic.get("cascading"):
        return
    cap = _cascade_max_increase(security_code, ic.get("rating", 6))
    if not hit:
        ic["cascade_sv_bonus"] = min(cap, ic.get("cascade_sv_bonus", 0) + 1)
    elif not damage_dealt:
        ic["cascade_rating_bonus"] = min(cap, ic.get("cascade_rating_bonus", 0) + 1)


def _activate_sheaf_step(state: dict, step: dict, security_code: str) -> list[dict]:
    """Process a triggered sheaf step. Returns list of event log entries."""
    events: list[dict] = []

    for ev in step.get("events", []):
        ev_type = ev.get("type")

        if ev_type == "ic":
            ic_type   = ev.get("ic_type", "Killer")
            ic_rating = ev.get("rating", 6)

            if ic_type in ("Tar Baby", "Tar Pit", "Worm"):
                # Ambush reactive IC -- lurks silently until the GM triggers it (Tar Baby/
                # Tar Pit on utility use; Worm against the deck's MPCP).
                lc_id = f"lc_{uuid.uuid4().hex[:8]}"
                state.setdefault("lurking_ic", []).append({
                    "id": lc_id,
                    "type": ic_type,
                    "rating": ic_rating,
                    "status": "lurking",
                })
                trigger = "against the deck's MPCP" if ic_type == "Worm" else "on utility use"
                events.append({
                    "type": "reactive_ic_armed",
                    "ic_id": lc_id,
                    "ic_type": ic_type,
                    "ic_rating": ic_rating,
                    "gm_only": True,  # reactive ambush IC does not betray itself (vr2 line 409)
                    "description": f"{ic_type}-{ic_rating} armed -- lurking. Triggers {trigger}.",
                })
            else:
                ic_id = f"ic_{uuid.uuid4().hex[:8]}"
                initiative = eng.ic_initiative_roll(ic_rating, security_code)
                _opts = [str(o).lower() for o in (ev.get("options") or [])]
                state["active_ic"].append({
                    "id": ic_id,
                    "type": ic_type,
                    "rating": ic_rating,
                    "category": rules.IC_CATALOG.get(ic_type, {}).get("category", "gray"),
                    "boxes": 0,
                    "suppressed": False,
                    "initiative": initiative,
                    "status": "active",
                    "hunt_cycle_successes": 0,
                    # Designer/generated options: Shield/Shift raise the decker's to-hit TN;
                    # Armor mitigates, Cascading chains, Expert modifies TNs (all carried for combat).
                    "shield": ("shielding" in _opts or "shield" in _opts),
                    "shift": ("shifting" in _opts or "shift" in _opts),
                    "options": ev.get("options", []),
                    "cascading": ev.get("cascading", False),
                    "expert": ev.get("expert"),
                })
                # Reactive IC do not betray themselves -- their activation is GM-only
                # until a Sensor Test / Analyze detects them (vr2 line 409).
                is_reactive = rules.IC_CATALOG.get(ic_type, {}).get("ic_type") == "reactive"
                events.append({
                    "type": "ic_activation",
                    "description": f"IC activated: {ic_type} Rating {ic_rating} (initiative {initiative})",
                    "ic_id": ic_id,
                    "ic_type": ic_type,
                    "ic_rating": ic_rating,
                    "gm_only": is_reactive,
                })

        elif ev_type == "trap_ic":
            # Surface IC goes active; hidden IC spawns when surface is crashed
            surface_type   = ev.get("surface_ic_type", "Probe")
            surface_rating = ev.get("surface_ic_rating", 6)
            hidden_type    = ev.get("hidden_ic_type", "Blaster")
            hidden_rating  = ev.get("hidden_ic_rating", 6)
            ic_id      = f"ic_{uuid.uuid4().hex[:8]}"
            initiative = eng.ic_initiative_roll(surface_rating, security_code)
            state["active_ic"].append({
                "id": ic_id,
                "type": surface_type,
                "rating": surface_rating,
                "category": rules.IC_CATALOG.get(surface_type, {}).get("category", "white"),
                "boxes": 0,
                "suppressed": False,
                "initiative": initiative,
                "status": "active",
                "hunt_cycle_successes": 0,
                "trap_hidden": {"type": hidden_type, "rating": hidden_rating},
            })
            events.append({
                "type": "ic_activation",
                "ic_id": ic_id,
                "ic_type": surface_type,
                "ic_rating": surface_rating,
                "is_trap": True,
                "gm_only": rules.IC_CATALOG.get(surface_type, {}).get("ic_type") == "reactive",
                "description": (
                    f"Trap IC activated: {surface_type}-{surface_rating} "
                    f"(conceals {hidden_type}-{hidden_rating})"
                ),
            })

        elif ev_type == "construct":
            # Single icon combining multiple IC programs; uses threat_rating for combat
            threat_rating = ev.get("threat_rating", 6)
            components    = ev.get("components", [])
            defenses      = ev.get("defenses", [])
            ic_id      = f"ic_{uuid.uuid4().hex[:8]}"
            initiative = eng.ic_initiative_roll(threat_rating, security_code)
            comp_names = ", ".join(c.get("type", "?") for c in components)
            state["active_ic"].append({
                "id": ic_id,
                "type": "Construct",
                "rating": threat_rating,
                "category": "construct",
                "boxes": 0,
                "suppressed": False,
                "initiative": initiative,
                "status": "active",
                "hunt_cycle_successes": 0,
                "construct_components": components,
                "construct_defenses": defenses,
            })
            events.append({
                "type": "ic_activation",
                "ic_id": ic_id,
                "ic_type": "Construct",
                "ic_rating": threat_rating,
                "description": f"Construct activated: Threat {threat_rating} [{comp_names}]",
                "construct_components": components,
            })

        elif ev_type == "party_ic":
            # Cluster of independent IC programs; each has its own icon and CM
            components = ev.get("components", [])
            cluster_id = f"cluster_{uuid.uuid4().hex[:8]}"
            for comp in components:
                comp_type   = comp.get("type", "Killer")
                comp_rating = comp.get("rating", 6)
                ic_id      = f"ic_{uuid.uuid4().hex[:8]}"
                initiative = eng.ic_initiative_roll(comp_rating, security_code)
                _copts = [str(o).lower() for o in (comp.get("options") or [])]
                state["active_ic"].append({
                    "id": ic_id,
                    "type": comp_type,
                    "rating": comp_rating,
                    "category": rules.IC_CATALOG.get(comp_type, {}).get("category", "gray"),
                    "boxes": 0,
                    "suppressed": False,
                    "initiative": initiative,
                    "status": "active",
                    "hunt_cycle_successes": 0,
                    "cluster_id": cluster_id,
                    # Carry the component's rolled Options/Defenses into combat.
                    "shield": ("shielding" in _copts or "shield" in _copts),
                    "shift": ("shifting" in _copts or "shift" in _copts),
                    "options": comp.get("options", []),
                    "cascading": comp.get("cascading", False),
                    "expert": comp.get("expert"),
                })
            comp_names = ", ".join(
                f"{c.get('type','?')}-{c.get('rating','?')}" for c in components
            )
            events.append({
                "type": "party_ic_activation",
                "cluster_id": cluster_id,
                "cluster_size": len(components),
                "description": f"Party IC ({len(components)} programs): {comp_names}",
            })

        elif ev_type == "passive_alert":
            if state["alert_status"] == "none":
                state["alert_status"] = "passive"
                events.append({"type": "alert", "level": "passive",
                                "description": "PASSIVE ALERT -- all subsystem ratings +2. Host suspects intrusion."})

        elif ev_type == "active_alert":
            state["alert_status"] = "active"
            state.pop("has_legitimate_status", None)  # Active alert deletes validate passcode
            state["decoy_successes"] = 0              # Active alert destroys decoy
            state["decoy_hp"] = 0
            events.append({"type": "alert", "level": "active",
                            "description": "ACTIVE ALERT -- response teams dispatched. Proactive Gray and Black IC authorized. Validate Passcode revoked."})

        elif ev_type == "shutdown":
            state["run_ended"] = True
            state["end_reason"] = "host_shutdown"
            events.append({"type": "shutdown",
                            "description": "HOST SHUTDOWN -- all sessions terminated."})

        elif ev_type == "enemy_decker":
            # Authored host dispatches a security decker at this tally threshold. It starts
            # hidden (GM-only) and then hunts the PC automatically via the app-as-GM loop.
            enemy = eng.generate_enemy_decker(
                security_code, state.get("host_security_value", 6),
                name=ev.get("name") or None)
            if ev.get("intent"):
                enemy["intent"] = ev["intent"]
            enemy["id"] = f"ed_{uuid.uuid4().hex[:8]}"
            _ed_init, _ed_passes = _roll_decker_initiative(enemy)  # rolled once on entry
            enemy["initiative"], enemy["initiative_passes"] = _ed_init, _ed_passes
            state.setdefault("enemy_deckers", []).append(enemy)
            events.append({
                "type": "enemy_decker_injected", "gm_only": True, "enemy_id": enemy["id"],
                "description": (
                    f"GM: {enemy['name']} (Computer {enemy['computer_skill']}, "
                    f"Attack-{enemy['utilities']['attack']}) dispatched to hunt the intruder."
                ),
            })

    return events


def _cluster_size(state: dict, cluster_id: str | None) -> int:
    """Count active IC in a Party IC cluster."""
    if not cluster_id:
        return 0
    return sum(
        1 for ic in state.get("active_ic", [])
        if ic.get("status") == "active" and ic.get("cluster_id") == cluster_id
    )


def _subsystem_rating(state: dict, subsystem: str) -> int:
    """Get the host's subsystem rating, applying alert modifiers.

    Passive Alert: all ratings +2 (VR2.0: "All Subsystem Ratings increase by 2").
    Active Alert: no blanket subsystem modifier. Logging back in is harder (Access TN context only).
    """
    acifs = state.get("host_acifs", [10, 10, 10, 10, 10])
    mapping = {"access": 0, "control": 1, "index": 2, "files": 3, "slave": 4}
    idx = mapping.get(subsystem, 1)
    base = acifs[idx] if idx < len(acifs) else 10
    modifier = {"passive": 2}.get(state.get("alert_status", "none"), 0)
    rating = base + modifier
    # Jackpoint Access modifier applies to Access Tests only (vr2 Jackpoint table);
    # Console access additionally halves the Access Rating (round up).
    if subsystem == "access":
        rating += state.get("access_modifier", 0)
        if state.get("console_access"):
            rating = -(-rating // 2)  # round-up halving
    return max(2, rating)


def _shield_shift_tn_modifier(ic: dict, *, penetration: bool, chaser: bool) -> int:
    """+2 TN for the decker to hit an IC running Shield or Shift (vr2).

    - Shield: +2; Penetration negates it entirely; Chaser makes it +4 (extra-effective).
    - Shift:  +2; Chaser negates it entirely; Penetration makes it +4 (extra-effective).
    Shield and Shift are mutually exclusive. Returns the net to-hit TN penalty.
    """
    if ic.get("shield"):
        if penetration:
            return 0
        return 4 if chaser else 2
    if ic.get("shift"):
        if chaser:
            return 0
        return 4 if penetration else 2
    return 0


def _ic_has_armor(ic: dict) -> bool:
    """IC carries the Armor defense (from the IC Defenses Table / designer)."""
    return "Armor" in (ic.get("options") or [])


def _ic_expert(ic: dict, kind: str) -> int:
    """Expert option value for the given kind ('offense' or 'defense'), else 0.
    Expert Offense raises the IC's attack effectiveness; Expert Defense raises the TN to
    hit it (vr2 IC Options Table)."""
    e = ic.get("expert") or {}
    return e.get("value", 0) if e.get("type") == kind else 0


def _compute_trace_tn(state: dict, decker: dict, ic_rating: int, eff: dict) -> int:
    """Full Trace Factor TN per VR2.0 rules.

    TF = Evasion - IC_Rating + Camo + Jackpoint + Bandwidth - Redirects_placed
    TN = max(2, TF)
    """
    utilities = decker.get("utilities") or {}
    tf = (
        eff.get("evasion", decker.get("evasion", 4))
        - ic_rating
        + utilities.get("camo", 0)
        + decker.get("trace_factor", 0)
        + _live_bandwidth_modifier(decker, state, eff)
        - state.get("redirects_placed", 0)
    )
    return max(2, tf)


def _effective_detection_factor(state: dict, decker: dict) -> int:
    """Live Detection Factor (vr2_rules Detection Factor + Suppression).

    Recomputed each test rather than frozen at logon, so it reflects:
      - Sleaze utility (round-up average with Masking, else Masking/2),
      - Masking reduced by Marker/Mark-rip cripplers (via _get_decker_effective),
      - minus 1 per suppressed active IC program (Suppression rule), floored at 1.
    """
    eff = _get_decker_effective(decker, state)
    sleaze = (decker.get("utilities") or {}).get("sleaze", 0)
    base = eng.detection_factor(eff["masking"], sleaze)
    # A suppressed IC costs 1 DF for as long as it is held down. Suppression is declared at the
    # moment the IC crashes, so a suppressed IC has status "crashed" (not "active") -- count it
    # regardless of status, floored at 1.
    suppressed = sum(
        1 for ic in state.get("active_ic", [])
        if ic.get("suppressed")
    )
    return max(1, base - suppressed)


# Persona Mode multipliers (vr2): the boosted attribute +50%, the listed others -50%.
# Masking/Sensor modes leave bandwidth alone; Bod/Evasion modes also cut I/O bandwidth.
_PERSONA_MODE_MULT = {
    "bod":     {"bod": 1.5, "evasion": 0.5, "masking": 0.5, "sensor": 0.5},
    "evasion": {"bod": 0.5, "evasion": 1.5, "masking": 0.5, "sensor": 0.5},
    "masking": {"bod": 1.0, "evasion": 0.5, "masking": 1.5, "sensor": 0.5},
    "sensor":  {"bod": 0.5, "evasion": 0.5, "masking": 0.5, "sensor": 1.5},
}


def _get_decker_effective(decker: dict, state: dict) -> dict:
    """Return decker persona stats with Persona Mode and crippler reductions applied."""
    dmg = state.get("condition_monitor", {}).get("persona_damage", {})
    mpcp_dmg = state.get("condition_monitor", {}).get("mpcp_damage", 0)
    mode = (decker.get("persona_mode") or state.get("persona_mode") or "none")
    mult = _PERSONA_MODE_MULT.get(mode, {})

    def _attr(name: str) -> int:
        base = decker.get(name, 4)
        if mult:
            base = max(1, round(base * mult.get(name, 1.0)))
        return max(1, base - dmg.get(name, 0))

    return {
        "bod":     _attr("bod"),
        "evasion": _attr("evasion"),
        "masking": _attr("masking"),
        "sensor":  _attr("sensor"),
        "mpcp":    max(1, decker.get("mpcp", 4) - mpcp_dmg),
    }


def _effective_shield(decker: dict, state: dict) -> int:
    """Effective Shield rating = the loaded Shield utility minus its accrued per-use wear.

    Wear lives in ``state['program_damage']['shield']`` -- the SAME slot Swap Memory resets --
    so a freshly swapped/reloaded Shield returns to full, and the worn rating is already what
    _live_icon_bandwidth/_highest_running_utility see. ``<= 0`` means the Shield is unloaded or
    burned out and can no longer parry.
    """
    base = (decker.get("utilities") or {}).get("shield", 0) or 0
    worn = (state.get("program_damage") or {}).get("shield", 0)
    return max(0, base - worn)


def _shield_parry(state: dict, decker: dict, *, attacker_skill: int, context: str) -> int:
    """Make ONE defensive Shield Test against an attack on the decker's persona (vr2).

    Rolls the effective Shield rating vs the attacker's skill (host Security Value, or an enemy
    decker's Computer skill), then degrades the Shield by 1 Rating Point regardless of outcome
    (reload via Swap Memory) and emits a player-visible ``shield_parry`` event. Returns the net
    successes, which the caller SUBTRACTS from a damage attack's successes or ADDS to the
    decker's side of a crippler/ripper opposed test. Returns 0 -- no test, no wear, no event --
    when the Shield is unloaded or already worn to 0.
    """
    rating = _effective_shield(decker, state)
    if rating <= 0:
        return 0
    res = eng.shield_parry(shield_rating=rating, attacker_skill=attacker_skill)
    succ = res["successes"]
    pd = state.setdefault("program_damage", {})
    pd["shield"] = pd.get("shield", 0) + 1  # -1 Rating Point per use, win or lose
    remaining = max(0, rating - 1)
    _append_event(state, {
        "type": "shield_parry",
        "context": context,
        "shield_rating": rating,
        "shield_remaining": remaining,
        "successes": succ,
        "roll": res["roll"],
        "description": (
            f"Shield-{rating} parries the {context} hit: {succ} success"
            f"{'' if succ == 1 else 'es'} (TN {res['tn']}). "
            + (f"Shield worn to {remaining} -- reload via Swap Memory."
               if remaining > 0 else
               "Shield burned out -- reload a fresh copy via Swap Memory.")
        ),
    })
    _spend_one_shot(state, decker, "shield")
    return succ


def _effective_medic(decker: dict, state: dict) -> int:
    """Effective Medic rating = the loaded Medic utility minus its accrued per-use wear.

    Wear lives in ``state['program_damage']['medic']`` -- the SAME slot Swap Memory resets -- so
    a freshly swapped/reloaded Medic returns to full (mirrors _effective_shield). ``<= 0`` means
    the Medic is unloaded or worn out and can no longer heal the icon."""
    base = (decker.get("utilities") or {}).get("medic", 0) or 0
    worn = (state.get("program_damage") or {}).get("medic", 0)
    return max(0, base - worn)


def _current_icon_wound_level(state: dict) -> str | None:
    """Worst current wound level of the decker's persona icon, derived from the filled Condition
    Monitor boxes via the vr2 Condition Monitor Table floors (Light >= 1, Moderate >= 2,
    Serious >= 3 boxes). Returns ``None`` when the icon is undamaged. Everything at or above the
    Serious floor (including the Deadly box-range, up to the 10-box crash) reports ``"Serious"``
    -- the Medic Target Numbers Table tops out at Serious, so a worse wound still heals at TN 6."""
    boxes = (state.get("condition_monitor") or {}).get("persona_boxes", 0) or 0
    if boxes <= 0:
        return None
    if boxes >= rules.DAMAGE_BOXES["Serious"]:
        return "Serious"
    if boxes >= rules.DAMAGE_BOXES["Moderate"]:
        return "Moderate"
    return "Light"


def _apply_medic(state: dict, decker: dict) -> None:
    """Resolve a Medic action (vr2, Complex Action, self-targeted). Heals boxes of persona/icon
    Condition Monitor damage equal to the Medic Test successes -- TN set by the icon's CURRENT
    wound level (Light 4 / Moderate 5 / Serious 6) -- capped by the current damage. The Medic
    degrades 1 Rating Point per use regardless of outcome (reload a fresh copy via Swap Memory).

    Mutates ``state`` in place (condition_monitor + program_damage) and always emits a
    player-visible ``medic_heal`` event. Heals/degrades nothing when the icon is undamaged or the
    Medic is worn out / not loaded (mirrors _shield_parry, which does not wear a 0-rating Shield).
    """
    cm = state.setdefault("condition_monitor", {})
    boxes = cm.get("persona_boxes", 0) or 0
    wound = _current_icon_wound_level(state)
    if wound is None:
        _append_event(state, {
            "type": "medic_heal", "healed": 0, "persona_boxes": boxes,
            "description": "Medic: icon undamaged -- nothing to heal.",
        })
        return
    rating = _effective_medic(decker, state)
    if rating <= 0:
        _append_event(state, {
            "type": "medic_heal", "healed": 0, "persona_boxes": boxes, "wound_level": wound,
            "description": ("Medic offline (worn out or not loaded) -- reload a fresh copy via "
                            "Swap Memory before it can heal the icon."),
        })
        return
    res = eng.medic_heal(medic_rating=rating, wound_level=wound)
    healed = min(boxes, res["boxes_healed"])
    cm["persona_boxes"] = max(0, boxes - healed)
    pd = state.setdefault("program_damage", {})
    pd["medic"] = pd.get("medic", 0) + 1   # -1 Rating Point per use, win or lose
    remaining_rating = max(0, rating - 1)
    remaining_dmg = cm["persona_boxes"]
    _append_event(state, {
        "type": "medic_heal",
        "wound_level": wound,
        "healed": healed,
        "persona_boxes": remaining_dmg,
        "medic_rating": rating,
        "medic_remaining": remaining_rating,
        "decker_roll": res["roll"],
        "description": (
            f"Medic-{rating} treats the {wound.lower()} icon wound (TN {res['tn']}): "
            f"{res['boxes_healed']} success{'' if res['boxes_healed'] == 1 else 'es'} -- "
            f"{healed} box{'' if healed == 1 else 'es'} healed. Icon damage now {remaining_dmg}/10. "
            + (f"Medic worn to {remaining_rating} -- reload via Swap Memory."
               if remaining_rating > 0 else
               "Medic burned out -- reload a fresh copy via Swap Memory.")
        ),
    })
    _spend_one_shot(state, decker, "medic")


_BEMS_ORDER = ("bod", "evasion", "masking", "sensor")
_RESTORE_FALLBACK_TN = 6  # legacy runs with crippler damage but no recorded causing rating


def _record_crippler_rating(state: dict, attr: str, rating: int) -> None:
    """Record the highest crippler/ripper program rating that has caused the CURRENT temporary
    damage to a persona attribute. This is the Restore Test target number (vr2: TN = rating of the
    program that caused the damage; highest if several). Reset to 0 by _apply_restore once the
    attribute's temporary damage is fully repaired (no longer relevant)."""
    cr = state.setdefault("condition_monitor", {}).setdefault(
        "crippler_rating", {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0})
    cr[attr] = max(int(cr.get(attr, 0) or 0), int(rating or 0))


def _effective_restore(decker: dict, state: dict) -> int:
    """Effective Restore rating = the loaded Restore utility minus any crash wear in
    ``state['program_damage']['restore']`` (e.g. from Tar Baby / Hog). Unlike Medic, Restore does
    NOT self-degrade per use, so normal Restore use never changes this -- it only drops if the
    program is crashed, and a Swap Memory reload restores it to full. ``<= 0`` means the Restore is
    unloaded or crashed and cannot repair attributes."""
    base = (decker.get("utilities") or {}).get("restore", 0) or 0
    worn = (state.get("program_damage") or {}).get("restore", 0)
    return max(0, base - worn)


def _apply_restore(state: dict, decker: dict, target: str = "") -> None:
    """Resolve a Restore action (vr2, Complex Action, self-targeted defensive utility): repair the
    TEMPORARY crippler reductions to the online icon's persona attributes (Bod/Evasion/Masking/
    Sensor). Restore Test TN = the highest rating of the crippler program(s) that caused the
    targeted attribute's current damage; every 2 successes repairs 1 point, capped by the
    repairable damage present.

    Restore does NOT lose a Rating Point per use (no degradation in the rule -- unlike Medic) and
    CANNOT repair permanent Persona-chip damage from gray/black IC (Rippers); that portion is
    tracked in ``persona_chip_damage`` and is the floor below which an attribute's damage is never
    reduced. ``target`` is an optional BEMS attribute name (reuses RunActionInput.target_program);
    blank/invalid defaults to the MOST-damaged repairable attribute (ties Bod>Evasion>Masking>
    Sensor). Mutates ``state`` in place and always emits a player-visible ``restore_repair`` event.
    No-ops (with a clear message) when there is no repairable temporary damage, or the Restore is
    unloaded / crashed.
    """
    cm = state.setdefault("condition_monitor", {})
    pd = cm.setdefault("persona_damage", {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0})
    chip = cm.get("persona_chip_damage", {}) or {}
    ratings = cm.setdefault("crippler_rating", {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0})

    def repairable(a: str) -> int:
        return max(0, int(pd.get(a, 0) or 0) - int(chip.get(a, 0) or 0))

    total_repairable = sum(repairable(a) for a in _BEMS_ORDER)
    perm_total = sum(max(0, int(chip.get(a, 0) or 0)) for a in _BEMS_ORDER)

    if total_repairable <= 0:
        msg = "Restore: no temporary attribute damage to repair."
        if perm_total > 0:
            msg += (f" {perm_total} point{'' if perm_total == 1 else 's'} of permanent "
                    "Persona-chip damage (gray/black IC) cannot be repaired by Restore.")
        _append_event(state, {"type": "restore_repair", "repaired": 0, "description": msg})
        return

    # Choose the attribute: an explicit valid target WITH repairable damage, else the most-damaged
    # repairable attribute. max() returns the first maximal element in BEMS order -> the requested
    # Bod>Evasion>Masking>Sensor tie-break.
    tgt = (target or "").strip().lower()
    attr = tgt if (tgt in _BEMS_ORDER and repairable(tgt) > 0) else max(_BEMS_ORDER, key=repairable)

    rating = _effective_restore(decker, state)
    if rating <= 0:
        _append_event(state, {
            "type": "restore_repair", "repaired": 0, "attribute": attr,
            "description": ("Restore offline (crashed or not loaded) -- reload a fresh copy via "
                            "Swap Memory before it can repair attributes."),
        })
        return

    causing = int(ratings.get(attr, 0) or 0)
    if causing <= 0:  # legacy/untracked: highest recorded rating, else a sane default TN
        causing = max([int(ratings.get(a, 0) or 0) for a in _BEMS_ORDER] + [0]) or _RESTORE_FALLBACK_TN

    res = eng.restore_repair(restore_rating=rating, causing_rating=causing, damage_points=repairable(attr))
    points = res["points_repaired"]
    floor = int(chip.get(attr, 0) or 0)  # never repair below the permanent Persona-chip floor
    pd[attr] = max(floor, int(pd.get(attr, 0) or 0) - points)
    if repairable(attr) <= 0:  # temporary damage cleared -> its causing rating is no longer relevant
        ratings[attr] = 0

    now = max(1, int(decker.get(attr, 4) or 4) - int(pd.get(attr, 0) or 0))
    _append_event(state, {
        "type": "restore_repair",
        "attribute": attr,
        "repaired": points,
        "restore_rating": rating,
        "causing_rating": causing,
        "attribute_damage": pd[attr],
        "decker_roll": res["roll"],
        "description": (
            f"Restore-{rating} repairs {attr.upper()} (TN {res['tn']} = causing crippler rating): "
            f"{res['successes']} success{'' if res['successes'] == 1 else 'es'} -> "
            f"{points} point{'' if points == 1 else 's'} restored. "
            f"{attr.upper()} now {now} ({pd[attr]} damage remaining"
            + (f", {floor} permanent chip -- not repairable" if floor > 0 else "") + ")."
        ),
    })
    _spend_one_shot(state, decker, "restore")


def _effective_disinfect(decker: dict, state: dict) -> int:
    """Effective Disinfect rating = the loaded Disinfect utility minus any crash wear in
    ``state['program_damage']['disinfect']``. Like Restore, Disinfect does NOT self-degrade per
    use (no degradation in the rule), so only a crash (e.g. Tar Baby / Hog) lowers it, and a Swap
    Memory reload restores it to full. ``<= 0`` means the Disinfect is unloaded or crashed -- the
    decker carries no anti-worm defense (worm-infection TN gets +0) and cannot run the active
    Disinfect operation."""
    base = (decker.get("utilities") or {}).get("disinfect", 0) or 0
    worn = (state.get("program_damage") or {}).get("disinfect", 0)
    return max(0, base - worn)


def _apply_disinfect(state: dict, decker: dict, *, subsystem: str, subsystem_rating: int,
                     decker_pool: int, target_ic_id: str = "") -> None:
    """Resolve an active Disinfect operation (vr2, Complex Action): a System Test against the
    subsystem hosting a worm, the Disinfect utility reducing the TN. On success the targeted Worm
    lurking-IC is DESTROYED and removed -- with NO security-tally increase (this is a Disinfect,
    not a cybercombat crash). On failure the worm may infect the MPCP (the Worm Infection Test,
    against which the carried Disinfect still defends): an infection sets ``mpcp_infected`` /
    ``chip_replacement_required`` (permanent) and removes the worm; otherwise the worm survives
    and stays lurking.

    Worms are not bound to a subsystem in run state, so the decker names the subsystem they are
    cleaning (``subsystem`` / ``subsystem_rating`` -> the System Test TN) and we target the first
    lurking Worm (or the one named by ``target_ic_id``). With no lurking Worm the subsystem scans
    clean. Mutates ``state`` in place and always emits a player-visible event (``worm_disinfected``
    on a clean/failed/destroyed sweep; ``worm_resolved`` when a failure infects the MPCP)."""
    rating = _effective_disinfect(decker, state)
    if rating <= 0:
        _append_event(state, {
            "type": "worm_disinfected", "destroyed": False, "subsystem": subsystem,
            "description": ("Disinfect offline (worn out or not loaded) -- load a Disinfect "
                            "utility (Swap Memory) before you can sweep a subsystem for worms."),
        })
        return

    lurking = state.get("lurking_ic", []) or []
    tid = (target_ic_id or "").strip()
    worm = next((ic for ic in lurking
                 if ic.get("type") == "Worm" and (not tid or ic.get("id") == tid)), None)
    if worm is None:
        msg = (f"Disinfect-{rating}: no lurking worm \"{tid}\" found."
               if tid else
               f"Disinfect-{rating}: the {subsystem} subsystem scans clean -- no worm found.")
        _append_event(state, {
            "type": "worm_disinfected", "destroyed": False, "subsystem": subsystem,
            "description": msg,
        })
        return

    res = eng.disinfect_test(decker_pool=decker_pool, subsystem_rating=subsystem_rating,
                             disinfect_utility=rating)
    _spend_one_shot(state, decker, "disinfect")
    if res["worm_destroyed"]:
        # Destroyed by the Disinfect -- remove the worm. NOT a cybercombat crash: no tally add.
        state["lurking_ic"] = [ic for ic in lurking if ic.get("id") != worm["id"]]
        _append_event(state, {
            "type": "worm_disinfected", "destroyed": True, "subsystem": subsystem,
            "ic_id": worm["id"], "ic_type": "Worm", "decker_roll": res["roll"],
            "description": (
                f"Disinfect-{rating} sweeps the {subsystem} subsystem (TN {res['tn']}): "
                f"{res['roll']['successes']} success"
                f"{'' if res['roll']['successes'] == 1 else 'es'} -- "
                f"Worm-{worm['rating']} destroyed. No security alert (maintenance op)."
            ),
        })
        return

    # Failed Disinfect: the worm may infect the MPCP. The carried Disinfect still defends the
    # infection test (vr2 raises the Worm Infection Test TN by the running Disinfect rating).
    wr = eng.worm_attack(
        ic_rating=worm["rating"],
        mpcp_rating=decker.get("mpcp", 1),
        hardening=decker.get("hardening", 0),
        disinfect_utility=rating,
    )
    if wr["mpcp_infected"]:
        state["mpcp_infected"] = True
        state["chip_replacement_required"] = True
        state["lurking_ic"] = [ic for ic in lurking if ic.get("id") != worm["id"]]
        _append_event(state, {
            "type": "worm_resolved", "ic_id": worm["id"], "ic_type": "Worm",
            "outcome": "mpcp_infected", "roll": wr["roll"], "subsystem": subsystem,
            "description": (
                f"Disinfect-{rating} FAILED on the {subsystem} subsystem (TN {res['tn']}) -- "
                f"Worm-{worm['rating']} infected the MPCP. Chip replacement required (permanent)."
            ),
        })
    else:
        _append_event(state, {
            "type": "worm_disinfected", "destroyed": False, "subsystem": subsystem,
            "ic_id": worm["id"], "ic_type": "Worm", "decker_roll": res["roll"],
            "infection_roll": wr["roll"],
            "description": (
                f"Disinfect-{rating} failed to destroy Worm-{worm['rating']} on the {subsystem} "
                f"subsystem (TN {res['tn']}), but Disinfect-{rating} held off the MPCP infection "
                f"(TN {wr['tn']}). The worm is still lurking."
            ),
        })


_TAR_IC_TYPES = ("Tar Baby", "Tar Pit")


def _effective_steamroller(decker: dict, state: dict) -> int:
    """Effective Steamroller rating = the loaded Steamroller utility minus any crash wear in
    ``state['program_damage']['steamroller']``. Steamroller is IMMUNE to the tar programs it hunts
    (a Tar Baby / Tar Pit can never crash it -- vr2_rules.md L1581-1585), so a tar strike never
    lowers it; only an unrelated crash source (e.g. a Hog virus drain) reduces it, and a Swap
    Memory reload restores it to full. ``<= 0`` means the Steamroller is unloaded or crashed -- the
    decker carries no anti-tar weapon."""
    base = (decker.get("utilities") or {}).get("steamroller", 0) or 0
    worn = (state.get("program_damage") or {}).get("steamroller", 0)
    return max(0, base - worn)


def _apply_steamroller(state: dict, decker: dict, *, sec_code: str,
                       decker_pool: int, target_ic_id: str = "") -> None:
    """Resolve a Steamroller utility strike (vr2_rules.md L1581-1585): the dedicated anti-tar
    weapon. It inflicts (Rating)D on a Tar Baby / Tar Pit IC and is IMMUNE to the tar programs'
    destructive backlash -- so unlike every other utility that touches a tar IC, Steamroller NEVER
    runs the opposed tar crash test (``tar_baby_test``) and the decker's loaded utilities are never
    crashed or corrupted (a Tar Pit's "corrupt all copies" path therefore can never fire here).

    Tar IC are GM-only lurking IC ({id, type "Tar Baby"/"Tar Pit", rating, status "lurking"}). The
    decker names the tar to crush (``target_ic_id``; with none we take the first lurking tar).
    Steamroller targets ONLY tar IC -- naming a non-tar IC is rejected (400).

    On a crash the tar is removed and its rating is added to the security tally UNLESS masked: the
    Steamroller's Stealth/Skulk option reduces the bump (mirrors the Attack-utility skulk rule --
    read from ``program_options['steamroller'].skulk``), and a SUPPRESSED tar adds no tally at all
    ("...unless the Steamroller has the Stealth option or the decker suppresses the IC"). A
    non-crashing strike just accumulates boxes on the tar's shallow monitor; it stays lurking.
    Always emits a player-visible ``tar_steamrolled`` event (the decker is attacking the tar, so it
    learns the result; the running tally figure is auto-redacted for non-admins)."""
    rating = _effective_steamroller(decker, state)
    if rating <= 0:
        _append_event(state, {
            "type": "tar_steamrolled", "destroyed": False,
            "description": ("Steamroller offline (worn out or not loaded) -- load a Steamroller "
                            "utility (Swap Memory) before you can crush a tar IC."),
        })
        return

    lurking = state.get("lurking_ic", []) or []
    tid = (target_ic_id or "").strip()
    if tid:
        target = next((ic for ic in lurking if ic.get("id") == tid), None)
        if target is not None and target.get("type") not in _TAR_IC_TYPES:
            # Steamroller is a tar-only weapon; reject any other IC type with a clear message.
            raise HTTPException(
                400,
                f"Steamroller can only target Tar Baby / Tar Pit IC -- "
                f"\"{target.get('type', 'that IC')}\" is not a tar program.",
            )
    else:
        target = next((ic for ic in lurking if ic.get("type") in _TAR_IC_TYPES), None)

    if target is None:
        msg = (f"Steamroller-{rating}: no lurking tar IC \"{tid}\" found."
               if tid else
               f"Steamroller-{rating}: no tar IC present to crush.")
        _append_event(state, {
            "type": "tar_steamrolled", "destroyed": False, "description": msg,
        })
        return

    sr_opts = (decker.get("program_options") or {}).get("steamroller") or {}
    to_hit_tn = rules.COMBAT_TN[sec_code]["intruding"]
    if bool(sr_opts.get("targeting")):
        to_hit_tn = max(2, to_hit_tn - 2)   # Targeting option: -2 to-hit TN

    res = eng.steamroller_attack(
        steamroller_rating=rating,
        steamroller_pool=decker_pool,
        tar_ic_rating=target.get("rating", 1),
        to_hit_tn=to_hit_tn,
        existing_boxes=target.get("boxes", 0),
    )
    _spend_one_shot(state, decker, "steamroller")
    # IMMUNITY: no tar_baby_test is run -- the tar program cannot crash the Steamroller, and the
    # decker's loaded utilities / program_damage are deliberately left untouched here.

    if not res["crashed"]:
        target["boxes"] = res["total_boxes"]
        _append_event(state, {
            "type": "tar_steamrolled", "destroyed": False,
            "ic_id": target["id"], "ic_type": target["type"], "decker_roll": res["to_hit_roll"],
            "description": (
                f"Steamroller-{rating} hits {target['type']}-{target.get('rating', 0)} for "
                f"{res['damage_level']} ({res['total_boxes']}/{res['tar_cm']}) -- it holds and "
                f"stays lurking."
            ),
        })
        return

    # Crashed: remove the tar IC. Tally add unless Stealth(Skulk)-masked or the tar is suppressed.
    state["lurking_ic"] = [ic for ic in lurking if ic.get("id") != target["id"]]
    ic_rating = target.get("rating", 0)
    skulk = max(0, int(sr_opts.get("skulk", 0) or 0))
    if target.get("suppressed"):
        tally_increase = 0
        note = " (IC suppressed -- silent crash, no tally)"
    else:
        tally_increase = max(0, ic_rating - skulk)
        note = (f" (Stealth/Skulk-{skulk} masked the crash)"
                if skulk > 0 and tally_increase < ic_rating else "")
    state["security_tally"] += tally_increase
    _append_event(state, {
        "type": "tar_steamrolled", "destroyed": True,
        "ic_id": target["id"], "ic_type": target["type"], "decker_roll": res["to_hit_roll"],
        "description": (
            f"Steamroller-{rating} CRUSHES {target['type']}-{ic_rating} ({res['damage_level']}). "
            f"Tally +{tally_increase} -> {state['security_tally']}{note}"
        ),
        "tally_increase": tally_increase,
    })
    if tally_increase:
        _check_and_activate_sheaf(state, sec_code)


def _effective_slow(decker: dict, state: dict) -> int:
    """Effective Slow rating = the loaded Slow utility minus any crash wear in
    ``state['program_damage']['slow']``. Slow is an offensive program with no per-use degradation
    clause (unlike Armor / Shield), so only an unrelated crash source (e.g. a Hog virus drain)
    lowers it and a Swap Memory reload restores it to full. ``<= 0`` means the decker carries no
    Slow program."""
    base = (decker.get("utilities") or {}).get("slow", 0) or 0
    worn = (state.get("program_damage") or {}).get("slow", 0)
    return max(0, base - worn)


def _slow_target_eligibility(ic: dict) -> tuple[bool, str]:
    """Whether the Slow utility may target this active IC (vr2_rules.md L1573): PROACTIVE IC ONLY.
    Reactive IC are immune; a trace IC is vulnerable ONLY during its Hunt Cycle (``trace_phase``
    "hunt"), not once it has begun its Location Cycle. Returns ``(ok, reason)`` -- ``reason`` is the
    400 message when ``ok`` is False."""
    info = rules.IC_CATALOG.get(_canonical_ic_type(ic.get("type", "")), {})
    if info.get("subtype", "") == "trace":
        if ic.get("trace_phase", "hunt") != "hunt":
            return False, ("trace IC can only be slowed during its Hunt Cycle -- this one has "
                           "begun its Location Cycle and is no longer vulnerable to Slow.")
        return True, ""
    if info.get("ic_type") != "proactive":
        return False, "reactive IC are immune to Slow -- only proactive IC can be slowed."
    return True, ""


def _apply_slow(state: dict, decker: dict, *, sec_code: str,
                decker_pool: int, target_ic_id: str = "") -> None:
    """Resolve a Slow utility strike (vr2_rules.md L1572-1578): reduce a proactive IC's execution
    speed. A to-hit Computer Test (``decker_pool`` vs the host combat TN, eased -2 by the Slow
    program's Targeting option) must land; then an opposed Resistance (Slow Rating) Test is rolled
    for the IC (``eng.slow_test``). If the attacker wins the IC loses one action per 2 net successes
    (at least one on a win); if that empties its remaining actions for the Combat Turn it HANGS
    (does nothing for the rest of the turn). The proactive-IC loop reads ``ic['actions_lost']`` to
    skip the lost passes, and ``new_turn`` clears the slow so the IC resumes -- UNLESS it is still
    suppressed. Reactive IC are immune and a trace IC is only vulnerable during its Hunt Cycle
    (both rejected with 400).

    Targets the GM-only active proactive/trace IC in ``state['active_ic']``; the decker names the IC
    (``target_ic_id``; with none we take the first eligible proactive IC). Always emits a
    player-visible ``ic_slowed`` event (the decker is attacking the IC, so it learns the result):
    outcome ``offline`` / ``no_target`` / ``missed`` / ``resisted`` / ``slowed`` / ``hung``."""
    rating = _effective_slow(decker, state)
    if rating <= 0:
        _append_event(state, {
            "type": "ic_slowed", "outcome": "offline",
            "description": ("Slow offline (worn out or not loaded) -- load a Slow utility "
                            "(Swap Memory) before you can slow a proactive IC."),
        })
        return

    active = [ic for ic in (state.get("active_ic") or [])
              if ic.get("status") == "active" and not ic.get("suppressed")]
    tid = (target_ic_id or "").strip()
    if tid:
        target = next((ic for ic in active if ic.get("id") == tid), None)
    else:
        target = next((ic for ic in active if _slow_target_eligibility(ic)[0]), None)

    if target is None:
        msg = (f"Slow-{rating}: no active IC \"{tid}\" found to slow."
               if tid else
               f"Slow-{rating}: no eligible proactive IC present to slow.")
        _append_event(state, {
            "type": "ic_slowed", "outcome": "no_target", "description": msg,
        })
        return

    ok, reason = _slow_target_eligibility(target)
    if not ok:
        raise HTTPException(
            400,
            f"Slow cannot target {target.get('type', 'that IC')}-"
            f"{target.get('rating', '?')}: {reason}",
        )

    # -- To-hit: Computer Test (decker_pool) vs the host combat TN; Targeting eases it -2 --------
    ic_status = "legitimate" if state.get("has_legitimate_status") else "intruding"
    to_hit_tn = rules.COMBAT_TN[sec_code][ic_status]
    slow_opts = (decker.get("program_options") or {}).get("slow") or {}
    if bool(slow_opts.get("targeting")):
        to_hit_tn = max(2, to_hit_tn - 2)
    ic_rating = target.get("rating", 1)
    to_hit = eng.roll_dice(max(1, decker_pool), to_hit_tn)
    _spend_one_shot(state, decker, "slow")
    if to_hit["successes"] <= 0:
        _append_event(state, {
            "type": "ic_slowed", "outcome": "missed",
            "ic_id": target["id"], "ic_type": target["type"], "ic_rating": ic_rating,
            "decker_roll": to_hit,
            "description": (f"Slow-{rating} vs {target['type']}-{ic_rating}: missed "
                            f"(0 hits vs TN {to_hit_tn}) -- the IC keeps its speed."),
        })
        return

    # -- Opposed Resistance (Slow Rating) Test for the IC ---------------------------------------
    res = eng.slow_test(decker_pool=rating, slow_rating=rating, ic_dice=ic_rating)
    net = res["net_successes"]
    if net <= 0:
        _append_event(state, {
            "type": "ic_slowed", "outcome": "resisted",
            "ic_id": target["id"], "ic_type": target["type"], "ic_rating": ic_rating,
            "decker_roll": res["decker_roll"], "ic_roll": res["ic_roll"], "net_successes": net,
            "description": (f"Slow-{rating} hits {target['type']}-{ic_rating}, but the IC RESISTS "
                            f"the opposed Slow test ({res['decker_roll']['successes']} vs "
                            f"{res['ic_roll']['successes']}) -- no effect."),
        })
        return

    # Attacker wins: lose one action per 2 net successes (at least one on a win). The IC's actions
    # this turn = ceil(Initiative / 10) passes; losing them all HANGS it for the rest of the turn.
    lost_now = max(1, res["actions_lost"])
    cur_turn = state.get("current_turn", 1)
    ic_passes = _init_passes(target.get("initiative", 0))
    prev_lost = target.get("actions_lost", 0) if target.get("slow_turn") == cur_turn else 0
    new_lost = min(ic_passes, prev_lost + lost_now)
    target["actions_lost"] = new_lost
    target["slow_turn"] = cur_turn
    remaining = ic_passes - new_lost
    if remaining <= 0:
        target["hung_turn"] = cur_turn
        outcome = "hung"
        tail = ("it HANGS -- no actions left this Combat Turn "
                "(resumes next turn unless suppressed).")
    else:
        outcome = "slowed"
        tail = (f"it loses {lost_now} action(s) this turn "
                f"({remaining} of {ic_passes} remaining).")
    _append_event(state, {
        "type": "ic_slowed", "outcome": outcome,
        "ic_id": target["id"], "ic_type": target["type"], "ic_rating": ic_rating,
        "decker_roll": res["decker_roll"], "ic_roll": res["ic_roll"],
        "net_successes": net, "actions_lost": new_lost, "hung": remaining <= 0,
        "description": (f"Slow-{rating} beats {target['type']}-{ic_rating} on the opposed test "
                        f"(net {net}) -- {tail}"),
    })


# -- DINAB ("Decker In A Box") program option (vr2_rules.md L1665) -------------------------------
# DINAB gives a utility a built-in Computer skill = the DINAB rating. The decker may spend a Free
# Action to let ONE DINAB-equipped program run itself autonomously (skill = effective DINAB rating)
# while still spending their Complex/2-Simple on their own action -- effectively a second ally that
# fires for free each pass. DINAB degrades -1 each time the program FAILS (lost opposed System Test,
# missed cybercombat, or target reduces all damage to 0); a FAILED roll of all 1s CRASHES it (reload
# via Swap Memory). Build-time rating is carried in decker["program_options"][util].dinab. Wear is
# tracked in state["dinab_damage"][util] (player-visible -- the decker's own deck); a crash sets
# program_damage[util]=base (effective-0, reload via Swap Mode-3) and clears the dinab wear (a fresh
# copy is pristine). Operational ops fire the autonomous program through a generic System Test; the
# six offensive utilities reuse the cybercombat / crippler resolution at pool = DINAB rating.
_DINAB_OFFENSIVE = ("attack", "poison", "restrict", "reveal", "black_hammer", "killjoy")


def _effective_dinab(decker: dict, state: dict, util: str) -> int:
    """Effective DINAB rating for ``util`` = its built-in DINAB option rating
    (decker.program_options[util].dinab) minus accumulated dinab wear (state.dinab_damage[util]).
    Returns 0 when the program is not DINAB-equipped, not loaded, or has crashed (program_damage
    >= its base utility rating), so the caller refuses to run a worn-out / offline DINAB."""
    key = _normalize_util_name(util)
    base = int(((decker.get("program_options") or {}).get(key) or {}).get("dinab", 0) or 0)
    if base <= 0:
        return 0
    util_base = int((decker.get("utilities") or {}).get(key, 0) or 0)
    if util_base <= 0:
        return 0  # the program itself is not loaded -- nothing for DINAB to drive
    if int((state.get("program_damage") or {}).get(key, 0) or 0) >= util_base:
        return 0  # the program crashed (reload via Swap Memory) -- DINAB cannot run it
    worn = int((state.get("dinab_damage") or {}).get(key, 0) or 0)
    return max(0, base - worn)


def _degrade_dinab(state: dict, util: str) -> None:
    """A DINAB program failed a test (-1 rating): bump its wear by one point."""
    key = _normalize_util_name(util)
    dd = state.setdefault("dinab_damage", {})
    dd[key] = int(dd.get(key, 0) or 0) + 1


def _crash_dinab(state: dict, decker: dict, util: str) -> None:
    """A DINAB program rolled all 1s on a failed test -> it CRASHES. Marks the program spent
    (program_damage[util] = base, so _effective_* reads 0 until a Swap Memory reload clears it) and
    clears the dinab wear (the reloaded copy is fresh). Emits a player-visible dinab_crashed event."""
    key = _normalize_util_name(util)
    base = int((decker.get("utilities") or {}).get(key, 0) or 0)
    if base > 0:
        state.setdefault("program_damage", {})[key] = base
    (state.get("dinab_damage") or {}).pop(key, None)
    _append_event(state, {
        "type": "dinab_crashed", "utility": key,
        "description": (
            f"The DINAB-driven {key.replace('_', ' ').title()} rolled all 1s and CRASHED -- "
            "reload a fresh copy via Swap Memory before running it autonomously again."
        ),
    })


def _dinab_resolve_failure(state: dict, decker: dict, util: str, failed: bool, all_ones: bool) -> None:
    """Apply the DINAB degrade / crash rule after a run: a failed test costs -1 rating; a failed
    all-1s test crashes the program. A success leaves it untouched."""
    if not failed:
        return
    if all_ones:
        _crash_dinab(state, decker, util)
    else:
        _degrade_dinab(state, util)
        _append_event(state, {
            "type": "dinab_degraded", "utility": _normalize_util_name(util),
            "description": (
                f"The DINAB-driven {util.replace('_', ' ').title()} failed -- its rating drops 1 "
                f"(now {_effective_dinab(decker, state, util)})."
            ),
        })


def _apply_dinab(state: dict, decker: dict, *, util: str, sec_code: str, sec_value: int,
                 subsystem: str, subsystem_rating: int, det_factor: int,
                 target_ic_id: str = "", target_file: str = "") -> None:
    """Run one DINAB-equipped program autonomously for the decker's Free Action (vr2_rules.md
    L1665). The program acts at skill = effective DINAB rating with NO extra Complex/Simple spend.
    Offensive utilities (attack / poison / restrict / reveal / black_hammer / killjoy) reuse the
    cybercombat / crippler resolution; everything else runs a generic System Test. A failed run
    degrades DINAB (-1); a failed all-1s run crashes it. <=0 effective DINAB is rejected (400)."""
    key = _normalize_util_name(util)
    if not key:
        raise HTTPException(400, "DINAB needs target_program -- the DINAB-equipped utility to run.")
    eff = _effective_dinab(decker, state, key)
    if eff <= 0:
        raise HTTPException(
            400,
            f"{key.replace('_', ' ').title()} has no usable DINAB rating (not DINAB-equipped, "
            "worn out, or crashed -- reload via Swap Memory).")
    if key in _DINAB_OFFENSIVE:
        _dinab_offense(state, decker, key, eff, sec_code=sec_code, target_ic_id=target_ic_id)
    else:
        _dinab_operate(state, decker, key, eff, subsystem=subsystem,
                       subsystem_rating=subsystem_rating, sec_value=sec_value, det_factor=det_factor)


def _dinab_operate(state: dict, decker: dict, util: str, eff: int, *, subsystem: str,
                   subsystem_rating: int, sec_value: int, det_factor: int) -> None:
    """A DINAB operational program runs one autonomous System Test at pool = DINAB rating vs the
    named subsystem. Tally rises by the host's successes; a lost opposed test degrades DINAB (-1)
    and an all-1s loss crashes it. Emits a player-visible dinab_op event."""
    test = eng.system_test(decker_pool=eff, subsystem_rating=subsystem_rating,
                           security_value=sec_value, det_factor=det_factor)
    state["security_tally"] = state.get("security_tally", 0) + test["tally_increase"]
    failed = not test["success"]
    dr = test["decker_roll"]
    all_ones = failed and dr.get("ones", 0) >= dr.get("pool", 0) and dr.get("successes", 0) == 0
    _append_event(state, {
        "type": "dinab_op", "utility": util, "subsystem": subsystem, "success": test["success"],
        "decker_roll": dr, "host_roll": test["host_roll"],
        "tally_increase": test["tally_increase"], "tally_total": state["security_tally"],
        "description": (
            f"DINAB {util.replace('_', ' ').title()}-{eff} runs the {subsystem} subsystem itself -- "
            f"{'SUCCESS' if test['success'] else 'FAILED'} "
            f"({dr['successes']} vs {test['host_roll']['successes']}). "
            f"Tally +{test['tally_increase']} -> {state['security_tally']}."
        ),
    })
    _dinab_resolve_failure(state, decker, util, failed, all_ones)
    if test["tally_increase"]:
        _check_and_activate_sheaf(state, state.get("host_security_code", "Green"))


def _dinab_offense(state: dict, decker: dict, util: str, eff: int, *, sec_code: str,
                   target_ic_id: str = "") -> None:
    """A DINAB offensive program fires autonomously at pool = DINAB rating. 'attack' hits an active
    IC (or a revealed enemy decker by id); the cripplers / lethal programs hit a revealed enemy
    decker. A miss or all-damage-resisted run degrades DINAB; an all-1s miss crashes it."""
    enemies = [e for e in (state.get("enemy_deckers") or [])
               if e.get("status") == "active" and e.get("revealed")]
    enemy = next((e for e in enemies if e.get("id") == target_ic_id), None) if target_ic_id else None

    if util != "attack" and enemy is None:
        enemy = next(iter(enemies), None)
    if util != "attack" and enemy is None:
        raise HTTPException(400, f"DINAB {util}: no revealed enemy decker to target.")

    if util == "attack" and enemy is None:
        active = [ic for ic in (state.get("active_ic") or []) if ic.get("status") == "active"]
        target_ic = next((ic for ic in active if ic.get("id") == target_ic_id), None) if target_ic_id else None
        if target_ic is None:
            target_ic = next(iter(active), None)
        if target_ic is None:
            raise HTTPException(400, "DINAB attack: no active IC or enemy decker to attack.")
        failed, all_ones = _dinab_attack_ic(state, decker, target_ic, eff, sec_code)
        _dinab_resolve_failure(state, decker, util, failed, all_ones)
        return

    failed, all_ones = _dinab_strike_decker(state, decker, enemy, eff, sec_code, util)
    _dinab_resolve_failure(state, decker, util, failed, all_ones)


def _dinab_attack_ic(state: dict, decker: dict, target_ic: dict, eff: int, sec_code: str) -> tuple[bool, bool]:
    """DINAB Attack vs an active IC at pool = DINAB rating. Returns (failed, all_ones); failed when
    no damage lands (miss or fully resisted). On a crash the IC is removed and tally rises (Skulk
    reduces the bump). Returns crash dinab on a failed all-1s roll to the caller."""
    sec_value = state["host_security_value"]
    opts = (decker.get("program_options") or {}).get("attack") or {}
    cluster_penalty = _cluster_size(state, target_ic.get("cluster_id"))
    shield_shift = _shield_shift_tn_modifier(target_ic, penetration=bool(opts.get("penetration")),
                                             chaser=bool(opts.get("chaser")))
    tn = rules.COMBAT_TN[sec_code]["intruding"] + cluster_penalty + shield_shift
    if opts.get("targeting"):
        tn = max(2, tn - 2)
    attack_roll = eng.roll_dice(max(1, eff), tn)
    base_dmg = rules.IC_DAMAGE_LEVEL[sec_code]
    resist_tn = rules.COMBAT_TN[sec_code]["intruding"] + cluster_penalty
    if _ic_has_armor(target_ic):
        resist_tn = max(2, resist_tn - 2)
    resist_pool = max(1, sec_value + _ic_expert(target_ic, "defense") - _ic_expert(target_ic, "offense"))
    resist_roll = eng.roll_dice(resist_pool, resist_tn)
    staged = eng.stage_damage(base_dmg, attack_roll["successes"], 1)
    final_dmg = eng.stage_damage(staged, resist_roll["successes"], -1)
    boxes = rules.DAMAGE_BOXES[final_dmg]
    target_ic["boxes"] = target_ic.get("boxes", 0) + boxes
    failed = attack_roll["successes"] <= 0  # a true miss (damage always lands >=1 box otherwise)
    all_ones = attack_roll.get("ones", 0) >= attack_roll.get("pool", 0) and attack_roll["successes"] == 0
    if target_ic["boxes"] >= 10:
        target_ic["status"] = "crashed"
        skulk = max(0, int(opts.get("skulk", 0) or 0))
        bump = max(0, target_ic["rating"] - skulk)
        state["security_tally"] += bump
        _append_event(state, {
            "type": "ic_crashed", "ic_id": target_ic["id"], "tally_increase": bump,
            "description": (f"DINAB Attack-{eff} CRASHED {target_ic['type']}-{target_ic['rating']}. "
                            f"Tally +{bump} -> {state['security_tally']}"),
        })
        _check_and_activate_sheaf(state, sec_code)
        return False, False
    _append_event(state, {
        "type": "dinab_attack", "ic_id": target_ic["id"], "success": not failed,
        "decker_roll": attack_roll,
        "description": (f"DINAB Attack-{eff} hits {target_ic['type']}-{target_ic['rating']}: "
                        f"{final_dmg} ({boxes} boxes), IC {target_ic['boxes']}/10."),
    })
    return failed, all_ones


def _dinab_strike_decker(state: dict, decker: dict, enemy: dict, eff: int, sec_code: str,
                         util: str) -> tuple[bool, bool]:
    """DINAB offensive strike vs an enemy decker at pool = DINAB rating. attack -> icon damage;
    poison/restrict/reveal -> cripple Bod/Evasion/Masking; black_hammer/killjoy -> lethal feedback.
    Returns (failed, all_ones); failed when the strike does nothing (no reduction / no boxes)."""
    util_r = decker.get("utilities") or {}
    if util in ("poison", "restrict", "reveal"):
        attr = {"poison": "bod", "restrict": "evasion", "reveal": "masking"}[util]
        target_rating = max(1, int(enemy.get(attr, 1) or 1))
        cr = eng.decker_attribute_attack(attacker_pool=eff, security_code=sec_code,
                                         target_status="intruding",
                                         program_rating=int(util_r.get(util, eff) or eff),
                                         target_attribute_rating=target_rating)
        reduction = cr["reduction"]
        new_val = max(1, target_rating - reduction)
        enemy[attr] = new_val
        if attr == "masking":
            enemy["detection_factor"] = eng.detection_factor(new_val, int((enemy.get("utilities") or {}).get("sleaze", 0) or 0))
        ar = cr["attack_roll"]
        _append_event(state, {"type": "dinab_attack", "enemy_id": enemy["id"], "utility": util,
            "success": reduction > 0, "decker_roll": ar,
            "description": f"DINAB {util.title()}-{eff} crips {enemy['name']} {attr} -> {new_val}."})
        return reduction <= 0, ar.get("ones", 0) >= ar.get("pool", 0) and ar["successes"] == 0
    if util in ("black_hammer", "killjoy"):
        cap = (max(1, int(decker.get("computer_skill", 1) or 1)) + 1) // 2
        rating = max(1, min(int(util_r.get(util, eff) or eff), cap))
        ar = eng.roll_dice(eff, max(2, rules.COMBAT_TN[sec_code]["intruding"]))
        resist = eng.damage_resistance(bod=max(1, int(enemy.get("bod", 1) or 1)), power=rating,
                                       base_damage_level=_LETHAL_BASE_LEVEL,
                                       attacker_successes=ar["successes"])
        boxes = resist["boxes"]
        ecm = enemy.setdefault("condition_monitor", {})
        ecm["persona_boxes"] = ecm.get("persona_boxes", 0) + boxes
        if ecm["persona_boxes"] >= 10:
            enemy["status"] = "crashed"
            _roll_enemy_mpcp_damage(enemy, rating, pool_multiplier=2)
        _append_event(state, {"type": "dinab_attack", "enemy_id": enemy["id"], "utility": util,
            "success": boxes > 0, "decker_roll": ar,
            "description": f"DINAB {util.replace('_',' ').title()}-{eff} hits {enemy['name']} ({boxes} boxes)."})
        return ar["successes"] <= 0, ar.get("ones", 0) >= ar.get("pool", 0) and ar["successes"] == 0
    atk = eng.cybercombat_attack(attacker_pool=eff, security_code=sec_code, target_status="intruding",
                                 target_bod=enemy["bod"], ic_rating=int(util_r.get("attack", 4) or 4),
                                 attacker_is_ic=False)
    boxes = atk["resistance"]["boxes"]
    ecm = enemy.setdefault("condition_monitor", {})
    ecm["persona_boxes"] = ecm.get("persona_boxes", 0) + boxes
    if ecm["persona_boxes"] >= 10:
        enemy["status"] = "crashed"
    ar = atk["attack_roll"]
    _append_event(state, {"type": "dinab_attack", "enemy_id": enemy["id"], "utility": "attack",
        "success": boxes > 0, "decker_roll": ar,
        "description": f"DINAB Attack-{eff} strikes {enemy['name']} ({boxes} boxes)."})
    return ar["successes"] <= 0, ar.get("ones", 0) >= ar.get("pool", 0) and ar["successes"] == 0


def _effective_compressor(decker: dict) -> int:
    """Effective Compressor rating = the loaded Compressor utility (vr2_rules.md L1512-1515).
    Unlike Slow / Steamroller, Compressor is a passive data-handling tool that NEVER wears with use
    (the rule lists no degradation), so there is deliberately NO ``program_damage`` subtraction here
    -- a loaded Compressor is always at full rating. ``<= 0`` means the decker carries no Compressor,
    so downloads store at full size."""
    return (decker.get("utilities") or {}).get("compressor", 0) or 0


def _compressed_store_size(compressor: int, density: int) -> tuple[int, bool]:
    """Compute the on-deck stored footprint of a downloaded file given the carried Compressor
    rating (vr2_rules.md L1512-1515: "Reduces size of data being transferred by 50%. Max file size
    is Program Rating * 100 Mp"). A file is COMPRESSIBLE iff a Compressor is loaded (rating > 0) AND
    the file is within the Rating * 100 Mp cap. A compressible file stores at HALF size, rounded UP
    so a 1 Mp file never collapses to 0 Mp (``(density + 1) // 2``); otherwise it stores at full
    size. Returns ``(stored_mp, compressible)``. The single source of truth shared by the download
    storage pre-check and the download success handler so they always agree on the footprint."""
    density = max(0, int(density or 0))
    if compressor > 0 and density <= compressor * 100:
        return (density + 1) // 2, True
    return density, False


def _apply_decompress(state: dict, decker: dict, *, target_file: str) -> None:
    """Resolve a Decompress File action (vr2_rules.md L1512-1515: "Files must be decompressed before
    being able to read or use them"). Pure storage bookkeeping with NO dice/test -- like Swap Memory
    -- it expands a chosen COMPRESSED downloaded file back to its full size on the deck.

    When deck storage is tracked the expansion needs the extra ``full_size_mp - stored`` free Mp
    (the rule's "Decks must have sufficient active memory to hold the uncompressed size of the
    file" -- this app models one storage pool, so that requirement is enforced here at decompress
    time rather than at download time). If there isn't room the action is REJECTED (400) and NOT
    spent. On success ``storage_used_mp`` grows by the delta, the ledger entry's ``size_mp`` grows
    back to ``full_size_mp``, and the ``compressed`` flag is cleared on BOTH the ledger entry and
    the matching paydata row, then a player-visible ``file_decompressed`` event is emitted. When
    storage is untracked (``storage_free_mp`` < 0) the storage math is skipped but the flag is still
    cleared and the event still fires. A missing or already-uncompressed target is a no-op event
    (never a crash)."""
    name = (target_file or "").strip()
    ledger = state.get("downloaded_files") or []
    entry = next((f for f in ledger
                  if str(f.get("name", "")).strip().lower() == name.lower()
                  and f.get("compressed")), None)
    if not name or entry is None:
        _append_event(state, {
            "type": "file_decompressed", "outcome": "no_target",
            "description": (
                f"Decompress: no compressed file \"{name}\" in storage to expand."
                if name else
                "Decompress: name a compressed downloaded file to expand."
            ),
        })
        return

    stored = max(0, int(entry.get("size_mp", 0) or 0))
    full = max(stored, int(entry.get("full_size_mp", stored) or stored))
    delta = full - stored

    free = state.get("storage_free_mp", -1)
    tracked = free is not None and free >= 0
    if tracked:
        remaining = max(0, free - state.get("storage_used_mp", 0))
        if delta > remaining:
            raise HTTPException(
                400,
                f"Not enough deck storage to decompress \"{entry.get('name')}\": needs {delta} "
                f"more Mp ({full} Mp uncompressed) but only {remaining} Mp free. Purge stored "
                "files or free storage memory first."
            )
        state["storage_used_mp"] = state.get("storage_used_mp", 0) + delta

    # Expand the ledger entry and clear the compressed flag on it AND the matching paydata row
    # (the file can now be read/used).
    entry["size_mp"] = full
    entry["compressed"] = False
    nm = str(entry.get("name", "")).strip().lower()
    for p in (state.get("paydata") or []):
        if str(p.get("name", "")).strip().lower() == nm:
            p["compressed"] = False

    free2 = state.get("storage_free_mp", -1)
    tracked2 = free2 is not None and free2 >= 0
    remaining2 = max(0, free2 - state.get("storage_used_mp", 0)) if tracked2 else None
    if tracked2:
        desc = (f"Decompressed \"{entry.get('name')}\" -> {full} Mp. "
                f"Storage used {state.get('storage_used_mp', 0)} Mp; {remaining2} Mp free.")
    else:
        desc = f"Decompressed \"{entry.get('name')}\" -> {full} Mp (storage untracked)."
    _append_event(state, {
        "type": "file_decompressed", "outcome": "expanded",
        "file_name": entry.get("name"),
        "size_mp": full,
        "storage_used_mp": state.get("storage_used_mp", 0),
        "storage_remaining_mp": remaining2,
        "description": desc,
    })


def _detonate_data_bomb(state: dict, decker: dict, eff: dict, *, ic_rating: int,
                        sec_value: int, sec_code: str, headline: str) -> dict:
    """Resolve a Data Bomb explosion (vr2_rules.md L475-480): a fixed (IC Rating)M against the
    persona (Bod resists, the Armor utility reduces Power, a Shield parry stages the resolved
    damage down), then add the bomb's rating to the security tally and check the sheaf. Mutates
    ``state`` in place and emits a player-visible ``data_bomb`` detonated event headed by
    ``headline`` (e.g. "DATA BOMB on Monthly Payroll"). Returns the detonation result dict.

    Single source of truth for the three ways a bomb goes off: an undefused access trigger, an
    all-1s botched defuse, and an Exploding Scramble's linked bomb."""
    shield_succ = _shield_parry(state, decker, attacker_skill=sec_value, context="data bomb")
    det = eng.data_bomb_detonate(
        ic_rating=ic_rating, target_bod=eff["bod"],
        armor_rating=(decker.get("utilities") or {}).get("armor", 0),
        shield_successes=shield_succ)
    cm = state.setdefault("condition_monitor", {})
    cm["persona_boxes"] = cm.get("persona_boxes", 0) + det["resistance"]["boxes"]
    state["security_tally"] += det["tally_increase"]
    _append_event(state, {
        "type": "data_bomb", "outcome": "detonated",
        "damage_level": det["resistance"]["final_damage_level"],
        "tally_increase": det["tally_increase"],
        "description": (
            f"{headline} detonated -- "
            f"{det['resistance']['final_damage_level']} damage; tally "
            f"+{det['tally_increase']} -> {state['security_tally']}."
        ),
    })
    _check_and_activate_sheaf(state, sec_code)
    return det


def _effective_defuse(decker: dict, state: dict) -> int:
    """Effective Defuse rating = the carried Defuse utility minus any crash wear in
    ``state['program_damage']['defuse']``. Like Disinfect/Restore, Defuse does NOT self-degrade
    per use (no degradation in the rule), so only a crash (e.g. Tar Baby / Hog) lowers it and a
    Swap Memory reload restores it to full. ``<= 0`` means the decker carries no Defuse, so the
    defuse TN gets no reduction (= the bare Files/Slave rating)."""
    base = (decker.get("utilities") or {}).get("defuse", 0) or 0
    worn = (state.get("program_damage") or {}).get("defuse", 0)
    return max(0, base - worn)


def _apply_defuse_bomb(state: dict, decker: dict, eff: dict, *, subsystem: str,
                       subsystem_rating: int, decker_pool: int, sec_value: int, sec_code: str,
                       target_file: str = "") -> None:
    """Resolve a deliberate Defuse Data Bomb operation (vr2_rules.md L463-471, Complex Action): a
    Computer Test against the controlling subsystem rating (Files for a file bomb, Slave for a
    device bomb -- the decker selects the subsystem) reduced by the carried Defuse utility.

    - Success (>=1 hit) disarms the bomb with NO security-tally increase: a successful defuse is
      not a crash, so the bomb's rating is never added to the tally and no suppression is needed.
    - Rolling ALL 1s detonates the bomb immediately (botch).
    - Any other failure leaves the bomb primed -- the decker may try again (or it triggers later
      if they access the protected target).

    The defuse models only the decker's Computer Test (no opposed-Security tally), matching the
    pure ``data_bomb_defuse`` helper and the no-tally rule. Targets the bomb on ``target_file``
    (trailing-segment match) or the first still-armed bomb when none is named. Mutates ``state``
    and always emits a player-visible ``data_bomb`` event."""
    armed = state.get("data_bombs") or []
    defused = set(state.get("defused_bombs") or [])
    tgt = (target_file or "").strip().lower()
    bomb = next((b for b in armed
                 if b.get("target") not in defused
                 and (not tgt or _target_file_name(b.get("target", "")).lower() == tgt)), None)
    if bomb is None:
        _append_event(state, {
            "type": "data_bomb", "outcome": "no_target",
            "description": (
                (f"No armed data bomb on \"{target_file}\" to defuse." if tgt
                 else "No armed data bomb detected on this host to defuse.")
                + " Detect one first with Analyze Icon on the protected file/device."
            ),
        })
        return

    btarget = bomb.get("target")
    brating = bomb.get("rating", 6)
    defuse_rating = _effective_defuse(decker, state)
    df = eng.data_bomb_defuse(decker_pool=decker_pool, subsystem_rating=subsystem_rating,
                              defuse_utility=defuse_rating)
    _spend_one_shot(state, decker, "defuse")
    if df["defused"]:
        state["data_bombs"] = [b for b in armed if b is not bomb]
        state.setdefault("defused_bombs", []).append(btarget)
        _append_event(state, {
            "type": "data_bomb", "outcome": "defused", "decker_roll": df["roll"],
            "description": (
                f"Data bomb on {btarget} DEFUSED (Computer Test TN {df['tn']} = {subsystem} "
                f"{subsystem_rating} - Defuse {defuse_rating}). No tally increase -- no suppression needed."
            ),
        })
        return
    if df["detonated"]:
        state["data_bombs"] = [b for b in armed if b is not bomb]  # one-shot
        _detonate_data_bomb(state, decker, eff, ic_rating=brating, sec_value=sec_value,
                            sec_code=sec_code,
                            headline=f"Data bomb on {btarget} (botched defuse -- all 1s)")
        return
    _append_event(state, {
        "type": "data_bomb", "outcome": "primed", "decker_roll": df["roll"],
        "description": (
            f"Defuse FAILED (Computer Test TN {df['tn']} = {subsystem} {subsystem_rating} - "
            f"Defuse {defuse_rating}) -- the data bomb on {btarget} stays primed. Try again, "
            "or it triggers if you successfully access the protected target."
        ),
    })


def _trigger_access_data_bomb(state: dict, decker: dict, eff: dict, *, action_type: str,
                              target_file: str, test_success: bool, sec_value: int,
                              sec_code: str) -> bool:
    """Data Bomb access trigger (vr2_rules.md L473): a SUCCESSFUL access (Download / Edit /
    Upload) of a file or Slave device that still carries an UNDEFUSED bomb sets it off -- the
    decker gets the access AND eats the blast. A FAILED access does NOT trigger it, and a bomb
    already disarmed (via the Defuse Data Bomb action) is inert. Returns True iff a bomb
    detonated; mutates ``state`` (removes the one-shot bomb and applies _detonate_data_bomb)."""
    if action_type not in ("download_data", "edit_file", "upload_data"):
        return False
    if not test_success or not target_file:
        return False
    armed = state.get("data_bombs") or []
    safe = set(state.get("defused_bombs") or [])
    tgt = target_file.strip().lower()
    bomb = next((b for b in armed
                 if b.get("target") not in safe
                 and _target_file_name(b.get("target", "")).lower() == tgt), None)
    if bomb is None:
        return False
    state["data_bombs"] = [b for b in armed if b is not bomb]  # one-shot
    _detonate_data_bomb(state, decker, eff, ic_rating=bomb.get("rating", 6),
                        sec_value=sec_value, sec_code=sec_code,
                        headline=f"DATA BOMB on {bomb.get('target')}")
    return True


def _apply_dump_log(state: dict, decker: dict, *, host_id: int, run_id: int,
                    sec_code: str, sec_value: int) -> None:
    """Dump Log success handler (vr2 Validate / Control System Test): reveal the host's access-log
    summary to the decker. The readout is fully player-visible -- it is the decker's own read of
    the logs (so it is NOT GM-redacted), and it is what a Graceful Logoff later wipes.

    Generation is deterministic from a LOCAL ``random.Random`` seeded by the host id + run id, so
    repeated dumps in the same run are identical. We never call ``random.seed()`` on the global
    RNG in the request path (that would make every later dice roll in the process predictable --
    see AGENTS.md RNG rule). The decker's OWN intrusion is recorded UNLESS they currently hold
    Legitimate status (a validated/linked passcode reads as a legal user in the host logs)."""
    intrusion_logged = not bool(state.get("has_legitimate_status"))
    seed = (int(host_id or 0) * 1_000_003) ^ (int(run_id or 0) * 31 + 17)
    rng = random.Random(seed)
    summary = eng.build_access_log_summary(
        security_code=sec_code,
        security_value=sec_value,
        intrusion_logged=intrusion_logged,
        rng=rng,
    )
    state["access_log_dumped"] = summary
    files = ", ".join(summary["files_accessed"]) or "none"
    progs = ", ".join(summary["programs_run"]) or "none"
    _append_event(state, {
        "type": "log_dumped",
        "legitimate_users": summary["legitimate_users"],
        "files_accessed": summary["files_accessed"],
        "programs_run": summary["programs_run"],
        "intrusions_on_record": summary["intrusions_on_record"],
        "intrusion_logged": summary["intrusion_logged"],
        "log_size_mp": summary["log_size_mp"],
        "description": (
            f"Dump Log -- {summary['legitimate_users']} legal user(s) on record; "
            f"files accessed: {files}; programs run: {progs}. "
            f"24h log ~{summary['log_size_mp']} Mp ({summary['difficulty']} host). "
            + ("YOUR intrusion IS currently in the host logs -- a Graceful Logoff will clear it."
               if intrusion_logged else
               "YOUR access reads as a legitimate user -- no intrusion on record.")
        ),
    })


def _live_icon_bandwidth(decker: dict, state: dict, eff: dict | None = None) -> int:
    """Live Icon Bandwidth (vr2): persona program ratings + the ratings of every utility held
    in active memory, recomputed from the *current* run state. Crippler/MPCP damage lowers the
    persona side (via _get_decker_effective) and program crashes (program_damage) lower the
    utilities, so the footprint shrinks/grows mid-run instead of being frozen at logon."""
    if eff is None:
        eff = _get_decker_effective(decker, state)
    persona = eff["bod"] + eff["evasion"] + eff["masking"] + eff["sensor"]
    pd = state.get("program_damage", {}) or {}
    utils = decker.get("utilities") or {}
    util_sum = sum(max(0, (r or 0) - pd.get(n, 0)) for n, r in utils.items())
    return persona + util_sum


def _live_bandwidth_modifier(decker: dict, state: dict, eff: dict | None = None) -> int:
    """Live Bandwidth Trace Modifier: -1 to Trace Factor per full multiple of the jackpoint's
    base bandwidth the Icon Bandwidth exceeds (a fatter icon is easier to trace). base==0 is a
    console/unlimited jackpoint (no penalty). Legacy runs with no stored base_bandwidth fall
    back to the value frozen on the decker at logon."""
    base = state.get("base_bandwidth")
    if base is None:
        return decker.get("bandwidth_modifier", 0)
    if base <= 0:
        return 0
    return -(_live_icon_bandwidth(decker, state, eff) // base)


def _secret_sensor_test(state: dict, decker: dict, ic: dict) -> int:
    """GM secret Sensor Test when a reactive IC acts (vr2 line 409).

    Rolls the decker's Sensor dice vs the IC rating and raises the IC's
    ``detection_level`` to the number of successes (capped 3, never lowered):
      0 unaware  1 'something triggered IC'  2 know the type  3 know rating + location.
    Emits a graduated, player-facing notice when the level increases. Returns the level.
    """
    if ic.get("analyzed"):
        ic["detection_level"] = 3
        return 3
    prev = _ic_detection_level(ic)
    eff = _get_decker_effective(decker, state)
    roll = eng.roll_dice(eff.get("sensor", 4), ic.get("rating", 6))
    new = min(3, max(prev, roll["successes"]))
    ic["detection_level"] = new
    if new > prev:
        notices = {
            1: "You sense your actions have triggered hidden IC.",
            2: f"You identify the lurking IC as {ic.get('type', '?')} IC.",
            3: f"You pinpoint {ic.get('type', '?')}-{ic.get('rating', '?')} IC and its location.",
        }
        _append_event(state, {
            "type": "ic_detected",
            "ic_id": ic["id"],
            "detection_level": new,
            "description": notices[new],
        })
    return new


# -- Rules / reference endpoints -----------------------------------------------

@router.get("/rules/ic-info")
async def ic_info():
    """Full VR2 IC catalog."""
    return rules.IC_CATALOG


@router.get("/rules/subsystem-info")
async def subsystem_info():
    return rules.SUBSYSTEM_INFO


@router.get("/rules/operations")
async def system_operations():
    return rules.SYSTEM_OPERATIONS


@router.get("/rules/host-difficulty")
async def host_difficulty():
    """Host design ranges + dice formulas keyed by difficulty tier."""
    return rules.HOST_DIFFICULTY


@router.get("/rules/paydata-table")
async def paydata_table():
    """Paydata points / density / base value keyed by host security code."""
    return rules.PAYDATA_TABLE


@router.post("/rules/sheaf-preview")
async def sheaf_preview(body: SheafGenerateInput):
    """Generate a preview sheaf without saving it."""
    sheaf = eng.generate_sheaf(
        security_code=body.security_code,
        security_value=body.security_value,
        step_count=body.step_count,
        seed=body.seed,
    )
    return {"sheaf": sheaf}


# -- Host sheaf endpoints (extends matrix hosts with SR2 sheaf data) ------------

@router.post("/hosts/{host_id}/sheaf", dependencies=[Depends(get_admin_token)])
async def save_sheaf(host_id: int, body: SheaveSaveInput, db: AsyncSession = Depends(get_db)):
    """Save a security sheaf + ACIFS to a matrix host's config_json."""
    host = await _get_host_or_404(db, host_id)
    cfg = dict(host.config_json or {})
    cfg["sheaf"] = [s.model_dump() for s in body.sheaf]
    cfg["security_code"] = body.security_code
    cfg["security_value"] = body.security_value
    cfg["acifs"] = body.acifs
    cfg["owner_type"] = body.owner_type
    host.config_json = cfg
    await db.commit()
    await db.refresh(host)
    return {"ok": True, "host_id": host.id}


@router.post("/rules/generate-sheaf", dependencies=[Depends(get_admin_token)])
async def generate_sheaf_endpoint(body: SheafGenerateInput):
    """Generate and return a sheaf (does not save)."""
    return {"sheaf": eng.generate_sheaf(
        security_code=body.security_code,
        security_value=body.security_value,
        step_count=body.step_count,
        seed=body.seed,
    )}


# -- Run session CRUD -----------------------------------------------------------

@router.get("/", response_model=list[MatrixRunSummary], dependencies=[Depends(get_admin_token)])
async def list_runs(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(MatrixRun).order_by(MatrixRun.created_at.desc()).limit(50))
    return result.scalars().all()


@router.post("/", response_model=MatrixRunRead, status_code=201)
async def start_run(
    body: MatrixRunCreate,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Start a new Matrix run. Any authenticated user can start a run.
    The starting token becomes the run owner; only admin or owner can mutate it after."""
    host = await _get_host_or_404(db, body.host_id)
    if not auth.get("is_admin") and not host.is_visible_to_players:
        raise HTTPException(404, "Matrix host not found")

    run = await _create_run(db, auth, host, body.decker.model_dump())
    return _serialize_run(run, auth)


async def _create_run(db: AsyncSession, auth: dict, host: MatrixHost, decker_dict: dict) -> MatrixRun:
    """Persist a fresh run on ``host`` for the given decker. Shared by start_run and the
    trap-door ENTER transit (which lands the decker on a new linked host)."""
    state = _initial_state(decker_dict, host)
    run = MatrixRun(
        host_id=host.id,
        decker_json=decker_dict,
        state_json=state,
        status="active",
        owner_token_hash=hash_token(auth["user_token"]) if auth.get("user_token") else None,
    )
    db.add(run)
    await db.commit()
    await db.refresh(run)
    return run


@router.get("/{run_id}", response_model=MatrixRunRead)
async def get_run(
    run_id: int,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    return _serialize_run(run, auth)


@router.delete("/{run_id}", status_code=204)
async def abandon_run(
    run_id: int,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    run.status = "abandoned"
    state = copy.deepcopy(run.state_json)  # deepcopy, not dict(): keep nested JSON mutations un-aliased so the UPDATE fires
    state["run_ended"] = True
    state["end_reason"] = "abandoned"
    run.state_json = state
    await db.commit()


# -- Run actions ---------------------------------------------------------------

# NOTE: perform_action is ~600 LOC and combines action resolution, probe IC, and
# the proactive IC turn loop. A split is planned but deferred until gameplay rules
# stabilize. See docs/refactor-notes.md (R1) for the planned structure, risks, and
# why this hasn't been done yet -- read that before reorganizing.
@router.post("/{run_id}/action", response_model=MatrixRunRead)
async def perform_action(
    run_id: int,
    body: RunActionInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """
    Perform a decker system operation.
    Resolves the test, updates security tally, checks sheaf triggers, activates IC.
    """
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, f"Run is not active (status: {run.status})")

    state = copy.deepcopy(run.state_json)  # deepcopy, not dict(): keep nested JSON mutations un-aliased so the UPDATE fires
    decker = run.decker_json
    eff = _get_decker_effective(decker, state)

    if state.get("run_ended"):
        raise HTTPException(400, "Run has already ended")
    if state.get("icon_crashed"):
        raise HTTPException(400, "Your icon is crashed by Black IC -- you can only jack out")

    # Graceful Logoff is its own Access Test (not a generic subsystem op), so resolve it via
    # the shared helper and return -- mirroring POST /{run_id}/logoff. Without this the
    # graceful_logoff action fell through to the generic test below and never actually ended
    # the run.
    if body.action_type == "graceful_logoff":
        _spend_pass_action(state, "graceful_logoff")   # vr2: Graceful Logoff is a Complex Action
        success = _apply_graceful_logoff(
            state, decker,
            hacking_pool_dice=body.hacking_pool_dice,
            deception_utility=body.utility_rating,
        )
        if success:
            run.status = "escaped"
        run.state_json = state
        await db.commit()
        await db.refresh(run)
        return _serialize_run(run, auth)

    # Storage pre-check: a Download cannot even be attempted if the named file would not fit the
    # deck's remaining free storage (vr2 finite memory). Block before spending the action so the
    # player isn't charged a pass for an impossible download. storage_free_mp < 0 = untracked.
    if body.action_type == "download_data" and body.target_file:
        free = state.get("storage_free_mp", -1)
        if free is not None and free >= 0:
            tgt_name = body.target_file.strip().lower()
            pd = next((p for p in (state.get("paydata") or [])
                       if str(p.get("name", "")).strip().lower() == tgt_name), None)
            if pd is not None and not pd.get("downloaded"):
                # Use the SAME effective stored size the download will charge, so a Compressor
                # lets the player grab a file that fits compressed even if its full size would not.
                comp = _effective_compressor(decker)
                stored, _compressible = _compressed_store_size(comp, pd.get("density", 0))
                remaining = max(0, free - state.get("storage_used_mp", 0))
                if stored > remaining:
                    raise HTTPException(
                        400,
                        f"Not enough deck storage: \"{pd.get('name')}\" needs {stored} Mp but only "
                        f"{remaining} Mp free. Purge stored files or free storage memory first."
                    )

    # Action economy: spend this action's cost from the current initiative pass (auto-advances
    # passes; blocks when all passes are spent -> New Turn). vr2: 2 Simple OR 1 Complex + 1 Free.
    _spend_pass_action(state, body.action_type)

    sec_code = state["host_security_code"]
    sec_value = state["host_security_value"]
    subsystem_rating = _subsystem_rating(state, body.subsystem)
    det_factor = _effective_detection_factor(state, decker)
    state["detection_factor"] = det_factor  # keep serialized run in sync for the UI

    # Decker skill dice + utility reduction
    _spend_hp(state, body.hacking_pool_dice)
    base_skill = decker.get("computer_skill", 4)
    pool = base_skill + body.hacking_pool_dice
    tn_modifier = body.extra_tn_modifier
    if body.utility_rating > 0:
        tn_modifier -= body.utility_rating  # utility reduces TN

    # Swap Memory (Simple Action, no test): move programs between storage and active memory.
    # Active programs always keep a storage copy, so a swap only shifts *active* memory usage --
    # deck storage_free_mp is unaffected. See _apply_swap_memory for the three resolution modes.
    if body.action_type == "swap_memory":
        new_decker = copy.deepcopy(decker)
        changed, desc = _apply_swap_memory(
            state, new_decker,
            target_program=body.target_program,
            swap_out_program=body.swap_out_program,
        )
        _append_event(state, {"type": "swap_memory", "description": desc})
        if changed:
            run.decker_json = new_decker
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Medic (Complex Action, self-targeted -- NOT an opposed subsystem System Test): heal boxes
    # of the decker's own persona/icon Condition Monitor. Resolved here and returned so it never
    # falls through to the generic system_test below, which would log a bogus subsystem result.
    if body.action_type == "medic":
        _apply_medic(state, decker)
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Restore (Complex Action, self-targeted defensive utility -- NOT an opposed subsystem System
    # Test): repair the TEMPORARY crippler reductions to the icon's persona attributes (BEMS). It
    # cannot touch permanent Persona-chip damage and does NOT degrade. Resolved here and returned
    # so it never falls through to the generic system_test below.
    if body.action_type == "restore":
        _apply_restore(state, decker, target=body.target_program)
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Disinfect (Complex Action): a System Test against the subsystem hosting a worm (TN reduced by
    # the carried Disinfect utility). Success DESTROYS the targeted Worm lurking-IC with no tally
    # add (a Disinfect is not a cybercombat crash); failure risks the Worm Infection Test against
    # the MPCP. Resolved here and returned so it never falls through to the generic system_test.
    if body.action_type == "disinfect":
        _apply_disinfect(
            state, decker,
            subsystem=body.subsystem,
            subsystem_rating=subsystem_rating,
            decker_pool=pool,
            target_ic_id=body.target_ic_id,
        )
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Defuse Data Bomb (Complex Action): a Computer Test against the controlling subsystem rating
    # (Files for a file bomb, Slave for a device bomb -- pick the subsystem) reduced by the carried
    # Defuse utility. Success disarms the bomb with NO tally add (a defuse is not a crash); an
    # all-1s botch detonates it; any other failure leaves it primed to retry. Resolved here and
    # returned so it never falls through to the generic system_test below.
    if body.action_type == "defuse_data_bomb":
        _apply_defuse_bomb(
            state, decker, eff,
            subsystem=body.subsystem,
            subsystem_rating=subsystem_rating,
            decker_pool=pool,
            sec_value=sec_value,
            sec_code=sec_code,
            target_file=body.target_file,
        )
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Steamroller (Complex Action): the dedicated anti-tar weapon. Inflicts (Rating)D on a named
    # Tar Baby / Tar Pit lurking-IC and is IMMUNE to the tar crash-backlash (it never runs the
    # tar's opposed crash test, so the decker's utilities are never crashed/corrupted). A crash
    # removes the tar and adds its rating to the tally unless Stealth(Skulk)-masked or the tar is
    # suppressed. Targets ONLY tar IC (non-tar target_ic_id is rejected). Resolved here and
    # returned so it never falls through to the generic system_test below.
    if body.action_type == "steamroller":
        _apply_steamroller(
            state, decker,
            sec_code=sec_code,
            decker_pool=pool,
            target_ic_id=body.target_ic_id,
        )
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Slow (Complex Action): reduce a proactive IC's execution speed. A to-hit Computer Test then
    # an opposed Resistance (Slow Rating) Test; on a win the IC loses actions and, with none left,
    # HANGS for the turn -- the proactive-IC loop honours ``ic['actions_lost']`` and new_turn clears
    # it unless the IC is suppressed. Reactive IC and location-cycle trace IC are rejected (400).
    # Resolved here and returned so it never falls through to the generic system_test below.
    if body.action_type == "slow":
        _apply_slow(
            state, decker,
            sec_code=sec_code,
            decker_pool=pool,
            target_ic_id=body.target_ic_id,
        )
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Decompress File (Complex Action, no test -- pure storage bookkeeping like Swap Memory):
    # expand a previously-downloaded COMPRESSED file (stored at half size via the Compressor
    # utility) back to its full size so it can be read/used. Needs the extra free Mp when storage
    # is tracked (rejected 400 if it won't fit -- and the action is not spent). Resolved here and
    # returned so it never falls through to the generic system_test below.
    if body.action_type == "decompress_file":
        _apply_decompress(state, decker, target_file=body.target_file)
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # DINAB ("Decker In A Box"), Free Action (vr2_rules.md L1665): let ONE DINAB-equipped program
    # run itself autonomously at skill = effective DINAB rating, alongside the decker's own pass.
    # Offensive utilities reuse cybercombat / crippler resolution; everything else runs a generic
    # System Test. Failure degrades the rating (-1); a failed all-1s roll crashes it. Resolved here
    # and returned so it never falls through to the generic system_test below.
    if body.action_type == "dinab":
        _apply_dinab(
            state, decker,
            util=body.target_program,
            sec_code=sec_code, sec_value=sec_value,
            subsystem=body.subsystem, subsystem_rating=subsystem_rating,
            det_factor=det_factor,
            target_ic_id=body.target_ic_id, target_file=body.target_file,
        )
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Purge Hog (Complex Action): Computer test to wipe a Hog virus -- success removes the
    # infection AND crashes the infected program (reload it afterward via Swap Memory).
    if body.action_type == "purge_hog":
        infections = state.get("hog_infections") or []
        if not infections:
            _append_event(state, {"type": "purge_hog", "description": "No Hog virus to purge."})
        else:
            inf = next((i for i in infections if i.get("id") == body.target_program), infections[0])
            pd = state.setdefault("program_damage", {})
            name, _eff = _highest_running_utility(decker, pd)
            base = (decker.get("utilities") or {}).get(name, 0) if name else 0
            purge = eng.hog_purge_test(
                computer_skill=decker.get("computer_skill", 4), hog_rating=inf.get("rating", 4),
                infected_program_rating=base, hardening=decker.get("hardening", 0))
            if purge["purged"]:
                state["hog_infections"] = [i for i in infections if i is not inf]
                if name:
                    pd[name] = base  # the purge sacrifices the infected program (crashed)
                desc = (f"Purged Hog-{inf.get('rating')} (TN {purge['tn']}) -- virus removed; the "
                        f"{name.replace('_', ' ').title() if name else 'infected'} program is wiped "
                        "(reload via Swap Memory).")
            else:
                desc = f"Purge FAILED (TN {purge['tn']}) -- Hog-{inf.get('rating')} persists."
            _append_event(state, {"type": "purge_hog", "decker_roll": purge["roll"], "description": desc})
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Decrypt File is resolved against a Scramble IC (its rating IS the decrypt TN),
    # not the generic subsystem test. A failed decrypt vs a POISON Scramble destroys the
    # protected data -- key data is a permanent, mission-critical loss shown to the player.
    if body.action_type == "decrypt_file" and (state.get("scrambles") or []):
        scrambles = state["scrambles"]
        scr = None
        if body.target_file:
            scr = next((s for s in scrambles if s.get("target_key") == body.target_file), None)
        if scr is None:
            scr = scrambles[0]
        dt = eng.scramble_decrypt_test(
            decker_pool=pool,
            scramble_rating=scr.get("rating", 6),
            decrypt_utility=body.utility_rating,
        )
        if dt["decrypted"]:
            state["scrambles"] = [s for s in scrambles if s is not scr]
            _append_event(state, {
                "type": "decrypt", "success": True, "decker_roll": dt["roll"],
                "description": "Scramble decrypted -- protected data accessible. No tally increase.",
            })
        else:
            paydata = state.get("paydata") or []
            tkey = str(scr.get("target_key", ""))
            protected = next((p for p in paydata if p.get("name") and p["name"] in tkey), None)
            is_key = bool(protected and protected.get("is_key"))
            cons = eng.scramble_failure_consequence(
                variant=scr.get("variant", "standard"), is_key=is_key)
            if cons.get("data_destroyed") and protected is not None:
                protected["destroyed"] = True
            _append_event(state, {
                "type": "decrypt", "success": False, "decker_roll": dt["roll"],
                "key_data_lost": cons.get("key_data_lost", False),
                "data_destroyed": cons.get("data_destroyed", False),
                "file_name": (protected or {}).get("name"),  # lets the UI grey the destroyed file
                "description": cons["message"],
            })
            # Exploding Scramble: a failed decrypt sets off its linked data bomb (vr2).
            if cons.get("detonate_data_bomb"):
                _detonate_data_bomb(
                    state, decker, eff, ic_rating=scr.get("rating", 6),
                    sec_value=sec_value, sec_code=sec_code,
                    headline="Exploding Scramble's data bomb")
        run.state_json = state
        await db.commit()
        await db.refresh(run)
        return _serialize_run(run, auth)

    # Console access additionally halves the host Security Value for Access Tests (vr2).
    test_sec_value = sec_value
    if body.subsystem == "access" and state.get("console_access"):
        test_sec_value = -(-sec_value // 2)
    # Stolen linked passcode + a Deception utility: -2 TN to Logon to Host (vr2).
    if (body.action_type == "logon_to_host" and body.utility_rating > 0
            and state.get("linked_passcode")):
        tn_modifier -= 2

    test = eng.system_test(
        decker_pool=pool,
        subsystem_rating=subsystem_rating,
        security_value=test_sec_value,
        det_factor=det_factor,
        extra_tn_modifier=tn_modifier,
    )

    # Update tally
    old_tally = state["security_tally"]
    state["security_tally"] = old_tally + test["tally_increase"]

    log_entry: dict[str, Any] = {
        "type": "action",
        "action": body.action_type,
        "subsystem": body.subsystem,
        "description": (
            f"{body.action_type.replace('_', ' ').title()} -- "
            f"{'SUCCESS' if test['success'] else 'FAILED'} "
            f"({test['decker_roll']['successes']} vs {test['host_roll']['successes']} successes). "
            f"Tally +{test['tally_increase']} -> {state['security_tally']}."
        ),
        "success": test["success"],
        "decker_roll": test["decker_roll"],
        "host_roll": test["host_roll"],
        "tally_increase": test["tally_increase"],
        "tally_total": state["security_tally"],
        "action_cost": _ACTION_COST.get(body.action_type, "Complex"),  # Free / Simple / Complex
        "note": body.note,
    }
    _append_event(state, log_entry)
    state["actions_this_turn"] = state.get("actions_this_turn", 0) + 1

    # Analyze IC: a successful Analyze reveals an IC's type + rating to the decker (vr2 #9).
    # Until then the player only sees an "Unknown IC" marker (redacted in _serialize_run).
    if body.action_type == "analyze_ic" and test["success"]:
        active = [ic for ic in state.get("active_ic", []) if ic.get("status") == "active"]
        target = None
        if body.target_ic_id:
            target = next((ic for ic in active if ic["id"] == body.target_ic_id), None)
        if target is None:
            target = next((ic for ic in active if not ic.get("analyzed")), None)
        if target is not None:
            target["analyzed"] = True
            _append_event(state, {
                "type": "ic_analyzed",
                "ic_id": target["id"],
                "ic_type": target["type"],
                "ic_rating": target["rating"],
                "description": f"IC analyzed: {target['type']} Rating {target['rating']} revealed.",
            })

    # Analyze Subsystem: a successful analysis of the concealing subsystem reveals any trap
    # door hidden on it. Per vr2 the decker learns a port to ANOTHER system exists, but the
    # Analyze Subsystem: a successful analysis of the concealing subsystem reveals any trap
    # door hidden on it. Per vr2 the decker learns a port to ANOTHER system exists, but the
    # destination stays hidden until they enter it (revealed on arrival). Separately, a
    # successful Analyze Subsystem on ACCESS reveals THIS host's LTG-access status -- the only
    # way to learn whether a host reached via a trap door is also reachable from the grid.
    if body.action_type == "analyze_subsystem" and test["success"]:
        sub = body.subsystem
        newly = [d for d in (state.get("trap_doors") or [])
                 if not d.get("discovered") and (d.get("subsystem", "slave") == sub)]
        for d in newly:
            d["discovered"] = True
            src = d.get("source_piece") or ""
            _append_event(state, {
                "type": "trap_door_found",
                "trap_door_id": d.get("id"),
                "subsystem": sub,
                "source_piece": src,
                "description": (
                    f"Concealed port detected on the {sub.capitalize()} subsystem"
                    + (f" ({src})" if src else "")
                    + " -- it links to another system. Destination unknown until you enter or file it."
                ),
            })
        if sub == "access" and not state.get("host_ltg_revealed"):
            state["host_ltg_revealed"] = True
            has_ltg = bool(state.get("host_has_ltg"))
            _append_event(state, {
                "type": "host_ltg_revealed",
                "has_ltg": has_ltg,
                "description": (
                    "Access subsystem analyzed -- this host "
                    + ("HAS dedicated LTG access (reachable from the regular grid)."
                       if has_ltg else
                       "has NO LTG access (reachable only via a direct line or trap door).")
                ),
            })

    # Analyze Host: each net success reveals one host subsystem (ACIFS) rating. The raw ratings
    # are GM-only (host_acifs); revealed values mirror into the player-visible
    # host_ratings_revealed map in ACIFS order (vr2: "each success reveals one piece of info").
    if body.action_type == "analyze_host" and test["success"]:
        acifs = state.get("host_acifs") or [10, 10, 10, 10, 10]
        names = ["access", "control", "index", "files", "slave"]
        revealed = state.setdefault("host_ratings_revealed", {})
        budget = max(1, test["decker_net_successes"])
        newly: list[tuple[str, int]] = []
        for i, nm in enumerate(names):
            if budget <= 0:
                break
            if nm not in revealed:
                revealed[nm] = int(acifs[i]) if i < len(acifs) else 10
                newly.append((nm, revealed[nm]))
                budget -= 1
        if newly:
            _append_event(state, {
                "type": "host_analyzed",
                "revealed": [{"subsystem": nm, "rating": rt} for nm, rt in newly],
                "description": "Analyze Host -- " + ", ".join(
                    f"{nm.capitalize()} {rt}" for nm, rt in newly
                ) + " revealed.",
            })
        else:
            _append_event(state, {
                "type": "host_analyzed", "revealed": [],
                "description": "Analyze Host -- all subsystem ratings already known.",
            })

    # Analyze Security: the decker learns its CURRENT security tally + alert status (otherwise
    # redacted for players). Snapshot them into the player-visible security_known (vr2: the GM
    # reveals the tally only when the decker runs this test).
    if body.action_type == "analyze_security" and test["success"]:
        snapshot = {
            "tally": state["security_tally"],
            "alert": state.get("alert_status", "none"),
            "turn": state.get("current_turn", 1),
        }
        state["security_known"] = snapshot
        _append_event(state, {
            "type": "security_analyzed",
            "known_tally": snapshot["tally"],
            "known_alert": snapshot["alert"],
            "description": (
                f"Analyze Security -- security tally {snapshot['tally']}, "
                f"alert status {snapshot['alert'].upper()} (as of turn {snapshot['turn']})."
            ),
        })

    # Dump Log (vr2 Validate / Control): a successful Control System Test reads the host access
    # logs. Like Analyze Host/Security this is a generic test followed by a success handler (NOT an
    # early return). Reveal a player-visible summary -- legal users, files accessed, programs run,
    # intrusions on record, and crucially whether the decker's OWN intrusion is logged (cleared by
    # a Graceful Logoff) -- into access_log_dumped. Generated deterministically from a local RNG.
    if body.action_type == "dump_log" and test["success"]:
        _apply_dump_log(
            state, decker,
            host_id=getattr(run, "host_id", 0),
            run_id=getattr(run, "id", 0),
            sec_code=sec_code, sec_value=sec_value,
        )

    # Crash Host: a successful Control/Crash test starts a host-shutdown countdown (vr2). turns =
    # round_up(10 / successes); during the countdown all IC ratings drop by 2, and at the END of
    # each turn the host rolls Security Value vs the decker's MPCP to abort (see
    # _process_crash_countdown). If the countdown completes the host crashes and the decker rides
    # it out, logging off cleanly -- a successful clean exit (no dump shock).
    if body.action_type == "crash_host" and test["success"]:
        successes = max(1, test["decker_net_successes"])
        turns = -(-10 // successes)   # ceil(10 / net successes) -- a more decisive win crashes faster
        decker_mpcp = int((run.decker_json or {}).get("mpcp", 1) or 1)
        state["crash_host_countdown"] = {
            "turns_remaining": turns,
            "total_turns": turns,
            "decker_mpcp": decker_mpcp,
            "started_turn": state.get("current_turn", 1),
        }
        _apply_crash_ic_penalty(state)
        _append_event(state, {
            "type": "crash_host_started",
            "turns": turns,
            "description": (
                f"Crash Host initiated -- host shutdown in {turns} turn"
                f"{'s' if turns != 1 else ''} ({successes} successes). All IC ratings -2 during "
                "the countdown; the host rolls Security Value vs your MPCP each turn to abort."
            ),
        })

    # Validate Passcode: grant Legitimate status (IC uses Legitimate TN column)
    if body.action_type == "validate_passcode" and test["success"]:
        state["has_legitimate_status"] = True
        _append_event(state, {
            "type": "validate_passcode",
            "description": "Validate Passcode successful -- Legitimate status granted. IC uses Legitimate TN column until logoff or active alert.",
        })

    # Decoy: deploy countermeasure persona; IC must roll 1D6 <= successes to hit it instead
    if body.action_type == "decoy" and test["success"]:
        d_successes = test["decker_roll"]["successes"]
        state["decoy_successes"] = d_successes
        state["decoy_hp"] = 0
        _append_event(state, {
            "type": "decoy_deployed",
            "description": (
                f"Decoy deployed with {d_successes} success(es). "
                "Each proactive IC attack: roll 1D6 -- if result <= successes, IC hits decoy (10-box CM)."
            ),
            "successes": d_successes,
        })

    # Relocate: reset any trace IC in its location cycle back to hunt cycle
    if body.action_type == "relocate" and test["success"]:
        reset_count = 0
        for ic in state.get("active_ic", []):
            if ic["status"] == "active" and ic.get("trace_phase") == "locate":
                ic["trace_phase"] = "hunt"
                ic.pop("trace_locate_remaining", None)
                reset_count += 1
                _append_event(state, {
                    "type": "relocate",
                    "ic_id": ic["id"],
                    "description": (
                        f"Relocate succeeded -- {ic['type']}-{ic['rating']} "
                        "reset to Hunt Cycle."
                    ),
                })
        if not reset_count:
            _append_event(state, {
                "type": "relocate",
                "description": "Relocate: no trace IC currently in location cycle.",
            })

    # Redirect Datatrail: each success increments redirects (-1 to Trace Factor)
    if body.action_type == "redirect_datatrail" and test["success"]:
        state["redirects_placed"] = state.get("redirects_placed", 0) + 1
        _append_event(state, {
            "type": "redirect_placed",
            "description": (
                f"Redirect placed. Trace Factor -1 going forward. "
                f"Total redirects this run: {state['redirects_placed']}."
            ),
            "redirects_total": state["redirects_placed"],
        })

    # Locate Paydata: a successful search reveals what files are present (name + size) so the
    # player can choose what to download against finite deck storage. Found files are surfaced
    # to the player via _serialize_run (located_paydata); the full paydata list stays GM-only.
    if body.action_type == "locate_paydata" and test["success"]:
        newly = [p for p in (state.get("paydata") or [])
                 if not p.get("located") and not p.get("destroyed")]
        for p in newly:
            p["located"] = True
        if newly:
            _append_event(state, {
                "type": "paydata_located",
                "description": "Paydata located: " + ", ".join(
                    f"{p.get('name', '?')} ({max(0, int(p.get('density', 0) or 0))} Mp)" for p in newly
                ) + ".",
                "files": [{"name": p.get("name"),
                           "size_mp": max(0, int(p.get("density", 0) or 0)),
                           "is_key": bool(p.get("is_key"))} for p in newly],
            })
        else:
            _append_event(state, {
                "type": "paydata_located",
                "description": "Search complete -- no further paydata found.",
            })

    # Locate Decker: a Sensor-aided Index sweep for a hidden hostile decker. The app plays the
    # opponent, so spawned enemy deckers start hidden and must locate the PC over several turns;
    # the PC can scan for them at any time (a mutual-detection race). On a successful Index test,
    # run an opposed Sensor Test vs each hidden enemy (Scanner reduces the TN); any net success
    # reveals it so the PC can Strike Back or evade first.
    if body.action_type == "locate_decker":
        hidden = [e for e in state.get("enemy_deckers", [])
                  if e.get("status") == "active" and not e.get("revealed")]
        sensor = int(decker.get("sensor", 1) or 1)
        scanner = max(0, int(body.utility_rating or 0))   # Scanner utility used for the sweep
        if not hidden:
            _append_event(state, {
                "type": "enemy_decker", "outcome": "scan_clear",
                "description": "Index sweep for hostile icons -- no hidden decker detected on this host.",
            })
        elif not test["success"]:
            _append_event(state, {
                "type": "enemy_decker", "outcome": "scan_fail",
                "description": "Index sweep failed -- you can't pick a hostile icon out of the noise this pass.",
            })
        else:
            found = []
            for e in hidden:
                res = eng.pc_locate_decker_test(
                    sensor_rating=sensor,
                    scanner_rating=scanner,
                    enemy_detection_factor=int(e.get("detection_factor", e.get("masking", 1)) or 1),
                    enemy_evasion=int(e.get("evasion", 1) or 1),
                )
                if res["located"]:
                    e["revealed"] = True
                    found.append((e, res))
            if found:
                for e, res in found:
                    _append_event(state, {
                        "type": "enemy_decker", "outcome": "scan_hit", "enemy_id": e["id"],
                        "description": (
                            f"Hostile decker located: {e['name']} (tier {e.get('tier', '?')}) -- "
                            f"Sensor {sensor} vs TN {res['target_tn']}, {res['net_successes']} net "
                            "success(es). You can Strike Back."
                        ),
                    })
            else:
                _append_event(state, {
                    "type": "enemy_decker", "outcome": "scan_fail",
                    "description": (
                        "Index sweep ran clean but your Sensor pass couldn't pin the hostile icon "
                        "-- try again next pass."
                    ),
                })

    # Download Data: on success, pull the named file -- record it in the player-visible ledger
    # (downloaded_files) and consume finite deck storage. The pre-check above guarantees it fits.
    if body.action_type == "download_data" and test["success"] and body.target_file:
        tgt_name = body.target_file.strip().lower()
        pd = next((p for p in (state.get("paydata") or [])
                   if str(p.get("name", "")).strip().lower() == tgt_name and not p.get("destroyed")),
                  None)
        if pd is not None and not pd.get("downloaded"):
            pd["downloaded"] = True
            pd["located"] = True
            density = max(0, int(pd.get("density", 0) or 0))
            # Compressor (vr2_rules.md L1512-1515): a loaded Compressor halves the STORED footprint
            # of a file within the Rating*100 Mp cap; it must be decompressed before it can be used.
            comp = _effective_compressor(decker)
            stored, compressible = _compressed_store_size(comp, density)
            pd["compressed"] = compressible
            if compressible:
                pd["full_size_mp"] = density
            state["storage_used_mp"] = state.get("storage_used_mp", 0) + stored
            state.setdefault("downloaded_files", []).append({
                "name": pd.get("name"),
                "size_mp": stored,
                "is_key": bool(pd.get("is_key")),
                "turn": state.get("current_turn", 1),
                "compressed": compressible,
                "full_size_mp": density,
            })
            free = state.get("storage_free_mp", -1)
            tracked = free is not None and free >= 0
            remaining = max(0, free - state["storage_used_mp"]) if tracked else None
            comp_note = (f" (compressed {density}->{stored} Mp; must decompress before use)"
                         if compressible else "")
            _append_event(state, {
                "type": "data_downloaded",
                "file_name": pd.get("name"),
                "size_mp": stored,
                "is_key": bool(pd.get("is_key")),
                "compressed": compressible,
                "full_size_mp": density,
                "storage_used_mp": state["storage_used_mp"],
                "storage_remaining_mp": remaining,
                "description": (
                    f"Downloaded \"{pd.get('name')}\" ({stored} Mp"
                    f"{', KEY DATA' if pd.get('is_key') else ''}){comp_note}. "
                    f"Storage used {state['storage_used_mp']} Mp"
                    + (f"; {remaining} Mp free." if tracked else ".")
                ),
            })
        elif pd is not None:
            _append_event(state, {
                "type": "data_downloaded",
                "file_name": pd.get("name"),
                "description": f"\"{pd.get('name')}\" already downloaded -- no additional storage used.",
            })

    # Data Bomb trigger (vr2_rules.md L473): a SUCCESSFUL access (Download/Edit/Upload) of a file
    # or Slave device that still carries an UNDEFUSED bomb sets it off -- the decker gets the
    # access AND eats the blast. A FAILED access does NOT trigger it, and a bomb already disarmed
    # (via the Defuse Data Bomb action) is inert. Detonation adds the bomb's rating to the tally.
    _trigger_access_data_bomb(
        state, decker, eff, action_type=body.action_type, target_file=body.target_file or "",
        test_success=test["success"], sec_value=sec_value, sec_code=sec_code)

    # Check sheaf triggers
    _check_and_activate_sheaf(state, sec_code)

    # Run probe tests for any active Probe IC
    for ic in state.get("active_ic", []):
        if ic["status"] != "active" or ic.get("suppressed"):
            continue
        if ic["type"] == "Probe":
            probe = eng.probe_test(ic["rating"], det_factor)
            # Probe IC is invisible (reactive): make a secret Sensor Test, then report
            # the tally change at a detail level matching what the decker has detected.
            lvl = _secret_sensor_test(state, decker, ic)
            if probe["tally_increase"] > 0:
                state["security_tally"] += probe["tally_increase"]
                tally = state["security_tally"]
                inc = probe["tally_increase"]
                if lvl >= 3:
                    desc = (f"Probe-{ic['rating']} test: {probe['roll']['successes']} successes "
                            f"-> tally +{inc} -> {tally}")
                elif lvl == 2:
                    desc = f"Probe IC test: tally +{inc} -> {tally}"
                elif lvl == 1:
                    desc = f"Hidden IC probes your actions: tally +{inc} -> {tally}"
                else:
                    desc = f"Security tally rose by {inc} -> {tally} (source unidentified)"
                ev = {"type": "probe_ic", "description": desc, "tally_increase": inc}
                if lvl >= 1:
                    ev["ic_id"] = ic["id"]  # only reference the IC once its presence is known
                _append_event(state, ev)
            _check_and_activate_sheaf(state, sec_code)

    # Active IC attacks (proactive IC + trace IC that has already activated, in initiative order)
    for ic in sorted(state.get("active_ic", []), key=lambda x: x.get("initiative", 0), reverse=True):
        if ic["status"] != "active" or ic.get("suppressed"):
            continue
        ic_info = rules.IC_CATALOG.get(_canonical_ic_type(ic["type"]), {})
        ic_category = ic_info.get("category", "white")
        ic_subtype = ic_info.get("subtype", "")

        # Trace IC is classified "reactive" in the catalog but acts every turn on
        # its initiative (hunt -> locate -> trigger), so let it through here.
        if ic_info.get("ic_type") != "proactive" and ic_subtype != "trace":
            continue
        if ic["type"] == "Probe":
            continue  # already handled above

        # NPC initiative passes (vr2): a proactive IC acts on each pass its OWN initiative
        # reaches (init in increments of 10), at most ONCE per pass -- not once per player
        # action. (Probe IC, above, test per System Test instead.)
        cur_pass = state.get("current_pass", 1)
        ic_passes = _init_passes(ic.get("initiative", 0))
        # Slow utility (vr2_rules.md L1576): a slowed IC loses actions this Combat Turn, so its
        # effective passes shrink by ic['actions_lost']; with none left it HANGS (does nothing this
        # turn). new_turn clears actions_lost so the IC resumes next turn -- unless still suppressed.
        effective_passes = max(0, ic_passes - ic.get("actions_lost", 0))
        if cur_pass > effective_passes or ic.get("acted_pass") == cur_pass:
            continue
        ic["acted_pass"] = cur_pass

        # -- Trace IC: hunt/location cycle -- does NOT do cybercombat ---------
        if ic_subtype == "trace":
            phase = ic.get("trace_phase", "hunt")
            if phase == "triggered":
                continue  # already fired -- dormant
            if phase == "hunt":
                trace_tn = _compute_trace_tn(state, decker, ic["rating"], eff)
                hunt = eng.trace_hunt_cycle_attack(sec_value, trace_tn)
                if hunt["hit"]:
                    hunt_successes = max(1, hunt["roll"]["successes"])
                    locate_turns = max(1, 10 // hunt_successes)
                    ic["trace_phase"] = "locate"
                    ic["trace_locate_remaining"] = locate_turns
                    _append_event(state, {
                        "type": "ic_attack",
                        "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                        "description": (
                            f"{ic['type']}-{ic['rating']} HUNT CYCLE HIT "
                            f"({hunt_successes} success(es)) -- "
                            f"Location Cycle: {locate_turns} turn(s) to trace."
                        ),
                        "trace_phase": "hunt_hit",
                        "hunt_roll": hunt["roll"],
                    })
                else:
                    _append_event(state, {
                        "type": "ic_attack",
                        "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                        "description": (
                            f"{ic['type']}-{ic['rating']} hunt cycle: searching... "
                            f"({hunt['roll']['successes']} hits vs TN {trace_tn})"
                        ),
                        "trace_phase": "hunting",
                        "hunt_roll": hunt["roll"],
                    })
            elif phase == "locate":
                remaining = max(0, ic.get("trace_locate_remaining", 1) - 1)
                ic["trace_locate_remaining"] = remaining
                if remaining <= 0:
                    ic["trace_phase"] = "triggered"
                    triggered_action = ic_info.get("triggered_action", "report")
                    if triggered_action == "report":
                        ic["status"] = "triggered"
                        if state.get("physical_trace_immune"):
                            _append_event(state, {
                                "type": "ic_attack",
                                "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                                "description": (
                                    f"{ic['type']}: Satellite jackpoint located, but the decker's "
                                    f"PHYSICAL LOCATION is protected (satellite uplink) -- no physical "
                                    f"security can be dispatched."
                                ),
                                "trace_action": "report",
                                "physical_trace_immune": True,
                            })
                        else:
                            _append_event(state, {
                                "type": "ic_attack",
                                "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                                "description": (
                                    f"{ic['type']}: Jackpoint TRACED -- physical location "
                                    f"reported to system operator."
                                ),
                                "trace_action": "report",
                            })
                    elif triggered_action == "dump":
                        ds = _apply_dump_shock(state, decker, sec_code, sec_value)
                        state["run_ended"] = True
                        state["end_reason"] = "trace_dump"
                        ic["status"] = "triggered"
                        _append_event(state, {
                            "type": "ic_attack",
                            "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                            "description": (
                                f"{ic['type']}: Jackpoint traced -- FORCED DISCONNECT! "
                                f"Dump shock: {ds.get('final_level','None')} "
                                f"({ds.get('boxes',0)} boxes physical)."
                            ),
                            "trace_action": "dump",
                            "dump_shock": ds,
                        })
                        break
                    elif triggered_action == "burn":
                        mpcp_burned = decker.get("mpcp", 1)
                        state["condition_monitor"]["mpcp_damage"] = (
                            state["condition_monitor"].get("mpcp_damage", 0) + mpcp_burned
                        )
                        ic["status"] = "triggered"
                        _append_event(state, {
                            "type": "ic_attack",
                            "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                            "description": (
                                f"{ic['type']}: Jackpoint burned -- MPCP destroyed at node of entry. "
                                f"MPCP -{mpcp_burned} (permanent)."
                            ),
                            "trace_action": "burn",
                            "mpcp_burned": mpcp_burned,
                        })
                else:
                    _append_event(state, {
                        "type": "ic_attack",
                        "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                        "description": (
                            f"{ic['type']}-{ic['rating']} location cycle: "
                            f"{remaining} turn(s) to trace completion."
                        ),
                        "trace_phase": "locating",
                    })
            continue

        # Legitimate status: IC uses different TN column
        ic_target_status = "legitimate" if state.get("has_legitimate_status") else "intruding"

        # -- Decoy intercept check (not effective vs trace IC) -----------------
        decoy_succ = state.get("decoy_successes", 0)
        if decoy_succ > 0 and state.get("decoy_hp", 0) < 10:
            d6 = random.randint(1, 6)
            if d6 <= decoy_succ:
                # IC attacks the decoy instead
                decoy_tn = rules.COMBAT_TN[sec_code][ic_target_status]
                decoy_pool = ic["rating"] if ic["type"] == "Construct" else sec_value
                decoy_atk = eng.roll_dice(decoy_pool, decoy_tn)
                decoy_staged = eng.stage_damage(rules.IC_DAMAGE_LEVEL[sec_code], decoy_atk["successes"], 1)
                decoy_boxes = rules.DAMAGE_BOXES[decoy_staged]
                state["decoy_hp"] = state.get("decoy_hp", 0) + decoy_boxes
                decoy_destroyed = state["decoy_hp"] >= 10
                if decoy_destroyed:
                    state["decoy_successes"] = 0
                    state["decoy_hp"] = 0
                _append_event(state, {
                    "type": "decoy_intercepted",
                    "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                    "description": (
                        f"D6={d6} <= {decoy_succ} -- {ic['type']}-{ic['rating']} hits DECOY! "
                        f"{decoy_staged} ({decoy_boxes} boxes). "
                        f"Decoy: {min(state.get('decoy_hp', 0), 10)}/10"
                        + (" -- DECOY DESTROYED." if decoy_destroyed else "")
                    ),
                    "d6": d6,
                    "attack_roll": decoy_atk,
                    "decoy_boxes": decoy_boxes,
                    "decoy_destroyed": decoy_destroyed,
                })
                continue  # IC consumed its action on the decoy

        # -- Crippler / Ripper: opposed test, reduces BEMS attributes ---------
        if ic_subtype in ("crippler", "ripper"):
            attr_key = _CRIPPLER_TARGET.get(_canonical_ic_type(ic["type"]), "bod")
            target_attr = eff.get(attr_key, 4)
            # Shield parry: net successes ADD to the decker's opposed defence (vr2).
            shield_succ = _shield_parry(state, decker, attacker_skill=sec_value, context=ic["type"])
            result = eng.crippler_attack(
                security_value=sec_value,
                security_code=sec_code,
                target_status=ic_target_status,
                target_attribute_rating=target_attr,
                ic_rating=ic["rating"],
                is_ripper=(ic_subtype == "ripper"),
                mpcp_rating=decker.get("mpcp", 1),
                hardening=decker.get("hardening", 0),
                shield_successes=shield_succ,
            )
            reduction = result["attribute_reduction"]
            pd = state["condition_monitor"]["persona_damage"]
            if reduction > 0:
                pd[attr_key] = min(pd.get(attr_key, 0) + reduction, target_attr - 1)
                # Record this IC's rating as the attribute's causing rating (the Restore Test TN).
                _record_crippler_rating(state, attr_key, ic["rating"])
            desc = (
                f"{ic['type']}-{ic['rating']} vs {attr_key.upper()}: "
                f"{result['attack_roll']['successes']} atk / "
                f"{result['defense_roll']['successes']} def -> "
                f"{attr_key.upper()} -{reduction}."
            )
            if ic_subtype == "ripper" and result.get("chip_damage", 0) > 0:
                chip = result["chip_damage"]
                # Ripper chip damage: PERMANENT -- stored in persona_damage (same slot, persists
                # run) AND recorded in persona_chip_damage so Restore leaves that portion untouched.
                before = pd.get(attr_key, 0)
                pd[attr_key] = min(before + chip, target_attr - 1)
                applied_chip = pd[attr_key] - before
                if applied_chip > 0:
                    pcd = state["condition_monitor"].setdefault(
                        "persona_chip_damage", {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0})
                    pcd[attr_key] = pcd.get(attr_key, 0) + applied_chip
                desc += f" Ripper chip: {attr_key.upper()} -{chip} more (permanent)."
            _append_event(state, {
                "type": "ic_attack",
                "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                "description": desc,
                "attack_roll": result["attack_roll"],
                "defense_roll": result["defense_roll"],
                "attribute_target": attr_key,
                "attribute_reduction": reduction,
            })
            continue

        # -- Standard cybercombat: Killer, Blaster, Sparky, Construct, Black IC
        is_black        = ic["type"] == "Black IC"
        is_non_lethal   = is_black and decker.get("deck_mode") == "cool"
        cluster_penalty = _cluster_size(state, ic.get("cluster_id"))
        ic_attack_pool  = ic["rating"] if ic["type"] == "Construct" else sec_value
        # Expert trade-off (vr2): Offense +N adds attack dice (and -N to its resistance, applied
        # in attack_ic); Defense +N removes attack dice (and +N to resistance).
        ic_attack_pool += _ic_expert(ic, "offense") - _ic_expert(ic, "defense")
        # Cascading IC: misses raise its attack Security Value; neutralized hits raise its rating.
        ic_attack_pool += ic.get("cascade_sv_bonus", 0)
        hardening       = decker.get("hardening", 0)

        if is_black:
            # Black IC: attack roll only (resistance is split into two separate tests below)
            attack_tn  = max(2, rules.COMBAT_TN[sec_code][ic_target_status] + cluster_penalty)
            attack_roll_black = eng.roll_dice(ic_attack_pool, attack_tn)
            base_dmg   = rules.IC_DAMAGE_LEVEL[sec_code]
            # Shield parry: net successes cancel the icon-damage staging. Black IC derives BOTH
            # the persona hit and (when lethal) the physical biofeedback from this one strike, so
            # a successful parry blunts every consequence of the parried attack.
            shield_succ = _shield_parry(state, decker, attacker_skill=sec_value, context="Black IC")
            black_succ = max(0, attack_roll_black["successes"] - shield_succ)
            staged_dmg = eng.stage_damage(base_dmg, black_succ, 1)
            power      = max(1, ic["rating"] - hardening)

            if is_non_lethal:
                # Cool deck: Non-Lethal Black IC -- Willpower test, Stun damage only
                will_roll = eng.roll_dice(decker.get("willpower", 4), power)
                stun_dmg  = eng.stage_damage(staged_dmg, will_roll["successes"], -1)
                stun_boxes = rules.DAMAGE_BOXES[stun_dmg]
                state["condition_monitor"]["physical_boxes"] += stun_boxes
                _append_event(state, {
                    "type": "ic_attack",
                    "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                    "description": (
                        f"Black IC (non-lethal) {ic['rating']}: "
                        f"{attack_roll_black['successes']} atk successes. "
                        f"Willpower resist ({will_roll['successes']} hits): "
                        f"Stun {stun_dmg} ({stun_boxes} boxes). "
                        f"Physical CM: {state['condition_monitor']['physical_boxes']}/10"
                    ),
                    "attack_roll": attack_roll_black,
                    "will_roll": will_roll,
                    "stun_damage": stun_dmg,
                    "stun_boxes": stun_boxes,
                })
            else:
                # Hot deck: Lethal Black IC -- TWO resistance tests
                # 1) Body test -> Physical damage
                body_roll  = eng.roll_dice(decker.get("body", 4), power)
                phys_dmg   = eng.stage_damage(staged_dmg, body_roll["successes"], -1)
                phys_boxes = rules.DAMAGE_BOXES[phys_dmg]
                state["condition_monitor"]["physical_boxes"] += phys_boxes
                # 2) Bod test -> Persona damage (Armor protects)
                armor      = (decker.get("utilities") or {}).get("armor", 0)
                bod_power  = max(1, ic["rating"] - hardening - armor)
                bod_roll   = eng.roll_dice(eff["bod"], bod_power)
                persona_dmg  = eng.stage_damage(staged_dmg, bod_roll["successes"], -1)
                persona_boxes = rules.DAMAGE_BOXES[persona_dmg]
                state["condition_monitor"]["persona_boxes"] += persona_boxes
                _append_event(state, {
                    "type": "ic_attack",
                    "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                    "description": (
                        f"Black IC (lethal) {ic['rating']}: "
                        f"{attack_roll_black['successes']} atk successes. "
                        f"Body resist: {phys_dmg} ({phys_boxes} phys). "
                        f"Bod resist: {persona_dmg} ({persona_boxes} persona). "
                        f"Physical: {state['condition_monitor']['physical_boxes']}/10 "
                        f"Persona: {state['condition_monitor']['persona_boxes']}/10"
                    ),
                    "attack_roll": attack_roll_black,
                    "body_roll": body_roll,
                    "bod_roll": bod_roll,
                    "physical_damage": phys_dmg,
                    "persona_damage": persona_dmg,
                })

            # Black IC: check thresholds (persona OR physical). On either, IC
            # fires one final MPCP attack at 2x rating (Blaster mechanics).
            if state["condition_monitor"]["physical_boxes"] >= 10:
                _append_event(state, {
                    "type": "persona_crash",
                    "description": "BLACK IC LETHAL -- physical damage threshold reached! Decker in critical condition.",
                })
                mpcp_hit, bl_roll = _roll_mpcp_damage(state, decker, ic["rating"], pool_multiplier=2)
                _append_event(state, {
                    "type": "ic_attack",
                    "ic_id": ic["id"], "ic_type": "Black IC",
                    "description": f"Black IC MPCP attack at 2x rating: MPCP -{mpcp_hit} (permanent).",
                    "mpcp_roll": bl_roll, "mpcp_damage": mpcp_hit,
                })
                state["run_ended"] = True
                state["end_reason"] = "black_ic_lethal"
                break

            if state["condition_monitor"]["persona_boxes"] >= 10 and not state.get("icon_crashed"):
                # VR2 Black IC: icon killed BEFORE the decker dies -> the Matrix connection
                # HOLDS, the IC's effective rating rises by 2, and the decker can only attempt
                # to jack out. The MPCP-as-blaster (2x) attack + dump shock happen ONLY when the
                # physical CM fills (the decker is killed) -- handled in the block above.
                state["icon_crashed"] = True
                ic["rating"] += 2
                _append_event(state, {
                    "type": "persona_crash",
                    "ic_id": ic["id"], "ic_type": "Black IC",
                    "description": (
                        "ICON CRASHED by Black IC -- connection holds. Black IC effective "
                        f"rating +2 (now {ic['rating']}). Decker can only attempt to jack out."
                    ),
                })
            continue  # Black IC handled -- skip the rest of the standard combat block

        # -- Killer / Blaster / Sparky / Construct (non-black) ----------------
        armor          = (decker.get("utilities") or {}).get("armor", 0)
        cascade_power  = ic["rating"] + ic.get("cascade_rating_bonus", 0)
        # Shield parry: net successes cancel attacker damage successes before staging (vr2).
        ic_skill       = ic["rating"] if ic["type"] == "Construct" else sec_value
        shield_succ    = _shield_parry(state, decker, attacker_skill=ic_skill, context=ic["type"])
        attack = eng.cybercombat_attack(
            attacker_pool=ic_attack_pool,
            security_code=sec_code,
            target_status=ic_target_status,
            target_bod=eff["bod"],
            armor_rating=armor,
            ic_rating=cascade_power,
            attacker_is_ic=True,
            tn_modifier=cluster_penalty,
            shield_successes=shield_succ,
        )
        final_dmg = attack["resistance"]["final_damage_level"]
        boxes = attack["resistance"]["boxes"]
        # Cascading IC: a miss raises its attack SV; a hit the decker fully resists raises its rating.
        _apply_cascade_outcome(ic, sec_code,
                               hit=attack["attack_roll"]["successes"] > 0, damage_dealt=boxes > 0)

        state["condition_monitor"]["persona_boxes"] += boxes
        _append_event(state, {
            "type": "ic_attack",
            "ic_id": ic["id"],
            "ic_type": ic["type"],
            "ic_rating": ic["rating"],
            "description": (
                f"{ic['type']}-{ic['rating']} attacks: "
                f"{attack['attack_roll']['successes']} attack successes vs "
                f"{attack['resistance']['resist_roll']['successes']} resist. "
                f"Damage: {final_dmg} ({boxes} boxes). "
                f"Persona: {state['condition_monitor']['persona_boxes']}/10"
            ),
            "attack_roll": attack["attack_roll"],
            "resist_roll": attack["resistance"]["resist_roll"],
            "final_damage_level": final_dmg,
            "boxes": boxes,
            "persona_total": state["condition_monitor"]["persona_boxes"],
        })

        # Simsense: hot deck only, white/gray IC only
        if ic_category in ("white", "gray") and decker.get("deck_mode") == "hot":
            sim = eng.simsense_check(
                damage_level=final_dmg,
                willpower=decker.get("willpower", 4),
                deck_mode=decker.get("deck_mode", "hot"),
                has_iccm=decker.get("iccm", False),
            )
            if not sim.get("immune") and sim.get("stun_taken"):
                state["condition_monitor"]["physical_boxes"] += 1
                _append_event(state, {
                    "type": "simsense_overload",
                    "description": f"Simsense overload! Willpower test failed (TN {sim['tn']}). 1 Stun damage.",
                    "roll": sim.get("roll"),
                })

        # Killer / Blaster / Sparky / Construct: check persona crash
        if state["condition_monitor"]["persona_boxes"] >= 10:
            _append_event(state, {
                "type": "persona_crash",
                "description": "PERSONA CRASHED -- decker dumped from the Matrix!",
            })

            # Blaster: MPCP damage test on persona crash (1 per 2 successes)
            if ic["type"] == "Blaster":
                mpcp_hit, b_roll = _roll_mpcp_damage(state, decker, ic["rating"])
                _append_event(state, {
                    "type": "ic_attack",
                    "ic_id": ic["id"], "ic_type": "Blaster",
                    "description": (
                        f"Blaster post-crash MPCP test (TN {b_roll['tn']}): "
                        f"{b_roll['successes']} hits -> MPCP -{mpcp_hit} (permanent)."
                    ),
                    "blaster_roll": b_roll, "mpcp_damage": mpcp_hit,
                })

            # Sparky: MPCP damage (1 per 2 successes) + physical discharge.
            # Sparky raises the MPCP-test TN by 2 vs Blaster.
            elif ic["type"] == "Sparky":
                mpcp_hit, s_roll = _roll_mpcp_damage(state, decker, ic["rating"], tn_bonus=2)
                # VR2 "Sparky": (IC Rating)M physical -- stage up per Sparky-test successes,
                # then the decker RESISTS with Body vs Power (IC rating, reduced by Hardening).
                hardening = decker.get("hardening", 0)
                sparky_staged = eng.stage_damage("Moderate", s_roll["successes"], 1)
                sparky_power = max(1, ic["rating"] - hardening)
                sparky_body = eng.roll_dice(decker.get("body", 4), sparky_power)
                sparky_final = eng.stage_damage(sparky_staged, sparky_body["successes"], -1)
                sparky_boxes = rules.DAMAGE_BOXES[sparky_final]
                state["condition_monitor"]["physical_boxes"] += sparky_boxes
                _append_event(state, {
                    "type": "ic_attack",
                    "ic_id": ic["id"], "ic_type": "Sparky",
                    "description": (
                        f"Sparky discharge on crash (TN {s_roll['tn']}): MPCP -{mpcp_hit} (perm). "
                        f"Body resist ({sparky_body['successes']} hits): "
                        f"{sparky_final} ({sparky_boxes} boxes physical)."
                    ),
                    "sparky_roll": s_roll,
                    "body_roll": sparky_body,
                    "mpcp_damage": mpcp_hit,
                    "physical_damage": sparky_final,
                })

            # Dump shock
            ds = _apply_dump_shock(state, decker, sec_code, sec_value)
            if not ds.get("immune"):
                _append_event(state, {
                    "type": "dump_shock",
                    "description": (
                        f"Dump shock: {ds['final_level']} ({ds['boxes']} boxes physical). "
                        f"Physical: {state['condition_monitor']['physical_boxes']}"
                    ),
                    "dump_shock": ds,
                })
            state["run_ended"] = True
            state["end_reason"] = "persona_crashed"
            break

    # Handle logon completion
    if body.action_type == "logon_to_host" and test["success"]:
        state["logon_complete"] = True
        _append_event(state, {
            "type": "logon",
            "description": f"Logged on to host successfully. Detection Factor: {det_factor}.",
        })

    # Enemy deckers act automatically (app-as-GM), once per pass on the passes their OWN
    # initiative reaches (init//10+1) -- they rolled initiative once when they entered.
    cur_pass = state.get("current_pass", 1)
    for enemy in list(state.get("enemy_deckers", [])):
        if state.get("run_ended"):
            break
        if (enemy.get("status") == "active"
                and cur_pass <= enemy.get("initiative_passes", 1)
                and enemy.get("acted_pass") != cur_pass):
            enemy["acted_pass"] = cur_pass
            _enemy_decker_take_turn(state, decker, run, enemy)

    if state.get("run_ended"):
        run.status = state.get("end_reason", "crashed")

    # Auto-refresh Hacking Pool only when no IC (active or lurking) remains
    if not state.get("run_ended") and "hackingPool_total" in state:
        active_ic  = [ic for ic in state.get("active_ic", []) if ic.get("status") == "active"]
        lurking_ic = state.get("lurking_ic", [])
        if not active_ic and not lurking_ic:
            state["hackingPool_remaining"] = state["hackingPool_total"]

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


@router.post("/{run_id}/attack", response_model=MatrixRunRead)
async def attack_ic(
    run_id: int,
    body: RunAttackInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Decker attacks an active IC program."""
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state = copy.deepcopy(run.state_json)  # deepcopy, not dict(): keep nested JSON mutations un-aliased so the UPDATE fires
    decker = run.decker_json
    sec_code = state["host_security_code"]
    sec_value = state["host_security_value"]

    if state.get("icon_crashed"):
        raise HTTPException(400, "Your icon is crashed by Black IC -- you can only jack out")
    target_ic = next((ic for ic in state.get("active_ic", []) if ic["id"] == body.target_ic_id), None)
    if not target_ic:
        raise HTTPException(404, f"IC {body.target_ic_id} not found or not active")
    if target_ic["status"] != "active":
        raise HTTPException(400, f"IC {body.target_ic_id} is already {target_ic['status']}")
    _one_shot_block(state, decker, "attack")  # a spent One-Shot Attack cannot fire again until reloaded
    _spend_pass_action(state, "attack")        # vr2: a cybercombat attack is a Simple Action

    _spend_hp(state, body.hacking_pool_dice)
    attack_pool     = body.attack_pool + body.hacking_pool_dice
    # Attack program options are read automatically from the deck (not entered per-attack).
    atk_opts   = (decker.get("program_options") or {}).get("attack") or {}
    opt_pen    = bool(atk_opts.get("penetration"))
    opt_chaser = bool(atk_opts.get("chaser"))
    opt_target = bool(atk_opts.get("targeting"))
    opt_skulk  = max(0, int(atk_opts.get("skulk", 0) or 0))
    opt_area   = max(0, int(atk_opts.get("area", 0) or 0))
    cluster_penalty = _cluster_size(state, target_ic.get("cluster_id"))
    # Area option lets one Attack Test cope with an IC cluster -- it offsets the cluster's
    # to-hit penalty (up to the Area rating). This is the single-target-engine equivalent of
    # "hit up to [Area] clustered targets with one test"; it eases the attacker's to-hit only.
    atk_cluster_penalty = max(0, cluster_penalty - opt_area) if opt_area > 0 else cluster_penalty
    base_tn = rules.COMBAT_TN[sec_code]["intruding"] + atk_cluster_penalty
    # Shield/Shift raise the decker's to-hit TN; Penetration defeats Shield, Chaser defeats Shift.
    shield_shift = _shield_shift_tn_modifier(
        target_ic, penetration=opt_pen, chaser=opt_chaser)
    tn = base_tn + shield_shift
    if opt_target:
        tn = max(2, tn - 2)   # Targeting option: -2 to-hit TN on attacks with this utility

    attack_roll = eng.roll_dice(attack_pool, tn)
    base_dmg = rules.IC_DAMAGE_LEVEL[sec_code]

    # IC resists with Security Value dice vs the combat TN (the attack Power here).
    # Armor reduces that POWER (lower TN -> the IC resists more easily) -- it does NOT lower
    # the damage level. Expert adds/removes resist dice (Defense +N, Offense -N -- the trade-off).
    resist_tn = rules.COMBAT_TN[sec_code]["intruding"] + cluster_penalty
    if _ic_has_armor(target_ic):
        # Armor lowers the attack Power, not the damage level. vr2: Armor is extra-effective
        # vs an Area-option utility (+2 effective Armor), so an Area strike resists 2 deeper.
        resist_tn = max(2, resist_tn - 2 - (2 if opt_area > 0 else 0))
    resist_pool = max(1, sec_value + _ic_expert(target_ic, "defense") - _ic_expert(target_ic, "offense"))
    resist_roll = eng.roll_dice(resist_pool, resist_tn)
    staged = eng.stage_damage(base_dmg, attack_roll["successes"], 1)
    final_dmg = eng.stage_damage(staged, resist_roll["successes"], -1)
    boxes = rules.DAMAGE_BOXES[final_dmg]

    target_ic["boxes"] = target_ic.get("boxes", 0) + boxes
    crashed = target_ic["boxes"] >= 10

    if crashed:
        target_ic["status"] = "crashed"
        # Skulk option on the Attack utility masks the crash: reduce the resulting security-tally
        # increase by the Skulk rating (vr2_rules). Skulk does NOT zero the bump at 6+ -- a high-
        # rating IC still leaks tally past the masking (e.g. Rating-10 IC, Skulk-8 -> +2). The
        # bump is otherwise the crashed IC's full rating. Read automatically from the deck.
        skulk = opt_skulk
        tally_increase = max(0, target_ic["rating"] - skulk)
        state["security_tally"] += tally_increase
        skulk_note = (
            f" (Skulk-{skulk} masked the crash)"
            if skulk > 0 and tally_increase < target_ic["rating"] else ""
        )
        _append_event(state, {
            "type": "ic_crashed",
            "ic_id": body.target_ic_id,
            "description": (
                f"{target_ic['type']}-{target_ic['rating']} CRASHED. "
                f"Tally +{tally_increase} -> {state['security_tally']}{skulk_note}"
            ),
            "tally_increase": tally_increase,
        })
        _check_and_activate_sheaf(state, sec_code)

        # Spawn hidden IC if this was a Trap IC
        trap_hidden = target_ic.get("trap_hidden")
        if trap_hidden:
            h_type   = trap_hidden.get("type", "Blaster")
            h_rating = trap_hidden.get("rating", 6)
            new_id   = f"ic_{uuid.uuid4().hex[:8]}"
            new_init = eng.ic_initiative_roll(h_rating, sec_code)
            state["active_ic"].append({
                "id": new_id,
                "type": h_type,
                "rating": h_rating,
                "category": rules.IC_CATALOG.get(h_type, {}).get("category", "gray"),
                "boxes": 0,
                "suppressed": False,
                "initiative": new_init,
                "status": "active",
                "hunt_cycle_successes": 0,
            })
            _append_event(state, {
                "type": "ic_activation",
                "ic_id": new_id,
                "ic_type": h_type,
                "ic_rating": h_rating,
                "is_trap_reveal": True,
                "description": (
                    f"TRAP TRIGGERED -- hidden {h_type}-{h_rating} revealed! "
                    f"(initiative {new_init})"
                ),
            })
    else:
        _append_event(state, {
            "type": "decker_attack",
            "ic_id": body.target_ic_id,
            "description": (
                f"Attacked {target_ic['type']}-{target_ic['rating']}: "
                f"{attack_roll['successes']} successes. Dealt {final_dmg} ({boxes} boxes). "
                f"IC: {target_ic['boxes']}/10"
            ),
            "attack_roll": attack_roll,
            "resist_roll": resist_roll,
            "final_damage_level": final_dmg,
            "boxes": boxes,
            "ic_boxes": target_ic["boxes"],
        })

    _spend_one_shot(state, decker, "attack")
    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


def _apply_swap_memory(
    state: dict,
    decker: dict,
    *,
    target_program: str,
    swap_out_program: str,
) -> tuple[bool, str]:
    """Resolve a Swap Memory action (vr2, Simple Action, no test). Mutates ``state``
    (storage_programs / program_sizes / program_damage) and ``decker`` (utilities) in place and
    returns ``(decker_changed, description)``. Modes, in priority order:

      1. Load a stored program into active memory (``target_program`` names a stored program),
         optionally pushing ``swap_out_program`` from active back to storage to make room.
      2. Push an active program to storage only (``swap_out_program`` set, no storage target).
      3. Reload a crashed/degraded *active* program from its storage copy (restore its rating
         after Hog / Tar Baby / One-Shot / degraded Armor-Shield).

    Active programs always keep a storage copy, so a swap only shifts *active* memory usage;
    deck storage_free_mp is unaffected. Raises 400 if a load would overflow the active cap and
    no program is freed.
    """
    utils   = decker.setdefault("utilities", {})
    storage = state.setdefault("storage_programs", [])
    sizes   = state.setdefault("program_sizes", {})
    pd      = state.setdefault("program_damage", {})
    cap     = int(state.get("active_memory_cap", 0) or 0)

    def _pretty(n: str) -> str:
        return str(n).replace("_", " ").title()

    def _active_used() -> int:
        return sum(int(sizes.get(n, 0)) for n, r in utils.items() if (r or 0) > 0)

    target   = (target_program or "").strip().lower()
    swap_out = (swap_out_program or "").strip().lower()
    store_entry = next((p for p in storage
                        if str(p.get("name", "")).strip().lower() == target), None)

    # A One-Shot program crashed by Tar IC is corrupted on EVERY copy (vr2_rules.md L1667): its
    # storage copy is already gone (see _wipe_one_shot), so refuse an explicit reload by name too.
    wiped = set(state.get("one_shot_wiped") or [])
    if target and target in wiped:
        raise HTTPException(
            400,
            f"{_pretty(target)}: all copies were corrupted by Tar IC -- it cannot be reloaded."
        )

    if store_entry:
        # Mode 1: load a stored program into active memory.
        in_size = int(store_entry.get("size", 0) or 0)
        note = ""
        if swap_out and (utils.get(swap_out, 0) or 0) > 0:
            storage.append({"name": swap_out, "rating": int(utils.get(swap_out, 0) or 0),
                            "size": int(sizes.get(swap_out, 0) or 0)})
            utils[swap_out] = 0
            pd.pop(swap_out, None)
            note = f" (swapped {_pretty(swap_out)} out to storage)"
        if cap > 0 and _active_used() + in_size > cap:
            used = _active_used()
            raise HTTPException(
                400,
                f"Not enough active memory to load {_pretty(target)}: needs {in_size} Mp but "
                f"only {max(0, cap - used)} Mp free ({used}/{cap} Mp used). Swap a program out "
                "to free active memory."
            )
        utils[target] = int(store_entry.get("rating", 0) or 0)
        sizes[target] = in_size
        pd.pop(target, None)   # fresh storage copy -- no accrued damage
        storage.remove(store_entry)
        return True, (f"Swap Memory -- loaded {_pretty(target)} (rating {utils[target]}) into "
                      f"active memory{note}.")

    if swap_out and (utils.get(swap_out, 0) or 0) > 0:
        # Mode 2: push an active program to storage (no incoming program).
        storage.append({"name": swap_out, "rating": int(utils.get(swap_out, 0) or 0),
                        "size": int(sizes.get(swap_out, 0) or 0)})
        utils[swap_out] = 0
        pd.pop(swap_out, None)
        return True, f"Swap Memory -- moved {_pretty(swap_out)} from active memory to storage."

    # Mode 3: reload a crashed/degraded active program from its storage copy.
    reload_target = target or next((k for k, v in pd.items() if v > 0 and k not in wiped), None)
    if reload_target and pd.get(reload_target, 0) > 0:
        pd[reload_target] = 0
        return False, (f"Swap Memory -- reloaded {_pretty(reload_target)} from storage; "
                       "rating restored.")
    return False, "Swap Memory -- no program to load or reload."


def _apply_graceful_logoff(
    state: dict,
    decker: dict,
    *,
    hacking_pool_dice: int,
    deception_utility: int,
) -> bool:
    """Resolve a Graceful Logoff Access Test (vr2). Mutates ``state`` in place and returns
    True on success. On success the run is marked ended with all traces cleared; on failure
    the security tally rises and the sheaf may activate. Shared by the POST /{run_id}/logoff
    endpoint and the ``graceful_logoff`` action on POST /{run_id}/action so both behave
    identically (the /action path was previously a no-op).
    """
    sec_code = state["host_security_code"]
    sec_value = state["host_security_value"]

    # Graceful logoff: Access Test vs. host Access Rating
    access_rating = _subsystem_rating(state, "access")
    det_factor = _effective_detection_factor(state, decker)
    state["detection_factor"] = det_factor

    # Check for active trace IC -- adds its rating to TN
    trace_tn_bonus = 0
    for ic in state.get("active_ic", []):
        if ic["status"] == "active" and "Trace" in ic.get("type", ""):
            trace_tn_bonus = max(trace_tn_bonus, ic["rating"])

    _spend_hp(state, hacking_pool_dice)
    pool = decker.get("computer_skill", 4) + hacking_pool_dice
    # Console access halves the host Security Value for this Access Test (vr2).
    logoff_sec_value = -(-sec_value // 2) if state.get("console_access") else sec_value
    test = eng.system_test(
        decker_pool=pool,
        subsystem_rating=access_rating,
        security_value=logoff_sec_value,
        det_factor=det_factor,
        extra_tn_modifier=(-deception_utility + trace_tn_bonus),
    )

    tally_increase = test["tally_increase"]
    state["security_tally"] += tally_increase

    if test["success"]:
        state["run_ended"] = True
        state["end_reason"] = "graceful_logoff"
        state.pop("has_legitimate_status", None)  # Host deletes passcode on logoff
        state["decoy_successes"] = 0
        state["decoy_hp"] = 0
        _append_event(state, {
            "type": "logoff_success",
            "description": "Graceful logoff successful. All traces cleared. Run complete.",
            "decker_roll": test["decker_roll"],
            "host_roll": test["host_roll"],
            "tally_increase": tally_increase,
        })
    else:
        _append_event(state, {
            "type": "logoff_fail",
            "description": (
                f"Graceful logoff FAILED. Tally +{tally_increase} -> {state['security_tally']}. "
                "Still logged on -- try again or jack out (dump shock)."
            ),
            "decker_roll": test["decker_roll"],
            "host_roll": test["host_roll"],
            "tally_increase": tally_increase,
        })
        _check_and_activate_sheaf(state, sec_code)

    return bool(test["success"])


@router.post("/{run_id}/logoff", response_model=MatrixRunRead)
async def graceful_logoff(
    run_id: int,
    body: RunLogoffInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Attempt graceful logoff. Clears traces on success; dump shock on failure."""
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state = copy.deepcopy(run.state_json)  # deepcopy, not dict(): keep nested JSON mutations un-aliased so the UPDATE fires
    decker = run.decker_json
    _spend_pass_action(state, "graceful_logoff")   # vr2: Graceful Logoff is a Complex Action
    success = _apply_graceful_logoff(
        state, decker,
        hacking_pool_dice=body.hacking_pool_dice,
        deception_utility=body.deception_utility,
    )
    if success:
        run.status = "escaped"

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


@router.post("/{run_id}/trap-door/{td_id}", response_model=MatrixRunRead)
async def trap_door_action(
    run_id: int,
    td_id: str,
    body: RunTrapDoorInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Act on a DISCOVERED trap door (vr2). ``action="file"`` records it for later -- the
    destination is reachable ONLY through this door (you have no LTG address for it), so filing
    just keeps it on the books; it does NOT reveal where it leads or whether the far host has LTG
    access. ``action="enter"`` resolves the SR2 transit: a Graceful Logoff through the concealing
    subsystem, then -- on success -- a fresh linked run on the destination host (returned), where
    the decker must Logon to Host (and can Analyze its Access subsystem to learn its LTG status).
    The destination is never sent to a player before arrival."""
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state = copy.deepcopy(run.state_json)  # deepcopy, not dict(): keep nested JSON mutations un-aliased so the UPDATE fires
    if state.get("run_ended"):
        raise HTTPException(400, "Run has already ended")
    door = next((d for d in (state.get("trap_doors") or []) if str(d.get("id")) == str(td_id)), None)
    if door is None:
        raise HTTPException(404, "Trap door not found")
    if not door.get("discovered"):
        raise HTTPException(400, "Trap door has not been discovered yet (Analyze Subsystem first)")

    # FILE: record the door for later. The destination stays unknown -- reachable only by entering
    # the door; its LTG access can only be learned on the far side (logon + Analyze Access).
    if body.action == "file":
        door["filed"] = True
        _append_event(state, {
            "type": "trap_door_filed",
            "trap_door_id": door.get("id"),
            "description": (
                "Trap door filed. The destination is reachable only through this door -- "
                "enter it and analyze its Access subsystem to learn whether it has LTG access."
            ),
        })
        run.state_json = state
        await db.commit()
        await db.refresh(run)
        return _serialize_run(run, auth)

    # ENTER: graceful logoff through the concealing subsystem, then arrive on the destination.
    dest_id = door.get("destination_host_id")
    if not dest_id:
        raise HTTPException(400, "This trap door has no linked destination host (LTG-only). File it for intel instead.")
    dest_host = await _get_host_or_404(db, dest_id)

    success = _apply_graceful_logoff(
        state, run.decker_json,
        hacking_pool_dice=body.hacking_pool_dice,
        deception_utility=body.deception_utility,
    )
    if not success:
        # Logoff failed -- still logged on to the current host; transit aborted.
        run.state_json = state
        await db.commit()
        await db.refresh(run)
        return _serialize_run(run, auth)

    # Logoff succeeded -- exit this host through the trap door and land on the destination.
    run.status = "escaped"
    state["end_reason"] = "trap_door_transit"
    _append_event(state, {
        "type": "trap_door_entered",
        "trap_door_id": door.get("id"),
        "destination_host_id": dest_id,
        "description": f"Entered trap door -- arrived at host \"{dest_host.name}\". Logon to continue.",
    })
    run.state_json = state
    await db.commit()

    new_run = await _create_run(db, auth, dest_host, dict(run.decker_json or {}))
    return _serialize_run(new_run, auth)


def _apply_crash_ic_penalty(state: dict) -> None:
    """Reduce every active IC's rating by 2 during a Crash Host countdown (vr2). Idempotent and
    re-asserted each turn so IC that activate mid-countdown are penalized too."""
    for ic in state.get("active_ic", []):
        if ic.get("status") == "active" and not ic.get("crash_penalized"):
            ic["crash_penalized"] = True
            ic["rating"] = max(1, int(ic.get("rating", 1)) - 2)


def _restore_crash_ic_penalty(state: dict) -> None:
    """Restore IC ratings reduced by a Crash Host countdown (when the host aborts the crash)."""
    for ic in state.get("active_ic", []):
        if ic.get("crash_penalized"):
            ic["rating"] = int(ic.get("rating", 1)) + 2
            ic.pop("crash_penalized", None)


def _complete_host_crash(state: dict) -> None:
    """Resolve a completed Crash Host: the host goes down and the decker rides the crash out,
    logging off cleanly -- effectively a graceful logoff (no dump shock, all traces cleared).
    The run ends successfully (vr2: crashing the host is a clean exit, not a forced dump)."""
    state.pop("crash_host_countdown", None)
    state["run_ended"] = True
    state["end_reason"] = "host_crashed"
    state.pop("has_legitimate_status", None)   # host is gone -- any passcode goes with it
    state["decoy_successes"] = 0
    state["decoy_hp"] = 0
    _append_event(state, {
        "type": "crash_host_complete",
        "description": (
            "HOST SUCCESSFULLY CRASHED -- the system goes down and you ride the crash out, "
            "logging off cleanly. No dump shock; all traces cleared. Run complete."
        ),
    })


def _process_crash_countdown(state: dict) -> None:
    """End-of-turn Crash Host processing: re-assert the IC penalty on any newly active IC, roll
    the host's abort test (Security Value vs decker MPCP -- any success aborts), then decrement or
    resolve the countdown. On completion the host crashes and the decker logs off cleanly (see
    _complete_host_crash)."""
    cd = state.get("crash_host_countdown")
    if not cd:
        return
    _apply_crash_ic_penalty(state)
    sec_value = int(state.get("host_security_value", 6) or 6)
    mpcp = int(cd.get("decker_mpcp", 1) or 1)
    abort_roll = eng.roll_dice(sec_value, max(2, mpcp))
    if abort_roll["successes"] > 0:
        _restore_crash_ic_penalty(state)
        state.pop("crash_host_countdown", None)
        _append_event(state, {
            "type": "crash_host_aborted",
            "roll": abort_roll,
            "description": (
                f"Host ABORTED the crash (Security Value {sec_value} vs MPCP {mpcp}: "
                f"{abort_roll['successes']} success(es)). IC ratings restored; countdown cancelled."
            ),
        })
        return
    cd["turns_remaining"] = int(cd.get("turns_remaining", 1)) - 1
    if cd["turns_remaining"] <= 0:
        _complete_host_crash(state)
    else:
        _append_event(state, {
            "type": "crash_host_tick",
            "turns_remaining": cd["turns_remaining"],
            "description": (
                f"Host crash countdown: {cd['turns_remaining']} turn"
                f"{'s' if cd['turns_remaining'] != 1 else ''} until shutdown "
                f"(host failed to abort: Security Value {sec_value} vs MPCP {mpcp})."
            ),
        })


@router.post("/{run_id}/new-turn", response_model=MatrixRunRead)
async def new_turn(
    run_id: int,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Advance to the decker's next action phase, refreshing the Hacking Pool."""
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")
    state = copy.deepcopy(run.state_json)  # deepcopy, not dict(): keep nested JSON mutations un-aliased so the UPDATE fires
    if state.get("run_ended"):
        raise HTTPException(400, "Run has already ended")

    hackingPool_total = state.get("hackingPool_total", 0)
    old_hp = state.get("hackingPool_remaining", hackingPool_total)
    state["hackingPool_remaining"] = hackingPool_total
    state["current_turn"] = state.get("current_turn", 1) + 1
    # Initiative is rolled ONCE per cybercombat encounter (not per Combat Turn). A new turn
    # just refreshes the action budget and lets every actor act again on its FIXED passes;
    # clear the per-pass "acted" markers so NPCs act again this turn.
    init = state.get("decker_initiative")
    passes = state.get("initiative_passes", 1)
    state["current_pass"] = 1
    state["actions_this_turn"] = 0
    _reset_pass_budget(state)
    for ic in state.get("active_ic", []):
        ic.pop("acted_pass", None)
        # Slow resume (vr2_rules.md L1578): a hung/slowed IC resumes normal operation at the start
        # of the next Combat Turn UNLESS it is still suppressed -- clear its per-turn slow markers
        # so it acts on its full initiative passes again.
        if not ic.get("suppressed"):
            ic.pop("actions_lost", None)
            ic.pop("slow_turn", None)
            ic.pop("hung_turn", None)
    for enemy in state.get("enemy_deckers", []):
        enemy.pop("acted_pass", None)

    _append_event(state, {
        "type": "new_turn",
        "description": (
            f"Turn {state['current_turn']} begins. Actions refreshed (initiative {init}, "
            f"{passes} pass{'es' if passes != 1 else ''}). Hacking Pool ({old_hp} -> {hackingPool_total})."
        ),
    })

    # Persistent Hog infections re-drain the highest running program each Combat Turn (vr2).
    decker = run.decker_json
    for inf in state.get("hog_infections", []):
        frag = _apply_hog_drain(state, decker, inf.get("drain", 0))
        if frag:
            _append_event(state, {
                "type": "enemy_decker", "outcome": "hog",
                "description": f"Hog-{inf.get('rating')} virus drains your deck: {frag}.",
            })

    # End-of-turn Crash Host processing: host abort roll + countdown decrement / resolution.
    _process_crash_countdown(state)

    # A completed Crash Host ends the run as a clean exit (treated like a graceful logoff).
    if state.get("run_ended"):
        run.status = "escaped" if state.get("end_reason") == "host_crashed" else state.get("end_reason", "crashed")

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


@router.post("/{run_id}/resolve-reactive", response_model=MatrixRunRead,
             dependencies=[Depends(get_admin_token)])
async def resolve_reactive_ic(
    run_id: int,
    body: RunReactiveInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """GM triggers a lurking Tar Baby / Tar Pit against the decker's utility."""
    run = await _get_run_or_404(db, run_id)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state  = dict(run.state_json)
    decker = run.decker_json

    lurking = next(
        (ic for ic in state.get("lurking_ic", []) if ic["id"] == body.ic_id),
        None,
    )
    if not lurking:
        raise HTTPException(404, f"Lurking IC {body.ic_id} not found")

    if lurking["type"] == "Worm":
        # Worm attacks the deck's MPCP; the CARRIED Disinfect utility defends automatically
        # (vr2: a running Disinfect raises the Worm Infection Test target number). We read the
        # rating from the decker's load-out -- NOT the GM-typed utility_rating -- so a decker who
        # actually loaded Disinfect defends without the GM re-entering it (and a decker who did
        # not stays at +0). utility_rating still drives the Tar Baby / Tar Pit branches below.
        disinfect_rating = _effective_disinfect(decker, state)
        wr = eng.worm_attack(
            ic_rating=lurking["rating"],
            mpcp_rating=decker.get("mpcp", 1),
            hardening=decker.get("hardening", 0),
            disinfect_utility=disinfect_rating,
        )
        if wr["mpcp_infected"]:
            state["mpcp_infected"] = True
            state["chip_replacement_required"] = True
            state["lurking_ic"] = [
                ic for ic in state.get("lurking_ic", []) if ic["id"] != body.ic_id]
            _append_event(state, {
                "type": "worm_resolved", "ic_id": body.ic_id, "ic_type": "Worm",
                "outcome": "mpcp_infected", "roll": wr["roll"],
                "description": (
                    f"Worm-{lurking['rating']} infected the MPCP -- chip replacement required "
                    f"(permanent). Carried Disinfect-{disinfect_rating} failed."
                ),
            })
        else:
            _append_event(state, {
                "type": "worm_resolved", "ic_id": body.ic_id, "ic_type": "Worm",
                "outcome": "repelled", "roll": wr["roll"],
                "description": (
                    f"Worm-{lurking['rating']} repelled by carried Disinfect-{disinfect_rating}. "
                    f"Worm still lurking."
                ),
            })
        run.state_json = state
        await db.commit()
        await db.refresh(run)
        return _serialize_run(run, auth)

    is_tar_pit = lurking["type"] == "Tar Pit"
    result = eng.tar_baby_test(
        ic_rating=lurking["rating"],
        utility_rating=body.utility_rating,
        is_tar_pit=is_tar_pit,
        mpcp_rating=decker.get("mpcp", 1),
        hardening=decker.get("hardening", 0),
    )

    if result["ic_wins"]:
        state["lurking_ic"] = [
            ic for ic in state.get("lurking_ic", []) if ic["id"] != body.ic_id
        ]
        _append_event(state, {
            "type": "reactive_ic_resolved",
            "ic_id": body.ic_id,
            "ic_type": lurking["type"],
            "outcome": "ic_wins",
            "ic_roll": result["ic_roll"],
            "util_roll": result["util_roll"],
            "description": (
                f"{lurking['type']}-{lurking['rating']} triggered vs "
                f"{body.utility_name}-{body.utility_rating}. "
                f"IC wins -- {body.utility_name} and {lurking['type']} both crash."
            ),
        })
        if is_tar_pit and result.get("all_copies_corrupted"):
            _append_event(state, {
                "type": "tar_pit_corruption",
                "description": f"Tar Pit: ALL copies of {body.utility_name} corrupted.",
                "tar_pit_roll": result.get("tar_pit_roll"),
            })
        # If the crashed utility was a One-Shot copy, the tar wipes EVERY copy on the deck
        # (vr2_rules.md L1667) -- it can never be reloaded this run. No-op for a normal program.
        _wipe_one_shot(state, decker, body.utility_name)
    else:
        _append_event(state, {
            "type": "reactive_ic_resolved",
            "ic_id": body.ic_id,
            "ic_type": lurking["type"],
            "outcome": "util_wins",
            "ic_roll": result["ic_roll"],
            "util_roll": result["util_roll"],
            "description": (
                f"{lurking['type']}-{lurking['rating']} triggered vs "
                f"{body.utility_name}-{body.utility_rating}. "
                f"Utility wins -- {lurking['type']} remains lurking."
            ),
        })

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


def _highest_running_utility(decker: dict, program_damage: dict) -> tuple[str | None, int]:
    """Return (name, effective_rating) of the decker's highest-rated still-running utility
    (for Hog to target). Excludes already-crashed programs."""
    utils = decker.get("utilities") or {}
    best_name, best_eff = None, 0
    for name, rating in utils.items():
        eff = (rating or 0) - program_damage.get(name, 0)
        if eff > best_eff:
            best_name, best_eff = name, eff
    return best_name, best_eff


def _apply_hog_drain(state: dict, decker: dict, drain: int) -> str:
    """One Hog drain pass: reduce the decker's highest running utility by ``drain``
    (vr2: 'reduce the highest-rated running program', repeating until it crashes, then the
    next-highest). Returns a short description fragment, or '' if nothing was drained."""
    if drain <= 0:
        return ""
    pd = state.setdefault("program_damage", {})
    name, eff = _highest_running_utility(decker, pd)
    if not name or eff <= 0:
        return ""
    applied = min(drain, eff)
    pd[name] = pd.get(name, 0) + applied
    base = (decker.get("utilities") or {}).get(name, 0)
    crashed = pd[name] >= base
    return f"{name.replace('_', ' ').title()} -{applied}{' (CRASHED)' if crashed else ''}"


def _enemy_decker_take_turn(state: dict, decker: dict, run, enemy: dict) -> None:
    """One enemy-decker action against the PC. Mutates ``state`` (and ``run.status`` on a
    kill/dump). Phase 1 = locate the PC; once located, Phase 2 = execute its program.

    Driven automatically by the app-as-GM loop (perform_action / new_turn): the app plays the
    opponent -- spawned enemy deckers hunt and act on their own. Does NOT commit -- the caller
    persists state.
    """
    if enemy.get("status") != "active" or state.get("run_ended"):
        return
    sec_code = state["host_security_code"]
    sec_value = state["host_security_value"]
    eff = _get_decker_effective(decker, state)

    # -- Phase 1: locate the PC --------------------------------------------------
    if not enemy.get("located"):
        first_contact = not enemy.get("revealed")
        enemy["revealed"] = True   # the PC realises a hostile decker is hunting them
        loc = eng.enemy_locate_test(
            computer_skill=enemy["computer_skill"],
            scanner_rating=(enemy.get("utilities") or {}).get("scanner", 0),
            sensor_rating=enemy["sensor"],
            pc_detection_factor=_effective_detection_factor(state, decker),
            pc_evasion=eff["evasion"],
        )
        enemy["locate_progress"] = enemy.get("locate_progress", 0) + loc["progress_gain"]
        if first_contact:
            _append_event(state, {
                "type": "enemy_decker", "outcome": "hunting", "enemy_id": enemy["id"],
                "description": (
                    f"ALERT -- a hostile decker ({enemy['name']}) is hunting your icon. "
                    "Evade (Relocate/Redirect), log off, or strike first."
                ),
            })
        if enemy["locate_progress"] >= eng.ENEMY_LOCATE_THRESHOLD:
            enemy["located"] = True
            _append_event(state, {
                "type": "enemy_decker", "outcome": "located", "enemy_id": enemy["id"],
                "description": f"{enemy['name']} has PINPOINTED your icon and jackpoint.",
            })
        else:
            _append_event(state, {
                "type": "enemy_decker", "outcome": "probing", "enemy_id": enemy["id"],
                "gm_only": True,
                "description": (
                    f"{enemy['name']} probing: +{loc['progress_gain']} -> "
                    f"{enemy['locate_progress']}/{eng.ENEMY_LOCATE_THRESHOLD} located."
                ),
            })
        return

    # -- Phase 2: execute the enemy's offensive program --------------------------
    intent = eng.escalate_enemy_intent(enemy["intent"], security_tally=state.get("security_tally", 0))
    if intent == "kill" and not enemy.get("lethal_program"):
        intent = "dump"   # no lethal program loaded -> can only crash the icon
    cm = state.setdefault("condition_monitor", {})
    cm.setdefault("persona_damage", {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0})
    hacking_pool = max(0, (enemy.get("intelligence", 3) + enemy.get("mpcp", 4)) // 3)

    # Choose the program by the enemy's (possibly escalated) intent.
    if intent == "kill" and enemy.get("lethal_program"):
        program = enemy["lethal_program"]
    else:
        program = "Attack"
    if program in ("Black Hammer", "Killjoy"):
        intent = "kill"
    enemy["intent"] = intent

    attack_rating = (enemy.get("utilities") or {}).get("attack", 4)
    is_lethal = program in ("Black Hammer", "Killjoy")
    power = enemy.get("lethal_rating", 0) if is_lethal else attack_rating
    pool = power + hacking_pool
    did_icon_damage = False

    if program == "Hog":
        hog = eng.hog_attack(
            attacker_pool=pool, security_code=sec_code, target_status="intruding",
            hog_rating=attack_rating, mpcp_rating=decker.get("mpcp", 4),
            hardening=decker.get("hardening", 0))
        if hog["attack_roll"]["successes"] > 0 and hog["reduction"] > 0:
            drain = hog["reduction"]
            state.setdefault("hog_infections", []).append({
                "id": f"hog_{uuid.uuid4().hex[:8]}", "rating": attack_rating, "drain": drain})
            frag = _apply_hog_drain(state, decker, drain)
            desc = (f"HOG -- {enemy['name']}'s virus takes hold (drains {drain}/turn): "
                    f"{frag or 'no running program left'}. Purge it or reload via Swap Memory.")
        else:
            desc = f"HOG -- {enemy['name']}'s virus fails to take hold this pass."
        _append_event(state, {
            "type": "enemy_decker", "outcome": "hog", "enemy_id": enemy["id"],
            "program": "Hog", "attack_roll": hog["attack_roll"], "description": desc})

    elif program in ("Poison", "Restrict", "Reveal"):
        attr = {"Poison": "bod", "Restrict": "evasion", "Reveal": "masking"}[program]
        # Shield parry: net successes ADD to the decker's opposed defence (vr2).
        shield_succ = _shield_parry(state, decker,
                                    attacker_skill=enemy["computer_skill"], context=program)
        cr = eng.decker_attribute_attack(
            attacker_pool=pool, security_code=sec_code, target_status="intruding",
            program_rating=attack_rating, target_attribute_rating=eff[attr],
            shield_successes=shield_succ)
        if cr["reduction"] > 0:
            cm["persona_damage"][attr] = cm["persona_damage"].get(attr, 0) + cr["reduction"]
            # Record the enemy program's rating as this attribute's causing rating (Restore TN).
            _record_crippler_rating(state, attr, attack_rating)
            now = max(1, decker.get(attr, 4) - cm["persona_damage"][attr])
            desc = (f"{program.upper()} -- {enemy['name']} cripples your {attr.title()} by "
                    f"{cr['reduction']} (now {now}, until logoff).")
        else:
            desc = f"{program.upper()} -- {enemy['name']}'s crippler attack is resisted."
        _append_event(state, {
            "type": "enemy_decker", "outcome": program.lower(), "enemy_id": enemy["id"],
            "program": program, "attack_roll": cr["attack_roll"], "description": desc})

    else:  # Attack / Black Hammer / Killjoy -> icon damage (+ biofeedback if lethal)
        # Shield parry once: it blunts the icon hit and (for lethal programs) the biofeedback
        # that derives from the same parried strike.
        shield_succ = _shield_parry(state, decker,
                                    attacker_skill=enemy["computer_skill"], context=program)
        atk = eng.cybercombat_attack(
            attacker_pool=pool, security_code=sec_code, target_status="intruding",
            target_bod=eff["bod"], armor_rating=(decker.get("utilities") or {}).get("armor", 0),
            ic_rating=power, attacker_is_ic=True, shield_successes=shield_succ)
        boxes = atk["resistance"]["boxes"]
        cm["persona_boxes"] = cm.get("persona_boxes", 0) + boxes
        did_icon_damage = True
        desc = (f"{enemy['name']} hits your icon with {program} -- "
                f"{atk['resistance']['final_damage_level']} ({boxes} boxes). "
                f"Persona {cm['persona_boxes']}/10.")
        if is_lethal:
            bio = eng.damage_resistance(
                bod=decker.get("body", 4), power=power, base_damage_level="Serious",
                attacker_successes=atk["attack_roll"]["successes"],
                shield_successes=shield_succ)
            cm["physical_boxes"] = cm.get("physical_boxes", 0) + bio["boxes"]
            dmg_kind = "Stun" if program == "Killjoy" else "Physical"
            desc = (f"{program.upper()} -- {enemy['name']} drives lethal biofeedback into you: "
                    f"icon {atk['resistance']['final_damage_level']} ({boxes}), {dmg_kind} "
                    f"{bio['final_damage_level']} ({bio['boxes']}). "
                    f"Persona {cm['persona_boxes']}/10, Physical {cm['physical_boxes']}/10.")
            if cm["physical_boxes"] >= 10:
                state["run_ended"] = True
                state["end_reason"] = "killed_by_" + ("killjoy" if program == "Killjoy" else "black_hammer")
                run.status = "killed"
        _append_event(state, {
            "type": "enemy_decker", "outcome": "kill" if is_lethal else "dump",
            "enemy_id": enemy["id"], "program": program,
            "attack_roll": atk["attack_roll"], "description": desc})

    # Icon crash -> dump shock (+ lethal MPCP burn) -- only when the program hit the icon.
    if did_icon_damage and not state.get("run_ended") and cm.get("persona_boxes", 0) >= 10:
        ds = _apply_dump_shock(state, decker, sec_code, sec_value)
        state["icon_crashed"] = True
        state["run_ended"] = True
        state["end_reason"] = "icon_crashed_by_decker"
        run.status = "dumped"
        shock = "immune" if ds.get("immune") else f"{ds['boxes']} physical boxes"
        mpcp_note = ""
        if is_lethal:
            mpcp_hit, _b = _roll_mpcp_damage(state, decker, power, pool_multiplier=2)
            if mpcp_hit > 0:
                mpcp_note = f" {program} fried the MPCP on the way out: -{mpcp_hit} (permanent)."
        _append_event(state, {
            "type": "persona_crash", "enemy_id": enemy["id"],
            "description": f"PERSONA CRASHED by {enemy['name']} -- dumped (dump shock: {shock}).{mpcp_note}",
        })

    if not state.get("run_ended"):
        # Reveal (masking) cripples flow into the Detection Factor -- keep it in sync for the UI.
        state["detection_factor"] = _effective_detection_factor(state, decker)


@router.post("/{run_id}/enemy-decker/attack", response_model=MatrixRunRead)
async def attack_enemy_decker(
    run_id: int,
    body: RunEnemyAttackInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """The PC strikes back at a revealed enemy decker (two-way cybercombat).

    ``program="attack"`` (default) crashes the enemy icon (10 boxes). ``program`` of
    ``"poison"`` / ``"restrict"`` / ``"reveal"`` runs the offensive crippler programs
    against the enemy's Bod / Evasion / Masking respectively (vr2: the decker versions of
    the Acid / Binder / Marker IC) -- the attacker's net successes // 2 reduce that
    attribute (floored at 1, lasting until the enemy logs off). ``program`` of
    ``"black_hammer"`` (lethal Physical) / ``"killjoy"`` (lethal Stun) are the decker's
    lethal offensive programs (vr2: they "function like black IC but from a decker") --
    a hard icon hit that, on an icon crash, burns the enemy's MPCP via a blaster-style
    test at DOUBLE the program rating and takes the hostile decker out; the effective
    rating is capped at ceil(Computer skill / 2). All of these target enemy DECKERS/frames
    only; they are never routed through IC."""
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")
    state = copy.deepcopy(run.state_json)
    decker = run.decker_json
    if state.get("icon_crashed"):
        raise HTTPException(400, "Your icon is crashed -- you can only jack out")
    enemy = next((e for e in state.get("enemy_deckers", [])
                  if e.get("id") == body.enemy_id and e.get("status") == "active"
                  and e.get("revealed")), None)
    if enemy is None:
        raise HTTPException(404, "No such revealed enemy decker to attack")
    # A spent / tar-wiped One-Shot offensive program (attack / poison / restrict / reveal /
    # black_hammer / killjoy) cannot fire again until a fresh copy is loaded via Swap Memory.
    _one_shot_block(state, decker, body.program)
    _spend_pass_action(state, "attack")        # vr2: a cybercombat attack is a Simple Action

    sec_code = state["host_security_code"]
    _spend_hp(state, body.hacking_pool_dice)
    pool = body.attack_pool + body.hacking_pool_dice
    util = decker.get("utilities") or {}

    # Poison / Restrict / Reveal -- the PC's offensive crippler programs vs an enemy decker
    # (vr2: the decker versions of the Acid / Binder / Marker IC). Attack to hit, then the
    # target resists with the targeted attribute (dice) vs the program rating; the attacker's
    # net successes // 2 reduce that attribute, floored at 1. Poison->Bod, Restrict->Evasion,
    # Reveal->Masking. These target enemy DECKERS/frames only -- never routed through IC.
    if body.program in ("poison", "restrict", "reveal"):
        attr = {"poison": "bod", "restrict": "evasion", "reveal": "masking"}[body.program]
        # Program rating = the carried Poison/Restrict/Reveal utility (the resist TN); fall back
        # to the thrown pool if the player supplied one but no rating is recorded.
        program_rating = int(util.get(body.program, 0) or 0) or body.attack_pool
        target_rating = max(1, int(enemy.get(attr, 1) or 1))
        cr = eng.decker_attribute_attack(
            attacker_pool=pool, security_code=sec_code, target_status="intruding",
            program_rating=program_rating, target_attribute_rating=target_rating,
            # The enemy decker has no Shield modeled -> shield_successes stays 0.
        )
        reduction = cr["reduction"]
        label = body.program.upper()
        if reduction > 0:
            new_val = max(1, target_rating - reduction)        # icon attribute never below 1
            applied = target_rating - new_val
            enemy[attr] = new_val
            if attr == "masking":
                # Reveal lowers Masking, which lowers the enemy's Detection Factor -- recompute
                # it so a later locate / scan sees the weakened icon (nothing keeps a stale value).
                enemy_sleaze = int((enemy.get("utilities") or {}).get("sleaze", 0) or 0)
                enemy["detection_factor"] = eng.detection_factor(new_val, enemy_sleaze)
            floor_note = ", floored at 1" if new_val <= 1 else ""
            desc = (f"{label} -- you cripple {enemy['name']}'s {attr.title()} by {applied} "
                    f"(now {new_val}{floor_note}, until it logs off).")
        else:
            applied = 0
            new_val = target_rating
            desc = f"{label} -- {enemy['name']} resists your crippler; {attr.title()} holds."
        _append_event(state, {
            "type": "decker_crippled", "success": reduction > 0, "enemy_id": enemy["id"],
            "program": body.program, "attribute": attr, "reduction": applied,
            "enemy_attr_value": new_val, "decker_roll": cr["attack_roll"], "description": desc,
        })
        _spend_one_shot(state, decker, body.program)
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Black Hammer / Killjoy -- the PC's lethal offensive programs vs an enemy decker (vr2:
    # they "function like black IC but from a decker"). Black Hammer inflicts lethal PHYSICAL
    # biofeedback, Killjoy lethal STUN; for an NPC enemy (whose meat operator is not simulated)
    # the practical effect is identical -- a hard icon hit at a lethal base level (resisted with
    # the enemy's Bod) that, on an icon CRASH, burns the enemy's MPCP via a blaster-style test at
    # DOUBLE the program rating and takes the hostile decker out of the run. The damage kind is
    # carried in the event text only. The effective program rating is capped at ceil(Computer
    # skill / 2) -- the RAW maximum rating for these programs -- and a carried rating above the
    # cap is clamped (with a note). These target enemy DECKERS only -- never routed through IC.
    if body.program in ("black_hammer", "killjoy"):
        program = body.program
        label = "KILLJOY" if program == "killjoy" else "BLACK HAMMER"
        dmg_kind = "Stun" if program == "killjoy" else "Physical"
        computer = max(1, int(decker.get("computer_skill", 1) or 1))
        cap = (computer + 1) // 2                       # ceil(Computer / 2) = RAW max rating
        carried = int(util.get(program, 0) or 0) or body.attack_pool
        rating = max(1, min(carried, cap))              # clamp to the RAW rating cap
        clamped = carried > cap
        target_bod = max(1, int(enemy.get("bod", 1) or 1))
        # Mirror the PC->enemy plain-Attack to-hit TN (host code, target intruding); resolve the
        # icon damage via damage_resistance at a fixed lethal base (the enemy resists with Bod).
        attack_tn = max(2, rules.COMBAT_TN[sec_code]["intruding"])
        attack_roll = eng.roll_dice(pool, attack_tn)
        resist = eng.damage_resistance(
            bod=target_bod, power=rating, base_damage_level=_LETHAL_BASE_LEVEL,
            attacker_successes=attack_roll["successes"],
            # The enemy decker has no Shield modeled -> shield_successes stays 0.
        )
        boxes = resist["boxes"]
        ecm = enemy.setdefault("condition_monitor", {})
        ecm["persona_boxes"] = ecm.get("persona_boxes", 0) + boxes
        clamp_note = f" (rating clamped {carried}->{rating}, max = ceil(Computer/2))" if clamped else ""
        hit_desc = (
            f"{label} -- you drive lethal {dmg_kind} biofeedback into {enemy['name']}: "
            f"icon {resist['final_damage_level']} ({boxes} boxes). "
            f"Enemy persona {ecm['persona_boxes']}/10.{clamp_note}"
        )
        _append_event(state, {
            "type": "decker_lethal", "outcome": "hit", "success": boxes > 0,
            "enemy_id": enemy["id"], "program": program, "damage_kind": dmg_kind,
            "program_rating": rating, "boxes": boxes, "decker_roll": attack_roll,
            "description": hit_desc,
        })
        # Icon crash -> dump the enemy + lethal MPCP burn (blaster at DOUBLE the program rating).
        if ecm["persona_boxes"] >= 10:
            enemy["status"] = "crashed"
            mpcp_hit, mpcp_roll = _roll_enemy_mpcp_damage(enemy, rating, pool_multiplier=2)
            mpcp_note = (f" The lethal feedback fries its MPCP: -{mpcp_hit} permanent."
                         if mpcp_hit > 0 else " Its MPCP weathered the feedback.")
            crash_desc = (
                f"{label} CRASHES {enemy['name']}'s icon -- the hostile decker is dumped and "
                f"taken out of the run.{mpcp_note}"
            )
            _append_event(state, {
                "type": "decker_lethal", "outcome": "crash", "success": True,
                "enemy_id": enemy["id"], "program": program, "damage_kind": dmg_kind,
                "program_rating": rating, "mpcp_reduction": mpcp_hit, "mpcp_roll": mpcp_roll,
                "description": crash_desc,
            })
        _spend_one_shot(state, decker, body.program)
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Plain Attack (default) -- crash the enemy icon.
    atk = eng.cybercombat_attack(
        attacker_pool=pool, security_code=sec_code, target_status="intruding",
        target_bod=enemy["bod"], armor_rating=0,
        ic_rating=util.get("attack", 4), attacker_is_ic=False,
    )
    boxes = atk["resistance"]["boxes"]
    ecm = enemy.setdefault("condition_monitor", {})
    ecm["persona_boxes"] = ecm.get("persona_boxes", 0) + boxes
    desc = (f"You strike {enemy['name']} -- {atk['resistance']['final_damage_level']} "
            f"({boxes} boxes). Enemy persona {ecm['persona_boxes']}/10.")
    if ecm["persona_boxes"] >= 10:
        enemy["status"] = "crashed"
        desc += f" {enemy['name']}'s icon CRASHED -- dumped from the host."
    _append_event(state, {
        "type": "decker_attack", "success": True, "enemy_id": enemy["id"],
        "decker_roll": atk["attack_roll"], "description": desc,
    })
    _spend_one_shot(state, decker, body.program)
    run.state_json = state
    await db.commit(); await db.refresh(run)
    return _serialize_run(run, auth)


@router.post("/{run_id}/suppress", response_model=MatrixRunRead)
async def suppress_ic(
    run_id: int,
    body: RunSuppressInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Suppress or release a crashed IC (vr2 Suppression).

    Suppression is declared at the MOMENT the IC crashes: the decker absorbs 1 Detection Factor
    (applied live by _effective_detection_factor) to refund the tally that crashing it added.
    Releasing it is a Free Action that restores the DF and re-adds the IC's rating to the tally;
    a released IC stays crashed and can NEVER be re-suppressed. The DF cannot fall below 1.
    """
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state = copy.deepcopy(run.state_json)
    decker = run.decker_json
    ic = next((c for c in state.get("active_ic", [])
               if c.get("id") == body.ic_id), None)
    if ic is None:
        raise HTTPException(404, f"IC {body.ic_id} not found")

    rating = ic.get("rating", 0)
    if body.release:
        if not ic.get("suppressed"):
            raise HTTPException(400, "IC is not suppressed -- nothing to release")
        ic["suppressed"] = False
        ic["suppression_released"] = True   # one-way: cannot be suppressed again
        state["pass_free"] = max(0, state.get("pass_free", 0) - 1)  # vr2: releasing IC is a Free Action
        state["security_tally"] = state.get("security_tally", 0) + rating
        _append_event(state, {
            "type": "ic_released", "ic_id": ic["id"],
            "description": (
                f"Suppressed IC released -- Detection Factor restored; tally "
                f"+{rating} -> {state['security_tally']}."
            ),
        })
        _check_and_activate_sheaf(state, state["host_security_code"])
    else:
        # vr2: "must declare suppression immediately when crashing IC" -- only a freshly crashed,
        # never-released IC may be suppressed, and doing so refunds the tally the crash just added.
        if ic.get("status") != "crashed":
            raise HTTPException(400, "Only a crashed IC may be suppressed (declare it on the crash)")
        if ic.get("suppression_released"):
            raise HTTPException(400, "This IC was already released -- it can no longer be suppressed")
        if ic.get("suppressed"):
            raise HTTPException(400, "IC is already suppressed")
        ic["suppressed"] = True
        state["security_tally"] = max(0, state.get("security_tally", 0) - rating)  # refund crash tally
        df = _effective_detection_factor(state, decker)
        state["detection_factor"] = df
        _append_event(state, {
            "type": "ic_suppressed", "ic_id": ic["id"],
            "description": f"IC suppressed -- Detection Factor {df}; tally -{rating} (no crash increase).",
        })

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


@router.post("/{run_id}/jack-out", response_model=MatrixRunRead)
async def jack_out(
    run_id: int,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Emergency jack-out -- instant disconnect, always triggers dump shock."""
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state = copy.deepcopy(run.state_json)  # deepcopy, not dict(): keep nested JSON mutations un-aliased so the UPDATE fires
    decker = run.decker_json
    sec_code = state["host_security_code"]
    sec_value = state["host_security_value"]

    ds = _apply_dump_shock(state, decker, sec_code, sec_value)

    # vr2 L610-611: jacking out is a Free Action before a black IC hit (best-effort -- emergency
    # exit is never blocked by the budget). After a black IC hit it requires a Complex Willpower
    # test, modeled via the dump-shock resolution above.
    state["pass_free"] = max(0, state.get("pass_free", 0) - 1)
    state["run_ended"] = True
    state["end_reason"] = "jack_out"
    run.status = "escaped"

    _append_event(state, {
        "type": "jack_out",
        "description": (
            f"Emergency jack-out. Dump shock: {ds.get('final_level', 'None')} "
            f"({ds.get('boxes', 0)} boxes physical)."
        ),
        "dump_shock": ds,
    })

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)
