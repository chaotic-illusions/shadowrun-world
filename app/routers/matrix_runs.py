"""
Matrix Run API -- SR2/VR2.0 rules engine endpoints.
Separate from /matrix-hosts (SR1 topology editor).
"""

from __future__ import annotations

import copy
import random
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
    RunSuppressInput, SheaveSaveInput, SheafGenerateInput,
)
from app.services import matrix_engine as eng
from app.services import matrix_rules as rules

router = APIRouter()


# State keys removed entirely from state_json when serving a non-admin.
# (Admin sees the full state.) lurking_ic is GM-only: reactive IC "lurks
# silently" by the rules, so players must not see it exists at all.
_GM_ONLY_STATE_KEYS = {"sheaf", "host_acifs", "lurking_ic", "scrambles", "paydata", "data_bombs"}

# Maps crippler/ripper IC type names to the decker attribute they attack.
_CRIPPLER_TARGET: dict[str, str] = {
    "Acid": "bod", "Binder": "evasion", "Jammer": "sensor", "Marker": "masking",
    "Acid-rip": "bod", "Bind-rip": "evasion", "Jam-rip": "sensor", "Mark-rip": "masking",
}


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
        for k in _GM_ONLY_STATE_KEYS:
            state.pop(k, None)
        if isinstance(state.get("active_ic"), list):
            redacted = [_redact_ic(ic) for ic in state["active_ic"] if isinstance(ic, dict)]
            state["active_ic"] = [ic for ic in redacted if ic is not None]
        if isinstance(state.get("event_log"), list):
            # Drop GM-only events (e.g. surreptitious reactive-IC activity the decker
            # has not yet detected) so the log never betrays a hidden IC's presence.
            state["event_log"] = [
                e for e in state["event_log"]
                if not (isinstance(e, dict) and e.get("gm_only"))
            ]
        data["state_json"] = state
    return data


def _ic_detection_level(ic: dict) -> int:
    """Effective detection level the decker currently has on an IC (vr2 line 409).

    Proactive IC betray themselves by attacking -> default level 1 (presence known).
    Reactive IC 'do not betray themselves' -> default level 0 (unaware) until a secret
    Sensor Test or Analyze raises ``detection_level``. ``analyzed`` forces a full reveal.
    """
    level = ic.get("detection_level")
    if level is None:
        is_reactive = rules.IC_CATALOG.get(ic.get("type", ""), {}).get("ic_type") == "reactive"
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


def _initial_state(decker: dict, host: MatrixHost) -> dict:
    """Build the initial run state from decker stats and host config."""
    cfg = host.config_json or {}
    masking = decker.get("masking", 1)
    sleaze = (decker.get("utilities") or {}).get("sleaze", 0)
    det_factor = eng.detection_factor(masking, sleaze)
    hackingPool_total = max(0, (decker.get("intelligence", 1) + decker.get("mpcp", 1)) // 3)

    return {
        "security_tally": 0,
        "alert_status": "none",
        "condition_monitor": {
            "persona_boxes": 0,
            "physical_boxes": 0,
            "mpcp_damage": 0,
            "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
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
        "access_modifier": decker.get("access_modifier", 0),  # jackpoint Access side
        "console_access": decker.get("console_access", False),
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
        + decker.get("bandwidth_modifier", 0)
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
    suppressed = sum(
        1 for ic in state.get("active_ic", [])
        if ic.get("suppressed") and ic.get("status") == "active"
    )
    return max(1, base - suppressed)


def _get_decker_effective(decker: dict, state: dict) -> dict:
    """Return decker stats with crippler reductions applied."""
    dmg = state.get("condition_monitor", {}).get("persona_damage", {})
    mpcp_dmg = state.get("condition_monitor", {}).get("mpcp_damage", 0)
    return {
        "bod":     max(1, decker.get("bod", 4) - dmg.get("bod", 0)),
        "evasion": max(1, decker.get("evasion", 4) - dmg.get("evasion", 0)),
        "masking": max(1, decker.get("masking", 4) - dmg.get("masking", 0)),
        "sensor":  max(1, decker.get("sensor", 4) - dmg.get("sensor", 0)),
        "mpcp":    max(1, decker.get("mpcp", 4) - mpcp_dmg),
    }


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

    decker_dict = body.decker.model_dump()
    state = _initial_state(decker_dict, host)

    run = MatrixRun(
        host_id=body.host_id,
        decker_json=decker_dict,
        state_json=state,
        status="active",
        owner_token_hash=hash_token(auth["user_token"]) if auth.get("user_token") else None,
    )
    db.add(run)
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


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
                "description": cons["message"],
            })
        run.state_json = state
        await db.commit()
        await db.refresh(run)
        return _serialize_run(run, auth)

    # Data Bomb: accessing a bombed file/slave triggers it unless defused first (vr2).
    # Supplying the Defuse utility (utility_rating) attempts a defuse; otherwise it detonates.
    armed_bombs = state.get("data_bombs") or []
    if (body.action_type in ("download_data", "edit_file", "upload_data")
            and body.target_file and armed_bombs):
        defused = set(state.get("defused_bombs") or [])
        bomb = next((b for b in armed_bombs
                     if b.get("target") == body.target_file and b.get("target") not in defused),
                    None)
        if bomb is not None:
            btarget = bomb.get("target")
            brating = bomb.get("rating", 6)
            if body.utility_rating > 0:  # Defuse utility supplied -> attempt defuse first
                df = eng.data_bomb_defuse(decker_pool=pool, subsystem_rating=subsystem_rating,
                                          defuse_utility=body.utility_rating)
                if df["defused"]:
                    state.setdefault("defused_bombs", []).append(btarget)
                    _append_event(state, {
                        "type": "data_bomb", "outcome": "defused", "decker_roll": df["roll"],
                        "description": f"Data bomb on {btarget} defused -- no tally increase.",
                    })
                    run.state_json = state
                    await db.commit(); await db.refresh(run)
                    return _serialize_run(run, auth)
            # no Defuse utility, or the defuse failed -> the bomb detonates
            det = eng.data_bomb_detonate(
                ic_rating=brating, target_bod=eff["bod"],
                armor_rating=(decker.get("utilities") or {}).get("armor", 0))
            state["data_bombs"] = [b for b in armed_bombs if b is not bomb]  # one-shot
            cm = state.setdefault("condition_monitor", {})
            cm["persona_boxes"] = cm.get("persona_boxes", 0) + det["resistance"]["boxes"]
            state["security_tally"] += det["tally_increase"]
            _append_event(state, {
                "type": "data_bomb", "outcome": "detonated",
                "damage_level": det["resistance"]["final_damage_level"],
                "tally_increase": det["tally_increase"],
                "description": (
                    f"DATA BOMB on {btarget} detonated -- "
                    f"{det['resistance']['final_damage_level']} damage; tally "
                    f"+{det['tally_increase']} -> {state['security_tally']}."
                ),
            })
            _check_and_activate_sheaf(state, sec_code)
            run.state_json = state
            await db.commit(); await db.refresh(run)
            return _serialize_run(run, auth)

    test = eng.system_test(
        decker_pool=pool,
        subsystem_rating=subsystem_rating,
        security_value=sec_value,
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
        "note": body.note,
    }
    _append_event(state, log_entry)

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
        ic_info = rules.IC_CATALOG.get(ic["type"], {})
        ic_category = ic_info.get("category", "white")
        ic_subtype = ic_info.get("subtype", "")

        # Trace IC is classified "reactive" in the catalog but acts every turn on
        # its initiative (hunt -> locate -> trigger), so let it through here.
        if ic_info.get("ic_type") != "proactive" and ic_subtype != "trace":
            continue
        if ic["type"] == "Probe":
            continue  # already handled above

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
            attr_key = _CRIPPLER_TARGET.get(ic["type"], "bod")
            target_attr = eff.get(attr_key, 4)
            result = eng.crippler_attack(
                security_value=sec_value,
                security_code=sec_code,
                target_status=ic_target_status,
                target_attribute_rating=target_attr,
                ic_rating=ic["rating"],
                is_ripper=(ic_subtype == "ripper"),
                mpcp_rating=decker.get("mpcp", 1),
                hardening=decker.get("hardening", 0),
            )
            reduction = result["attribute_reduction"]
            pd = state["condition_monitor"]["persona_damage"]
            if reduction > 0:
                pd[attr_key] = min(pd.get(attr_key, 0) + reduction, target_attr - 1)
            desc = (
                f"{ic['type']}-{ic['rating']} vs {attr_key.upper()}: "
                f"{result['attack_roll']['successes']} atk / "
                f"{result['defense_roll']['successes']} def -> "
                f"{attr_key.upper()} -{reduction}."
            )
            if ic_subtype == "ripper" and result.get("chip_damage", 0) > 0:
                chip = result["chip_damage"]
                # Ripper chip damage: permanent -- stored in persona_damage (same slot, persists run)
                pd[attr_key] = min(pd.get(attr_key, 0) + chip, target_attr - 1)
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
        hardening       = decker.get("hardening", 0)

        if is_black:
            # Black IC: attack roll only (resistance is split into two separate tests below)
            attack_tn  = max(2, rules.COMBAT_TN[sec_code][ic_target_status] + cluster_penalty)
            attack_roll_black = eng.roll_dice(ic_attack_pool, attack_tn)
            base_dmg   = rules.IC_DAMAGE_LEVEL[sec_code]
            staged_dmg = eng.stage_damage(base_dmg, attack_roll_black["successes"], 1)
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
        attack = eng.cybercombat_attack(
            attacker_pool=ic_attack_pool,
            security_code=sec_code,
            target_status=ic_target_status,
            target_bod=eff["bod"],
            armor_rating=armor,
            ic_rating=ic["rating"],
            attacker_is_ic=True,
            tn_modifier=cluster_penalty,
        )
        final_dmg = attack["resistance"]["final_damage_level"]
        boxes = attack["resistance"]["boxes"]

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

    _spend_hp(state, body.hacking_pool_dice)
    attack_pool     = body.attack_pool + body.hacking_pool_dice
    cluster_penalty = _cluster_size(state, target_ic.get("cluster_id"))
    tn = rules.COMBAT_TN[sec_code]["intruding"] + cluster_penalty

    attack_roll = eng.roll_dice(attack_pool, tn)
    base_dmg = rules.IC_DAMAGE_LEVEL[sec_code]

    # IC resists with Security Value dice; TN = same as attacker's TN (code-based, not IC rating)
    resist_tn = rules.COMBAT_TN[sec_code]["intruding"] + cluster_penalty
    resist_roll = eng.roll_dice(sec_value, resist_tn)
    staged = eng.stage_damage(base_dmg, attack_roll["successes"], 1)
    final_dmg = eng.stage_damage(staged, resist_roll["successes"], -1)
    boxes = rules.DAMAGE_BOXES[final_dmg]

    target_ic["boxes"] = target_ic.get("boxes", 0) + boxes
    crashed = target_ic["boxes"] >= 10

    if crashed:
        target_ic["status"] = "crashed"
        tally_increase = target_ic["rating"]
        state["security_tally"] += tally_increase
        _append_event(state, {
            "type": "ic_crashed",
            "ic_id": body.target_ic_id,
            "description": (
                f"{target_ic['type']}-{target_ic['rating']} CRASHED. "
                f"Tally +{tally_increase} -> {state['security_tally']}"
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

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


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
    sec_code = state["host_security_code"]
    sec_value = state["host_security_value"]

    # Graceful logoff: Access Test vs. host Access Rating
    access_rating = _subsystem_rating(state, "access")
    det_factor = _effective_detection_factor(state, decker)
    state["detection_factor"] = det_factor
    deception = body.deception_utility

    # Check for active trace IC -- adds its rating to TN
    trace_tn_bonus = 0
    for ic in state.get("active_ic", []):
        if ic["status"] == "active" and "Trace" in ic.get("type", ""):
            trace_tn_bonus = max(trace_tn_bonus, ic["rating"])

    _spend_hp(state, body.hacking_pool_dice)
    pool = decker.get("computer_skill", 4) + body.hacking_pool_dice
    test = eng.system_test(
        decker_pool=pool,
        subsystem_rating=access_rating,
        security_value=sec_value,
        det_factor=det_factor,
        extra_tn_modifier=(-deception + trace_tn_bonus),
    )

    tally_increase = test["tally_increase"]
    state["security_tally"] += tally_increase

    if test["success"]:
        state["run_ended"] = True
        state["end_reason"] = "graceful_logoff"
        state.pop("has_legitimate_status", None)  # Host deletes passcode on logoff
        state["decoy_successes"] = 0
        state["decoy_hp"] = 0
        run.status = "escaped"
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

    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


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

    _append_event(state, {
        "type": "new_turn",
        "description": (
            f"Turn {state['current_turn']} begins. "
            f"Hacking Pool refreshed ({old_hp} -> {hackingPool_total})."
        ),
    })

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
        # Worm attacks the deck's MPCP; the Disinfect utility (utility_rating) defends.
        wr = eng.worm_attack(
            ic_rating=lurking["rating"],
            mpcp_rating=decker.get("mpcp", 1),
            hardening=decker.get("hardening", 0),
            disinfect_utility=body.utility_rating,
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
                    f"(permanent). Disinfect {body.utility_name}-{body.utility_rating} failed."
                ),
            })
        else:
            _append_event(state, {
                "type": "worm_resolved", "ic_id": body.ic_id, "ic_type": "Worm",
                "outcome": "repelled", "roll": wr["roll"],
                "description": (
                    f"Worm-{lurking['rating']} repelled by Disinfect "
                    f"{body.utility_name}-{body.utility_rating}. Worm still lurking."
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


@router.post("/{run_id}/suppress", response_model=MatrixRunRead)
async def suppress_ic(
    run_id: int,
    body: RunSuppressInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Suppress or release an active IC (vr2 Suppression).

    Suppressing costs 1 Detection Factor per IC (applied live by
    _effective_detection_factor); releasing restores it and adds the IC's rating to the
    security tally. The Decker's Detection Factor cannot fall below 1.
    """
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state = copy.deepcopy(run.state_json)
    decker = run.decker_json
    ic = next((c for c in state.get("active_ic", [])
               if c.get("id") == body.ic_id and c.get("status") == "active"), None)
    if ic is None:
        raise HTTPException(404, f"Active IC {body.ic_id} not found")

    if body.release:
        ic["suppressed"] = False
        state["security_tally"] = state.get("security_tally", 0) + ic.get("rating", 0)
        _append_event(state, {
            "type": "ic_released", "ic_id": ic["id"],
            "description": (
                f"Suppressed IC released -- Detection Factor restored; tally "
                f"+{ic.get('rating', 0)} -> {state['security_tally']}."
            ),
        })
        _check_and_activate_sheaf(state, state["host_security_code"])
    else:
        ic["suppressed"] = True
        df = _effective_detection_factor(state, decker)
        state["detection_factor"] = df
        _append_event(state, {
            "type": "ic_suppressed", "ic_id": ic["id"],
            "description": f"IC suppressed -- Detection Factor reduced to {df} (no tally increase).",
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
