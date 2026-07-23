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
from typing import Any, Callable

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.auth.core import hash_token
from app.auth.dependencies import get_admin_token, get_any_token
from app.auth.rate_limit import enforce_call_rate
from app.models.matrix_run import MatrixRun
from app.models.matrix_host import MatrixHost
from app.models.character import Character
from app.schemas.matrix_run import (
    MatrixRunCreate, MatrixRunRead, MatrixRunSummary, MatrixRunAAR,
    RunActionInput, RunAttackInput, RunDefendInput, RunLogoffInput, RunReactiveInput,
    RunSuppressInput, RunRevealHostRatingsInput, RunEnemyAttackInput,
    RunEnemyScanInput, RunAreaAttackInput,
    RunTrapDoorInput, SheaveSaveInput, SheafGenerateInput,
)
from app.services import matrix_engine as eng
from app.services import matrix_rules as rules
from app.services import run_trace
from app.services.host_visibility import (
    sync_host_reveal_to_org, sync_host_security_to_org,
)

router = APIRouter()


async def trace_action(request: Request, run_id: int):
    """Opt-in per-action engine trace (``SR_TRACE`` env flag). Starts a computation-trace buffer
    for this request and, once the action resolves (or is refused), flushes the collected engine
    steps to ``data/traces/run_<id>.log`` for developer / GM observability. A no-op unless
    ``SR_TRACE`` is set, so normal play and the test suite are unaffected."""
    run_trace.start()
    try:
        yield
    finally:
        lines = run_trace.collect()
        if lines:
            run_trace.flush_run(run_id, f"{request.method} {request.url.path}", lines)


# State keys removed entirely from state_json when serving a non-admin.
# (Admin sees the full state.) lurking_ic is GM-only: reactive IC "lurks
# silently" by the rules, so players must not see it exists at all.
_GM_ONLY_STATE_KEYS = {"sheaf", "host_acifs", "lurking_ic", "scrambles", "paydata", "data_bombs",
                       "trap_doors", "enemy_decker_cap", "shutdown_countdown", "_acting_init",
                       "host_stack", "_stack_current_host_name", "excluded_handles"}

# Trap-door host stack (B34): a decker who enters a discovered trap door does NOT log off -- the
# current host is SUSPENDED and pushed onto ``state["host_stack"]`` while a fresh session opens on
# the destination host (same run row, run.host_id retargeted). A graceful logoff or a host crash on
# the deeper host POPS back to the suspended parent instead of ending the run; a dump / death / KO
# on ANY host ends the whole run (the single row -- and thus the entire stack -- goes down together).
# Practical depth cap so a pathological chain can't balloon the state blob.
HOST_STACK_CAP = 10

# Persona-scoped state that stays CONTINUOUS across the stack: it belongs to the decker/deck, not
# the host, so it is carried forward on entry and back on return (icon/deck damage, MPCP infections,
# hacking-pool spend, deck storage ledger + downloaded loot, memory config, detection factor). Every
# OTHER key is host-scoped and is snapshot/restored with the host frame.
_PERSONA_CARRY_KEYS = {
    "condition_monitor", "mpcp_infections", "mpcp_infected", "chip_replacement_required",
    "hackingPool_total", "hackingPool_remaining", "storage_free_mp", "storage_used_mp",
    "downloaded_files", "storage_programs", "active_memory_cap", "program_sizes",
    "squeeze_keys", "squeezed_active",
    "detection_factor", "interactive_defense",
}

# Single source of truth for the attribute-crippling family. Each persona attribute maps to the
# decker PROGRAM that attacks it (Poison/Restrict/Reveal) and to the crippler / ripper IC that
# attacks it (Acid/Binder/Marker + *-rip). Jammer -> Sensor is IC-ONLY: no decker program targets
# Sensor in vr2, so its "program" is None (a rules-correct asymmetry, not a gap). The dice math
# lives once in eng.attribute_attack_core and the state application once in
# _resolve_attribute_attack -- only the per-actor LABELS differ (IC = Acid/Binder/Marker/Jammer,
# decker = Poison/Restrict/Reveal). The two lookup maps below are DERIVED so they cannot drift.
_ATTRIBUTE_ATTACK: dict[str, dict[str, str | None]] = {
    "bod":     {"program": "poison",   "ic": "Acid",   "ripper": "Acid-rip"},
    "evasion": {"program": "restrict", "ic": "Binder", "ripper": "Bind-rip"},
    "masking": {"program": "reveal",   "ic": "Marker", "ripper": "Mark-rip"},
    "sensor":  {"program": None,       "ic": "Jammer", "ripper": "Jam-rip"},
}
# Derived: crippler/ripper IC type name -> the decker attribute it attacks.
_CRIPPLER_TARGET: dict[str, str] = {
    name: attr
    for attr, m in _ATTRIBUTE_ATTACK.items()
    for name in (m["ic"], m["ripper"]) if name
}
# Derived: decker program (poison/restrict/reveal) -> the persona attribute it attacks.
_PROGRAM_ATTR: dict[str, str] = {
    m["program"]: attr for attr, m in _ATTRIBUTE_ATTACK.items() if m["program"]
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
_TALLY_CLAUSE_RE = re.compile(r"\s*[Tt]ally \+(\d+) -> \d+\.?")


def _tally_clause_generic(m: "re.Match[str]") -> str:
    """Replace a raw "Tally +N -> M" clause with a number-free player signal: a positive increase
    becomes "Security tally increased." (the decker knows the system noticed, not by how much);
    a +0 clause is dropped entirely."""
    return " Security tally increased." if int(m.group(1)) > 0 else ""

# Operation-test descriptions read "(<decker successes> vs <host successes>[ successes])". The
# HOST success count equals the tally increase the decker is not supposed to know (see above), so
# collapse it to the decker's own successes. Only applied to tally-bearing events (see below), so
# cybercombat "X vs Y" lines are untouched.
_VS_HOST_SUCC_RE = re.compile(r"\((\d+) vs \d+(?: successes)?\)")


def _redact_event_ic(e: dict, redact_ids: set) -> dict:
    """Mask an un-identified IC's name in a player-facing event.

    An active IC the decker has not analysed past presence (detection level < 2) reads as
    'Unknown IC' in the log, matching its redacted chip -- so activation / attack lines never
    disclose the IC's type or rating before an Analyze IC identifies it.
    """
    if not isinstance(e, dict):
        return e
    ic_id = e.get("ic_id")
    ic_type = e.get("ic_type")
    if not ic_id or ic_id not in redact_ids or not ic_type:
        return e
    out = dict(e)
    rating = out.get("ic_rating")
    desc = out.get("description")
    if isinstance(desc, str):
        variants = []
        if rating not in (None, ""):
            variants += [f"{ic_type}-{rating}", f"{ic_type} Rating {rating}"]
        variants.append(ic_type)
        for v in variants:
            desc = desc.replace(v, "Unknown IC")
        out["description"] = desc
    out["ic_type"] = "Unknown IC"
    out.pop("ic_rating", None)
    return out


def _redact_event_tally(e: dict) -> dict:
    """Return a player-safe copy of an event with the running security tally removed.

    The decker learns its tally only via Analyze Security, so every tally-equivalent signal is
    stripped for non-admins: the structured ``tally_increase`` / ``tally_total`` fields, the
    ``host_roll`` (the host's security successes ARE the tally increase), the "Tally +N -> M"
    clause, and the host half of the "(X vs Y successes)" summary.
    """
    if not isinstance(e, dict):
        return e
    out = dict(e)
    had_tally = ("tally_increase" in out) or ("tally_total" in out)
    inc = out.get("tally_increase")
    out.pop("tally_increase", None)
    out.pop("tally_total", None)
    if had_tally:
        # The host security roll (dice + successes) reveals the tally delta; the decker knows its
        # own Detection Factor, so even the raw dice would let it back out the successes.
        out.pop("host_roll", None)
    desc = out.get("description")
    if isinstance(desc, str):
        scrubbed = _TALLY_CLAUSE_RE.sub(_tally_clause_generic, desc)
        if had_tally:
            scrubbed = _VS_HOST_SUCC_RE.sub(r"(\1 successes)", scrubbed)
            # Global generic signal: if the event raised the tally but its text had no "Tally +N"
            # clause to convert, still tell the player the system took notice (without the number).
            if (isinstance(inc, int) and inc > 0
                    and "Security tally increased" not in scrubbed):
                scrubbed = (scrubbed.rstrip() + " Security tally increased.").strip()
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
    # ``view_as_player`` lets an admin preview the EXACT player payload (UI runner view): redact
    # exactly as for a real non-admin so no GM-only state ever reaches the browser in that mode.
    if not auth.get("is_admin") or auth.get("view_as_player"):
        state = dict(data.get("state_json") or {})
        # Surface only the paydata the decker has actually LOCATED (name/size/key/downloaded) so
        # the player can make storage decisions; the full GM paydata list is then redacted below.
        located_paydata = [
            {"name": p.get("name"),
             "size_mp": max(0, int(p.get("density", 0) or 0)),
             "is_key": bool(p.get("is_key")),
             "downloaded": bool(p.get("downloaded")),
             "destroyed": bool(p.get("destroyed")),
             "tampered": bool(p.get("tampered"))}
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
        # Reveal only tar IC (Tar Baby / Tar Pit) whose ambush was blown (revealed=True) so the
        # decker can target and Steamroller them; every other lurking IC stays fully GM-only.
        revealed_tars = [
            {"id": ic.get("id"), "type": ic.get("type"), "rating": ic.get("rating"),
             "status": ic.get("status", "lurking"), "revealed": True}
            for ic in (state.get("lurking_ic") or [])
            if isinstance(ic, dict) and ic.get("revealed")
            and ic.get("type") in ("Tar Baby", "Tar Pit")
        ]
        # How many hosts are suspended below this one on the trap-door stack (B34). The player
        # sees the DEPTH (so the UI can show "2 hosts deep") without the GM-only suspended frames.
        state["host_stack_depth"] = len(state.get("host_stack") or [])
        for k in _GM_ONLY_STATE_KEYS:
            state.pop(k, None)
        if revealed_tars:
            state["revealed_lurking_ic"] = revealed_tars
        state["located_paydata"] = located_paydata
        state["discovered_trap_doors"] = discovered_trap_doors
        state["discovered_data_bombs"] = discovered_data_bombs
        state["discovered_scrambles"] = discovered_scrambles
        # Slave device icons are perceptible only once the decker is INSIDE the host; before logon
        # the run reveals nothing about the interior, so keep the scan-target list empty until then.
        if not state.get("logon_complete"):
            state["slave_devices"] = []
        # The current host's LTG-access status is unknown to the decker until a successful
        # Analyze Subsystem on Access reveals it (host_ltg_revealed). Hide both the yes/no flag
        # and the actual grid address until then.
        if not state.get("host_ltg_revealed"):
            state.pop("host_has_ltg", None)
            state.pop("host_ltg_address", None)
        # The host Security Rating (code + value) is a mystery for every host until Analyze Host
        # reveals it (host_security_revealed). Redact both until then.
        if not state.get("host_security_revealed"):
            state.pop("host_security_code", None)
            state.pop("host_security_value", None)
        # A pending interactive-defense prompt keeps an internal ``ctx`` (host Security code/value +
        # attack modifiers) that only /defend needs to resolve the parked strike. The player must
        # see the prompt itself -- attacker, successes, Power, Hacking Pool available -- but NOT that
        # ctx, which would leak the still-secret host Security Rating. Strip it to display fields.
        pend = state.get("pending_defense")
        if isinstance(pend, dict):
            state["pending_defense"] = {
                k: v for k, v in pend.items()
                if k not in ("ctx", "resume_logon_completed")
            }
        if isinstance(state.get("active_ic"), list):
            redacted = [_redact_ic(ic) for ic in state["active_ic"] if isinstance(ic, dict)]
            state["active_ic"] = [ic for ic in redacted if ic is not None]
        if isinstance(state.get("event_log"), list):
            # IC the decker has detected but not yet identified (detection level < 2): their name
            # must read as "Unknown IC" in the log, matching the redacted chip. active_ic is already
            # redacted above, so its detection_level fields drive which IC names to mask.
            _ic_redact_ids = {
                ic.get("id") for ic in (state.get("active_ic") or [])
                if isinstance(ic, dict) and ic.get("id") and (ic.get("detection_level") or 0) < 2
            }
            # Drop GM-only events (e.g. surreptitious reactive-IC activity the decker
            # has not yet detected) so the log never betrays a hidden IC's presence, and
            # scrub the running security tally from the survivors (the decker only learns
            # its tally via Analyze Security -- see _redact_event_tally).
            state["event_log"] = [
                _redact_event_ic(_redact_event_tally(e), _ic_redact_ids)
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


# Scan Icon (vr2 L1895): the ratings a successful scan reveals about a hostile decker, in the
# priority order the app-as-GM discloses them (1 per net success; 3+ successes reveal ALL). The
# player otherwise never sees a raw enemy rating -- _redact_enemy_decker hides them until scanned.
_SCAN_REVEAL_ORDER = ["mpcp", "bod", "evasion", "masking", "sensor", "response_increase"]
# The crippler-targetable persona attributes -> the PC-side program that attacks each. An enemy
# that has scanned the PC (see _enemy_scan_pc) focuses the weakest of these it can attack.
_ATTR_CRIPPLER = {"bod": "Poison", "evasion": "Restrict", "masking": "Reveal"}


def _enemy_name_revealed(e: dict) -> bool:
    """True once the PC has Analyzed / Scanned this enemy decker's icon (any Scan Icon net success
    latches ``name_revealed``). Until then the decker shows only the generic "Security Decker"
    identifier; afterward its street handle is disclosed (vr2 icon identification, roadmap #4)."""
    return bool(e.get("name_revealed") or int(e.get("scan_reveal", 0) or 0) > 0)


def _enemy_display_name(e: dict) -> str:
    """Player-facing identifier for an enemy decker. Generic "Security Decker" until its icon is
    Analyzed / Scanned; then "Enemy Decker (Handle)" using the revealed street handle. This is the
    name shown on the card AND used in every player-visible event/test line so the log matches what
    the decker actually knows at that moment."""
    if _enemy_name_revealed(e) and e.get("handle"):
        return f"Enemy Decker ({e['handle']})"
    return "Security Decker"


def _enemy_gm_name(e: dict) -> str:
    """GM-facing identifier for an enemy decker -- always includes the real handle (the GM sees the
    un-redacted state), e.g. "Security Decker (Redline)". Used in gm_only event lines so the GM can
    tell multiple deckers apart even before the players have scanned them."""
    handle = e.get("handle")
    return f"Security Decker ({handle})" if handle else "Security Decker"


def _redact_enemy_decker(e: dict) -> dict:
    """Player view of a revealed enemy decker -- presence + condition, not raw ratings (unless
    the PC has run Scan Icon on it, which discloses ratings in _SCAN_REVEAL_ORDER)."""
    cm = e.get("condition_monitor", {}) or {}
    name_known = _enemy_name_revealed(e)
    reveal_n = int(e.get("scan_reveal", 0) or 0)
    out = {
        "id": e.get("id"),
        "name": _enemy_display_name(e),
        "name_revealed": name_known,
        "handle": e.get("handle") if name_known else None,
        # Threat tier (Green/Orange/Red/Black rating class) is unknown until the PC runs Scan Icon.
        # Intent (kill/dump/crash) is NEVER surfaced -- a decker's plan is not knowable from outside
        # the icon; the PC only learns it once the decker acts.
        "tier": e.get("tier") if reveal_n > 0 else None,
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
    # Scan Icon reveal: disclose the first N base ratings the PC has uncovered (N latched on the
    # enemy as scan_reveal; 6 == fully scanned). Base ratings, not the live combat-damaged values.
    if reveal_n > 0:
        out["scanned"] = {k: int(e.get(k, 0) or 0) for k in _SCAN_REVEAL_ORDER[:reveal_n]}
        out["scan_level"] = min(reveal_n, len(_SCAN_REVEAL_ORDER))
    return out


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
    # Crashing an IC fully identifies it: you plainly know what you just destroyed (type + rating +
    # any options it was running). Force a full reveal regardless of prior Analyze/Sensor level.
    if ic.get("status") == "crashed":
        level = 3
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
    # Threat class (white/gray/black) is part of an IC's identity: withhold it until the type is
    # known (level >= 2), so an un-analysed IC never leaks its class through the chip badge/colour.
    if level < 2:
        out["category"] = None
    # IC Options (Expert Offense/Defense, Cascading, Shielding/Shifting, Armor) are learned only at
    # a full Analyze IC (level 3). Below that, strip them so a partial ID cannot leak the defenses.
    if level < 3:
        for k in ("options", "expert", "shield", "shift", "cascading"):
            out.pop(k, None)
    # level >= 3: full reveal
    out["detection_level"] = level
    return out


# Action cost (Free/Simple/Complex) per action_type, from the vr2 System Operations table.
# (Action-economy ENFORCEMENT -- 2 Simple OR 1 Complex + 1 Free per pass -- is the next step;
# for now this is surfaced on each action for awareness. See docs GAPS PLAN section D.)
_ACTION_COST = {op["name"].lower().replace(" ", "_"): op["action"] for op in rules.SYSTEM_OPERATIONS}
_ACTION_COST.update({
    "swap_memory": "Simple", "unload_program": "Free", "purge_hog": "Complex",
    "decrypt_file": "Simple",
    "relocate": "Simple", "redirect_datatrail": "Complex",
    "analyze_subsystem": "Simple", "analyze_icon": "Free",
    "locate_decker": "Complex",               # vr2: Index/Sensor search for a hostile decker (was defaulting)
    "attack": "Simple",                       # vr2: all cybercombat attacks are Simple Actions
    "scan_icon": "Simple",                    # vr2: Scan Icon (read a hostile decker) is a Simple Action
    "medic": "Complex", "restore": "Complex", "disinfect": "Complex",
    "defuse_data_bomb": "Complex",
    "steamroller": "Simple", "slow": "Simple", "decompress_file": "Complex",
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
        deck_mode=decker.get("deck_mode", "hot"),
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

    # Pre-placed Worm IC configured in the host designer (config_json["worms"]). A Worm booby-traps
    # a subsystem, so it lurks from the moment the decker logs on. Each carries its variant:
    #   standard  -> MPCP Infection Test only (chip burn / degradation)
    #   deathworm -> once it INFECTS the MPCP: ongoing cybercombat-TN penalty (persists across runs)
    #   tapeworm  -> once it INFECTS the MPCP: erases carried paydata at every run end
    # Infection is the GATE for every variant -- a worm does nothing until it compromises the MPCP.
    # (Dataworm is narrative-only and is not authored here.)
    lurking_worms = []
    for _w in (cfg.get("worms") or []):
        if not isinstance(_w, dict):
            continue
        variant = str(_w.get("variant", "standard") or "standard").lower()
        if variant not in ("standard", "deathworm", "tapeworm"):
            variant = "standard"
        lurking_worms.append({
            "id": f"lc_{uuid.uuid4().hex[:8]}",
            "type": "Worm",
            "variant": variant,
            "rating": int(_w.get("rating", 6) or 6),
            "subsystem": str(_w.get("target", "") or ""),
            "status": "lurking",
        })

    # Carried-forward MPCP infections from the persistent deck (client-supplied). An infection is
    # permanent until the MPCP chip is replaced, so a deck that was infected on a previous run
    # starts THIS run already compromised -- a Deathworm's cybercombat penalty and a Tapeworm's
    # paydata erasure apply from the outset. Sanitize to a small, typed list.
    carried_infections = []
    for _inf in (decker.get("mpcp_infections") or []):
        if not isinstance(_inf, dict):
            continue
        v = str(_inf.get("variant", "standard") or "standard").lower()
        if v not in ("standard", "deathworm", "tapeworm"):
            v = "standard"
        carried_infections.append({
            "variant": v,
            "rating": int(_inf.get("rating", 6) or 6),
            "ic_id": str(_inf.get("ic_id", "") or f"carried_{uuid.uuid4().hex[:6]}"),
        })

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
        "lurking_ic": lurking_worms,
        "mpcp_infections": carried_infections,
        # A deck arriving with carried infections is already compromised (chip degraded until replaced).
        "mpcp_infected": bool(carried_infections),
        "chip_replacement_required": bool(carried_infections),
        "current_turn": 1,
        "sheaf_steps_triggered": [],
        "detection_factor": det_factor,
        "host_security_code": cfg.get("security_code", "Green"),
        "host_security_value": cfg.get("security_value", 6),
        # The host Security Rating (code + value) is GM-only for EVERY host until a sufficiently
        # successful Analyze Host reveals it (host_security_code/value are redacted while this is
        # False). Keeps a host's security class a mystery until the decker jacks in and probes it.
        "host_security_revealed": False,
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
        # The host's actual grid address, GM-only (redacted) until host_ltg_revealed. A successful
        # Analyze Subsystem on Access surfaces this string AND flips the host visible on the grid.
        "host_ltg_address": str(getattr(host, "ltg_address", "") or ""),
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
             "size": int(p.get("size", 0) or 0), "squeezed": bool(p.get("squeezed"))}
            for p in (decker.get("storage_programs") or [])
            if isinstance(p, dict) and p.get("name")
        ],
        # Squeeze option (vr2 L1673): programs built compressed sit at HALF size in storage but must
        # be Decompressed (Complex Action, no test) to full size before use after a mid-run swap into
        # active memory. squeeze_keys = every util key built squeezed (active copies start already
        # decompressed/usable; only storage->active swaps need the decompress). squeezed_active =
        # programs swapped into active but NOT yet decompressed: they occupy full active memory but
        # are held OUT of decker.utilities (so every effective-rating path ignores them) until
        # Decompress moves them in. Both are the decker's own deck data -- player-visible.
        "squeeze_keys": sorted(
            {str(k) for k, v in (decker.get("program_options") or {}).items()
             if isinstance(v, dict) and v.get("squeeze")}
            | {str(p.get("name", "")) for p in (decker.get("storage_programs") or [])
               if isinstance(p, dict) and p.get("name") and p.get("squeezed")}
        ),
        "squeezed_active": [],

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
        # Interactive defense (Hacking Pool spent on the NPC phase). When interactive_defense is
        # True and an IC cybercombat attack scores net successes, perform_action's proactive pass
        # PAUSES with pending_defense set so the decker can allocate Hacking Pool dice to the
        # icon's damage resistance before the hit resolves. None = no pending prompt; otherwise a
        # dict describing the parked attack (see _park_pending_defense). Defaults off so existing
        # runs/tests resolve IC hits inline exactly as before.
        "interactive_defense": False,
        "pending_defense": None,
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
    """Append a timestamped event to the state log.

    Each event is stamped with the INITIATIVE COUNT of whoever is acting (``state['_acting_init']``,
    set to the decker's Matrix initiative while a player action resolves and to each IC/enemy's own
    initiative while the app-as-GM driver runs it). Initiative is rolled once per encounter, so the
    stamp is stable and lets the Event Log show 'the Crippler acted on init 15'."""
    event["turn"] = state.get("current_turn", 1)
    if "init" not in event:
        acting_init = state.get("_acting_init")
        if acting_init is not None:
            event["init"] = acting_init
    event["ts"] = datetime.now(UTC).isoformat()
    state["event_log"].append(event)


def _completed_trace_count(state: dict) -> int:
    """Number of Trace IC that have finished their location cycle. Drives both vr2 Trace
    'Effects on Completion' (vr2_rules.md L590-591): every proactive IC gets -1 to its to-hit TN,
    and every subsequent security-tally increase gains +1 -- per completed trace, cumulatively."""
    return max(0, int(state.get("traces_completed", 0) or 0))


def _bump_security_tally(state: dict, amount: int) -> int:
    """Add a security-tally INCREASE and return the amount actually applied. A positive increase is
    accelerated by vr2 Trace 'Tally acceleration' (vr2_rules.md L591): each completed Trace IC adds
    +1 to every subsequent tally increase. Non-positive amounts (refunds) pass through un-accelerated.
    The tally floors at 0. Route every genuine tally increase through this so the acceleration can
    never be silently skipped (drift guard)."""
    amount = int(amount)
    if amount > 0:
        amount += _completed_trace_count(state)
    state["security_tally"] = max(0, int(state.get("security_tally", 0) or 0) + amount)
    return amount


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


def _wipe_all_copies(state: dict, decker: dict, util_name: str) -> None:
    """Tar Pit corruption (vr2_rules.md L540-542 + user ruling 2026-07-10): a Tar Pit that wins its
    MPCP test injects viral code that corrupts EVERY copy of the program -- in active AND storage
    memory. For the rest of the run (until jack out) the program is GONE: it cannot be reloaded via
    Swap Memory. Unlike ``_wipe_one_shot`` this applies to ANY program, not just One-Shots. Marks
    the active copy spent (program_damage == base), flags it in ``one_shot_wiped`` (the shared
    'cannot reload' list Swap Memory honours) and drops every storage copy."""
    # A One-Shot program already has its own corrupt-all-copies path (event + list + storage
    # removal); reuse it so one-shots keep emitting the one_shot_wiped event. For any OTHER
    # program the call below no-ops and the generic wipe here does the work.
    _wipe_one_shot(state, decker, util_name)
    key = _normalize_util_name(util_name)
    base = int((decker.get("utilities") or {}).get(key, 0) or 0)
    pd = state.setdefault("program_damage", {})
    if base > 0:
        pd[key] = base  # the copy in active memory is corrupted too
    wiped = state.setdefault("one_shot_wiped", [])
    if key not in wiped:
        wiped.append(key)
    storage = state.get("storage_programs")
    if isinstance(storage, list):
        state["storage_programs"] = [
            p for p in storage if _normalize_util_name(p.get("name", "")) != key
        ]


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
    # Per-pass DINAB lock (vr2): a program run autonomously by DINAB may not also be used manually
    # by the decker on the SAME pass, and vice versa. Only one DINAB fires per pass (it costs the
    # single Free action), so one slot tracks the DINAB'd program key and a list tracks the
    # program keys the decker used by hand. Cleared here at every pass/turn boundary.
    state["dinab_prog_this_pass"] = ""
    state["manual_progs_this_pass"] = []


def _spend_pass_action(state: dict, action_type: str) -> None:
    """Enforce the per-pass action economy (vr2). Each initiative pass grants 2 action points
    (Simple=1, Complex=2) plus 1 separate Free action. When the current pass can no longer afford
    the action, raise 400 -- the decker must click End Turn to close the pass (letting the hostiles
    on it act) and open the next one. Free actions draw from their own slot, so they still work
    after the action points are gone. Legacy runs without a budget are not enforced."""
    if "pass_action_points" not in state:
        return
    cost = _ACTION_COST.get(action_type, "Complex")
    if cost == "Free":
        if state.get("pass_free", 0) >= 1:
            state["pass_free"] -= 1
            return
        raise HTTPException(
            400, "No Free action left this turn -- click End Turn to advance to "
                 "your next turn.")
    need_ap = 2 if cost == "Complex" else 1
    if state.get("pass_action_points", 0) >= need_ap:
        state["pass_action_points"] -= need_ap
        return
    # Out of action points for this pass. Do NOT silently roll into the next pass -- the decker
    # decides when to end the pass (End Turn), which is also when the hostiles on the pass being
    # left get their action. Report whether another pass remains so the UI can guide the click.
    cur, total = state.get("current_pass", 1), state.get("initiative_passes", 1)
    if cur >= total:
        raise HTTPException(
            400, f"No action points left and all {total} turn(s) are spent this "
                 "Round -- click End Round to begin the next round.")
    raise HTTPException(
        400, f"Not enough action points this turn -- {cost} needs {need_ap}. Click End Turn to "
             f"close turn {cur}/{total} and start your next turn.")


# Manual actions map to the utility program they run, so the per-pass DINAB lock can tell when the
# decker is trying to use a program by hand that DINAB already ran this pass (or vice versa). The
# DINAB-capable programs with a manual equivalent are named directly; every other operation falls
# back to the System Operations utility (lower-snake, matching the DINAB utility keys).
_ACTION_PROGRAM_KEY_DIRECT = {
    "medic": "medic", "restore": "restore", "slow": "slow",
    "steamroller": "steamroller", "disinfect": "disinfect",
}


def _action_program_key(action_type: str) -> str | None:
    """Return the utility program key a manual action runs, or None if it uses no carried program."""
    if action_type in _ACTION_PROGRAM_KEY_DIRECT:
        return _ACTION_PROGRAM_KEY_DIRECT[action_type]
    util = _ACTION_UTILITY.get(action_type)
    if not util:
        return None
    return util.strip().lower().replace(" ", "_").replace("/", "_")


def _assert_not_dinab_locked(state: dict, prog_key: str | None) -> None:
    """Reject a MANUAL use of ``prog_key`` if DINAB already ran that program this pass (vr2: a
    program run autonomously by DINAB cannot also be used by the decker on the same pass). No-op
    for legacy runs (no action budget) or actions that run no carried program."""
    if not prog_key or "pass_action_points" not in state:
        return
    if state.get("dinab_prog_this_pass") == prog_key:
        pretty = prog_key.replace("_", " ").title()
        raise HTTPException(
            400, f"{pretty} is already running autonomously via DINAB this turn -- you cannot also "
                 "use it by hand until your next turn.")


def _record_manual_program(state: dict, prog_key: str | None) -> None:
    """Record that the decker used ``prog_key`` by hand this pass, so a later DINAB on the same
    program is blocked. No-op for legacy runs or program-less actions."""
    if not prog_key or "pass_action_points" not in state:
        return
    used = state.setdefault("manual_progs_this_pass", [])
    if prog_key not in used:
        used.append(prog_key)


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
    description (jack_out / persona_crash each do this differently).
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


def _pending_suppression_holdback(state: dict) -> int:
    """Tally that is provisionally in ``security_tally`` but still awaiting the decker's immediate
    suppression decision (vr2 Suppression -- the "you may spend 1 DF to suppress" query fired when an
    IC crashes or a data bomb detonates). While an item is UNDECIDED the increment it added is held
    back from the sheaf so a crash/detonation cannot trip a passive alert (or any higher step) BEFORE
    the decker chooses. Suppressing refunds the tally (removed from ``security_tally``, so no longer
    counted here); accepting marks it decided (then it counts). Only freshly-crashed IC (``crash_pending``)
    and undecided ``suppressions`` ledger entries are held -- older crashed IC and hung IC are not."""
    holdback = 0
    for s in state.get("suppressions", []):
        if not s.get("suppressed") and not s.get("released"):
            holdback += int(s.get("rating", 0) or 0)
    for ic in state.get("active_ic", []):
        if (ic.get("crash_pending")
                and not ic.get("suppressed") and not ic.get("suppression_released")):
            holdback += int(ic.get("crash_tally", ic.get("rating", 0)) or 0)
    return holdback


def _sheaf_trigger_tally(state: dict) -> int:
    """Security tally used for SHEAF threshold checks: the raw tally minus any increment still
    pending an immediate suppression decision (see ``_pending_suppression_holdback``). Floored at 0."""
    return max(0, state.get("security_tally", 0) - _pending_suppression_holdback(state))


def _check_sheaf_triggers(state: dict) -> list[dict]:
    """
    Check if the current security tally has crossed any sheaf trigger thresholds.
    Returns list of newly triggered steps.

    Uses ``_sheaf_trigger_tally`` (not the raw tally) so an increment still awaiting the decker's
    immediate suppress/accept decision cannot trip a step until that decision is made.
    """
    tally = _sheaf_trigger_tally(state)
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
    # Names that are OFF-LIMITS for the NPC handle: every player-character name (snapshot into
    # state["excluded_handles"] at run start) plus any handle already taken by another enemy this
    # run -- so an NPC never shares a name with a player or a sibling decker (case-insensitive).
    exclude = {str(h).strip().lower() for h in (state.get("excluded_handles") or []) if str(h).strip()}
    exclude |= {str(e.get("handle", "")).strip().lower()
                for e in state.get("enemy_deckers", []) if str(e.get("handle", "")).strip()}
    enemy = eng.generate_enemy_decker(
        security_code, state.get("host_security_value", 6), name=name, exclude_handles=exclude)
    enemy["id"] = f"ed_{uuid.uuid4().hex[:8]}"
    enemy["initiative"], enemy["initiative_passes"] = _roll_decker_initiative(enemy)  # rolled once on entry
    state.setdefault("enemy_deckers", []).append(enemy)
    _append_event(state, {
        "type": "enemy_decker_injected", "gm_only": True, "enemy_id": enemy["id"],
        "description": (
            f"GM: {_enemy_gm_name(enemy)} (Computer {enemy['computer_skill']}, "
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
                lurker = {
                    "id": lc_id,
                    "type": ic_type,
                    "rating": ic_rating,
                    "status": "lurking",
                }
                if ic_type == "Worm":
                    # Carry the worm variant (standard / deathworm / tapeworm) so its distinct
                    # end-of-run and cybercombat effects resolve. Defaults to standard infection.
                    variant = str(ev.get("variant", "standard") or "standard").lower()
                    lurker["variant"] = variant if variant in ("standard", "deathworm", "tapeworm") else "standard"
                state.setdefault("lurking_ic", []).append(lurker)
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

        elif ev_type == "bouncer":
            # Bouncer (vr2 L300): a triggered sheaf step HARDENS the host, upgrading the security
            # code/value the whole engine reads from (state host_security_code / host_security_value)
            # for the rest of the run. The designer supplies the new posture; fall back to the
            # current values if a field is absent so a malformed step cannot blank the host.
            old_code  = state.get("host_security_code", security_code)
            old_value = state.get("host_security_value", 0)
            new_code  = ev.get("new_security_code") or old_code
            _nv       = ev.get("new_security_value")
            new_value = int(_nv) if _nv is not None else old_value
            state["host_security_code"]  = new_code
            state["host_security_value"] = new_value
            events.append({
                "type": "bouncer",
                "old_security_code": old_code,
                "old_security_value": old_value,
                "new_security_code": new_code,
                "new_security_value": new_value,
                "description": (
                    f"BOUNCER -- host security hardens from {old_code} {old_value} "
                    f"to {new_code} {new_value}."
                ),
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
            # Host Shutdown (vr2_rules.md L771-789): the host does NOT dump instantly -- it starts
            # a self-shutdown SEQUENCE lasting a rolled number of Combat Turns, secret to the
            # deckers until a Sensor Test succeeds or the final-warning turn arrives. Only the FIRST
            # shutdown trigger starts the clock; later ones are ignored. Processing/dump happens at
            # end of each Combat Turn in _process_host_shutdown_countdown.
            if not state.get("shutdown_countdown"):
                sv = int(state.get("host_security_value", 6) or 6)
                num_dice = max(1, -(-sv // 2))          # 1D6 per 2 points of SV (round up)
                turns = sum(random.randint(1, 6) for _ in range(num_dice))
                warning = random.randint(1, 3)          # 1D3 final-warning turn
                state["shutdown_countdown"] = {
                    "turns_remaining": turns,
                    "total_turns": turns,
                    "final_warning_turn": warning,
                    "elapsed": 0,
                    "known": False,
                }
                events.append({
                    "type": "shutdown_initiated", "gm_only": True,
                    "turns_remaining": turns, "final_warning_turn": warning,
                    "description": (
                        f"(GM) HOST SHUTDOWN SEQUENCE started -- {turns} Combat Turn(s), final "
                        f"warning on turn {warning}. Deckers are not yet aware."
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


def _combat_target_status(target: dict | None = None) -> str:
    """Cybercombat to-hit column for an icon the PC is ATTACKING (vr2 L2028).

    The COMBAT_TN table keys off the TARGET icon's status, not the attacker's: "any icon logged on
    with a valid passcode is Legitimate; all others are Intruding." IC programs and host security
    deckers are legitimate residents of the host, so the PC always hits them on the Legitimate
    column. (A target explicitly flagged ``intruding`` -- e.g. a rival runner sharing the host --
    uses the Intruding column -- a PC's Invalidate Passcode sets ``intruding`` on the affected IC /
    enemy deckers so the PC then hits those targets on the Intruding column.)"""
    return "intruding" if (target or {}).get("intruding") else "legitimate"


def _pc_target_status(state: dict) -> str:
    """Cybercombat to-hit column an attacker (IC or enemy decker) uses against the PC's persona.

    Mirrors the target-status rule (vr2 L2028) for the player's own icon: after a successful
    Validate Passcode the persona is Legitimate (``has_legitimate_status``) and every attacker --
    dumb IC and skilled security deckers alike -- hits it on the Legitimate COMBAT_TN column, until
    logoff / active alert wipes the fake passcode. Otherwise the intruder is on the Intruding
    column."""
    return "legitimate" if state.get("has_legitimate_status") else "intruding"


# Sentinel target id for Invalidate Passcode's whole-list variant (erase EVERY passcode at +4 TN).
# Collision-safe: IC ids look like "ic1" / "td1" and enemy-decker ids are "ed_<hex>".
_INVALIDATE_ALL = "__all__"


def _invalidate_passcodes(state: dict, target_id: str | None) -> list[str]:
    """PC's Invalidate Passcode (vr2 L1879): flip host security icons Legitimate -> Intruding.

    ``target_id`` None erases the ENTIRE passcode list -- every ACTIVE IC and every enemy decker
    flips; otherwise only the single IC / enemy decker whose id matches flips (an empty / unknown id
    matches nothing). The flip is PERMANENT: unlike the PC's own Validate Passcode (wiped on active
    alert / logoff), an enemy icon never regains Legitimate status. Returns the display labels
    actually flipped (icons already Intruding are skipped). Once flipped, ``_combat_target_status``
    reads the ``intruding`` flag so the PC hits those targets on the Intruding COMBAT_TN column."""
    flipped: list[str] = []

    def _flip_ic(ic: dict) -> None:
        if ic.get("status") == "active" and not ic.get("intruding"):
            ic["intruding"] = True
            flipped.append(f"{ic.get('type', 'IC')}-{ic.get('rating', '?')}")

    def _flip_enemy(enemy: dict) -> None:
        if not enemy.get("intruding"):
            enemy["intruding"] = True
            flipped.append(str(_enemy_display_name(enemy)))

    if target_id is None:
        for ic in state.get("active_ic", []):
            _flip_ic(ic)
        for enemy in state.get("enemy_deckers", []):
            _flip_enemy(enemy)
    else:
        ic = next((i for i in state.get("active_ic", []) if i.get("id") == target_id), None)
        if ic is not None:
            _flip_ic(ic)
        else:
            enemy = next((e for e in state.get("enemy_deckers", []) if e.get("id") == target_id), None)
            if enemy is not None:
                _flip_enemy(enemy)
    return flipped


def _attack_damage_level(decker: dict, sec_code: str) -> str:
    """Base Damage LEVEL of the decker's own Attack utility (vr2 Attack-6L/-6M/-6S/-6D).

    Unlike IC (whose severity comes from the host Security Code via ``IC_DAMAGE_LEVEL``), a decker's
    Attack utility carries its own damage level, chosen at code time and priced by level. It rides
    on the run as ``program_options['attack'].damage_level``. A legacy run that never recorded one
    falls back to the host IC Damage Table (the prior behaviour), so old saves resolve unchanged."""
    lvl = str((((decker.get("program_options") or {}).get("attack") or {})
               .get("damage_level") or "")).strip().title()
    return lvl if lvl in ("Light", "Moderate", "Serious", "Deadly") else rules.IC_DAMAGE_LEVEL[sec_code]


def _trap_trace_factor_bonus(ic: dict | None) -> int:
    """A Trace IC that carries a trap is LESS effective at tracing (vr2 Trap IC + user ruling
    2026-07-10): add to its Trace Factor (raising its hunt-test TN). +ceil(hidden_rating / 2)
    (rounded UP -- a benefit to the decker) for a normal hidden IC, or the FULL hidden_rating if
    the hidden IC is Black IC. Returns 0 for a trace that carries no trap (or a non-trace)."""
    if not ic:
        return 0
    trap_hidden = ic.get("trap_hidden")
    if not trap_hidden:
        return 0
    h_rating = int(trap_hidden.get("rating", 0) or 0)
    if h_rating <= 0:
        return 0
    h_info = rules.IC_CATALOG.get(_canonical_ic_type(trap_hidden.get("type", "")), {})
    if h_info.get("category") == "black":
        return h_rating
    return -(-h_rating // 2)  # ceil(h_rating / 2)


def _compute_trace_tn(state: dict, decker: dict, ic_rating: int, eff: dict,
                      ic: dict | None = None) -> int:
    """Full Trace Factor TN per VR2.0 rules (vr2_rules.md L578).

    TF = Evasion - IC_Rating + Camo + Jackpoint + Bandwidth + Redirects_placed + TrapPenalty
    TN = max(2, TF)

    Each Redirect Datatrail operation ADDS to the Trace Factor (the Trace IC's target number), so
    more redirects make the jackpoint HARDER to trace -- the same direction as Camo. A trap carried
    by the trace itself also ADDS (see ``_trap_trace_factor_bonus``): a trapped trace is worse at
    tracing (the trap costs it effectiveness).
    """
    utilities = decker.get("utilities") or {}
    tf = (
        eff.get("evasion", decker.get("evasion", 4))
        - ic_rating
        + utilities.get("camo", 0)
        + decker.get("trace_factor", 0)
        + _live_bandwidth_modifier(decker, state, eff)
        + state.get("redirects_placed", 0)
        + _trap_trace_factor_bonus(ic)
    )
    return max(2, tf)


def _effective_detection_factor(state: dict, decker: dict) -> int:
    """Live Detection Factor (vr2_rules Detection Factor + Suppression).

    Recomputed each test rather than frozen at logon, so it reflects:
      - Sleaze utility (round-up average with Masking, else Masking/2),
      - Masking reduced by Marker/Mark-rip cripplers (via _get_decker_effective),
      - minus 1 per suppressed active IC program (Suppression rule), floored at 1.
    """
    return max(1, _base_detection_factor(state, decker) - _suppressed_count(state))


def _base_detection_factor(state: dict, decker: dict) -> int:
    """Detection Factor BEFORE any suppression cost (Sleaze/Masking, with cripple reduction)."""
    eff = _get_decker_effective(decker, state)
    sleaze = (decker.get("utilities") or {}).get("sleaze", 0)
    return eng.detection_factor(eff["masking"], sleaze)


def _suppressed_count(state: dict) -> int:
    """How many suppressible sources the decker is currently holding down -- each costs 1 DF.
    Counts suppressed active IC (crashed/hung/trace, regardless of status) PLUS suppressed non-IC
    ledger entries (data bombs, etc.)."""
    return (
        sum(1 for ic in state.get("active_ic", []) if ic.get("suppressed"))
        + sum(1 for s in state.get("suppressions", []) if s.get("suppressed"))
    )


def _assert_suppression_df_room(state: dict, decker: dict) -> None:
    """A suppression costs 1 Detection Factor and DF cannot be spent below its floor of 1. If the
    decker is already holding down enough sources that DF is at the floor, they must RELEASE one
    before they can suppress another (vr2 Suppression -- you can't spend DF you don't have)."""
    if _base_detection_factor(state, decker) - _suppressed_count(state) <= 1:
        raise HTTPException(
            400,
            "Detection Factor is already at its minimum -- release another suppression first to "
            "free up 1 DF before suppressing this one.",
        )



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


def _shield_parry_core(wear_owner: dict, *, rating: int, attacker_skill: int) -> tuple[dict, int, int]:
    """Shared Shield mechanic for ANY actor (PC decker or enemy decker) -- the single resolver both
    ``_shield_parry`` and ``_enemy_shield_parry`` route through so a Shield Test resolves the SAME
    way whoever raises it. Rolls the (already-gated, > 0) effective Shield rating vs the attacker's
    skill via ``eng.shield_parry`` and degrades the Shield 1 Rating Point (win or lose) in the
    actor's OWN ``program_damage`` slot (``wear_owner`` = the PC run ``state`` or the ``enemy`` dict).
    Returns ``(roll_result, successes, remaining_rating)``; the caller owns the actor-specific event
    (player-visible vs GM-only) and any One-Shot spend."""
    res = eng.shield_parry(shield_rating=rating, attacker_skill=attacker_skill)
    pd = wear_owner.setdefault("program_damage", {})
    pd["shield"] = pd.get("shield", 0) + 1  # -1 Rating Point per use, win or lose
    return res, res["successes"], max(0, rating - 1)


def _shield_parry(state: dict, decker: dict, *, attacker_skill: int, context: str) -> int:
    """Make ONE defensive Shield Test against an attack on the PC decker's persona (vr2).

    Thin PC-side wrapper over the shared ``_shield_parry_core``: rolls the effective Shield rating
    vs the attacker's skill (host Security Value, or an enemy decker's Computer skill), degrades the
    Shield 1 Rating Point (reload via Swap Memory) and emits a player-visible ``shield_parry`` event.
    Returns the net successes, which the caller SUBTRACTS from a damage attack's successes or ADDS to
    the decker's side of a crippler/ripper opposed test. Returns 0 -- no test, no wear, no event --
    when the Shield is unloaded or already worn to 0.
    """
    rating = _effective_shield(decker, state)
    if rating <= 0:
        return 0
    res, succ, remaining = _shield_parry_core(state, rating=rating, attacker_skill=attacker_skill)
    # Stash the Shield dice + successes so the attacker's event can fold them into its resist/defence
    # roll for display (the parry ADDS to the persona's defence / reduces the attacker, vr2). The
    # caller pops this right after the strike resolves; the standalone shield_parry event is kept for
    # the GM/AAR, but the client renders these dice inline (a distinct colour) with the shield's own
    # success count on the resist line rather than a separate line.
    state["_shield_dice_pending"] = {"dice": list(res["roll"].get("dice", [])), "successes": succ}
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

    Thin enemy-side wrapper over the SAME ``_shield_parry_core`` the PC uses -- so an enemy decker's
    Shield resolves identically (roll effective Shield vs the PC's Computer skill, wear 1 Rating
    Point win or lose) -- differing only in that the wear lives on the ``enemy`` dict and it emits a
    GM-only ``enemy_shield_parry`` event (the PC never sees the defender's exact program). Returns
    the net successes for the caller to SUBTRACT from the PC's attack successes (damage) or ADD to
    the enemy's side of a crippler test. Returns 0 -- no test, no wear, no event -- when the enemy
    carries no Shield or it is worn to 0."""
    rating = _enemy_effective_shield(enemy)
    if rating <= 0:
        return 0
    res, succ, remaining = _shield_parry_core(enemy, rating=rating, attacker_skill=attacker_skill)
    _append_event(state, {
        "type": "enemy_shield_parry", "gm_only": True,
        "enemy_id": enemy.get("id"), "context": context,
        "shield_rating": rating, "shield_remaining": remaining,
        "successes": succ, "roll": res["roll"],
        "description": (
            f"GM: {_enemy_gm_name(enemy)} Shield-{rating} parries the {context} hit -- "
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


def _add_cm_damage(cm: dict, track: str, boxes: int) -> int:
    """Add damage boxes to one Condition Monitor track (``persona_boxes`` / ``stun_boxes`` /
    ``physical_boxes``), clamped to the SR2 maximum of 10. Every CM has exactly ten boxes; the 10th
    is the Deadly/crash box that the run-end and persona-crash checks detect via ``>= 10``, so a
    full track saturates at 10 rather than overflowing past it (which used to surface as e.g.
    ``12/10`` on the sheet). Damage only ever raises a track toward the cap -- healing goes through
    the medic/restore paths. Same clamp for a PC and an enemy icon. Returns the new box count."""
    new = min(10, max(0, int(cm.get(track, 0) or 0)) + max(0, int(boxes or 0)))
    cm[track] = new
    return new


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
        _add_cm_damage(cm, "physical_boxes", overflow)
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
    """Enemy decker's EFFECTIVE Armor utility rating = its loaded Armor minus the per-hit wear it
    has accrued (``enemy['program_damage']['armor']``). Armor reduces the Power of incoming persona
    damage and -- per vr2 -- loses 1 Rating Point every time the decker takes damage (see
    ``_wear_armor``); a fresh copy is restored via Swap Memory. Enemy deckers are modeled EXACTLY
    like the PC decker (Bod dice vs Power, the Armor utility lowering that Power; see the PC path in
    ``_effective_armor`` / ``_detonate_data_bomb`` / Black IC resistance). Most auto-generated
    enemies carry no Armor, so this is 0 unless one is explicitly loaded."""
    base = int((enemy.get("utilities") or {}).get("armor", 0) or 0)
    worn = int((enemy.get("program_damage") or {}).get("armor", 0) or 0)
    return max(0, base - worn)


def _effective_armor(decker: dict, state: dict) -> int:
    """PC decker's EFFECTIVE Armor utility rating = its loaded Armor minus accrued per-hit wear
    (``state['program_damage']['armor']`` -- the SAME slot Swap Memory resets, mirroring
    _effective_shield). Armor reduces the Power of attacks against the persona icon and, per vr2,
    loses 1 Rating Point every time the decker takes damage (see ``_wear_armor``). ``<= 0`` means
    no Armor is loaded or it has been worn out (a Swap Memory reload restores full rating)."""
    base = int((decker.get("utilities") or {}).get("armor", 0) or 0)
    worn = int((state.get("program_damage") or {}).get("armor", 0) or 0)
    return max(0, base - worn)


def _wear_armor(state: dict, wear_owner: dict, utils_owner: dict, boxes: int,
                *, gm_only: bool = False, actor: str = "") -> None:
    """vr2 Armor: "loses 1 Rating Point every time the decker takes damage." When an armor-resisted
    hit lands 1+ boxes AND an Armor utility is loaded, degrade it 1 point in the owner's
    ``program_damage['armor']`` slot (reset by a Swap Memory reload). ``wear_owner`` is where the
    wear lives (the PC run ``state`` or an ``enemy`` dict); ``utils_owner`` is where the utilities
    live (the PC ``decker`` or the same ``enemy`` dict). Emits an ``armor_wear`` event on ``state``
    -- player-visible for the PC, GM-only for an enemy. No-op when no boxes land, no Armor is
    loaded, or the Armor is already worn out (never wears past 0 effective rating)."""
    if boxes <= 0:
        return
    base = int((utils_owner.get("utilities") or {}).get("armor", 0) or 0)
    if base <= 0:
        return
    pd = wear_owner.setdefault("program_damage", {})
    if pd.get("armor", 0) >= base:
        return  # already worn out -- nothing left to degrade
    pd["armor"] = pd.get("armor", 0) + 1
    remaining = max(0, base - pd["armor"])
    if gm_only:
        _append_event(state, {
            "type": "armor_wear", "gm_only": True, "armor_remaining": remaining,
            "description": (f"GM: {actor or 'Security decker'} Armor worn to {remaining}"
                            + (" -- burned out." if remaining == 0 else " by the hit.")),
        })
    else:
        _append_event(state, {
            "type": "armor_wear", "armor_remaining": remaining,
            "description": (f"Armor worn to {remaining} by the hit"
                            + (" -- burned out; Swap Memory a fresh copy." if remaining == 0
                               else " -- Swap Memory to restore full rating.")),
        })


def _enemy_sleaze(enemy: dict) -> int:
    """Enemy decker's Sleaze utility rating (raises its Detection Factor). Read when recomputing an
    enemy's Detection Factor after Reveal crips its Masking -- mirrors the shape of _enemy_armor."""
    return int((enemy.get("utilities") or {}).get("sleaze", 0) or 0)


def _enemy_effective_attr(enemy: dict, attr: str) -> int:
    """Enemy decker's CURRENT (cripple-adjusted) persona attribute = base rating minus the
    temporary + permanent crippler damage tracked in its condition monitor, floored at 1. Mirrors
    the PC model EXACTLY (the base attribute in ``enemy[attr]`` is never mutated by a crippler --
    the damage lives in ``condition_monitor.persona_damage`` so a Restore can repair it). Every
    enemy resist/attack pool that reads a persona attribute goes through this, so a Poisoned/
    Restricted/Revealed enemy fights (and is detected) with the reduced value."""
    base = int(enemy.get(attr, 1) or 1)
    dmg = int(((enemy.get("condition_monitor") or {}).get("persona_damage") or {}).get(attr, 0) or 0)
    return max(1, base - dmg)


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


def _boxes_to_wound_level(boxes: int) -> str:
    """Map filled persona/icon Condition Monitor boxes to the Medic Target Numbers Table wound
    level (Light >= 1, Moderate >= 3, Serious >= 6 boxes). Callers guarantee ``boxes > 0``. The
    table tops out at Serious, so the Deadly box-range (up to the 10-box crash) also heals at the
    Serious TN."""
    if boxes >= rules.DAMAGE_BOXES["Serious"]:
        return "Serious"
    if boxes >= rules.DAMAGE_BOXES["Moderate"]:
        return "Moderate"
    return "Light"


def _current_icon_wound_level(state: dict) -> str | None:
    """Worst current wound level of the decker's persona icon, derived from the filled Condition
    Monitor boxes via the vr2 Condition Monitor Table floors (Light >= 1, Moderate >= 3,
    Serious >= 6 boxes). Returns ``None`` when the icon is undamaged. Everything at or above the
    Serious floor (including the Deadly box-range, up to the 10-box crash) reports ``"Serious"``
    -- the Medic Target Numbers Table tops out at Serious, so a worse wound still heals at TN 6."""
    boxes = (state.get("condition_monitor") or {}).get("persona_boxes", 0) or 0
    if boxes <= 0:
        return None
    return _boxes_to_wound_level(boxes)


def _medic_heal_core(cm: dict, wear_owner: dict, *, rating: int) -> tuple[dict, str, int]:
    """Shared Medic mechanic for ANY actor (PC decker or enemy decker) -- the single resolver both
    ``_apply_medic`` and ``_enemy_medic_heal`` route through so a Medic heal resolves the SAME way
    whoever runs it. The caller must gate ``current persona boxes > 0`` and ``rating > 0`` first.
    Rolls the Medic rating vs the icon's CURRENT wound-level TN via ``eng.medic_heal``, heals
    ``min(current boxes, successes)`` persona/icon boxes on ``cm`` (the actor's condition monitor),
    and degrades the Medic 1 Rating Point (win or lose) in the actor's OWN ``program_damage`` slot
    (``wear_owner`` = the PC run ``state`` or the ``enemy`` dict). Returns ``(roll_result,
    wound_level, boxes_healed)``; the caller owns the actor-specific event and any One-Shot spend."""
    boxes = int(cm.get("persona_boxes", 0) or 0)
    wound = _boxes_to_wound_level(boxes)
    res = eng.medic_heal(medic_rating=rating, wound_level=wound)
    healed = min(boxes, res["boxes_healed"])
    cm["persona_boxes"] = max(0, boxes - healed)
    pd = wear_owner.setdefault("program_damage", {})
    pd["medic"] = pd.get("medic", 0) + 1   # -1 Rating Point per use, win or lose
    return res, wound, healed


def _apply_medic(state: dict, decker: dict, *, pool_override: int | None = None,
                 via_dinab: bool = False) -> None:
    """Resolve a Medic action (vr2, Complex Action, self-targeted). Heals boxes of persona/icon
    Condition Monitor damage equal to the Medic Test successes -- TN set by the icon's CURRENT
    wound level (Light 4 / Moderate 5 / Serious 6) -- capped by the current damage. The Medic
    degrades 1 Rating Point per use regardless of outcome (reload a fresh copy via Swap Memory).

    Mutates ``state`` in place (condition_monitor + program_damage) and always emits a
    player-visible ``medic_heal`` event. Heals/degrades nothing when the icon is undamaged or the
    Medic is worn out / not loaded (mirrors _shield_parry, which does not wear a 0-rating Shield).

    ``pool_override`` (DINAB) rolls the heal at the DINAB rating instead of the Medic's own
    effective rating; the Medic program STILL wears -1 per use (its own rule applies whether run by
    hand or by DINAB), but the DINAB rating itself does not degrade here (the caller skips
    _dinab_resolve_failure for the self-targeted defensive programs).
    """
    cm = state.setdefault("condition_monitor", {})
    boxes = cm.get("persona_boxes", 0) or 0
    wound = _current_icon_wound_level(state)
    label = "DINAB Medic" if via_dinab else "Medic"
    if wound is None:
        _append_event(state, {
            "type": "medic_heal", "healed": 0, "persona_boxes": boxes,
            "description": f"{label}: icon undamaged -- nothing to heal.",
        })
        return
    rating = pool_override if pool_override is not None else _effective_medic(decker, state)
    if rating <= 0:
        _append_event(state, {
            "type": "medic_heal", "healed": 0, "persona_boxes": boxes, "wound_level": wound,
            "description": ("Medic offline (worn out or not loaded) -- reload a fresh copy via "
                            "Swap Memory before it can heal the icon."),
        })
        return
    res, wound, healed = _medic_heal_core(cm, state, rating=rating)
    remaining_rating = _effective_medic(decker, state)   # Medic program rating AFTER this use's wear
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
            f"{label}-{rating} treats the {wound.lower()} icon wound (TN {res['tn']}): "
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
    res, wound, healed = _medic_heal_core(ecm, enemy, rating=rating)
    name = _enemy_display_name(enemy)
    if healed > 0:
        desc = f"{name} repairs damage to their icon."
    else:
        desc = f"{name} attempts to repair damage to their icon, but it fails."
    _append_event(state, {
        "type": "enemy_decker", "outcome": "medic", "enemy_id": enemy.get("id"),
        "description": desc,
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
                        f"{_enemy_display_name(enemy)} is wounded ({boxes}/10) and "
                        f"its nerve breaks -- it jacks out, abandoning the hunt."
                    ),
                })
                return True
    return False


_BEMS_ORDER = ("bod", "evasion", "masking", "sensor")
_RESTORE_FALLBACK_TN = 6  # legacy runs with crippler damage but no recorded causing rating


def _record_crippler_rating_cm(cm: dict, attr: str, rating: int) -> None:
    """Record the highest crippler/ripper program rating that caused the CURRENT temporary damage
    to a persona attribute, in the given condition-monitor dict (the PC's state condition monitor
    OR an enemy decker's). This is the Restore Test target number (vr2: TN = rating of the causing
    program; highest if several). Reset to 0 by the Restore core once the attribute's temporary
    damage is fully repaired (no longer relevant)."""
    cr = cm.setdefault("crippler_rating", {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0})
    cr[attr] = max(int(cr.get(attr, 0) or 0), int(rating or 0))


def _record_crippler_rating(state: dict, attr: str, rating: int) -> None:
    """PC convenience wrapper: record the crippler causing-rating in the player's condition
    monitor. See _record_crippler_rating_cm."""
    _record_crippler_rating_cm(state.setdefault("condition_monitor", {}), attr, rating)


def _resolve_attribute_attack(
    state: dict,
    *,
    attacker_pool: int,
    resist_tn: int,
    target_attr_rating: int,
    attr: str,
    sec_code: str,
    target_status: str,
    target_kind: str,
    enemy: dict | None = None,
    causing_rating: int = 0,
    shield_successes: int = 0,
    tn_modifier: int = 0,
    is_ripper: bool = False,
    mpcp_rating: int = 0,
    hardening: int = 0,
    shield_parry: Callable[[], int] | None = None,
) -> dict:
    """Single application path for the attribute-crippling family (decker Poison/Restrict/Reveal
    AND the Acid/Binder/Marker/Jammer cripplers + *-rip rippers). Both attack directions route the
    dice through eng.attribute_attack_core (via crippler_attack for the shared ripper rider) and
    apply the resulting reduction here, so the mechanic is modelled ONCE -- callers differ only in
    the event label they build. BOTH directions add to the TARGET's persona_damage ledger (PC ->
    state's condition monitor, enemy -> its own), record the Restore causing-rating, and, for
    rippers, add permanent Persona-chip damage -- the base attribute is never mutated, so a Restore
    can repair either persona identically. The enemy's stored Detection Factor is recomputed off the
    new effective Masking when Reveal drops it. Either way the attribute is floored at 1 (applied =
    min(reduction, target_attr_rating - 1)), which also fixes the multi-hit accumulation that the
    old per-site caps got wrong. Returns the engine result augmented with ``reduction`` (raw net //
    2), ``applied`` (points actually removed after the floor), ``new_value`` (post-hit effective
    attribute) and ``chip_applied`` (ripper only)."""
    res = eng.crippler_attack(
        security_value=attacker_pool,
        security_code=sec_code,
        target_status=target_status,
        target_attribute_rating=max(1, int(target_attr_rating or 1)),
        ic_rating=resist_tn,
        is_ripper=is_ripper,
        mpcp_rating=mpcp_rating,
        hardening=hardening,
        shield_successes=shield_successes,
        tn_modifier=tn_modifier,
        shield_parry=shield_parry,
    )
    reduction = int(res.get("attribute_reduction", 0) or 0)
    room = max(0, int(target_attr_rating or 1) - 1)
    applied = min(reduction, room) if reduction > 0 else 0
    chip_applied = 0
    # ONE ledger model for BOTH actors (vr2): the base persona attribute is never mutated -- the
    # temporary crippler damage (and permanent ripper chip) live in the target's condition monitor,
    # so a Restore can repair it whether the wounded persona is the PC's or an enemy decker's. The
    # PC writes to state's condition monitor; an enemy writes to its own. Effective attribute =
    # base - persona_damage (PC reads inline / via now-calcs; enemy via _enemy_effective_attr).
    cm = (enemy.setdefault("condition_monitor", {}) if target_kind == "enemy" and enemy is not None
          else state.setdefault("condition_monitor", {}))
    pd = cm.setdefault("persona_damage", {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0})
    if applied > 0:
        pd[attr] = pd.get(attr, 0) + applied
        _record_crippler_rating_cm(cm, attr, causing_rating)
    if is_ripper:
        chip = int(res.get("chip_damage", 0) or 0)
        chip_applied = max(0, min(chip, room - applied))
        if chip_applied > 0:
            pd[attr] = pd.get(attr, 0) + chip_applied
            pcd = cm.setdefault(
                "persona_chip_damage", {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0})
            pcd[attr] = pcd.get(attr, 0) + chip_applied
    new_value = max(1, int(target_attr_rating or 1) - applied - chip_applied)
    # An enemy's Detection Factor is stored (derived from its Masking); recompute it off the new
    # EFFECTIVE masking so a Reveal still lights the enemy up. (The PC's DF is computed on read via
    # _effective_detection_factor, so there is no stored value to refresh.)
    if (target_kind == "enemy" and enemy is not None and attr == "masking"
            and (applied + chip_applied) > 0):
        enemy["detection_factor"] = eng.detection_factor(new_value, _enemy_sleaze(enemy))
    res["reduction"] = reduction
    res["applied"] = applied
    res["new_value"] = new_value
    res["chip_applied"] = chip_applied
    return res


def _effective_restore(decker: dict, state: dict) -> int:
    """Effective Restore rating = the loaded Restore utility minus any crash wear in
    ``state['program_damage']['restore']`` (e.g. from Tar Baby / Hog). Unlike Medic, Restore does
    NOT self-degrade per use, so normal Restore use never changes this -- it only drops if the
    program is crashed, and a Swap Memory reload restores it to full. ``<= 0`` means the Restore is
    unloaded or crashed and cannot repair attributes."""
    base = (decker.get("utilities") or {}).get("restore", 0) or 0
    worn = (state.get("program_damage") or {}).get("restore", 0)
    return max(0, base - worn)


def _select_restore_attr(cm: dict, target: str = "") -> str | None:
    """Pick the persona attribute a Restore repairs: an explicit valid ``target`` WITH repairable
    damage, else the most-damaged repairable attribute (max() returns the first maximal element in
    _BEMS_ORDER -> the Bod>Evasion>Masking>Sensor tie-break). None when nothing is repairable."""
    pd = cm.get("persona_damage") or {}
    chip = cm.get("persona_chip_damage") or {}

    def repairable(a: str) -> int:
        return max(0, int(pd.get(a, 0) or 0) - int(chip.get(a, 0) or 0))

    if sum(repairable(a) for a in _BEMS_ORDER) <= 0:
        return None
    tgt = (target or "").strip().lower()
    return tgt if (tgt in _BEMS_ORDER and repairable(tgt) > 0) else max(_BEMS_ORDER, key=repairable)


def _restore_repair_core(cm: dict, *, rating: int, target: str = "") -> tuple[dict, str, int, int] | None:
    """Shared Restore application for BOTH actors (PC + enemy): repair ONE persona attribute's
    TEMPORARY crippler damage in the given condition-monitor ledger. Rolls eng.restore_repair (TN =
    the attribute's recorded causing crippler rating, or the highest recorded / a fallback), reduces
    ``persona_damage[attr]`` by every-2-successes but never below the permanent Persona-chip floor,
    and clears ``crippler_rating[attr]`` once the temporary damage is gone. Restore does NOT
    self-degrade, so NO program_damage wear is applied here (the key difference from Medic). Returns
    ``(res, attr, points, floor)`` or ``None`` when nothing is repairable. The caller supplies the
    effective Restore rating, handles the offline gate, and builds the actor-specific event."""
    attr = _select_restore_attr(cm, target)
    if attr is None:
        return None
    pd = cm.setdefault("persona_damage", {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0})
    chip = cm.get("persona_chip_damage", {}) or {}
    ratings = cm.setdefault("crippler_rating", {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0})
    repairable = max(0, int(pd.get(attr, 0) or 0) - int(chip.get(attr, 0) or 0))
    causing = int(ratings.get(attr, 0) or 0)
    if causing <= 0:  # legacy/untracked: highest recorded rating, else a sane default TN
        causing = max([int(ratings.get(a, 0) or 0) for a in _BEMS_ORDER] + [0]) or _RESTORE_FALLBACK_TN
    res = eng.restore_repair(restore_rating=rating, causing_rating=causing, damage_points=repairable)
    points = res["points_repaired"]
    floor = int(chip.get(attr, 0) or 0)  # never repair below the permanent Persona-chip floor
    pd[attr] = max(floor, int(pd.get(attr, 0) or 0) - points)
    if max(0, int(pd.get(attr, 0) or 0) - floor) <= 0:  # temp damage cleared -> causing rating moot
        ratings[attr] = 0
    return res, attr, points, floor


def _apply_restore(state: dict, decker: dict, target: str = "", *,
                   pool_override: int | None = None, via_dinab: bool = False) -> None:
    """Resolve a Restore action (vr2, Complex Action, self-targeted defensive utility): repair the
    TEMPORARY crippler reductions to the online icon's persona attributes (Bod/Evasion/Masking/
    Sensor) through the shared _restore_repair_core. Restore Test TN = the highest rating of the
    crippler program(s) that caused the targeted attribute's current damage; every 2 successes
    repairs 1 point, capped by the repairable damage present.

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
    chip = cm.get("persona_chip_damage", {}) or {}
    pd = cm.get("persona_damage", {}) or {}

    def repairable(a: str) -> int:
        return max(0, int(pd.get(a, 0) or 0) - int(chip.get(a, 0) or 0))

    if sum(repairable(a) for a in _BEMS_ORDER) <= 0:
        perm_total = sum(max(0, int(chip.get(a, 0) or 0)) for a in _BEMS_ORDER)
        msg = "Restore: no temporary attribute damage to repair."
        if perm_total > 0:
            msg += (f" {perm_total} point{'' if perm_total == 1 else 's'} of permanent "
                    "Persona-chip damage (gray/black IC) cannot be repaired by Restore.")
        _append_event(state, {"type": "restore_repair", "repaired": 0, "description": msg})
        return

    rating = pool_override if pool_override is not None else _effective_restore(decker, state)
    if rating <= 0:
        _append_event(state, {
            "type": "restore_repair", "repaired": 0, "attribute": _select_restore_attr(cm, target),
            "description": ("Restore offline (crashed or not loaded) -- reload a fresh copy via "
                            "Swap Memory before it can repair attributes."),
        })
        return

    res, attr, points, floor = _restore_repair_core(cm, rating=rating, target=target)
    pd = cm["persona_damage"]
    now = max(1, int(decker.get(attr, 4) or 4) - int(pd.get(attr, 0) or 0))
    label = "DINAB Restore" if via_dinab else "Restore"
    _append_event(state, {
        "type": "restore_repair",
        "attribute": attr,
        "repaired": points,
        "restore_rating": rating,
        "causing_rating": res["causing_rating"],
        "attribute_damage": pd[attr],
        "decker_roll": res["roll"],
        "description": (
            f"{label}-{rating} repairs {attr.upper()} (TN {res['tn']} = causing crippler rating): "
            f"{res['successes']} success{'' if res['successes'] == 1 else 'es'} -> "
            f"{points} point{'' if points == 1 else 's'} restored. "
            f"{attr.upper()} now {now} ({pd[attr]} damage remaining"
            + (f", {floor} permanent chip -- not repairable" if floor > 0 else "") + ")."
        ),
    })
    _spend_one_shot(state, decker, "restore")


def _enemy_effective_restore(enemy: dict) -> int:
    """Enemy decker's effective Restore rating = the loaded Restore utility minus any crash wear in
    its ``program_damage['restore']``. Like the PC (and unlike Medic), Restore does NOT self-degrade
    per use. ``<= 0`` -> unloaded or crashed: it cannot repair attributes. Mirrors _effective_restore."""
    base = (enemy.get("utilities") or {}).get("restore", 0) or 0
    worn = (enemy.get("program_damage") or {}).get("restore", 0)
    return max(0, base - worn)


def _enemy_carries_restore(enemy: dict) -> bool:
    """True if this enemy decker has a Restore utility loaded (mirrors _enemy_carries_medic)."""
    return int((enemy.get("utilities") or {}).get("restore", 0) or 0) > 0


def _enemy_repairable_damage(enemy: dict) -> int:
    """Total TEMPORARY (repairable) persona-attribute damage on an enemy decker = persona_damage
    minus the permanent Persona-chip floor, summed over BEMS. Drives the wounded-AI self-repair
    trigger (the enemy Restores when this is worth an action)."""
    cm = enemy.get("condition_monitor") or {}
    pd = cm.get("persona_damage") or {}
    chip = cm.get("persona_chip_damage") or {}
    return sum(max(0, int(pd.get(a, 0) or 0) - int(chip.get(a, 0) or 0)) for a in _BEMS_ORDER)


def _enemy_restore_repair(state: dict, enemy: dict) -> None:
    """Enemy-decker mirror of _apply_restore: repair the enemy's OWN temporary attribute cripple
    damage through the SAME shared _restore_repair_core the PC uses (one resolver, whoever runs it).
    Emits a GM-only event and refreshes the enemy's stored Detection Factor when Masking is repaired.
    No One-Shot / DINAB (enemy loadouts carry neither). No-ops silently when the Restore is offline
    or nothing is repairable (the caller only invokes it when both hold)."""
    rating = _enemy_effective_restore(enemy)
    if rating <= 0:
        return
    cm = enemy.setdefault("condition_monitor", {})
    result = _restore_repair_core(cm, rating=rating)
    if result is None:
        return
    res, attr, points, _floor = result
    pd = cm["persona_damage"]
    if attr == "masking":
        enemy["detection_factor"] = eng.detection_factor(
            _enemy_effective_attr(enemy, "masking"), _enemy_sleaze(enemy))
    now = max(1, int(enemy.get(attr, 4) or 4) - int(pd.get(attr, 0) or 0))
    name = _enemy_display_name(enemy)
    if points > 0:
        desc = f"{name} repairs damage to their {attr.upper()}."
    else:
        desc = f"{name} attempts to repair damage to their {attr.upper()}, but it fails."
    _append_event(state, {
        "type": "enemy_decker", "outcome": "restore", "enemy_id": enemy.get("id"),
        "description": desc,
    })


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

    # Failed Disinfect: the worm may infect the MPCP. The Worm Infection Test is the HOST's
    # Security Value dice vs the deck's MPCP rating, with Hardening subtracted from the worm's
    # successes (net > 1 infects) -- see eng.worm_attack (vr2_rules.md L548-550 + user ruling).
    wr = eng.worm_attack(
        security_value=state.get("host_security_value", 1),
        mpcp_rating=decker.get("mpcp", 1),
        hardening=decker.get("hardening", 0),
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
                f"Worm-{worm['rating']} infected the MPCP (Infection Test: host "
                f"{wr['roll']['pool']}d6 vs MPCP TN {wr['tn']}, net {wr['net_successes']} "
                f"after Hardening). Chip replacement required (permanent)."
            ),
        })
    else:
        _append_event(state, {
            "type": "worm_disinfected", "destroyed": False, "subsystem": subsystem,
            "ic_id": worm["id"], "ic_type": "Worm", "decker_roll": res["roll"],
            "infection_roll": wr["roll"],
            "description": (
                f"Disinfect-{rating} failed to destroy Worm-{worm['rating']} on the {subsystem} "
                f"subsystem (TN {res['tn']}), but the MPCP shrugged off the infection (host "
                f"{wr['roll']['pool']}d6 vs MPCP TN {wr['tn']}, net {wr['net_successes']}). "
                f"The worm is still lurking."
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
                       decker_pool: int, target_ic_id: str = "",
                       via_dinab: bool = False) -> tuple[bool, bool]:
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
    non-crashing strike just accumulates boxes on the tar's 10-box monitor; it stays lurking.
    Always emits a player-visible ``tar_steamrolled`` event (the decker is attacking the tar, so it
    learns the result; the running tally figure is auto-redacted for non-admins). Returns
    ``(failed, all_ones)`` for the DINAB degrade check -- ``failed`` = no boxes were inflicted this
    strike (missed or fully staged down), ``all_ones`` = the to-hit roll botched. The manual caller
    ignores the return; ``via_dinab`` only relabels the event as a DINAB-run strike."""
    rating = _effective_steamroller(decker, state)
    src = "DINAB Steamroller" if via_dinab else "Steamroller"
    if rating <= 0:
        # Manual use with no Steamroller loaded is a no-op that must NOT cost the action: reject
        # BEFORE the endpoint commits the spent action point. DINAB (autonomous) only logs it.
        if not via_dinab:
            raise HTTPException(
                400, "No Steamroller utility loaded (worn out or not in active memory) -- load one "
                     "via Swap Memory before you can crush a tar IC.")
        _append_event(state, {
            "type": "tar_steamrolled", "destroyed": False,
            "description": ("Steamroller offline (worn out or not loaded) -- load a Steamroller "
                            "utility (Swap Memory) before you can crush a tar IC."),
        })
        return False, False

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
        return False, False

    sr_opts = (decker.get("program_options") or {}).get("steamroller") or {}
    # vr2 L2028: hit the TARGET's status column. The target is a lurking tar-IC (a Legitimate host
    # resident), so Steamroller uses the Legitimate column, not the PC-attacker's Intruding status.
    to_hit_tn = rules.COMBAT_TN[sec_code][_combat_target_status(target)]
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
    to_hit = res["to_hit_roll"]
    all_ones = to_hit.get("ones", 0) >= to_hit.get("pool", 0) and to_hit.get("successes", 0) == 0

    if not res["crashed"]:
        target["boxes"] = res["total_boxes"]
        failed = res["boxes"] <= 0   # no boxes inflicted this strike -> a DINAB-degrading miss
        _append_event(state, {
            "type": "tar_steamrolled", "destroyed": False,
            "ic_id": target["id"], "ic_type": target["type"], "decker_roll": res["to_hit_roll"],
            "description": (
                f"{src}-{rating} hits {target['type']}-{target.get('rating', 0)} for "
                f"{res['damage_level']} ({res['total_boxes']}/{res['tar_cm']}) -- it holds and "
                f"stays lurking."
            ),
        })
        return failed, all_ones

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
    applied = _bump_security_tally(state, tally_increase)
    _append_event(state, {
        "type": "tar_steamrolled", "destroyed": True,
        "ic_id": target["id"], "ic_type": target["type"], "decker_roll": res["to_hit_roll"],
        "description": (
            f"{src}-{rating} CRUSHES {target['type']}-{ic_rating} ({res['damage_level']}). "
            f"Tally +{applied} -> {state['security_tally']}{note}"
        ),
        "tally_increase": applied,
    })
    if applied:
        _check_and_activate_sheaf(state, sec_code)
    return False, False   # a crash is an unambiguous hit -- never degrades DINAB


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
    Reactive IC are immune; a trace IC is vulnerable while VISIBLE -- during its Hunt Cycle, or once
    a Locate IC has re-acquired it in its Location Cycle (``_trace_is_targetable``). A trace that
    has vanished into an un-located Location Cycle cannot be slowed. Returns ``(ok, reason)`` --
    ``reason`` is the 400 message when ``ok`` is False."""
    info = rules.IC_CATALOG.get(_canonical_ic_type(ic.get("type", "")), {})
    if info.get("subtype", "") == "trace":
        if not _trace_is_targetable(ic):
            return False, ("that trace IC has vanished into its location cycle -- run Locate IC "
                           "to re-acquire it before you can slow it.")
        return True, ""
    if info.get("ic_type") != "proactive":
        return False, "reactive IC are immune to Slow -- only proactive IC can be slowed."
    return True, ""


def _apply_slow(state: dict, decker: dict, *, sec_code: str,
                decker_pool: int, target_ic_id: str = "",
                via_dinab: bool = False) -> tuple[bool, bool]:
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
    outcome ``offline`` / ``no_target`` / ``missed`` / ``resisted`` / ``slowed`` / ``hung``.

    Returns ``(failed, all_ones)`` for the DINAB degrade check -- ``failed`` = the strike did
    nothing (missed the to-hit or the IC won the opposed test), ``all_ones`` = the to-hit roll
    botched. The manual caller ignores the return; ``via_dinab`` only relabels the event."""
    rating = _effective_slow(decker, state)
    src = "DINAB Slow" if via_dinab else "Slow"
    if rating <= 0:
        # Manual use with no Slow loaded is a no-op that must NOT cost the action: reject BEFORE
        # the endpoint commits the spent action point. DINAB (autonomous) only logs it.
        if not via_dinab:
            raise HTTPException(
                400, "No Slow utility loaded (worn out or not in active memory) -- load one via "
                     "Swap Memory before you can slow a proactive IC.")
        _append_event(state, {
            "type": "ic_slowed", "outcome": "offline",
            "description": ("Slow offline (worn out or not loaded) -- load a Slow utility "
                            "(Swap Memory) before you can slow a proactive IC."),
        })
        return False, False

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
        return False, False

    ok, reason = _slow_target_eligibility(target)
    if not ok:
        raise HTTPException(
            400,
            f"Slow cannot target {target.get('type', 'that IC')}-"
            f"{target.get('rating', '?')}: {reason}",
        )

    # -- To-hit: Computer Test (decker_pool) vs the host combat TN; Targeting eases it -2 --------
    # vr2 L2028: the to-hit column is the TARGET's status. The target is an IC (a Legitimate host
    # resident), so Slow always uses the Legitimate column -- not the PC-attacker's own status.
    to_hit_tn = rules.COMBAT_TN[sec_code][_combat_target_status(target)]
    slow_opts = (decker.get("program_options") or {}).get("slow") or {}
    if bool(slow_opts.get("targeting")):
        to_hit_tn = max(2, to_hit_tn - 2)
    ic_rating = target.get("rating", 1)
    to_hit = eng.roll_dice(max(1, decker_pool), to_hit_tn)
    _spend_one_shot(state, decker, "slow")
    if to_hit["successes"] <= 0:
        all_ones = to_hit.get("ones", 0) >= to_hit.get("pool", 0) and to_hit.get("successes", 0) == 0
        _append_event(state, {
            "type": "ic_slowed", "outcome": "missed",
            "ic_id": target["id"], "ic_type": target["type"], "ic_rating": ic_rating,
            "decker_roll": to_hit,
            "description": (f"{src}-{rating} vs {target['type']}-{ic_rating}: missed "
                            f"(0 hits vs TN {to_hit_tn}) -- the IC keeps its speed."),
        })
        return True, all_ones

    # -- Opposed Resistance (Slow Rating) Test for the IC ---------------------------------------
    res = eng.slow_test(decker_pool=rating, slow_rating=rating, ic_dice=ic_rating)
    net = res["net_successes"]
    if net <= 0:
        _append_event(state, {
            "type": "ic_slowed", "outcome": "resisted",
            "ic_id": target["id"], "ic_type": target["type"], "ic_rating": ic_rating,
            "decker_roll": res["decker_roll"], "ic_roll": res["ic_roll"], "net_successes": net,
            "description": "The IC is unaffected by your Slow.",
        })
        return True, False   # IC won the opposed test -> degrade DINAB, but the to-hit was not all-1s

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
        tail = ("it HANGS -- no actions left this Round "
                "(resumes next round unless suppressed).")
    else:
        outcome = "slowed"
        tail = (f"it loses {lost_now} action(s) this round "
                f"({remaining} of {ic_passes} remaining).")
    _append_event(state, {
        "type": "ic_slowed", "outcome": outcome,
        "ic_id": target["id"], "ic_type": target["type"], "ic_rating": ic_rating,
        "decker_roll": res["decker_roll"], "ic_roll": res["ic_roll"],
        "net_successes": net, "actions_lost": new_lost, "hung": remaining <= 0,
        "description": (f"{src}-{rating} beats {target['type']}-{ic_rating} on the opposed test "
                        f"(net {net}) -- {tail}"),
    })
    return False, False   # attacker won the opposed test -> a hit, never degrades DINAB


def _toggle_entry_suppression(state: dict, decker: dict, *, entry: dict, release: bool) -> dict:
    """Suppress or release a NON-IC suppression entry (a data bomb detonation, etc.) registered by
    ``_register_suppression``. Mirrors the crashed-IC path: suppressing refunds the tally this event
    added and costs 1 Detection Factor (applied live by ``_effective_detection_factor``); releasing
    re-adds the tally and restores the DF, and is one-way (a released entry can never be re-suppressed).
    Neither direction costs an action -- suppression is an out-of-band immediate query, not part of the
    action economy. Returns the entry dict; raises HTTPException on an invalid request."""
    rating = int(entry.get("rating", 0) or 0)
    label = entry.get("label", "event")
    if release:
        # RELEASE covers two cases, mirroring the crashed-IC path: (a) releasing an entry that IS
        # suppressed (re-add the deferred tally, restore DF) and (b) ACCEPTING a still-pending entry
        # (the decker declines to suppress during the immediate query) -- its tally is already
        # applied, so accepting only closes the decision so the sheaf can finally see it.
        if entry.get("released"):
            raise HTTPException(400, "That event was already released -- nothing to release")
        was_suppressed = bool(entry.get("suppressed"))
        entry["suppressed"] = False
        entry["released"] = True   # one-way; also closes a pending decision
        if was_suppressed:
            state["security_tally"] = state.get("security_tally", 0) + rating
            tally_note = f"tally +{rating}"
        else:
            tally_note = f"tally +{rating} accepted (already applied)"
        # C10 merge: a data-bomb detonation records the (un)suppressed outcome on its own line.
        if not _finalize_data_bomb_suppression(state, entry, suppressed=False):
            _append_event(state, {
                "type": "suppression_released", "suppression_id": entry["id"],
                "description": (f"Suppression released ({label}) -- Detection Factor restored; "
                                f"{tally_note}."),
            })
        _check_and_activate_sheaf(state, state["host_security_code"])
    else:
        if entry.get("released"):
            raise HTTPException(400, "That event was already released -- it can no longer be suppressed")
        if entry.get("suppressed"):
            raise HTTPException(400, "That event is already suppressed")
        _assert_suppression_df_room(state, decker)   # each suppression costs 1 DF; can't go below the floor
        entry["suppressed"] = True
        state["security_tally"] = max(0, state.get("security_tally", 0) - rating)  # refund the tally
        df = _effective_detection_factor(state, decker)
        state["detection_factor"] = df
        # C10 merge: a data-bomb detonation folds the result into its own line; every other source
        # keeps the standalone suppression event.
        if not _finalize_data_bomb_suppression(state, entry, suppressed=True):
            _append_event(state, {
                "type": "suppression_added", "suppression_id": entry["id"],
                "description": (f"Suppressed ({label}) -- Detection Factor {df}; "
                                f"tally of {rating} suppressed."),
            })
    return entry


def _flush_pending_suppressions(state: dict, sec_code: str | None) -> None:
    """Auto-accept every still-UNDECIDED suppression immediate query (a fresh crash or a data-bomb
    detonation the decker neither suppressed nor accepted). The suppress/accept decision is an
    out-of-band query raised the instant the event fires; it must not persist past the pass/turn it
    was raised on -- otherwise a decker could indefinitely defer a sheaf step by leaving the query
    open. Accepting closes the decision (the tally was already applied), releasing the held-back
    increment to the sheaf. Idempotent: items already suppressed/released/accepted are skipped."""
    flushed = 0
    for ic in state.get("active_ic", []):
        if (ic.get("crash_pending")
                and not ic.get("suppressed") and not ic.get("suppression_released")):
            ic["crash_pending"] = False
            ic["suppression_released"] = True   # decided (accepted): one-way, cannot suppress later
            flushed += 1
        if ic.get("relocate_suppress_pending") and not ic.get("suppressed"):
            # A held Relocate suppress offer the decker never took -- it lapses at turn end. The
            # trace was already spoofed for the turn, so no state beyond the offer flag is affected.
            ic["relocate_suppress_pending"] = False
            flushed += 1
    for s in state.get("suppressions", []):
        if not s.get("suppressed") and not s.get("released"):
            s["released"] = True   # accepted
            # C10 merge: fold the auto-accept (unsuppressed) outcome into the detonation line.
            _finalize_data_bomb_suppression(state, s, suppressed=False)
            flushed += 1
    if flushed:
        _append_event(state, {
            "type": "suppressions_flushed",
            "description": (f"{flushed} pending suppression decision(s) auto-accepted at pass/turn "
                            "end -- held-back security tally now applies."),
        })
        if sec_code is not None:
            _check_and_activate_sheaf(state, sec_code)


def _toggle_ic_suppression(state: dict, decker: dict, *, ic_id: str, release: bool) -> dict:
    """Suppress or release a crashed OR hung IC (vr2_rules.md Suppression L418-424 + Slow L1578).

    Mutates ``state`` in place; raises HTTPException on an invalid request; returns the ic dict.

    Suppression is declared the moment an IC is neutralized -- either it CRASHED (crashing added its
    rating to the security tally) or it HANGS from a Slow strike (its passes drained to 0 for the
    turn; Slow adds NO tally). The decker absorbs 1 Detection Factor per suppressed IC (applied live
    by ``_effective_detection_factor``): for a crashed IC this defers the crash tally, for a hung IC
    there is nothing to defer. Releasing a suppressed IC restores the DF; a crashed IC re-adds its
    rating to the tally (the deferred crash increase), a hung IC re-adds nothing (the "appropriate
    amount" for a hang is 0). Neither suppress nor release costs an action -- suppression is an
    out-of-band immediate query, done at any time on the decker's turn. A released IC can NEVER be
    re-suppressed; the DF cannot fall below 1 (enforced by ``_effective_detection_factor``).

    A THIRD suppression source exists but is declared elsewhere (the relocate handler, not here): a
    Trace IC paused by a won Relocate (vr2 L588) carries ``suppress_mode == "trace"``. This function's
    RELEASE path handles it -- resuming the trace in place with no tally and leaving it re-suppressible
    (unlike the one-way crash/hung modes).
    """
    ic = next((c for c in state.get("active_ic", [])
               if c.get("id") == ic_id), None)
    if ic is None:
        # Not an IC id -- try a non-IC suppression entry (data bomb, etc.) in state["suppressions"].
        entry = next((s for s in state.get("suppressions", [])
                      if s.get("id") == ic_id), None)
        if entry is not None:
            return _toggle_entry_suppression(state, decker, entry=entry, release=release)
        raise HTTPException(404, f"IC {ic_id} not found")

    rating = ic.get("rating", 0)
    crash_tally = int(ic.get("crash_tally", rating) or 0)   # exact tally the crash added (skulk-masked)
    crashed = ic.get("status") == "crashed"
    if release:
        # RELEASE covers two cases: (a) releasing an IC that IS suppressed (restore DF, re-add the
        # deferred tally), and (b) ACCEPTING a still-pending fresh crash (the decker declines to
        # suppress during the immediate query) -- the tally is already applied, so accepting only
        # closes the decision so the sheaf can finally see it.
        was_suppressed = bool(ic.get("suppressed"))
        was_pending = bool(ic.get("crash_pending"))
        if not was_suppressed and not was_pending:
            raise HTTPException(400, "IC is not suppressed -- nothing to release")
        ic["suppressed"] = False
        ic["crash_pending"] = False   # decision made -- stop holding this crash back from the sheaf
        if ic.get("suppress_mode") == "trace":
            # A trace suppressed via a won Relocate (vr2 L588) was merely PAUSED -- releasing lets it
            # resume its cycle exactly where it left off (phase/location remaining were untouched),
            # adds no tally, and can be suppressed again by another successful Relocate (NOT one-way).
            ic.pop("suppress_mode", None)
            tally_note = "no tally change (trace resumes its cycle)"
        else:
            ic["suppression_released"] = True   # one-way: a crashed/hung IC cannot be re-suppressed
            if crashed and was_suppressed:
                # A crashed IC's suppression had refunded the crash tally -- releasing re-adds it.
                state["security_tally"] = state.get("security_tally", 0) + crash_tally
                tally_note = f"tally +{crash_tally} -> {state['security_tally']}"
            elif crashed:
                # Accept-from-pending: the crash tally is already applied, so accepting adds nothing
                # new -- it just lets the (previously held-back) increment reach the sheaf.
                tally_note = f"tally +{crash_tally} accepted (already applied)"
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
        # A THIRD path: a won Relocate that could not afford the DF cost left the trace spoofed with
        # ``relocate_suppress_pending`` (the held offer). Once the decker frees a DF point, Suppress
        # here converts that held offer into a real trace-pause (mode 'trace'; no tally to refund).
        relocate_pending = bool(ic.get("relocate_suppress_pending"))
        if not (crashed or hung or relocate_pending):
            raise HTTPException(
                400, "Only a crashed or hung IC may be suppressed (declare it on the crash/hang)")
        if ic.get("suppression_released"):
            raise HTTPException(400, "This IC was already released -- it can no longer be suppressed")
        if ic.get("suppressed"):
            raise HTTPException(400, "IC is already suppressed")
        _assert_suppression_df_room(state, decker)   # each suppression costs 1 DF; can't go below the floor
        ic["suppressed"] = True
        ic["crash_pending"] = False   # decision made -- the crash is now suppressed, not pending
        ic["relocate_suppress_pending"] = False   # held Relocate offer (if any) now taken
        if crashed:
            state["security_tally"] = max(0, state.get("security_tally", 0) - crash_tally)  # refund crash tally
        elif relocate_pending and not hung:
            # A trace has no crash tally to refund; taking the held Relocate offer pauses it in place.
            ic["suppress_mode"] = "trace"   # re-suppressible; release resumes the cycle (not one-way)
            ic.pop("trace_spoofed_turn", None)   # upgraded from a per-turn spoof to a full pause
        # (A hung IC added no tally, so there is nothing to refund.)
        df = _effective_detection_factor(state, decker)
        state["detection_factor"] = df
        _append_event(state, {
            "type": "ic_suppressed", "ic_id": ic["id"],
            # The suppression's tally refund is intentionally NOT shown here: crashing already logged
            # the "+N", and suppression merely holds it back (net zero), so a "-N" line read as a loss.
            # The Suppressions panel shows the tally that returns if the IC is released.
            "description": f"IC suppressed -- Detection Factor {df}.",
        })
    return ic


# -- DINAB ("Decker In A Box") program option (vr2_rules.md L1665) -------------------------------
# DINAB gives a utility a built-in Computer skill = the DINAB rating. The decker may spend a Free
# Action to let ONE DINAB-equipped program run itself autonomously (skill = effective DINAB rating)
# while still spending their Complex/2-Simple on their own action -- effectively a second ally that
# fires for free each pass. Only one DINAB fires per pass (it costs the single Free action), and a
# program run by DINAB this pass may NOT also be used by hand this pass (enforced via
# state["dinab_prog_this_pass"] / state["manual_progs_this_pass"]).
#
# DINAB degrades -1 each time the program FAILS (lost opposed System Test, missed cybercombat, or
# target reduces all damage to 0); a FAILED roll of all 1s CRASHES it (reload via Swap Memory). The
# self-targeted defensive programs (Medic, Restore) never degrade the DINAB rating -- there is no
# opposed test to lose -- though Medic still wears its OWN -1/use (its rule applies whether run by
# hand or by DINAB) and Restore has no wear at all (pure upside). Build-time rating is carried in
# decker["program_options"][util].dinab. Wear is tracked in state["dinab_damage"][util]
# (player-visible -- the decker's own deck); a crash sets program_damage[util]=base (effective-0,
# reload via Swap Mode-3) and clears the dinab wear (a fresh copy is pristine).
#
# Routing by program family: Medic/Restore run their own self-heal/repair at the DINAB pool;
# Slow/Steamroller reuse their anti-IC resolvers at the DINAB pool; Attack/Poison/Restrict/Reveal/
# Hog reuse the cybercombat / crippler resolution; every other (operational) utility fires a generic
# System Test. Black Hammer / Killjoy CANNOT carry DINAB (RAW: lethal programs are hand-run only).
_DINAB_OFFENSIVE = ("attack", "poison", "restrict", "reveal", "hog")
_DINAB_SELF_TARGETED = ("medic", "restore")   # never degrade the DINAB rating (no opposed test)
_DINAB_ANTI_IC = ("slow", "steamroller")       # target a host IC; resolver returns (failed, all_ones)


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
    L1665). The program acts at skill = effective DINAB rating with NO extra Complex/Simple spend,
    and auto-targets (the app is the GM). Routing by family:

    - Medic / Restore: self-heal / repair at the DINAB pool; NEVER degrade the DINAB rating (Medic
      still wears its own -1/use; Restore has no wear).
    - Slow / Steamroller: reuse their anti-IC resolvers at the DINAB pool; degrade on a miss / IC win.
    - Attack / Poison / Restrict / Reveal / Hog: cybercombat / crippler resolution; degrade on miss
      or fully-resisted damage.
    - Everything else (operational): a generic System Test; degrade on a lost opposed test.

    A failed run degrades DINAB (-1); a failed all-1s run crashes it. <=0 effective DINAB, or a
    program the decker already used by hand this pass, is rejected (400)."""
    key = _normalize_util_name(util)
    if not key:
        raise HTTPException(400, "DINAB needs target_program -- the DINAB-equipped utility to run.")
    eff = _effective_dinab(decker, state, key)
    if eff <= 0:
        raise HTTPException(
            400,
            f"{key.replace('_', ' ').title()} has no usable DINAB rating (not DINAB-equipped, "
            "worn out, or crashed -- reload via Swap Memory).")
    if key in state.get("manual_progs_this_pass", []):
        raise HTTPException(
            400,
            f"You already used {key.replace('_', ' ').title()} by hand this pass -- it cannot also "
            "run autonomously via DINAB until your next pass.")

    if key == "medic":
        _apply_medic(state, decker, pool_override=eff, via_dinab=True)
    elif key == "restore":
        _apply_restore(state, decker, target="", pool_override=eff, via_dinab=True)
    elif key == "slow":
        failed, all_ones = _apply_slow(state, decker, sec_code=sec_code, decker_pool=eff,
                                       target_ic_id=target_ic_id, via_dinab=True)
        _dinab_resolve_failure(state, decker, key, failed, all_ones)
    elif key == "steamroller":
        failed, all_ones = _apply_steamroller(state, decker, sec_code=sec_code, decker_pool=eff,
                                              target_ic_id=target_ic_id, via_dinab=True)
        _dinab_resolve_failure(state, decker, key, failed, all_ones)
    elif key in _DINAB_OFFENSIVE:
        _dinab_offense(state, decker, key, eff, sec_code=sec_code, target_ic_id=target_ic_id)
    else:
        _dinab_operate(state, decker, key, eff, subsystem=subsystem,
                       subsystem_rating=subsystem_rating, sec_value=sec_value, det_factor=det_factor)

    # Lock this program out of a manual use for the rest of the pass (and vice versa is already
    # enforced above). Only when the action economy is tracked (legacy runs skip the lock).
    if "pass_action_points" in state:
        state["dinab_prog_this_pass"] = key


def _dinab_operate(state: dict, decker: dict, util: str, eff: int, *, subsystem: str,
                   subsystem_rating: int, sec_value: int, det_factor: int) -> None:
    """A DINAB operational program runs one autonomous System Test at pool = DINAB rating vs the
    named subsystem. Tally rises by the host's successes; a lost opposed test degrades DINAB (-1)
    and an all-1s loss crashes it. Emits a player-visible dinab_op event."""
    test = eng.system_test(decker_pool=eff, subsystem_rating=subsystem_rating,
                           security_value=sec_value, det_factor=det_factor)
    applied = _bump_security_tally(state, test["tally_increase"])
    failed = not test["success"]
    dr = test["decker_roll"]
    all_ones = failed and dr.get("ones", 0) >= dr.get("pool", 0) and dr.get("successes", 0) == 0
    _append_event(state, {
        "type": "dinab_op", "utility": util, "subsystem": subsystem, "success": test["success"],
        "decker_roll": dr, "host_roll": test["host_roll"],
        "tally_increase": applied, "tally_total": state["security_tally"],
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
    """DINAB Attack vs an active IC, resolved through the SHARED eng.cybercombat_attack -- the same
    primitive every other attack direction uses (PC->IC, IC->PC, decker->PC) -- so a DINAB-driven
    Attack cannot drift from hand cybercombat. The DINAB runs the Attack program at its effective
    rating: attacker pool = eff, attack Power = eff (+ any Party-IC cluster). Returns (failed,
    all_ones); failed on a whiff (no net to-hit successes), which degrades the DINAB (an all-1s
    whiff crashes it). On a crash the IC is removed and the tally rises (Skulk reduces the bump)."""
    sec_value = state["host_security_value"]
    opts = (decker.get("program_options") or {}).get("attack") or {}
    cluster_penalty = _cluster_size(state, target_ic.get("cluster_id"))
    shield_shift = _shield_shift_tn_modifier(target_ic, penetration=bool(opts.get("penetration")),
                                             chaser=bool(opts.get("chaser")))
    # All to-hit modifiers ride in via tn_modifier so the core rolls one identical way (cluster +
    # Shield/Shift raise the TN; Targeting lowers it). The IC resists with a Bod-style Resistance
    # Test (Security Value +/- Expert) vs the attack Power; Armor reduces that Power.
    tn_mod = cluster_penalty + shield_shift - (2 if opts.get("targeting") else 0)
    ic_resist_pool = max(1, sec_value + _ic_expert(target_ic, "defense") - _ic_expert(target_ic, "offense"))
    ic_armor = 2 if _ic_has_armor(target_ic) else 0
    attack = eng.cybercombat_attack(
        attacker_pool=max(1, eff),
        security_code=sec_code,
        target_status=_combat_target_status(target_ic),   # IC = Legitimate host resident (vr2 L2028)
        target_bod=ic_resist_pool,
        armor_rating=ic_armor,
        ic_rating=eff + cluster_penalty,   # Power = DINAB effective rating (+ cluster, per canonical)
        attacker_is_ic=False,
        tn_modifier=tn_mod,
        base_damage_level=_attack_damage_level(decker, sec_code),
    )
    attack_roll = attack["attack_roll"]
    final_dmg = attack["resistance"]["final_damage_level"]
    boxes = attack["resistance"]["boxes"]
    target_ic["boxes"] = target_ic.get("boxes", 0) + boxes
    failed = attack_roll["successes"] <= 0  # a whiff (no net to-hit successes)
    all_ones = attack_roll.get("ones", 0) >= attack_roll.get("pool", 0) and attack_roll["successes"] == 0
    if target_ic["boxes"] >= 10:
        target_ic["status"] = "crashed"
        skulk = max(0, int(opts.get("skulk", 0) or 0))
        bump = max(0, target_ic["rating"] - skulk)
        applied = _bump_security_tally(state, bump)
        # Fresh crash = suppressible immediate query: hold this increment from the sheaf until decided.
        target_ic["crash_tally"] = applied
        target_ic["crash_pending"] = True
        target_ic["crash_turn"] = state.get("current_turn", 1)
        _append_event(state, {
            "type": "ic_crashed", "ic_id": target_ic["id"], "tally_increase": applied,
            "description": (f"DINAB Attack-{eff} CRASHED {target_ic['type']}-{target_ic['rating']}. "
                            f"Tally +{applied} -> {state['security_tally']}"),
        })
        _check_and_activate_sheaf(state, sec_code)
        # Trap IC destroyed in cybercombat triggers its hidden IC (vr2 L688); a Trap Trace crashed
        # mid-hunt is defused instead (its hidden IC triggers only on location-cycle completion).
        if not _ic_is_trace(target_ic):
            _spawn_trap_hidden(state, target_ic, sec_code)
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
    poison/restrict/reveal -> cripple Bod/Evasion/Masking; hog -> drain the enemy's highest running
    program. Returns (failed, all_ones); failed when the strike does nothing (no reduction / no
    boxes). (Black Hammer / Killjoy cannot carry DINAB, so no lethal branch here.)"""
    util_r = decker.get("utilities") or {}
    if util in _PROGRAM_ATTR:
        attr = _PROGRAM_ATTR[util]
        target_rating = _enemy_effective_attr(enemy, attr)
        cr = _resolve_attribute_attack(
            state, attacker_pool=eff, resist_tn=int(util_r.get(util, eff) or eff),
            target_attr_rating=target_rating, attr=attr, sec_code=sec_code,
            target_status=_combat_target_status(enemy), target_kind="enemy", enemy=enemy,
            causing_rating=int(util_r.get(util, eff) or eff))
        reduction = cr["reduction"]
        new_val = cr["new_value"]
        ar = cr["attack_roll"]
        if reduction > 0:
            dinab_desc = f"DINAB {util.title()}-{eff} cripples {_enemy_display_name(enemy)}'s {attr.title()} -> {new_val}."
        else:
            dinab_desc = f"{_enemy_display_name(enemy)} resisted your DINAB {util.title()}."
        _append_event(state, {"type": "dinab_attack", "enemy_id": enemy["id"], "utility": util,
            "success": reduction > 0, "decker_roll": ar,
            "description": dinab_desc})
        return reduction <= 0, ar.get("ones", 0) >= ar.get("pool", 0) and ar["successes"] == 0
    if util == "hog":
        # DINAB Hog vs an enemy decker uses the SAME resolver the enemy uses against the PC: a
        # hit seeds a persistent infection (re-drained each Combat Turn by _drain_all_hog_infections)
        # and applies the first drain now. Modelled once for both directions.
        res = _resolve_hog(state, _hog_target_for_enemy(state, enemy), attacker_id="pc",
                           attacker_pool=eff, hog_rating=int(util_r.get("hog", eff) or eff),
                           sec_code=sec_code, target_status=_combat_target_status(enemy))
        ar = res["attack_roll"]
        if res["infected"] and res["drained"]:
            desc = (f"DINAB Hog-{eff} infects {_enemy_display_name(enemy)} (drains {res['reduction']}/turn): "
                    f"{res['drained'].replace('_', ' ').title()} -{res['applied']}"
                    f"{' (CRASHED)' if res['crashed'] else ''}.")
        elif res["infected"]:
            desc = f"DINAB Hog-{eff} infects {_enemy_display_name(enemy)} but it has no running program left to drain."
        else:
            desc = f"DINAB Hog-{eff} fails to take hold on {_enemy_display_name(enemy)} this pass."
        _append_event(state, {"type": "dinab_attack", "enemy_id": enemy["id"], "utility": "hog",
            "success": res["infected"], "decker_roll": ar, "description": desc})
        return (not res["infected"]), ar.get("ones", 0) >= ar.get("pool", 0) and ar["successes"] == 0
    atk = eng.cybercombat_attack(attacker_pool=eff, security_code=sec_code,
                                 target_status=_combat_target_status(enemy),
                                 target_bod=_enemy_effective_attr(enemy, "bod"), armor_rating=_enemy_armor(enemy),
                                 ic_rating=int(util_r.get("attack", 4) or 4),
                                 attacker_is_ic=False,
                                 base_damage_level=_attack_damage_level(decker, sec_code))
    boxes = atk["resistance"]["boxes"]
    ecm = enemy.setdefault("condition_monitor", {})
    _add_cm_damage(ecm, "persona_boxes", boxes)
    _wear_armor(state, enemy, enemy, boxes, gm_only=True, actor=enemy.get("name") or "Security decker")
    if ecm["persona_boxes"] >= 10:
        enemy["status"] = "crashed"
        enemy["outcome"] = "dumped"
        enemy["end_reason"] = "icon_crashed"
    ar = atk["attack_roll"]
    if boxes > 0:
        dinab_atk_desc = f"DINAB Attack-{eff} strikes {_enemy_display_name(enemy)} ({boxes} boxes)."
    else:
        dinab_atk_desc = "DINAB attack fully resisted. DINAB rating reduced as enemy learns attack patterns!"
    _append_event(state, {"type": "dinab_attack", "enemy_id": enemy["id"], "utility": "attack",
        "success": boxes > 0, "decker_roll": ar,
        "description": dinab_atk_desc})
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
    _bump_security_tally(state, test["tally_increase"])
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


def _apply_decompress_program(state: dict, decker: dict, *, target_program: str) -> bool:
    """Decompress a Squeezed program that was swapped into active memory (vr2_rules.md L1673:
    "Cannot be used until decompressed -- Complex Action, no test required"). Pure bookkeeping --
    it moves the program out of the ``squeezed_active`` holding area into ``decker.utilities`` so
    every effective-rating / auto-defense path now sees it. The program already occupies its full
    active footprint (charged when it was swapped in), so there is NO memory check here. Returns
    True when a program was expanded (the caller must persist ``decker``); a missing target emits a
    no-op event and returns False (never a crash)."""
    name = (target_program or "").strip().lower()
    squeezed_active = state.setdefault("squeezed_active", [])
    ent = next((p for p in squeezed_active
                if str(p.get("name", "")).strip().lower() == name), None)
    pretty = str(name).replace("_", " ").title()
    if not name or ent is None:
        _append_event(state, {
            "type": "program_decompressed", "outcome": "no_target",
            "description": (
                f"Decompress: no compressed program \"{pretty}\" in active memory to expand."
                if name else
                "Decompress: name a compressed program in active memory to expand."
            ),
        })
        return False
    squeezed_active.remove(ent)
    utils = decker.setdefault("utilities", {})
    sizes = state.setdefault("program_sizes", {})
    rating = int(ent.get("rating", 0) or 0)
    utils[name] = rating
    sizes[name] = int(ent.get("size", sizes.get(name, 0)) or 0)
    state.setdefault("program_damage", {}).pop(name, None)   # fresh copy -- no accrued damage
    _append_event(state, {
        "type": "program_decompressed", "outcome": "ok", "program": name,
        "description": (f"Decompressed {pretty} (rating {rating}) -- now usable in active memory."),
    })
    return True


def _register_suppression(state: dict, *, source: str, label: str, rating: int) -> dict:
    """Register a non-IC suppressible tally event (a data bomb detonation, etc.) so the decker can
    later choose to suppress it (vr2 Suppression, generalized from crashed IC). The tally has ALREADY
    been applied by the caller; ``rating`` is how much this event added (what a suppression refunds
    and a later release re-adds). Appends an entry to ``state['suppressions']`` and returns it. The
    entry is undecided (``suppressed``/``released`` both False) until the player acts on it."""
    entry = {
        "id": f"sup-{len(state.get('suppressions', []))}-{state.get('current_turn', 1)}",
        "source": source,
        "label": label,
        "rating": int(rating),
        "suppressed": False,
        "released": False,
        "turn": state.get("current_turn", 1),
    }
    state.setdefault("suppressions", []).append(entry)
    return entry


def _finalize_data_bomb_suppression(state: dict, entry: dict, *, suppressed: bool) -> bool:
    """C10 merge: fold the suppress/unsuppress outcome back into the ORIGINAL data-bomb detonation
    event so the player sees ONE line that ends "Bomb suppressed." / "Bomb unsuppressed." once the
    immediate query resolves -- instead of a separate suppression event. Returns True when it
    handled a ``data_bomb`` entry (so the caller skips emitting the generic suppression event)."""
    if entry.get("source") != "data_bomb":
        return False
    sid = entry.get("id")
    for ev in reversed(state.get("event_log", [])):
        if ev.get("type") == "data_bomb" and ev.get("suppression_id") == sid:
            base = ev.get("description", "").replace(" Suppression pending.", "").rstrip()
            ev["description"] = base + (
                " Bomb suppressed." if suppressed else " Bomb unsuppressed.")
            break
    return True


def _detonate_data_bomb(state: dict, decker: dict, eff: dict, *, ic_rating: int,
                        sec_value: int, sec_code: str, headline: str) -> dict:
    """Resolve a Data Bomb explosion (vr2_rules.md L475-480): a fixed (IC Rating)M against the
    persona (Bod resists, the Armor utility reduces Power, a Shield parry stages the resolved
    damage down), then add the bomb's rating to the security tally and check the sheaf. Mutates
    ``state`` in place and emits a player-visible ``data_bomb`` detonated event headed by
    ``headline`` (e.g. "DATA BOMB on Monthly Payroll"). Returns the detonation result dict.

    The bomb-rating tally is applied immediately; per vr2 L479 the decker MAY then spend 1 Detection
    Factor to suppress the IC and avoid that tally. That choice is post-hoc (an immediate query, not
    part of the action economy), so the detonation registers a suppression entry the decker can act
    on afterward (``_register_suppression`` -> the /suppress endpoint), exactly like a crashed IC.

    Single source of truth for the three ways a bomb goes off: an undefused access trigger, an
    all-1s botched defuse, and an Exploding Scramble's linked bomb."""
    shield_succ = _shield_parry(state, decker, attacker_skill=sec_value, context="data bomb")
    det = eng.data_bomb_detonate(
        ic_rating=ic_rating, target_bod=eff["bod"],
        armor_rating=_effective_armor(decker, state),
        shield_successes=shield_succ)
    cm = state.setdefault("condition_monitor", {})
    _add_cm_damage(cm, "persona_boxes", det["resistance"]["boxes"])
    _wear_armor(state, state, decker, det["resistance"]["boxes"])
    applied = _bump_security_tally(state, det["tally_increase"])
    sup = None
    if applied > 0:
        sup = _register_suppression(state, source="data_bomb", label=headline, rating=applied)
    boxes = det["resistance"]["boxes"]
    dmg_part = (f"{det['resistance']['final_damage_level']} damage."
                if boxes > 0 else "All damage resisted.")
    # The suppress/unsuppress outcome is appended to THIS line once the player resolves the
    # immediate query (C10 merge -- see _finalize_data_bomb_suppression); until then it is pending.
    # No tally_increase field: the suppressed/unsuppressed suffix is the player's tally signal, so
    # the generic "Security tally increased." redaction must NOT also fire on this event.
    _append_event(state, {
        "type": "data_bomb", "outcome": "detonated",
        "damage_level": det["resistance"]["final_damage_level"],
        "suppression_id": (sup or {}).get("id"),
        "suppressible": bool(sup),
        "description": (
            f"{headline} detonated -- {dmg_part}"
            + (" Suppression pending." if sup else "")
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


def _host_security_rating_str(state: dict) -> str:
    """Composed "Code-Value" host Security Rating (e.g. "Red-9") from the live run state. Reads the
    un-redacted state (engine context), so the real code/value are present here even though they are
    stripped from the player payload until ``host_security_revealed``."""
    code = state.get("host_security_code", "Green")
    val = state.get("host_security_value", 6)
    return f"{code}-{val}"


def _apply_analyze_host(state: dict, net_successes: int) -> dict:
    """Analyze Host success handler (vr2 System Operations: Control test, Analyze utility).

    Reveals the host's subsystem ratings. The revealable set is the 5 ACIFS ratings (Access,
    Control, Index, Files, Slave) PLUS the host Security Rating (code + value) -- 6 items in all.
    The raw ACIFS ratings live in GM-only ``host_acifs`` and mirror into the player-visible
    ``host_ratings_revealed`` map in ACIFS order; the Security Rating is gated by the separate
    ``host_security_revealed`` flag (its code/value stay redacted until it flips). USER OVERRIDE of
    RAW: VM status is not modeled, and the "reveal all" threshold is 6+ net successes (not RAW's 7).

    Let ``net`` = net successes and ``U`` = number of still-hidden items (hidden ACIFS + security if
    not yet revealed). On a successful test:
      * ``net >= 6`` OR ``net >= U`` -> auto-reveal ALL still-hidden items now (no choice to make)
        and clear any banked pending.
      * ``1 <= net < U`` -> a genuine choice exists: BANK ``host_analyze_pending`` = {credits, turn}
        and reveal nothing yet (the decker then picks which to reveal via _reveal_host_ratings).
        A later banking roll REPLACES the previous pending credits.
      * no still-hidden items at all -> nothing to reveal; clear any pending.

    Mutates ``state`` and appends a ``host_analyzed`` event. Returns a small summary
    ``{"revealed": [{"subsystem": nm, "rating": rt}, ...], "pending": <credits or 0>}``. The caller
    is responsible for pushing a newly revealed Security Rating onto the org LTG listing
    (``sync_host_security_to_org``) -- this pure helper has no DB access.
    """
    acifs = state.get("host_acifs") or [10, 10, 10, 10, 10]
    names = ["access", "control", "index", "files", "slave"]
    revealed = state.setdefault("host_ratings_revealed", {})
    hidden = [nm for nm in names if nm not in revealed]
    sec_hidden = not state.get("host_security_revealed")
    hidden_count = len(hidden) + (1 if sec_hidden else 0)
    net = max(0, int(net_successes))

    if hidden_count == 0:
        state.pop("host_analyze_pending", None)
        _append_event(state, {
            "type": "host_analyzed", "revealed": [],
            "description": "Analyze Host -- all subsystem ratings already known.",
        })
        return {"revealed": [], "pending": 0}

    # Reveal-all: 6+ net successes, or enough successes to cover every still-hidden item anyway.
    if net >= 6 or net >= hidden_count:
        newly: list[dict] = []
        for i, nm in enumerate(names):
            if nm in hidden:
                revealed[nm] = int(acifs[i]) if i < len(acifs) else 10
                newly.append({"subsystem": nm, "rating": revealed[nm]})
        if sec_hidden:
            state["host_security_revealed"] = True
            newly.append({"subsystem": "security", "rating": _host_security_rating_str(state)})
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
    # decker choose which hidden items to reveal via /reveal-host-ratings (reveal NOTHING yet).
    credits = max(1, net)
    state["host_analyze_pending"] = {
        "credits": credits,
        "turn": state.get("current_turn", 1),
    }
    reveals = min(credits, hidden_count)
    _append_event(state, {
        "type": "host_analyzed", "revealed": [],
        "description": f"Analyze Host succeeded -- choose {reveals} subsystem rating(s) to reveal.",
    })
    return {"revealed": [], "pending": credits}


def _reveal_host_ratings(state: dict, subsystems: list[str]) -> list[tuple[str, int | str]]:
    """Phase two of Analyze Host (vr2 override): spend banked Analyze Host credits by choosing which
    still-hidden items to reveal. Reads ``host_analyze_pending`` (banked by ``_apply_analyze_host``
    when the decker rolled fewer net successes than there were hidden items); reveals the chosen
    ACIFS ratings from GM-only ``host_acifs`` into the player-visible ``host_ratings_revealed`` map,
    and/or flips ``host_security_revealed`` for the Security Rating; clears the pending; appends a
    ``host_analyzed`` event.

    The pickable set is the 5 ACIFS names plus ``"security"``. Validates the picks: each must be a
    real item, currently hidden, and non-duplicate; the number picked must equal
    ``min(credits, hidden count)``. Raises HTTPException(400) otherwise. Returns the list of revealed
    ``(name, rating)`` tuples (security's rating is the "Code-Value" string). The caller pushes a
    newly revealed Security Rating onto the org LTG listing -- this pure helper has no DB access."""
    pending = state.get("host_analyze_pending") or {}
    credits = int(pending.get("credits", 0) or 0)
    if credits <= 0:
        raise HTTPException(400, "No pending Analyze Host reveals -- run Analyze Host first.")

    names = ["access", "control", "index", "files", "slave"]
    acifs = state.get("host_acifs") or [10, 10, 10, 10, 10]
    revealed = state.setdefault("host_ratings_revealed", {})
    hidden = [nm for nm in names if nm not in revealed]
    sec_hidden = not state.get("host_security_revealed")
    hidden_count = len(hidden) + (1 if sec_hidden else 0)

    picks: list[str] = []
    seen: set[str] = set()
    for raw in (subsystems or []):
        nm = str(raw).strip().lower()
        if nm == "security":
            if not sec_hidden:
                raise HTTPException(400, "Security Rating is already revealed.")
        elif nm not in names:
            raise HTTPException(400, f"Unknown subsystem: {raw!r}.")
        elif nm in revealed:
            raise HTTPException(400, f"Subsystem '{nm}' is already revealed.")
        if nm in seen:
            raise HTTPException(400, f"Duplicate subsystem: '{nm}'.")
        seen.add(nm)
        picks.append(nm)

    need = min(credits, hidden_count)
    if len(picks) != need:
        raise HTTPException(400, f"Choose exactly {need} subsystem rating(s) to reveal.")

    result: list[tuple[str, int | str]] = []
    for nm in picks:
        if nm == "security":
            state["host_security_revealed"] = True
            result.append(("security", _host_security_rating_str(state)))
        else:
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
    decoy_boxes = rules.ICON_DAMAGE_BOXES[decoy_staged]
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
    """Resolve a deliberate Defuse Data Bomb operation (vr2_rules.md L463-471, Complex Action): an
    OPPOSED System Test against the bomb's controlling subsystem (Files for a file bomb, Slave for
    a device bomb -- derived from the bomb's own scope by the caller) reduced by the carried Defuse
    utility. Like every system test the host rolls its Security Value vs the Detection Factor and
    its successes add to the security tally on EVERY attempt (user ruling 2026-07-10).

    - Success (decker net successes > host) disarms the bomb. The successful defuse is not a crash,
      so the bomb's RATING is never added to the tally and no suppression is needed -- but the
      opposed host successes from this test still count (normal system-test tally).
    - Rolling ALL 1s on the decker dice detonates the bomb immediately (botch).
    - Any other failure leaves the bomb primed -- the decker may try again (each attempt carries
      the opposed-tally risk) or it triggers later if they access the protected target.

    Targets the bomb on ``target_file`` (decoded-name match, consistent with the surfaced
    discovered_data_bombs) or the first still-armed bomb when none is named. Mutates ``state`` and
    always emits a player-visible ``data_bomb`` event."""
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
    # Opposed host side: the host rolls Security Value vs the Detection Factor; its successes add
    # to the security tally on every attempt (this is a system test, not a crash of the bomb).
    det_factor = _effective_detection_factor(state, decker)
    host_roll = eng.roll_dice(sec_value, det_factor)
    host_succ = host_roll["successes"]
    tally_applied = _bump_security_tally(state, host_succ) if host_succ else 0
    tally_note = (f" Host detected activity: tally +{tally_applied} -> {state['security_tally']}."
                  if tally_applied else "")
    decker_succ = df["roll"]["successes"]
    if df["detonated"]:
        state["data_bombs"] = [b for b in armed if b is not bomb]  # one-shot
        _detonate_data_bomb(state, decker, eff, ic_rating=brating, sec_value=sec_value,
                            sec_code=sec_code,
                            headline=f"Data bomb on {btarget} (botched defuse -- all 1s)")
        return
    # House rule (vr2 line 152, modified): defuse is an opposed System Test, so a TIE goes to
    # the decker -- the bomb is defused on decker_succ >= host_succ. A 0-vs-0 tie is a mutual
    # whiff (nothing happened), so the decker needs at least 1 success to defuse it.
    if decker_succ >= host_succ and decker_succ > 0:
        state["data_bombs"] = [b for b in armed if b is not bomb]
        state.setdefault("defused_bombs", []).append(btarget)
        _append_event(state, {
            "type": "data_bomb", "outcome": "defused", "decker_roll": df["roll"],
            "host_roll": host_roll, "tally_increase": tally_applied,
            "description": (
                f"Data bomb on {btarget} DEFUSED (opposed Computer Test TN {df['tn']} = {subsystem} "
                f"{subsystem_rating} - Defuse {defuse_rating}; {decker_succ} vs {host_succ}). "
                f"No bomb-rating tally -- no suppression needed.{tally_note}"
            ),
        })
        return
    _append_event(state, {
        "type": "data_bomb", "outcome": "primed", "decker_roll": df["roll"],
        "host_roll": host_roll, "tally_increase": tally_applied,
        "description": (
            f"Defuse FAILED (opposed Computer Test TN {df['tn']} = {subsystem} {subsystem_rating} - "
            f"Defuse {defuse_rating}; {decker_succ} vs {host_succ}) -- the data bomb on {btarget} "
            f"stays primed. Try again, or it triggers if you successfully access the protected "
            f"target.{tally_note}"
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
            1: "Sensor sweep: your deck's sensors snag on hidden IC activity (identity unknown).",
            2: f"Sensor sweep identifies the lurking IC as {ic.get('type', '?')} IC.",
            3: f"Sensor sweep pinpoints {ic.get('type', '?')}-{ic.get('rating', '?')} IC and its location.",
        }
        _append_event(state, {
            "type": "ic_detected",
            "ic_id": ic["id"],
            "detection_level": new,
            # The dice behind the sweep are your Sensor roll; the TN is the IC's rating, which you
            # do NOT know until a full ID -- so expose the dice + successes but NOT the target number.
            "sensor_roll": {"dice": roll["dice"], "successes": roll["successes"]},
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
                 if isinstance(ic, dict) and ic.get("status") == "active"
                 and not (_ic_is_trace(ic) and not _trace_is_targetable(ic))]
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


def _npc_position_bonus(state: dict, net: int) -> dict:
    """Shared NPC heuristic for a won Position Attack (vr2 L2004): the winner may take the position
    as a to-hit bonus (-TN) OR channel it into a heavier blow (+Power). An NPC presses for the kill
    with +Power when the PC is already badly wounded (>=5 persona boxes), else takes the easier hit
    (-TN). Used both when an NPC initiates a winning Position Attack and when a PC-initiated one
    backfires and the enemy seizes the positioning instead, so both paths choose identically."""
    pc_persona = int((state.get("condition_monitor", {}) or {}).get("persona_boxes", 0) or 0)
    return {"power_bonus": net} if pc_persona >= 5 else {"tn_reduction": net}


def _apply_maneuver(state: dict, decker: dict, eff: dict, body) -> None:
    """Resolve a PC-initiated combat maneuver (Evade/Parry/Position) against one opposing icon
    (vr2 L1982): the PC is the maneuvering icon (Evasion), the target is the opposing icon
    (Sensor). Mutates ``state`` in place; raises HTTPException on an invalid/absent target."""
    maneuver = body.action_type
    kind, target = _maneuver_target_lookup(state, (body.maneuver_target or "").strip())
    if target is None:
        raise HTTPException(
            400, "No eligible icon to maneuver against (need an active IC or a revealed enemy decker).")
    sec_value = state.get("host_security_value", 6)
    if kind == "ic":
        opp_sensor_dice = sec_value
        opp_sensor_rating = int(target.get("rating", 6) or 6)
        opp_label = str(target.get("type", "IC"))
    else:
        opp_sensor_dice = int(target.get("sensor", 4) or 4)
        opp_sensor_rating = int(target.get("sensor", 4) or 4)
        opp_label = str(target.get("name", "enemy decker"))

    # Cloak (maneuvering side = the PC) lowers the PC's Evasion-test TN; Lock-On (opposing side)
    # lowers the opposing icon's Sensor-test TN. IC carry no utilities; an enemy decker may.
    pc_cloak = int((decker.get("utilities") or {}).get("cloak", 0) or 0)
    opp_lock_on = (int((target.get("utilities") or {}).get("lock_on", 0) or 0)
                   if kind == "enemy" else 0)
    result = eng.maneuver_test(
        maneuvering_evasion_dice=eff.get("evasion", 4),
        maneuvering_evasion_rating=eff.get("evasion", 4),
        opposing_sensor_dice=opp_sensor_dice,
        opposing_sensor_rating=opp_sensor_rating,
        cloak=pc_cloak,
        lock_on=opp_lock_on,
    )
    man_succ = result["maneuvering_roll"]["successes"]
    opp_succ = result["opposing_roll"]["successes"]
    net = result["net_successes"]
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
        subject = opp_label if kind == "enemy" else "Icon"
        tracker = opp_label if kind == "enemy" else "Enemy icon"
        if won:
            _break_parry_on_evade(state, target)
            target["evaded"] = True
            target["evade_dir"] = "lost_pc"      # the PC hid; the icon keeps its place but loses you
            target["redetect_turn"] = current_turn + net
            target["redetect_tally_base"] = tally
            ev["description"] = (
                f"{subject} successfully evaded for {net} turn{'s' if net != 1 else ''}!")
        else:
            ev["description"] = f"Evasion unsuccessful. {tracker} still tracking you..."
    elif maneuver == "parry_attack":
        attacker_ref = f"{opp_label}'s next" if kind == "enemy" else "the next enemy"
        if won:
            state["pc_parry"] = {"vs": target.get("id"), "bonus": net}
            ev["description"] = f"Parry success! +{net} TN penalty applied to {attacker_ref} attack."
        else:
            ev["description"] = "Parry maneuver unsuccessful!"
    else:  # position_attack
        choice = "power" if str(getattr(body, "position_choice", "tn")).strip().lower() == "power" else "tn"
        target_ref = opp_label if kind == "enemy" else "the target"
        if won:
            state["pc_position"] = {"power_bonus": net} if choice == "power" else {"tn_reduction": net}
            ev["position_choice"] = choice
            ev["description"] = f"You gain a position advantage for your next attack against {target_ref}!"
        elif opp_succ > man_succ:
            # Risky maneuver: the opposing icon wins the exchange and gains the positioning instead.
            # The enemy chooses TN vs Power via the same heuristic an NPC-initiated win uses.
            opp_net = opp_succ - man_succ
            target["position_bonus"] = _npc_position_bonus(state, opp_net)
            ev["description"] = f"Your move was anticipated and {target_ref} gains the position advantage!"
        else:
            ev["description"] = "You dance with the enemy, and no advantage is gained or lost."
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

    # Cloak (maneuvering side = the NPC/IC) lowers its Evasion-test TN; Lock-On (opposing side =
    # the PC) lowers the PC's Sensor-test TN, helping it keep the evading icon in its sensors.
    npc_cloak = 0 if is_ic else int((actor.get("utilities") or {}).get("cloak", 0) or 0)
    pc_lock_on = int((decker.get("utilities") or {}).get("lock_on", 0) or 0)
    result = eng.maneuver_test(
        maneuvering_evasion_dice=man_evasion_dice,
        maneuvering_evasion_rating=man_evasion_rating,
        opposing_sensor_dice=eff.get("sensor", 4),
        opposing_sensor_rating=eff.get("sensor", 4),
        cloak=npc_cloak,
        lock_on=pc_lock_on,
    )
    man_succ = result["maneuvering_roll"]["successes"]
    opp_succ = result["opposing_roll"]["successes"]
    net = result["net_successes"]
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
            # vr2 L2004: the winner may take the position as a to-hit bonus (-TN) OR channel it
            # into a heavier blow (+Power). NPC heuristic: if the PC is already badly wounded,
            # press for the kill with +Power; otherwise take the easier hit (-TN).
            actor["position_bonus"] = _npc_position_bonus(state, net)
            if "power_bonus" in actor["position_bonus"]:
                ev["description"] = (f"{label} sets up a heavy strike -- +{net} Power on its next "
                                     "attack on you.")
            else:
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


def _apply_locate_ic(state: dict, *, test_success: bool, target_ic_id: str = "") -> None:
    """Locate IC (vr2 L1884 + L1998, correction #5): a System Test ONLY (no Sensor Test) that
    RE-DETECTS icons the decker has lost track of. Two cases:
      1. IC that evaded the decker via the Evade Detection maneuver (evade_dir == "hid_from_pc").
      2. A Trace IC that hit the decker and vanished into its Location Cycle (``trace_phase`` ==
         "locate" and not yet ``located``). Re-acquiring it sets ``ic['located'] = True`` so it can
         be attacked / slowed / relocated again (vr2 Trace IC visibility, user ruling 2026-07-10).
    Per the user ruling it does NOT reveal never-seen IC -- a lurking reactive IC betrays itself
    only by acting. A successful System Test clears each evaded IC's markers (via _clear_evade) and
    re-acquires each hidden locating trace. Mutates ``state``."""
    evaded_ic = [ic for ic in state.get("active_ic", [])
                 if isinstance(ic, dict) and ic.get("status") == "active"
                 and ic.get("evaded") and ic.get("evade_dir") == "hid_from_pc"]
    hidden_traces = [ic for ic in state.get("active_ic", [])
                     if isinstance(ic, dict) and ic.get("status") == "active"
                     and _ic_is_trace(ic) and ic.get("trace_phase") == "locate"
                     and not ic.get("located")]
    tid = (target_ic_id or "").strip()
    if tid:
        evaded_ic = [ic for ic in evaded_ic if ic.get("id") == tid]
        hidden_traces = [ic for ic in hidden_traces if ic.get("id") == tid]
    if not evaded_ic and not hidden_traces:
        _append_event(state, {
            "type": "ic_relocate", "outcome": "none",
            "description": "Locate IC: no IC has slipped your sensors -- nothing to re-locate.",
        })
        return
    if not test_success:
        _append_event(state, {
            "type": "ic_relocate", "outcome": "fail",
            "description": "Locate IC failed -- the hidden IC stays off your sensors this pass.",
        })
        return
    for ic in evaded_ic:
        _clear_evade(state, ic, redetected=True)
    for ic in hidden_traces:
        ic["located"] = True
        _append_event(state, {
            "type": "ic_relocate", "outcome": "trace_reacquired",
            "ic_id": ic.get("id"), "ic_type": ic.get("type"), "ic_rating": ic.get("rating"),
            "description": (
                f"{ic.get('type')}-{ic.get('rating')} trace RE-ACQUIRED in its location cycle "
                "-- you can attack, slow, or relocate it again."
            ),
        })



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
async def sheaf_preview(body: SheafGenerateInput, _rl: None = Depends(enforce_call_rate)):
    """Generate a preview sheaf without saving it. Rate-limited per caller (enforce_call_rate):
    it runs the RNG/table sheaf generator on every call and is otherwise open to any runner."""
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


# -- GM after-action report (AAR) ----------------------------------------------

# Machine end_reason -> (human outcome line, was-it-a-clean-getaway). Mirrors the runner-view
# terminated screen so the GM report reads the same as what the player saw.
_AAR_OUTCOME = {
    "graceful_logoff":        ("Logged off cleanly -- connection closed.", True),
    "jack_out":               ("Emergency jack-out (user interrupt) -- dump shock.", False),
    "host_shutdown":          ("Host shut down -- connection lost.", False),
    "host_crashed":           ("Host crashed -- all processes stopped, connection lost.", False),
    "persona_crashed":        ("Persona crashed -- icon damage threshold exceeded.", False),
    "icon_crashed_by_decker": ("Persona crashed -- icon damage threshold exceeded.", False),
    "black_ic_unconscious":   ("Black IC biofeedback -- decker rendered UNCONSCIOUS (DocWagon dispatched).", False),
    "killed_by_killjoy":      ("Killjoy IC biofeedback -- decker rendered UNCONSCIOUS (DocWagon dispatched).", False),
    "black_ic_lethal":        ("Black IC biofeedback -- decker FLATLINED.", False),
    "killed_by_black_hammer": ("Black Hammer biofeedback -- decker FLATLINED.", False),
}


def _build_run_aar(run: MatrixRun) -> dict:
    """Assemble the GM after-action report for an ENDED run from its frozen state.

    Surfaces exactly the consequences the GM must adjudicate after a player-run session the GM did
    not watch live: the paydata haul, whether the decker was traced and physically located, any
    injuries / permanent deck damage, lingering MPCP infections, and the alert level / tally the run
    reached. Pure read of ``run`` -- no mutation, so it is safe to call from any list/read path."""
    state = run.state_json or {}
    decker = run.decker_json or {}
    cm = state.get("condition_monitor") or {}

    outcome, escaped_clean = _AAR_OUTCOME.get(
        state.get("end_reason"),
        (str(state.get("end_reason") or "Session closed.").replace("_", " "), run.status == "escaped"),
    )

    # Trace: a completed Trace IC locates the jackpoint; whether that yields a PHYSICAL location
    # depends on the satellite-uplink immunity (a satlink decker is traced in the Matrix but their
    # meat body cannot be pinpointed / dispatched to).
    traced = int(state.get("traces_completed", 0) or 0) > 0
    immune = bool(state.get("physical_trace_immune"))
    physical_found = traced and not immune

    # Injuries / permanent consequences -> human lines.
    injuries: list[str] = []
    mpcp_damage = int(cm.get("mpcp_damage", 0) or 0)
    if mpcp_damage > 0:
        injuries.append(f"MPCP damage: -{mpcp_damage} (permanent until deck repair)")
    chip = cm.get("persona_chip_damage") or {}
    chip_burn = {k: int(chip.get(k, 0) or 0) for k in ("bod", "evasion", "masking", "sensor")}
    burned = {k: v for k, v in chip_burn.items() if v > 0}
    if burned:
        injuries.append(
            "Persona chips burned: "
            + ", ".join(f"{k.upper()} -{v}" for k, v in burned.items())
        )
    stun = int(cm.get("stun_boxes", 0) or 0)
    phys = int(cm.get("physical_boxes", 0) or 0)
    if stun > 0:
        injuries.append(f"Stun damage: {stun}/10 boxes (biofeedback)")
    if phys > 0:
        injuries.append(f"Physical damage: {phys}/10 boxes (biofeedback)")
    infections = [i for i in (state.get("mpcp_infections") or []) if isinstance(i, dict)]
    if infections:
        injuries.append(
            "MPCP infected: "
            + ", ".join(
                f"{i.get('variant', 'worm')} (R{i.get('rating', '?')})" for i in infections
            )
        )

    secured = state.get("paydata_secured") if isinstance(state.get("paydata_secured"), dict) else None
    paydata = secured or {"files": [], "count": 0, "total_mp": 0, "key_count": 0}

    # Enemy security deckers spawned during the run. The GM AAR names every one (handle if the run
    # ever assigned it) plus its final status, so the GM knows who Static crossed and who is still
    # standing to remember / retaliate. Unnamed spawns fall back to a generic label.
    enemy_deckers = []
    for e in (state.get("enemy_deckers") or []):
        if not isinstance(e, dict):
            continue
        handle = str(e.get("handle", "") or "").strip()
        enemy_deckers.append({
            "handle": handle or None,
            "tier": e.get("tier"),
            "status": str(e.get("status", "") or "active"),
            "located_pc": bool(e.get("located", False)),
        })

    # Trap doors this run surfaced (concealed comm ports to other hosts). Only discovered ones are
    # intel worth reporting; the destination is included since the GM sees un-redacted state.
    trap_doors = []
    for td in (state.get("trap_doors") or []):
        if not isinstance(td, dict) or not td.get("discovered"):
            continue
        trap_doors.append({
            "subsystem": str(td.get("subsystem", "") or ""),
            "destination_label": str(td.get("destination_label", "") or ""),
            "destination_host_id": td.get("destination_host_id"),
            "destination_ltg": str(td.get("destination_ltg", "") or ""),
            "filed": bool(td.get("filed", False)),
            "entered": bool(td.get("entered", False)),
        })

    return {
        "run_id": run.id,
        "host_id": run.host_id,
        "status": run.status,
        "end_reason": state.get("end_reason"),
        "outcome": outcome,
        "escaped_clean": bool(escaped_clean),
        "decker_name": str(decker.get("name", "") or "Unknown decker"),
        "character_id": decker.get("character_id"),
        "paydata": paydata,
        "traced": traced,
        "physical_location_found": physical_found,
        "physical_trace_immune": immune,
        "injuries": injuries,
        "mpcp_damage": mpcp_damage,
        "persona_chip_burn": chip_burn,
        "mpcp_infections": infections,
        "enemy_deckers": enemy_deckers,
        "trap_doors": trap_doors,
        "alert_status": str(state.get("alert_status", "none") or "none"),
        "security_tally": int(state.get("security_tally", 0) or 0),
        "acknowledged": bool(run.aar_acknowledged),
        "created_at": run.created_at,
        "updated_at": run.updated_at,
    }


# -- Run session CRUD -----------------------------------------------------------

@router.get("/", response_model=list[MatrixRunSummary], dependencies=[Depends(get_admin_token)])
async def list_runs(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(MatrixRun).order_by(MatrixRun.created_at.desc()).limit(50))
    return result.scalars().all()


@router.get("/aar/pending", response_model=list[MatrixRunAAR],
            dependencies=[Depends(get_admin_token)])
async def list_pending_aars(db: AsyncSession = Depends(get_db)):
    """GM queue of ended runs whose after-action report has not yet been acknowledged. These are
    the runs blocking their deckers from starting a new session -- the GM reviews each, applies any
    lingering consequences, then acknowledges it to clear the gate. Most recent first."""
    result = await db.execute(
        select(MatrixRun)
        .where(MatrixRun.status != "active", MatrixRun.aar_acknowledged.is_(False))
        .order_by(MatrixRun.updated_at.desc())
        .limit(100)
    )
    return [_build_run_aar(r) for r in result.scalars().all()]


@router.get("/{run_id}/aar", response_model=MatrixRunAAR,
            dependencies=[Depends(get_admin_token)])
async def get_run_aar(run_id: int, db: AsyncSession = Depends(get_db)):
    """Full after-action report for a single run (GM-only)."""
    run = await _get_run_or_404(db, run_id)
    return _build_run_aar(run)


@router.post("/{run_id}/aar/acknowledge", response_model=MatrixRunAAR,
             dependencies=[Depends(get_admin_token)])
async def acknowledge_run_aar(run_id: int, db: AsyncSession = Depends(get_db)):
    """Acknowledge a run's after-action report: clears the run-start gate for that decker and
    removes the ended run so the GM review queue only ever holds outstanding reports. The AAR is
    returned one last time in the response so the caller can display what was just cleared."""
    run = await _get_run_or_404(db, run_id)
    if run.status == "active":
        raise HTTPException(400, "Run is still active -- nothing to acknowledge yet.")
    aar = _build_run_aar(run)
    aar["acknowledged"] = True
    await db.delete(run)
    await db.commit()
    return aar


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

    await _assert_no_unacknowledged_run(db, auth, body.decker.model_dump())

    run = await _create_run(db, auth, host, body.decker.model_dump())
    return _serialize_run(run, auth)


async def _assert_no_unacknowledged_run(db: AsyncSession, auth: dict, decker_dict: dict) -> None:
    """Block a new run while the caller has an ENDED run whose AAR the GM has not acknowledged yet.

    The GM never watches a player's live session, so an ended run's consequences (deck damage,
    trace fallout, infections) may still need adjudication before the decker jacks in again. Admins
    (no owner token) bypass -- they start runs directly. When the new run names a character, the gate
    is scoped to that character's prior runs; otherwise it applies to any of the token's ended runs."""
    token = auth.get("user_token")
    if not token:
        return  # admin / tokenless: no gate
    owner_hash = hash_token(token)
    result = await db.execute(
        select(MatrixRun).where(
            MatrixRun.owner_token_hash == owner_hash,
            MatrixRun.status != "active",
            MatrixRun.aar_acknowledged.is_(False),
        )
    )
    pending = result.scalars().all()
    new_char = (decker_dict or {}).get("character_id")
    if new_char is not None:
        pending = [r for r in pending if (r.decker_json or {}).get("character_id") == new_char]
    if pending:
        raise HTTPException(
            409,
            "A previous run for this decker is awaiting GM review. The GM must acknowledge its "
            "after-action report before a new run can start.",
        )


async def _gather_player_handles(db: AsyncSession, decker_dict: dict) -> list[str]:
    """Snapshot every player-character name (plus this run's decker name) into a lowercased list,
    stored on the run state as ``excluded_handles``. A spawned security decker never takes a handle
    on this list, so an NPC can't share a name with any player character (directive #4). Snapshotted
    once at run start rather than queried per-spawn so the enemy spawner stays a pure state helper.
    A DB hiccup degrades gracefully to just the run's own decker name (never blocks starting a run)."""
    names: set[str] = set()
    own = str((decker_dict or {}).get("name", "")).strip()
    if own:
        names.add(own.lower())
    try:
        result = await db.execute(select(Character.name))
        for (nm,) in result.all():
            cleaned = str(nm or "").strip()
            if cleaned:
                names.add(cleaned.lower())
    except Exception:  # pragma: no cover - defensive: never block a run on a name-lookup failure
        pass
    return sorted(names)


async def _create_run(db: AsyncSession, auth: dict, host: MatrixHost, decker_dict: dict) -> MatrixRun:
    """Persist a fresh run on ``host`` for the given decker. Shared by start_run and the
    trap-door ENTER transit (which lands the decker on a new linked host)."""
    state = _initial_state(decker_dict, host)
    # Real runs opt into interactive per-attack defense: a landing IC cybercombat strike pauses the
    # host response phase (state['pending_defense']) so the decker can allocate Hacking Pool dice to
    # the icon's resist before the hit lands (resolved via POST /{run_id}/defend). Tests build state
    # through _initial_state directly (defaults off), so they keep resolving IC hits inline.
    state["interactive_defense"] = True
    state["excluded_handles"] = await _gather_player_handles(db, decker_dict)
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


# Persona chip-damage attribute -> the deck's as-built persona rating field on the saved deck.
_CHIP_TO_DECK_FIELD = {"bod": "pBod", "evasion": "pEvasion", "masking": "pMasking", "sensor": "pSensor"}


async def _apply_run_damage_to_deck(db: AsyncSession, run: MatrixRun, auth: dict) -> None:
    """Write a finished run's hardware consequences back onto the owning character's saved deck.

    Runs -- not the GM -- are the source of deck damage: every permanent consequence a run inflicts
    (MPCP damage, Ripper persona-chip burn, and persistent MPCP Worm infections) is stamped onto
    the deck's ``damage`` overlay / ``mpcp_infections`` list so the player must institute a Deck
    Workshop repair (GM-approved) before the deck is whole again. Consistent across all damage
    types. No-op (silently) when the run is not linked to a deck, the character/deck can't be
    resolved, the caller doesn't own the character, or the damage was already applied
    (idempotent via ``state["deck_damage_applied"]``)."""
    state = run.state_json or {}
    if state.get("deck_damage_applied"):
        return
    decker = run.decker_json or {}
    char_id = decker.get("character_id")
    deck_name = (decker.get("deck_name") or "").strip()
    if not char_id or not deck_name:
        return
    char = await db.get(Character, char_id)
    if char is None:
        return
    # Only the character's owner (or an admin) may mutate its deck store.
    if not auth.get("is_admin"):
        tok = auth.get("user_token")
        if not tok or char.owner_token != hash_token(tok):
            return

    dbs = copy.deepcopy(char.deck_builder_state or {})
    decks = ((dbs.get("stores") or {}).get("sr2_decks_v1"))
    if not isinstance(decks, list):
        return
    idx = next((i for i, d in enumerate(decks) if isinstance(d, dict) and d.get("name") == deck_name), None)
    if idx is None:
        return
    deck = dict(decks[idx])
    dmg = dict(deck.get("damage") or {})

    cm = state.get("condition_monitor") or {}
    changed = False

    # MPCP damage -> degraded MPCP rating (stack: keep the worst = lowest surviving rating).
    mpcp_hit = int(cm.get("mpcp_damage", 0) or 0)
    if mpcp_hit > 0:
        as_built = int(deck.get("mpcp", 1) or 1)
        degraded = max(1, as_built - mpcp_hit)
        cur = dmg.get("mpcp")
        if cur is None or degraded < int(cur):
            dmg["mpcp"] = degraded
            changed = True

    # Ripper persona chip burn -> degraded persona-chip rating (permanent floor).
    chip = cm.get("persona_chip_damage") or {}
    for attr, field in _CHIP_TO_DECK_FIELD.items():
        hit = int(chip.get(attr, 0) or 0)
        if hit <= 0:
            continue
        as_built = int(deck.get(field, 0) or 0)
        degraded = max(0, as_built - hit)
        cur = dmg.get(field)
        if cur is None or degraded < int(cur):
            dmg[field] = degraded
            changed = True

    # Persistent MPCP Worm infections -> merge onto the deck (dedup by ic_id).
    infections = state.get("mpcp_infections") or []
    if infections:
        existing = deck.get("mpcp_infections")
        existing = list(existing) if isinstance(existing, list) else []
        seen = {inf.get("ic_id") for inf in existing if isinstance(inf, dict)}
        for inf in infections:
            if not isinstance(inf, dict):
                continue
            iid = inf.get("ic_id")
            if iid and iid in seen:
                continue
            existing.append({
                "variant": str(inf.get("variant", "standard")),
                "rating": int(inf.get("rating", 6) or 6),
                "ic_id": str(iid or ""),
            })
            if iid:
                seen.add(iid)
        deck["mpcp_infections"] = existing
        changed = True

    if changed:
        if dmg:
            deck["damage"] = dmg
        decks[idx] = deck
        char.deck_builder_state = dbs
        await db.commit()

    state = copy.deepcopy(run.state_json or {})
    state["deck_damage_applied"] = True
    run.state_json = state
    await db.commit()


@router.post("/{run_id}/apply-deck-damage", response_model=MatrixRunRead)
async def apply_deck_damage(
    run_id: int,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Stamp a finished run's hardware consequences (MPCP damage, Ripper chip burn, Worm
    infections) onto the owning character's saved deck. Idempotent; only fires once the run has
    ended. The client calls this once when it detects the run is over."""
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if not (run.state_json or {}).get("run_ended"):
        raise HTTPException(409, "Run has not ended")
    await _apply_run_damage_to_deck(db, run, auth)
    await db.refresh(run)
    return _serialize_run(run, auth)


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


def _defense_offer_wanted(state: dict, to_hit: dict) -> bool:
    """True when the decker should be offered an interactive Hacking-Pool defense against an IC
    cybercombat strike: the run opted into interactive defense (``interactive_defense``), the attack
    scored at least one net success (so damage is pending), the decker still has Hacking Pool dice
    to spend, and no defense prompt is already outstanding. When False the strike resolves inline
    exactly as before -- so existing runs and tests (which never set ``interactive_defense``) are
    completely unaffected."""
    return bool(
        state.get("interactive_defense")
        and to_hit.get("successes", 0) > 0
        and state.get("hackingPool_remaining", 0) > 0
        and not state.get("pending_defense")
    )


def _assert_no_pending_defense(state: dict) -> None:
    """Reject a player action while an IC cybercombat strike is parked awaiting the decker's
    interactive defense (``state['pending_defense']``). The strike must be resolved via POST
    /{run_id}/defend first -- otherwise acting again would let the decker skip the parked hit or
    advance the pass out from under it. 409 Conflict: the request is well-formed, but the run is in
    a state that must be cleared first. Never trips for runs without interactive defense (they never
    park), so existing runs and the test suite are unaffected."""
    if state.get("pending_defense"):
        raise HTTPException(409, "An IC strike is awaiting your defense -- resolve it first.")


def _park_pending_defense(state: dict, decker: dict, ic: dict, *, to_hit: dict,
                          ic_attack_pool: int, ic_target_status: str, atk_power_delta: int,
                          atk_tn_delta: int, cluster_penalty: int, ic_category: str,
                          sec_code: str, sec_value: int, logon_completed: bool = False) -> None:
    """Pause an IC's standard cybercombat strike so the decker can allocate Hacking Pool dice to the
    icon's damage resistance before it resolves. Stashes everything ``_resolve_ic_cybercombat`` needs
    to finish the SAME strike later -- the already-rolled to-hit is reused verbatim, so no dice are
    re-rolled -- and emits a ``defense_pending`` event carrying the attacker's successes so the
    client can show them before the player chooses. The parked IC already has ``acted_pass`` set, so
    resuming the pass skips it: only the resolution is deferred, not the action."""
    power = (ic["rating"] + ic.get("cascade_rating_bonus", 0)
             + atk_power_delta + _deathworm_tn_bonus(state))
    label = f"{ic['type']}-{ic['rating']}"
    state["pending_defense"] = {
        "ic_id": ic["id"],
        "attacker_label": label,
        "attack_successes": to_hit.get("successes", 0),
        "to_hit_roll": to_hit,
        "power": power,
        "hp_available": state.get("hackingPool_remaining", 0),
        "resume_logon_completed": bool(logon_completed),
        "ctx": {
            "ic_attack_pool": ic_attack_pool,
            "ic_target_status": ic_target_status,
            "atk_power_delta": atk_power_delta,
            "atk_tn_delta": atk_tn_delta,
            "cluster_penalty": cluster_penalty,
            "ic_category": ic_category,
            "sec_code": sec_code,
            "sec_value": sec_value,
        },
    }
    _append_event(state, {
        "type": "defense_pending",
        "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
        "description": (
            f"{label} strikes your icon -- {to_hit.get('successes', 0)} attack success(es), "
            f"Power {power}. Allocate Hacking Pool dice to resist (or defend with none)."
        ),
        "attack_roll": to_hit,
        "hp_available": state.get("hackingPool_remaining", 0),
    })


def _resolve_ic_cybercombat(state: dict, decker: dict, ic: dict, *, ic_attack_pool: int,
                            ic_target_status: str, eff: dict, atk_power_delta: int,
                            atk_tn_delta: int, cluster_penalty: int, ic_category: str,
                            sec_code: str, sec_value: int,
                            precomputed_attack_roll: dict | None = None,
                            defender_bonus_dice: int = 0) -> bool:
    """Resolve one standard (non-black) IC cybercombat strike -- Killer / Blaster / Sparky /
    Construct -- against the decker's persona icon: damage resistance, Armor wear, Simsense overload,
    and persona-crash consequences (Blaster/Sparky MPCP burn + dump shock).

    Split out of ``_advance_npc_pass`` so the interactive-defense flow can resolve the SAME strike
    after the decker allocates Hacking Pool dice: the caller rolls the to-hit first and passes it as
    ``precomputed_attack_roll`` (reused verbatim -- RNG-identical to the old inline roll), and
    ``defender_bonus_dice`` adds the decker's chosen Hacking Pool dice to the icon's Bod resistance.
    Returns True when the strike ended the run (caller must stop the pass); False otherwise.
    """
    armor          = _effective_armor(decker, state)
    cascade_power  = ic["rating"] + ic.get("cascade_rating_bonus", 0)
    # Shield parry: fired ONLY if the attack lands; net successes then cancel attacker damage
    # successes before staging (vr2). A clean miss rolls no Shield and wears nothing.
    ic_skill       = ic["rating"] if ic["type"] == "Construct" else sec_value
    attack = eng.cybercombat_attack(
        attacker_pool=ic_attack_pool,
        security_code=sec_code,
        target_status=ic_target_status,
        target_bod=eff["bod"],
        armor_rating=armor,
        ic_rating=cascade_power + atk_power_delta + _deathworm_tn_bonus(state),   # + Position Power + Deathworm resist TN
        attacker_is_ic=True,
        # + Parry(+)/Position(-) to-hit delta + the IC's own wound penalty, minus the
        # -1-per-completed-Trace proactive-IC to-hit bonus (vr2 Trace L590)
        tn_modifier=cluster_penalty + atk_tn_delta + _ic_wound_mod(ic) - _completed_trace_count(state),
        shield_parry=lambda: _shield_parry(state, decker, attacker_skill=ic_skill, context=ic["type"]),
        precomputed_attack_roll=precomputed_attack_roll,
        defender_bonus_dice=defender_bonus_dice,
    )
    final_dmg = attack["resistance"]["final_damage_level"]
    boxes = attack["resistance"]["boxes"]
    # Cascading IC: a miss raises its attack SV; a hit the decker fully resists raises its rating.
    _apply_cascade_outcome(ic, sec_code,
                           hit=attack["attack_roll"]["successes"] > 0, damage_dealt=boxes > 0)

    _add_cm_damage(state["condition_monitor"], "persona_boxes", boxes)
    _wear_armor(state, state, decker, boxes)
    _sp = state.pop("_shield_dice_pending", None)
    if _sp:
        attack["resistance"]["resist_roll"]["shield_dice"] = _sp["dice"]
        attack["resistance"]["resist_roll"]["shield_successes"] = _sp["successes"]
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

    # Simsense: hot deck only, white/gray IC only. This app has no separate manual-vs-DNI
    # control axis, so a hot deck IS "running hot on pure DNI" -- the same convention that
    # grants the +1D6 hot-DNI initiative die (see _roll_decker_initiative). Per RAW that pure-
    # DNI interface also adds +2 to the simsense overload TN (an ICCM filter cancels it).
    if ic_category in ("white", "gray") and decker.get("deck_mode") == "hot":
        sim = eng.simsense_check(
            damage_level=final_dmg,
            willpower=decker.get("willpower", 4),
            deck_mode=decker.get("deck_mode", "hot"),
            hot_dnil_only=True,
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
            sparky_boxes = rules.ICON_DAMAGE_BOXES[sparky_final]
            _add_cm_damage(state["condition_monitor"], "physical_boxes", sparky_boxes)
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
        _finalize_run_end(state)
        return True

    return False


def _advance_npc_pass(state: dict, decker: dict, run, *, eff: dict, sec_code: str,
                      sec_value: int, det_factor: int, logon_completed: bool = False,
                      allow_defense_pause: bool = False) -> None:
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
        # Stamp every event this IC logs with its own initiative count (vr2: init is rolled once
        # per encounter, so this is stable). Reset to the decker's init when the driver finishes.
        state["_acting_init"] = ic.get("initiative")

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
                trace_tn = _compute_trace_tn(state, decker, ic["rating"], eff, ic)
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
                # Relocate spoof (vr2 L588): a trace spoofed THIS Combat Turn makes no location-
                # cycle progress this turn -- its countdown does not tick. Self-clearing next turn.
                if ic.get("trace_spoofed_turn") == state.get("current_turn", 1):
                    _append_event(state, {
                        "type": "ic_attack",
                        "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                        "description": (
                            f"{ic['type']}-{ic['rating']} location cycle SPOOFED this turn "
                            "-- no trace progress."
                        ),
                        "trace_phase": "spoofed",
                    })
                    continue
                remaining = max(0, ic.get("trace_locate_remaining", 1) - 1)
                ic["trace_locate_remaining"] = remaining
                if remaining <= 0:
                    # Location cycle complete (vr2 Trace 'Effects on Completion', L588-591): the
                    # jackpoint is traced. Apply the two mechanical effects by counting this
                    # completion -- every proactive IC now hits at -1 TN and every subsequent
                    # security-tally increase gains +1. (Recording the jackpoint address is
                    # narrative only; nothing in the app models physical dispatch beyond this.)
                    ic["trace_phase"] = "triggered"
                    ic["status"] = "triggered"
                    state["traces_completed"] = _completed_trace_count(state) + 1
                    if state.get("physical_trace_immune"):
                        _append_event(state, {
                            "type": "ic_attack",
                            "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                            "description": (
                                f"{ic['type']}: Satellite jackpoint located, but the decker's "
                                f"PHYSICAL LOCATION is protected (satellite uplink) -- no physical "
                                f"security can be dispatched. Proactive IC now hit at -1 TN; "
                                f"every further tally increase +1."
                            ),
                            "trace_action": "report",
                            "physical_trace_immune": True,
                            "traces_completed": state["traces_completed"],
                        })
                    else:
                        _append_event(state, {
                            "type": "ic_attack",
                            "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                            "description": (
                                f"{ic['type']}: Jackpoint TRACED -- physical location reported to "
                                f"system operator. Proactive IC now hit at -1 TN; every further "
                                f"tally increase +1."
                            ),
                            "trace_action": "report",
                            "traces_completed": state["traces_completed"],
                        })
                    # Trap Trace (vr2 Trap IC, L688): the hidden IC triggers when the location
                    # cycle completes successfully (a crashed Trap Trace was defused instead).
                    _spawn_trap_hidden(state, ic, sec_code)
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

        # Legitimate status: attackers use the PC's to-hit column (Validate Passcode flips it).
        ic_target_status = _pc_target_status(state)

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
            # Shield parry: fired ONLY if the crippler lands (net successes then ADD to the decker's
            # opposed defence, vr2). A resisted/whiffed crippler rolls no Shield and wears nothing.
            # Same shared resolver the decker uses vs enemy icons (only the label differs by actor).
            result = _resolve_attribute_attack(
                state,
                attacker_pool=sec_value,
                resist_tn=ic["rating"],
                target_attr_rating=target_attr,
                attr=attr_key,
                sec_code=sec_code,
                target_status=ic_target_status,
                target_kind="pc",
                causing_rating=ic["rating"],
                shield_parry=lambda: _shield_parry(state, decker, attacker_skill=sec_value, context=ic["type"]),
                # combat-maneuver Parry(+)/Position(-) to-hit delta + the IC's own wound penalty,
                # minus the -1-per-completed-Trace proactive-IC to-hit bonus (vr2 Trace L590)
                tn_modifier=atk_tn_delta + _ic_wound_mod(ic) - _completed_trace_count(state),
                is_ripper=(ic_subtype == "ripper"),
                mpcp_rating=decker.get("mpcp", 1),
                hardening=decker.get("hardening", 0),
            )
            _sp = state.pop("_shield_dice_pending", None)
            if _sp and result.get("defense_roll"):
                result["defense_roll"]["shield_dice"] = _sp["dice"]
                result["defense_roll"]["shield_successes"] = _sp["successes"]
            reduction = result["reduction"]
            atk_succ = result["attack_roll"]["successes"]
            def_succ = result["defense_roll"]["successes"]
            net_succ = max(0, atk_succ - def_succ)
            if reduction > 0:
                desc = (
                    f"{ic['type']}-{ic['rating']} vs {attr_key.upper()}: "
                    f"{net_succ} successes, {attr_key.upper()} -{reduction}."
                )
            else:
                desc = f"{ic['type']}-{ic['rating']} vs {attr_key.upper()}. Resisted, no damage!"
            if ic_subtype == "ripper" and result.get("chip_damage", 0) > 0:
                chip = result["chip_damage"]
                desc += f" {attr_key.upper()} permanently reduced by {chip}."
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
        # A tortoise deck has no ASIST/simsense link, so Black IC cannot reach the operator at all:
        # it behaves like ordinary attack IC (icon damage only -- no biofeedback, no jack-out
        # Willpower gate, no dump shock, no MPCP burn). So drop the "black" treatment for a tortoise
        # and let it fall through to the standard icon-only cybercombat path below.
        is_black        = ic["type"] == "Black IC" and decker.get("deck_mode") != "tortoise"
        # Hot decks take lethal (Physical) biofeedback; a cool deck takes non-lethal (Stun).
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
            # Black IC (vr2): ONE Attack Test drives BOTH resistance tests off the same successes --
            # the persona icon (Bod, Armor protects) AND the operator's flesh (Body when lethal /
            # Willpower when non-lethal, Armor does NOT protect). Shield parry blunts every
            # consequence of the one parried strike; Hardening reduces the resist Power. Hot deck ->
            # lethal Physical; cool deck -> non-lethal Stun. Either mode can still crash the icon.
            armor       = _effective_armor(decker, state)
            black = eng.black_attack(
                attacker_pool=ic_attack_pool,
                security_code=sec_code,
                target_status=ic_target_status,
                base_damage_level=rules.IC_DAMAGE_LEVEL[sec_code],
                power=ic["rating"] + atk_power_delta + _deathworm_tn_bonus(state),  # + Position Power + Deathworm resist TN
                hardening=hardening,
                icon_bod=eff["bod"],
                icon_armor=armor,
                tn_modifier=cluster_penalty + atk_tn_delta + _ic_wound_mod(ic) - _completed_trace_count(state),
                shield_parry=lambda: _shield_parry(state, decker, attacker_skill=sec_value, context="Black IC"),
                meat_pool=decker.get("willpower", 4) if is_non_lethal else decker.get("body", 4),
                meat_is_stun=is_non_lethal,
            )
            _sp = state.pop("_shield_dice_pending", None)
            if _sp:
                black["icon"]["resist_roll"]["shield_dice"] = _sp["dice"]
                black["icon"]["resist_roll"]["shield_successes"] = _sp["successes"]   # parry folds into the persona (Bod) resist
            persona_boxes = black["icon"]["boxes"]
            meat_boxes    = black["meat"]["boxes"]
            # vr2 L612: after the FIRST Black IC hit (even if no damage), jacking out stops being a
            # Free Action -- it needs a Complex Action + Willpower(Black IC Rating) Test (see
            # jack_out). A "hit" is any successful Attack Test, regardless of boxes that land.
            if black["attack_roll"]["successes"] > 0:
                state["black_ic_engaged"] = True
            _add_cm_damage(state["condition_monitor"], "persona_boxes", persona_boxes)
            _wear_armor(state, state, decker, persona_boxes)

            if is_non_lethal:
                # Cool deck: Non-Lethal Black IC -- Willpower -> Stun (meat) + Bod -> icon.
                _add_stun(state["condition_monitor"], meat_boxes)
                _append_event(state, {
                    "type": "ic_attack",
                    "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                    "description": (
                        f"Black IC (non-lethal) {ic['rating']}: "
                        f"{black['attack_roll']['successes']} atk successes. "
                        f"Bod resist: {black['icon']['final_damage_level']} ({persona_boxes} persona). "
                        f"Willpower resist: {black['meat']['final_damage_level']} ({meat_boxes} stun). "
                        f"Persona: {state['condition_monitor']['persona_boxes']}/10 "
                        f"Stun: {state['condition_monitor']['stun_boxes']}/10"
                    ),
                    "attack_roll": black["attack_roll"],
                    "bod_roll": black["icon"]["resist_roll"],
                    "will_roll": black["meat"]["resist_roll"],
                    "persona_damage": black["icon"]["final_damage_level"],
                    "stun_damage": black["meat"]["final_damage_level"],
                    "stun_boxes": meat_boxes,
                })
            else:
                # Hot deck: Lethal Black IC -- Body -> Physical (meat) + Bod -> icon.
                _add_cm_damage(state["condition_monitor"], "physical_boxes", meat_boxes)
                _append_event(state, {
                    "type": "ic_attack",
                    "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                    "description": (
                        f"Black IC (lethal) {ic['rating']}: "
                        f"{black['attack_roll']['successes']} atk successes. "
                        f"Body resist: {black['meat']['final_damage_level']} ({meat_boxes} phys). "
                        f"Bod resist: {black['icon']['final_damage_level']} ({persona_boxes} persona). "
                        f"Physical: {state['condition_monitor']['physical_boxes']}/10 "
                        f"Persona: {state['condition_monitor']['persona_boxes']}/10"
                    ),
                    "attack_roll": black["attack_roll"],
                    "body_roll": black["meat"]["resist_roll"],
                    "bod_roll": black["icon"]["resist_roll"],
                    "physical_damage": black["meat"]["final_damage_level"],
                    "persona_damage": black["icon"]["final_damage_level"],
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
                _finalize_run_end(state)
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
        # Roll the to-hit up front so an interactive defender sees the attacker's successes before
        # choosing Hacking Pool dice. The TN mirrors eng.cybercombat_attack exactly, and the roll is
        # reused verbatim (precomputed_attack_roll), so with no pause this is RNG-identical to the
        # old inline resolution.
        _to_hit_tn = max(2, rules.COMBAT_TN[sec_code][ic_target_status]
                         + cluster_penalty + atk_tn_delta + _ic_wound_mod(ic)
                         - _completed_trace_count(state))
        _to_hit = eng.roll_dice(ic_attack_pool, _to_hit_tn)
        if allow_defense_pause and _defense_offer_wanted(state, _to_hit):
            # Pause the whole NPC pass: stash the strike and return. The decker allocates Hacking
            # Pool via POST /{run_id}/defend, which resolves it and resumes the pass. The IC's
            # acted_pass is already set, so it will not act again when the pass resumes.
            _park_pending_defense(
                state, decker, ic, to_hit=_to_hit,
                ic_attack_pool=ic_attack_pool, ic_target_status=ic_target_status,
                atk_power_delta=atk_power_delta, atk_tn_delta=atk_tn_delta,
                cluster_penalty=cluster_penalty, ic_category=ic_category,
                sec_code=sec_code, sec_value=sec_value, logon_completed=logon_completed,
            )
            return
        if _resolve_ic_cybercombat(
            state, decker, ic,
            ic_attack_pool=ic_attack_pool, ic_target_status=ic_target_status, eff=eff,
            atk_power_delta=atk_power_delta, atk_tn_delta=atk_tn_delta,
            cluster_penalty=cluster_penalty, ic_category=ic_category,
            sec_code=sec_code, sec_value=sec_value, precomputed_attack_roll=_to_hit,
        ):
            break

    # Handle logon completion (player-action result; parameterized so new_turn's flush skips it).
    if logon_completed:
        state["logon_complete"] = True
        _append_event(state, {
            "type": "logon",
            "description": f"Logged on to host successfully. Detection Factor: {det_factor}.",
        })
        # Logging on is the ENTRY step, not one of Turn 1's actions: refresh the pass budget so the
        # decker begins Round 1 Turn 1 with a full 2 AP + 1 Free (the logon test still rolled its
        # dice and cost its Hacking Pool; it just no longer eats the first turn's action points).
        _reset_pass_budget(state)

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
            state["_acting_init"] = enemy.get("initiative")
            _enemy_decker_take_pass(state, decker, run, enemy)
    # Restore the decker's initiative as the acting context: any events logged after the driver
    # (e.g. a structural new_pass/new_turn line, or a follow-up player action) belong to the decker.
    state["_acting_init"] = state.get("decker_initiative")


# NOTE: perform_action is ~600 LOC and combines action resolution, probe IC, and
# the proactive IC turn loop. A split is planned but deferred until gameplay rules
# stabilize. See docs/refactor-notes.md (R1) for the planned structure, risks, and
# why this hasn't been done yet -- read that before reorganizing.
@router.post("/{run_id}/action", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
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
    _assert_no_pending_defense(state)   # a parked IC strike must be resolved (POST /defend) first
    # Events logged while THIS player action resolves belong to the decker's initiative count.
    state["_acting_init"] = state.get("decker_initiative")

    # Snapshot the IDs of every IC ALREADY active before this action resolves. Two RAW timing rules
    # both key off "was this IC present when the decker made the System Test?":
    #   1. Probe IC (vr2_rules.md L485) test every System Test the decker makes -- but a Probe that
    #      first activates as a CONSEQUENCE of this action (its own tally bump crossing a sheaf step)
    #      did not witness the test, so it must NOT test the action that spawned it (starts next test).
    #   2. Initiative (vr2): an IC that spawns mid-action has not yet reached its initiative segment,
    #      so it must NOT act in the pass it appeared -- it first acts on its next pass/turn.
    # Any active IC below whose ID is missing from this set is therefore newly-spawned and held back.
    _preexisting_ic_ids = {
        ic.get("id") for ic in state.get("active_ic", []) if ic.get("id")
    }
    # Same initiative rule for every OTHER app-controlled hostile: an enemy decker (or any future
    # construct list) dispatched as a consequence of THIS action has not reached its initiative
    # segment either, so it must not act in the pass it spawned. Snapshot the pre-action ids and
    # stamp any newcomer as already-acted this pass (see the stamping loop after the IC turn loop).
    _preexisting_enemy_ids = {
        e.get("id") for e in state.get("enemy_deckers", []) if e.get("id")
    }

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
            # Deep-linked via trap doors? Drop back to the suspended parent host instead of
            # ending the whole run (B34). An empty stack is a real run end.
            popped = _pop_host_stack(state)
            if popped is not None:
                state, parent_host_id = popped
                if parent_host_id is not None:
                    run.host_id = parent_host_id
            else:
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

    # Redirect Datatrail is once-per-host (vr2: you can redirect your datatrail once per grid; a
    # second host reached via a trap door is a fresh run with its own redirect). Once the +1 Trace
    # Factor benefit is banked, refuse another attempt BEFORE spending the action -- the UI also
    # disables the button, this is the server-side guard.
    if body.action_type == "redirect_datatrail" and state.get("redirects_placed", 0) >= 1:
        raise HTTPException(
            400, "Datatrail already redirected on this host -- the Trace Factor benefit is banked. "
                 "Follow a trap door to a new system to redirect again.")

    # Action economy: spend this action's cost from the current initiative pass (auto-advances
    # passes; blocks when all passes are spent -> New Turn). vr2: 2 Simple OR 1 Complex + 1 Free.
    _spend_pass_action(state, body.action_type)

    # DINAB per-pass lock (vr2): a program DINAB ran autonomously this pass may not also be used by
    # hand this pass. Reject a manual use of a DINAB-locked program, and record this manual use so a
    # later DINAB on the same program is blocked. No-op for legacy runs / program-less actions.
    _prog_key = _action_program_key(body.action_type)
    _assert_not_dinab_locked(state, _prog_key)
    _record_manual_program(state, _prog_key)

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

    # Invalidate Passcode: erasing the ENTIRE host passcode list at once (the "__all__" target) is a
    # +4 TN Control test (vr2 L1879); erasing a single passcode runs at the base TN.
    if body.action_type == "invalidate_passcode" and body.target_ic_id == _INVALIDATE_ALL:
        tn_modifier += 4

    # Swap Memory (Simple Action, no test): LOAD a stored program into active memory (or reload a
    # crashed/degraded active program from its pristine storage copy). RAW split (vr2): Swap Memory
    # only brings a program IN -- freeing active memory (pushing an active program to storage) is
    # the separate Unload Program Free action below, so no swap_out is passed here. Active programs
    # always keep a storage copy, so a swap only shifts *active* memory usage (deck storage_free_mp
    # is unaffected). See _apply_swap_memory for the resolution modes.
    if body.action_type == "swap_memory":
        new_decker = copy.deepcopy(decker)
        changed, desc = _apply_swap_memory(
            state, new_decker,
            target_program=body.target_program,
            swap_out_program="",
        )
        _append_event(state, {"type": "swap_memory", "description": desc})
        if changed:
            run.decker_json = new_decker
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Unload Program (Free Action, no test): push an ACTIVE program out to storage to free active
    # memory (the "swap out" half that Swap Memory no longer does). Reuses _apply_swap_memory Mode 2
    # (swap_out only, no incoming program). vr2 memory model: the program keeps its storage copy, so
    # this only frees active memory -- reload it later via Swap Memory.
    if body.action_type == "unload_program":
        new_decker = copy.deepcopy(decker)
        changed, desc = _apply_swap_memory(
            state, new_decker,
            target_program="",
            swap_out_program=body.target_program,
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

    # Decompress (Complex Action, no test -- pure bookkeeping like Swap Memory): expand EITHER a
    # Squeezed program swapped into active memory (target_program -- held compressed/unusable until
    # now) OR a previously-downloaded COMPRESSED paydata file (target_file -- stored at half size via
    # the Compressor utility) back to full size so it can be used/read. Program decompress mutates
    # decker.utilities (reassign decker_json when it changed); file decompress is state-only and may
    # 400 if the expanded file will not fit tracked storage (the action is then not spent). Resolved
    # here and returned so it never falls through to the generic system_test below.
    if body.action_type == "decompress_file":
        if body.target_program:
            new_decker = copy.deepcopy(decker)
            if _apply_decompress_program(state, new_decker, target_program=body.target_program):
                run.decker_json = new_decker
        else:
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
        all_infections = state.get("hog_infections") or []
        # The PC purges only viruses on its OWN deck (target 'pc'); infections it cast on an
        # enemy live in the same list but are drained/cleared on the enemy side, not purged here.
        infections = [i for i in all_infections if i.get("target_id", "pc") == "pc"]
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
                state["hog_infections"] = [i for i in all_infections if i is not inf]
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
                "description": "Scramble decrypted -- protected data accessible.",
            })
        else:
            paydata = state.get("paydata") or []
            protected = next((p for p in paydata
                              if p.get("name")
                              and _target_file_name(scr.get("target_key", "")).strip().lower()
                              == str(p["name"]).strip().lower()), None)
            is_key = bool(protected and protected.get("is_key"))
            cons = eng.scramble_failure_consequence(
                variant=scr.get("variant", "standard"), is_key=is_key,
                scramble_rating=scr.get("rating", 6),
                decker_computer_skill=decker.get("computer_skill", 6))
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

    # Update tally (accelerated by any completed Trace)
    applied = _bump_security_tally(state, test["tally_increase"])

    # Human label for the event log. Analyze Subsystem names its targeted subsystem (e.g.
    # "Analyze Subsystem - Files") so the player can easily re-reference which one they probed.
    action_label = body.action_type.replace("_", " ").title()
    if body.action_type == "analyze_subsystem" and body.subsystem:
        action_label += f" - {body.subsystem.replace('_', ' ').title()}"

    log_entry: dict[str, Any] = {
        "type": "action",
        "action": body.action_type,
        "subsystem": body.subsystem,
        "description": (
            f"{action_label} -- "
            f"{'SUCCESS' if test['success'] else 'FAILED'} "
            f"({test['decker_roll']['successes']} vs {test['host_roll']['successes']} successes). "
            f"Tally +{applied} -> {state['security_tally']}."
        ),
        "success": test["success"],
        "decker_roll": test["decker_roll"],
        "host_roll": test["host_roll"],
        "tally_increase": applied,
        "tally_total": state["security_tally"],
        "action_cost": _ACTION_COST.get(body.action_type, "Complex"),  # Free / Simple / Complex
        "note": body.note,
    }
    _append_event(state, log_entry)
    state["actions_this_turn"] = state.get("actions_this_turn", 0) + 1

    # Worm trigger (vr2 L548): this was a genuine System Test against a host subsystem, so any Worm
    # booby-trapping that subsystem now rolls its Infection Test against the deck's MPCP. Self-
    # targeted / non-subsystem actions (medic, restore, swap, maneuvers) returned earlier and never
    # reach here, so they correctly don't trip a worm. Disinfect resolves its own worm test.
    _trigger_subsystem_worms(state, decker, body.subsystem)
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
                    + " -- it links to another system. Destination unknown until you enter it."
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
            # GROUNDED reveal (first successful Access analysis only): learn whether this host has
            # regular-grid LTG access. If it does, surface the real grid address AND flip the host
            # visible on the grid (a persisted DB edit), mirroring the reveal onto its org LTG
            # listing -- so a host discovered via a trap door becomes reachable normally. A host
            # with no LTG stays trap-door-only.
            state["host_ltg_revealed"] = True
            host = await _get_host_or_404(db, run.host_id)
            addr = str(getattr(host, "ltg_address", "") or "").strip()
            if addr:
                if not host.is_visible_to_players:
                    host.is_visible_to_players = True
                    await sync_host_reveal_to_org(db, host)
                state["host_has_ltg"] = True
                state["host_ltg_address"] = addr
                _append_event(state, {
                    "type": "host_ltg_revealed",
                    "has_ltg": True,
                    "ltg_address": addr,
                    "description": (
                        f"Access subsystem analyzed -- this host HAS dedicated LTG access at {addr}."
                    ),
                })
            else:
                state["host_has_ltg"] = False
                _append_event(state, {
                    "type": "host_ltg_revealed",
                    "has_ltg": False,
                    "description": (
                        "Access subsystem analyzed -- this host has NO LTG access (reachable only "
                        "via a direct line or trap door)."
                    ),
                })

    # Analyze Subsystem on ACCESS that FAILS: the host rebuffed the probe. Retryable -- emit a
    # themed "blocked" event so the decker knows the discovery attempt was fought off (rather than a
    # silent generic failure), without leaking whether an LTG actually exists.
    if (body.action_type == "analyze_subsystem" and not test["success"]
            and body.subsystem == "access" and not state.get("host_ltg_revealed")):
        _append_event(state, {
            "type": "access_analysis_blocked",
            "description": ("Access subsystem analysis failed -- the host blocked the discovery "
                            "attempt. You can try again."),
        })

    # Analyze Host: reveal the host's subsystem ratings (5 ACIFS + the Security Rating = 6 items).
    # 6+ net successes (or enough to cover every hidden item) reveals ALL remaining; otherwise the
    # credits are banked and the decker chooses which to reveal via POST /reveal-host-ratings. When
    # the Security Rating is newly revealed, mirror it onto the host's org LTG listing.
    if body.action_type == "analyze_host" and test["success"]:
        sec_before = bool(state.get("host_security_revealed"))
        _apply_analyze_host(state, test["decker_net_successes"])
        if state.get("host_security_revealed") and not sec_before:
            host = await _get_host_or_404(db, run.host_id)
            await sync_host_security_to_org(db, host, mark_revealed=True)

    # Analyze Security: the decker learns its CURRENT security tally + alert status AND the host's
    # Security Rating (code + value) -- vr2 L1869. Snapshot them into the player-visible
    # security_known and reveal the Security Rating in-state (kept DB-free; the org LTG listing is
    # mirrored when Analyze Host reveals the rating).
    if body.action_type == "analyze_security" and test["success"]:
        state["host_security_revealed"] = True
        snapshot = {
            "tally": state["security_tally"],
            "alert": state.get("alert_status", "none"),
            "turn": state.get("current_turn", 1),
            "security_code": state.get("host_security_code"),
            "security_value": state.get("host_security_value"),
        }
        state["security_known"] = snapshot
        _append_event(state, {
            "type": "security_analyzed",
            "known_tally": snapshot["tally"],
            "known_alert": snapshot["alert"],
            "description": (
                f"Analyze Security -- Security Rating {snapshot['security_code']}-"
                f"{snapshot['security_value']}, security tally {snapshot['tally']}, "
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
                "the countdown."
            ),
        })

    # Validate Passcode (vr2 L1899): planting a fake passcode succeeds when the decker wins the
    # opposed System Test -- it grants Legitimate status, so IC attack the persona on the Legitimate
    # to-hit TN column (COMBAT_TN) until logoff or an active alert deletes the passcode. It does NOT
    # buff the decker's other System Tests, and a failed plant may be retried (the failed attempt
    # still raised the security tally by the host's opposed successes, via the generic bump above).
    if body.action_type == "validate_passcode" and test["success"]:
        state["has_legitimate_status"] = True
        _append_event(state, {
            "type": "validate_passcode",
            "success": True,
            "description": "Validate Passcode successful -- Legitimate status granted.",
        })
    elif body.action_type == "validate_passcode" and not test["success"]:
        _append_event(state, {
            "type": "validate_passcode",
            "success": False,
            "description": "Validate Passcode failed -- the host rejected the plant.",
        })

    # Invalidate Passcode (vr2 L1879): a successful Control/Validate test ERASES a host passcode from
    # the security tables -- the affected security icon(s) flip from Legitimate to Intruding, so the
    # PC then attacks them on the Intruding COMBAT_TN column (their to-hit TNs are revised). One
    # success flips a single named IC / enemy decker; the +4-TN whole-list variant (the "__all__"
    # target) flips EVERY active IC and enemy decker at once. The flip is PERMANENT: unlike the PC's
    # own Validate Passcode (wiped on active alert / logoff), an enemy never regains Legitimate
    # status. A failed erase may be retried (the attempt still raised the tally via the generic bump).
    if body.action_type == "invalidate_passcode" and test["success"]:
        whole_list = body.target_ic_id == _INVALIDATE_ALL
        flipped = _invalidate_passcodes(state, None if whole_list else body.target_ic_id)
        if not flipped:
            desc = ("Invalidate Passcode succeeded, but no Legitimate security icon was affected "
                    "(target already Intruding, crashed, or gone).")
        elif whole_list:
            desc = (f"Invalidate Passcode successful -- the entire passcode list is erased. "
                    f"{len(flipped)} security icon(s) flip to Intruding: {', '.join(flipped)}. "
                    "They stay Intruding for the rest of the run.")
        else:
            desc = (f"Invalidate Passcode successful -- {flipped[0]}'s passcode is erased; it flips "
                    "to Intruding (revised to-hit TN) for the rest of the run.")
        _append_event(state, {
            "type": "invalidate_passcode",
            "success": True,
            "whole_list": whole_list,
            "flipped": flipped,
            "description": desc,
        })
    elif body.action_type == "invalidate_passcode" and not test["success"]:
        _append_event(state, {
            "type": "invalidate_passcode",
            "success": False,
            "description": "Invalidate Passcode failed -- the host preserved its passcode tables.",
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

    # Relocate (vr2_rules.md L588 + Relocate utility L... "Cannot defeat trace IC during the hunt
    # cycle"): a Control Test against ONE trace IC that is in its LOCATION cycle. Relocate targets a
    # single trace at a time -- with multiple traces hunting, the decker must Relocate each one
    # separately. On a won test the decker picks ONE of two outcomes at this point:
    #   - suppress_trace=True: SUPPRESS that trace in place -- paused (no further tests) for 1
    #     Detection Factor, resuming EXACTLY where it left off when released (phase / location-cycle
    #     remaining untouched). Re-suppressible (not the one-way crash mode).
    #   - otherwise: SPOOF it for THIS Combat Turn only -- the trace makes no location-cycle progress
    #     this turn (its countdown does not tick) but is NOT reset to hunt. If the decker does not
    #     spoof or suppress it again, it resumes its location cycle next turn normally.
    if body.action_type == "relocate" and test["success"]:
        # Eligible = active trace IC in its location cycle. Relocate cannot touch a trace during its
        # hunt cycle (utility restriction) or one that has already triggered.
        eligible = [ic for ic in state.get("active_ic", [])
                    if ic["status"] == "active" and _ic_is_trace(ic)
                    and ic.get("trace_phase") == "locate"]
        # Single-target: honor an explicit target_ic_id, else the first eligible trace.
        target = None
        if body.target_ic_id:
            target = next((ic for ic in eligible if ic["id"] == body.target_ic_id), None)
        elif eligible:
            target = eligible[0]
        if target is None:
            _append_event(state, {
                "type": "relocate",
                "description": "Relocate: no trace IC currently in its location cycle to spoof.",
            })
        elif body.suppress_trace:
            if target.get("suppressed"):
                _append_event(state, {
                    "type": "relocate",
                    "description": (
                        f"Relocate: {target['type']}-{target['rating']} is already suppressed."),
                })
            elif _base_detection_factor(state, decker) - _suppressed_count(state) <= 1:
                # Suppression costs 1 DF and DF cannot go below its floor of 1. The Relocate test
                # already SUCCEEDED, so rather than waste it we do BOTH: (1) spoof the trace for this
                # turn as the safe default (the won test is never wasted), and (2) HOLD the suppress
                # offer open by flagging the trace ``relocate_suppress_pending``. That flag surfaces
                # the trace in the SUPPRESSIONS panel with a Suppress button, so the decker can go
                # release another suppression to free 1 DF and THEN convert this won Relocate into a
                # full trace-pause -- exactly like the held crash/bomb suppression queries. The offer
                # lapses at end of turn (``_flush_pending_suppressions``); the spoof already covered
                # this turn either way.
                target["trace_spoofed_turn"] = state.get("current_turn", 1)
                target["relocate_suppress_pending"] = True
                _append_event(state, {
                    "type": "relocate", "ic_id": target["id"],
                    "description": (
                        f"Relocate succeeded, but Detection Factor is at its minimum -- cannot "
                        f"suppress {target['type']}-{target['rating']} yet. It was spoofed for this "
                        "turn AND the suppress offer is HELD: release another suppression from the "
                        "SUPPRESSIONS panel to free 1 DF, then Suppress this trace there (offer "
                        "lapses at end of turn)."
                    ),
                })
            else:
                target["suppressed"] = True
                target["suppress_mode"] = "trace"   # paused-in-place; release resumes, re-suppressible
                df = _effective_detection_factor(state, decker)
                state["detection_factor"] = df
                _append_event(state, {
                    "type": "ic_suppressed", "ic_id": target["id"],
                    "description": (
                        f"Relocate succeeded -- {target['type']}-{target['rating']} suppressed "
                        "(trace paused in place; -1 Detection Factor; resumes if released)."
                    ),
                })
        else:
            # Spoof for this Combat Turn only: mark the turn so the trace handler skips its
            # location-cycle tick this turn. Self-clearing (compared to current_turn), so next turn
            # it resumes unless spoofed/suppressed again.
            target["trace_spoofed_turn"] = state.get("current_turn", 1)
            _append_event(state, {
                "type": "relocate",
                "ic_id": target["id"],
                "description": (
                    f"Relocate succeeded -- {target['type']}-{target['rating']} spoofed for this "
                    "turn (no trace progress this turn; resumes next turn unless spoofed again)."
                ),
            })

    # Redirect Datatrail: once-per-host, banks a single +1 Trace Factor benefit (guarded above).
    if body.action_type == "redirect_datatrail" and test["success"]:
        state["redirects_placed"] = 1
        _append_event(state, {
            "type": "redirect_placed",
            "description": (
                "Redirect placed. Trace Factor +1 going forward (trace IC locates your "
                "jackpoint less easily). You cannot redirect again on this host."
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
            all_found = not [p for p in (state.get("paydata") or [])
                             if not p.get("located") and not p.get("destroyed")]
            _append_event(state, {
                "type": "paydata_located",
                "description": "Paydata located: " + ", ".join(
                    f"{p.get('name', '?')} ({max(0, int(p.get('density', 0) or 0))} Mp)" for p in newly
                ) + "."
                + (" All paydata on this host is now located." if all_found else ""),
                "all_located": all_found,
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
        _apply_locate_ic(state, test_success=test["success"],
                         target_ic_id=(body.target_ic_id or ""))

    if body.action_type == "locate_decker":
        _apply_locate_decker(state, decker, test_success=test["success"],
                             scanner=max(0, int(body.utility_rating or 0)))

    # Edit File (vr2 Edit File / Files Test) has two in-app sub-modes on a located paydata file:
    # ERASE (destroy it -- it drops out of the located/decrypt/download lists and the UI greys it)
    # and MODIFY (tamper with / corrupt the host's copy in place -- the file stays, but the owner's
    # data is now falsified). Both are sabotage that deny CLEAN data to the owner; neither changes
    # the Mp the decker can bank. The RAW create/copy sub-modes are intentionally omitted: this app
    # has no paydata-value or mission consumer for a fabricated or duplicated file (paydata value is
    # the Mp actually downloaded), so they would be flavor-only. A bombed file still detonates on
    # this access (see _trigger_access_data_bomb).
    if body.action_type == "edit_file" and test["success"] and body.target_file:
        tgt_name = body.target_file.strip().lower()
        pd = next((p for p in (state.get("paydata") or [])
                   if str(p.get("name", "")).strip().lower() == tgt_name and not p.get("destroyed")),
                  None)
        if pd is not None:
            if (body.edit_mode or "erase").strip().lower() == "modify":
                pd["tampered"] = True
                _append_event(state, {
                    "type": "file_modified",
                    "file_name": pd.get("name"),
                    "description": (
                        f"File \"{pd.get('name')}\" altered on the host -- the owner's copy is now "
                        "corrupted/falsified."
                    ),
                })
            else:
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

    # Run a Probe Test for every Probe IC that was ALREADY active when this System Test began
    # (vr2_rules.md L485). A Probe that only just activated as a consequence of THIS action -- its
    # own tally bump crossing a sheaf step -- is NOT in _preexisting_ic_ids, so it is skipped: it
    # did not witness this test and starts probing from the next one.
    for ic in state.get("active_ic", []):
        if ic["status"] != "active" or ic.get("suppressed"):
            continue
        if ic["type"] == "Probe" and ic.get("id") in _preexisting_ic_ids:
            probe = eng.probe_test(ic["rating"], det_factor)
            # Probe IC is invisible (reactive): make a secret Sensor Test, then report
            # the tally change at a detail level matching what the decker has detected.
            lvl = _secret_sensor_test(state, decker, ic)
            if probe["tally_increase"] > 0:
                inc = _bump_security_tally(state, probe["tally_increase"])
                tally = state["security_tally"]
                # The tally clause is stripped for non-admins by _redact_event_tally, so the
                # narrative sentence must stand on its own -- the decker knows the Probe is
                # working, but never its numeric severity. (Successes == tally delta, so the
                # raw roll is GM-only too and is NOT shown even at full detail.)
                if lvl >= 3:
                    desc = (f"Probe-{ic['rating']} IC is examining your data trail and "
                            f"reporting to host security. Tally +{inc} -> {tally}")
                elif lvl == 2:
                    desc = ("Probe IC is examining your data trail and notifying security... "
                            f"Tally +{inc} -> {tally}")
                elif lvl == 1:
                    desc = ("A hidden IC is quietly probing your actions and alerting the host. "
                            f"Tally +{inc} -> {tally}")
                else:
                    desc = (f"Something is examining your data trail. Tally +{inc} -> {tally}")
                ev = {"type": "probe_ic", "description": desc, "tally_increase": inc}
                if lvl >= 1:
                    ev["ic_id"] = ic["id"]  # only reference the IC once its presence is known
                _append_event(state, ev)
            elif lvl >= 1 or ic.get("analyzed"):
                # No successes -> no tally. Stay silent while the Probe is still unknown, but once
                # the decker has detected/analyzed it, report the clean pass so the log isn't a
                # mysterious gap (vr2 Probe: a whiffed Probe finds nothing this cycle).
                _append_event(state, {
                    "type": "probe_ic", "ic_id": ic["id"],
                    "description": (f"The Probe-{ic['rating']} finds no evidence of your actions "
                                    "this turn."),
                })
            _check_and_activate_sheaf(state, sec_code)

    # vr2 initiative: any IC that first appeared DURING this action (a sheaf trigger, a trap-door
    # reveal, etc. -- its ID is absent from _preexisting_ic_ids) has not yet reached its own
    # initiative segment, so it must not act in the pass it spawned. Stamp it as already-acted THIS
    # pass so the NPC driver below holds it back; new_turn clears acted_pass, so it takes its first
    # real action on its next pass/turn. Mirrors the Probe rule that a just-spawned Probe does not
    # test the action that created it.
    _cur_pass = state.get("current_pass", 1)
    for ic in state.get("active_ic", []):
        if ic.get("id") not in _preexisting_ic_ids and "acted_pass" not in ic:
            ic["acted_pass"] = _cur_pass
    # Same gate for enemy deckers / constructs spawned by this action (see _preexisting_enemy_ids).
    for enemy in state.get("enemy_deckers", []):
        if enemy.get("id") not in _preexisting_enemy_ids and "acted_pass" not in enemy:
            enemy["acted_pass"] = _cur_pass

    # Drive every app-controlled hostile for this initiative pass: proactive/trace IC attacks
    # then enemy deckers. Probe IC (which test per System Test, above) are NOT driven here.
    # The just-resolved Logon is carried in so its event still fires between the IC and enemy loops.
    _advance_npc_pass(
        state, decker, run,
        eff=eff, sec_code=sec_code, sec_value=sec_value, det_factor=det_factor,
        logon_completed=(body.action_type == "logon_to_host" and test["success"]),
        allow_defense_pause=True,
    )

    if state.get("run_ended"):
        run.status = state.get("end_reason", "crashed")
    # A run that ends mid-transfer (e.g. a Free action drew a fatal enemy-decker attack) corrupts
    # the in-progress download -- a partial copy is worthless (vr2 Download Data).
    if state.get("run_ended") and state.get("active_download"):
        _corrupt_active_download(state)

    # Strict SR2 RAW: the Hacking Pool is NOT topped back up between actions. It depletes as the
    # decker spends it -- whether or not IC are present -- and only refreshes at the start of each
    # initiative pass and each Combat Turn (handled by _reset_pass_budget on pass-advance / New
    # Turn). So dice spent on one action leave fewer for the next until the pass/turn rolls over.
    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


@router.post("/{run_id}/defend", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
async def defend(
    run_id: int,
    body: RunDefendInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Resolve a paused IC cybercombat strike after the decker allocates Hacking Pool dice.

    The interactive-defense flow (``perform_action`` -> ``_advance_npc_pass`` with
    ``allow_defense_pause``) PARKS a standard IC strike in ``state['pending_defense']`` once the
    to-hit lands, so the decker can add Hacking Pool dice to the icon's Bod resistance before the
    hit resolves. This endpoint spends those dice, resolves the SAME strike (reusing the parked
    to-hit verbatim -- no re-roll), then RESUMES the rest of the NPC pass, which may immediately
    park again on the next IC. When nothing is left pending, the pass is complete and the client
    stops prompting. ``hacking_pool_dice`` of 0 resists with Bod alone (declines the offer).
    """
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, f"Run is not active (status: {run.status})")

    state = copy.deepcopy(run.state_json)  # deepcopy so nested JSON mutations un-alias (UPDATE fires)
    pending = state.get("pending_defense")
    if not pending:
        raise HTTPException(400, "No defense is pending on this run")

    decker = run.decker_json
    # Events logged while this defense resolves belong to the decker's initiative count.
    state["_acting_init"] = state.get("decker_initiative")
    sec_code = state["host_security_code"]
    sec_value = state["host_security_value"]
    det_factor = _effective_detection_factor(state, decker)
    eff = _get_decker_effective(decker, state)

    ctx = pending.get("ctx", {})
    # Hacking Pool dice actually applied to the icon's resistance, capped at what remains in the
    # pool (the schema also bounds the request). 0 = resist with Bod alone / decline the offer.
    hp = min(int(body.hacking_pool_dice or 0), state.get("hackingPool_remaining", 0))
    if hp > 0:
        _spend_hp(state, hp)

    # Clear the prompt BEFORE resolving so a fresh park later in the resumed pass can set a new one.
    state["pending_defense"] = None

    ic = next((x for x in state.get("active_ic", []) if x.get("id") == pending.get("ic_id")), None)
    if ic is not None:
        run_ended = _resolve_ic_cybercombat(
            state, decker, ic,
            ic_attack_pool=ctx.get("ic_attack_pool", sec_value),
            ic_target_status=ctx.get("ic_target_status", _pc_target_status(state)),
            eff=eff,
            atk_power_delta=ctx.get("atk_power_delta", 0),
            atk_tn_delta=ctx.get("atk_tn_delta", 0),
            cluster_penalty=ctx.get("cluster_penalty", 0),
            ic_category=ctx.get("ic_category", "white"),
            sec_code=ctx.get("sec_code", sec_code),
            sec_value=ctx.get("sec_value", sec_value),
            precomputed_attack_roll=pending.get("to_hit_roll"),
            defender_bonus_dice=hp,
        )
    else:
        # The parked IC vanished (crashed/suppressed between park and defend) -- nothing to resolve;
        # just resume the pass so the remaining hostiles still act.
        run_ended = bool(state.get("run_ended"))

    # Resume the rest of the NPC pass (remaining IC + enemy deckers). This may park again on the
    # next IC that lands a hit, setting a fresh pending_defense the client will prompt for. The
    # already-resolved IC has acted_pass set, so it will not act again. logon_completed is carried
    # forward so a Logon that paused mid-pass still fires its event once the pass finally finishes.
    if not run_ended:
        _advance_npc_pass(
            state, decker, run,
            eff=eff, sec_code=sec_code, sec_value=sec_value, det_factor=det_factor,
            logon_completed=bool(pending.get("resume_logon_completed")),
            allow_defense_pause=True,
        )

    if state.get("run_ended"):
        run.status = state.get("end_reason", "crashed")
    # A run that ends mid-transfer corrupts the in-progress download (a partial copy is worthless).
    if state.get("run_ended") and state.get("active_download"):
        _corrupt_active_download(state)

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


def _ic_is_trace(ic: dict) -> bool:
    """True when this IC is a Trace IC (catalog subtype 'trace'). A Trap Trace is defused (its
    hidden IC never triggers) if it is crashed in cybercombat; the hidden IC triggers only when the
    location cycle completes (vr2 Trap IC, vr2_rules.md L688)."""
    return rules.IC_CATALOG.get(_canonical_ic_type(ic.get("type", "")), {}).get("subtype") == "trace"


def _trace_is_targetable(ic: dict) -> bool:
    """Whether a Trace IC can currently be targeted by the decker (attack/Slow/etc.), per the
    visibility rule (vr2 Trace IC + user ruling 2026-07-10). A trace is VISIBLE while it is
    running its Hunt Cycle (it is "attacking" the decker). The instant it hits and enters its
    Location Cycle it "disappears" and becomes reactive/hidden -- untargetable until a successful
    Locate IC op re-acquires it (sets ``ic['located']``). Non-trace IC: this helper is not used."""
    phase = ic.get("trace_phase", "hunt")
    if phase in ("hunt", "hunting", "hunt_hit"):
        return True
    if phase == "locate":
        return bool(ic.get("located"))
    return False



def _spawn_trap_hidden(state: dict, source_ic: dict, sec_code: str) -> dict | None:
    """Reveal + activate the hidden IC concealed behind a Trap IC (vr2 Trap IC). Spawns a fresh
    active IC (new initiative roll) and logs the trap-trigger. Returns the new IC dict, or None if
    ``source_ic`` carried no ``trap_hidden``. Shared by the cybercombat-crash paths (white/gray trap)
    and the Trace location-cycle-completion path (trace trap)."""
    trap_hidden = source_ic.get("trap_hidden")
    if not trap_hidden:
        return None
    h_type   = trap_hidden.get("type", "Blaster")
    h_rating = trap_hidden.get("rating", 6)
    new_id   = f"ic_{uuid.uuid4().hex[:8]}"
    new_init = eng.ic_initiative_roll(h_rating, sec_code)
    new_ic = {
        "id": new_id,
        "type": h_type,
        "rating": h_rating,
        "category": rules.IC_CATALOG.get(h_type, {}).get("category", "gray"),
        "boxes": 0,
        "suppressed": False,
        "initiative": new_init,
        "status": "active",
        "hunt_cycle_successes": 0,
    }
    state["active_ic"].append(new_ic)
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
    return new_ic


def _apply_ic_crash(state: dict, target_ic: dict, sec_code: str, skulk: int) -> None:
    """Resolve an IC crash: mark it crashed, bump the security tally (masked by the Skulk
    rating), log the crash event, check sheaf triggers, and spawn any hidden Trap IC (a Trap
    Trace crashed in cybercombat is defused instead -- vr2 L688). Shared by the single-target
    Attack and the Area strike so both stay in lock-step."""
    target_ic["status"] = "crashed"
    # Skulk masks the crash: reduce the tally increase by the Skulk rating, but never below 0
    # and never zero out a high-rating IC entirely (Rating-10 IC, Skulk-8 -> +2).
    tally_increase = max(0, target_ic["rating"] - skulk)
    applied = _bump_security_tally(state, tally_increase)
    # Suppression immediate query (vr2): a fresh crash is a suppressible event -- record the exact
    # tally it added (``crash_tally``) and mark it pending so the sheaf holds this increment until
    # the decker chooses to suppress (refund) or accept it. Cleared once decided / flushed.
    target_ic["crash_tally"] = applied
    target_ic["crash_pending"] = True
    target_ic["crash_turn"] = state.get("current_turn", 1)
    skulk_note = (
        f" (Skulk-{skulk} masked the crash)"
        if skulk > 0 and tally_increase < target_ic["rating"] else ""
    )
    _append_event(state, {
        "type": "ic_crashed",
        "ic_id": target_ic["id"],
        "description": (
            f"{target_ic['type']}-{target_ic['rating']} CRASHED. "
            f"Tally +{applied} -> {state['security_tally']}{skulk_note}"
        ),
        "tally_increase": applied,
    })
    _check_and_activate_sheaf(state, sec_code)

    # Trap IC (vr2 L688): a white/gray trap triggers its hidden IC when DESTROYED in cybercombat.
    # A Trap Trace is the exception -- crashing it during the hunt cycle DEFUSES it; its hidden IC
    # triggers only on location-cycle completion (handled in the Trace phase logic).
    if not _ic_is_trace(target_ic):
        _spawn_trap_hidden(state, target_ic, sec_code)


@router.post("/{run_id}/attack", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
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
    # A trace IC that has begun its Location Cycle has vanished (reactive/hidden) -- it cannot be
    # attacked until a successful Locate IC re-acquires it (vr2 Trace IC visibility, user ruling).
    if _ic_is_trace(target_ic) and not _trace_is_targetable(target_ic):
        raise HTTPException(
            400, "That trace IC has vanished into its location cycle -- run Locate IC to "
                 "re-acquire it before you can attack it.")
    # Limit option (vr2): an Attack utility Limited to deckers is useless against IC.
    if (((decker.get("program_options") or {}).get("attack") or {}).get("limit_target")) == "decker":
        raise HTTPException(400, "This Attack utility is Limited to deckers -- it cannot target IC.")
    _one_shot_block(state, decker, "attack")  # a spent One-Shot Attack cannot fire again until reloaded
    _spend_pass_action(state, "attack")        # vr2: a cybercombat attack is a Simple Action
    _assert_not_dinab_locked(state, "attack")  # DINAB per-pass lock: can't hand-fire an Attack DINAB ran
    _record_manual_program(state, "attack")

    _spend_hp(state, body.hacking_pool_dice)
    attack_pool     = body.attack_pool + body.hacking_pool_dice
    run_trace.trace(
        f"PC attacks {target_ic['type']}-{target_ic['rating']} ({body.target_ic_id}); "
        f"pool {attack_pool} = {body.attack_pool} attack + {body.hacking_pool_dice} hacking"
    )
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
    # vr2 L2028: the to-hit column is the TARGET icon's status, not the attacker's. IC are
    # Legitimate host residents, so the PC hits them on the Legitimate column.
    tgt_status = _combat_target_status(target_ic)
    base_tn = rules.COMBAT_TN[sec_code][tgt_status] + atk_cluster_penalty
    # Shield/Shift raise the decker's to-hit TN; Penetration defeats Shield, Chaser defeats Shift.
    shield_shift = _shield_shift_tn_modifier(
        target_ic, penetration=opt_pen, chaser=opt_chaser)
    # A lurking Deathworm raises the decker's cybercombat attack (and resist) TN (vr2 worm variant).
    dw_bonus = _deathworm_tn_bonus(state)
    # The decker's own cumulative wound penalty raises their to-hit TN (+1 per wound level).
    tn = base_tn + shield_shift + tgt_tn_delta + _decker_wound_mod(state) + dw_bonus
    if opt_target:
        tn = max(2, tn - 2)   # Targeting option: -2 to-hit TN on attacks with this utility
    tn = max(2, tn)           # clamp (a Position TN reduction can never push the TN below 2)

    run_trace.trace(
        f"to-hit TN {tn}: base {base_tn} (COMBAT_TN {rules.COMBAT_TN[sec_code][tgt_status]} "
        f"{tgt_status} + cluster {atk_cluster_penalty}) + shield/shift {shield_shift} "
        f"+ parry {tgt_tn_delta} + wound {_decker_wound_mod(state)}"
        + (" - 2 targeting" if opt_target else "")
    )
    # Unified cybercombat resolution -- the SAME eng.cybercombat_attack primitive every other
    # attack direction uses (IC->PC, decker->PC, PC->enemy). The decker is the attacker
    # (attacker_is_ic=False); per vr2 the targeted icon resists with a Bod Resistance Test vs a
    # TN equal to the Power of the attack -- so Power = the Attack utility's Rating (+ any Position
    # bonus), NOT the combat-to-hit TN. Armor reduces that Power (extra-effective vs an Area burst).
    # The IC resists with Security Value dice (+/- Expert). All to-hit modifiers (cluster, Shield/
    # Shift, Parry, wound, Targeting) ride in via tn_modifier so the core rolls one identical way.
    attack_rating  = int((decker.get("utilities") or {}).get("attack", 4) or 4)
    ic_resist_pool = max(1, sec_value + _ic_expert(target_ic, "defense") - _ic_expert(target_ic, "offense"))
    ic_armor       = (2 + (2 if opt_area > 0 else 0)) if _ic_has_armor(target_ic) else 0
    # NOTE: cluster_penalty is folded into Power to preserve current Party-IC resist behaviour
    # verbatim (Party-IC is revisited in coverage item C10); with no Party cluster it is 0.
    attack_power   = attack_rating + cluster_penalty + tgt_power_delta
    attack = eng.cybercombat_attack(
        attacker_pool=attack_pool,
        security_code=sec_code,
        target_status=tgt_status,
        target_bod=ic_resist_pool,
        armor_rating=ic_armor,
        ic_rating=attack_power,
        attacker_is_ic=False,
        tn_modifier=atk_cluster_penalty + shield_shift + tgt_tn_delta
                    + _decker_wound_mod(state) + dw_bonus - (2 if opt_target else 0),
        base_damage_level=_attack_damage_level(decker, sec_code),
    )
    attack_roll = attack["attack_roll"]
    resist_roll = attack["resistance"]["resist_roll"]
    final_dmg   = attack["resistance"]["final_damage_level"]
    boxes       = attack["resistance"]["boxes"]
    run_trace.trace(
        f"IC resist {ic_resist_pool}d6 vs Power {attack_power} (attack rating {attack_rating}"
        + (f" + cluster {cluster_penalty}" if cluster_penalty else "")
        + (f" + position {tgt_power_delta}" if tgt_power_delta else "")
        + (f", -armor {ic_armor}" if ic_armor else "")
        + f") -> {resist_roll['successes']} succ -> {final_dmg} ({boxes} boxes)"
    )

    target_ic["boxes"] = target_ic.get("boxes", 0) + boxes
    crashed = target_ic["boxes"] >= 10
    run_trace.trace(
        f"outcome: {final_dmg} = {boxes} boxes; {target_ic['type']} now "
        f"{target_ic['boxes']}/10" + (" -> CRASHED" if crashed else "")
    )

    if crashed:
        target_ic["status"] = "crashed"
        # Skulk option on the Attack utility masks the crash: reduce the resulting security-tally
        # increase by the Skulk rating (vr2_rules). Skulk does NOT zero the bump at 6+ -- a high-
        # rating IC still leaks tally past the masking (e.g. Rating-10 IC, Skulk-8 -> +2). The
        # bump is otherwise the crashed IC's full rating. Read automatically from the deck.
        skulk = opt_skulk
        tally_increase = max(0, target_ic["rating"] - skulk)
        applied = _bump_security_tally(state, tally_increase)
        # Fresh crash = suppressible immediate query: hold this increment from the sheaf until decided.
        target_ic["crash_tally"] = applied
        target_ic["crash_pending"] = True
        target_ic["crash_turn"] = state.get("current_turn", 1)
        skulk_note = (
            f" (Skulk-{skulk} reduced the crash tally by {target_ic['rating'] - tally_increase})"
            if skulk > 0 and tally_increase < target_ic["rating"] else ""
        )
        _append_event(state, {
            "type": "ic_crashed",
            "ic_id": body.target_ic_id,
            "description": (
                f"{target_ic['type']}-{target_ic['rating']} CRASHED. "
                f"Tally +{applied} -> {state['security_tally']}{skulk_note}"
            ),
            "tally_increase": applied,
            "attack_roll": attack_roll,
            "resist_roll": resist_roll,
            "final_damage_level": final_dmg,
            "boxes": boxes,
            "ic_boxes": target_ic["boxes"],
        })
        _check_and_activate_sheaf(state, sec_code)

        # Trap IC (vr2 L688): destroying a white/gray trap in cybercombat triggers its hidden IC.
        # A Trap Trace is the exception -- crashing it during the hunt cycle DEFUSES it; its hidden
        # IC triggers only on location-cycle completion.
        if not _ic_is_trace(target_ic):
            _spawn_trap_hidden(state, target_ic, sec_code)
    else:
        _append_event(state, {
            "type": "decker_attack",
            "ic_id": body.target_ic_id,
            "description": (
                f"Attacked {target_ic['type']}-{target_ic['rating']}: "
                f"{attack_roll['successes']} successes. "
                + ("Target resisted all damage." if boxes <= 0
                   else f"Dealt {final_dmg} ({boxes} boxes).")
                + f" IC: {target_ic['boxes']}/10"
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
    (storage_programs / program_sizes / program_damage / squeezed_active) and ``decker``
    (utilities) in place and returns ``(decker_changed, description)``. Modes, in priority order:

      1. Load a stored program into active memory (``target_program`` names a stored program),
         optionally pushing ``swap_out_program`` from active back to storage to make room. A
         Squeezed program loads at FULL active size but stays COMPRESSED (held out of
         decker.utilities so it is unusable) until a Decompress action expands it (vr2 L1673).
      2. Push an active program to storage only (``swap_out_program`` set, no storage target) --
         a usable program OR a still-compressed one swapped in earlier. A squeezed program returns
         to storage at half footprint, re-compressed (no test).
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
    squeezed_active = state.setdefault("squeezed_active", [])
    squeeze_keys = set(state.get("squeeze_keys") or [])
    cap     = int(state.get("active_memory_cap", 0) or 0)

    def _pretty(n: str) -> str:
        return str(n).replace("_", " ").title()

    def _active_used() -> int:
        # Full active footprint = usable loaded utilities PLUS squeezed programs swapped in but not
        # yet decompressed (they occupy full active memory even while unusable).
        used = sum(int(sizes.get(n, 0)) for n, r in utils.items() if (r or 0) > 0)
        used += sum(int(p.get("size", 0) or 0) for p in squeezed_active)
        return used

    def _store_append(name: str, rating: int, size: int) -> None:
        # A squeezed program returns to storage still flagged so its footprint stays halved and a
        # later reload needs another decompress.
        storage.append({"name": name, "rating": int(rating or 0), "size": int(size or 0),
                        "squeezed": name in squeeze_keys})

    def _pop_squeezed_active(name: str):
        ent = next((p for p in squeezed_active
                    if str(p.get("name", "")).strip().lower() == name), None)
        if ent is not None:
            squeezed_active.remove(ent)
        return ent

    def _push_active_out(name: str) -> str:
        # Push an active program (usable OR a pending compressed copy) back to storage to free
        # room; returns a note fragment ("" if nothing was pushed).
        if (utils.get(name, 0) or 0) > 0:
            _store_append(name, utils.get(name, 0), sizes.get(name, 0))
            utils[name] = 0
            pd.pop(name, None)
            return f" (swapped {_pretty(name)} out to storage)"
        ent = _pop_squeezed_active(name)
        if ent is not None:
            _store_append(name, ent.get("rating", 0), ent.get("size", 0))
            return f" (swapped compressed {_pretty(name)} out to storage)"
        return ""

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
        is_squeezed = bool(store_entry.get("squeezed")) or target in squeeze_keys
        note = ""
        if swap_out:
            note = _push_active_out(swap_out)
        if cap > 0 and _active_used() + in_size > cap:
            used = _active_used()
            raise HTTPException(
                400,
                f"Not enough active memory to load {_pretty(target)}: needs {in_size} Mp but "
                f"only {max(0, cap - used)} Mp free ({used}/{cap} Mp used). Swap a program out "
                "to free active memory."
            )
        storage.remove(store_entry)
        if is_squeezed:
            # Occupies FULL active memory immediately but stays UNUSABLE (out of decker.utilities)
            # until a Decompress action expands it.
            squeezed_active.append({"name": target,
                                    "rating": int(store_entry.get("rating", 0) or 0),
                                    "size": in_size})
            return True, (f"Swap Memory -- loaded {_pretty(target)} into active memory still "
                          f"COMPRESSED{note}. Decompress it (Complex Action) before use.")
        utils[target] = int(store_entry.get("rating", 0) or 0)
        sizes[target] = in_size
        pd.pop(target, None)   # fresh storage copy -- no accrued damage
        return True, (f"Swap Memory -- loaded {_pretty(target)} (rating {utils[target]}) into "
                      f"active memory{note}.")

    if swap_out:
        # Mode 2: push an active program to storage (no incoming program) -- usable or compressed.
        if (utils.get(swap_out, 0) or 0) > 0:
            _store_append(swap_out, utils.get(swap_out, 0), sizes.get(swap_out, 0))
            utils[swap_out] = 0
            pd.pop(swap_out, None)
            return True, f"Swap Memory -- moved {_pretty(swap_out)} from active memory to storage."
        ent = _pop_squeezed_active(swap_out)
        if ent is not None:
            _store_append(swap_out, ent.get("rating", 0), ent.get("size", 0))
            return True, (f"Swap Memory -- moved compressed {_pretty(swap_out)} from active memory "
                          "back to storage.")

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

    tally_increase = _bump_security_tally(state, test["tally_increase"])

    if test["success"]:
        state["run_ended"] = True
        state["end_reason"] = "graceful_logoff"
        _finalize_run_end(state)
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


@router.post("/{run_id}/logoff", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
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
    # Bailing out mid-transfer corrupts the partial download (vr2: needs the COMPLETE file).
    if success and state.get("active_download"):
        _corrupt_active_download(state)
    if success:
        # Deep-linked via trap doors? A graceful logoff drops back to the suspended parent host
        # rather than ending the whole run (B34). Only an empty stack is a real run end.
        popped = _pop_host_stack(state)
        if popped is not None:
            state, parent_host_id = popped
            if parent_host_id is not None:
                run.host_id = parent_host_id
        else:
            run.status = "escaped"

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


def _push_host_stack(state: dict, current_host: MatrixHost, dest_host: MatrixHost, decker: dict) -> dict:
    """Suspend the CURRENT host onto the run's trap-door stack and open a fresh session on
    ``dest_host`` (B34). Returns the new state: a fresh initial state for the destination with the
    decker's persona-scoped fields (icon/deck damage, hacking pool, loot) carried forward, and the
    suspended parent frame pushed onto ``host_stack``. Persona continuity in; host frame swapped."""
    stack = list(state.get("host_stack") or [])
    snapshot = copy.deepcopy(state)
    snapshot.pop("host_stack", None)
    snapshot["_stack_host_id"] = current_host.id
    snapshot["_stack_host_name"] = current_host.name
    fresh = _initial_state(decker, dest_host)
    for k in _PERSONA_CARRY_KEYS:
        if k in state:
            fresh[k] = copy.deepcopy(state[k])
    fresh["host_stack"] = stack + [snapshot]
    fresh["_stack_current_host_name"] = dest_host.name
    return fresh


def _pop_host_stack(state: dict) -> tuple[dict, int | None] | None:
    """Resume the suspended parent host off the top of the trap-door stack (B34), carrying the
    decker's persona-scoped fields back from the just-exited deeper host. Returns
    ``(resumed_state, parent_host_id)`` or None when the stack is empty (a real run end). The
    caller retargets ``run.host_id`` to the returned id and keeps the run active."""
    stack = list(state.get("host_stack") or [])
    if not stack:
        return None
    parent = stack.pop()
    host_id = parent.pop("_stack_host_id", None)
    parent_name = parent.pop("_stack_host_name", "the previous host")
    for k in _PERSONA_CARRY_KEYS:
        if k in state:
            parent[k] = copy.deepcopy(state[k])
    parent["host_stack"] = stack
    parent["run_ended"] = False
    parent["end_reason"] = None
    child_name = state.get("_stack_current_host_name", "the deeper host")
    _append_event(parent, {
        "type": "trap_door_return",
        "description": (
            f"Dropped back through the trap door from \"{child_name}\" to \"{parent_name}\" "
            "-- still jacked in."
        ),
    })
    return parent, host_id


@router.post("/{run_id}/trap-door/{td_id}", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
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
    subsystem, then -- on success -- the current host is SUSPENDED onto the run's trap-door stack
    (B34) and a fresh session opens on the destination host (same run, run.host_id retargeted),
    where the decker must Logon to Host (and can Analyze its Access subsystem to learn its LTG
    status). A later graceful logoff or host crash drops back to the suspended parent; a dump /
    death / KO on any host ends the whole run. The destination is never sent to a player before
    arrival. Depth is capped at HOST_STACK_CAP."""
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
    if len(state.get("host_stack") or []) >= HOST_STACK_CAP:
        raise HTTPException(
            400,
            f"Trap-door stack is at its practical depth limit ({HOST_STACK_CAP}). "
            "Log off a host before diving deeper.",
        )
    dest_host = await _get_host_or_404(db, dest_id)
    src_host = await _get_host_or_404(db, run.host_id) if run.host_id else None

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

    # Transit succeeded -- the current host is SUSPENDED (not logged off): neutralize the run-ending
    # side effects the shared logoff helper applied, then suspend it onto the stack and open a fresh
    # session on the destination (same run row; run.host_id retargeted). B34.
    if state.get("event_log") and state["event_log"][-1].get("type") == "logoff_success":
        state["event_log"].pop()
    state["run_ended"] = False
    state["end_reason"] = None
    if src_host is None:
        # No source host row (shouldn't happen for an active run) -- fall back to a bare frame.
        src_host = type("_H", (), {"id": run.host_id, "name": "the previous host"})()
    new_state = _push_host_stack(state, src_host, dest_host, run.decker_json)
    _append_event(new_state, {
        "type": "trap_door_entered",
        "trap_door_id": door.get("id"),
        "destination_host_id": dest_id,
        "description": (
            f"Entered trap door -- suspended \"{src_host.name}\" and arrived at "
            f"host \"{dest_host.name}\". Logon to continue (logoff or crash this host to drop back)."
        ),
    })
    run.host_id = dest_host.id
    run.state_json = new_state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


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
    _finalize_run_end(state)
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


def _process_host_shutdown_countdown(state: dict, decker: dict) -> None:
    """End-of-Combat-Turn Host Shutdown processing (vr2_rules.md L771-789).

    The host shutdown runs for a fixed number of Combat Turns (rolled at initiation). Each turn:
    decrement the countdown; if it reaches zero the sequence completes and every online decker is
    DUMPED (Dump Shock applies) with all frames/programs crashing and the run ending. Otherwise,
    until the decker becomes aware, make a SECRET Sensor Test against TN = turns remaining -- the
    first success reveals the shutdown; on the final-warning turn the decker is told automatically.
    """
    cd = state.get("shutdown_countdown")
    if not cd or state.get("run_ended"):
        return
    cd["elapsed"] = int(cd.get("elapsed", 0)) + 1
    cd["turns_remaining"] = int(cd.get("turns_remaining", 1)) - 1
    remaining = cd["turns_remaining"]

    if remaining <= 0:
        sec_code = state.get("host_security_code", "Green")
        sec_value = int(state.get("host_security_value", 6) or 6)
        ds = _apply_dump_shock(state, decker, sec_code, sec_value)
        state["run_ended"] = True
        state["end_reason"] = "host_shutdown"
        _finalize_run_end(state)
        state.pop("shutdown_countdown", None)
        _append_event(state, {
            "type": "shutdown", "dump_shock": ds,
            "description": (
                "HOST SHUTDOWN COMPLETE -- all online deckers are dumped (Dump Shock); every "
                "frame and program crashes and all operations terminate."
            ),
        })
        return

    if not cd.get("known"):
        if cd["elapsed"] >= int(cd.get("final_warning_turn", 1) or 1):
            cd["known"] = True
            _append_event(state, {
                "type": "shutdown_warning", "turns_remaining": remaining,
                "description": (
                    f"FINAL WARNING -- the host announces it is shutting down. {remaining} Combat "
                    f"Turn(s) until every decker is dumped. Grab paydata and get out."
                ),
            })
            return
        eff = _get_decker_effective(decker, state)
        sensor = int(eff.get("sensor", decker.get("sensor", 1)) or 1)
        roll = eng.roll_dice(max(1, sensor), max(2, remaining))
        if roll["successes"] > 0:
            cd["known"] = True
            _append_event(state, {
                "type": "shutdown_detected", "turns_remaining": remaining, "roll": roll,
                "description": (
                    f"Your Sensors catch it: the HOST IS SHUTTING DOWN -- roughly {remaining} "
                    f"Combat Turn(s) until you are dumped. Get out."
                ),
            })
        else:
            _append_event(state, {
                "type": "shutdown_tick", "gm_only": True, "turns_remaining": remaining,
                "description": (
                    f"(GM) Host shutdown in progress: {remaining} turn(s) left; the decker's "
                    f"secret Sensor Test (TN {max(2, remaining)}) failed -- still unaware."
                ),
            })
        return

    _append_event(state, {
        "type": "shutdown_tick", "turns_remaining": remaining,
        "description": f"Host shutdown: {remaining} Combat Turn(s) until you are dumped.",
    })


@router.post("/{run_id}/new-turn", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
async def new_turn(
    run_id: int,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """End the decker's current initiative pass ("End Turn" / "End Pass" in the UI).

    If the decker still has initiative passes left this Combat Turn, this ENDS THE PASS: the
    hostiles on the pass being left get to act, then the decker's action budget and Hacking Pool
    refresh for the next pass. The Combat Turn and the decker's initiative are unchanged -- SR2
    rolls initiative ONCE per cybercombat encounter, never per turn or per pass.

    On the decker's LAST pass this ENDS THE COMBAT TURN: any hostiles with more passes finish out
    the turn, then the next Combat Turn begins. Initiative is still unchanged; only the decker's
    pass COUNT is re-derived from its current cumulative wound penalty."""
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")
    state = copy.deepcopy(run.state_json)  # deepcopy, not dict(): keep nested JSON mutations un-aliased so the UPDATE fires
    if state.get("run_ended"):
        raise HTTPException(400, "Run has already ended")
    _assert_no_pending_defense(state)   # resolve a parked IC strike (POST /defend) before ending the pass

    # Default acting context to the decker's initiative; the NPC driver overrides it per hostile.
    state["_acting_init"] = state.get("decker_initiative")

    npc_decker = run.decker_json
    npc_sec_code = state.get("host_security_code")

    # Any suppression immediate query the decker left UNDECIDED (a fresh crash or a bomb detonation
    # they neither suppressed nor accepted) is auto-accepted now: the decision cannot outlive the
    # pass/turn it was raised on, so the held-back tally is released to the sheaf before the NPCs act.
    _flush_pending_suppressions(state, npc_sec_code)

    # -- END PASS: the decker still has initiative passes left this Combat Turn -------------------
    # Close the current pass -- the hostiles on it act now (idempotent via acted_pass: any that
    # already acted when the decker took an action this pass are skipped) -- then open the next
    # pass with a fresh action budget + Hacking Pool. Combat Turn and initiative are unchanged.
    cur_pass = state.get("current_pass", 1)
    total_passes = state.get("initiative_passes", 1)
    if npc_sec_code is not None and cur_pass < total_passes:
        npc_sec_value = state["host_security_value"]
        _check_and_activate_sheaf(state, npc_sec_code)
        _advance_npc_pass(
            state, npc_decker, run,
            eff=_get_decker_effective(npc_decker, state),
            sec_code=npc_sec_code, sec_value=npc_sec_value,
            det_factor=_effective_detection_factor(state, npc_decker),
            logon_completed=False,
        )
        if state.get("run_ended"):
            # A hostile on the pass being left killed the decker -- end the run here.
            run.status = state.get("end_reason", "crashed")
            if state.get("active_download"):
                _corrupt_active_download(state)
            run.state_json = state
            await db.commit()
            await db.refresh(run)
            return _serialize_run(run, auth)
        state["current_pass"] = cur_pass + 1
        _reset_pass_budget(state)
        _append_event(state, {
            "type": "new_pass",
            "description": (
                f"Turn {cur_pass + 1}/{total_passes} begins -- actions refreshed "
                "(2 AP + 1 Free) and Hacking Pool restored."
            ),
        })
        run.state_json = state
        await db.commit()
        await db.refresh(run)
        return _serialize_run(run, auth)

    # -- END TURN: the decker is on its last pass -> finish hostile passes, then next Combat Turn -
    # -- End-of-turn NPC pass flush (app-as-GM) --------------------------------------------------
    # current_pass only ever climbs as far as the DECKER's own initiative passes (via the action
    # economy), so a hostile with MORE passes than the decker -- or any hostile at all, when the
    # decker ends the turn without acting -- would be cheated of the passes it never got. Before
    # the turn resets, drive those remaining passes now: no human GM runs the opposition. Each
    # NPC self-gates on its OWN initiative passes and its acted_pass marker, so passes already
    # taken this turn are skipped (idempotent) and only the missing ones fire.
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
            f"Round {state['current_turn']} begins. Actions refreshed (initiative {init} "
            f"unchanged, {passes} turn{'s' if passes != 1 else ''}). "
            f"Hacking Pool ({old_hp} -> {hackingPool_total})."
        ),
    })

    # Persistent Hog infections re-drain the highest running program each Combat Turn (vr2),
    # in BOTH directions -- an enemy's virus on the PC and the PC's own virus on an enemy decker
    # (one loop, one resolver; see _drain_all_hog_infections).
    decker = run.decker_json
    _drain_all_hog_infections(state, decker)

    # Worm infection is NOT a per-turn tick (vr2 L548): a Worm booby-traps a subsystem and only
    # risks infecting the MPCP when the decker makes a System Test AGAINST that infested subsystem.
    # That trigger lives in perform_action (_trigger_subsystem_worms), not here. (Historically this
    # loop fired every Combat Turn -- reconciled to RAW 2026-07-17.)

    # Multi-turn Download Data (vr2 ongoing operation): each turn a background transfer runs, the
    # deck auto-performs a Null Operation (Control System Test) while it waits -- its tally rises
    # like any op and can wake the sheaf. When the final turn elapses the file lands on the deck
    # (storage charged); until then the decker had only Free actions.
    _dl = state.get("active_download")
    if _dl and not state.get("run_ended"):
        _tick_active_download(state, decker, _dl)

    # End-of-turn Crash Host processing: host abort roll + countdown decrement / resolution.
    _process_crash_countdown(state)

    # End-of-turn Host Shutdown processing: secret Sensor detection + countdown / final dump.
    _process_host_shutdown_countdown(state, decker)

    # A completed Crash Host ends the run as a clean exit (treated like a graceful logoff).
    if state.get("run_ended"):
        _er = state.get("end_reason")
        if _er == "host_crashed" and (state.get("host_stack")):
            # Deep-linked via trap doors: crashing the CURRENT host drops back to the suspended
            # parent rather than ending the whole run (B34).
            popped = _pop_host_stack(state)
            if popped is not None:
                state, parent_host_id = popped
                if parent_host_id is not None:
                    run.host_id = parent_host_id
        if state.get("run_ended"):
            _er = state.get("end_reason")
            if _er == "host_crashed":
                run.status = "escaped"
            elif _er == "host_shutdown":
                run.status = "dumped"
            else:
                run.status = _er or "crashed"
    # A transfer still running when the run ends this turn (host crash, etc.) is corrupted (vr2).
    if state.get("run_ended") and state.get("active_download"):
        _corrupt_active_download(state)

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


def _trigger_subsystem_worms(state: dict, decker: dict, subsystem: str) -> None:
    """vr2 L548 -- "Any System Test against a worm-infested subsystem risks infecting the decker's
    MPCP." Called right after the generic System Test in perform_action: for every lurking Worm on
    the subsystem just tested, roll its Worm Infection Test. A worm with no recorded subsystem
    (legacy/authoring gap) is treated as covering any subsystem so it still fires. Mutates
    ``state``; each worm appends a ``worm_resolved`` event via ``_resolve_lurking_worm``."""
    sub = (subsystem or "").strip().lower()
    for worm in list(state.get("lurking_ic", [])):
        if state.get("run_ended"):
            break
        if worm.get("type") != "Worm" or worm.get("status", "lurking") != "lurking":
            continue
        wsub = (worm.get("subsystem", "") or "").strip().lower()
        if wsub and sub and wsub != sub:
            continue   # this worm guards a different subsystem
        _resolve_lurking_worm(state, decker, worm, subsystem=subsystem)


def _resolve_lurking_worm(state: dict, decker: dict, lurking: dict, *, subsystem: str = "") -> None:
    """Resolve one lurking Worm's infection attempt against the deck's MPCP (vr2_rules.md L548-550).

    The Worm Infection Test is the HOST's Security Value dice vs the deck's MPCP rating; the deck's
    Hardening is subtracted from the worm's successes and a net greater than 0 infects the MPCP
    (permanent -- the chip must be replaced). The worm carries no IC rating, so no security tally is
    added. Infection is the GATE for every worm: only once it compromises the MPCP does the worm's
    variant payload take effect (Deathworm cybercombat penalty / Tapeworm paydata erasure); a plain
    worm simply degrades the chip. An infected worm is recorded in ``state["mpcp_infections"]`` --
    a PERSISTENT deck status that carries across runs until the MPCP chip is replaced -- and removed
    from ``lurking_ic``; a repelled worm stays lurking to try again on the next System Test against
    its subsystem. Mutates ``state``; appends a ``worm_resolved`` event. Called from
    ``_trigger_subsystem_worms`` when the decker makes a System Test against the worm's subsystem.
    """
    hardening = decker.get("hardening", 0)
    variant = lurking.get("variant", "standard")
    _sub_label = (subsystem or lurking.get("subsystem", "") or "").strip()
    _where = f" on the {_sub_label.title()} subsystem" if _sub_label else ""
    wr = eng.worm_attack(
        security_value=state.get("host_security_value", 1),
        mpcp_rating=decker.get("mpcp", 1),
        hardening=hardening,
    )
    if wr["mpcp_infected"]:
        state["mpcp_infected"] = True
        state["chip_replacement_required"] = True
        # Record the infection as a persistent deck status keyed by variant (carried across runs
        # via the decker payload until the chip is replaced). Deathworm -> ongoing cybercombat
        # penalty; Tapeworm -> paydata erasure at every run end; standard -> chip degraded only.
        state.setdefault("mpcp_infections", []).append({
            "variant": variant, "rating": lurking.get("rating", 6), "ic_id": lurking["id"],
        })
        state["lurking_ic"] = [
            ic for ic in state.get("lurking_ic", []) if ic["id"] != lurking["id"]]
        _vlabel = {"deathworm": "Deathworm", "tapeworm": "Tapeworm"}.get(variant, "Worm")
        _payload = {
            "deathworm": " Cybercombat TNs are now degraded until the MPCP chip is replaced.",
            "tapeworm": " It will corrupt downloaded paydata every run until the chip is replaced.",
        }.get(variant, "")
        _append_event(state, {
            "type": "worm_resolved", "ic_id": lurking["id"], "ic_type": "Worm",
            "outcome": "mpcp_infected", "variant": variant, "roll": wr["roll"],
            "subsystem": _sub_label,
            "description": (
                f"Your System Test{_where} tripped a {_vlabel}-{lurking['rating']} -- it infected "
                f"the MPCP causing permanent infection."
                f"{_payload} Infection Test: host {wr['roll']['pool']}d6 vs MPCP TN "
                f"{wr['tn']}, net {wr['net_successes']} after Hardening-{hardening}."
            ),
        })
    else:
        _rlabel = {"deathworm": "Deathworm", "tapeworm": "Tapeworm"}.get(variant, "Worm")
        _append_event(state, {
            "type": "worm_resolved", "ic_id": lurking["id"], "ic_type": "Worm",
            "outcome": "repelled", "roll": wr["roll"], "subsystem": _sub_label,
            "description": (
                f"A {_rlabel}-{lurking['rating']}{_where} tried to infect your MPCP but was "
                f"repelled. Worm still lurking."
            ),
        })


def _deathworm_tn_bonus(state: dict) -> int:
    """Cybercombat TN penalty from Deathworm infection(s) (vr2 worm variant + user ruling).

    A Deathworm can only degrade the deck once it has INFECTED the MPCP -- the infection is the
    gate. An infected Deathworm adds +2 to the decker's cybercombat attack AND damage-resistance
    target numbers; each ADDITIONAL infected Deathworm adds +1 more. The infection persists across
    runs (carried in ``state["mpcp_infections"]``) until the MPCP chip is replaced. Returns 0 when
    no Deathworm has infected the deck."""
    n = sum(
        1 for inf in state.get("mpcp_infections", [])
        if inf.get("variant") == "deathworm"
    )
    return (n + 1) if n > 0 else 0


def _apply_tapeworm_run_end(state: dict) -> None:
    """Tapeworm payload sabotage, resolved once at run end (vr2 worm variant + user ruling).

    A Tapeworm can only corrupt data once it has INFECTED the MPCP -- the infection is the gate,
    and it persists across runs (carried in ``state["mpcp_infections"]``) so an infected deck loses
    paydata at the end of EVERY run until the MPCP chip is replaced. For each Tapeworm infection,
    when the run ends the worm deletes ``1D6-1`` NON-key files from the haul (``downloaded_files``)
    and -- if any KEY data was downloaded -- rolls ``1D6`` and on a 5-6 erases the key data. Both
    paths run when there is data to lose in either. Idempotent (guarded by ``tapeworm_resolved``);
    emits a ``tapeworm_payload_loss`` event listing what was destroyed."""
    if state.get("tapeworm_resolved"):
        return
    tapeworms = [
        inf for inf in state.get("mpcp_infections", [])
        if inf.get("variant") == "tapeworm"
    ]
    if not tapeworms:
        return
    state["tapeworm_resolved"] = True
    files = state.get("downloaded_files") or []
    if not files:
        return

    for _wm in tapeworms:
        files = state.get("downloaded_files") or []
        non_key = [f for f in files if not f.get("is_key")]
        key = [f for f in files if f.get("is_key")]
        destroyed: list[str] = []

        # 1D6-1 non-key files deleted.
        n_delete = max(0, random.randint(1, 6) - 1)
        if non_key and n_delete > 0:
            for f in non_key[:n_delete]:
                destroyed.append(str(f.get("name", "?")))

        # Key data: 1D6, on a 5-6 the key data is erased.
        key_roll = 0
        key_erased = False
        if key:
            key_roll = random.randint(1, 6)
            if key_roll >= 5:
                key_erased = True
                for f in key:
                    destroyed.append(str(f.get("name", "?")))

        if not destroyed:
            _append_event(state, {
                "type": "tapeworm_payload_loss", "ic_id": _wm.get("ic_id"),
                "destroyed_files": [], "key_erased": False, "key_roll": key_roll,
                "description": (
                    f"Tapeworm-{_wm.get('rating')} activates on jack-out but finds nothing to "
                    f"corrupt (rolled {n_delete} non-key deletions"
                    + (f", key roll {key_roll}" if key else "")
                    + ")."
                ),
            })
            continue

        state["downloaded_files"] = [
            f for f in (state.get("downloaded_files") or [])
            if str(f.get("name", "?")) not in destroyed
        ]
        _append_event(state, {
            "type": "tapeworm_payload_loss", "ic_id": _wm.get("ic_id"),
            "destroyed_files": destroyed, "key_erased": key_erased, "key_roll": key_roll,
            "description": (
                f"TAPEWORM-{_wm.get('rating')} corrupts your haul on jack-out: "
                f"{len(destroyed)} file(s) erased ({', '.join(destroyed)})"
                + (" -- KEY DATA LOST." if key_erased else ".")
            ),
        })


def _finalize_paydata_haul(state: dict) -> None:
    """Secure the paydata haul once the run truly ends (directive #6). Runs AFTER any Tapeworm
    payload loss so it only counts the files that survived.

    - Compressed files AUTO-COUNT: the deck's Compressor no longer needs a manual Decompress action
      once the run is over, so every surviving compressed file is expanded to its full size and its
      ``compressed`` flag is cleared on both the ledger row and the matching paydata row.
    - A persisted ``paydata_secured`` summary is stored on state so the after-action panel still
      shows what was secured AFTER the deck's working memory is wiped.
    - Emits a generic player-visible ``paydata_secured`` event (no behind-the-scenes detail) plus a
      detailed GM-only ``paydata_aar``.
    - Then clears the deck's working memory (downloaded ledger + storage meter + any aborted
      transfer) -- the haul has been delivered.

    Idempotent (guarded by ``paydata_finalized``). Skipped while a trap-door host stack is still
    suspended (``host_stack`` non-empty) so a graceful logoff that merely pops back to a parent host
    does NOT prematurely secure and wipe the mid-run haul."""
    if state.get("paydata_finalized") or state.get("host_stack"):
        return
    state["paydata_finalized"] = True

    files = list(state.get("downloaded_files") or [])
    secured: list[dict] = []
    total_mp = 0
    for f in files:
        full = max(int(f.get("size_mp", 0) or 0), int(f.get("full_size_mp", 0) or 0))
        was_compressed = bool(f.get("compressed"))
        f["size_mp"] = full
        f["compressed"] = False
        nm = str(f.get("name", "")).strip().lower()
        for p in (state.get("paydata") or []):
            if str(p.get("name", "")).strip().lower() == nm:
                p["compressed"] = False
        total_mp += full
        secured.append({
            "name": f.get("name"), "size_mp": full,
            "is_key": bool(f.get("is_key")), "was_compressed": was_compressed,
        })

    key_count = sum(1 for s in secured if s["is_key"])
    state["paydata_secured"] = {
        "files": secured, "count": len(secured),
        "total_mp": total_mp, "key_count": key_count,
    }

    # Player-visible confirmation -- generic, no GM detail.
    if secured:
        player_desc = (
            f"Run complete -- {len(secured)} paydata file(s) secured ({total_mp} Mp"
            + (f", {key_count} key data" if key_count else "") + ")."
        )
    else:
        player_desc = "Run complete -- no paydata secured."
    _append_event(state, {
        "type": "paydata_secured", "count": len(secured),
        "total_mp": total_mp, "key_count": key_count, "description": player_desc,
    })

    # GM-only after-action report -- full per-file breakdown incl. auto-decompressed flag.
    if secured:
        lines = ", ".join(
            f"{s['name']} ({s['size_mp']} Mp"
            + (", KEY" if s["is_key"] else "")
            + (", auto-decompressed" if s["was_compressed"] else "") + ")"
            for s in secured
        )
        gm_desc = (
            f"GM AAR -- {len(secured)} paydata file(s) survived to jack-out, {total_mp} Mp total"
            + (f", {key_count} key data" if key_count else "") + ": " + lines + "."
        )
    else:
        gm_desc = "GM AAR -- no paydata survived to jack-out."
    _append_event(state, {
        "type": "paydata_aar", "gm_only": True, "count": len(secured),
        "total_mp": total_mp, "key_count": key_count, "files": secured, "description": gm_desc,
    })

    # Deck working memory cleared -- the haul has been offloaded to the meat world.
    state["downloaded_files"] = []
    state["storage_used_mp"] = 0
    state["active_download"] = None


def _finalize_run_end(state: dict) -> None:
    """Single run-end hook: resolve Tapeworm payload loss, then secure the surviving paydata haul
    (directive #6). Both steps are idempotent, so calling this on any run-end path is safe."""
    _apply_tapeworm_run_end(state)
    _finalize_paydata_haul(state)


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
                f"{lurking['type']}-{lurking['rating']} triggered when "
                f"{utility_name}-{utility_rating} executed! "
                + (f"All copies of {utility_name} wiped." if is_tar_pit
                   else f"Active copy of {utility_name} wiped.")
            ),
        })
        if is_tar_pit and result.get("all_copies_corrupted"):
            _append_event(state, {
                "type": "tar_pit_corruption",
                "utility": _normalize_util_name(utility_name),
                "description": (
                    f"Tar Pit: ALL copies of {utility_name} corrupted -- gone for the rest of the "
                    "run (cannot be reloaded via Swap Memory)."
                ),
                "tar_pit_roll": result.get("tar_pit_roll"),
            })
            # Viral corruption of every copy (active + storage): the program is gone for the run.
            _wipe_all_copies(state, decker, utility_name)
        else:
            # A normal tar crash: a One-Shot copy is wiped from the deck (vr2_rules.md L1667);
            # a reloadable program can be restored from storage via Swap Memory. No-op otherwise.
            _wipe_one_shot(state, decker, utility_name)
    else:
        # The tar failed to catch the utility -- its ambush is blown, so it is now REVEALED to the
        # decker (surfaced by _serialize_run as a targetable lurking icon). The decker can Steamroller
        # it before it gets another free shot at a program (vr2 + user ruling 2026-07-17).
        lurking["revealed"] = True
        _append_event(state, {
            "type": "reactive_ic_resolved",
            "ic_id": lurking["id"],
            "ic_type": lurking["type"],
            "outcome": "util_wins",
            "ic_roll": result["ic_roll"],
            "util_roll": result["util_roll"],
            "description": (
                f"{lurking['type']}-{lurking['rating']} triggered when "
                f"{utility_name}-{utility_rating} executed, but was ineffective!"
            ),
        })


@router.post("/{run_id}/resolve-reactive", response_model=MatrixRunRead,
             dependencies=[Depends(get_admin_token), Depends(trace_action)])
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
    """One Hog drain pass against the PC (kept as a thin wrapper over the shared
    _HogTarget seam so any remaining PC-only caller behaves identically)."""
    name, applied, crashed = _hog_target_for_pc(state, decker).drain(drain)
    if not name:
        return ""
    return f"{name.replace('_', ' ').title()} -{applied}{' (CRASHED)' if crashed else ''}"


# -- Hog (viral offensive) -- modelled ONCE for both directions ---------------
# Hog is decker-vs-decker: whoever fires it, a hit seeds a persistent infection that
# re-drains the target's highest running program every Combat Turn until it is purged or
# the program crashes. The PC and an enemy decker store their programs differently (the PC
# over an immutable utilities map + a program_damage ledger; an enemy in a mutable in-state
# utilities dict), so a small adapter lets one resolver drain either side identically.
class _HogTarget:
    """Adapter exposing the two things Hog needs of a target -- its MPCP/Hardening (to
    resist) and 'drain its highest running program' -- regardless of which deck shape it is."""
    __slots__ = ("id", "name", "kind", "mpcp", "hardening", "_deck", "_state")

    def __init__(self, *, target_id: str, name: str, kind: str, mpcp, hardening,
                 deck: dict, state: dict):
        self.id = target_id
        self.name = name
        self.kind = kind                       # "pc" | "enemy"
        self.mpcp = max(1, int(mpcp or 1))
        self.hardening = max(0, int(hardening or 0))
        self._deck = deck
        self._state = state

    def _running_pairs(self) -> list[tuple[str, int]]:
        utils = self._deck.get("utilities") or {}
        if self.kind == "pc":
            pd = self._state.setdefault("program_damage", {})
            return [(k, int(r or 0) - pd.get(k, 0)) for k, r in utils.items()]
        return [(k, int(v or 0)) for k, v in utils.items()]

    def has_running(self) -> bool:
        return any(eff > 0 for _, eff in self._running_pairs())

    def drain(self, reduction: int) -> tuple[str | None, int, bool]:
        """Reduce the highest running program by ``reduction``. Returns
        (program_name, amount_applied, crashed) or (None, 0, False) if nothing ran."""
        if reduction <= 0:
            return None, 0, False
        running = [(k, eff) for k, eff in self._running_pairs() if eff > 0]
        if not running:
            return None, 0, False
        name, eff = max(running, key=lambda kv: kv[1])
        applied = min(reduction, eff)
        utils = self._deck.get("utilities") or {}
        if self.kind == "pc":
            pd = self._state.setdefault("program_damage", {})
            pd[name] = pd.get(name, 0) + applied
            crashed = pd[name] >= int(utils.get(name, 0) or 0)
        else:
            orig = int(utils.get(name, 0) or 0)
            # Remember the pre-drain rating so the enemy can reload the program later (Purge Hog +
            # Swap Memory). setdefault keeps the FIRST (highest) value seen == the true base rating.
            self._deck.setdefault("base_utilities", {}).setdefault(name, orig)
            new_val = max(0, orig - applied)
            utils[name] = new_val
            crashed = new_val <= 0
        return name, applied, crashed


def _hog_target_for_pc(state: dict, decker: dict) -> _HogTarget:
    return _HogTarget(target_id="pc", name=decker.get("name", "Your icon"), kind="pc",
                      mpcp=decker.get("mpcp", 4), hardening=decker.get("hardening", 0),
                      deck=decker, state=state)


def _hog_target_for_enemy(state: dict, enemy: dict) -> _HogTarget:
    return _HogTarget(target_id=enemy.get("id", ""), name=enemy.get("name", "decker"),
                      kind="enemy", mpcp=enemy.get("mpcp", 4),
                      hardening=enemy.get("hardening", 0), deck=enemy, state=state)


def _hog_target_by_id(state: dict, decker: dict, target_id: str) -> _HogTarget | None:
    """Resolve an infection's stored target id back to a live target. 'pc' (or a legacy
    infection with no target_id) is always the PC; otherwise an active enemy decker, or
    None if that enemy has crashed / logged off (the infection then lapses)."""
    if target_id == "pc" or not target_id:
        return _hog_target_for_pc(state, decker)
    for e in state.get("enemy_deckers", []):
        if e.get("id") == target_id and e.get("status") == "active":
            return _hog_target_for_enemy(state, e)
    return None


def _resolve_hog(state: dict, target: _HogTarget, *, attacker_id: str, attacker_pool: int,
                 hog_rating: int, sec_code: str, target_status: str = "intruding",
                 tn_modifier: int = 0) -> dict:
    """Resolve a single Hog strike (either direction). On a hit that beats the target's
    MPCP resist, seed a persistent infection (drained each Combat Turn by
    _drain_all_hog_infections) AND apply the first drain immediately. Returns
    {attack_roll, reduction, infected, drained, applied, crashed}."""
    hog = eng.hog_attack(attacker_pool=attacker_pool, security_code=sec_code,
                         target_status=target_status, hog_rating=hog_rating,
                         mpcp_rating=target.mpcp, hardening=target.hardening,
                         tn_modifier=tn_modifier)
    reduction = hog["reduction"]
    out = {"attack_roll": hog["attack_roll"], "reduction": reduction,
           "infected": False, "drained": None, "applied": 0, "crashed": False}
    if hog["attack_roll"]["successes"] > 0 and reduction > 0:
        state.setdefault("hog_infections", []).append({
            "id": f"hog_{uuid.uuid4().hex[:8]}", "attacker_id": attacker_id,
            "target_id": target.id, "rating": hog_rating, "drain": reduction})
        name, applied, crashed = target.drain(reduction)
        out.update(infected=True, drained=name, applied=applied, crashed=crashed)
    return out


def _drain_all_hog_infections(state: dict, decker: dict) -> None:
    """Each Combat Turn every active Hog infection re-drains its target's highest running
    program (vr2). One loop covers both directions -- an enemy's virus on the PC and the
    PC's virus on an enemy -- and drops any infection whose target is gone."""
    infections = state.get("hog_infections") or []
    if not infections:
        return
    survivors: list[dict] = []
    for inf in infections:
        target = _hog_target_by_id(state, decker, inf.get("target_id", "pc"))
        if target is None:
            continue   # target crashed / logged off -> infection lapses
        name, applied, crashed = target.drain(inf.get("drain", 0))
        if name:
            frag = f"{name.replace('_', ' ').title()} -{applied}{' (CRASHED)' if crashed else ''}"
            if target.id == "pc":
                _append_event(state, {
                    "type": "enemy_decker", "outcome": "hog",
                    "description": f"Hog-{inf.get('rating')} virus drains your deck: {frag}.",
                })
            else:
                _append_event(state, {
                    "type": "enemy_decker", "outcome": "hog", "enemy_id": target.id,
                    "gm_only": True,
                    "description": f"GM: your Hog virus drains {target.name}'s program: {frag}.",
                })
        survivors.append(inf)
    state["hog_infections"] = survivors


def _enemy_hog_infection(state: dict, enemy: dict) -> dict | None:
    """Return the first active Hog virus the PC has planted on THIS enemy (an infection whose
    target is the enemy's id), or None."""
    eid = enemy.get("id")
    for inf in state.get("hog_infections") or []:
        if inf.get("target_id") == eid:
            return inf
    return None


def _enemy_hog_lost_points(enemy: dict) -> int:
    """Total program-rating points this enemy has lost to Hog drain (base minus current)."""
    utils = enemy.get("utilities") or {}
    return sum(max(0, orig - int(utils.get(name, 0) or 0))
               for name, orig in (enemy.get("base_utilities") or {}).items())


def _enemy_purge_hog(state: dict, enemy: dict) -> bool:
    """Enemy self-defence (spec #1): a security decker the PC has infected with Hog spends a
    Complex action to Purge the virus off its own deck (mirrors the PC's purge_hog). A success
    wipes the virus and arms a Swap-Memory reload next action; a failure leaves it draining. Only
    bothers once the drain is meaningful (>= 2 rating points lost). Returns True if it acted."""
    inf = _enemy_hog_infection(state, enemy)
    if inf is None or _enemy_hog_lost_points(enemy) < 2:
        return False
    bu = enemy.get("base_utilities") or {}
    # TN uses the ORIGINAL rating of the worst-hit program (vr2 purge TN = Hog - Hardening + prog).
    infected_rating = max((v for v in bu.values()), default=0)
    purge = eng.hog_purge_test(
        computer_skill=enemy.get("computer_skill", 4), hog_rating=inf.get("rating", 4),
        infected_program_rating=infected_rating, hardening=enemy.get("hardening", 0))
    if purge["purged"]:
        state["hog_infections"] = [i for i in (state.get("hog_infections") or []) if i is not inf]
        enemy["hog_reload_pending"] = True
        _append_event(state, {
            "type": "enemy_decker", "outcome": "purge_hog", "enemy_id": enemy.get("id"),
            "description": (
                f"{_enemy_display_name(enemy)} purges your Hog-{inf.get('rating')} virus "
                "off its deck -- it will reload the crashed program from storage next."
            ),
        })
    else:
        _append_event(state, {
            "type": "enemy_decker", "outcome": "purge_hog", "enemy_id": enemy.get("id"),
            "gm_only": True,
            "description": (
                f"GM: {_enemy_gm_name(enemy)} tries to purge your Hog-"
                f"{inf.get('rating')} (TN {purge['tn']}) but fails -- the virus keeps draining it."
            ),
        })
    return True


def _enemy_swap_reload(state: dict, enemy: dict) -> bool:
    """Enemy Swap Memory (Simple): after purging a Hog, reload the drained programs from storage,
    restoring each to its recorded base rating. Returns True if anything was restored."""
    if not enemy.get("hog_reload_pending"):
        return False
    utils = enemy.setdefault("utilities", {})
    bu = enemy.get("base_utilities") or {}
    restored = [name for name, orig in bu.items() if int(utils.get(name, 0) or 0) < int(orig or 0)]
    for name in restored:
        utils[name] = int(bu[name] or 0)
    enemy["base_utilities"] = {}
    enemy["hog_reload_pending"] = False
    if restored:
        pretty = ", ".join(n.replace("_", " ").title() for n in restored)
        _append_event(state, {
            "type": "enemy_decker", "outcome": "swap_memory", "enemy_id": enemy.get("id"),
            "description": (
                f"{_enemy_display_name(enemy)} reloads {pretty} from storage (Swap Memory)"
                " -- its programs are back to full strength."
            ),
        })
        return True
    return False


def _enemy_scan_pc(state: dict, enemy: dict, eff: dict) -> bool:
    """The 'vice versa' Analyze-Icon read. After locating the PC, a crippler-carrying security
    decker spends a separate action to study the icon, latch its read (``scanned_pc``), and peg the
    PC's weakest crippler-targetable attribute so it can FOCUS that soft spot (see
    ``_enemy_focus_program``). Emits a player-visible warning and returns True when it actually
    scanned. Blue/Green deckers carry no cripplers, so they have nothing to scan for, stay silent,
    and return False -- keeping their behaviour (and existing tests) unchanged."""
    if enemy.get("scanned_pc"):
        return False
    util = enemy.get("utilities") or {}
    targetable = [(attr, int(eff.get(attr, 99) or 99)) for attr in ("bod", "evasion", "masking")
                  if int(util.get(_ATTR_CRIPPLER[attr].lower(), 0) or 0) > 0]
    if not targetable:
        return False
    enemy["scanned_pc"] = True
    weakest = min(targetable, key=lambda kv: kv[1])[0]
    enemy["pc_weakest_attr"] = weakest
    _append_event(state, {
        "type": "enemy_decker", "outcome": "scanned", "enemy_id": enemy["id"],
        "description": (
            f"{_enemy_display_name(enemy)} runs an Analyze on your icon -- it now has your {weakest.title()} "
            "pegged as the soft spot and moves to exploit it."
        ),
    })
    return True


def _enemy_focus_program(enemy: dict, eff: dict) -> str:
    """Smart-decker option (spec: enemy deckers are 'smarter than average IC'): once it has scanned
    the PC, the enemy OPENS with the crippler that hits the PC's weakest attribute -- softening it
    toward the crash -- exactly ONCE, then reverts to raw Attack/lethal so crashing the icon stays
    the priority. Returns 'Poison'/'Restrict'/'Reveal' for that opening move, else 'Attack'."""
    if not enemy.get("scanned_pc") or enemy.get("focus_used"):
        return "Attack"
    attr = enemy.get("pc_weakest_attr")
    prog = _ATTR_CRIPPLER.get(attr or "")
    util = enemy.get("utilities") or {}
    if not prog or int(util.get(prog.lower(), 0) or 0) <= 0:
        return "Attack"
    if int(eff.get(attr, 99) or 99) <= 1:
        return "Attack"   # already floored -- crippling it further is wasted; just hit it
    return prog


def _enemy_decker_take_turn(state: dict, decker: dict, run, enemy: dict) -> str:
    """One enemy-decker action against the PC. Mutates ``state`` (and ``run.status`` on a
    kill/dump). Phase 1 = locate the PC; once located, Phase 2 = execute its program.

    Driven automatically by the app-as-GM loop (perform_action / new_turn): the app plays the
    opponent -- spawned enemy deckers hunt and act on their own. Does NOT commit -- the caller
    persists state.

    Returns the vr2 action cost of what it did so ``_enemy_decker_take_pass`` can spend the
    enemy's 2-action-point pass budget across multiple actions: ``"simple"`` (1 AP -- a cybercombat
    attack / crippler / Hog / maneuver), ``"complex"`` (2 AP -- Locate the PC, or self-Restore), or
    ``"end"`` (a pass-ending action: flee / hide / heal-while-hidden / icon crash / nothing to do).
    """
    if enemy.get("status") != "active" or state.get("run_ended"):
        return "end"
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
                        f"GM: {_enemy_gm_name(enemy)} has patched its icon to "
                        f"{boxes}/10 and drops its hide to resume the hunt."
                    ),
                })
                return "end"
            _enemy_medic_heal(state, enemy)
        return "end"
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
            sensor_rating=_enemy_effective_attr(enemy, "sensor"),
            pc_detection_factor=_effective_detection_factor(state, decker),
            pc_evasion=eff["evasion"],
        )
        if first_contact:
            _append_event(state, {
                "type": "enemy_decker", "outcome": "hunting", "enemy_id": enemy["id"],
                "description": (
                    f"ALERT -- a hostile decker ({_enemy_display_name(enemy)}) is hunting your icon. "
                    "Evade (Relocate/Redirect), log off, or strike first."
                ),
            })
        if loc["located"]:
            enemy["located"] = True
            _append_event(state, {
                "type": "enemy_decker", "outcome": "located", "enemy_id": enemy["id"],
                "description": f"{_enemy_display_name(enemy)} has pinpointed your icon's position.",
            })
        else:
            _append_event(state, {
                "type": "enemy_decker", "outcome": "probing", "enemy_id": enemy["id"],
                "gm_only": True,
                "description": (
                    f"{_enemy_display_name(enemy)} keeps searching but has not pinpointed your icon this pass."
                ),
            })
        return "complex"

    # -- Phase 1b: Analyze the located icon (crippler-carriers only) --------------
    # A separate Analyze-Icon read (mirrors the PC's analyze_icon): now that the icon is located, a
    # crippler-carrier spends one action to study it and peg the PC's weakest attribute BEFORE it
    # starts exploiting the soft spot. Non-crippler deckers skip this and go straight to Phase 2.
    if not enemy.get("scanned_pc") and _enemy_scan_pc(state, enemy, eff):
        return "simple"

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
                f"{_enemy_display_name(enemy)}'s icon is crashing ({boxes}/10) -- it is dumped from the host."
            ),
        })
        return "end"
    # Escalating nerve check at 7/8/9 boxes (once per newly-reached threshold; bravery softens it).
    if _enemy_nerve_check(state, enemy, boxes):
        return "end"   # nerve broke -> jacked out (the helper set status="fled" + logged it)
    # Held its nerve but hurt: a Medic-carrier (Red/Black) tactically breaks contact to heal --
    # Evade Detection now, then heal while hidden (top-of-function loop) and re-engage once patched.
    if boxes >= _ENEMY_WOUNDED_BOXES and _enemy_carries_medic(enemy):
        _resolve_npc_maneuver(state, decker, eff, enemy, "evade_detection", is_ic=False)
        return "end"
    # Self-repair: a Restore-carrier (Red/Black) with meaningful temporary attribute cripple damage
    # (>= 2 repairable points) spends its action to Restore -- the SAME defensive utility the PC
    # runs, via the shared _restore_repair_core -- before choosing an offensive program. Restore
    # patches the icon in place (no need to break contact like the Medic hide-heal loop).
    if (_enemy_carries_restore(enemy) and _enemy_effective_restore(enemy) > 0
            and _enemy_repairable_damage(enemy) >= 2):
        _enemy_restore_repair(state, enemy)
        return "complex"
    # Hog self-defence (spec #1): reload first if a purge already armed a Swap-Memory (finish
    # getting its programs back), otherwise purge an active Hog virus off its own deck. This keeps
    # a PC's Hog from being a permanent disable -- the enemy recovers just like the PC can.
    if enemy.get("hog_reload_pending") and _enemy_swap_reload(state, enemy):
        return "simple"
    if _enemy_purge_hog(state, enemy):
        return "complex"
    # Combat maneuver: the enemy may spend its action to maneuver against you instead of attacking
    # (heuristic; only when npc_combat_maneuvers is set).
    if _npc_maybe_maneuver(state, decker, eff, enemy, is_ic=False):
        if not state.get("run_ended"):
            state["detection_factor"] = _effective_detection_factor(state, decker)
        return "simple"
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
        # Smart opener: if it has scanned the PC, focus the weakest attribute with the matching
        # crippler ONCE (softening toward the crash), otherwise a plain Attack.
        program = _enemy_focus_program(enemy, eff)
        if program != "Attack":
            enemy["focus_used"] = True
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
        # One shared resolver seeds the persistent infection AND applies the first drain.
        res = _resolve_hog(
            state, _hog_target_for_pc(state, decker), attacker_id=enemy["id"],
            attacker_pool=pool, hog_rating=power, sec_code=sec_code,
            target_status=_pc_target_status(state), tn_modifier=_enemy_wound_mod(enemy))
        if res["infected"]:
            frag = (f"{res['drained'].replace('_', ' ').title()} -{res['applied']}"
                    f"{' (CRASHED)' if res['crashed'] else ''}") if res["drained"] else "no running program left"
            desc = (f"HOG -- {_enemy_display_name(enemy)}'s virus takes hold (drains {res['reduction']}/turn): "
                    f"{frag}. Purge it or reload via Swap Memory.")
        else:
            desc = f"HOG -- {_enemy_display_name(enemy)}'s virus fails to take hold this turn."
        _append_event(state, {
            "type": "enemy_decker", "outcome": "hog", "enemy_id": enemy["id"],
            "program": "Hog", "attack_roll": res["attack_roll"], "description": desc})

    elif program in ("Poison", "Restrict", "Reveal"):
        attr = _PROGRAM_ATTR[program.lower()]
        # Shield parry: fired ONLY if the crippler lands (net successes then ADD to the decker's
        # opposed defence, vr2). A resisted/whiffed crippler rolls no Shield and wears nothing.
        # Combat maneuver: Parry (raises the enemy's TN) / Position (held by the enemy) delta.
        atk_tn_delta, _atk_power_delta = _consume_attack_mods_vs_pc(state, enemy)
        # Enemy program rating is the Restore causing-rating (its Attack rating, per legacy behavior).
        cr = _resolve_attribute_attack(
            state, attacker_pool=pool, resist_tn=power, target_attr_rating=eff[attr],
            attr=attr, sec_code=sec_code, target_status=_pc_target_status(state), target_kind="pc",
            causing_rating=attack_rating,
            shield_parry=lambda: _shield_parry(state, decker, attacker_skill=enemy["computer_skill"], context=program),
            tn_modifier=atk_tn_delta + _enemy_wound_mod(enemy))
        if cr["reduction"] > 0:
            now = max(1, decker.get(attr, 4) - cm["persona_damage"][attr])
            desc = (f"{program.upper()} -- {_enemy_display_name(enemy)} cripples your {attr.title()} by "
                    f"{cr['reduction']} (now {now}, until logoff).")
        else:
            desc = f"{program.upper()} -- {_enemy_display_name(enemy)}'s crippler attack is resisted."
        _append_event(state, {
            "type": "enemy_decker", "outcome": program.lower(), "enemy_id": enemy["id"],
            "program": program, "attack_roll": cr["attack_roll"], "description": desc})

    else:  # Attack / Black Hammer / Killjoy -> icon damage (+ biofeedback for black programs)
        # Shield parry once: it blunts the icon hit and (for black programs) the biofeedback
        # that derives from the same parried strike -- but only when the strike actually lands.
        _pc_shield = lambda: _shield_parry(state, decker, attacker_skill=enemy["computer_skill"], context=program)
        # Combat maneuver: Parry (raises the enemy's TN) + Position (held by the enemy: -TN / +Power).
        atk_tn_delta, atk_power_delta = _consume_attack_mods_vs_pc(state, enemy)
        did_icon_damage = True
        if is_lethal:
            # Black Hammer / Killjoy (vr2: "function like black IC but from a decker") -> the shared
            # black resolver: ONE strike at a fixed Serious base drives the icon (Bod, Armor
            # protects) AND the operator's flesh (Body -> Physical for Black Hammer, Willpower ->
            # Stun for Killjoy, Armor does NOT protect). Hardening reduces both resist Powers.
            black = eng.black_attack(
                attacker_pool=pool, security_code=sec_code, target_status=_pc_target_status(state),
                base_damage_level=_LETHAL_BASE_LEVEL,
                power=power + atk_power_delta,
                hardening=decker.get("hardening", 0),
                icon_bod=eff["bod"],
                icon_armor=_effective_armor(decker, state),
                tn_modifier=atk_tn_delta + _enemy_wound_mod(enemy),
                shield_parry=_pc_shield,
                meat_pool=decker.get("willpower", 4) if program == "Killjoy" else decker.get("body", 4),
                meat_is_stun=(program == "Killjoy"),
            )
            attack_roll = black["attack_roll"]
            boxes = black["icon"]["boxes"]
            _add_cm_damage(cm, "persona_boxes", boxes)
            _wear_armor(state, state, decker, boxes)
            meat_boxes = black["meat"]["boxes"]
            if program == "Killjoy":
                # Killjoy (non-lethal black IC): meat damage is Physical STUN (overflows to physical).
                _add_stun(cm, meat_boxes)
                meat_kind, meat_val = "Stun", cm["stun_boxes"]
                meat_full = cm["stun_boxes"] >= 10
            else:
                # Black Hammer (lethal black IC): meat damage is Physical DAMAGE.
                _add_cm_damage(cm, "physical_boxes", meat_boxes)
                meat_kind, meat_val = "Physical", cm["physical_boxes"]
                meat_full = cm["physical_boxes"] >= 10
            desc = (f"{program.upper()} -- {_enemy_display_name(enemy)} drives lethal biofeedback into you: "
                    f"icon {black['icon']['final_damage_level']} ({boxes}), {meat_kind} "
                    f"{black['meat']['final_damage_level']} ({meat_boxes}). "
                    f"Persona {cm['persona_boxes']}/10, {meat_kind} {meat_val}/10.")
            if meat_full:
                state["run_ended"] = True
                state["end_reason"] = "killed_by_" + ("killjoy" if program == "Killjoy" else "black_hammer")
                _finalize_run_end(state)
                run.status = "killed"
        else:
            # Plain Attack -> standard icon damage (host Security Code base level, no biofeedback).
            atk = eng.cybercombat_attack(
                attacker_pool=pool, security_code=sec_code, target_status=_pc_target_status(state),
                target_bod=eff["bod"], armor_rating=_effective_armor(decker, state),
                ic_rating=power + atk_power_delta, attacker_is_ic=True,
                tn_modifier=atk_tn_delta + _enemy_wound_mod(enemy),
                shield_parry=_pc_shield)
            attack_roll = atk["attack_roll"]
            boxes = atk["resistance"]["boxes"]
            _add_cm_damage(cm, "persona_boxes", boxes)
            _wear_armor(state, state, decker, boxes)
            _atk_letter = rules.IC_DAMAGE_LEVEL.get(sec_code, "Moderate")[0]
            desc = (f"{_enemy_display_name(enemy)} hits your icon with {program}-{power}{_atk_letter} -- "
                    f"{atk['resistance']['final_damage_level']} ({boxes} boxes). "
                    f"Persona {cm['persona_boxes']}/10.")
        _append_event(state, {
            "type": "enemy_decker", "outcome": "kill" if is_lethal else "dump",
            "enemy_id": enemy["id"], "program": program,
            "attack_roll": attack_roll, "description": desc})

    # Icon crash -> dump shock (+ lethal MPCP burn) -- only when the program hit the icon.
    if did_icon_damage and not state.get("run_ended") and cm.get("persona_boxes", 0) >= 10:
        ds = _apply_dump_shock(state, decker, sec_code, sec_value)
        state["icon_crashed"] = True
        state["run_ended"] = True
        state["end_reason"] = "icon_crashed_by_decker"
        _finalize_run_end(state)
        run.status = "dumped"
        shock = "immune" if ds.get("immune") else f"{ds['boxes']} stun boxes"
        mpcp_note = ""
        if is_lethal:
            mpcp_hit, _b = _roll_mpcp_damage(state, decker, power, pool_multiplier=2)
            if mpcp_hit > 0:
                mpcp_note = f" {program} fried the MPCP on the way out: -{mpcp_hit} (permanent)."
        _append_event(state, {
            "type": "persona_crash", "enemy_id": enemy["id"],
            "description": f"PERSONA CRASHED by {_enemy_display_name(enemy)} -- dumped (dump shock: {shock}).{mpcp_note}",
        })

    if not state.get("run_ended"):
        # Reveal (masking) cripples flow into the Detection Factor -- keep it in sync for the UI.
        state["detection_factor"] = _effective_detection_factor(state, decker)
    return "simple"


def _enemy_decker_take_pass(state: dict, decker: dict, run, enemy: dict) -> None:
    """Run one enemy decker's full initiative pass under the vr2 action-point economy -- the SAME
    budget the PC gets (2 action points + 1 Free action), applied to the app-as-GM enemy AI.

    The PC can take two Simple actions (or one Complex) per pass; enemy deckers previously acted
    only ONCE per pass. This spends the enemy's 2 action points by calling the single-action
    decision (:func:`_enemy_decker_take_turn`) up to twice: a cybercombat attack / crippler / Hog /
    maneuver is a Simple action (1 AP), so a located, healthy enemy now strikes up to TWICE per
    pass; Locate and self-Restore are Complex (2 AP -> one per pass, unchanged); flee / hide /
    heal-while-hidden / icon crash end the pass immediately. The spare Free action is not modelled
    for enemies -- the enemy AI carries no Free-action program (no DINAB), so it has nothing to
    spend one on. Stops early if the enemy leaves play (fled / hidden) or the run ends.
    """
    for _ in range(2):          # 2 action points -> at most two Simple actions this pass
        if enemy.get("status") != "active" or state.get("run_ended"):
            return
        if _enemy_decker_take_turn(state, decker, run, enemy) != "simple":
            return              # Complex spent both points, or a pass-ending action -> done


@router.post("/{run_id}/enemy-decker/attack", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
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
    _assert_not_dinab_locked(state, body.program)  # DINAB per-pass lock: can't hand-fire what DINAB ran
    _record_manual_program(state, body.program)

    sec_code = state["host_security_code"]
    _spend_hp(state, body.hacking_pool_dice)
    pool = body.attack_pool + body.hacking_pool_dice
    util = decker.get("utilities") or {}
    computer_skill = int(decker.get("computer_skill", 1) or 1)   # PC skill: enemy Shield TN + lethal-program cap
    # Combat maneuver: the enemy's Parry (raises the PC's to-hit TN) + the PC's own Position
    # (lowers the TN and/or raises Power). Consumed by this single attack (exactly one of the
    # branches below runs, so it is read once here).
    tgt_tn_delta, tgt_power_delta = _consume_attack_mods_vs_target(state, enemy)

    # Hog -- the PC's offensive virus vs an enemy decker (vr2: the SAME persistent infection
    # an enemy decker can plant on you, modelled once for both directions). One shared resolver
    # seeds the infection on the enemy and applies the first drain; _drain_all_hog_infections
    # then bleeds the enemy's highest running program every Combat Turn until it purges or
    # crashes. The specific enemy program drained is GM detail (surfaced gm-only in that loop),
    # so the strike feedback reports only that it took hold and the per-turn drain rate.
    if body.program == "hog":
        hog_rating = int(util.get("hog", 0) or 0) or body.attack_pool
        res = _resolve_hog(
            state, _hog_target_for_enemy(state, enemy), attacker_id="pc",
            attacker_pool=pool, hog_rating=hog_rating, sec_code=sec_code,
            target_status=_combat_target_status(enemy), tn_modifier=tgt_tn_delta + _decker_wound_mod(state))
        if res["infected"]:
            desc = (f"HOG -- your virus takes hold on {_enemy_display_name(enemy)}: it will drain "
                    f"{res['reduction']} off its highest running program each Combat Turn "
                    f"until it purges or crashes.")
        else:
            desc = f"HOG -- your virus fails to take hold on {_enemy_display_name(enemy)} this pass."
        _append_event(state, {
            "type": "decker_hog", "outcome": "hog", "success": res["infected"],
            "enemy_id": enemy["id"], "program": "hog", "attack_roll": res["attack_roll"],
            "description": desc,
        })
        _spend_one_shot(state, decker, body.program)
        run.state_json = state
        await db.commit(); await db.refresh(run)
        return _serialize_run(run, auth)

    # Poison / Restrict / Reveal -- the PC's offensive crippler programs vs an enemy decker
    # (vr2: the decker versions of the Acid / Binder / Marker IC). Attack to hit, then the
    # target resists with the targeted attribute (dice) vs the program rating; the attacker's
    # net successes // 2 reduce that attribute, floored at 1. Poison->Bod, Restrict->Evasion,
    # Reveal->Masking. These target enemy DECKERS/frames only -- never routed through IC.
    if body.program in _PROGRAM_ATTR:
        attr = _PROGRAM_ATTR[body.program]
        # Program rating = the carried Poison/Restrict/Reveal utility (the resist TN); fall back
        # to the thrown pool if the player supplied one but no rating is recorded.
        program_rating = int(util.get(body.program, 0) or 0) or body.attack_pool
        target_rating = _enemy_effective_attr(enemy, attr)
        # The enemy parries with its Shield utility (if loaded), but ONLY when the crippler lands:
        # its net successes ADD to the enemy's side of the opposed test, raising the bar the PC must
        # clear. A resisted/whiffed crippler rolls no Shield and wears nothing.
        cr = _resolve_attribute_attack(
            state, attacker_pool=pool, resist_tn=program_rating,
            target_attr_rating=target_rating, attr=attr, sec_code=sec_code,
            target_status=_combat_target_status(enemy), target_kind="enemy", enemy=enemy,
            shield_parry=lambda: _enemy_shield_parry(state, enemy, attacker_skill=computer_skill, context=body.program),
            causing_rating=program_rating,
            tn_modifier=tgt_tn_delta + _decker_wound_mod(state))
        reduction = cr["reduction"]
        applied = cr["applied"]
        new_val = cr["new_value"]
        label = body.program.upper()
        if reduction > 0:
            floor_note = ", floored at 1" if new_val <= 1 else ""
            desc = (f"{label} -- you cripple {_enemy_display_name(enemy)}'s {attr.title()} by {applied} "
                    f"(now {new_val}{floor_note}).")
        else:
            desc = f"{label} -- {_enemy_display_name(enemy)} resists your crippler; {attr.title()} holds."
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
        cap = (computer_skill + 1) // 2                 # ceil(Computer / 2) = RAW max rating
        carried = int(util.get(program, 0) or 0) or body.attack_pool
        rating = max(1, min(carried, cap))              # clamp to the RAW rating cap
        clamped = carried > cap
        target_bod = _enemy_effective_attr(enemy, "bod")
        # The enemy parries the lethal hit with its Shield utility (if loaded), but ONLY when the
        # strike lands: its net successes SUBTRACT from the PC's attack successes before the
        # icon-damage resistance stages. A clean miss rolls no Shield and wears nothing.
        # Shared black resolver: host-code to-hit (target intruding), fixed Serious base. The enemy
        # resists the ICON hit with Bod -- its Armor reduces Power, its Hardening reduces it further.
        # The enemy's MEAT is now simulated too (like the PC target) so the strike can KO/kill the
        # operator, not just crash the icon: Black Hammer -> lethal Physical (resisted with Body),
        # Killjoy -> Stun (resisted with Willpower); Armor never protects the flesh.
        black = eng.black_attack(
            attacker_pool=pool, security_code=sec_code,
            target_status=_combat_target_status(enemy),
            base_damage_level=_LETHAL_BASE_LEVEL,
            power=rating + tgt_power_delta,
            hardening=int(enemy.get("hardening", 0) or 0),
            icon_bod=target_bod,
            icon_armor=_enemy_armor(enemy),
            tn_modifier=tgt_tn_delta + _decker_wound_mod(state),
            shield_parry=lambda: _enemy_shield_parry(state, enemy, attacker_skill=computer_skill, context=program),
            meat_pool=(int(enemy.get("willpower") or enemy.get("intelligence") or 4)
                       if program == "killjoy"
                       else int(enemy.get("body") or enemy.get("bod") or 4)),
            meat_is_stun=(program == "killjoy"),
        )
        attack_roll = black["attack_roll"]
        boxes = black["icon"]["boxes"]
        ecm = enemy.setdefault("condition_monitor", {})
        _add_cm_damage(ecm, "persona_boxes", boxes)
        _wear_armor(state, enemy, enemy, boxes, gm_only=True, actor=enemy.get("name") or "Security decker")
        # Meat biofeedback: Black Hammer overflows Physical, Killjoy fills Stun (overflows Physical).
        meat_boxes = black["meat"]["boxes"]
        if program == "killjoy":
            _add_stun(ecm, meat_boxes)
            meat_kind, meat_val = "Stun", ecm.get("stun_boxes", 0)
            meat_full = ecm.get("stun_boxes", 0) >= 10
        else:
            _add_cm_damage(ecm, "physical_boxes", meat_boxes)
            meat_kind, meat_val = "Physical", ecm.get("physical_boxes", 0)
            meat_full = ecm.get("physical_boxes", 0) >= 10
        clamp_note = f" (rating clamped {carried}->{rating}, max = ceil(Computer/2))" if clamped else ""
        nice = "Killjoy" if program == "killjoy" else "Black Hammer"
        if boxes <= 0 and meat_boxes <= 0:
            hit_desc = f"The enemy resists your {nice} attack!"
        else:
            hit_desc = (
                f"{label} -- you drive lethal {dmg_kind} biofeedback into {_enemy_display_name(enemy)}: "
                f"icon {black['icon']['final_damage_level']} ({boxes} boxes), {meat_kind} "
                f"{black['meat']['final_damage_level']} ({meat_boxes}). "
                f"Enemy persona {ecm['persona_boxes']}/10, {meat_kind} {meat_val}/10.{clamp_note}"
            )
        _append_event(state, {
            "type": "decker_lethal", "outcome": "hit", "success": boxes > 0 or meat_boxes > 0,
            "enemy_id": enemy["id"], "program": program, "damage_kind": dmg_kind,
            "program_rating": rating, "boxes": boxes, "meat_boxes": meat_boxes,
            "decker_roll": attack_roll, "description": hit_desc,
        })
        # The hostile decker leaves the run if EITHER its icon crashes (dumped) OR its meat fills
        # (KO'd on Stun / killed on Physical). Report the human outcome and store it on the record.
        icon_crashed = ecm["persona_boxes"] >= 10
        if meat_full or icon_crashed:
            enemy["status"] = "crashed"
            if program != "killjoy" and ecm.get("physical_boxes", 0) >= 10:
                enemy["outcome"] = "killed"
                enemy["end_reason"] = "killed_by_black_hammer"
                fate = (f"{_enemy_display_name(enemy)} takes lethal physical biofeedback -- the decker flatlines. "
                        f"Dead and out of the run.")
            elif program == "killjoy" and ecm.get("stun_boxes", 0) >= 10:
                enemy["outcome"] = "knocked_out"
                enemy["end_reason"] = "ko_by_killjoy"
                fate = (f"{_enemy_display_name(enemy)} is overwhelmed by stun biofeedback -- knocked unconscious "
                        f"and out of the run.")
            else:
                enemy["outcome"] = "dumped"
                enemy["end_reason"] = "icon_crashed"
                fate = (f"{label} CRASHES {_enemy_display_name(enemy)}'s icon -- the hostile decker is dumped and "
                        f"taken out of the run.")
            # MPCP burn happens only when the ICON actually crashed (blaster at DOUBLE the rating).
            mpcp_hit, mpcp_roll = (0, None)
            mpcp_note = ""
            if icon_crashed:
                mpcp_hit, mpcp_roll = _roll_enemy_mpcp_damage(enemy, rating, pool_multiplier=2)
                mpcp_note = (f" The lethal feedback fries its MPCP: -{mpcp_hit} permanent."
                             if mpcp_hit > 0 else " Its MPCP weathered the feedback.")
            _append_event(state, {
                "type": "decker_lethal", "outcome": "crash", "success": True,
                "enemy_id": enemy["id"], "program": program, "damage_kind": dmg_kind,
                "program_rating": rating, "mpcp_reduction": mpcp_hit, "mpcp_roll": mpcp_roll,
                "enemy_outcome": enemy["outcome"],
                "description": fate + mpcp_note,
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
    # Shield utility (if loaded) parrying successes off the incoming hit -- but ONLY when the
    # strike lands. A clean miss rolls no Shield and wears nothing.
    atk = eng.cybercombat_attack(
        attacker_pool=pool, security_code=sec_code,
        target_status=_combat_target_status(enemy),
        target_bod=_enemy_effective_attr(enemy, "bod"), armor_rating=_enemy_armor(enemy),
        ic_rating=util.get("attack", 4) + tgt_power_delta, attacker_is_ic=False,
        tn_modifier=tgt_tn_delta + _decker_wound_mod(state),
        shield_parry=lambda: _enemy_shield_parry(state, enemy, attacker_skill=computer_skill, context="attack"),
        base_damage_level=_attack_damage_level(decker, sec_code),
    )
    boxes = atk["resistance"]["boxes"]
    ecm = enemy.setdefault("condition_monitor", {})
    _add_cm_damage(ecm, "persona_boxes", boxes)
    _wear_armor(state, enemy, enemy, boxes, gm_only=True, actor=enemy.get("name") or "Security decker")
    if boxes <= 0:
        desc = f"You strike {_enemy_display_name(enemy)} -- Target resisted all damage."
    else:
        desc = (f"You strike {_enemy_display_name(enemy)} -- {atk['resistance']['final_damage_level']} "
                f"({boxes} boxes). Enemy persona {ecm['persona_boxes']}/10.")
    if ecm["persona_boxes"] >= 10:
        enemy["status"] = "crashed"
        enemy["outcome"] = "dumped"
        enemy["end_reason"] = "icon_crashed"
        desc += f" {_enemy_display_name(enemy)}'s icon CRASHED -- dumped from the host (the decker survives)."
    _append_event(state, {
        "type": "decker_attack", "success": True, "enemy_id": enemy["id"],
        "decker_roll": atk["attack_roll"], "description": desc,
    })
    _spend_one_shot(state, decker, body.program)
    run.state_json = state
    await db.commit(); await db.refresh(run)
    return _serialize_run(run, auth)


@router.post("/{run_id}/enemy-decker/scan", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
async def scan_enemy_decker(
    run_id: int,
    body: RunEnemyScanInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Scan Icon vs a revealed enemy decker (vr2 L1895).

    A Computer Test vs the target's Masking Rating, adjusted by the target's Sleaze minus the PC's
    Scanner utility (only when the target runs Sleaze): the scanner out-rating the sleaze lowers the
    TN, the reverse raises it. Each net success discloses one of the enemy's otherwise-hidden
    ratings in ``_SCAN_REVEAL_ORDER`` (MPCP -> the four Persona ratings -> Response Increase); a
    decisive 3+ success scan lays the whole icon bare. Decker-only target -- it doubles as the
    Analyze-Icon read for a hostile decker. A Simple action that spends one action point but adds no
    security tally (a passive read of another icon, not a host operation)."""
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
        raise HTTPException(404, "No such revealed enemy decker to scan")
    _spend_pass_action(state, "scan_icon")     # vr2: Scan Icon is a Simple Action
    _spend_hp(state, body.hacking_pool_dice)

    util = decker.get("utilities") or {}
    scanner = int(util.get("scanner", 0) or 0)
    target_masking = int(enemy.get("masking", 1) or 1)
    target_sleaze = int((enemy.get("utilities") or {}).get("sleaze", 0) or 0)
    # TN = target Masking, adjusted by the target's Sleaze vs the PC's Scanner (only if the target
    # runs Sleaze); the PC's own wound penalty raises it. Floored at 2.
    tn = target_masking + (target_sleaze - scanner if target_sleaze > 0 else 0)
    tn = max(2, tn + _decker_wound_mod(state))
    pool = int(decker.get("computer_skill", 1) or 1) + body.hacking_pool_dice
    roll = eng.roll_dice(pool, tn)
    successes = roll["successes"]

    prev = int(enemy.get("scan_reveal", 0) or 0)
    all_n = len(_SCAN_REVEAL_ORDER)
    new_level = all_n if successes >= 3 else min(all_n, prev + successes)
    enemy["scan_reveal"] = max(prev, new_level)

    # Any successful scan (net success) IDs the icon -> reveal its street handle from now on.
    newly_named = not _enemy_name_revealed(enemy) and enemy["scan_reveal"] > 0
    if enemy["scan_reveal"] > 0:
        enemy["name_revealed"] = True
    disp = _enemy_display_name(enemy)

    if enemy["scan_reveal"] > prev:
        labels = {"mpcp": "MPCP", "bod": "Bod", "evasion": "Evasion", "masking": "Masking",
                  "sensor": "Sensor", "response_increase": "Response Increase"}
        newly = _SCAN_REVEAL_ORDER[prev:enemy["scan_reveal"]]
        parts = ", ".join(f"{labels[k]} {int(enemy.get(k, 0) or 0)}" for k in newly)
        full = " -- icon fully scanned" if enemy["scan_reveal"] >= all_n else ""
        idtag = " -- icon identified" if newly_named else ""
        desc = f"Scan Icon on {disp}: {parts}{full}{idtag}."
    else:
        detail = "no successes" if successes == 0 else "already fully read"
        desc = f"Scan Icon on {disp} reveals nothing new ({detail})."
    _append_event(state, {
        "type": "icon_scanned", "success": enemy["scan_reveal"] > prev,
        "enemy_id": enemy["id"], "decker_roll": roll,
        "scan_level": enemy["scan_reveal"], "description": desc,
    })
    run.state_json = state
    await db.commit(); await db.refresh(run)
    return _serialize_run(run, auth)


@router.post("/{run_id}/area-attack", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
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
    _assert_not_dinab_locked(state, "attack")  # DINAB per-pass lock: can't hand-fire an Attack DINAB ran
    _record_manual_program(state, "attack")
    _spend_hp(state, body.hacking_pool_dice)
    attack_pool = body.attack_pool + body.hacking_pool_dice
    # vr2 L2028: hit the TARGET's status column. Area targets are IC and/or enemy deckers -- all
    # Legitimate host residents -- so the burst uses the Legitimate column for every target.
    base_tn = rules.COMBAT_TN[sec_code][_combat_target_status()]
    wound_mod = _decker_wound_mod(state)
    # The Attack utility carries its OWN base Damage Level (Attack-6L/-6M/-6S/-6D), not the host
    # IC Damage Table; every target in the burst resists against that single program severity.
    base_dmg = _attack_damage_level(decker, sec_code)
    attack_util_rating = int((decker.get("utilities") or {}).get("attack", 4) or 4)
    computer_skill = int(decker.get("computer_skill", 1) or 1)   # PC skill: enemy Shield parry TN

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
            # IC resists through the SHARED eng.damage_resistance seam (the SAME resistance stage
            # eng.cybercombat_attack uses internally, so the burst cannot drift from a hand attack):
            # Security Value +/- Expert dice vs the attack Power, Armor reducing that Power (+2 more
            # effective vs an Area burst). Identical model to the single-target /attack and DINAB.
            ic_resist_pool = max(1, sec_value + _ic_expert(obj, "defense") - _ic_expert(obj, "offense"))
            ic_armor = (2 + (2 if is_burst else 0)) if _ic_has_armor(obj) else 0
            resist = eng.damage_resistance(
                bod=ic_resist_pool, power=attack_util_rating + p["cluster"] + p["power_delta"],
                armor_rating=ic_armor, base_damage_level=base_dmg,
                attacker_successes=succ,
            )
            final_dmg = resist["final_damage_level"]
            boxes = resist["boxes"]
            obj["boxes"] = obj.get("boxes", 0) + boxes
            crashed = obj["boxes"] >= 10
            results.append({"kind": "ic", "id": obj["id"],
                            "label": f"{obj['type']}-{obj['rating']}",
                            "boxes": boxes, "final": final_dmg,
                            "total": obj["boxes"], "crashed": crashed})
            if crashed:
                _apply_ic_crash(state, obj, sec_code, opt_skulk)
        else:
            # Enemy decker resists EXACTLY like the PC, through the SAME seam: its Shield utility (if
            # loaded) parries successes off the incoming hit, and its Armor reduces the attack Power
            # (+2 more vs an Area burst) before the Bod Resistance Test. Shield only fires on a
            # landing hit -- a 0-success burst against this target rolls no Shield and wears nothing.
            e_shield = _enemy_shield_parry(state, obj, attacker_skill=computer_skill, context="area") if succ > 0 else 0
            earmor = _enemy_armor(obj)
            if earmor > 0 and is_burst:
                earmor += 2
            resist = eng.damage_resistance(
                bod=obj["bod"], power=attack_util_rating + p["power_delta"],
                armor_rating=earmor, base_damage_level=base_dmg,
                attacker_successes=succ, shield_successes=e_shield,
            )
            boxes = resist["boxes"]
            ecm = obj.setdefault("condition_monitor", {})
            _add_cm_damage(ecm, "persona_boxes", boxes)
            _wear_armor(state, obj, obj, boxes, gm_only=True, actor=obj.get("name") or "enemy decker")
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


@router.post("/{run_id}/suppress", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
async def suppress_ic(
    run_id: int,
    body: RunSuppressInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Suppress or release a crashed/hung IC OR a non-IC suppression entry (data bomb) (vr2
    Suppression + Slow L1578).

    Suppression is declared the MOMENT the source event happens -- a fresh crash (crashing added its
    rating to the tally), a Slow HANG (adds no tally), or a data bomb detonation (added its rating).
    The decker absorbs 1 Detection Factor (applied live by _effective_detection_factor) to refund
    that tally. Releasing restores the DF and re-adds a crashed IC's / bomb's rating to the tally (a
    hung IC re-adds nothing); a released item stays down and can NEVER be re-suppressed. Neither
    suppress nor release costs an action. The DF cannot fall below 1.
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


@router.post("/{run_id}/reveal-host-ratings", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
async def reveal_host_ratings(
    run_id: int,
    body: RunRevealHostRatingsInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Phase two of Analyze Host (vr2 override): spend banked Analyze Host credits by choosing which
    still-hidden items to reveal (the 5 ACIFS subsystem ratings and/or the host Security Rating).

    When a successful Analyze Host rolled fewer net successes than there were hidden items,
    ``_apply_analyze_host`` banks ``host_analyze_pending`` and reveals nothing. The decker then
    calls this endpoint with the chosen items (one per banked credit). ``_reveal_host_ratings``
    validates the picks, reveals them from the GM-only ratings, and clears the pending. A newly
    revealed Security Rating is mirrored onto the host's org LTG listing.
    """
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state = copy.deepcopy(run.state_json)
    sec_before = bool(state.get("host_security_revealed"))
    _reveal_host_ratings(state, body.subsystems)
    if state.get("host_security_revealed") and not sec_before:
        host = await _get_host_or_404(db, run.host_id)
        await sync_host_security_to_org(db, host, mark_revealed=True)

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


def _highest_engaged_black_ic(state: dict) -> dict | None:
    """Return the highest-rating active Black IC on the host, or None. Used to gate jack-out once
    the decker has taken a Black IC hit (vr2 L612)."""
    blacks = [
        ic for ic in state.get("active_ic", [])
        if ic.get("type") == "Black IC" and ic.get("status", "active") == "active"
    ]
    if not blacks:
        return None
    return max(blacks, key=lambda ic: int(ic.get("rating", 0) or 0))


def _black_ic_final_attack(state: dict, decker: dict, ic: dict) -> dict:
    """One final Black IC Attack as the decker tears free (vr2 L613).

    Mirrors the inline cybercombat Black IC resolution with neutral combat modifiers: resolves a
    single ``eng.black_attack``, applies persona + meat damage, and -- if that strike fills the
    physical or stun monitor -- fires the 2x-rating MPCP attack (Blaster mechanics). Returns the
    ``black_attack`` result. The caller (jack_out) ends the run regardless."""
    sec_code = state["host_security_code"]
    sec_value = state["host_security_value"]
    eff = _get_decker_effective(decker, state)
    is_non_lethal = decker.get("deck_mode") == "cool"
    armor = _effective_armor(decker, state)
    ic_attack_pool = ic["rating"] if ic["type"] == "Construct" else sec_value
    black = eng.black_attack(
        attacker_pool=ic_attack_pool,
        security_code=sec_code,
        target_status=_pc_target_status(state),
        base_damage_level=rules.IC_DAMAGE_LEVEL[sec_code],
        power=ic["rating"] + _deathworm_tn_bonus(state),
        hardening=decker.get("hardening", 0),
        icon_bod=eff["bod"],
        icon_armor=armor,
        tn_modifier=-_completed_trace_count(state),
        shield_parry=lambda: _shield_parry(state, decker, attacker_skill=sec_value, context="Black IC"),
        meat_pool=decker.get("willpower", 4) if is_non_lethal else decker.get("body", 4),
        meat_is_stun=is_non_lethal,
    )
    persona_boxes = black["icon"]["boxes"]
    meat_boxes = black["meat"]["boxes"]
    _add_cm_damage(state["condition_monitor"], "persona_boxes", persona_boxes)
    _wear_armor(state, state, decker, persona_boxes)
    if is_non_lethal:
        _add_stun(state["condition_monitor"], meat_boxes)
    else:
        _add_cm_damage(state["condition_monitor"], "physical_boxes", meat_boxes)
    _append_event(state, {
        "type": "ic_attack", "ic_id": ic["id"], "ic_type": "Black IC", "ic_rating": ic["rating"],
        "description": (
            f"Black IC {ic['rating']} lands one final attack as you jack out: "
            f"{black['attack_roll']['successes']} atk successes -- "
            f"{meat_boxes} {'stun' if is_non_lethal else 'phys'} / {persona_boxes} persona."
        ),
        "attack_roll": black["attack_roll"],
    })
    if state["condition_monitor"]["physical_boxes"] >= 10 or state["condition_monitor"]["stun_boxes"] >= 10:
        mpcp_hit, bl_roll = _roll_mpcp_damage(state, decker, ic["rating"], pool_multiplier=2)
        _append_event(state, {
            "type": "ic_attack", "ic_id": ic["id"], "ic_type": "Black IC",
            "description": f"Black IC MPCP attack at 2x rating: MPCP -{mpcp_hit} (permanent).",
            "mpcp_roll": bl_roll, "mpcp_damage": mpcp_hit,
        })
    return black


@router.post("/{run_id}/jack-out", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
async def jack_out(
    run_id: int,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Emergency jack-out.

    Before a Black IC hit this is an instant Free-Action disconnect (dump shock only). AFTER a
    Black IC has hit the decker (vr2 L612-614) it becomes a Complex Action requiring a
    Willpower (Black IC Rating) Test: on failure the decker stays jacked in (action spent); on
    success the decker breaks free but the Black IC lands one final attack before the connection
    drops. An ICCM biofeedback filter lowers the jack-out TN by 2.
    """
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state = copy.deepcopy(run.state_json)  # deepcopy, not dict(): keep nested JSON mutations un-aliased so the UPDATE fires
    decker = run.decker_json
    sec_code = state["host_security_code"]
    sec_value = state["host_security_value"]

    # -- Black IC jack-out gate (vr2 L612-614) --------------------------------------------------
    black_ic = _highest_engaged_black_ic(state) if state.get("black_ic_engaged") else None
    if black_ic is not None:
        tn = max(2, int(black_ic.get("rating", 1)) - (2 if decker.get("iccm") else 0))
        wp_roll = eng.roll_dice(decker.get("willpower", 4), tn)
        if wp_roll["successes"] <= 0:
            # Failed: the decker cannot tear free this action. Burn the Complex Action; run continues.
            state["pass_action_points"] = max(0, state.get("pass_action_points", 0) - 2)
            _append_event(state, {
                "type": "jack_out_failed", "roll": wp_roll,
                "description": (
                    f"Jack-out BLOCKED by Black IC {black_ic.get('rating')} -- Willpower Test "
                    f"(TN {tn}) failed ({wp_roll['successes']} success"
                    f"{'es' if wp_roll['successes'] != 1 else ''}). Still jacked in."
                ),
            })
            run.state_json = state
            await db.commit()
            await db.refresh(run)
            return _serialize_run(run, auth)
        # Success: break free, but Black IC lands one final strike first.
        state["pass_action_points"] = max(0, state.get("pass_action_points", 0) - 2)
        _append_event(state, {
            "type": "jack_out", "roll": wp_roll,
            "description": (
                f"Willpower Test (TN {tn}) SUCCEEDS ({wp_roll['successes']} success"
                f"{'es' if wp_roll['successes'] != 1 else ''}) -- you tear free, but Black IC "
                f"{black_ic.get('rating')} gets one final attack."
            ),
        })
        _black_ic_final_attack(state, decker, black_ic)

    ds = _apply_dump_shock(state, decker, sec_code, sec_value)

    # vr2 L610-611: jacking out is a Free Action before a black IC hit (best-effort -- emergency
    # exit is never blocked by the budget). After a black IC hit it required the Complex Willpower
    # test resolved above.
    if black_ic is None:
        state["pass_free"] = max(0, state.get("pass_free", 0) - 1)
    state["run_ended"] = True
    _finalize_run_end(state)
    # If the final Black IC attack put the decker down, record that cause; else a clean jack-out.
    if state["condition_monitor"]["physical_boxes"] >= 10:
        state["end_reason"] = "black_ic_lethal"
    elif state["condition_monitor"]["stun_boxes"] >= 10:
        state["end_reason"] = "black_ic_unconscious"
    else:
        state["end_reason"] = "jack_out"
    run.status = "killed" if state["end_reason"] == "black_ic_lethal" else "escaped"

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
