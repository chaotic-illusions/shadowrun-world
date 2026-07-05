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
    RunSuppressInput, RunRevealHostRatingsInput, RunEnemyAttackInput,
    RunAreaAttackInput,
    RunTrapDoorInput, SheaveSaveInput, SheafGenerateInput,
)
from app.services import matrix_engine as eng
from app.services import matrix_rules as rules

router = APIRouter()


# State keys removed entirely from state_json when serving a non-admin.
# (Admin sees the full state.) lurking_ic is GM-only: reactive IC "lurks
# silently" by the rules, so players must not see it exists at all.
_GM_ONLY_STATE_KEYS = {"sheaf", "host_acifs", "lurking_ic", "scrambles", "paydata", "data_bombs",
                       "trap_doors", "enemy_decker_cap"}

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


def _data_bomb_scope_name(target: str) -> tuple[str, str]:
    """Decode a data-bomb target key into (subsystem, bare name).

    The designer encodes bombs as "files::<name>" (a datafile) or "slave::<name>" (a device);
    a bare/legacy name is treated as a Files bomb. The subsystem is the bomb's CONTROLLING
    subsystem -- Files for a file bomb, Slave for a device bomb -- which fixes both the Defuse
    Computer Test TN (vr2 L463-471) and how the icon is labelled to the player. This is the
    authoritative bomb decoder (it special-cases the legacy "__slave__" token); use it -- not
    the generic _target_file_name -- wherever a bomb is matched or surfaced."""
    t = (target or "").strip()
    if t.startswith("files::"):
        return "files", t[len("files::"):]
    if t.startswith("slave::"):
        return "slave", t[len("slave::"):]
    if t == "__slave__":
        return "slave", "Slave device"
    return "files", t


def _scramble_subsystem(target_key: str) -> str:
    """Controlling subsystem ("access"/"slave"/"files") for a scramble target key.

    The designer keys a scramble as "<subsystem>::..." (e.g. "files::file::<name>",
    "slave::piece::<name>", "access::entire" -- see the designer's _encodeScrambleTargetKey).
    The subsystem it lives on is the first "::" segment; a bare/legacy key with no prefix is
    treated as a Files scramble. This drives BOTH discovery (an Analyze Subsystem on that
    subsystem reveals it) and how it is offered to the player for Decrypt File."""
    seg = (target_key or "").split("::", 1)[0].strip().lower()
    return seg if seg in {"access", "slave", "files"} else "files"


def _scramble_label(target_key: str) -> str:
    """Human-readable label for a scramble in the Decrypt File dropdown / discovery event."""
    tk = (target_key or "").strip()
    name = _target_file_name(tk)
    if tk.startswith("files::file::"):
        return f"File: {name}"
    if tk == "files::entire":
        return "Files subsystem (all files)"
    if tk.startswith("slave::piece::"):
        return f"Slave device: {name}"
    if tk == "slave::entire":
        return "Slave subsystem"
    if tk.startswith("access::piece::"):
        return f"Access: {name}"
    if tk == "access::entire":
        return "Access subsystem"
    return f"File: {tk}"


def _defuse_target_subsystem(state: dict, target_file: str) -> str | None:
    """Controlling subsystem ("files"/"slave") for a Defuse, taken from the matching armed bomb.

    vr2 L463-471: a data bomb is defused with a Computer Test vs its controlling subsystem -- the
    Files Rating for a datafile, the Slave Rating for a device. The bomb records which via its
    scope-encoded target, so the TN never depends on the client-sent subsystem. Matches the bomb
    exactly as ``_apply_defuse_bomb`` does (same decoder, same first-match order) so the derived
    rating lines up with the bomb the handler will disarm. Returns None when no armed, undefused
    bomb matches -- the caller then falls back to the requested subsystem."""
    armed = state.get("data_bombs") or []
    defused = set(state.get("defused_bombs") or [])
    tgt = (target_file or "").strip().lower()
    for b in armed:
        if not isinstance(b, dict) or b.get("target") in defused:
            continue
        scope, name = _data_bomb_scope_name(b.get("target", ""))
        if not tgt or name.strip().lower() == tgt:
            return scope
    return None


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
        # Surface only DISCOVERED data bombs (found via Analyze Icon on the protected file/device),
        # redacted to the protected target + which subsystem hosts it -- enough for the player to
        # target a Defuse, without leaking undiscovered bombs (the rest of data_bombs stays GM-only).
        discovered_data_bombs = []
        for b in (state.get("data_bombs") or []):
            if not isinstance(b, dict) or not b.get("discovered"):
                continue
            scope, name = _data_bomb_scope_name(b.get("target", ""))
            discovered_data_bombs.append({"target": name, "scope": scope, "name": name})
        # Surface only DISCOVERED scrambles (found via Analyze Subsystem on the Files/Slave
        # subsystem that holds them). Redacted to target_key + subsystem + a human label -- enough
        # to offer Decrypt File against the RIGHT scramble -- WITHOUT leaking its rating or variant
        # (Poison/Exploding stay GM-only; scrambles is popped below with the other GM-only keys).
        discovered_scrambles = [
            {"target_key": s.get("target_key", ""),
             "subsystem": _scramble_subsystem(s.get("target_key", "")),
             "label": _scramble_label(s.get("target_key", ""))}
            for s in (state.get("scrambles") or [])
            if isinstance(s, dict) and s.get("discovered")
        ]
        for k in _GM_ONLY_STATE_KEYS:
            state.pop(k, None)
        state["located_paydata"] = located_paydata
        state["discovered_trap_doors"] = discovered_trap_doors
        state["discovered_data_bombs"] = discovered_data_bombs
        state["discovered_scrambles"] = discovered_scrambles
        # Slave device icons are perceptible only once the decker is INSIDE the host; before logon
        # the run reveals nothing about the interior, so keep the scan-target list empty until then.
        if not state.get("logon_complete"):
            state["slave_devices"] = []
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
        # Combat maneuver: the PC evaded this enemy (it lost the trail and won't attack until it
        # re-detects). An enemy that HID from the PC (hid_from_pc) is un-revealed and never reaches
        # here. Raw redetect internals stay GM-only (whitelist above omits them).
        "lost_track": bool(e.get("evaded") and e.get("evade_dir") == "lost_pc"),
        "condition_monitor": {
            "persona_boxes": cm.get("persona_boxes", 0),
            "stun_boxes": cm.get("stun_boxes", 0),
            "physical_boxes": cm.get("physical_boxes", 0),
        },
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
    # Combat maneuver: an IC that successfully Evaded the PC (hid_from_pc) vanishes from the
    # decker's view until it is re-detected (Analyze Icon / timer). A PC-evaded IC (lost_pc)
    # stays visible but is flagged so the UI can show it has lost the trail.
    if ic.get("evaded") and ic.get("evade_dir") == "hid_from_pc":
        return None
    out = dict(ic)
    # Keep the ``evaded`` badge (lost_pc) for the UI but strip the GM-only maneuver internals.
    for k in ("redetect_turn", "redetect_tally_base", "evade_dir", "position_bonus", "parry_tn_bonus"):
        out.pop(k, None)
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
    "relocate": "Simple", "redirect_datatrail": "Complex",
    "analyze_subsystem": "Simple", "analyze_icon": "Free", "logon_to_ltg": "Complex",
    "attack": "Simple",                       # vr2: all cybercombat attacks are Simple Actions
    "medic": "Complex", "restore": "Complex", "disinfect": "Complex",
    "defuse_data_bomb": "Complex",
    "steamroller": "Complex", "slow": "Complex", "decompress_file": "Complex",
    "dinab": "Free",                          # DINAB: a Free action runs one program autonomously
    # Combat maneuvers (vr2 L1982) are Simple Actions.
    "evade_detection": "Simple", "parry_attack": "Simple", "position_attack": "Simple",
})

# Operation -> the utility program it runs (from the vr2 System Operations table). Used to auto-fire
# a lurking Tar Baby / Tar Pit against whatever utility the decker just ran (app-as-GM; there is no
# human GM to pick the target program). Same snake_case keying as _ACTION_COST.
_ACTION_UTILITY = {op["name"].lower().replace(" ", "_"): op["utility"] for op in rules.SYSTEM_OPERATIONS}

# Balanced enemy-decker AI (wounded behaviour, spec section 3.2). Replaces the old hard 7-box
# flee with a graduated model: an escalating nerve check at 7/8/9 persona boxes (10 = dumped),
# softened by the decker's per-instance bravery, plus a hide-heal-return loop for Medic-carriers.
_ENEMY_WOUNDED_BOXES = 5    # Medic-carrier breaks contact (Evade Detection) to heal at/above this
_ENEMY_REENGAGE_BOXES = 3   # ... and voluntarily re-engages once healed back down to at/below this
# Base flee chance (before bravery) the FIRST time a wound reaches each persona-box threshold; the
# decker jacks out on a failed nerve. 10 boxes is a forced dump (handled separately, not a check).
_ENEMY_NERVE_FLEE = {7: 0.30, 8: 0.55, 9: 0.80}


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
    # Roll this run's TOTAL enemy-decker cap ONCE (stable for the whole run). The count-gated
    # probabilistic spawner (vr2 #5) dispatches at most this many security deckers across the run.
    _sec_code = cfg.get("security_code", "Green")
    _spawn_cfg = eng._ENEMY_DECKER_SPAWN.get(_sec_code, eng._ENEMY_DECKER_SPAWN["Green"])
    enemy_decker_cap = random.randint(*_spawn_cfg["cap"])

    return {
        "security_tally": 0,
        "alert_status": "none",
        "decker_initiative": decker_initiative,   # Matrix initiative this Combat Turn
        "initiative_passes": initiative_passes,    # action passes (increments of 10)
        "current_pass": 1,
        "actions_this_turn": 0,
        # Combat maneuvers (vr2 L1982): with this flag set the app-as-GM lets IC and enemy
        # deckers INITIATE maneuvers (Evade/Parry/Position) via heuristics, not just oppose the
        # PC's. Fresh runs opt in; legacy/test states built without it get no NPC maneuvers.
        "npc_combat_maneuvers": True,
        "pass_action_points": 2,   # per-pass: 2 Simple OR 1 Complex
        "pass_free": 1,            # per-pass: 1 Free action
        "condition_monitor": {
            "persona_boxes": 0,
            "stun_boxes": 0,
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
        # Named Slave devices (cameras, locks, sensors). Each is an Analyze Icon scan target, so a
        # data bomb on a SPECIFIC device can be found and defused by name rather than lumped into a
        # single generic "Slave device". Perceptible only once inside the host -- _serialize_run
        # blanks this list for players until logon (interior iconography, like located paydata).
        "slave_devices": [str(x) for x in (cfg.get("slave_pieces") or []) if str(x).strip()],
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
        # Deck storage ledger for downloaded paydata (vr2 Mp). storage_free_mp < 0 = untracked/
        # unlimited; >= 0 = real free capacity at jack-in (downloads consume it).
        "storage_free_mp": decker.get("storage_free_mp", -1),
        "storage_used_mp": 0,
        "downloaded_files": [],   # [{name, size_mp, is_key, turn}] -- player-visible ledger
        # Multi-turn Download Data in progress (vr2 ongoing op). None = no transfer. While set, the
        # deck auto-rolls a Null Operation each turn and the decker may take only Free actions;
        # {file, stored_mp, full_mp, compressed, is_key, turns_total, turns_left, started_turn}.
        "active_download": None,
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
        "enemy_decker_cap": enemy_decker_cap,   # per-run TOTAL cap for the probabilistic spawner
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
        ov = _add_stun(state["condition_monitor"], ds["boxes"])
        ds["stun_overflow"] = ov["overflow"]
        ds["unconscious"] = ov["unconscious"]
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
        # vr2 #5: after EACH activated step the host may dispatch a security decker (the sole,
        # count-gated probabilistic spawner). Rolled once per step so deckers arrive paced.
        _maybe_spawn_enemy_decker(state, security_code)


def _spawn_enemy_decker(state: dict, security_code: str, *, name: str | None = None) -> dict:
    """Build a fully-programmatic security decker, roll its initiative, add it to the run HIDDEN
    (GM-only ``enemy_decker_injected``), and return it. The sole enemy-decker spawner -- every
    decker is generated from ratings + dice (there is no hand-authored path). It becomes visible
    only via its own hunt reveal or the PC's Locate Decker."""
    enemy = eng.generate_enemy_decker(security_code, state.get("host_security_value", 6), name=name)
    enemy["id"] = f"ed_{uuid.uuid4().hex[:8]}"
    enemy["initiative"], enemy["initiative_passes"] = _roll_decker_initiative(enemy)  # rolled once on entry
    state.setdefault("enemy_deckers", []).append(enemy)
    _append_event(state, {
        "type": "enemy_decker_injected", "gm_only": True, "enemy_id": enemy["id"],
        "description": (
            f"GM: {enemy['name']} (Computer {enemy['computer_skill']}, "
            f"Attack-{enemy['utilities']['attack']}) dispatched to hunt the intruder."
        ),
    })
    return enemy


def _maybe_spawn_enemy_decker(state: dict, security_code: str) -> None:
    """Count-gated probabilistic dispatch (vr2 #5): after a sheaf step fires, roll the tier chance
    to send ONE security decker, capped by the per-run ``enemy_decker_cap`` (the TOTAL from all
    sources). Skips when the run has ended (e.g. a shutdown step) or the cap is already reached."""
    if state.get("run_ended"):
        return
    spawn_cfg = eng._ENEMY_DECKER_SPAWN.get(security_code)
    if not spawn_cfg:
        return
    cap = state.get("enemy_decker_cap")
    if cap is None:
        # Legacy run started before the cap was tracked -- roll it once now and store it.
        cap = random.randint(*spawn_cfg["cap"])
        state["enemy_decker_cap"] = cap
    if len(state.get("enemy_deckers", [])) >= cap:
        return
    if random.random() < spawn_cfg["chance"]:
        _spawn_enemy_decker(state, security_code)


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


def _enemy_effective_shield(enemy: dict) -> int:
    """Effective Shield rating for an ENEMY decker = its loaded Shield utility minus its OWN accrued
    wear (``enemy['program_damage']['shield']``). Mirrors _effective_shield, but the wear lives on
    the enemy dict (each security decker tracks its own program damage) rather than the PC's state
    slot. ``<= 0`` means the enemy carries no Shield, or has worn it out parrying, and cannot parry."""
    base = (enemy.get("utilities") or {}).get("shield", 0) or 0
    worn = (enemy.get("program_damage") or {}).get("shield", 0)
    return max(0, base - worn)


def _enemy_shield_parry(state: dict, enemy: dict, *, attacker_skill: int, context: str) -> int:
    """Make ONE defensive Shield Test for an ENEMY decker against the PC's Strike Back (vr2).

    Mirror of _shield_parry: rolls the enemy's effective Shield vs the PC's Computer skill, wears the
    enemy's own Shield by 1 Rating Point (win or lose), emits a GM-only ``enemy_shield_parry`` event
    (the PC never sees the defender's exact program), and returns the net successes for the caller to
    SUBTRACT from the PC's attack successes (damage) or ADD to the enemy's side of a crippler test.
    Returns 0 -- no test, no wear, no event -- when the enemy carries no Shield or it is worn to 0."""
    rating = _enemy_effective_shield(enemy)
    if rating <= 0:
        return 0
    res = eng.shield_parry(shield_rating=rating, attacker_skill=attacker_skill)
    succ = res["successes"]
    pd = enemy.setdefault("program_damage", {})
    pd["shield"] = pd.get("shield", 0) + 1  # -1 Rating Point per use, win or lose (reloadable by the app)
    remaining = max(0, rating - 1)
    _append_event(state, {
        "type": "enemy_shield_parry", "gm_only": True,
        "enemy_id": enemy.get("id"), "context": context,
        "shield_rating": rating, "shield_remaining": remaining,
        "successes": succ, "roll": res["roll"],
        "description": (
            f"GM: {enemy.get('name', 'Security decker')} Shield-{rating} parries the {context} hit -- "
            f"{succ} success{'' if succ == 1 else 'es'} (TN {res['tn']}), worn to {remaining}."
        ),
    })
    return succ


def _effective_medic(decker: dict, state: dict) -> int:
    """Effective Medic rating = the loaded Medic utility minus its accrued per-use wear.

    Wear lives in ``state['program_damage']['medic']`` -- the SAME slot Swap Memory resets -- so
    a freshly swapped/reloaded Medic returns to full (mirrors _effective_shield). ``<= 0`` means
    the Medic is unloaded or worn out and can no longer heal the icon."""
    base = (decker.get("utilities") or {}).get("medic", 0) or 0
    worn = (state.get("program_damage") or {}).get("medic", 0)
    return max(0, base - worn)


def _add_stun(cm: dict, boxes: int) -> dict:
    """Add Stun boxes to a condition monitor's Physical Stun track (``stun_boxes``). SR2 Stun
    OVERFLOWS into Physical Damage: the Stun track caps at 10 and any excess spills 1-for-1 into
    ``physical_boxes``. Returns {stun, overflow, unconscious}; ``unconscious`` (Stun filled to 10)
    means the icon's owner blacks out -- the caller ends the run (dumped)."""
    cur = int(cm.get("stun_boxes", 0) or 0)
    total = cur + max(0, int(boxes or 0))
    overflow = max(0, total - 10)
    cm["stun_boxes"] = min(10, total)
    if overflow:
        cm["physical_boxes"] = int(cm.get("physical_boxes", 0) or 0) + overflow
    return {"stun": cm["stun_boxes"], "overflow": overflow, "unconscious": cm["stun_boxes"] >= 10}


def _wound_mod_from_boxes(boxes: int) -> int:
    """Wound-level TN / initiative modifier from the filled boxes on ONE Condition Monitor track
    (SR2 floors): 1-2 boxes = Light (+1), 3-5 = Moderate (+2), 6-9 = Serious (+3), 10 = Deadly
    (crash/out). Undamaged = 0. Same floors as the ``DAMAGE_BOXES`` wound thresholds."""
    b = int(boxes or 0)
    if b >= rules.DAMAGE_BOXES["Serious"]:    # >= 6
        return 3
    if b >= rules.DAMAGE_BOXES["Moderate"]:   # >= 3
        return 2
    if b >= rules.DAMAGE_BOXES["Light"]:      # >= 1
        return 1
    return 0


def _cm_wound_mod(cm: dict) -> int:
    """Total wound modifier for an icon with three Condition Monitors (persona + physical stun +
    physical damage), summed -- the wounds are CUMULATIVE (a Light persona + a Moderate physical =
    +3 TN / -3 initiative)."""
    cm = cm or {}
    return (_wound_mod_from_boxes(cm.get("persona_boxes", 0))
            + _wound_mod_from_boxes(cm.get("stun_boxes", 0))
            + _wound_mod_from_boxes(cm.get("physical_boxes", 0)))


def _decker_wound_mod(state: dict) -> int:
    """PLAYER decker's cumulative wound modifier (persona + stun + physical)."""
    return _cm_wound_mod(state.get("condition_monitor") or {})


def _enemy_wound_mod(enemy: dict) -> int:
    """Enemy decker's cumulative wound modifier (persona + stun + physical)."""
    return _cm_wound_mod(enemy.get("condition_monitor") or {})


def _enemy_armor(enemy: dict) -> int:
    """Enemy decker's Armor utility rating (reduces the Power of incoming persona damage). Enemy
    deckers are modeled EXACTLY like the PC decker: they resist icon/persona hits with Bod dice
    and the Armor utility -- if loaded -- lowers the attack Power (see the PC path in
    ``_detonate_data_bomb`` / Black IC resistance). Most auto-generated enemies carry no Armor,
    so this is 0 unless one is explicitly loaded."""
    return int((enemy.get("utilities") or {}).get("armor", 0) or 0)


def _ic_wound_mod(ic: dict) -> int:
    """IC has a single Condition Monitor track (``boxes``)."""
    return _wound_mod_from_boxes(ic.get("boxes", 0))


def _ic_passes(ic: dict) -> int:
    """Action passes for an IC this turn, reduced by its wound penalty (-1 initiative per wound
    level). Initiative is rolled once per encounter, so the wound penalty is re-derived here every
    time the passes are needed."""
    return _init_passes(ic.get("initiative", 0) - _ic_wound_mod(ic))


def _enemy_passes(enemy: dict) -> int:
    """Action passes for an enemy decker this turn, reduced by its cumulative wound penalty
    (-1 initiative per wound level, summed across its three Condition Monitors). Initiative is
    rolled once per encounter, so the wound penalty is re-derived here every time it is needed."""
    return _init_passes(enemy.get("initiative", 0) - _enemy_wound_mod(enemy))


def _current_icon_wound_level(state: dict) -> str | None:
    """Worst current wound level of the decker's persona icon, derived from the filled Condition
    Monitor boxes via the vr2 Condition Monitor Table floors (Light >= 1, Moderate >= 3,
    Serious >= 6 boxes). Returns ``None`` when the icon is undamaged. Everything at or above the
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


def _enemy_carries_medic(enemy: dict) -> bool:
    """True if this enemy decker has a Medic utility loaded (Red/Black tiers) -- the gate for the
    wounded-AI hide-heal-return loop. A healless decker (Blue/Green/Orange) never disengages to heal."""
    return int((enemy.get("utilities") or {}).get("medic", 0) or 0) > 0


def _enemy_effective_medic(enemy: dict) -> int:
    """Effective Medic rating for an ENEMY decker = its loaded Medic utility minus its OWN per-use
    wear (``enemy['program_damage']['medic']``). Mirrors _effective_medic, but the wear lives on the
    enemy dict rather than the PC's state slot."""
    base = (enemy.get("utilities") or {}).get("medic", 0) or 0
    worn = (enemy.get("program_damage") or {}).get("medic", 0)
    return max(0, base - worn)


def _enemy_medic_heal(state: dict, enemy: dict) -> None:
    """Enemy-decker self-heal -- mirror of _apply_medic on the enemy's OWN condition monitor.

    Heals persona/icon boxes equal to the Medic Test successes (TN by the icon's CURRENT wound
    level, capped by the current damage) and degrades the enemy's Medic 1 Rating Point per use.
    Emits a GM-only ``enemy_decker``/``medic`` event. No-op when the icon is undamaged or the Medic
    is worn out / not loaded (mirrors _apply_medic, which does not wear a 0-rating Medic)."""
    ecm = enemy.setdefault("condition_monitor", {})
    boxes = int(ecm.get("persona_boxes", 0) or 0)
    if boxes <= 0:
        return
    rating = _enemy_effective_medic(enemy)
    if rating <= 0:
        return
    if boxes >= rules.DAMAGE_BOXES["Serious"]:
        wound = "Serious"
    elif boxes >= rules.DAMAGE_BOXES["Moderate"]:
        wound = "Moderate"
    else:
        wound = "Light"
    res = eng.medic_heal(medic_rating=rating, wound_level=wound)
    healed = min(boxes, res["boxes_healed"])
    ecm["persona_boxes"] = max(0, boxes - healed)
    pd = enemy.setdefault("program_damage", {})
    pd["medic"] = pd.get("medic", 0) + 1   # -1 Rating Point per use, win or lose
    _append_event(state, {
        "type": "enemy_decker", "outcome": "medic", "enemy_id": enemy.get("id"),
        "gm_only": True, "medic_rating": rating, "healed": healed,
        "persona_boxes": ecm["persona_boxes"],
        "description": (
            f"GM: {enemy.get('name', 'Security decker')} Medic-{rating} treats its {wound.lower()} "
            f"icon wound (TN {res['tn']}): {healed} box{'' if healed == 1 else 'es'} healed -- "
            f"now {ecm['persona_boxes']}/10."
        ),
    })


def _enemy_nerve_check(state: dict, enemy: dict, boxes: int) -> bool:
    """Escalating nerve check (spec section 3.2): the FIRST time a wound reaches 7/8/9 persona
    boxes, roll ONCE at that threshold to see if the decker's nerve breaks and it jacks out.

    Checked once per newly-reached threshold (tracked in ``enemy['nerve_checks_done']``) so a
    decker sitting at 7 boxes isn't re-rolled every turn. A single hit that jumps several
    thresholds resolves them in ascending order; the decker flees on the first failure. Bravery
    lowers the flee chance: ``flee_chance = clamp(base - 0.15 * bravery, 0.05, 0.95)``. Sets
    ``status = "fled"`` and logs on a break. Returns True if the decker fled."""
    done = enemy.setdefault("nerve_checks_done", [])
    bravery = int(enemy.get("bravery", 0) or 0)
    for threshold in (7, 8, 9):
        if boxes >= threshold and threshold not in done:
            done.append(threshold)
            flee_chance = min(0.95, max(0.05, _ENEMY_NERVE_FLEE[threshold] - 0.15 * bravery))
            if random.random() < flee_chance:
                enemy["status"] = "fled"
                _append_event(state, {
                    "type": "enemy_decker", "outcome": "fled", "enemy_id": enemy.get("id"),
                    "description": (
                        f"{enemy.get('name', 'The security decker')} is wounded ({boxes}/10) and "
                        f"its nerve breaks -- it jacks out, abandoning the hunt."
                    ),
                })
                return True
    return False


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
    ic_passes = _ic_passes(target)
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


def _toggle_ic_suppression(state: dict, decker: dict, *, ic_id: str, release: bool) -> dict:
    """Suppress or release a crashed OR hung IC (vr2_rules.md Suppression L418-424 + Slow L1578).

    Mutates ``state`` in place; raises HTTPException on an invalid request; returns the ic dict.

    Suppression is declared the moment an IC is neutralized -- either it CRASHED (crashing added its
    rating to the security tally) or it HANGS from a Slow strike (its passes drained to 0 for the
    turn; Slow adds NO tally). The decker absorbs 1 Detection Factor per suppressed IC (applied live
    by ``_effective_detection_factor``): for a crashed IC this defers the crash tally, for a hung IC
    there is nothing to defer. Releasing a suppressed IC is a Free Action that restores the DF; a
    crashed IC re-adds its rating to the tally (the deferred crash increase), a hung IC re-adds
    nothing (the "appropriate amount" for a hang is 0). A released IC can NEVER be re-suppressed; the
    DF cannot fall below 1 (enforced by ``_effective_detection_factor``).
    """
    ic = next((c for c in state.get("active_ic", [])
               if c.get("id") == ic_id), None)
    if ic is None:
        raise HTTPException(404, f"IC {ic_id} not found")

    rating = ic.get("rating", 0)
    crashed = ic.get("status") == "crashed"
    if release:
        if not ic.get("suppressed"):
            raise HTTPException(400, "IC is not suppressed -- nothing to release")
        ic["suppressed"] = False
        ic["suppression_released"] = True   # one-way: cannot be suppressed again
        state["pass_free"] = max(0, state.get("pass_free", 0) - 1)  # vr2: releasing IC is a Free Action
        if crashed:
            # A crashed IC's suppression deferred the crash tally -- releasing re-adds it.
            state["security_tally"] = state.get("security_tally", 0) + rating
            tally_note = f"tally +{rating} -> {state['security_tally']}"
        else:
            # A hung IC (Slow) never added tally, so the "appropriate amount" to re-add is 0.
            tally_note = "no tally change (a hung IC added none)"
        _append_event(state, {
            "type": "ic_released", "ic_id": ic["id"],
            "description": f"Suppressed IC released -- Detection Factor restored; {tally_note}.",
        })
        _check_and_activate_sheaf(state, state["host_security_code"])
    else:
        # vr2: suppression must be declared the moment the IC is neutralized -- either a fresh crash
        # (crashing added tally; suppressing refunds it) or a Slow HANG (L1578; adds no tally).
        hung = ic.get("status") == "active" and ic.get("hung_turn") is not None
        if not (crashed or hung):
            raise HTTPException(
                400, "Only a crashed or hung IC may be suppressed (declare it on the crash/hang)")
        if ic.get("suppression_released"):
            raise HTTPException(400, "This IC was already released -- it can no longer be suppressed")
        if ic.get("suppressed"):
            raise HTTPException(400, "IC is already suppressed")
        ic["suppressed"] = True
        if crashed:
            state["security_tally"] = max(0, state.get("security_tally", 0) - rating)  # refund crash tally
            tally_note = f"tally -{rating} (no crash increase)"
        else:
            # A hung IC added no tally, so there is nothing to refund.
            tally_note = "no tally change (Slow added none)"
        df = _effective_detection_factor(state, decker)
        state["detection_factor"] = df
        _append_event(state, {
            "type": "ic_suppressed", "ic_id": ic["id"],
            "description": f"IC suppressed -- Detection Factor {df}; {tally_note}.",
        })
    return ic


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
                                       armor_rating=_enemy_armor(enemy),
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
                                 target_bod=enemy["bod"], armor_rating=_enemy_armor(enemy),
                                 ic_rating=int(util_r.get("attack", 4) or 4),
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


def _download_turns(decker: dict, stored_mp: int) -> int:
    """Combat Turns to transfer a file whose on-deck footprint is ``stored_mp`` at the deck's I/O
    Speed (vr2_rules.md L1256-1261: I/O Speed is the transfer rate; this app stores it as Mp per
    Combat Turn). ``turns = ceil(stored_mp / io_speed)``. ``stored_mp`` is the SAME
    compressor-effective size the file occupies on the deck, so a Compressor that can handle the
    file halves what must be transferred (an oversized file transfers full). A legacy deck with no
    io_speed (<=0) transfers instantly (1 turn)."""
    io = int(decker.get("io_speed", 0) or 0)
    if io <= 0 or stored_mp <= 0:
        return 1
    return -(-stored_mp // io)  # ceil


def _complete_download(state: dict, decker: dict, pd: dict) -> None:
    """Land a fully-transferred paydata file on the deck: mark it downloaded, charge its
    compressor-effective footprint to deck storage, record the player-visible ledger entry, and
    emit a ``data_downloaded`` event. Shared by the single-turn Download Data action and the final
    tick of a multi-turn background transfer so both charge storage identically. Compressed files
    stay compressed on the deck (must be decompressed before use)."""
    if pd.get("downloaded"):
        return
    pd["downloaded"] = True
    pd["located"] = True
    density = max(0, int(pd.get("density", 0) or 0))
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


def _auto_null_operation(state: dict, decker: dict) -> dict:
    """Roll one automatic Null Operation while a background Download runs (vr2: Download Data is an
    ongoing operation, L1873; Null Operation is 'performed while waiting', L1892). A Control System
    Test at the decker's Computer skill (NO Hacking Pool -- the decker isn't actively rolling); the
    host's opposed Security Test adds to the tally exactly like a manual op. Returns the test."""
    pool = int(decker.get("computer_skill", 4) or 0)
    test = eng.system_test(
        decker_pool=pool,
        subsystem_rating=_subsystem_rating(state, "control"),
        security_value=state.get("host_security_value", 6),
        det_factor=_effective_detection_factor(state, decker),
    )
    state["security_tally"] = state.get("security_tally", 0) + test["tally_increase"]
    return test


def _corrupt_active_download(state: dict) -> None:
    """Terminating a transfer early yields a corrupted, worthless copy (vr2 Download Data, L1873; a
    Paydata Point needs the COMPLETE file, L992). Discard the in-progress download with NO storage
    charged and NO paydata credited, and tell the player."""
    dl = state.get("active_download")
    if not dl:
        return
    state["active_download"] = None
    _append_event(state, {
        "type": "download_corrupted",
        "file_name": dl.get("file"),
        "description": (
            f"Transfer of \"{dl.get('file')}\" interrupted before completion -- the partial copy "
            "is corrupted and worthless. No data recovered."
        ),
    })


def _tick_active_download(state: dict, decker: dict, dl: dict) -> None:
    """Advance a multi-turn background Download by one Combat Turn: roll the automatic Null
    Operation (adds tally, may wake the sheaf), decrement the turns remaining, and land the file
    when the transfer finishes. If the source file was destroyed mid-transfer, the partial copy is
    corrupted (a Paydata Point needs the COMPLETE file)."""
    test = _auto_null_operation(state, decker)
    dl["turns_left"] = int(dl.get("turns_left", 0)) - 1
    left = max(0, dl["turns_left"])
    _append_event(state, {
        "type": "null_operation",
        "success": test["success"],
        "decker_roll": test["decker_roll"],
        "host_roll": test["host_roll"],
        "tally_increase": test["tally_increase"],
        "tally_total": state.get("security_tally", 0),
        "file_name": dl.get("file"),
        "turns_left": left,
        "description": (
            f"Auto Null Operation covers the ongoing download of \"{dl.get('file')}\" "
            f"({'SUCCESS' if test['success'] else 'FAILED'}). "
            + (f"{left} turn(s) of transfer remaining." if left > 0 else "Transfer complete.")
        ),
    })
    _check_and_activate_sheaf(state, state.get("host_security_code", "Green"))
    if dl["turns_left"] > 0:
        return
    pd = next((p for p in (state.get("paydata") or [])
               if str(p.get("name", "")).strip().lower() == str(dl.get("file", "")).strip().lower()
               and not p.get("destroyed")), None)
    if pd is not None:
        _complete_download(state, decker, pd)
        state["active_download"] = None
    else:
        _corrupt_active_download(state)  # source file gone before the transfer finished


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


def _apply_analyze_host(state: dict, net_successes: int) -> dict:
    """Analyze Host success handler (vr2 System Operations: Control test, Analyze utility).

    Reveals the host's ACIFS subsystem ratings (Access, Control, Index, Files, Slave). The raw
    ratings live in GM-only ``host_acifs``; revealed values mirror into the player-visible
    ``host_ratings_revealed`` map in ACIFS order. USER OVERRIDE of RAW: the revealable set is
    exactly the 5 ACIFS ratings (the host Security Rating is already known; VM status is not
    modeled), and the "reveal all" threshold is 5+ net successes (not RAW's 7+).

    Let ``net`` = net successes and ``U`` = number of still-hidden ratings. On a successful test:
      * ``net >= 5`` OR ``net >= U`` -> auto-reveal ALL still-hidden ratings now (no choice to make)
        and clear any banked pending.
      * ``1 <= net < U`` -> a genuine choice exists: BANK ``host_analyze_pending`` = {credits, turn}
        and reveal nothing yet (the decker then picks which to reveal via _reveal_host_ratings).
        A later banking roll REPLACES the previous pending credits.
      * no still-hidden ratings at all -> nothing to reveal; clear any pending.

    Mutates ``state`` and appends a ``host_analyzed`` event. Returns a small summary
    ``{"revealed": [{"subsystem": nm, "rating": rt}, ...], "pending": <credits or 0>}``.
    """
    acifs = state.get("host_acifs") or [10, 10, 10, 10, 10]
    names = ["access", "control", "index", "files", "slave"]
    revealed = state.setdefault("host_ratings_revealed", {})
    hidden = [nm for nm in names if nm not in revealed]
    net = max(0, int(net_successes))

    if not hidden:
        state.pop("host_analyze_pending", None)
        _append_event(state, {
            "type": "host_analyzed", "revealed": [],
            "description": "Analyze Host -- all subsystem ratings already known.",
        })
        return {"revealed": [], "pending": 0}

    # Reveal-all: 5+ net successes, or enough successes to cover every still-hidden rating anyway.
    if net >= 5 or net >= len(hidden):
        newly: list[dict] = []
        for i, nm in enumerate(names):
            if nm in hidden:
                revealed[nm] = int(acifs[i]) if i < len(acifs) else 10
                newly.append({"subsystem": nm, "rating": revealed[nm]})
        state.pop("host_analyze_pending", None)
        _append_event(state, {
            "type": "host_analyzed",
            "revealed": newly,
            "description": "Analyze Host -- " + ", ".join(
                f"{d['subsystem'].capitalize()} {d['rating']}" for d in newly
            ) + " revealed.",
        })
        return {"revealed": newly, "pending": 0}

    # Otherwise a genuine choice exists (1 <= net < hidden count): bank the credits and let the
    # decker choose which hidden ratings to reveal via /reveal-host-ratings (reveal NOTHING yet).
    credits = max(1, net)
    state["host_analyze_pending"] = {
        "credits": credits,
        "turn": state.get("current_turn", 1),
    }
    reveals = min(credits, len(hidden))
    _append_event(state, {
        "type": "host_analyzed", "revealed": [],
        "description": f"Analyze Host succeeded -- choose {reveals} subsystem rating(s) to reveal.",
    })
    return {"revealed": [], "pending": credits}


def _reveal_host_ratings(state: dict, subsystems: list[str]) -> list[tuple[str, int]]:
    """Phase two of Analyze Host (vr2 override): spend banked Analyze Host credits by choosing which
    still-hidden ACIFS ratings to reveal. Reads ``host_analyze_pending`` (banked by
    ``_apply_analyze_host`` when the decker rolled fewer net successes than there were hidden
    ratings); reveals the chosen ratings from GM-only ``host_acifs`` into the player-visible
    ``host_ratings_revealed`` map; clears the pending; appends a ``host_analyzed`` event.

    Validates the picks: each must be a real ACIFS name, currently hidden, and non-duplicate; the
    number picked must equal ``min(credits, hidden count)``. Raises HTTPException(400) otherwise.
    Returns the list of revealed ``(name, rating)`` tuples."""
    pending = state.get("host_analyze_pending") or {}
    credits = int(pending.get("credits", 0) or 0)
    if credits <= 0:
        raise HTTPException(400, "No pending Analyze Host reveals -- run Analyze Host first.")

    names = ["access", "control", "index", "files", "slave"]
    acifs = state.get("host_acifs") or [10, 10, 10, 10, 10]
    revealed = state.setdefault("host_ratings_revealed", {})
    hidden = [nm for nm in names if nm not in revealed]

    picks: list[str] = []
    seen: set[str] = set()
    for raw in (subsystems or []):
        nm = str(raw).strip().lower()
        if nm not in names:
            raise HTTPException(400, f"Unknown subsystem: {raw!r}.")
        if nm in revealed:
            raise HTTPException(400, f"Subsystem '{nm}' is already revealed.")
        if nm in seen:
            raise HTTPException(400, f"Duplicate subsystem: '{nm}'.")
        seen.add(nm)
        picks.append(nm)

    need = min(credits, len(hidden))
    if len(picks) != need:
        raise HTTPException(400, f"Choose exactly {need} subsystem rating(s) to reveal.")

    result: list[tuple[str, int]] = []
    for nm in picks:
        i = names.index(nm)
        rt = int(acifs[i]) if i < len(acifs) else 10
        revealed[nm] = rt
        result.append((nm, rt))

    state.pop("host_analyze_pending", None)
    _append_event(state, {
        "type": "host_analyzed",
        "revealed": [{"subsystem": nm, "rating": rt} for nm, rt in result],
        "description": "Analyze Host -- " + ", ".join(
            f"{nm.capitalize()} {rt}" for nm, rt in result
        ) + " revealed.",
    })
    return result


def _decoy_intercept(state: dict, ic: dict, *, sec_code: str, sec_value: int,
                     ic_target_status: str) -> bool:
    """Decoy redirect check for a single proactive IC attack (vr2_rules.md L1871).

    A live decoy (Control Test successes recorded, its 10-box Condition Monitor not yet full)
    draws a proactive IC's attack on a 1D6 <= successes -- ties go to the decoy, so the check is
    ``<=`` not ``<``. The decoy has NO defences: it eats the IC's fully staged-up damage with no
    resistance roll, accruing boxes on its own Condition Monitor, and is removed once the CM fills
    (10 boxes). Trace IC never reach this check (the caller skips it before calling), so decoys are
    correctly NOT effective against trace IC. Returns True when the IC's action was consumed on the
    decoy (the caller should stop resolving this IC's attack for the turn)."""
    decoy_succ = state.get("decoy_successes", 0)
    if decoy_succ <= 0 or state.get("decoy_hp", 0) >= 10:
        return False
    d6 = random.randint(1, 6)
    if d6 > decoy_succ:
        return False
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
    return True


def _apply_analyze_icon(state: dict, *, target_file: str) -> None:
    """Analyze Icon success handler (vr2 System Operations: Control test, Analyze utility, Free): a
    targeted scan of ONE icon -- a located file (Files node) or the host's Slave device (Slave
    node). vr2 L463: "Detecting [a data bomb]: Analyze Icon operation on the protected file or
    device." A success reveals an undefused data bomb on the scanned icon so the decker can Defuse
    it BEFORE an access trips it. This is the ONLY discovery path -- a broad Analyze Subsystem no
    longer surfaces bombs (too cheap for the whole node).

    The target is scope-encoded ("files::<name>" / "slave::<device>"): a file scan is icon-specific
    (the named file must match) and a NAMED slave device scans only that device, so multiple bombed
    devices are told apart. A GENERIC slave scan ("slave::__device__" / legacy "__slave__", used
    when the host declares no named devices) still matches any undiscovered slave bomb. Mutates
    ``state`` and emits a player-visible ``data_bomb_found`` (a bomb was on the icon) or
    ``data_bomb_clear`` event."""
    scope, want_name = _data_bomb_scope_name(target_file or "")
    wn = want_name.strip().lower()
    # A generic slave scan (the old single-device UI option, the legacy "__slave__" token, or an
    # empty name) matches any undiscovered slave bomb; a named device matches that device only.
    slave_generic = scope == "slave" and wn in ("", "__device__", "slave device")
    bomb = None
    for b in (state.get("data_bombs") or []):
        if not isinstance(b, dict) or b.get("discovered"):
            continue
        bscope, bname = _data_bomb_scope_name(b.get("target", ""))
        if bscope != scope:
            continue
        if not slave_generic and bname.strip().lower() != wn:
            continue
        bomb = b
        break
    icon_label = "Slave device" if slave_generic else (want_name or "Slave device")
    if bomb is not None:
        bomb["discovered"] = True
        _append_event(state, {
            "type": "data_bomb_found",
            "subsystem": scope,
            "description": (
                f"Analyze Icon on \"{icon_label}\" -- DATA BOMB detected. "
                + ("Defuse it before you download or edit the file."
                   if scope == "files" else
                   "Defuse it before you access the device.")
            ),
        })
    else:
        _append_event(state, {
            "type": "data_bomb_clear",
            "subsystem": scope,
            "description": (
                f"Analyze Icon on \"{icon_label}\" -- nothing unusual; no data bomb on this "
                + ("file." if scope == "files" else "device.")
            ),
        })


def _apply_defuse_bomb(state: dict, decker: dict, eff: dict, *, subsystem: str,
                       subsystem_rating: int, decker_pool: int, sec_value: int, sec_code: str,
                       target_file: str = "") -> None:
    """Resolve a deliberate Defuse Data Bomb operation (vr2_rules.md L463-471, Complex Action): a
    Computer Test against the bomb's controlling subsystem rating (Files for a file bomb, Slave
    for a device bomb -- derived from the bomb's own scope by the caller) reduced by the carried
    Defuse utility.

    - Success (>=1 hit) disarms the bomb with NO security-tally increase: a successful defuse is
      not a crash, so the bomb's rating is never added to the tally and no suppression is needed.
    - Rolling ALL 1s detonates the bomb immediately (botch).
    - Any other failure leaves the bomb primed -- the decker may try again (or it triggers later
      if they access the protected target).

    The defuse models only the decker's Computer Test (no opposed-Security tally), matching the
    pure ``data_bomb_defuse`` helper and the no-tally rule. Targets the bomb on ``target_file``
    (decoded-name match, consistent with the surfaced discovered_data_bombs) or the first
    still-armed bomb when none is named. Mutates ``state`` and always emits a player-visible
    ``data_bomb`` event."""
    armed = state.get("data_bombs") or []
    defused = set(state.get("defused_bombs") or [])
    tgt = (target_file or "").strip().lower()
    bomb = next((b for b in armed
                 if b.get("target") not in defused
                 and (not tgt or _data_bomb_scope_name(b.get("target", ""))[1].strip().lower() == tgt)), None)
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
    """Data Bomb access trigger (vr2_rules.md L473): a SUCCESSFUL access (Download / Edit) of a
    file or Slave device that still carries an UNDEFUSED bomb sets it off -- the decker gets the
    access AND eats the blast. A FAILED access does NOT trigger it, and a bomb already disarmed
    (via the Defuse Data Bomb action) is inert. Returns True iff a bomb detonated; mutates
    ``state`` (removes the one-shot bomb and applies _detonate_data_bomb)."""
    if action_type not in ("download_data", "edit_file"):
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


# -- Combat maneuvers (vr2 L1982) ----------------------------------------------
# Evade Detection / Parry Attack / Position Attack are Simple Actions resolved as an opposed
# Evasion-vs-Sensor test between the maneuvering icon and ONE opposing icon (eng.maneuver_test).
# They are fully symmetric: the PC initiates against an IC / revealed enemy decker, and -- when
# state["npc_combat_maneuvers"] is set -- IC and revealed enemy deckers initiate against the PC
# via _npc_maybe_maneuver (they can INITIATE, not merely oppose).
#
# State written on the target/actor icon dict (also consumed by the re-detect work, item #5):
#   evaded (bool); evade_dir ("lost_pc" = the PC evaded it, it stays visible but cannot act until
#     it re-detects; "hid_from_pc" = it hid from the PC and vanishes from view until re-detected);
#   redetect_turn (absolute Combat Turn of automatic re-detection);
#   redetect_tally_base (security tally when it evaded -- every later tally point shortens the
#     hidden window by one Combat Turn, per vr2);
#   parry_tn_bonus (int, +TN to the PC's next attack on it);
#   position_bonus ({"tn_reduction": n} | {"power_bonus": n}, applied to its next attack on the PC).
# Run-level: pc_parry ({"vs": target_id, "bonus": n}); pc_position ({"tn_reduction": n} |
#   {"power_bonus": n}). An evade-detection maneuver by either party voids a pending Parry.

_MANEUVER_ACTIONS = ("evade_detection", "parry_attack", "position_attack")


def _evade_turns_remaining(state: dict, actor: dict) -> int:
    """Combat Turns until an evaded icon is automatically re-detected. Each security-tally point
    gained since it evaded shortens the hidden window by one turn (vr2). <= 0 means re-detected."""
    if not actor.get("evaded"):
        return 0
    tally_gain = max(0, state.get("security_tally", 0) - actor.get("redetect_tally_base", 0))
    return actor.get("redetect_turn", 0) - state.get("current_turn", 1) - tally_gain


def _clear_evade(state: dict, actor: dict, *, redetected: bool) -> None:
    """Clear an icon's evade/hidden markers. When ``redetected`` (the timer/tally window elapsed)
    restore a hidden enemy to view and emit a player-facing re-detection notice."""
    was_hidden = actor.get("evade_dir") == "hid_from_pc"
    for k in ("evaded", "evade_dir", "redetect_turn", "redetect_tally_base"):
        actor.pop(k, None)
    if redetected and was_hidden and "revealed" in actor:
        actor["revealed"] = True   # a hidden enemy decker comes back into contact
    if redetected:
        label = actor.get("type") or actor.get("name") or "The icon"
        desc = (f"{label} re-enters your sensors -- back in contact."
                if was_hidden else
                f"{label} has re-detected your icon -- it can act against you again.")
        _append_event(state, {"type": "maneuver", "maneuver": "re_detect",
                               "actor_id": actor.get("id"), "description": desc})


def _evade_active(state: dict, actor: dict) -> bool:
    """True while ``actor`` is still hidden from its opponent (skip its actions / hide it).
    Lazily re-detects + logs once the timer/tally window has elapsed."""
    if not actor.get("evaded"):
        return False
    if _evade_turns_remaining(state, actor) > 0:
        return True
    _clear_evade(state, actor, redetected=True)
    return False


def _sweep_evade_expiry(state: dict) -> None:
    """At the start of a new Combat Turn, re-detect any icon whose hidden window has elapsed."""
    for actor in list(state.get("active_ic", [])) + list(state.get("enemy_deckers", [])):
        if isinstance(actor, dict):
            _evade_active(state, actor)


def _break_parry_on_evade(state: dict, actor: dict) -> None:
    """An evade-detection maneuver by either party voids a pending Parry between them (vr2)."""
    actor.pop("parry_tn_bonus", None)
    parry = state.get("pc_parry")
    if parry and parry.get("vs") == actor.get("id"):
        state.pop("pc_parry", None)


def _consume_attack_mods_vs_pc(state: dict, attacker: dict) -> tuple[int, int]:
    """(tn_delta, power_delta) for one attack by an IC/enemy against the PC, consuming the PC's
    pending Parry (vs this attacker) and this attacker's own Position bonus."""
    tn_delta = 0
    power_delta = 0
    parry = state.get("pc_parry")
    if parry and parry.get("vs") == attacker.get("id"):
        tn_delta += int(parry.get("bonus", 0))        # Parry raises the TN of the attack on the PC
        state.pop("pc_parry", None)                    # consumed by the opposing icon's next attack
    pos = attacker.get("position_bonus")
    if pos:
        tn_delta -= int(pos.get("tn_reduction", 0))    # Position lowers the attacker's own TN ...
        power_delta += int(pos.get("power_bonus", 0))  # ... or raises its Power
        attacker.pop("position_bonus", None)
    return tn_delta, power_delta


def _consume_attack_mods_vs_target(state: dict, target: dict) -> tuple[int, int]:
    """(tn_delta, power_delta) for one PC attack against an IC/enemy, consuming the target's
    Parry bonus and the PC's own Position bonus."""
    tn_delta = 0
    power_delta = 0
    pbonus = target.get("parry_tn_bonus")
    if pbonus:
        tn_delta += int(pbonus)                        # the target parried -> the PC's to-hit TN rises
        target.pop("parry_tn_bonus", None)             # consumed by the PC's next attack
    pos = state.get("pc_position")
    if pos:
        tn_delta -= int(pos.get("tn_reduction", 0))
        power_delta += int(pos.get("power_bonus", 0))
        state.pop("pc_position", None)
    return tn_delta, power_delta


def _maneuver_target_lookup(state: dict, target_id: str) -> tuple[str | None, dict | None]:
    """Resolve a maneuver target id to (kind, obj): ("ic", ic) | ("enemy", enemy) | (None, None).
    A blank id picks the first eligible target (an active IC, else a revealed enemy decker)."""
    active_ic = [ic for ic in state.get("active_ic", [])
                 if isinstance(ic, dict) and ic.get("status") == "active"]
    enemies = [e for e in state.get("enemy_deckers", [])
               if isinstance(e, dict) and e.get("status") == "active" and e.get("revealed")]
    if target_id:
        ic = next((i for i in active_ic if i.get("id") == target_id), None)
        if ic is not None:
            return "ic", ic
        en = next((e for e in enemies if e.get("id") == target_id), None)
        if en is not None:
            return "enemy", en
        return None, None
    if active_ic:
        return "ic", active_ic[0]
    if enemies:
        return "enemy", enemies[0]
    return None, None


def _apply_maneuver(state: dict, decker: dict, eff: dict, body) -> None:
    """Resolve a PC-initiated combat maneuver (Evade/Parry/Position) against one opposing icon
    (vr2 L1982): the PC is the maneuvering icon (Evasion), the target is the opposing icon
    (Sensor). Mutates ``state`` in place; raises HTTPException on an invalid/absent target."""
    maneuver = body.action_type
    kind, target = _maneuver_target_lookup(state, (body.maneuver_target or "").strip())
    if target is None:
        raise HTTPException(
            400, "No eligible icon to maneuver against (need an active IC or a revealed enemy decker).")
    # vr2: you cannot Evade a reactive trace IC while it is running its location cycle.
    if maneuver == "evade_detection" and kind == "ic":
        info = rules.IC_CATALOG.get(_canonical_ic_type(target.get("type", "")), {})
        if info.get("subtype") == "trace" and target.get("trace_phase") == "locate":
            raise HTTPException(
                400, "You cannot evade a trace IC while it is running its location cycle.")
    sec_value = state.get("host_security_value", 6)
    if kind == "ic":
        opp_sensor_dice = sec_value
        opp_sensor_rating = int(target.get("rating", 6) or 6)
        opp_label = str(target.get("type", "IC"))
    else:
        opp_sensor_dice = int(target.get("sensor", 4) or 4)
        opp_sensor_rating = int(target.get("sensor", 4) or 4)
        opp_label = str(target.get("name", "enemy decker"))

    result = eng.maneuver_test(
        maneuvering_evasion_dice=eff.get("evasion", 4),
        maneuvering_evasion_rating=eff.get("evasion", 4),
        opposing_sensor_dice=opp_sensor_dice,
        opposing_sensor_rating=opp_sensor_rating,
    )
    net = result["net_successes"]
    man_succ = result["maneuvering_roll"]["successes"]
    opp_succ = result["opposing_roll"]["successes"]
    won = result["success"]
    current_turn = state.get("current_turn", 1)
    tally = state.get("security_tally", 0)
    ev: dict[str, Any] = {
        "type": "maneuver", "maneuver": maneuver, "initiator": "pc",
        "target_id": target.get("id"), "target": opp_label,
        "maneuvering_roll": result["maneuvering_roll"], "opposing_roll": result["opposing_roll"],
        "net_successes": net, "success": won,
    }

    if maneuver == "evade_detection":
        if won:
            _break_parry_on_evade(state, target)
            target["evaded"] = True
            target["evade_dir"] = "lost_pc"      # the PC hid; the icon keeps its place but loses you
            target["redetect_turn"] = current_turn + net
            target["redetect_tally_base"] = tally
            ev["description"] = (
                f"Evade Detection SUCCESS vs {opp_label} ({man_succ} vs {opp_succ}) -- it loses "
                f"your trail for {net} Combat Turn{'s' if net != 1 else ''} "
                "(sooner as the security tally climbs).")
        else:
            ev["description"] = (f"Evade Detection FAILED vs {opp_label} ({man_succ} vs {opp_succ}) "
                                 "-- it keeps you in its sensors.")
    elif maneuver == "parry_attack":
        if won:
            state["pc_parry"] = {"vs": target.get("id"), "bonus": net}
            ev["description"] = (f"Parry Attack SUCCESS vs {opp_label} ({man_succ} vs {opp_succ}) "
                                 f"-- +{net} TN to its next attack on you.")
        else:
            ev["description"] = f"Parry Attack FAILED vs {opp_label} ({man_succ} vs {opp_succ})."
    else:  # position_attack
        choice = "power" if str(getattr(body, "position_choice", "tn")).strip().lower() == "power" else "tn"
        if won:
            state["pc_position"] = {"power_bonus": net} if choice == "power" else {"tn_reduction": net}
            gain = f"+{net} Power" if choice == "power" else f"-{net} TN"
            ev["position_choice"] = choice
            ev["description"] = (f"Position Attack SUCCESS vs {opp_label} ({man_succ} vs {opp_succ}) "
                                 f"-- {gain} on your next attack.")
        elif opp_succ > man_succ:
            # Risky maneuver: the opposing icon wins the exchange and gains the positioning instead.
            opp_net = opp_succ - man_succ
            target["position_bonus"] = {"tn_reduction": opp_net}
            ev["description"] = (f"Position Attack BACKFIRED vs {opp_label} ({man_succ} vs {opp_succ}) "
                                 f"-- it gains -{opp_net} TN on its next attack on you.")
        else:
            ev["description"] = (f"Position Attack tied vs {opp_label} ({man_succ} vs {opp_succ}) "
                                 "-- no advantage gained.")
    _append_event(state, ev)


def _resolve_npc_maneuver(state: dict, decker: dict, eff: dict, actor: dict,
                          maneuver: str, *, is_ic: bool) -> bool:
    """An IC / enemy decker INITIATES a combat maneuver against the PC (npc_combat_maneuvers).
    The NPC is the maneuvering icon (Evasion); the PC is the opposing icon (Sensor). Mutates
    ``state`` and returns True (the NPC spent its action on the maneuver instead of attacking)."""
    sec_value = state.get("host_security_value", 6)
    if is_ic:
        man_evasion_dice = sec_value
        man_evasion_rating = int(actor.get("rating", 6) or 6)
        label = str(actor.get("type", "IC"))
    else:
        man_evasion_dice = int(actor.get("evasion", 4) or 4)
        man_evasion_rating = int(actor.get("evasion", 4) or 4)
        label = str(actor.get("name", "enemy decker"))

    result = eng.maneuver_test(
        maneuvering_evasion_dice=man_evasion_dice,
        maneuvering_evasion_rating=man_evasion_rating,
        opposing_sensor_dice=eff.get("sensor", 4),
        opposing_sensor_rating=eff.get("sensor", 4),
    )
    net = result["net_successes"]
    man_succ = result["maneuvering_roll"]["successes"]
    opp_succ = result["opposing_roll"]["successes"]
    won = result["success"]
    current_turn = state.get("current_turn", 1)
    tally = state.get("security_tally", 0)
    ev: dict[str, Any] = {
        "type": "maneuver", "maneuver": maneuver, "initiator": "npc",
        "actor_id": actor.get("id"), "actor": label,
        "maneuvering_roll": result["maneuvering_roll"], "opposing_roll": result["opposing_roll"],
        "net_successes": net, "success": won,
    }

    if maneuver == "evade_detection":
        if won:
            _break_parry_on_evade(state, actor)
            actor["evaded"] = True
            actor["evade_dir"] = "hid_from_pc"   # the NPC hides and vanishes from your view
            actor["redetect_turn"] = current_turn + net
            actor["redetect_tally_base"] = tally
            if "revealed" in actor:
                actor["revealed"] = False        # an enemy decker drops off your sensors entirely
            ev["description"] = (f"{label} breaks contact and slips out of your sensors "
                                 f"({man_succ} vs {opp_succ}).")
        else:
            ev["description"] = (f"{label} tries to break contact but you hold the lock "
                                 f"({man_succ} vs {opp_succ}).")
    elif maneuver == "parry_attack":
        if won:
            actor["parry_tn_bonus"] = net
            ev["description"] = (f"{label} takes a defensive stance -- +{net} TN to your next "
                                 "attack on it.")
        else:
            ev["description"] = f"{label} fails to set a guard ({man_succ} vs {opp_succ})."
    else:  # position_attack
        if won:
            actor["position_bonus"] = {"tn_reduction": net}
            ev["description"] = f"{label} maneuvers into position -- -{net} TN on its next attack on you."
        elif opp_succ > man_succ:
            opp_net = opp_succ - man_succ
            state["pc_position"] = {"tn_reduction": opp_net}
            ev["description"] = (f"{label} overreaches for position -- you turn it around "
                                 f"(-{opp_net} TN on your next attack).")
        else:
            ev["description"] = f"{label} jockeys for position but gains no edge ({man_succ} vs {opp_succ})."
    _append_event(state, ev)
    return True


def _npc_maybe_maneuver(state: dict, decker: dict, eff: dict, actor: dict, *, is_ic: bool) -> bool:
    """Decide whether an IC / enemy decker spends its action on a combat maneuver instead of an
    attack (gated by state["npc_combat_maneuvers"]). Deterministic priority: break off when
    badly wounded, guard when moderately wounded, seize position when healthy and already pressing
    a wounded PC. Returns True if a maneuver was performed (its attack is then skipped)."""
    if not state.get("npc_combat_maneuvers") or actor.get("evaded"):
        return False
    if is_ic:
        boxes = int(actor.get("boxes", 0) or 0)
    else:
        boxes = int((actor.get("condition_monitor", {}) or {}).get("persona_boxes", 0) or 0)
    pc_persona = int((state.get("condition_monitor", {}) or {}).get("persona_boxes", 0) or 0)
    # 1) Badly wounded -> Evade Detection to break off. IC-only: enemy DECKERS handle breaking off
    # in the wounded-AI loop (which runs before this and only hides Medic-carriers, since a healless
    # decker gains nothing by hiding), so a decker reaching here stands and fights (Parry/attack).
    if boxes >= 7 and is_ic:
        return _resolve_npc_maneuver(state, decker, eff, actor, "evade_detection", is_ic=is_ic)
    # 2) Moderately wounded -> Parry to blunt the PC's next strike.
    if 4 <= boxes <= 6 and not actor.get("parry_tn_bonus"):
        return _resolve_npc_maneuver(state, decker, eff, actor, "parry_attack", is_ic=is_ic)
    # 3) Healthy but the PC is already hurt -> Position Attack to press the advantage.
    if boxes <= 3 and pc_persona >= 2 and not actor.get("position_bonus"):
        return _resolve_npc_maneuver(state, decker, eff, actor, "position_attack", is_ic=is_ic)
    return False


def _apply_locate_ic(state: dict, *, test_success: bool) -> None:
    """Locate IC (vr2 L1884 + L1998, correction #5): a System Test ONLY (no Sensor Test) that
    RE-DETECTS every IC which evaded the decker via the Evade Detection maneuver
    (evade_dir == "hid_from_pc"). Per the user ruling it does NOT reveal never-seen IC -- a
    lurking reactive IC betrays itself only by acting -- so Locate IC matters only once an IC has
    hidden. A successful System Test clears each evaded IC's markers (via _clear_evade, which also
    logs a RE-DETECT notice) so _serialize_run shows the IC again. Mutates ``state``."""
    evaded_ic = [ic for ic in state.get("active_ic", [])
                 if isinstance(ic, dict) and ic.get("status") == "active"
                 and ic.get("evaded") and ic.get("evade_dir") == "hid_from_pc"]
    if not evaded_ic:
        _append_event(state, {
            "type": "ic_relocate", "outcome": "none",
            "description": "Locate IC: no IC has slipped your sensors -- nothing to re-locate.",
        })
        return
    if not test_success:
        _append_event(state, {
            "type": "ic_relocate", "outcome": "fail",
            "description": "Locate IC failed -- the evaded IC stays off your sensors this pass.",
        })
        return
    for ic in evaded_ic:
        _clear_evade(state, ic, redetected=True)


def _apply_locate_decker(state: dict, decker: dict, *, test_success: bool, scanner: int) -> None:
    """Locate Decker (vr2 L1880 two-step + L1999, corrections #5/#6): RE-DETECTS a decker that
    evaded the PC (evade_dir == "hid_from_pc"). Per the user ruling it re-acquires ONLY evaded
    deckers -- a never-seen hunter reveals itself when it starts hunting, so this is not a blanket
    "find every hidden icon" scan. Two-step per RAW: the Index System Test (``test_success``)
    gates the attempt, then an opposed Sensor Test vs the enemy's FULL current Masking + Sleaze
    (#6, Scanner reduces the TN) decides each re-acquisition. A located enemy has its evade
    cleared (back into view, can be Struck Back). Mutates ``state``."""
    evaded = [e for e in state.get("enemy_deckers", [])
              if isinstance(e, dict) and e.get("status") == "active"
              and e.get("evaded") and e.get("evade_dir") == "hid_from_pc"]
    sensor = int(decker.get("sensor", 1) or 1)
    if not evaded:
        _append_event(state, {
            "type": "enemy_decker", "outcome": "scan_clear",
            "description": "Index sweep for evaded icons -- no decker has slipped your sensors to re-locate.",
        })
        return
    if not test_success:
        _append_event(state, {
            "type": "enemy_decker", "outcome": "scan_fail",
            "description": "Index sweep failed -- you can't re-acquire the decker that evaded you this pass.",
        })
        return
    found = []
    for e in evaded:
        # #6: opposed test vs the enemy's FULL current Masking + Sleaze (not the halved Detection
        # Factor) -- current masking means a Reveal-crippled decker is easier to re-find.
        mask = int(e.get("masking", 1) or 1)
        sleaze = int((e.get("utilities") or {}).get("sleaze", 0) or 0)
        res = eng.pc_locate_decker_test(
            sensor_rating=sensor,
            scanner_rating=scanner,
            enemy_mask_sleaze=mask + sleaze,
            enemy_evasion=int(e.get("evasion", 1) or 1),
        )
        if res["located"]:
            _clear_evade(state, e, redetected=True)   # clears evade + revealed=True + RE-DETECT notice
            found.append((e, res))
    if found:
        names = ", ".join(f"{e['name']} (tier {e.get('tier', '?')})" for e, _ in found)
        _append_event(state, {
            "type": "enemy_decker", "outcome": "scan_hit", "enemy_id": found[0][0]["id"],
            "description": f"Re-acquired evaded decker(s): {names}. You can Strike Back.",
        })
    else:
        _append_event(state, {
            "type": "enemy_decker", "outcome": "scan_fail",
            "description": (
                "Index sweep ran clean but your Sensor pass couldn't re-acquire the evaded decker "
                "-- try again next pass."
            ),
        })


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

def _autofire_lurking_tar(state: dict, decker: dict, action_type: str, utility_rating: int) -> None:
    """Auto-fire every lurking Tar Baby / Tar Pit against the utility the decker just ran on a
    System Test (app-as-GM -- there is no human GM to pick the target program). A tar makes one
    opposed test per utility use; ``utility_rating <= 0`` means the operation ran no reducible
    utility, so nothing fires. The utility's name is taken from the operation it belongs to."""
    if utility_rating <= 0:
        return
    utility_name = _ACTION_UTILITY.get(action_type) or "utility"
    for lurking in list(state.get("lurking_ic", [])):
        if state.get("run_ended"):
            break
        if (lurking.get("type") in ("Tar Baby", "Tar Pit")
                and lurking.get("status", "lurking") == "lurking"):
            _resolve_lurking_tar(state, decker, lurking, utility_name, utility_rating)


def _advance_npc_pass(state: dict, decker: dict, run, *, eff: dict, sec_code: str,
                      sec_value: int, det_factor: int, logon_completed: bool = False) -> None:
    """Drive every app-controlled hostile for the CURRENT initiative pass (``state['current_pass']``):
    proactive / trace IC attacks (in initiative order) followed by enemy deckers, each gated by its
    own initiative passes and an ``acted_pass`` marker so it acts at most once per pass.

    There is no human GM -- this is the app-as-GM loop. It is called from ``perform_action`` after
    the player's action resolves, and from ``new_turn`` to flush the passes the player never reached
    so hostiles always take their full allotment each Combat Turn. Probe IC (which test per System
    Test, not per pass) are handled by the caller, NOT here. ``logon_completed`` carries the player's
    just-resolved Logon so the event fires in its original position between the IC and enemy loops.
    Mutates ``state`` (and ``run.status`` on a kill/dump); does NOT commit.
    """
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
        ic_passes = _ic_passes(ic)
        # Slow utility (vr2_rules.md L1576): a slowed IC loses actions this Combat Turn, so its
        # effective passes shrink by ic['actions_lost']; with none left it HANGS (does nothing this
        # turn). new_turn clears actions_lost so the IC resumes next turn -- unless still suppressed.
        effective_passes = max(0, ic_passes - ic.get("actions_lost", 0))
        if cur_pass > effective_passes or ic.get("acted_pass") == cur_pass:
            continue
        ic["acted_pass"] = cur_pass

        # Combat maneuver: an IC that has lost/hidden from the PC (Evade Detection) does not act
        # this pass; the hidden window auto-expires (timer / security tally) inside _evade_active.
        if _evade_active(state, ic):
            continue

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
                                f"({ds.get('boxes',0)} boxes stun)."
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
        if _decoy_intercept(state, ic, sec_code=sec_code, sec_value=sec_value,
                            ic_target_status=ic_target_status):
            continue  # IC consumed its action on the decoy

        # Combat maneuver: an attacking IC may spend its action to maneuver against you instead
        # of attacking (heuristic; only when npc_combat_maneuvers is set).
        if _npc_maybe_maneuver(state, decker, eff, ic, is_ic=True):
            continue
        # Parry (against this IC) + Position (held by this IC) modifiers for this attack.
        atk_tn_delta, atk_power_delta = _consume_attack_mods_vs_pc(state, ic)

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
                # combat-maneuver Parry(+)/Position(-) to-hit delta + the IC's own wound penalty
                tn_modifier=atk_tn_delta + _ic_wound_mod(ic),
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
            attack_tn  = max(2, rules.COMBAT_TN[sec_code][ic_target_status] + cluster_penalty + atk_tn_delta + _ic_wound_mod(ic))
            attack_roll_black = eng.roll_dice(ic_attack_pool, attack_tn)
            base_dmg   = rules.IC_DAMAGE_LEVEL[sec_code]
            # Shield parry: net successes cancel the icon-damage staging. Black IC derives BOTH
            # the persona hit and (when lethal) the physical biofeedback from this one strike, so
            # a successful parry blunts every consequence of the parried attack.
            shield_succ = _shield_parry(state, decker, attacker_skill=sec_value, context="Black IC")
            black_succ = max(0, attack_roll_black["successes"] - shield_succ)
            staged_dmg = eng.stage_damage(base_dmg, black_succ, 1)
            power      = max(1, ic["rating"] - hardening + atk_power_delta)  # + combat-maneuver Position Power

            if is_non_lethal:
                # Cool deck: Non-Lethal Black IC -- Willpower test, Stun damage only
                will_roll = eng.roll_dice(decker.get("willpower", 4), power)
                stun_dmg  = eng.stage_damage(staged_dmg, will_roll["successes"], -1)
                stun_boxes = rules.DAMAGE_BOXES[stun_dmg]
                _add_stun(state["condition_monitor"], stun_boxes)
                _append_event(state, {
                    "type": "ic_attack",
                    "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                    "description": (
                        f"Black IC (non-lethal) {ic['rating']}: "
                        f"{attack_roll_black['successes']} atk successes. "
                        f"Willpower resist ({will_roll['successes']} hits): "
                        f"Stun {stun_dmg} ({stun_boxes} boxes). "
                        f"Stun CM: {state['condition_monitor']['stun_boxes']}/10"
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

            # Black IC meat threshold: lethal fills Physical Damage (10 = killed); non-lethal fills
            # Physical Stun (10 = unconscious -> connection breaks). Either drop triggers one final
            # MPCP attack at 2x rating (Blaster mechanics) as the decker goes down.
            phys_full = state["condition_monitor"]["physical_boxes"] >= 10
            stun_full = state["condition_monitor"]["stun_boxes"] >= 10
            if phys_full or stun_full:
                crit = ("physical damage -- decker in critical condition" if phys_full
                        else "stun -- decker unconscious, connection dropping")
                _append_event(state, {
                    "type": "persona_crash",
                    "description": f"BLACK IC -- {crit}!",
                })
                mpcp_hit, bl_roll = _roll_mpcp_damage(state, decker, ic["rating"], pool_multiplier=2)
                _append_event(state, {
                    "type": "ic_attack",
                    "ic_id": ic["id"], "ic_type": "Black IC",
                    "description": f"Black IC MPCP attack at 2x rating: MPCP -{mpcp_hit} (permanent).",
                    "mpcp_roll": bl_roll, "mpcp_damage": mpcp_hit,
                })
                state["run_ended"] = True
                state["end_reason"] = "black_ic_lethal" if phys_full else "black_ic_unconscious"
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
            ic_rating=cascade_power + atk_power_delta,     # + combat-maneuver Position Power
            attacker_is_ic=True,
            # + Parry(+)/Position(-) to-hit delta + the IC's own wound penalty
            tn_modifier=cluster_penalty + atk_tn_delta + _ic_wound_mod(ic),
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
                _add_stun(state["condition_monitor"], 1)
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
                        f"Dump shock: {ds['final_level']} ({ds['boxes']} boxes stun). "
                        f"Stun: {state['condition_monitor']['stun_boxes']}"
                    ),
                    "dump_shock": ds,
                })
            state["run_ended"] = True
            state["end_reason"] = "persona_crashed"
            break

    # Handle logon completion (player-action result; parameterized so new_turn's flush skips it).
    if logon_completed:
        state["logon_complete"] = True
        _append_event(state, {
            "type": "logon",
            "description": f"Logged on to host successfully. Detection Factor: {det_factor}.",
        })

    # Enemy deckers act automatically (app-as-GM), once per pass on the passes their OWN
    # initiative reaches (ceil(init/10) passes) -- they rolled initiative once when they entered.
    cur_pass = state.get("current_pass", 1)
    for enemy in list(state.get("enemy_deckers", [])):
        if state.get("run_ended"):
            break
        if (enemy.get("status") == "active"
                and cur_pass <= _enemy_passes(enemy)
                and enemy.get("acted_pass") != cur_pass):
            enemy["acted_pass"] = cur_pass
            _enemy_decker_take_turn(state, decker, run, enemy)


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

    # Validate Passcode (house rule): a FAILED attempt permanently locks the operation out for the
    # rest of the run -- reject a retry BEFORE spending the action so no initiative pass is wasted.
    if body.action_type == "validate_passcode" and state.get("validate_passcode_attempted"):
        raise HTTPException(400, "Validate Passcode already failed this run -- it cannot be attempted again.")

    # A background Download Data transfer commits the deck's Complex action to an automatic Null
    # Operation each turn (vr2 ongoing operation), so while one runs the decker may take only FREE
    # actions (e.g. Analyze IC). Refuse any Simple/Complex op until the transfer completes or is
    # abandoned (log off) -- advancing the turn (New Turn) is what progresses it.
    if state.get("active_download") and _ACTION_COST.get(body.action_type, "Complex") != "Free":
        _dl = state["active_download"]
        if body.action_type == "download_data":
            raise HTTPException(
                400,
                f"A download is already in progress (\"{_dl.get('file')}\", "
                f"{_dl.get('turns_left')} turn(s) left). Finish or abandon it before starting another.")
        raise HTTPException(
            400,
            f"Download in progress (\"{_dl.get('file')}\", {_dl.get('turns_left')} turn(s) left) -- "
            "the deck's Complex action is committed to the transfer. Only Free actions are available "
            "until it completes; advance the turn (New Turn) to continue it.")

    # Action economy: spend this action's cost from the current initiative pass (auto-advances
    # passes; blocks when all passes are spent -> New Turn). vr2: 2 Simple OR 1 Complex + 1 Free.
    _spend_pass_action(state, body.action_type)

    # Combat maneuvers (vr2 L1982): Evade Detection / Parry Attack / Position Attack are opposed
    # Evasion-vs-Sensor tests against ONE opposing icon -- NOT a host System Test -- so they add
    # no security tally and never fall through to the generic test below. Resolved and returned.
    if body.action_type in _MANEUVER_ACTIONS:
        _apply_maneuver(state, decker, eff, body)
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

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
    # Analyze Icon (Control test) is uniquely sharpened by the decker's gear: vr2 reduces its TN
    # by the Sensor rating IN ADDITION to the Analyze utility (already applied above). The rules
    # floor of "minimum TN of 2" is enforced by system_test's max(2, ...) clamp.
    if body.action_type == "analyze_icon":
        tn_modifier -= eff.get("sensor", 0)
    # Validate Passcode (house rule): the plant test itself is +2 TN. Separately, once a passcode
    # has been validated this run (passcode_tn_bonus), every OTHER System Test gets -2 TN -- the
    # buff never helps the validate test itself. Both feed the generic system_test below.
    if body.action_type == "validate_passcode":
        tn_modifier += 2
    elif state.get("passcode_tn_bonus"):
        tn_modifier -= 2

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
    # (Files for a file bomb, Slave for a device bomb -- derived from the bomb's own scope, not the
    # client) reduced by the carried Defuse utility. Success disarms the bomb with NO tally add (a
    # defuse is not a crash); an all-1s botch detonates it; any other failure leaves it primed to
    # retry. Resolved here and returned so it never falls through to the generic system_test below.
    if body.action_type == "defuse_data_bomb":
        # vr2 L463-471: test the bomb against ITS controlling subsystem -- Files for a file bomb,
        # Slave for a device bomb -- derived from the matched bomb's scope, not the client-sent
        # subsystem (so a Slave bomb is never mis-tested against the Files rating).
        defuse_sub = _defuse_target_subsystem(state, body.target_file) or body.subsystem
        _apply_defuse_bomb(
            state, decker, eff,
            subsystem=defuse_sub,
            subsystem_rating=_subsystem_rating(state, defuse_sub),
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

    # Decrypt File is resolved against a Scramble IC (its rating IS the decrypt TN), NOT the generic
    # subsystem test, and NEVER falls through to it -- Decrypt adds no security tally (vr2 L495).
    # A scramble can only be targeted once DISCOVERED via an Analyze Subsystem on the Files/Slave
    # subsystem that holds it (vr2 L1864); until then the player cannot even see it, and this
    # handler refuses the op. A failed decrypt vs a POISON Scramble destroys the protected data --
    # key data is a permanent, mission-critical loss shown to the player.
    if body.action_type == "decrypt_file":
        scrambles = state.get("scrambles") or []
        disc = [s for s in scrambles if s.get("discovered")]
        scr = None
        if body.target_file:
            scr = next((s for s in disc if s.get("target_key") == body.target_file), None)
            if scr is None:
                want = _target_file_name(body.target_file).strip().lower()
                scr = next((s for s in disc
                            if _target_file_name(s.get("target_key", "")).strip().lower() == want), None)
        if scr is None:
            # No discovered scramble matches (unknown target, or none discovered yet). Do NOT run
            # the decrypt test and do NOT touch the tally -- just tell the decker to Analyze first.
            _append_event(state, {"type": "decrypt", "success": False,
                "description": "No discovered scramble on that target -- Analyze the Files/Slave subsystem first."})
            run.state_json = state
            await db.commit(); await db.refresh(run)
            return _serialize_run(run, auth)
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
            protected = next((p for p in paydata
                              if p.get("name")
                              and _target_file_name(scr.get("target_key", "")).strip().lower()
                              == str(p["name"]).strip().lower()), None)
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

    # Analyze Icon (Free, Control test): targeted scan that reveals an undefused data bomb on the
    # named file or the Slave device (vr2 L463). The ONLY bomb-discovery path -- a broad Analyze
    # Subsystem no longer surfaces them. See _apply_analyze_icon.
    if body.action_type == "analyze_icon" and test["success"]:
        _apply_analyze_icon(state, target_file=body.target_file or "")

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
        # Scramble IC is likewise revealed by an Analyze Subsystem on the subsystem that holds it
        # (vr2 L1864: Analyze Subsystem "identifies ... scramble IC, and other defenses"). Until a
        # scramble is discovered it is not even offered for Decrypt File. Access scramble is not
        # meaningfully authored in this app, but _scramble_subsystem handles it generically.
        newly_scr = [s for s in (state.get("scrambles") or [])
                     if not s.get("discovered") and _scramble_subsystem(s.get("target_key", "")) == sub]
        for s in newly_scr:
            s["discovered"] = True
            _append_event(state, {
                "type": "scramble_found",
                "target_key": s.get("target_key", ""),
                "subsystem": sub,
                "description": (
                    f"Scramble IC detected on the {sub.capitalize()} subsystem "
                    f"({_scramble_label(s.get('target_key', ''))}) -- Decrypt it before "
                    "operating on the protected data."
                ),
            })
        # Data bombs are NOT surfaced here: a node-wide Analyze Subsystem is too cheap to also
        # reveal every booby-trapped file/device. Per vr2 a data bomb is detected by an Analyze
        # Icon on the specific protected file or device (see the analyze_icon handler above).
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

    # Analyze Host: reveal the host's ACIFS subsystem ratings. 5+ net successes (or enough to cover
    # every hidden rating) reveals ALL remaining; otherwise the credits are banked and the decker
    # chooses which hidden ratings to reveal via POST /reveal-host-ratings. See _apply_analyze_host.
    if body.action_type == "analyze_host" and test["success"]:
        _apply_analyze_host(state, test["decker_net_successes"])

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

    # Validate Passcode (house rule): a net success grants Legitimate status (IC uses the
    # Legitimate TN column) AND a run-long -2 TN to every other System Test. A failed plant is a
    # ONE-SHOT -- it can never be retried this run, and the security tally still rose by the host's
    # successes (already applied by the generic tally bump above).
    if body.action_type == "validate_passcode" and test["success"]:
        state["has_legitimate_status"] = True
        state["passcode_tn_bonus"] = True
        _append_event(state, {
            "type": "validate_passcode",
            "success": True,
            "description": (
                "Validate Passcode successful -- Legitimate status granted (IC uses the Legitimate "
                "TN column until logoff or active alert), and every other System Test gets -2 TN for "
                "the rest of the run."
            ),
        })
    elif body.action_type == "validate_passcode" and not test["success"]:
        state["validate_passcode_attempted"] = True
        _append_event(state, {
            "type": "validate_passcode",
            "success": False,
            "description": (
                f"Validate Passcode FAILED -- the host rejected the plant (tally +"
                f"{test['tally_increase']}). It cannot be attempted again this run."
            ),
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

    # Locate Paydata (vr2 "Locate Paydata" -- ongoing operation): RAW reveals ONE Paydata Point
    # per NET success. Reveal min(net successes, remaining) undiscovered files chosen at RANDOM
    # via a LOCAL random.Random -- never seed the global RNG in a request path (AGENTS.md RNG
    # rule). The seed is derived from run id + current turn + security tally + the count already
    # located, so results are reproducible for fixed inputs yet reveal DIFFERENT files as the run
    # progresses. Located files surface to the player via _serialize_run (located_paydata); the
    # full paydata list stays GM-only. Repeatable until every paydata point is found.
    if body.action_type == "locate_paydata" and test["success"]:
        pool = [p for p in (state.get("paydata") or [])
                if not p.get("located") and not p.get("destroyed")]
        if pool:
            net = max(1, int(test["decker_net_successes"]))
            already_located = sum(1 for p in (state.get("paydata") or []) if p.get("located"))
            seed = (
                (int(getattr(run, "id", 0) or 0) * 1_000_003)
                ^ (int(state.get("current_turn", 0) or 0) * 8191)
                ^ (int(state.get("security_tally", 0) or 0) * 131)
                ^ (already_located * 17)
            )
            rng = random.Random(seed)
            newly = rng.sample(pool, min(net, len(pool)))
            for p in newly:
                p["located"] = True
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

    # Locate IC / Locate Decker (vr2 L1884/L1880 + L1998-1999, corrections #5/#6): the two
    # re-detect operations for an icon that slipped you with an Evade Detection maneuver. Locate
    # IC is a System Test only; Locate Decker adds the #6 opposed Sensor Test vs full Masking +
    # Sleaze. Neither reveals never-seen icons (those betray themselves by acting) -- they only
    # re-acquire icons you had already detected and then lost. See the helper docstrings.
    if body.action_type == "locate_ic":
        _apply_locate_ic(state, test_success=test["success"])

    if body.action_type == "locate_decker":
        _apply_locate_decker(state, decker, test_success=test["success"],
                             scanner=max(0, int(body.utility_rating or 0)))

    # Delete File (vr2 Edit File / Files Test): the only in-app use of Edit File is to ERASE a
    # located paydata file -- sabotage that denies the data to its owner. A successful Files test
    # marks the targeted paydata destroyed (it drops out of the located/decrypt/download lists and
    # the UI greys it). A bombed file still detonates on this access (see _trigger_access_data_bomb).
    if body.action_type == "edit_file" and test["success"] and body.target_file:
        tgt_name = body.target_file.strip().lower()
        pd = next((p for p in (state.get("paydata") or [])
                   if str(p.get("name", "")).strip().lower() == tgt_name and not p.get("destroyed")),
                  None)
        if pd is not None:
            pd["destroyed"] = True
            _append_event(state, {
                "type": "file_deleted",
                "file_name": pd.get("name"),
                "description": f"File \"{pd.get('name')}\" erased from the host -- the data is gone.",
            })

    # Download Data: on success, pull the named file -- record it in the player-visible ledger
    # (downloaded_files) and consume finite deck storage. The pre-check above guarantees it fits.
    if body.action_type == "download_data" and test["success"] and body.target_file:
        tgt_name = body.target_file.strip().lower()
        pd = next((p for p in (state.get("paydata") or [])
                   if str(p.get("name", "")).strip().lower() == tgt_name and not p.get("destroyed")),
                  None)
        if pd is not None and not pd.get("downloaded"):
            # Transfer time (vr2 Download Data is an ongoing op at the deck's I/O bandwidth,
            # L1873/L1256): turns = ceil(stored / io_speed) where ``stored`` is the SAME
            # compressor-effective footprint the file will occupy on the deck -- a Compressor that
            # can handle the file halves what must be transferred; an oversized file transfers
            # full. A file that fits in one turn's bandwidth lands immediately; a larger one runs
            # as a multi-turn BACKGROUND transfer that auto-rolls a Null Operation each turn.
            density = max(0, int(pd.get("density", 0) or 0))
            comp = _effective_compressor(decker)
            stored, compressible = _compressed_store_size(comp, density)
            turns = _download_turns(decker, stored)
            if turns <= 1:
                _complete_download(state, decker, pd)
            else:
                io = int(decker.get("io_speed", 0) or 0)
                state["active_download"] = {
                    "file": pd.get("name"),
                    "stored_mp": stored,
                    "full_mp": density,
                    "compressed": compressible,
                    "is_key": bool(pd.get("is_key")),
                    "turns_total": turns,
                    "turns_left": turns - 1,
                    "started_turn": state.get("current_turn", 1),
                }
                _append_event(state, {
                    "type": "download_started",
                    "file_name": pd.get("name"),
                    "size_mp": stored,
                    "turns_total": turns,
                    "turns_left": turns - 1,
                    "description": (
                        f"Began downloading \"{pd.get('name')}\" ({stored} Mp) at {io} Mp/turn -- "
                        f"about {turns} Combat Turns. The deck auto-runs a Null Operation each turn "
                        "until it completes; only Free actions are available until then. Logging "
                        "off or a host crash before it finishes corrupts the file."
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

    # Ambush IC (app-as-GM): any lurking Tar Baby / Tar Pit fires at the utility the decker just
    # ran on this System Test -- one opposed test per utility use. Gated on utility_rating > 0, so
    # actions that ran no reducible utility (or the early-return actions above) never trigger it.
    _autofire_lurking_tar(state, decker, body.action_type, body.utility_rating)

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

    # Drive every app-controlled hostile for this initiative pass: proactive/trace IC attacks
    # then enemy deckers. Probe IC (which test per System Test, above) are NOT driven here.
    # The just-resolved Logon is carried in so its event still fires between the IC and enemy loops.
    _advance_npc_pass(
        state, decker, run,
        eff=eff, sec_code=sec_code, sec_value=sec_value, det_factor=det_factor,
        logon_completed=(body.action_type == "logon_to_host" and test["success"]),
    )

    if state.get("run_ended"):
        run.status = state.get("end_reason", "crashed")
    # A run that ends mid-transfer (e.g. a Free action drew a fatal enemy-decker attack) corrupts
    # the in-progress download -- a partial copy is worthless (vr2 Download Data).
    if state.get("run_ended") and state.get("active_download"):
        _corrupt_active_download(state)

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


def _apply_ic_crash(state: dict, target_ic: dict, sec_code: str, skulk: int) -> None:
    """Resolve an IC crash: mark it crashed, bump the security tally (masked by the Skulk
    rating), log the crash event, check sheaf triggers, and spawn any hidden Trap IC. Shared
    by the single-target Attack and the Area strike so both stay in lock-step."""
    target_ic["status"] = "crashed"
    # Skulk masks the crash: reduce the tally increase by the Skulk rating, but never below 0
    # and never zero out a high-rating IC entirely (Rating-10 IC, Skulk-8 -> +2).
    tally_increase = max(0, target_ic["rating"] - skulk)
    state["security_tally"] += tally_increase
    skulk_note = (
        f" (Skulk-{skulk} masked the crash)"
        if skulk > 0 and tally_increase < target_ic["rating"] else ""
    )
    _append_event(state, {
        "type": "ic_crashed",
        "ic_id": target_ic["id"],
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
    # Limit option (vr2): an Attack utility Limited to deckers is useless against IC.
    if (((decker.get("program_options") or {}).get("attack") or {}).get("limit_target")) == "decker":
        raise HTTPException(400, "This Attack utility is Limited to deckers -- it cannot target IC.")
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
    # Combat maneuver: the target's Parry (raises the PC's to-hit TN) + the PC's own Position
    # (lowers the TN and/or raises Power). Consumed by this single attack.
    tgt_tn_delta, tgt_power_delta = _consume_attack_mods_vs_target(state, target_ic)
    # Area option lets one Attack Test cope with an IC cluster -- it offsets the cluster's
    # to-hit penalty (up to the Area rating). This is the single-target-engine equivalent of
    # "hit up to [Area] clustered targets with one test"; it eases the attacker's to-hit only.
    atk_cluster_penalty = max(0, cluster_penalty - opt_area) if opt_area > 0 else cluster_penalty
    base_tn = rules.COMBAT_TN[sec_code]["intruding"] + atk_cluster_penalty
    # Shield/Shift raise the decker's to-hit TN; Penetration defeats Shield, Chaser defeats Shift.
    shield_shift = _shield_shift_tn_modifier(
        target_ic, penetration=opt_pen, chaser=opt_chaser)
    # The decker's own cumulative wound penalty raises their to-hit TN (+1 per wound level).
    tn = base_tn + shield_shift + tgt_tn_delta + _decker_wound_mod(state)
    if opt_target:
        tn = max(2, tn - 2)   # Targeting option: -2 to-hit TN on attacks with this utility
    tn = max(2, tn)           # clamp (a Position TN reduction can never push the TN below 2)

    attack_roll = eng.roll_dice(attack_pool, tn)
    base_dmg = rules.IC_DAMAGE_LEVEL[sec_code]

    # IC resists with Security Value dice vs the combat TN (the attack Power here).
    # Armor reduces that POWER (lower TN -> the IC resists more easily) -- it does NOT lower
    # the damage level. Expert adds/removes resist dice (Defense +N, Offense -N -- the trade-off).
    # A Position "Power" bonus raises the resist TN (the IC resists a harder-hitting strike).
    resist_tn = rules.COMBAT_TN[sec_code]["intruding"] + cluster_penalty + tgt_power_delta
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
    # Bailing out mid-transfer corrupts the partial download (vr2: needs the COMPLETE file).
    if success and state.get("active_download"):
        _corrupt_active_download(state)

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

    # -- End-of-turn NPC pass flush (app-as-GM) --------------------------------------------------
    # current_pass only ever climbs as far as the DECKER's own initiative passes (via the action
    # economy), so a hostile with MORE passes than the decker -- or any hostile at all, when the
    # decker ends the turn without acting -- would be cheated of the passes it never got. Before
    # the turn resets, drive those remaining passes now: no human GM runs the opposition. Each
    # NPC self-gates on its OWN initiative passes and its acted_pass marker, so passes already
    # taken this turn are skipped (idempotent) and only the missing ones fire.
    npc_decker = run.decker_json
    npc_sec_code = state.get("host_security_code")
    if npc_sec_code is not None:
        npc_sec_value = state["host_security_value"]
        max_npc_passes = 1
        for _ic in state.get("active_ic", []):
            if _ic.get("status") == "active":
                max_npc_passes = max(max_npc_passes, _ic_passes(_ic))
        for _enemy in state.get("enemy_deckers", []):
            if _enemy.get("status") == "active":
                max_npc_passes = max(max_npc_passes, _enemy_passes(_enemy))
        for _p in range(state.get("current_pass", 1), max_npc_passes + 1):
            if state.get("run_ended"):
                break
            state["current_pass"] = _p
            _check_and_activate_sheaf(state, npc_sec_code)
            _advance_npc_pass(
                state, npc_decker, run,
                eff=_get_decker_effective(npc_decker, state),
                sec_code=npc_sec_code, sec_value=npc_sec_value,
                det_factor=_effective_detection_factor(state, npc_decker),
                logon_completed=False,
            )
        if state.get("run_ended"):
            # A flushed hostile pass killed the decker -- end the run here; do NOT advance the turn.
            run.status = state.get("end_reason", "crashed")
            if state.get("active_download"):
                _corrupt_active_download(state)
            run.state_json = state
            await db.commit()
            await db.refresh(run)
            return _serialize_run(run, auth)

    hackingPool_total = state.get("hackingPool_total", 0)
    old_hp = state.get("hackingPool_remaining", hackingPool_total)
    state["hackingPool_remaining"] = hackingPool_total
    state["current_turn"] = state.get("current_turn", 1) + 1
    # Initiative is rolled ONCE per cybercombat encounter (not per Combat Turn). A new turn
    # just refreshes the action budget and lets every actor act again on its FIXED passes;
    # clear the per-pass "acted" markers so NPCs act again this turn.
    # Wounds reduce initiative (rolled once per encounter): re-derive the decker's action passes
    # from the raw initiative minus the CURRENT cumulative wound penalty.
    state["initiative_passes"] = _init_passes(
        state.get("decker_initiative", 0) - _decker_wound_mod(state))
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

    # Combat maneuver: expire any Evade Detection windows whose re-detect turn has arrived
    # (lazy re-detect also runs whenever an evaded icon is consulted mid-turn via _evade_active).
    _sweep_evade_expiry(state)

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

    # Persistent Worm infections attack the deck's MPCP once each Combat Turn (vr2). App-as-GM --
    # the carried Disinfect utility defends automatically inside _resolve_lurking_worm; no human GM
    # triggers it. An infected Worm is consumed; a failed one stays lurking to retry next turn.
    for _worm in list(state.get("lurking_ic", [])):
        if state.get("run_ended"):
            break
        if _worm.get("type") == "Worm" and _worm.get("status", "lurking") == "lurking":
            _resolve_lurking_worm(state, decker, _worm)

    # Multi-turn Download Data (vr2 ongoing operation): each turn a background transfer runs, the
    # deck auto-performs a Null Operation (Control System Test) while it waits -- its tally rises
    # like any op and can wake the sheaf. When the final turn elapses the file lands on the deck
    # (storage charged); until then the decker had only Free actions.
    _dl = state.get("active_download")
    if _dl and not state.get("run_ended"):
        _tick_active_download(state, decker, _dl)

    # End-of-turn Crash Host processing: host abort roll + countdown decrement / resolution.
    _process_crash_countdown(state)

    # A completed Crash Host ends the run as a clean exit (treated like a graceful logoff).
    if state.get("run_ended"):
        run.status = "escaped" if state.get("end_reason") == "host_crashed" else state.get("end_reason", "crashed")
    # A transfer still running when the run ends this turn (host crash, etc.) is corrupted (vr2).
    if state.get("run_ended") and state.get("active_download"):
        _corrupt_active_download(state)

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


def _resolve_lurking_worm(state: dict, decker: dict, lurking: dict) -> None:
    """Resolve one lurking Worm's infection attempt against the deck's MPCP (vr2).

    The CARRIED Disinfect utility defends automatically (a running Disinfect raises the Worm
    Infection Test target number) -- read from the decker's load-out, never a GM-typed value, so a
    decker who actually loaded Disinfect defends and one who did not stays at +0. On infection the
    MPCP is permanently corrupted (chip replacement required) and the Worm is consumed; otherwise
    it stays lurking to try again next Combat Turn. Mutates ``state``; appends a ``worm_resolved``
    event. Called automatically each Combat Turn (new_turn) -- there is no human GM.
    """
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
            ic for ic in state.get("lurking_ic", []) if ic["id"] != lurking["id"]]
        _append_event(state, {
            "type": "worm_resolved", "ic_id": lurking["id"], "ic_type": "Worm",
            "outcome": "mpcp_infected", "roll": wr["roll"],
            "description": (
                f"Worm-{lurking['rating']} infected the MPCP -- chip replacement required "
                f"(permanent). Carried Disinfect-{disinfect_rating} failed."
            ),
        })
    else:
        _append_event(state, {
            "type": "worm_resolved", "ic_id": lurking["id"], "ic_type": "Worm",
            "outcome": "repelled", "roll": wr["roll"],
            "description": (
                f"Worm-{lurking['rating']} repelled by carried Disinfect-{disinfect_rating}. "
                f"Worm still lurking."
            ),
        })


def _resolve_lurking_tar(state: dict, decker: dict, lurking: dict,
                         utility_name: str, utility_rating: int) -> None:
    """Resolve one lurking Tar Baby / Tar Pit against the utility the decker just ran (vr2).

    An opposed test, utility rating vs IC. If the IC wins, both it and the utility crash (a Tar Pit
    additionally corrupts EVERY copy of the utility, and a One-Shot copy is wiped from the deck);
    if the utility wins, the tar stays lurking to trigger on the next utility use. Mutates
    ``state``; appends a ``reactive_ic_resolved`` (and possibly ``tar_pit_corruption``) event.
    Called automatically on utility use (perform_action) -- there is no human GM.
    """
    is_tar_pit = lurking["type"] == "Tar Pit"
    result = eng.tar_baby_test(
        ic_rating=lurking["rating"],
        utility_rating=utility_rating,
        is_tar_pit=is_tar_pit,
        mpcp_rating=decker.get("mpcp", 1),
        hardening=decker.get("hardening", 0),
    )

    if result["ic_wins"]:
        state["lurking_ic"] = [
            ic for ic in state.get("lurking_ic", []) if ic["id"] != lurking["id"]
        ]
        _append_event(state, {
            "type": "reactive_ic_resolved",
            "ic_id": lurking["id"],
            "ic_type": lurking["type"],
            "outcome": "ic_wins",
            "ic_roll": result["ic_roll"],
            "util_roll": result["util_roll"],
            "description": (
                f"{lurking['type']}-{lurking['rating']} triggered vs "
                f"{utility_name}-{utility_rating}. "
                f"IC wins -- {utility_name} and {lurking['type']} both crash."
            ),
        })
        if is_tar_pit and result.get("all_copies_corrupted"):
            _append_event(state, {
                "type": "tar_pit_corruption",
                "description": f"Tar Pit: ALL copies of {utility_name} corrupted.",
                "tar_pit_roll": result.get("tar_pit_roll"),
            })
        # If the crashed utility was a One-Shot copy, the tar wipes EVERY copy on the deck
        # (vr2_rules.md L1667) -- it can never be reloaded this run. No-op for a normal program.
        _wipe_one_shot(state, decker, utility_name)
    else:
        _append_event(state, {
            "type": "reactive_ic_resolved",
            "ic_id": lurking["id"],
            "ic_type": lurking["type"],
            "outcome": "util_wins",
            "ic_roll": result["ic_roll"],
            "util_roll": result["util_roll"],
            "description": (
                f"{lurking['type']}-{lurking['rating']} triggered vs "
                f"{utility_name}-{utility_rating}. "
                f"Utility wins -- {lurking['type']} remains lurking."
            ),
        })


@router.post("/{run_id}/resolve-reactive", response_model=MatrixRunRead,
             dependencies=[Depends(get_admin_token)])
async def resolve_reactive_ic(
    run_id: int,
    body: RunReactiveInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """TEST HARNESS (admin-only) -- deterministically trigger a lurking Tar Baby / Tar Pit / Worm.

    There is no human GM: lurking ambush IC now fire AUTOMATICALLY -- Tar Baby / Tar Pit on utility
    use (perform_action) and Worm each Combat Turn (new_turn). This endpoint remains ONLY so the
    reactive-IC resolution can be triggered on demand with known inputs while we validate that
    auto-fire behaves correctly in play. MARK FOR DELETION once auto-fire is confirmed satisfactory.
    """
    run = await _get_run_or_404(db, run_id)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state  = copy.deepcopy(run.state_json)
    decker = run.decker_json

    lurking = next(
        (ic for ic in state.get("lurking_ic", []) if ic["id"] == body.ic_id),
        None,
    )
    if not lurking:
        raise HTTPException(404, f"Lurking IC {body.ic_id} not found")

    if lurking["type"] == "Worm":
        _resolve_lurking_worm(state, decker, lurking)
    else:
        _resolve_lurking_tar(state, decker, lurking, body.utility_name, body.utility_rating)

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
    # Combat maneuver: an enemy that has lost/hidden from the PC (Evade Detection) does not attack.
    # Relaxed for the wounded-AI hide-heal loop: a HIDDEN Medic-carrier keeps healing its own icon
    # while it lurks (healing is not an attack, so it does not break the hide), then re-engages once
    # patched up. Any other hidden decker simply stays dark this pass. The hidden window auto-expires
    # (timer / security tally) inside _evade_active, which re-detects it back into view.
    if _evade_active(state, enemy):
        if _enemy_carries_medic(enemy):
            ecm = enemy.setdefault("condition_monitor", {})
            boxes = int(ecm.get("persona_boxes", 0) or 0)
            if boxes <= _ENEMY_REENGAGE_BOXES:
                _clear_evade(state, enemy, redetected=False)
                enemy["revealed"] = True   # back in the open -- the PC can Strike Back at it again
                _append_event(state, {
                    "type": "enemy_decker", "outcome": "reengage", "enemy_id": enemy.get("id"),
                    "gm_only": True,
                    "description": (
                        f"GM: {enemy.get('name', 'Security decker')} has patched its icon to "
                        f"{boxes}/10 and drops its hide to resume the hunt."
                    ),
                })
                return
            _enemy_medic_heal(state, enemy)
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
    # Wounded-decker AI (spec section 3.2): a graduated self-preservation model that replaces the
    # old hard 7-box flee. Runs BEFORE _npc_maybe_maneuver so the shared maneuver's boxes>=7 Evade
    # branch stays IC-only for deckers (a healless decker gains nothing by hiding).
    ecm = enemy.setdefault("condition_monitor", {})
    boxes = int(ecm.get("persona_boxes", 0) or 0)
    if boxes >= 10:
        # Icon crashing -> forced out (not a choice). (Normally the PC's Strike Back crashes it
        # first; this is a defensive backstop for an enemy that reaches 10 on its own turn.)
        enemy["status"] = "fled"
        _append_event(state, {
            "type": "enemy_decker", "outcome": "fled", "enemy_id": enemy["id"],
            "description": (
                f"{enemy['name']}'s icon is crashing ({boxes}/10) -- it is dumped from the host."
            ),
        })
        return
    # Escalating nerve check at 7/8/9 boxes (once per newly-reached threshold; bravery softens it).
    if _enemy_nerve_check(state, enemy, boxes):
        return   # nerve broke -> jacked out (the helper set status="fled" + logged it)
    # Held its nerve but hurt: a Medic-carrier (Red/Black) tactically breaks contact to heal --
    # Evade Detection now, then heal while hidden (top-of-function loop) and re-engage once patched.
    if boxes >= _ENEMY_WOUNDED_BOXES and _enemy_carries_medic(enemy):
        _resolve_npc_maneuver(state, decker, eff, enemy, "evade_detection", is_ic=False)
        return
    # Combat maneuver: the enemy may spend its action to maneuver against you instead of attacking
    # (heuristic; only when npc_combat_maneuvers is set).
    if _npc_maybe_maneuver(state, decker, eff, enemy, is_ic=False):
        if not state.get("run_ended"):
            state["detection_factor"] = _effective_detection_factor(state, decker)
        return
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

    util_map = enemy.get("utilities") or {}
    attack_rating = util_map.get("attack", 4)
    is_lethal = program in ("Black Hammer", "Killjoy")
    # Each program uses its OWN carried rating (falling back to the Attack rating for a legacy
    # enemy that only stored Attack): lethal -> lethal_rating; Hog / cripplers -> their utility.
    if is_lethal:
        power = enemy.get("lethal_rating", 0)
    elif program == "Hog":
        power = util_map.get("hog", attack_rating)
    elif program in ("Poison", "Restrict", "Reveal"):
        power = util_map.get(program.lower(), attack_rating)
    else:  # Attack
        power = attack_rating
    pool = power + hacking_pool
    did_icon_damage = False

    if program == "Hog":
        hog = eng.hog_attack(
            attacker_pool=pool, security_code=sec_code, target_status="intruding",
            hog_rating=power, mpcp_rating=decker.get("mpcp", 4),
            hardening=decker.get("hardening", 0), tn_modifier=_enemy_wound_mod(enemy))
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
        # Combat maneuver: Parry (raises the enemy's TN) / Position (held by the enemy) delta.
        atk_tn_delta, _atk_power_delta = _consume_attack_mods_vs_pc(state, enemy)
        cr = eng.decker_attribute_attack(
            attacker_pool=pool, security_code=sec_code, target_status="intruding",
            program_rating=power, target_attribute_rating=eff[attr],
            shield_successes=shield_succ, tn_modifier=atk_tn_delta + _enemy_wound_mod(enemy))
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
        # Combat maneuver: Parry (raises the enemy's TN) + Position (held by the enemy: -TN / +Power).
        atk_tn_delta, atk_power_delta = _consume_attack_mods_vs_pc(state, enemy)
        atk = eng.cybercombat_attack(
            attacker_pool=pool, security_code=sec_code, target_status="intruding",
            target_bod=eff["bod"], armor_rating=(decker.get("utilities") or {}).get("armor", 0),
            ic_rating=power + atk_power_delta, attacker_is_ic=True,
            tn_modifier=atk_tn_delta + _enemy_wound_mod(enemy),
            shield_successes=shield_succ)
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
            if program == "Killjoy":
                # Killjoy (non-lethal black IC): meat damage is Physical STUN (overflows to physical).
                _add_stun(cm, bio["boxes"])
                meat_kind, meat_val = "Stun", cm["stun_boxes"]
                meat_full = cm["stun_boxes"] >= 10
            else:
                # Black Hammer (lethal black IC): meat damage is Physical DAMAGE.
                cm["physical_boxes"] = cm.get("physical_boxes", 0) + bio["boxes"]
                meat_kind, meat_val = "Physical", cm["physical_boxes"]
                meat_full = cm["physical_boxes"] >= 10
            desc = (f"{program.upper()} -- {enemy['name']} drives lethal biofeedback into you: "
                    f"icon {atk['resistance']['final_damage_level']} ({boxes}), {meat_kind} "
                    f"{bio['final_damage_level']} ({bio['boxes']}). "
                    f"Persona {cm['persona_boxes']}/10, {meat_kind} {meat_val}/10.")
            if meat_full:
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
        shock = "immune" if ds.get("immune") else f"{ds['boxes']} stun boxes"
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
    # Combat maneuver: the enemy's Parry (raises the PC's to-hit TN) + the PC's own Position
    # (lowers the TN and/or raises Power). Consumed by this single attack (exactly one of the
    # branches below runs, so it is read once here).
    tgt_tn_delta, tgt_power_delta = _consume_attack_mods_vs_target(state, enemy)

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
        # The enemy parries with its Shield utility (if loaded): its net successes ADD to the
        # enemy's side of the opposed crippler test, raising the bar the PC must clear.
        e_shield = _enemy_shield_parry(
            state, enemy, attacker_skill=int(decker.get("computer_skill", 1) or 1),
            context=body.program)
        cr = eng.decker_attribute_attack(
            attacker_pool=pool, security_code=sec_code, target_status="intruding",
            program_rating=program_rating, target_attribute_rating=target_rating,
            shield_successes=e_shield,
            tn_modifier=tgt_tn_delta + _decker_wound_mod(state),
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
        attack_tn = max(2, rules.COMBAT_TN[sec_code]["intruding"] + tgt_tn_delta + _decker_wound_mod(state))
        attack_roll = eng.roll_dice(pool, attack_tn)
        # The enemy parries the lethal hit with its Shield utility (if loaded): its net successes
        # SUBTRACT from the PC's attack successes before the icon-damage resistance stages.
        e_shield = _enemy_shield_parry(
            state, enemy, attacker_skill=int(decker.get("computer_skill", 1) or 1),
            context=program)
        resist = eng.damage_resistance(
            bod=target_bod, power=rating + tgt_power_delta, base_damage_level=_LETHAL_BASE_LEVEL,
            armor_rating=_enemy_armor(enemy),
            attacker_successes=attack_roll["successes"],
            shield_successes=e_shield,
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

    # Limit option (vr2): an Attack utility Limited to IC is useless against an enemy decker.
    if (((decker.get("program_options") or {}).get("attack") or {}).get("limit_target")) == "ic":
        raise HTTPException(400, "This Attack utility is Limited to IC -- it cannot target enemy deckers.")
    # Plain Attack (default) -- crash the enemy icon. The enemy resists EXACTLY like the PC
    # decker: Bod dice vs Power, with its Armor utility (if loaded) reducing that Power, and its
    # Shield utility (if loaded) parrying successes off the incoming hit.
    e_shield = _enemy_shield_parry(
        state, enemy, attacker_skill=int(decker.get("computer_skill", 1) or 1), context="attack")
    atk = eng.cybercombat_attack(
        attacker_pool=pool, security_code=sec_code, target_status="intruding",
        target_bod=enemy["bod"], armor_rating=_enemy_armor(enemy),
        ic_rating=util.get("attack", 4) + tgt_power_delta, attacker_is_ic=False,
        tn_modifier=tgt_tn_delta + _decker_wound_mod(state),
        shield_successes=e_shield,
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


@router.post("/{run_id}/area-attack", response_model=MatrixRunRead)
async def area_attack(
    run_id: int,
    body: RunAreaAttackInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """One Area-option Attack burst against several icons at once (vr2 Area utility).

    The Attack utility's Area rating caps how many icons a single burst can engage. ``target_ids``
    mixes active IC and revealed enemy deckers. ONE Attack Test is made; per vr2 the to-hit TN
    rises by the number of targets, and the Area option BYPASSES a Party-IC cluster's to-hit
    penalty entirely. Each target then resists INDIVIDUALLY with its own mechanic -- IC with
    Security Value vs the combat TN, enemy deckers with Bod (exactly like the PC). Any target
    carrying Armor gets +2 effective Armor against an Area strike. With a single target the burst
    collapses to a plain Attack (no Area penalty, no Area armor bonus) -- identical to a non-Area
    utility.
    """
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

    atk_opts   = (decker.get("program_options") or {}).get("attack") or {}
    opt_pen    = bool(atk_opts.get("penetration"))
    opt_chaser = bool(atk_opts.get("chaser"))
    opt_target = bool(atk_opts.get("targeting"))
    opt_skulk  = max(0, int(atk_opts.get("skulk", 0) or 0))
    opt_area   = max(0, int(atk_opts.get("area", 0) or 0))
    if opt_area < 1:
        raise HTTPException(400, "This Attack utility has no Area option.")
    limit_target = (atk_opts.get("limit_target") or "")

    # Resolve every target id to an active IC or a revealed, active enemy decker. Order is
    # preserved from the request. An unknown / dead / hidden id is a hard error (nothing is
    # spent yet).
    active_ic = {ic["id"]: ic for ic in state.get("active_ic", [])
                 if isinstance(ic, dict) and ic.get("status") == "active"}
    enemies = {e["id"]: e for e in state.get("enemy_deckers", [])
               if isinstance(e, dict) and e.get("status") == "active" and e.get("revealed")}
    targets: list[tuple[str, dict]] = []
    for tid in body.target_ids:
        if tid in active_ic:
            if limit_target == "decker":
                raise HTTPException(400, "This Attack utility is Limited to deckers -- it cannot target IC.")
            targets.append(("ic", active_ic[tid]))
        elif tid in enemies:
            if limit_target == "ic":
                raise HTTPException(400, "This Attack utility is Limited to IC -- it cannot target enemy deckers.")
            targets.append(("enemy", enemies[tid]))
        else:
            raise HTTPException(404, f"Target {tid} not found, crashed, or not a valid Area target")

    n_targets = len(targets)
    if n_targets > opt_area:
        raise HTTPException(400, f"Area rating {opt_area} can engage at most {opt_area} target(s); {n_targets} selected.")
    # A single target collapses to a plain attack: no Area to-hit penalty, no Area armor bonus.
    is_burst = n_targets >= 2
    area_penalty = n_targets if is_burst else 0

    _one_shot_block(state, decker, "attack")   # a spent One-Shot Attack cannot fire again until reloaded
    _spend_pass_action(state, "attack")        # vr2: one cybercombat attack (burst) is a Simple Action
    _spend_hp(state, body.hacking_pool_dice)
    attack_pool = body.attack_pool + body.hacking_pool_dice
    base_tn = rules.COMBAT_TN[sec_code]["intruding"]
    wound_mod = _decker_wound_mod(state)
    base_dmg = rules.IC_DAMAGE_LEVEL[sec_code]
    attack_util_rating = int((decker.get("utilities") or {}).get("attack", 4) or 4)

    # Pre-compute each target's individual to-hit TN and consume its per-target combat maneuvers
    # (Parry/Position) BEFORE the single shared Attack Test. Area bypasses the Party-IC cluster
    # penalty entirely, so clustered IC contribute 0 to-hit penalty on a real burst.
    plans: list[dict] = []
    for kind, obj in targets:
        tgt_tn_delta, tgt_power_delta = _consume_attack_mods_vs_target(state, obj)
        if kind == "ic":
            cluster = 0 if is_burst else _cluster_size(state, obj.get("cluster_id"))
            shield_shift = _shield_shift_tn_modifier(obj, penetration=opt_pen, chaser=opt_chaser)
            tn = base_tn + cluster + shield_shift + tgt_tn_delta + wound_mod + area_penalty
        else:
            cluster = 0
            tn = base_tn + tgt_tn_delta + wound_mod + area_penalty
        if opt_target:
            tn -= 2                    # Targeting option: -2 to-hit TN
        tn = max(2, tn)
        plans.append({"kind": kind, "obj": obj, "tn": tn,
                      "power_delta": tgt_power_delta, "cluster": cluster})

    # ONE Attack Test (vr2 Area: "make one Attack Test and apply the result to all targets").
    # Roll at the HIGHEST target TN so the rule-of-6 explosions are fully accumulated, then count
    # each target's successes from the SAME dice against its own TN (shield/shift stay per-target).
    roll_tn = max(p["tn"] for p in plans)
    attack_roll = eng.roll_dice(attack_pool, roll_tn)

    results: list[dict] = []
    for p in plans:
        kind, obj, tn = p["kind"], p["obj"], p["tn"]
        succ = sum(1 for d in attack_roll["dice"] if d >= tn)
        if kind == "ic":
            # IC resists with Security Value vs the combat TN; Armor lowers that Power (and is +2
            # more effective vs an Area burst); Expert trades resist dice.
            resist_tn = base_tn + p["cluster"] + p["power_delta"]
            if _ic_has_armor(obj):
                resist_tn = max(2, resist_tn - 2 - (2 if is_burst else 0))
            resist_pool = max(1, sec_value + _ic_expert(obj, "defense") - _ic_expert(obj, "offense"))
            resist_roll = eng.roll_dice(resist_pool, resist_tn)
            staged = eng.stage_damage(base_dmg, succ, 1)
            final_dmg = eng.stage_damage(staged, resist_roll["successes"], -1)
            boxes = rules.DAMAGE_BOXES[final_dmg]
            obj["boxes"] = obj.get("boxes", 0) + boxes
            crashed = obj["boxes"] >= 10
            results.append({"kind": "ic", "id": obj["id"],
                            "label": f"{obj['type']}-{obj['rating']}",
                            "boxes": boxes, "final": final_dmg,
                            "total": obj["boxes"], "crashed": crashed})
            if crashed:
                _apply_ic_crash(state, obj, sec_code, opt_skulk)
        else:
            # Enemy decker resists EXACTLY like the PC: Bod dice vs Power, its Armor utility (if
            # loaded) reducing that Power and gaining +2 more vs an Area burst.
            earmor = _enemy_armor(obj)
            if earmor > 0 and is_burst:
                earmor += 2
            resist = eng.damage_resistance(
                bod=obj["bod"], power=attack_util_rating + p["power_delta"],
                armor_rating=earmor, base_damage_level=base_dmg,
                attacker_successes=succ,
            )
            boxes = resist["boxes"]
            ecm = obj.setdefault("condition_monitor", {})
            ecm["persona_boxes"] = ecm.get("persona_boxes", 0) + boxes
            crashed = ecm["persona_boxes"] >= 10
            if crashed:
                obj["status"] = "crashed"
            results.append({"kind": "enemy", "id": obj["id"],
                            "label": obj.get("name", "enemy decker"),
                            "boxes": boxes, "final": resist["final_damage_level"],
                            "total": ecm["persona_boxes"], "crashed": crashed})

    crashed_n = sum(1 for r in results if r["crashed"])
    if is_burst:
        head = (f"AREA STRIKE ({attack_roll['successes']} successes) hits {n_targets} icons "
                f"[+{area_penalty} to-hit]")
    else:
        head = f"Attack ({attack_roll['successes']} successes)"
    parts = [f"{r['label']} {r['final']} ({r['boxes']}b{'; CRASHED' if r['crashed'] else ''})"
             for r in results]
    desc = f"{head}: " + "; ".join(parts) + f". {crashed_n} crashed." if parts else head
    _append_event(state, {
        "type": "area_attack",
        "n_targets": n_targets,
        "area_penalty": area_penalty,
        "attack_roll": attack_roll,
        "results": results,
        "crashed": crashed_n,
        "description": desc,
    })

    _spend_one_shot(state, decker, "attack")
    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


@router.post("/{run_id}/suppress", response_model=MatrixRunRead)
async def suppress_ic(
    run_id: int,
    body: RunSuppressInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Suppress or release a crashed OR hung IC (vr2 Suppression + Slow L1578).

    Suppression is declared the MOMENT the IC is neutralized -- a fresh crash (crashing added its
    rating to the tally) or a Slow HANG (Slow adds no tally). The decker absorbs 1 Detection Factor
    (applied live by _effective_detection_factor) to defer/refund that tally. Releasing it is a Free
    Action that restores the DF and re-adds a CRASHED IC's rating to the tally (a hung IC re-adds
    nothing); a released IC stays down and can NEVER be re-suppressed. The DF cannot fall below 1.
    """
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state = copy.deepcopy(run.state_json)
    _toggle_ic_suppression(state, run.decker_json, ic_id=body.ic_id, release=body.release)

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


@router.post("/{run_id}/reveal-host-ratings", response_model=MatrixRunRead)
async def reveal_host_ratings(
    run_id: int,
    body: RunRevealHostRatingsInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Phase two of Analyze Host (vr2 override): spend banked Analyze Host credits by choosing which
    still-hidden ACIFS subsystem ratings to reveal.

    When a successful Analyze Host rolled fewer net successes than there were hidden ratings,
    ``_apply_analyze_host`` banks ``host_analyze_pending`` and reveals nothing. The decker then
    calls this endpoint with the chosen subsystems (one per banked credit). ``_reveal_host_ratings``
    validates the picks, reveals them from the GM-only ACIFS ratings, and clears the pending.
    """
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state = copy.deepcopy(run.state_json)
    _reveal_host_ratings(state, body.subsystems)

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
            f"({ds.get('boxes', 0)} boxes stun)."
        ),
        "dump_shock": ds,
    })

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)
