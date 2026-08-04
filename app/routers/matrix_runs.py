"""
Matrix Run API -- SR2/VR2.0 rules engine endpoints.
Separate from /matrix-hosts (SR1 topology editor).
"""

from __future__ import annotations

import copy
import math
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
    RunActionInput, RunAttackInput, RunDefendInput, RunLogoffInput,
    RunSuppressInput, RunRevealHostRatingsInput, RunEnemyAttackInput,
    RunEnemyScanInput, RunAreaAttackInput, RunScrambleAttackInput,
    RunTrapDoorInput, SheaveSaveInput, SheafGenerateInput,
)
from app.services import matrix_engine as eng
from app.services import matrix_rules as rules
from app.services import run_trace
from app.services.matrix_host_config import normalize_host_config
from app.services.host_visibility import (
    sync_host_reveal_to_org, sync_host_security_to_org,
)

router = APIRouter()


async def trace_action(
    request: Request,
    run_id: int,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Opt-in per-action engine trace (``SR_TRACE`` env flag). Starts a computation-trace buffer
    for this request and, once the action resolves (or is refused), flushes the collected engine
    steps to ``data/traces/run_<id>.log`` for developer / GM observability. A no-op unless
    ``SR_TRACE`` is set, so normal play and the test suite are unaffected."""
    run_trace.start()
    try:
        if not request.url.path.endswith(("/suppress", "/logoff", "/jack-out")):
            run = await _get_run_or_404(db, run_id)
            _assert_run_access(run, auth)
            _assert_suppression_capacity(run.state_json, run.decker_json)
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
                       "_acting_count",
                       "host_stack", "_stack_current_host_name", "excluded_handles",
                       "pending_bouncer"}

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
    "hackingPool_total", "hackingPool_remaining", "storage_free_mp", "storage_capacity_mp",
    "storage_used_mp",
    "downloaded_files", "storage_programs", "active_memory_cap", "program_sizes",
    "squeeze_keys", "squeezed_active",
    "detection_factor", "interactive_defense", "program_damage", "dinab_damage",
    "one_shot_wiped",
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
# Derived: attacked attribute -> family recognizable from the attack, without Crippler/Ripper.
_CRIPPLER_OBSERVED_TYPE: dict[str, str] = {
    attr: str(mapping["ic"]) for attr, mapping in _ATTRIBUTE_ATTACK.items()
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
    if ic_type in {"Black IC (Lethal)", "Black IC (Non-Lethal)"}:
        return "Black IC"
    m = _IC_WRAPPER_RE.match(ic_type)
    return m.group(1).strip() if m else ic_type


def _ic_display_type(ic: dict) -> str:
    """Return the player-facing IC type, including modeled Worm variants."""
    observed_type = str(ic.get("observed_type") or "").strip()
    if observed_type and not ic.get("analyzed"):
        return observed_type
    ic_type = str(ic.get("type") or "IC")
    if _canonical_ic_type(ic_type) != "Worm":
        return ic_type
    return {
        "deathworm": "Deathworm",
        "tapeworm": "Tapeworm",
    }.get(str(ic.get("variant") or "").lower(), "Unknown IC")


def _worm_variant(value: Any) -> str | None:
    """Normalize one of the two supported Worm variants; reject missing or unknown values."""
    variant = str(value or "").strip().lower()
    return variant if variant in {"deathworm", "tapeworm"} else None


def _normalized_ic_payload(raw: dict, *, default_type: str = "Killer") -> dict:
    """Normalize legacy/designer IC keys into the runtime representation."""
    display_type = str(raw.get("ic_type") or raw.get("type") or default_type)
    ic_type = _canonical_ic_type(display_type) or default_type
    options = raw.get("options") or raw.get("defenses") or []
    mode = raw.get("mode")
    if display_type == "Black IC (Lethal)":
        mode = "lethal"
    elif display_type == "Black IC (Non-Lethal)":
        mode = "non_lethal"
    out = {
        key: value for key, value in raw.items()
        if key not in {"type", "ic_type", "rating", "options", "defenses", "mode", "cascading", "expert"}
        and value is not None
    }
    out.update({
        "type": ic_type,
        "rating": max(1, int(raw.get("rating", 1) or 1)),
    })
    if isinstance(options, list) and options:
        out["options"] = list(options)
    if raw.get("cascading"):
        out["cascading"] = True
    if raw.get("expert"):
        out["expert"] = raw["expert"]
    if mode in {"lethal", "non_lethal"}:
        out["mode"] = mode
    return out


def _host_composite_errors(config: dict) -> list[str]:
    """Return RAW legality errors for Construct and Party IC events in a host sheaf."""
    security_value = max(1, int(config.get("security_value", 1) or 1))
    security_code = str(config.get("security_code", "Green") or "Green")
    capacity = security_value * 2
    max_rating = -(-(security_value * 2) // 3)
    max_party_count = max(1, security_value // 2)
    max_threat = {"Blue": 0, "Green": 1, "Orange": 2, "Red": 3, "Black": 4}.get(
        security_code, 4,
    )
    errors: list[str] = []
    for step_index, step in enumerate(config.get("sheaf") or [], start=1):
        if not isinstance(step, dict):
            continue
        for event_index, event in enumerate(step.get("events") or [], start=1):
            if not isinstance(event, dict) or event.get("type") not in {"construct", "party_ic"}:
                continue
            kind = str(event["type"])
            label = f"sheaf step {step_index}, event {event_index}"
            components = [item for item in (event.get("components") or []) if isinstance(item, dict)]
            minimum = 2 if kind == "construct" else 1
            if len(components) < minimum:
                errors.append(f"{label}: {kind} requires at least {minimum} IC component(s)")
            if kind == "party_ic" and len(components) > max_party_count:
                errors.append(f"{label}: Party IC exceeds its {max_party_count}-component limit")
            used = 0
            for component in components:
                ic_type = _canonical_ic_type(str(component.get("ic_type") or component.get("type") or ""))
                rating = int(component.get("rating", 0) or 0)
                if rating < 1 or rating > max_rating:
                    errors.append(f"{label}: {ic_type or 'IC'} rating must be 1-{max_rating}")
                category = rules.IC_CATALOG.get(ic_type, {}).get("category")
                used += max(0, rating) + (2 if category == "black" else 1 if category == "gray" else 0)
                if kind == "party_ic":
                    options = component.get("options") or component.get("defenses") or []
                    used += len(options) if isinstance(options, list) else 0
            if kind == "construct":
                defenses = event.get("defenses") or []
                used += len(defenses) * 2 if isinstance(defenses, list) else 0
                threat = int(event.get("threat_rating", 0) or 0)
                if threat < 0 or threat > max_threat:
                    errors.append(f"{label}: Threat Rating must be 0-{max_threat} for {security_code}")
            if used > capacity:
                errors.append(f"{label}: {kind} uses {used} of {capacity} capacity")
    return errors


def _target_file_name(target: str) -> str:
    """Extract the bare file/piece name from a defense target key.

    Defense targets are stored with inconsistent prefixes across features -- a file-level
    data bomb as "files::<name>", a Files scramble as "files::file::<name>" -- while a
    download addresses the bare "<name>". Compare on the trailing segment so the bomb/
    scramble actually fires on the matching download.
    """
    return target.rsplit("::", 1)[-1].strip() if target else ""


def _paydata_matches(item: dict, target: str) -> bool:
    """Match a paydata target by stable ID, with name fallback for legacy payloads."""
    wanted = str(target or "").strip()
    item_id = str(item.get("id") or "").strip()
    if item_id and wanted == item_id:
        return True
    return str(item.get("name") or "").strip().lower() == wanted.lower()


def _paydata_for_target(state: dict, target: str) -> dict | None:
    return next(
        (
            item for item in (state.get("paydata") or [])
            if isinstance(item, dict) and _paydata_matches(item, target)
        ),
        None,
    )


def _paydata_label(state: dict, target: str) -> str:
    if str(target or "").strip() == "__entire__":
        return "Files datastore (all files)"
    item = _paydata_for_target(state, target)
    return str(item.get("name") or target) if item else str(target or "")


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
    if t.startswith("access::"):
        return "access", t[len("access::"):]
    if t.startswith("slave::"):
        return "slave", t[len("slave::"):]
    if t == "__slave__":
        return "slave", "Slave device"
    return "files", t


def _assert_known_action_target(state: dict, body: RunActionInput) -> None:
    """Reject hidden file/device targets before any action resources are spent."""
    if body.action_type in ("download_data", "edit_file"):
        wanted = (body.target_file or "").strip()
        known = any(
            _paydata_matches(item, wanted)
            and item.get("located") and not item.get("destroyed")
            for item in (state.get("paydata") or []) if isinstance(item, dict)
        )
        if not wanted or not known:
            raise HTTPException(400, "File target is not located or is no longer available")
        return

    if body.action_type != "analyze_icon":
        return

    scope, name = _data_bomb_scope_name(body.target_file or "")
    wanted = name.strip().lower()
    if scope == "files":
        known = any(
            _paydata_matches(item, name)
            and item.get("located") and not item.get("destroyed")
            for item in (state.get("paydata") or []) if isinstance(item, dict)
        )
    else:
        devices = [
            str(item).strip().lower() for item in (state.get("slave_devices") or [])
            if str(item).strip()
        ]
        slave_known = "slave" in (state.get("analyzed_subsystems") or [])
        known = slave_known and (
            wanted in devices
            or (not devices and wanted in ("__device__", "slave device"))
        )
    if not wanted or not known:
        raise HTTPException(400, "Icon target is not located or visible")


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


def _scramble_player_label(state: dict, target_key: str) -> str:
    """Player-safe Scramble label that withholds an unlocated paydata filename."""
    if (target_key or "").startswith("files::file::"):
        name = _target_file_name(target_key).strip()
        located = any(
            _paydata_matches(item, name) and item.get("located")
            for item in (state.get("paydata") or []) if isinstance(item, dict)
        )
        if not located:
            return "Scramble IC protecting an unidentified file"
    return _scramble_label(target_key)


def _scramble_ref(index: int) -> str:
    """Stable run-local player reference that does not disclose a Scramble's target key."""
    return f"scramble_{index + 1}"


def _scramble_ref_for(state: dict, scramble: dict) -> str | None:
    """The stable player ref (``scramble_N``) for a specific Scramble dict, or None if not found."""
    for i, s in enumerate(state.get("scrambles") or []):
        if s is scramble:
            return _scramble_ref(i)
    return None


def _file_scramble_for_target(state: dict, target_file: str) -> dict | None:
    """Return unresolved Scramble IC that blocks access to the selected Files target."""
    for scramble in (state.get("scrambles") or []):
        if not isinstance(scramble, dict):
            continue
        target_key = str(scramble.get("target_key") or "")
        if _scramble_subsystem(target_key) != "files":
            continue
        if target_key == "files::entire":
            return scramble
        protected_name = _target_file_name(target_key)
        if protected_name.strip().lower() == str(target_file or "").strip().lower():
            return scramble
        if any(
            _paydata_matches(item, target_file) and _paydata_matches(item, protected_name)
            for item in (state.get("paydata") or []) if isinstance(item, dict)
        ):
            return scramble
    return None


def _paydata_encrypted(state: dict, pd: dict) -> bool:
    """A located file is ENCRYPTED while any unresolved Scramble IC still covers it (vr2: the
    Scramble IS the encryption). Encryption is observable (garbled data) even before the scramble
    has been formally discovered/analyzed."""
    if not isinstance(pd, dict):
        return False
    return _file_scramble_for_target(state, str(pd.get("id") or pd.get("name") or "")) is not None


def _reveal_located_file_encryption(state: dict, pd: dict) -> bool:
    """On locating a file, report whether it is ENCRYPTED (its data is garbled by a covering
    Scramble). This NO LONGER auto-discovers the Scramble: discovery now requires an **Analyze Icon**
    on the file (which also reveals the variant and any linked/standalone data bomb) or an Analyze
    Subsystem. The file still renders garbled via ``_paydata_encrypted`` regardless of discovery, so
    the decker SEES the lock but must scan the icon to learn how to defeat it."""
    return _paydata_encrypted(state, pd)


def _scramble_protected_files(state: dict, scramble: dict) -> list[dict]:
    """The paydata files a Scramble protects -- a per-file scramble guards its one file; a
    ``files::entire`` scramble guards every still-present file. Access/other scopes protect no
    downloadable data (return empty)."""
    target_key = str(scramble.get("target_key") or "")
    paydata = state.get("paydata") or []
    if target_key == "files::entire":
        return [item for item in paydata if isinstance(item, dict) and not item.get("destroyed")]
    if target_key.startswith("files::file::"):
        one = next(
            (item for item in paydata
             if isinstance(item, dict) and _paydata_matches(item, _target_file_name(target_key))),
            None,
        )
        return [one] if one is not None else []
    return []


def _scramble_poison_react(state: dict, decker: dict, scramble: dict) -> bool:
    """A Poison Scramble reacts to EACH cybercombat attack against it (hit OR miss, user ruling
    2026-07-28 / vr2 L493): it rolls its Poison Test (rating dice vs the decker's Computer skill)
    and, on a success, ERASES the data it protects -- one file for a per-file scramble, the whole
    datastore for ``files::entire``. Returns True if data was destroyed; emits a player event."""
    protected = _scramble_protected_files(state, scramble)
    consequence = eng.scramble_failure_consequence(
        variant="poison",
        is_key=any(bool(f.get("is_key")) for f in protected),
        scramble_rating=int(scramble.get("rating", 6) or 6),
        decker_computer_skill=decker.get("computer_skill", 6),
    )
    destroyed = bool(consequence.get("data_destroyed"))
    if destroyed:
        for f in protected:
            f["destroyed"] = True
    _append_event(state, {
        "type": "scramble_poison",
        "success": False,
        "data_destroyed": destroyed,
        "key_data_lost": bool(consequence.get("key_data_lost")),
        "files_destroyed": [f.get("name") for f in protected] if destroyed else [],
        "description": (
            "The Poison IC erased the protected data."
            if destroyed else
            "The Poison IC attempted to erase the data, but failed."
        ),
    })
    return destroyed


def _link_exploding_scramble_bombs(state: dict) -> None:
    """RAW L491: an Exploding Scramble is linked to a data bomb. Ensure every exploding
    ``files::file::<id>`` scramble has a data bomb on the same file so the decker can DISCOVER it
    (Analyze Icon) and DEFUSE it (Defuse Data Bomb) before decrypting -- and so a decrypt/crash
    WITHOUT defusing first detonates it. Idempotent; only creates a bomb when the file has none
    (a designer-authored bomb on the same file already serves as the linked bomb)."""
    scrambles = state.get("scrambles") or []
    bombs = state.setdefault("data_bombs", [])
    if not isinstance(bombs, list):
        return
    for scr in scrambles:
        if not isinstance(scr, dict) or scr.get("variant") != "exploding":
            continue
        target_key = str(scr.get("target_key") or "")
        if target_key.startswith("files::file::"):
            file_id = _target_file_name(target_key)
            bomb_target = f"files::{file_id}"
            has_bomb = any(
                isinstance(b, dict)
                and _data_bomb_scope_name(b.get("target", ""))[0] == "files"
                and _data_bomb_scope_name(b.get("target", ""))[1].strip().lower()
                == file_id.strip().lower()
                for b in bombs
            )
        elif target_key == "files::entire":
            # One sentinel bomb guards the whole datastore: accessing ANY file -- or decrypting/
            # crashing the scramble -- without defusing it first detonates it once.
            bomb_target = "files::__entire__"
            has_bomb = any(
                isinstance(b, dict) and b.get("target") == bomb_target for b in bombs
            )
        elif target_key.startswith("access::"):
            # An Access Exploding Scramble's linked bomb detonates on a successful Access operation
            # (graceful logoff -- including a trap-door transit -- or Validate Passcode), or on a
            # decrypt/crash of the scramble, unless defused first. Distinct sentinel ("__all__") so
            # its Defuse handle never collides with the Files datastore bomb ("__entire__").
            piece = _target_file_name(target_key) if "::piece::" in target_key else "__all__"
            bomb_target = f"access::{piece}"
            has_bomb = any(
                isinstance(b, dict) and b.get("target") == bomb_target for b in bombs
            )
        else:
            continue
        if not has_bomb:
            bombs.append({
                "target": bomb_target,
                "rating": int(scr.get("rating", 6) or 6),
                "linked_scramble": target_key,
            })


def _armed_bomb_on_file(state: dict, scramble: dict) -> dict | None:
    """The undefused data bomb protecting the same file as this Scramble (an Exploding Scramble's
    linked bomb), or None once it has been defused."""
    target_key = str(scramble.get("target_key") or "")
    file_id = _target_file_name(target_key).strip().lower()
    defused = set(state.get("defused_bombs") or [])
    for b in (state.get("data_bombs") or []):
        if not isinstance(b, dict) or b.get("target") in defused:
            continue
        # A subsystem-wide Exploding Scramble's sentinel bomb is matched by its linkage back to the
        # scramble (there is no single filename to compare for a whole-datastore bomb).
        if b.get("linked_scramble") == target_key:
            return b
        scope, name = _data_bomb_scope_name(b.get("target", ""))
        if scope != "files":
            continue
        if name.strip().lower() == file_id or any(
            _paydata_matches(item, file_id) and _paydata_matches(item, name)
            for item in (state.get("paydata") or []) if isinstance(item, dict)
        ):
            return b
    return None


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
        same_target = name.strip().lower() == tgt
        if not same_target:
            same_target = any(
                _paydata_matches(item, target_file) and _paydata_matches(item, name)
                for item in (state.get("paydata") or []) if isinstance(item, dict)
            )
        if not tgt or same_target:
            return scope
    return None


def _build_trap_doors(host: MatrixHost) -> list[dict]:
    """Normalize a host's designer trap doors into GM-only run-state entries.

    A trap door is a concealed comm port to another host, hidden on a subsystem (the designer
    attaches it to a Slave device). Per vr2 it is found via an Analyze Subsystem operation on
    the concealing subsystem -- so each entry starts undiscovered. The destination is redacted
    from players (see _serialize_run) until they ENTER it. The far host's LTG access can be learned
    only on the far side (logon + Analyze Access there).
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

_ACTION_LABELS = {
    "analyze_host": "Analyze Host",
    "analyze_icon": "Analyze Icon",
    "analyze_ic": "Analyze IC",
    "analyze_security": "Analyze Security",
    "analyze_subsystem": "Analyze Subsystem",
    "dinab": "DINAB",
    "locate_ic": "Locate IC",
    "mpcp_attack": "MPCP Attack",
}


def _action_label(action: str) -> str:
    key = str(action or "").strip().lower()
    return _ACTION_LABELS.get(key, key.replace("_", " ").title())


def _successes(value: int) -> str:
    count = int(value or 0)
    return f"{count} success{'es' if count != 1 else ''}"

_IC_EVENT_PUBLIC_FIELDS = {
    "type", "description", "turn", "init", "action", "action_label", "success", "net_successes",
    "outcome", "subsystem", "status", "damage_level", "boxes", "power", "resisted",
    "ic_id", "actor_id", "target_id", "initiator", "actor", "target", "ic_type",
    "maneuvering_roll", "attack_successes", "defense_successes", "shield_successes",
    "defense_margin", "attribute_target", "attribute_reduction", "shield_rating", "trace_phase",
    "shield_remaining", "successes",
}
_IC_EVENT_FULL_FIELDS = _IC_EVENT_PUBLIC_FIELDS | {
    "ic_rating", "roll", "attack_roll", "defense_roll", "decker_roll", "maneuvering_roll", "opposing_roll",
    "sensor_roll", "resistance_roll", "damage_resistance_roll", "to_hit_roll", "variant",
    "cluster_size", "attack_successes", "defense_successes", "staged_level", "base_level",
}


def _redact_event_ic(e: dict, disclosures: dict[str, dict]) -> dict:
    """Project IC identity and opposed rolls at the decker's current detection level."""
    if not isinstance(e, dict):
        return e
    if e.get("type") == "party_ic_activation":
        count = max(0, int(e.get("cluster_size", 0) or 0))
        return {
            key: value for key, value in {
                "type": e.get("type"),
                "turn": e.get("turn"),
                "init": e.get("init"),
                "cluster_size": count,
                "description": (
                    f"Party IC activated: {count} unidentified "
                    f"component{'s' if count != 1 else ''}."
                ),
            }.items()
            if value is not None
        }
    is_maneuver = e.get("type") == "maneuver"
    ic_id = e.get("ic_id")
    if is_maneuver:
        ic_id = e.get("actor_id") if e.get("initiator") == "npc" else e.get("target_id")
    disclosure = disclosures.get(ic_id)
    if not disclosure:
        return e

    level = disclosure["level"]
    allowed = _IC_EVENT_FULL_FIELDS if level >= 3 else _IC_EVENT_PUBLIC_FIELDS
    out = {key: value for key, value in e.items() if key in allowed}
    ic_type = str(disclosure.get("type") or out.get("ic_type") or "IC")
    rating = disclosure.get("rating", out.get("ic_rating"))
    safe_label = ic_type if level >= 2 else "Unknown IC"
    desc = out.get("description")
    if isinstance(desc, str):
        variants = []
        if rating not in (None, ""):
            variants += [f"{ic_type}-{rating}", f"{ic_type} Rating {rating}"]
        if level < 2:
            variants.append(ic_type)
        for v in variants:
            desc = desc.replace(v, safe_label)
        out["description"] = desc
    if e.get("type") == "ic_activation" and _canonical_ic_type(ic_type) == "Construct" and level < 3:
        count = len(e.get("construct_components") or [])
        out["description"] = (
            f"{safe_label} activated: {count} unidentified "
            f"component{'s' if count != 1 else ''}."
        )
    if (e.get("type") == "ic_attack"
            and e.get("attribute_target")
            and level < 3):
        attribute = str(e.get("attribute_target") or "attribute").upper()
        attack_successes = int(e.get("attack_successes", 0) or 0)
        total_defense = int(e.get("defense_successes", 0) or 0)
        shield_successes = int(e.get("shield_successes", 0) or 0)
        persona_successes = max(0, total_defense - shield_successes)
        net_successes = int(e.get("net_successes", 0) or 0)
        defense_margin = int(e.get("defense_margin", 0) or 0)
        reduction = int(e.get("attribute_reduction", 0) or 0)
        component_label = (
            safe_label if level >= 2
            else "Unknown IC component" if _canonical_ic_type(ic_type) == "Construct"
            else "Unknown IC"
        )
        out["description"] = (
            f"{component_label} vs {attribute}: {attack_successes} attack / "
            f"{total_defense} total defense ({persona_successes} persona + "
            f"{shield_successes} Shield). Net Successes: {net_successes}. "
            f"Defense Margin: {defense_margin}. {attribute} -{reduction}."
        )
    if out.get("ic_type") is not None:
        out["ic_type"] = safe_label
    if level < 3:
        out.pop("ic_rating", None)
    if out.get("type") == "defense_pending":
        out.pop("attack_roll", None)
    if out.get("type") == "shield_parry" and level < 3:
        shield_rating = int(e.get("shield_rating", 0) or 0)
        shield_remaining = int(e.get("shield_remaining", 0) or 0)
        successes = int(e.get("successes", 0) or 0)
        source = ic_type if level >= 2 else "Unknown IC"
        wear = (
            f"Shield worn to {shield_remaining} -- reload via Swap Memory."
            if shield_remaining > 0
            else "Shield burned out -- reload a fresh copy via Swap Memory."
        )
        out["description"] = (
            f"Shield-{shield_rating} contributes {successes} defense "
            f"success{'es' if successes != 1 else ''} against {source}. {wear}"
        )
        out.pop("roll", None)
    if out.get("type") == "ic_attack" and level < 3:
        defense_roll = e.get("defense_roll")
        if isinstance(defense_roll, dict):
            shield_dice = defense_roll.get("shield_dice")
            shield_successes = int(defense_roll.get("shield_successes", 0) or 0)
            out["defense_roll"] = {
                "successes": 0,
                "persona_successes": int(defense_roll.get("successes", 0) or 0),
                "dice": list(defense_roll.get("dice") or []),
                "shield_dice": list(shield_dice) if isinstance(shield_dice, list) else [],
                "shield_successes": shield_successes,
            }
        out.pop("attack_roll", None)
    if out.get("type") == "ic_attack" and _canonical_ic_type(ic_type) == "Trace" and level < 3:
        phase = str(e.get("trace_phase") or "")
        if phase in ("hunt_hit", "locating", "spoofed"):
            out["description"] = {
                "hunt_hit": "Trace IC Hunt Cycle succeeded -- it enters its Location Cycle.",
                "locating": "Trace IC Location Cycle continues.",
                "spoofed": "Trace IC Location Cycle spoofed this round -- no trace progress.",
            }[phase]
        elif phase == "hunting":
            out["description"] = "Trace IC Hunt Cycle continues -- the jackpoint is not yet located."
    if out.get("type") == "worm_resolved" and level < 3:
        out.pop("roll", None)
        out.pop("variant", None)
        out.pop("ic_rating", None)
        outcome = out.get("outcome")
        where = out.get("subsystem")
        location = f" on the {str(where).title()} subsystem" if where else ""
        if outcome == "mpcp_infected":
            out["description"] = (
                f"Hidden IC activity{location} infected your MPCP. The chip requires replacement."
            )
        else:
            out["description"] = (
                f"Hidden IC activity{location} tried to infect your MPCP but was repelled."
            )
    if is_maneuver:
        label_key = "actor" if out.get("initiator") == "npc" else "target"
        out[label_key] = safe_label
        if level < 3:
            opponent_roll = "maneuvering_roll" if out.get("initiator") == "npc" else "opposing_roll"
            out.pop(opponent_roll, None)
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


def _redact_system_action_event(e: dict, state: dict) -> dict:
    """Return a player-safe generic System Test event.

    Opposed roll totals would let the player derive the host's successes and therefore its hidden
    security-tally increase. Show only the signed net result. The effective target number is shown
    only after Analyze Host has revealed the tested subsystem's ACIFS rating.
    """
    if not isinstance(e, dict):
        return e
    if not e.get("host_system_test") or "net_successes" not in e:
        return e
    out = dict(e)
    out.pop("host_system_test", None)
    out.pop("decker_roll", None)
    out.pop("host_roll", None)
    subsystem = str(out.get("subsystem", "") or "").strip().lower()
    known_ratings = state.get("host_ratings_revealed") or {}
    target_number = (
        out.get("target_number")
        if subsystem in known_ratings and not out.get("target_number_concealed")
        else None
    )
    if target_number is None:
        out.pop("target_number", None)
    out.pop("target_number_concealed", None)
    action_label = str(out.get("action_label") or _action_label(out.get("action", "System Test")))
    result = "succeeded" if out.get("success") else "failed"
    net = int(out.get("net_successes", 0) or 0)
    decker_successes = int((e.get("decker_roll") or {}).get("successes", 0) or 0)
    target_text = f"; Target Number: {target_number}" if target_number is not None else ""
    if out.get("action") in ("analyze_host", "crash_host"):
        out["description"] = (
            f"{action_label} -- {result} (Player Successes: {decker_successes}{target_text})."
        )
        return out
    if net == 0 and decker_successes > 0 and out.get("action") != "locate_paydata":
        resolution = "; Nonzero tie: ties favor the decker"
    elif net == 0 and decker_successes > 0:
        resolution = "; Locate Paydata requires positive net successes"
    elif net == 0:
        resolution = "; No successes on either side: task fails"
    else:
        resolution = ""
    out["description"] = (
        f"{action_label} -- {result} (Net Successes: {net}{resolution}{target_text})."
    )
    return out


def _normalize_legacy_shield_events(events: list[dict]) -> None:
    """Repair the pre-Shield-roll-folding event shape in serialized response copies only."""
    for index, parry in enumerate(events[:-1]):
        attack = events[index + 1]
        if (
            not isinstance(parry, dict)
            or not isinstance(attack, dict)
            or parry.get("type") != "shield_parry"
            or attack.get("type") != "ic_attack"
            or not attack.get("attribute_target")
            or parry.get("turn") != attack.get("turn")
        ):
            continue
        defense_roll = attack.get("defense_roll")
        shield_roll = parry.get("roll")
        if (
            not isinstance(defense_roll, dict)
            or not isinstance(shield_roll, dict)
            or "shield_dice" in defense_roll
        ):
            continue
        shield_successes = int(parry.get("successes", shield_roll.get("successes", 0)) or 0)
        attack_successes = int((attack.get("attack_roll") or {}).get("successes", 0) or 0)
        persona_successes = int(defense_roll.get("successes", 0) or 0)
        total_defense = persona_successes + shield_successes
        net_successes = max(0, attack_successes - total_defense)
        defense_margin = max(0, total_defense - attack_successes)
        defense_roll["shield_dice"] = list(shield_roll.get("dice") or [])
        defense_roll["shield_successes"] = shield_successes
        attack.update({
            "attack_successes": attack_successes,
            "defense_successes": total_defense,
            "shield_successes": shield_successes,
            "net_successes": net_successes,
            "defense_margin": defense_margin,
        })
        attr = str(attack.get("attribute_target") or "attribute").upper()
        reduction = int(attack.get("attribute_reduction", 0) or 0)
        ic_type = str(attack.get("ic_type") or parry.get("context") or "IC")
        ic_rating = attack.get("ic_rating")
        label = f"{ic_type}-{ic_rating}" if ic_rating not in (None, "") else ic_type
        attack["description"] = (
            f"{label} Construct component vs {attr}: {attack_successes} attack / "
            f"{total_defense} total defense ({persona_successes} persona + "
            f"{shield_successes} Shield). Net Successes: {net_successes}. "
            f"Defense Margin: {defense_margin}. {attr} -{reduction}."
        )
        parry.update({
            "ic_id": attack.get("ic_id"),
            "ic_type": attack.get("ic_type"),
            "ic_rating": attack.get("ic_rating"),
        })
        shield_rating = int(parry.get("shield_rating", 0) or 0)
        shield_remaining = int(parry.get("shield_remaining", 0) or 0)
        wear = (
            f"Shield worn to {shield_remaining} -- reload via Swap Memory."
            if shield_remaining > 0
            else "Shield burned out -- reload a fresh copy via Swap Memory."
        )
        parry["description"] = (
            f"Shield-{shield_rating} contributes {shield_successes} defense "
            f"success{'es' if shield_successes != 1 else ''} against {ic_type} "
            f"(TN {shield_roll.get('tn')}). {wear}"
        )


def _build_located_paydata(state: dict, *, redact: bool) -> list[dict]:
    """Project the decker's LOCATED paydata for the run payload (name/size/key/downloaded state) so
    the UI can drive its storage decisions and Analyze Icon / Download pickers. Built for BOTH the
    player view and the admin view (the admin also keeps the full GM ``paydata`` list) -- otherwise
    files vanish from the admin console and its Analyze Icon has no targets.

    Progressive disclosure (``redact``, players + runner-view preview): a located file's true size
    (Mp) stays hidden until the decker runs an Analyze Icon on it (``size_mp`` None -> the UI shows
    "??? Mp"); admins (``redact`` False) always see the real size. The encryption ACTION GATE is
    uniform: ``encrypted`` (and the covering Scramble's ref/variant/rating) is disclosed only once
    the Scramble is DISCOVERED -- via an Analyze Icon on the file, an Analyze Subsystem, or a blind
    Download/Edit attempt (which trips an Exploding Scramble's bomb) -- for BOTH views, so the admin
    plays with the SAME file affordances as the player (a blind Download stays available to both
    until discovery). The admin merely ALSO sees a ``scrambled`` marker so it knows a lock is hidden
    there. Once known, the Scramble ref/variant/rating ride the entry so the file's card can offer
    Decrypt / Crash / Analyze IC in place."""
    out: list[dict] = []
    for p in (state.get("paydata") or []):
        if not isinstance(p, dict) or not p.get("located"):
            continue
        analyzed = bool(p.get("analyzed"))
        scramble = _file_scramble_for_target(state, str(p.get("id") or p.get("name") or ""))
        covered = scramble is not None
        known = covered and bool(scramble.get("discovered"))
        entry = {
            "id": p.get("id"),
            "name": p.get("name"),
            # Uniform action gate: the lock is "encrypted" only once DISCOVERED, for admin + player
            # alike -- so both blind-download until it is found in play.
            "encrypted": known,
            "analyzed": analyzed,
            "size_mp": max(0, int(p.get("density", 0) or 0)) if (analyzed or not redact) else None,
            "is_key": bool(p.get("is_key")),
            "downloaded": bool(p.get("downloaded")),
            "destroyed": bool(p.get("destroyed")),
            "tampered": bool(p.get("tampered")),
        }
        # GM "sees more": flag a still-undiscovered Scramble to the admin/runner view WITHOUT
        # changing the action set (it still blind-downloads like a player until discovery).
        if covered and not known and not redact:
            entry["scrambled"] = True
        # Surface the covering Scramble so the file's own card can drive Decrypt / Crash / Analyze
        # IC -- but ONLY once DISCOVERED, so admin and player share the identical action set.
        if known:
            tk = str(scramble.get("target_key") or "")
            entry["scramble_ref"] = tk if not redact else _scramble_ref_for(state, scramble)
            entry["scramble_kind"] = "file" if tk.startswith("files::file::") else "node"
            if scramble.get("rating_revealed"):
                entry["scramble_rating"] = int(scramble.get("rating", 0) or 0)
            if scramble.get("variant_revealed"):
                entry["scramble_variant"] = scramble.get("variant")
        out.append(entry)
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
    state_data = data.get("state_json") or {}
    decker_data = data.get("decker_json") or {}
    effective_persona = _get_decker_effective(decker_data, state_data)
    base_df = _base_detection_factor(state_data, decker_data)
    suppression_count = _suppressed_count(state_data)
    state_data["effective_persona"] = effective_persona
    state_data["base_detection_factor"] = base_df
    state_data["detection_factor"] = max(1, base_df - suppression_count)
    state_data["suppression_count"] = suppression_count
    state_data["suppression_overflow"] = _suppression_overflow(state_data, decker_data)
    data["state_json"] = state_data
    # Located-paydata projection for EVERYONE (admins included). Without it, located files vanish
    # from the admin console and its Analyze Icon has no targets (see B). The player branch below
    # rebuilds this with progressive-disclosure redaction; admins keep the real sizes.
    state_data["located_paydata"] = _build_located_paydata(state_data, redact=False)
    serialized_events = (data.get("state_json") or {}).get("event_log")
    if isinstance(serialized_events, list):
        _normalize_legacy_shield_events(serialized_events)
    # ``view_as_player`` lets an admin preview the EXACT player payload (UI runner view): redact
    # exactly as for a real non-admin so no GM-only state ever reaches the browser in that mode.
    if not auth.get("is_admin") or auth.get("view_as_player"):
        state = dict(data.get("state_json") or {})
        # Surface only the paydata the decker has actually LOCATED (name/key/downloaded state) so
        # the player can make storage decisions; the full GM paydata list is then redacted below.
        # Progressive disclosure: a located file's true size (Mp) and confirmed encryption status
        # stay hidden ("??? Mp", no lock badge) until the decker runs an Analyze Icon on it (see C).
        located_paydata = _build_located_paydata(state, redact=True)
        # Surface only DISCOVERED trap doors, and even then without the destination -- the player
        # knows a port to "another system" exists, not where it leads. Filing only records it for
        # later (the destination is reachable ONLY through the door); the destination -- and
        # whether it has LTG access -- stays unknown until the decker enters and analyzes it there.
        discovered_trap_doors = [
            {"id": d.get("id"),
             "source_piece": d.get("source_piece", ""),
             "subsystem": d.get("subsystem", "slave")}
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
            if scope == "files":
                display = _paydata_label(state, name)
            elif scope == "access":
                display = "Access subsystem" if name == "__all__" else f"Access: {name}"
            else:
                display = name
            discovered_data_bombs.append({
                "target": name,
                "scope": scope,
                "name": display,
            })
        # Surface only DISCOVERED scrambles (found via Analyze Subsystem on the Files/Slave
        # subsystem that holds them). Redacted to target_key + subsystem + a human label -- enough
        # to offer Decrypt File against the RIGHT scramble -- WITHOUT leaking its rating or variant
        # (Poison/Exploding stay GM-only; scrambles is popped below with the other GM-only keys).
        discovered_scrambles = []
        for index, s in enumerate(state.get("scrambles") or []):
            if not isinstance(s, dict) or not s.get("discovered"):
                continue
            entry = {
                "scramble_ref": _scramble_ref(index),
                "subsystem": _scramble_subsystem(s.get("target_key", "")),
                "label": _scramble_player_label(state, s.get("target_key", "")),
                # A per-file Scramble (files::file::<id>) lives on its file's card in the Files pane;
                # only node-level Scrambles (files::entire, access, slave) show in Subsystem Defenses.
                "target_kind": ("file" if str(s.get("target_key", "")).startswith("files::file::")
                                else "node"),
            }
            # Rating is disclosed only after an Analyze IC on the scramble. The variant
            # (Poison/Exploding) is surfaced once an Analyze Icon (file) or Analyze Subsystem has
            # revealed it -- the decker needs the variant to pick the safe order (defuse-before-
            # decrypt for Exploding).
            if s.get("rating_revealed"):
                entry["rating"] = int(s.get("rating", 0) or 0)
            if s.get("variant_revealed"):
                entry["variant"] = s.get("variant")
            discovered_scrambles.append(entry)
        # Lurking reactive IC remains GM-only until detected. A blown Tar ambush is fully known;
        # other detected/located lurkers use the same graduated redaction as active IC.
        revealed_lurking_ic = []
        for ic in (state.get("lurking_ic") or []):
            if not isinstance(ic, dict):
                continue
            if ic.get("revealed") and ic.get("type") in ("Tar Baby", "Tar Pit"):
                revealed_lurking_ic.append({
                    "id": ic.get("id"), "type": ic.get("type"), "rating": ic.get("rating"),
                    "status": ic.get("status", "lurking"), "revealed": True,
                    "detection_level": 3,
                })
                continue
            redacted = _redact_ic(ic)
            if redacted is not None:
                revealed_lurking_ic.append(redacted)
        _ic_disclosures = {
            str(ic.get("id")): {
                "level": _ic_detection_level(ic),
                "type": _ic_display_type(ic),
                "rating": ic.get("rating"),
            }
            for ic in [*(state.get("active_ic") or []), *(state.get("lurking_ic") or [])]
            if isinstance(ic, dict) and ic.get("id")
        }
        # How many hosts are suspended below this one on the trap-door stack (B34). The player
        # sees the DEPTH (so the UI can show "2 hosts deep") without the GM-only suspended frames.
        state["host_stack_depth"] = len(state.get("host_stack") or [])
        for k in _GM_ONLY_STATE_KEYS:
            state.pop(k, None)
        if revealed_lurking_ic:
            state["revealed_lurking_ic"] = revealed_lurking_ic
        state["located_paydata"] = located_paydata
        state["discovered_trap_doors"] = discovered_trap_doors
        state["discovered_data_bombs"] = discovered_data_bombs
        state["discovered_scrambles"] = discovered_scrambles
        # Named Slave device icons become scan targets only after the decker successfully analyzes
        # the Slave subsystem. Until then, exposing their names would leak host topology.
        if "slave" not in (state.get("analyzed_subsystems") or []):
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
            proj = {k: v for k, v in pend.items()
                if k not in ("ctx", "resume_logon_completed", "resume_count_window",
                     "resume_phase_transition", "acting_init", "acting_count")}
            # If the attacking IC is not yet identified (detection level < 2), mask its identity in
            # the prompt too: attacker_label ("Killer-6") and the raw to-hit roll (dice + TN) would
            # otherwise leak the IC type/rating that active_ic and the event log both redact. Power
            # is kept -- the incoming attack force is legitimately felt, matching the redacted event
            # text -- so the player can still size their Hacking-Pool defense against an Unknown IC.
            atk_ic = next(
                (ic for ic in (state.get("active_ic") or [])
                 if isinstance(ic, dict) and ic.get("id") == pend.get("ic_id")),
                None,
            )
            if atk_ic is not None and _ic_detection_level(atk_ic) < 3:
                level = _ic_detection_level(atk_ic)
                proj["attacker_label"] = (
                    str(atk_ic.get("type") or "IC") if level >= 2 else "Unknown IC"
                )
                proj.pop("to_hit_roll", None)
            state["pending_defense"] = proj
        if isinstance(state.get("active_ic"), list):
            redacted = [_redact_ic(ic) for ic in state["active_ic"] if isinstance(ic, dict)]
            state["active_ic"] = [ic for ic in redacted if ic is not None]
        if isinstance(state.get("event_log"), list):
            # IC the decker has detected but not yet identified (detection level < 2): their name
            # must read as "Unknown IC" in the log, matching the redacted chip. active_ic is already
            # redacted above, so its detection_level fields drive which IC names to mask.
            # Drop GM-only events (e.g. surreptitious reactive-IC activity the decker
            # has not yet detected) so the log never betrays a hidden IC's presence, and
            # scrub the running security tally from the survivors (the decker only learns
            # its tally via Analyze Security -- see _redact_event_tally).
            projected_events = [
                _redact_event_tally(_redact_system_action_event(e, state))
                for e in state["event_log"]
                if not (isinstance(e, dict) and e.get("gm_only"))
            ]
            state["event_log"] = [
                _redact_event_ic(event, _ic_disclosures)
                for event in projected_events
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
# that has scanned the PC (see _enemy_scan_pc) focuses the weakest of these it can attack. Derived
# from _ATTRIBUTE_ATTACK (title-cased program name) so it can never drift from the single crippler
# map (poison->Bod, restrict->Evasion, reveal->Masking).
_ATTR_CRIPPLER = {
    attr: str(m["program"]).title()
    for attr, m in _ATTRIBUTE_ATTACK.items()
    if m["program"]
}


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
    Sensor Test or Analyze raises ``detection_level``. Trace is a hybrid exception: it is
    type-known at level 2 while visibly running its Hunt Cycle, but its rating remains hidden.
    ``analyzed`` forces a full reveal.
    """
    level = ic.get("detection_level")
    if level is None:
        catalog = rules.IC_CATALOG.get(_canonical_ic_type(ic.get("type", "")), {})
        if catalog.get("subtype") == "trace":
            level = 2
        else:
            level = 0 if catalog.get("ic_type") == "reactive" else 1
    if ic.get("analyzed"):
        level = 3
    return level


def _redact_ic(ic: dict) -> dict | None:
    """Player view of an active IC. Returns None when the decker is unaware of it.

    Graduated reveal (vr2 reactive-IC detection, line 409, + #9):
      0 -> unaware: hidden entirely (None)        2 -> type known, rating hidden
      1 -> presence known ("Unknown IC")          3 -> type + rating revealed
    Reactive IC running surreptitiously (Probe, Data Bomb, Scramble, Worm) stay invisible until
    detected, so nothing leaks that they are operating. Trace is visible during its Hunt Cycle at
    level 2 (type and phase, not rating). A trapped icon only reveals that it is trapped once the
    decker Analyzes it (Analyze IC) or crashes it -- passive detection never exposes the trap.
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
    common_fields = {
        "id", "status", "boxes", "initiative", "suppressed", "suppression_released",
        "evaded", "located", "revealed", "cluster_id", "cluster_size",
    }
    identity_fields = {"type", "category"}
    full_fields = identity_fields | {
        "rating", "options", "expert", "shield", "shift", "cascading", "mode", "variant",
        "threat_rating", "construct_components", "construct_defenses", "trace_phase",
        "trace_locate_remaining",
    }
    allowed = common_fields | (full_fields if level >= 3 else identity_fields if level >= 2 else set())
    out = {key: value for key, value in ic.items() if key in allowed}
    # Trap IC is a HIDDEN layer (vr2 L695): the decker learns an icon is trapped only by ANALYZING
    # it (Analyze IC, which sets ``analyzed``) or by crashing it (the trap springs). Passive sensor
    # detection reveals the surface IC but NOT that it conceals a trap.
    if ic.get("trap_hidden") and (ic.get("analyzed") or ic.get("status") == "crashed"):
        out["trap_hidden"] = True
    if level == 1:
        out["type"] = "Unknown IC"
        out["rating"] = None
    elif level >= 2:
        out["type"] = _ic_display_type(ic)
        if _canonical_ic_type(ic.get("type", "")) == "Worm":
            variant = _worm_variant(ic.get("variant"))
            if variant is not None:
                out["variant"] = variant
    if level == 2:
        out["rating"] = None  # type known, exact rating still unknown
        if ic.get("observed_type") and not ic.get("analyzed"):
            out.pop("category", None)
        if _ic_is_trace(ic):
            out["trace_phase"] = ic.get("trace_phase", "hunt")
    # Threat class (white/gray/black) is part of an IC's identity: withhold it until the type is
    # known (level >= 2), so an un-analysed IC never leaks its class through the chip badge/colour.
    if level < 2:
        out["category"] = None
    out["detection_level"] = level
    return out


# Action cost (Free/Simple/Complex) per action_type, from the vr2 System Operations table.
# _spend_pass_action uses this map to enforce 2 Simple OR 1 Complex + 1 Free per pass.
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
    "trap_door_enter": "Complex",
    "steamroller": "Simple", "slow": "Simple", "decompress_file": "Complex",
    "dinab": "Free",                          # DINAB: a Free action runs one program autonomously
    # Combat maneuvers (vr2 L1982) are Simple Actions.
    "evade_detection": "Simple", "parry_attack": "Simple", "position_attack": "Simple",
})

# Operation -> the utility program it runs (from the vr2 System Operations table). Used to auto-fire
# a lurking Tar Baby / Tar Pit against whatever utility the decker just ran (app-as-GM; there is no
# human GM to pick the target program). Same snake_case keying as _ACTION_COST.
_ACTION_UTILITY = {op["name"].lower().replace(" ", "_"): op["utility"] for op in rules.SYSTEM_OPERATIONS}
_ACTION_UTILITY["analyze_subsystem"] = "Analyze"
# Redirect Datatrail runs the Camo utility (vr2_rules.md L1600/L2294): Camo reduces the operation's
# Security Test TN by its rating. Wiring it here also makes a One-Shot Camo spend a copy when the
# decker runs the redirect, and auto-fires any lurking Tar against the Camo program.
_ACTION_UTILITY["redirect_datatrail"] = "Camo"

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
    cfg = normalize_host_config(host.config_json) or {}
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
    program_sizes = {str(k): int(v) for k, v in (decker.get("program_sizes") or {}).items()}
    squeeze_keys = {
        str(k) for k, v in (decker.get("program_options") or {}).items()
        if isinstance(v, dict) and v.get("squeeze")
    } | {
        str(p.get("name", "")) for p in (decker.get("storage_programs") or [])
        if isinstance(p, dict) and p.get("name") and p.get("squeezed")
    }
    active_counts = {
        str(key): max(0, int(count or 0))
        for key, count in (decker.get("one_shot_active") or {}).items()
        if int(count or 0) > 0
    }
    active_backup_mp = sum(
        ((program_sizes.get(str(key), 0) + 1) // 2 if str(key) in squeeze_keys
         else program_sizes.get(str(key), 0))
        for key, rating in (decker.get("utilities") or {}).items()
        if int(rating or 0) > 0
        and not (decker.get("program_options") or {}).get(str(key), {}).get("one_shot")
    )
    stored_program_mp = sum(
        ((int(p.get("size", 0) or 0) + 1) // 2 if p.get("squeezed")
         else int(p.get("size", 0) or 0))
        for p in (decker.get("storage_programs") or []) if isinstance(p, dict)
    )
    raw_storage_free_mp = decker.get("storage_free_mp", -1)
    storage_free_mp = int(raw_storage_free_mp) if raw_storage_free_mp is not None else -1
    storage_capacity_mp = (
        active_backup_mp + stored_program_mp + storage_free_mp
        if storage_free_mp >= 0 else -1
    )

    # Pre-placed Worm IC configured in the host designer (config_json["worms"]). A Worm booby-traps
    # a subsystem, so it lurks from the moment the decker logs on. Each carries its variant:
    #   deathworm -> once it INFECTS the MPCP: ongoing cybercombat-TN penalty (persists across runs)
    #   tapeworm  -> once it INFECTS the MPCP: erases carried paydata at every run end
    # Infection is the GATE for every variant -- a worm does nothing until it compromises the MPCP.
    # (Dataworm is narrative-only and is not authored here.)
    lurking_worms = []
    for _w in (cfg.get("worms") or []):
        if not isinstance(_w, dict):
            continue
        variant = _worm_variant(_w.get("variant"))
        if variant is None:
            continue
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
        v = _worm_variant(_inf.get("variant"))
        if v is None:
            continue
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
        # stay redacted from players until entered -- see _serialize_run).
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
        "storage_free_mp": storage_free_mp,
        "storage_capacity_mp": storage_capacity_mp,
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
        "program_sizes": program_sizes,
        "one_shot_active": active_counts,
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
        "squeeze_keys": sorted(squeeze_keys),
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


_HP_INELIGIBLE_ACTIONS = {"swap_memory", "unload_program", "decompress_file", "dinab"}


def _assert_hp_eligible(action_type: str, requested: int) -> None:
    """Reject Hacking Pool allocations on actions that make no player-controlled test."""
    if requested > 0 and action_type in _HP_INELIGIBLE_ACTIONS:
        raise HTTPException(400, f"Hacking Pool cannot be used for {_action_label(action_type)}")


def _assert_logged_on(state: dict) -> None:
    """Reject Matrix operations until Logon to Host succeeds."""
    if not state.get("logon_complete"):
        raise HTTPException(400, "Logon to Host must succeed before performing Matrix operations")


_MAX_EVENT_LOG_ENTRIES = 750


def _append_event(state: dict, event: dict) -> None:
    """Append a timestamped event to the state log.

    Each event is stamped with the INITIATIVE COUNT of whoever is acting (``state['_acting_init']``,
    set to the decker's Matrix initiative while a player action resolves and to each IC/enemy's own
    initiative while the app-as-GM driver runs it). The count drops by 10 each pass, so an actor
    with Initiative 26 is stamped i26, i16, then i6 across its three passes."""
    event["turn"] = state.get("current_turn", 1)
    if "init" not in event:
        acting_count = state.get("_acting_count")
        acting_init = state.get("_acting_init")
        if acting_count is not None:
            event["init"] = max(0, int(acting_count))
        elif acting_init is not None:
            current_pass = max(1, int(state.get("current_pass", 1) or 1))
            event["init"] = max(0, int(acting_init) - (10 * (current_pass - 1)))
    event["ts"] = datetime.now(UTC).isoformat()
    event_log = state["event_log"]
    event_log.append(event)
    if len(event_log) > _MAX_EVENT_LOG_ENTRIES:
        del event_log[:-_MAX_EVENT_LOG_ENTRIES]


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
# a fresh copy from storage to use it again. Tar Baby wipes every active copy and leaves storage
# untouched; a successful Tar Pit MPCP test wipes every on-deck copy, preventing reload this run.
#
# Active copy counts are carried in ``state["one_shot_active"]``; ``storage_programs`` contains one
# entry per stored copy. Spending destroys one active copy. Swap Memory moves one surviving copy
# between the two pools. Legacy runs without the count map retain the former single-copy behavior.
#
# Consumption is wired at each execution boundary: generic System Test utilities after their test,
# named combat/recovery utilities after their effect, Cloak/Lock-On after a maneuver test, and Camo
# after each Trace hunt test. Recovery/defensive utilities (medic, restore, disinfect, defuse,
# steamroller, slow, shield)
#     have an ``_effective_<util>`` gate, so a spent one-shot is HARD-blocked until reloaded.
#     Offensive utilities (attack, poison, restrict, reveal, black_hammer, killjoy) have no such
#     gate -- consuming them records the spend, emits the player-visible event, shrinks live icon
#     bandwidth and makes Hog skip the slot, but does NOT hard-refuse the next use (a SOFT gate).
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
    active_counts = state.get("one_shot_active")
    if isinstance(active_counts, dict):
        remaining = max(0, int(active_counts.get(key, 0) or 0))
        if remaining <= 0:
            return
        remaining -= 1
        active_counts[key] = remaining
        if remaining > 0:
            pd.pop(key, None)
        else:
            decker.setdefault("utilities", {})[key] = 0
            pd.pop(key, None)
        suffix = (
            f" {remaining} active cop{'y remains' if remaining == 1 else 'ies remain'}."
            if remaining else " Load another stored copy to use it again."
        )
        _append_event(state, {
            "type": "one_shot_spent", "utility": key, "copies_remaining": remaining,
            "description": f"{_action_label(key)} spent one active One-Shot copy." + suffix,
        })
        return
    if int(pd.get(key, 0) or 0) >= base:
        return  # this copy is already spent -- do not double-emit the event
    pd[key] = base  # effective rating -> 0: "executes ONCE then vanishes from active memory"
    _append_event(state, {
        "type": "one_shot_spent",
        "utility": key,
        "description": f"{_action_label(key)} spent one active One-Shot copy.",
    })


def _wipe_one_shot(state: dict, decker: dict, util_name: str) -> None:
    """Successful Tar Pit corruption: destroy every active and storage One-Shot copy.

    Removes all active copies, flags the program in ``one_shot_wiped`` so Swap Memory refuses to
    reload it, and drops every matching storage copy. No-op for a non-One-Shot program.
    """
    key = _normalize_util_name(util_name)
    if not _is_one_shot(decker, key):
        return
    _release_wiped_program_storage(state, decker, key)
    decker.setdefault("utilities", {})[key] = 0
    state.setdefault("program_damage", {}).pop(key, None)
    active_counts = state.get("one_shot_active")
    if isinstance(active_counts, dict):
        active_counts[key] = 0
    wiped = state.setdefault("one_shot_wiped", [])
    if key not in wiped:
        wiped.append(key)
    _append_event(state, {
        "type": "one_shot_wiped",
        "utility": key,
        "description": f"Tar Pit corrupted all copies of the One-Shot {_action_label(key)} on the deck.",
    })


def _release_wiped_program_storage(state: dict, decker: dict, key: str) -> None:
    """Remove a program's retained backup and storage copies, returning their tracked Mp."""
    storage = state.get("storage_programs")
    removed = []
    if isinstance(storage, list):
        removed = [p for p in storage if _normalize_util_name(p.get("name", "")) == key]
        state["storage_programs"] = [p for p in storage if p not in removed]
    free = state.get("storage_free_mp", -1)
    if not isinstance(free, int) or free < 0:
        return
    released = sum(
        ((max(0, int(p.get("size", 0) or 0)) + 1) // 2 if p.get("squeezed")
         else max(0, int(p.get("size", 0) or 0)))
        for p in removed
    )
    if (int((decker.get("utilities") or {}).get(key, 0) or 0) > 0
            and not _is_one_shot(decker, key)):
        full_size = max(0, int((state.get("program_sizes") or {}).get(key, 0) or 0))
        released += ((full_size + 1) // 2 if key in (state.get("squeeze_keys") or [])
                 else full_size)
    state["storage_free_mp"] = free + released


def _wipe_all_copies(state: dict, decker: dict, util_name: str) -> None:
    """Tar Pit corruption (vr2_rules.md L540-542 + user ruling 2026-07-10): a Tar Pit that wins its
    MPCP test injects viral code that corrupts EVERY copy of the program -- in active AND storage
    memory. For the rest of the run (until jack out) the program is GONE: it cannot be reloaded via
    Swap Memory. Unlike ``_wipe_one_shot`` this applies to ANY program, not just One-Shots. Removes
    every active copy, flags it in ``one_shot_wiped`` (the shared 'cannot reload' list Swap Memory
    honours) and drops every storage copy."""
    # A One-Shot program already has its own corrupt-all-copies path (event + list + storage
    # removal); reuse it so one-shots keep emitting the one_shot_wiped event. For any OTHER
    # program the call below no-ops and the generic wipe here does the work.
    _wipe_one_shot(state, decker, util_name)
    key = _normalize_util_name(util_name)
    _release_wiped_program_storage(state, decker, key)
    decker.setdefault("utilities", {})[key] = 0
    state.setdefault("program_damage", {}).pop(key, None)
    active_counts = state.get("one_shot_active")
    if isinstance(active_counts, dict):
        active_counts[key] = 0
    wiped = state.setdefault("one_shot_wiped", [])
    if key not in wiped:
        wiped.append(key)


def _move_active_copy_to_storage(state: dict, decker: dict, key: str) -> None:
    """Expose a regular active program's retained deck copy after it leaves active memory."""
    rating = int((decker.get("utilities") or {}).get(key, 0) or 0)
    if rating <= 0 or _is_one_shot(decker, key):
        return
    storage = state.setdefault("storage_programs", [])
    storage.append({
        "name": key,
        "rating": rating,
        "size": max(0, int((state.get("program_sizes") or {}).get(key, 0) or 0)),
        "squeezed": key in (state.get("squeeze_keys") or []),
    })


def _wipe_active_copies(state: dict, decker: dict, util_name: str) -> None:
    """Remove every active instance; only regular programs retain a storage copy."""
    key = _normalize_util_name(util_name)
    _move_active_copy_to_storage(state, decker, key)
    decker.setdefault("utilities", {})[key] = 0
    state.setdefault("program_damage", {}).pop(key, None)
    active_counts = state.get("one_shot_active")
    if isinstance(active_counts, dict):
        active_counts[key] = 0


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
    pretty = _action_label(key)
    if key in (state.get("one_shot_wiped") or []):
        raise HTTPException(
            400,
            f"One-Shot {pretty}: Tar IC corrupted every copy -- it cannot be used again this run.",
        )
    active_counts = state.get("one_shot_active")
    if isinstance(active_counts, dict):
        spent = int(active_counts.get(key, 0) or 0) <= 0
    else:
        spent = int((state.get("program_damage") or {}).get(key, 0) or 0) >= base
    if spent:
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


def _complete_logon(state: dict, decker: dict, det_factor: int) -> None:
    """Emit the logon-success event and refresh the entry budget (logon is the ENTRY step, not one
    of Round 1's actions -- see _reset_pass_budget). Shared by the direct logon path (perform_action)
    and the resume-after-defense-pause path (_advance_npc_count_window) so the two cannot drift."""
    state["logon_complete"] = True
    _append_event(state, {
        "type": "logon",
        "description": f"Logged on to host successfully. Detection Factor: {det_factor}.",
    })
    _reset_pass_budget(state)
    _run_reactive_activation_sensor_checks(state, decker)


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
    # decides when to end the phase (End Turn), which advances the shared initiative clock through
    # every hostile count before the decker's next count. Report whether another pass remains.
    cur, total = state.get("current_pass", 1), state.get("initiative_passes", 1)
    if cur >= total:
        raise HTTPException(
            400, f"No action points left and all {total} Turn"
            f"{'s are' if total != 1 else ' is'} spent this "
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
    "attack": "attack",
}


def _action_program_key(action_type: str) -> str | None:
    """Return the utility program key a manual action runs, or None if it uses no carried program."""
    if action_type in _ACTION_PROGRAM_KEY_DIRECT:
        return _ACTION_PROGRAM_KEY_DIRECT[action_type]
    util = _ACTION_UTILITY.get(action_type)
    if not util:
        return None
    return util.strip().lower().replace(" ", "_").replace("/", "_")


def _effective_program_rating(decker: dict, state: dict, key: str) -> int:
    """Return a loaded program's current rating after run-time wear."""
    key = _normalize_util_name(key)
    if not key:
        return 0
    base = int((decker.get("utilities") or {}).get(key, 0) or 0)
    worn = int((state.get("program_damage") or {}).get(key, 0) or 0)
    return max(0, base - worn)


def _effective_action_utility(decker: dict, state: dict, action_type: str,
                              target_program: str = "") -> int:
    """Return the effective loaded utility rating used by a host System Test."""
    key = _normalize_util_name(target_program) if action_type == "dinab" else _action_program_key(action_type)
    return _effective_program_rating(decker, state, key or "")


def _assert_not_dinab_locked(state: dict, prog_key: str | None) -> None:
    """Reject a MANUAL use of ``prog_key`` if DINAB already ran that program this pass (vr2: a
    program run autonomously by DINAB cannot also be used by the decker on the same pass). No-op
    for legacy runs (no action budget) or actions that run no carried program."""
    if not prog_key or "pass_action_points" not in state:
        return
    if state.get("dinab_prog_this_pass") == prog_key:
        pretty = _action_label(prog_key)
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
            normalized = _normalized_ic_payload(ev)
            ic_type   = normalized["type"]
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
                    variant = _worm_variant(ev.get("variant"))
                    if variant is None:
                        continue
                    lurker["variant"] = variant
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
                is_trace = rules.IC_CATALOG.get(ic_type, {}).get("subtype") == "trace"
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
                    "mode": normalized.get("mode"),
                    **({"trace_phase": "hunt", "detection_level": 2} if is_trace else {}),
                })
                # Reactive IC do not betray themselves -- their activation is GM-only until a
                # Sensor Test / Analyze detects them (vr2 line 409). Trace is the hybrid exception:
                # it visibly hunts and can be attacked, so its type/phase are public immediately.
                is_reactive = (
                    rules.IC_CATALOG.get(ic_type, {}).get("ic_type") == "reactive"
                    and not is_trace
                )
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
            hidden = _normalized_ic_payload({
                "ic_type": ev.get("hidden_ic_type", "Blaster"),
                "rating": ev.get("hidden_ic_rating", 6),
                "options": ev.get("hidden_ic_options", []),
                "cascading": ev.get("hidden_ic_cascading", False),
                "mode": ev.get("hidden_ic_mode"),
            }, default_type="Blaster")
            hidden_type    = hidden["type"]
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
                "trap_hidden": hidden,
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
            # One icon/Condition Monitor. Components supply effects; host SV + Threat supplies dice.
            threat_rating = max(0, int(ev.get("threat_rating", 0) or 0))
            components = [
                _normalized_ic_payload(component)
                for component in (ev.get("components", []) or [])
                if isinstance(component, dict)
            ]
            defenses      = ev.get("defenses", [])
            ic_id      = f"ic_{uuid.uuid4().hex[:8]}"
            initiative_rating = min((c["rating"] for c in components), default=1)
            initiative = eng.ic_initiative_roll(initiative_rating, security_code)
            comp_names = ", ".join(f"{c['type']}-{c['rating']}" for c in components)
            state["active_ic"].append({
                "id": ic_id,
                "type": "Construct",
                "rating": threat_rating,
                "threat_rating": threat_rating,
                "initiative_rating": initiative_rating,
                "category": "construct",
                "boxes": 0,
                "suppressed": False,
                "initiative": initiative,
                "status": "active",
                "hunt_cycle_successes": 0,
                "construct_components": components,
                "construct_defenses": defenses,
                "options": defenses,
                "expert": ev.get("expert"),
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
            components = [
                _normalized_ic_payload(component)
                for component in (ev.get("components", []) or [])
                if isinstance(component, dict)
            ]
            cluster_id = f"cluster_{uuid.uuid4().hex[:8]}"
            for comp in components:
                comp_type   = comp["type"]
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
                    "mode": comp.get("mode"),
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
            # Bouncer (vr2 L300): schedule the upgrade for the next Combat Turn. The payload stays
            # GM-only; a separate secret Sensor Test may warn the decker that security is rising.
            old_code  = state.get("host_security_code", security_code)
            old_value = state.get("host_security_value", 0)
            new_code  = ev.get("new_security_code") or old_code
            _nv       = ev.get("new_security_value")
            new_value = int(_nv) if _nv is not None else old_value
            state["pending_bouncer"] = {
                "old_security_code": old_code,
                "old_security_value": old_value,
                "new_security_code": new_code,
                "new_security_value": new_value,
                "complete_turn": state.get("current_turn", 1) + 1,
                "sensor_checked": False,
            }
            events.append({
                "type": "bouncer_scheduled", "gm_only": True,
                "old_security_code": old_code,
                "old_security_value": old_value,
                "new_security_code": new_code,
                "new_security_value": new_value,
                "description": (
                    f"(GM) Bouncer triggered -- host security will harden from {old_code} "
                    f"{old_value} to {new_code} {new_value} next Combat Turn."
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
                        f"(GM) HOST SHUTDOWN SEQUENCE started -- {turns} Round"
                        f"{'s' if turns != 1 else ''}, final "
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


def _construct_components(ic: dict) -> list[dict]:
    """Return normalized component IC programs from a Construct's single icon."""
    out: list[dict] = []
    for raw in (ic.get("construct_components") or []):
        if not isinstance(raw, dict):
            continue
        ic_type = str(raw.get("type") or raw.get("ic_type") or "").strip()
        if ic_type:
            out.append({**raw, "type": ic_type, "rating": max(1, int(raw.get("rating", 1) or 1))})
    return out


def _construct_component(ic: dict) -> dict:
    """Choose one available proactive component for an app-controlled Construct action."""
    components = _construct_components(ic)
    return next(
        (
            component for component in components
            if rules.IC_CATALOG.get(_canonical_ic_type(component["type"]), {}).get("ic_type")
            == "proactive"
        ),
        components[0] if components else {"type": "Killer", "rating": 1},
    )


def _ic_test_pool(ic: dict, security_value: int, *, defense: bool) -> int:
    """IC dice pool, with Construct Threat dice added to the host Security Value base."""
    threat = max(0, int(ic.get("threat_rating", 0) or 0)) if ic.get("type") == "Construct" else 0
    expert = (
        _ic_expert(ic, "defense") - _ic_expert(ic, "offense")
        if defense else _ic_expert(ic, "offense") - _ic_expert(ic, "defense")
    )
    return max(1, security_value + threat + expert)


def _combat_target_status(target: dict | None = None, *, ic_state: dict | None = None) -> str:
    """Cybercombat to-hit column for an icon the PC is ATTACKING (vr2 L2028).

    The COMBAT_TN table keys off the TARGET icon's status, not the attacker's: "any icon logged on
    with a valid passcode is Legitimate; all others are Intruding." IC programs and host security
    deckers are legitimate residents of the host, so the PC always hits them on the Legitimate
    column. (A target explicitly flagged ``intruding`` -- e.g. a rival runner sharing the host --
    uses the Intruding column -- a PC's Invalidate Passcode sets ``intruding`` on the affected IC /
    enemy deckers so the PC then hits those targets on the Intruding column.)

    ``ic_state`` is passed ONLY at IC target sites: a whole-system Invalidate Passcode latches
    ``state['passcodes_invalidated']``, which flips EVERY host IC (active, lurking, or activated
    later) to the Intruding column even if it was not individually flagged when the table was
    erased. It is never passed for enemy-decker targets, so a rival runner is unaffected."""
    if (target or {}).get("intruding"):
        return "intruding"
    if ic_state and ic_state.get("passcodes_invalidated"):
        return "intruding"
    return "legitimate"


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
        # Erase the ENTIRE passcode table: flip every host IC on the system -- active AND still
        # lurking -- and latch a flag so any IC that activates LATER is also an intruder (the table
        # is gone, so nothing on the host can ever present a valid passcode again). Enemy deckers
        # (rival runners with their own passcodes) still flip individually, as before.
        state["passcodes_invalidated"] = True
        for ic in state.get("active_ic", []):
            _flip_ic(ic)
        for ic in state.get("lurking_ic", []):
            if isinstance(ic, dict) and not ic.get("intruding"):
                ic["intruding"] = True
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


def _suppression_overflow(state: dict, decker: dict) -> int:
    """Number of active suppressions that no longer fit above Detection Factor's floor of 1."""
    capacity = max(0, _base_detection_factor(state, decker) - 1)
    return max(0, _suppressed_count(state) - capacity)


def _assert_suppression_capacity(state: dict, decker: dict) -> None:
    overflow = _suppression_overflow(state, decker)
    if overflow:
        raise HTTPException(
            409,
            f"Masking damage reduced your Detection Factor. You can no longer maintain all "
            f"suppressed IC; release {overflow} suppression{'s' if overflow != 1 else ''} "
            "before continuing.",
        )


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
            base = max(1, math.ceil(base * mult.get(name, 1.0)))
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


def _shield_parry(
    state: dict,
    decker: dict,
    *,
    attacker_skill: int,
    context: str,
    source_ic: dict | None = None,
) -> int:
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
    event = {
        "type": "shield_parry",
        "context": context,
        "shield_rating": rating,
        "shield_remaining": remaining,
        "successes": succ,
        "roll": res["roll"],
        "description": (
            f"Shield-{rating} contributes {succ} defense success"
            f"{'' if succ == 1 else 'es'} (TN {res['tn']}). "
            + (f"Shield worn to {remaining} -- reload via Swap Memory."
               if remaining > 0 else
               "Shield burned out -- reload a fresh copy via Swap Memory.")
        ),
    }
    if source_ic is not None:
        event.update({
            "ic_id": source_ic.get("id"),
            "ic_type": source_ic.get("type"),
            "ic_rating": source_ic.get("rating"),
        })
        event["description"] = event["description"].replace(
            f" (TN {res['tn']}).",
            f" against {context} (TN {res['tn']}).",
        )
    _append_event(state, event)
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


def _decker_effective_initiative(state: dict) -> int:
    """Current player initiative after cumulative wound penalties."""
    return max(0, int(state.get("decker_initiative", 0) or 0) - _decker_wound_mod(state))


def _decker_action_count(state: dict) -> int:
    """Player's count on the shared initiative clock for the current action pass."""
    current_pass = max(1, int(state.get("current_pass", 1) or 1))
    return max(0, _decker_effective_initiative(state) - 10 * (current_pass - 1))


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
    event = {"type": "armor_wear", "armor_remaining": remaining}
    if gm_only:
        event["gm_only"] = True
        event["description"] = (f"{actor or 'Security decker'} Armor worn to {remaining}"
                                + (" -- burned out." if remaining == 0 else " by the hit."))
    else:
        event["description"] = (f"Armor worn to {remaining} by the hit"
                                + (" -- burned out; Swap Memory a fresh copy." if remaining == 0
                                   else " -- Swap Memory to restore full rating."))
    _append_event(state, event)


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
                 hacking_pool_dice: int = 0, via_dinab: bool = False) -> None:
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
    utility_rating = pool_override if pool_override is not None else _effective_medic(decker, state)
    if utility_rating <= 0:
        _append_event(state, {
            "type": "medic_heal", "healed": 0, "persona_boxes": boxes, "wound_level": wound,
            "description": ("Medic offline (worn out or not loaded) -- reload a fresh copy via "
                            "Swap Memory before it can heal the icon."),
        })
        return
    pool = utility_rating + (0 if pool_override is not None else max(0, hacking_pool_dice))
    res, wound, healed = _medic_heal_core(cm, state, rating=pool)
    remaining_rating = _effective_medic(decker, state)   # Medic program rating AFTER this use's wear
    remaining_dmg = cm["persona_boxes"]
    _append_event(state, {
        "type": "medic_heal",
        "wound_level": wound,
        "healed": healed,
        "persona_boxes": remaining_dmg,
        "medic_rating": utility_rating,
        "medic_remaining": remaining_rating,
        "decker_roll": res["roll"],
        "description": (
            f"{label}-{utility_rating} treats the {wound.lower()} icon wound with {pool} dice "
            f"(TN {res['tn']}): "
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
        desc = f"{name} attempts to repair damage to their icon, but fails."
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
                        "their nerve breaks. They jack out, abandoning the hunt."
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
    target_decker: dict | None = None,
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
    overflow_before = (
        _suppression_overflow(state, target_decker)
        if target_kind == "pc" and attr == "masking" and target_decker is not None
        else 0
    )
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
    if (target_kind == "pc" and attr == "masking" and target_decker is not None
            and (applied + chip_applied) > 0):
        overflow_after = _suppression_overflow(state, target_decker)
        if overflow_after > overflow_before:
            _append_event(state, {
                "type": "suppression_overflow",
                "description": (
                    "Masking damage reduced your Detection Factor. You can no longer maintain "
                    f"all suppressed IC; release {overflow_after} "
                    f"suppression{'s' if overflow_after != 1 else ''} before continuing."
                ),
            })
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
                   pool_override: int | None = None, hacking_pool_dice: int = 0,
                   via_dinab: bool = False) -> None:
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

    utility_rating = pool_override if pool_override is not None else _effective_restore(decker, state)
    if utility_rating <= 0:
        _append_event(state, {
            "type": "restore_repair", "repaired": 0, "attribute": _select_restore_attr(cm, target),
            "description": ("Restore offline (crashed or not loaded) -- reload a fresh copy via "
                            "Swap Memory before it can repair attributes."),
        })
        return

    pool = utility_rating + (0 if pool_override is not None else max(0, hacking_pool_dice))
    res, attr, points, floor = _restore_repair_core(cm, rating=pool, target=target)
    pd = cm["persona_damage"]
    now = max(1, int(decker.get(attr, 4) or 4) - int(pd.get(attr, 0) or 0))
    label = "DINAB Restore" if via_dinab else "Restore"
    _append_event(state, {
        "type": "restore_repair",
        "attribute": attr,
        "repaired": points,
        "restore_rating": utility_rating,
        "causing_rating": res["causing_rating"],
        "attribute_damage": pd[attr],
        "decker_roll": res["roll"],
        "description": (
            f"{label}-{utility_rating} repairs {attr.title()} with {pool} dice "
            f"(TN {res['tn']} = causing crippler rating): "
            f"{res['successes']} success{'' if res['successes'] == 1 else 'es'} -> "
            f"{points} point{'' if points == 1 else 's'} restored. "
            f"{attr.title()} now {now} ({pd[attr]} damage remaining"
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
        desc = f"{name} repairs damage to their {attr.title()}."
    else:
        desc = f"{name} attempts to repair damage to their {attr.title()}, but fails."
    _append_event(state, {
        "type": "enemy_decker", "outcome": "restore", "enemy_id": enemy.get("id"),
        "description": desc,
    })


def _effective_disinfect(decker: dict, state: dict) -> int:
    """Effective Disinfect rating = the loaded Disinfect utility minus any crash wear in
    ``state['program_damage']['disinfect']``. Like Restore, Disinfect does NOT self-degrade per
    use (no degradation in the rule), so only a crash (e.g. Tar Baby / Hog) lowers it, and a Swap
    Memory reload restores it to full. ``<= 0`` means the Disinfect is unloaded or crashed, so it
    provides no target-number reduction; the decker may still attempt the active operation."""
    base = (decker.get("utilities") or {}).get("disinfect", 0) or 0
    worn = (state.get("program_damage") or {}).get("disinfect", 0)
    return max(0, base - worn)


def _apply_disinfect(state: dict, decker: dict, *, subsystem: str, subsystem_rating: int,
                     decker_pool: int, sec_value: int | None = None,
                     det_factor: int | None = None,
                     target_ic_id: str = "") -> None:
    """Resolve an active Disinfect operation (vr2, Complex Action): a System Test against the
    subsystem hosting a worm, the Disinfect utility reducing the TN. On success the targeted Worm
    lurking-IC is DESTROYED and removed -- with NO security-tally increase (this is a Disinfect,
    not a cybercombat crash). On failure the worm may infect the MPCP (the Worm Infection Test,
    against which the carried Disinfect still defends): an infection sets ``mpcp_infected`` /
    ``chip_replacement_required`` (permanent) and removes the worm; otherwise the worm survives
    and stays lurking.

    The targeted Worm's stored subsystem is authoritative for the System Test and event location;
    request subsystem fields are only a legacy fallback for Worms without a location. With no
    lurking Worm the requested subsystem scans clean. Mutates ``state`` in place and always emits
    a player-visible event (``worm_disinfected`` on a clean/failed/destroyed sweep;
    ``worm_resolved`` when a failure infects the MPCP)."""
    rating = _effective_disinfect(decker, state)

    lurking = state.get("lurking_ic", []) or []
    tid = (target_ic_id or "").strip()
    worm = next((ic for ic in lurking
                 if ic.get("type") == "Worm" and (not tid or ic.get("id") == tid)), None)
    if worm is not None:
        worm_subsystem = str(worm.get("subsystem") or subsystem).strip().lower()
        if worm_subsystem in {"access", "control", "index", "files", "slave"}:
            subsystem = worm_subsystem
            subsystem_rating = _subsystem_rating(state, subsystem)

    host_security = int(sec_value if sec_value is not None else state.get("host_security_value", 1))
    effective_df = int(det_factor if det_factor is not None
                       else _effective_detection_factor(state, decker))
    res = eng.disinfect_test(decker_pool=decker_pool, subsystem_rating=subsystem_rating,
                             disinfect_utility=rating, security_value=host_security,
                             det_factor=effective_df)
    tally_applied = _bump_security_tally(state, res["tally_increase"])
    _spend_one_shot(state, decker, "disinfect")
    event_base = {
        "type": "worm_disinfected", "host_system_test": True,
        "action_label": "Disinfect", "subsystem": subsystem,
        "success": res["success"], "net_successes": res["decker_net_successes"],
        "target_number": res["tn"], "decker_roll": res["decker_roll"],
        "host_roll": res["host_roll"], "tally_increase": tally_applied,
        "tally_total": state["security_tally"],
    }
    if worm is None:
        msg = (f"Disinfect-{rating}: no lurking worm \"{tid}\" found."
               if tid else
               f"Disinfect-{rating}: the {subsystem} subsystem scans clean -- no worm found.")
        _append_event(state, {**event_base, "destroyed": False, "description": msg})
        return

    if res["worm_destroyed"]:
        # Destroyed by the Disinfect -- remove the worm. NOT a cybercombat crash: no tally add.
        state["lurking_ic"] = [ic for ic in lurking if ic.get("id") != worm["id"]]
        _append_event(state, {
            **event_base, "destroyed": True,
            "ic_id": worm["id"], "ic_type": "Worm",
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
    # successes (net > 0 infects) -- see eng.worm_attack (vr2_rules.md L548-550 + user ruling).
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
            **event_base, "type": "worm_resolved",
            "ic_id": worm["id"], "ic_type": "Worm",
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
            **event_base, "destroyed": False,
            "ic_id": worm["id"], "ic_type": "Worm",
            "infection_roll": wr["roll"],
            "description": "Disinfect failed -- MPCP not compromised; the worm is still lurking.",
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
    # resident by default -- unless a whole-system Invalidate Passcode erased the host passcode
    # table, which flips it to Intruding), not the PC-attacker's own Intruding status.
    to_hit_tn = rules.COMBAT_TN[sec_code][_combat_target_status(target, ic_state=state)]
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
                f"{res['damage_level']} ({res['total_boxes']}/{res['tar_cm']})."
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
    # A fresh crash is a suppressible immediate query (like any crashed IC / crashed Scramble): the
    # decker may absorb 1 Detection Factor to refund this tally. Register the entry so the /suppress
    # endpoint can act on it afterward.
    sup_id = None
    if applied > 0:
        sup = _register_suppression(
            state, source="tar_crash",
            label=f"Crashed {target['type']}-{ic_rating}", rating=applied)
        sup_id = sup.get("id")
    _append_event(state, {
        "type": "tar_steamrolled", "destroyed": True,
        "ic_id": target["id"], "ic_type": target["type"], "decker_roll": res["to_hit_roll"],
        "suppression_id": sup_id,
        "description": (
            f"{src}-{rating} crashes {target['type']}-{ic_rating} ({res['damage_level']}). "
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
    Reactive IC are immune; a trace IC is vulnerable only while visible during its Hunt Cycle
    (``_trace_is_targetable``). Returns ``(ok, reason)`` -- ``reason`` is the 400 message when
    ``ok`` is False."""
    info = rules.IC_CATALOG.get(_canonical_ic_type(ic.get("type", "")), {})
    if info.get("subtype", "") == "trace":
        if not _trace_is_targetable(ic):
            return False, ("that trace IC has vanished into its location cycle -- only Relocate "
                           "can affect it until the trace completes.")
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
    # vr2 L2028: the to-hit column is the TARGET's status. The target IC uses the Legitimate column
    # by default -- unless a whole-system Invalidate Passcode erased the host passcode table, which
    # flips it (and every host IC) to Intruding -- never the PC-attacker's own status.
    to_hit_tn = rules.COMBAT_TN[sec_code][_combat_target_status(target, ic_state=state)]
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
    if base > 0 and not _is_one_shot(decker, key):
        state.setdefault("program_damage", {})[key] = base
    (state.get("dinab_damage") or {}).pop(key, None)
    _append_event(state, {
        "type": "dinab_crashed", "utility": key,
        "description": "The DINAB attack fumbled and the construct crashed.",
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
                f"The DINAB-driven {_action_label(util)} failed -- its rating drops 1 "
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
            f"{_action_label(key)} has no usable DINAB rating (not DINAB-equipped, "
            "worn out, or crashed -- reload via Swap Memory).")
    if key in state.get("manual_progs_this_pass", []):
        raise HTTPException(
            400,
            f"You already used {_action_label(key)} by hand this pass -- it cannot also "
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
        _spend_one_shot(state, decker, key)
    else:
        _dinab_operate(state, decker, key, eff, subsystem=subsystem,
                       subsystem_rating=subsystem_rating, sec_value=sec_value, det_factor=det_factor)
        _spend_one_shot(state, decker, key)

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
        "type": "dinab_op", "host_system_test": True,
        "action_label": f"DINAB {_action_label(util)}",
        "utility": util, "subsystem": subsystem, "success": test["success"],
        "net_successes": test["decker_net_successes"],
        "target_number": dr.get("tn"),
        "decker_roll": dr, "host_roll": test["host_roll"],
        "tally_increase": applied, "tally_total": state["security_tally"],
        "description": (
            f"DINAB {_action_label(util)}-{eff} runs the {subsystem} subsystem itself -- "
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
        target_status=_combat_target_status(target_ic, ic_state=state),   # IC = Legitimate resident unless passcodes invalidated (vr2 L2028)
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
            "description": (f"DINAB Attack-{eff} crashed {target_ic['type']}-{target_ic['rating']}. "
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
                    f"{_action_label(res['drained'])} -{res['applied']}"
                    f"{' (CRASHED)' if res['crashed'] else ''}.")
        elif res["infected"]:
            desc = f"DINAB Hog-{eff} infects {_enemy_display_name(enemy)} but it has no running program left to drain."
        else:
            desc = f"DINAB Hog-{eff} fails to take hold on {_enemy_display_name(enemy)}."
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
        "id": pd.get("id"),
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
            f"{', key data' if pd.get('is_key') else ''}){comp_note}. "
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
    preexisting_ic_ids = {
        ic.get("id") for ic in state.get("active_ic", []) if ic.get("id")
    }
    test = _auto_null_operation(state, decker)
    dl["turns_left"] = int(dl.get("turns_left", 0)) - 1
    left = max(0, dl["turns_left"])
    net_successes = test.get("decker_net_successes")
    if net_successes is None:
        net_successes = (
            int(test.get("decker_roll", {}).get("successes", 0) or 0)
            - int(test.get("host_roll", {}).get("successes", 0) or 0)
        )
    _append_event(state, {
        "type": "null_operation",
        "host_system_test": True,
        "action_label": "Auto Null Operation",
        "success": test["success"],
        "net_successes": net_successes,
        "target_number": test["decker_roll"].get("tn"),
        "subsystem": "control",
        "decker_roll": test["decker_roll"],
        "host_roll": test["host_roll"],
        "tally_increase": test["tally_increase"],
        "tally_total": state.get("security_tally", 0),
        "file_name": dl.get("file"),
        "turns_left": left,
        "description": (
            f"Download continuing -- {left} turn{'s' if left != 1 else ''} remaining."
            if left > 0 else "Download complete."
        ),
    })
    _run_reactive_security_followup(
        state,
        decker,
        action_type="null_operation",
        utility_rating=_effective_action_utility(decker, state, "null_operation"),
        sec_code=state.get("host_security_code", "Green"),
        det_factor=_effective_detection_factor(state, decker),
        preexisting_ic_ids=preexisting_ic_ids,
    )
    if dl["turns_left"] > 0:
        return
    pd = _paydata_for_target(state, dl.get("file_id") or dl.get("file", ""))
    if pd is not None and pd.get("destroyed"):
        pd = None
    if pd is not None:
        _complete_download(state, decker, pd)
        state["active_download"] = None
    else:
        _corrupt_active_download(state)  # source file gone before the transfer finished


def _squeezed_active_footprint(full_size: int) -> int:
    """Active-memory footprint of a SQUEEZED program held (still compressed) in active memory: half
    its full size, rounded up (vr2 Squeeze). Decompressing it (a Complex Action) restores the full
    footprint, which needs the extra half free -- so a squeezed program lets the decker park it in
    active memory cheaply and pay the rest only when they expand it for use."""
    return (max(0, int(full_size or 0)) + 1) // 2


def _active_memory_used(state: dict, decker: dict) -> int:
    """Total active-memory Mp in use: every usable loaded utility at its full footprint PLUS every
    still-compressed squeezed program at HALF its full footprint (it occupies active memory even
    while unusable). One-shot utilities count once per loaded copy."""
    sizes = state.get("program_sizes") or {}
    utils = decker.get("utilities") or {}
    one_shot_counts = state.get("one_shot_active") or {}
    used = sum(
        int(sizes.get(n, 0) or 0) * (
            max(0, int(one_shot_counts.get(n, 0) or 0)) if n in one_shot_counts else 1)
        for n, r in utils.items() if (r or 0) > 0
    )
    used += sum(_squeezed_active_footprint(int(p.get("size", 0) or 0))
                for p in (state.get("squeezed_active") or []) if isinstance(p, dict))
    return used


def _apply_decompress_program(state: dict, decker: dict, *, target_program: str) -> bool:
    """Decompress a Squeezed program held in active memory (vr2_rules.md L1673: "Cannot be used
    until decompressed -- Complex Action, no test required"). A squeezed program occupies only HALF
    its footprint while compressed; expanding it restores the FULL footprint, so it needs the extra
    half of active memory free (exactly-enough is allowed -- it may max out active memory). If there
    is not room the action is REJECTED (400) and not spent. On success the program moves out of the
    ``squeezed_active`` holding area into ``decker.utilities`` (now usable) at its full size. Returns
    True when a program was expanded (the caller must persist ``decker``); a missing target emits a
    no-op event and returns False (never a crash)."""
    name = (target_program or "").strip().lower()
    squeezed_active = state.setdefault("squeezed_active", [])
    ent = next((p for p in squeezed_active
                if str(p.get("name", "")).strip().lower() == name), None)
    pretty = _action_label(name)
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
    full = int(ent.get("size", 0) or 0)
    cap = int(state.get("active_memory_cap", 0) or 0)
    if cap > 0:
        # Expanding restores the full footprint from the squeezed half -- it needs the extra half
        # free. Exactly-enough is fine (it may max out active memory).
        delta = full - _squeezed_active_footprint(full)
        used = _active_memory_used(state, decker)   # counts THIS program at its squeezed half
        if used + delta > cap:
            raise HTTPException(
                400,
                f"Not enough active memory to decompress {pretty}: expanding to {full} Mp needs "
                f"{delta} more Mp but only {max(0, cap - used)} Mp is free. Swap a program out first."
            )
    squeezed_active.remove(ent)
    utils = decker.setdefault("utilities", {})
    sizes = state.setdefault("program_sizes", {})
    rating = int(ent.get("rating", 0) or 0)
    utils[name] = rating
    sizes[name] = full
    state.setdefault("program_damage", {}).pop(name, None)   # fresh copy -- no accrued damage
    active_counts = state.get("one_shot_active")
    if isinstance(active_counts, dict) and _is_one_shot(decker, name):
        active_counts[name] = int(active_counts.get(name, 0) or 0) + 1
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


def _apply_analyze_host(state: dict, decker_successes: int) -> dict:
    """Analyze Host success handler (vr2 System Operations: Control test, Analyze utility).

    Reveals the host's subsystem ratings. The revealable set is the 5 ACIFS ratings (Access,
    Control, Index, Files, Slave) PLUS the host Security Rating (code + value) -- 6 items in all.
    The raw ACIFS ratings live in GM-only ``host_acifs`` and mirror into the player-visible
    ``host_ratings_revealed`` map in ACIFS order; the Security Rating is gated by the separate
    ``host_security_revealed`` flag (its code/value stay redacted until it flips). USER OVERRIDE of
    RAW: each decker success reveals one item. VM status is not modeled, so the app's six modeled
    items are all revealed at 6+ decker successes rather than RAW's seven-item threshold.

    Let ``successes`` = the decker's rolled successes and ``U`` = number of still-hidden items (hidden ACIFS + security if
    not yet revealed). On a successful test:
    * ``successes >= 6`` OR ``successes >= U`` -> auto-reveal ALL still-hidden items now (no choice to make)
        and clear any banked pending.
    * ``1 <= successes < U`` -> a genuine choice exists: BANK ``host_analyze_pending`` = {credits, turn}
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
    successes = max(0, int(decker_successes))

    if hidden_count == 0:
        state.pop("host_analyze_pending", None)
        _append_event(state, {
            "type": "host_analyzed", "revealed": [],
            "description": "Analyze Host -- all subsystem ratings already known.",
        })
        return {"revealed": [], "pending": 0}

    # Reveal-all: 6+ decker successes, or enough successes to cover every still-hidden item anyway.
    if successes >= 6 or successes >= hidden_count:
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
    credits = max(1, successes)
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
    when the decker rolled fewer successes than there were hidden items); reveals the chosen
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
    decoy_pool = _ic_test_pool(ic, sec_value, defense=False)
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
            f"D6={d6} <= {decoy_succ} -- {ic['type']}-{ic['rating']} hits decoy! "
            f"{decoy_staged} ({decoy_boxes} boxes). "
            f"Decoy: {min(state.get('decoy_hp', 0), 10)}/10"
            + (" -- decoy destroyed." if decoy_destroyed else "")
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
    # Analyzing a file icon reveals its properties to the decker: its true size (Mp) and whether a
    # covering Scramble encrypts it. Mark the scanned file analyzed so the run projection can surface
    # the real size + encryption status -- a mere Locate keeps both hidden ("??? Mp", no lock badge).
    if scope == "files":
        for pd in (state.get("paydata") or []):
            if isinstance(pd, dict) and (
                str(pd.get("id") or "") == want_name or _paydata_matches(pd, want_name)
            ):
                pd["analyzed"] = True
    bomb = None
    for b in (state.get("data_bombs") or []):
        if not isinstance(b, dict) or b.get("discovered"):
            continue
        bscope, bname = _data_bomb_scope_name(b.get("target", ""))
        if bscope != scope:
            continue
        same_target = bname.strip().lower() == wn
        if scope == "files" and not same_target:
            same_target = any(
                _paydata_matches(item, bname) and _paydata_matches(item, want_name)
                for item in (state.get("paydata") or []) if isinstance(item, dict)
            )
        if not slave_generic and not same_target:
            continue
        bomb = b
        break
    icon_label = (
        "Slave device" if slave_generic else
        (_paydata_label(state, want_name) if scope == "files" else want_name or "Slave device")
    )
    # Analyze Icon on a FILE also reveals a file-specific Scramble on that icon -- its presence AND
    # variant (Poison/Exploding), which the decker needs to pick the safe order (for Exploding you
    # must defuse the linked bomb BEFORE you decrypt or crash it). Subsystem-wide Scramble stays an
    # Analyze Subsystem finding.
    if scope == "files":
        scramble = None
        for scr in (state.get("scrambles") or []):
            if not isinstance(scr, dict):
                continue
            tk = str(scr.get("target_key") or "")
            if not tk.startswith("files::file::"):
                continue
            sname = _target_file_name(tk)
            if sname.strip().lower() == wn or any(
                _paydata_matches(item, want_name) and _paydata_matches(item, sname)
                for item in (state.get("paydata") or []) if isinstance(item, dict)
            ):
                scramble = scr
                break
        if scramble is not None:
            already = scramble.get("discovered") and scramble.get("variant_revealed")
            scramble["discovered"] = True
            scramble["variant_revealed"] = True
            if not already:
                is_exploding = scramble.get("variant") == "exploding"
                _append_event(state, {
                    "type": "scramble_analyzed",
                    "subsystem": "files",
                    "variant": scramble.get("variant"),
                    "description": (
                        f"Analyze Icon on \"{icon_label}\" -- "
                        + ("Exploding Scramble IC detected. Defuse its linked data bomb first, then decrypt."
                           if is_exploding else
                           "Poison Scramble IC detected. Decrypt it to reach the data.")
                    ),
                })
    if bomb is not None:
        bomb["discovered"] = True
        _append_event(state, {
            "type": "data_bomb_found",
            "subsystem": scope,
            "description": f"Analyze Icon on \"{icon_label}\" -- data bomb detected. Defuse the bomb before attempting access.",
        })
    else:
        _append_event(state, {
            "type": "data_bomb_clear",
            "subsystem": scope,
            "description": (
                f"Analyze Icon on \"{icon_label}\" -- no data bomb detected on this "
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
                 and (not tgt or _data_bomb_scope_name(b.get("target", ""))[1].strip().lower() == tgt
                      or any(
                          _paydata_matches(item, target_file)
                          and _paydata_matches(item, _data_bomb_scope_name(b.get("target", ""))[1])
                          for item in (state.get("paydata") or []) if isinstance(item, dict)
                      ))), None)
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
        _append_event(state, {
            "type": "data_bomb_defuse", "host_system_test": True,
            "action_label": "Defuse Data Bomb", "outcome": "botched", "success": False,
            "subsystem": subsystem, "net_successes": decker_succ - host_succ,
            "target_number": df["tn"], "decker_roll": df["roll"],
            "host_roll": host_roll, "tally_increase": tally_applied,
            "description": "Defuse Data Bomb botched -- the protected bomb detonates.",
        })
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
            "type": "data_bomb", "host_system_test": True,
            "action_label": "Defuse Data Bomb", "outcome": "defused", "success": True,
            "subsystem": subsystem, "net_successes": decker_succ - host_succ,
            "target_number": df["tn"], "decker_roll": df["roll"],
            "host_roll": host_roll, "tally_increase": tally_applied,
            "description": (
                f"Data bomb on {btarget} defused (opposed Computer Test TN {df['tn']}; "
                f"{decker_succ} vs {host_succ}).{tally_note}"
            ),
        })
        return
    _append_event(state, {
        "type": "data_bomb", "host_system_test": True,
        "action_label": "Defuse Data Bomb", "outcome": "primed", "success": False,
        "subsystem": subsystem, "net_successes": decker_succ - host_succ,
        "target_number": df["tn"], "decker_roll": df["roll"],
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
                 and (_target_file_name(b.get("target", "")).lower() == tgt
                      or any(
                          _paydata_matches(item, target_file)
                          and _paydata_matches(item, _target_file_name(b.get("target", "")))
                          for item in (state.get("paydata") or []) if isinstance(item, dict)
                      ))), None)
    if bomb is None:
        # A Files-subsystem-wide Exploding Scramble's linked bomb triggers on accessing ANY file.
        bomb = next(
            (b for b in armed
             if isinstance(b, dict) and b.get("target") == "files::__entire__"
             and b.get("target") not in safe),
            None,
        )
    if bomb is None:
        return False
    state["data_bombs"] = [b for b in armed if b is not bomb]  # one-shot
    _detonate_data_bomb(state, decker, eff, ic_rating=bomb.get("rating", 6),
                        sec_value=sec_value, sec_code=sec_code,
                        headline=f"Data bomb on {bomb.get('target')}")
    return True


def _trigger_access_subsystem_bomb(state: dict, decker: dict, *, op_label: str) -> bool:
    """An Access Exploding Scramble's linked bomb detonates on a successful ACCESS operation the
    decker did not defuse first -- a graceful logoff (which also covers a trap-door transit) or a
    Validate Passcode (user ruling 2026-07-28). One-shot; returns True if a bomb detonated. Self-
    contained (derives eff / Security Value / code from ``state``) so it can be called from the
    logoff helper and the control-op handler without threading those through."""
    armed = state.get("data_bombs") or []
    safe = set(state.get("defused_bombs") or [])
    bomb = next(
        (b for b in armed
         if isinstance(b, dict) and b.get("target") not in safe
         and _data_bomb_scope_name(b.get("target", ""))[0] == "access"),
        None,
    )
    if bomb is None:
        return False
    state["data_bombs"] = [b for b in armed if b is not bomb]  # one-shot
    eff = _get_decker_effective(decker, state)
    _detonate_data_bomb(
        state, decker, eff, ic_rating=bomb.get("rating", 6),
        sec_value=state.get("host_security_value", 6),
        sec_code=state.get("host_security_code", "Green"),
        headline=f"Access-subsystem data bomb ({op_label})",
    )
    return True


def _apply_scrambled_file_access(state: dict, decker: dict, body: RunActionInput,
                                 scramble: dict) -> None:
    """A Download/Edit ATTEMPT on a file still covered by an undecrypted Scramble IC (vr2). The
    data is encrypted garbage, so the transfer/edit itself is refused -- but the attempt DISCOVERS
    the Scramble (it now rides the file's card, offering Decrypt), and an undefused EXPLODING
    Scramble's linked data bomb DETONATES: the price of grabbing a file blind instead of Analyzing
    it first. A Poison Scramble (no bomb) is simply revealed -- its Poison Test only reacts to a
    cybercombat crash, not to a read. Mutates ``state`` and emits a player-visible event."""
    newly_found = not scramble.get("discovered")
    scramble["discovered"] = True
    # Name the file the decker actually tried to grab (its real name, not the internal id/target key).
    _pd = _paydata_for_target(state, body.target_file or "")
    file_label = str((_pd or {}).get("name") or body.target_file or "the file")
    op = "download" if body.action_type == "download_data" else "edit"
    # An undefused data bomb guarding this file (an Exploding Scramble's linked bomb, or a
    # standalone file bomb) trips on the blind access -- the decker eats the blast, not the data.
    bomb = _armed_bomb_on_file(state, scramble)
    detonated = False
    if bomb is not None:
        scramble["variant_revealed"] = True   # the blast reveals it was an Exploding Scramble
        state["data_bombs"] = [b for b in (state.get("data_bombs") or []) if b is not bomb]
        eff = _get_decker_effective(decker, state)
        _detonate_data_bomb(
            state, decker, eff,
            ic_rating=int(bomb.get("rating", scramble.get("rating", 6)) or 6),
            sec_value=state.get("host_security_value", 6),
            sec_code=state.get("host_security_code", "Green"),
            headline="Exploding Scramble's linked data bomb")
        detonated = True
    _append_event(state, {
        "type": "file_access_encrypted",
        "action_label": "Download Data" if body.action_type == "download_data" else "Edit File",
        "subsystem": "files",
        "success": False,
        "scramble_discovered": newly_found,
        "detonated": detonated,
        "description": (
            f"You try to {op} \"{file_label}\" but the data is ENCRYPTED by Scramble IC"
            + (" -- and its linked data bomb DETONATES!" if detonated
               else ". Decrypt the Scramble first (Analyze Icon to learn its type safely).")
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
    """Run the GM's one secret Sensor Test when reactive IC activates (vr2 line 409).

    Rolls the decker's Sensor dice vs the IC rating and raises the IC's
    ``detection_level`` to the number of successes (capped 3, never lowered):
      0 unaware  1 'something triggered IC'  2 know the type  3 know rating + location.
    Emits a graduated, player-facing notice when the level increases. Returns the level.
    """
    if ic.get("sensor_checked"):
        return _ic_detection_level(ic)
    ic["sensor_checked"] = True
    if ic.get("analyzed"):
        ic["detection_level"] = 3
        return 3
    prev = _ic_detection_level(ic)
    eff = _get_decker_effective(decker, state)
    roll = eng.roll_dice(eff.get("sensor", 4), ic.get("rating", 6))
    new = min(3, max(prev, roll["successes"]))
    ic["detection_level"] = new
    if new > prev:
        ic_type = _ic_display_type(ic)
        notices = {
            1: "Sensor sweep detects IC activity. Type: Unknown.",
            2: f"Sensor sweep identifies a lurking IC. Type: {ic_type}.",
            3: (f"Sensor sweep identifies a lurking IC. Type: {ic_type}-{ic.get('rating', '?')}. "
                "Location pinpointed."),
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


def _run_reactive_activation_sensor_checks(state: dict, decker: dict) -> None:
    """Run one-time secret Sensor checks for newly activated reactive defenses."""
    bouncer = state.get("pending_bouncer")
    if isinstance(bouncer, dict) and not bouncer.get("sensor_checked"):
        bouncer["sensor_checked"] = True
        eff = _get_decker_effective(decker, state)
        roll = eng.roll_dice(
            max(1, eff.get("sensor", 4)),
            max(2, int(state.get("host_security_value", 1) or 1)),
        )
        if roll.get("successes", 0) > 0:
            _append_event(state, {
                "type": "bouncer_warning",
                "description": "Your Sensors detect that host security is rising.",
            })
    for ic in [*(state.get("active_ic") or []), *(state.get("lurking_ic") or [])]:
        if not isinstance(ic, dict) or ic.get("status") not in ("active", "lurking"):
            continue
        ic_type = _canonical_ic_type(ic.get("type", ""))
        if rules.IC_CATALOG.get(ic_type, {}).get("ic_type") == "reactive":
            _secret_sensor_test(state, decker, ic)


def _complete_pending_bouncer(state: dict) -> None:
    """Apply a due Bouncer upgrade without disclosing its exact new posture to the player."""
    pending = state.get("pending_bouncer")
    if not isinstance(pending, dict):
        return
    if state.get("current_turn", 1) < int(pending.get("complete_turn", 0) or 0):
        return
    state["host_security_code"] = pending.get(
        "new_security_code", state.get("host_security_code"))
    state["host_security_value"] = int(pending.get(
        "new_security_value", state.get("host_security_value", 1)) or 1)
    state["host_security_revealed"] = False
    state.pop("security_known", None)
    state.pop("pending_bouncer", None)
    _append_event(state, {
        "type": "bouncer_completed", "gm_only": True,
        "description": (
            f"Bouncer upgrade complete: {state['host_security_code']} "
            f"{state['host_security_value']}."
        ),
    })


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
        maneuvering_evasion_dice=eff.get("evasion", 4) + body.hacking_pool_dice,
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
    if pc_cloak > 0:
        _spend_one_shot(state, decker, "cloak")
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
    if pc_lock_on > 0:
        _spend_one_shot(state, decker, "lock_on")
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
            ev["description"] = f"{label} jockeys for position but gains no advantage ({man_succ} vs {opp_succ})."
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
    """Locate every operational IC presence on a successful Index System Test.

    The operation does not identify an IC: a newly found icon starts at detection level 1 and
    still requires Analyze IC for its type/rating. It also re-acquires evaded IC. Trace IC in its
    Location Cycle has vanished and cannot be re-acquired; Relocate is the operation that affects
    it then. Lurking reactive IC stays in GM state so its trigger logic is preserved.
    """
    operational = [
        ic for ic in [*(state.get("active_ic") or []), *(state.get("lurking_ic") or [])]
        if isinstance(ic, dict) and ic.get("status") in ("active", "lurking")
        and not (_ic_is_trace(ic) and ic.get("trace_phase") == "locate")
    ]
    tid = (target_ic_id or "").strip()
    if tid:
        operational = [ic for ic in operational if ic.get("id") == tid]
    hidden = [
        ic for ic in operational
        if _ic_detection_level(ic) <= 0
        or (ic.get("evaded") and ic.get("evade_dir") == "hid_from_pc")
    ]
    if not hidden:
        _append_event(state, {
            "type": "ic_relocate", "outcome": "none",
            "description": "Locate IC sweep found no unlocated operational IC.",
        })
        return
    if not test_success:
        _append_event(state, {
            "type": "ic_relocate", "outcome": "fail",
            "description": "Locate IC failed -- the hidden IC stays off your sensors this turn.",
        })
        return
    for ic in hidden:
        if ic.get("evaded") and ic.get("evade_dir") == "hid_from_pc":
            _clear_evade(state, ic, redetected=True)
        ic["detection_level"] = max(1, _ic_detection_level(ic))
        ic["located"] = True
    _append_event(state, {
        "type": "ic_relocate", "outcome": "located",
        "count": len(hidden),
        "description": (
            f"Locate IC found {len(hidden)} operational IC icon"
            f"{'s' if len(hidden) != 1 else ''}. "
            "Analyze each icon to identify its type and rating."
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
            "description": "Index sweep failed -- you can't re-acquire the decker that evaded you.",
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
        names = ", ".join(e["name"] for e, _ in found)
        _append_event(state, {
            "type": "enemy_decker", "outcome": "scan_hit", "enemy_id": found[0][0]["id"],
            "description": f"Re-acquired target: {names}.",
        })
    else:
        slipped = ", ".join(e["name"] for e in evaded)
        _append_event(state, {
            "type": "enemy_decker", "outcome": "scan_fail",
            "description": f"Re-acquire failed. {slipped} slips past your sensors.",
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
async def sheaf_preview(
    body: SheafGenerateInput,
    request: Request,
    auth: dict = Depends(get_any_token),
):
    """Generate a preview sheaf without saving it. Rate-limited per caller (enforce_call_rate):
    it runs the RNG/table sheaf generator on every call and is otherwise open to any runner."""
    await enforce_call_rate(request, auth)
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
                f"{_ic_display_type({'type': 'Worm', 'variant': i['variant']})} "
                f"(R{i.get('rating', '?')})" for i in infections
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
            "entered": bool(td.get("entered", False)),
        })

    # Key/target files the decker LOCATED this run (found via Locate File). The GM-authored
    # narrative rides here so the acknowledged AAR carries the mission flavor -- surfaced whether
    # or not the file was downloaded (finding it is the trigger). GM-only, like the rest of the AAR.
    target_files = []
    for pd in (state.get("paydata") or []):
        if not isinstance(pd, dict) or not pd.get("is_key") or not pd.get("located"):
            continue
        target_files.append({
            "name": str(pd.get("name", "") or ""),
            "narrative": str(pd.get("narrative", "") or ""),
            "downloaded": bool(pd.get("downloaded")),
            "destroyed": bool(pd.get("destroyed")),
            "tampered": bool(pd.get("tampered")),
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
        "target_files": target_files,
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
    """Acknowledge a run's after-action report and PURGE the run.

    This PERMANENTLY DELETES the ended run row (and its frozen state_json) from the database. The
    AAR is computed on demand from that state, so once purged the report cannot be regenerated or
    re-reviewed -- there is no archived copy kept. Acknowledging therefore both clears the run-start
    gate for that decker AND drops the run from the GM review queue (which only holds outstanding
    reports). The AAR is returned one last time in the response so the caller can display what was
    just cleared before it is gone."""
    run = await _get_run_or_404(db, run_id)
    if run.status == "active":
        raise HTTPException(400, "Run is still active -- nothing to acknowledge yet.")
    # The browser eagerly applies damage when it observes run end, but acknowledgment is the
    # destructive boundary: guarantee permanent consequences are durable before deleting the
    # only copy of the run state. The helper is idempotent when the browser already applied them.
    await _apply_run_damage_to_deck(db, run, {"is_admin": True})
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

    decker_dict = body.decker.model_dump()
    if not auth.get("is_admin"):
        selections = (
            [item.model_dump() for item in body.run_loadout_items]
            if body.run_loadout_items is not None else None
        )
        decker_dict = await _authoritative_player_decker(db, auth, decker_dict, selections)

    await _assert_no_unacknowledged_run(db, auth, decker_dict)

    run = await _create_run(db, auth, host, decker_dict)
    return _serialize_run(run, auth)


async def _authoritative_player_decker(
    db: AsyncSession,
    auth: dict,
    decker_dict: dict,
    run_loadout_items: list[dict] | None = None,
) -> dict:
    """Build a player run snapshot from the owned character's persisted deck and loadout."""
    character_id = decker_dict.get("character_id")
    if character_id is None:
        raise HTTPException(400, "character_id is required to start a player Matrix run")
    character = await db.get(Character, character_id)
    if character is None or not character.is_pc or not character.is_active:
        raise HTTPException(404, "Active player character not found")
    token = auth.get("user_token")
    if not token or character.owner_token != hash_token(token):
        raise HTTPException(404, "Active player character not found")

    authoritative = _decker_from_persisted_loadout(
        character, decker_dict, run_loadout_items,
    )
    authoritative.update({
        "character_id": character.id,
        "name": character.name,
        "computer_skill": character.computer_skill_rating,
        "intelligence": character.intelligence,
        "quickness": character.quickness,
        "willpower": character.willpower,
        "body": character.body,
    })
    return authoritative


_JACKPOINT_PROFILES = {
    (-2, -2, 20, False, 0, False),
    (0, 0, 20, False, 0, False),
    (-4, -4, 50, False, 0, False),
    (4, 4, 20, False, 0, False),
    (-6, 0, 0, True, 0, False),
    (0, 2, 50, False, -2, True),
}


def _program_key(item: dict) -> str:
    raw = str(item.get("programTypeKey") or item.get("utilName") or "").strip().lower()
    raw = raw.replace("/", "_").replace("-", "_").replace(" ", "_")
    return {"read__write": "read_write", "validate": "validate_pgm"}.get(raw, raw)


def _program_options_from_item(item: dict, rating: int) -> dict:
    opts = {
        "skulk": 0, "area": 0, "dinab": 0, "targeting": False,
        "penetration": False, "chaser": False, "one_shot": False,
        "squeeze": False, "limit_target": "", "damage_level": "",
    }
    for part in str(item.get("mods") or "").split(","):
        token = part.strip()
        match = re.fullmatch(r"(Area|DINAB|Skulk)\s+(\d+)", token, re.IGNORECASE)
        if match:
            opts[match.group(1).lower()] = min(rating, int(match.group(2)))
        elif token.lower() in {"targeting", "penetration", "chaser", "one-shot", "squeeze"}:
            opts[token.lower().replace("-", "_")] = True
        else:
            match = re.fullmatch(r"Limit\s*:\s*(IC|DECKER)", token, re.IGNORECASE)
            if match:
                opts["limit_target"] = match.group(1).lower()
    if item.get("isOneShot"):
        opts["one_shot"] = True
    limit_target = str(item.get("limitTarget") or "").strip().lower()
    if item.get("hasLimit") and limit_target in {"ic", "decker"}:
        opts["limit_target"] = limit_target
    if _program_key(item) == "attack":
        opts["damage_level"] = {
            2: "Light", 3: "Moderate", 4: "Serious", 5: "Deadly",
        }.get(int(item.get("attackDamage", 0) or 0), "")
    if opts["penetration"] and opts["chaser"]:
        opts["chaser"] = False
    return opts


def _program_actual_size(item: dict, key: str, rating: int) -> int:
    """Recompute a persisted program's object-code footprint from rules inputs."""
    def half_up(value: float) -> int:
        return int(value + 0.5)

    multiplier = rules.PROGRAM_MULTIPLIERS.get(key)
    if multiplier is None:
        raise HTTPException(400, f"Unknown persisted utility type: {key or '(blank)'}")
    if key == "attack":
        multiplier = int(item.get("attackDamage", 0) or 0)
        if multiplier not in {2, 3, 4, 5}:
            raise HTTPException(400, "Persisted Attack utility has an invalid Damage Level")

    opts = _program_options_from_item(item, rating)
    effective = rating + opts["area"] + opts["dinab"] + opts["skulk"]
    effective += 1 if opts["chaser"] else 0
    effective += 1 if opts["penetration"] else 0
    effective += 2 if opts["targeting"] else 0
    effective -= 1 if opts["limit_target"] else 0
    before_squeeze = max(1, effective)
    effective = before_squeeze + (1 if opts["squeeze"] else 0)
    size = effective * effective * multiplier
    mods = str(item.get("mods") or "")
    optimized = bool(re.search(r"(?:^|,)\s*Optimization\s*(?:,|$)", mods, re.IGNORECASE))
    if opts["one_shot"]:
        size = half_up(size * 0.25)
    if optimized:
        size = half_up(size * 0.5)
    if opts["squeeze"]:
        unsqueezed = before_squeeze * before_squeeze * multiplier
        if opts["one_shot"]:
            unsqueezed = half_up(unsqueezed * 0.25)
        if optimized:
            unsqueezed = half_up(unsqueezed * 0.5)
        size = half_up(unsqueezed * 0.5)
    return max(1, size)


def _validated_deck_values(deck: dict) -> dict[str, int | bool | str]:
    """Validate persisted hardware/persona constraints and return normalized values."""
    try:
        mpcp = int(deck.get("mpcp", 0) or 0)
        persona = {k: int(deck.get(v, 0) or 0) for k, v in {
            "bod": "pBod", "evasion": "pEvasion", "masking": "pMasking", "sensor": "pSensor",
        }.items()}
        hardening = int(deck.get("hardening", 0) or 0)
        response = int(deck.get("respIncrease", 0) or 0)
        active_memory = int(deck.get("activeMem", 0) or 0)
        storage = int(deck.get("offlineStorage", 0) or 0)
        io_speed = int(deck.get("ioSpeed", 0) or 0)
    except (TypeError, ValueError) as exc:
        raise HTTPException(400, "Persisted deck contains non-numeric ratings") from exc
    mode = str(deck.get("deckType") or "hot").lower()
    has_rf = bool(deck.get("realityFilter"))
    if not 1 <= mpcp <= 50 or mode not in {"hot", "cool", "tortoise"}:
        raise HTTPException(400, "Persisted deck has invalid MPCP or deck mode")
    if any(value < 1 or value > mpcp for value in persona.values()):
        raise HTTPException(400, "Persisted persona ratings must be between 1 and MPCP")
    persona_cap = max(0, mpcp - (1 if has_rf else 0)) * 3
    if sum(persona.values()) > persona_cap:
        raise HTTPException(400, f"Persisted persona total exceeds its {persona_cap}-point budget")
    if hardening < 0 or hardening > mpcp // 2:
        raise HTTPException(400, "Persisted Hardening exceeds floor(MPCP / 2)")
    if response < 0 or response > min(3, mpcp // 4):
        raise HTTPException(400, "Persisted Response Increase exceeds its MPCP limit")
    if active_memory < 0 or active_memory > mpcp * 100:
        raise HTTPException(400, "Persisted Active Memory exceeds MPCP x 100 Mp")
    if storage < 0 or storage > 65535:
        raise HTTPException(400, "Persisted Storage Memory exceeds the 65,535 Mp app limit")
    if io_speed < 10 or io_speed % 10 or io_speed > mpcp * persona["sensor"] * 10:
        raise HTTPException(400, "Persisted I/O Speed must be a valid multiple of 10 Mp")
    return {
        "mpcp": mpcp, **persona, "hardening": hardening, "response": response,
        "active_memory": active_memory, "storage": storage, "io_speed": io_speed,
        "mode": mode, "reality_filter": has_rf,
    }


def _resolve_run_loadout_items(
    stores: dict,
    loadout: dict,
    selections: list[dict],
) -> list[dict]:
    loadout_items = loadout.get("items") or []
    compiled_items = stores.get("sr2_compiled_programs_v1") or []
    if not isinstance(loadout_items, list) or not isinstance(compiled_items, list):
        raise HTTPException(400, "Persisted program stores are invalid")
    resolved: list[dict] = []
    for selection in selections:
        source = selection.get("source")
        if source == "loadout":
            index = selection.get("source_index")
            if index is None or index >= len(loadout_items):
                raise HTTPException(400, "Adjusted loadout references an invalid saved item")
            persisted = loadout_items[index]
            if _run_program_signature(persisted) != selection.get("source_signature"):
                raise HTTPException(400, "Adjusted loadout is stale; reopen it and try again")
        elif source == "compiled":
            artifact_id = str(selection.get("artifact_id") or "")
            persisted = next((
                item for item in compiled_items
                if isinstance(item, dict) and str(item.get("id") or "") == artifact_id
            ), None)
            if persisted is None:
                raise HTTPException(400, "Adjusted loadout references an unknown compiled program")
        else:
            raise HTTPException(400, "Adjusted loadout contains an invalid source")
        if not isinstance(persisted, dict):
            raise HTTPException(400, "Adjusted loadout references an invalid program")

        item = copy.deepcopy(persisted)
        item["target"] = selection.get("target")
        limit_target = str(selection.get("limit_target") or "").lower()
        if item.get("hasLimit"):
            if limit_target not in {"ic", "decker"}:
                raise HTTPException(400, "A Limited program requires an IC or decker target")
            item["limitTarget"] = limit_target
        elif limit_target:
            raise HTTPException(400, "Only a Limited program can select a Limit target")
        resolved.append(item)
    return resolved


def _run_program_signature(item: Any) -> str:
    if not isinstance(item, dict):
        return ""
    return "|".join([
        _program_key(item),
        str(int(item.get("baseRating", 0) or 0)),
        str(item.get("mods") or "None").strip().lower(),
        "1" if item.get("isOneShot") else "0",
        "1" if item.get("hasLimit") else "0",
        str(int(item.get("attackDamage", 0) or 0)),
        str(int(item.get("actualSize", 0) or 0)),
    ])


def _decker_from_persisted_loadout(
    character: Character,
    request: dict,
    run_loadout_items: list[dict] | None = None,
) -> dict:
    stores = ((character.deck_builder_state or {}).get("stores") or {})
    decks = stores.get("sr2_decks_v1") or []
    loadouts = stores.get("sr2_loadouts_v1") or []
    deck_name = str(request.get("deck_name") or "").strip()
    loadout_name = str(request.get("loadout_name") or "").strip()
    deck = next((item for item in decks
                 if isinstance(item, dict) and item.get("name") == deck_name), None)
    loadout = next((item for item in loadouts
                    if isinstance(item, dict) and item.get("name") == loadout_name), None)
    if deck is None or str(deck.get("status") or "draft").lower() != "ready":
        raise HTTPException(400, "Select a persisted, ready deck before starting a run")
    if loadout is None or loadout.get("deckName") != deck_name:
        raise HTTPException(400, "Select a persisted loadout for the chosen deck")
    values = _validated_deck_values(deck)
    selected_items = (
        _resolve_run_loadout_items(stores, loadout, run_loadout_items)
        if run_loadout_items is not None else loadout.get("items") or []
    )

    profile = (
        int(request.get("trace_factor", 0) or 0),
        int(request.get("access_modifier", 0) or 0),
        int(request.get("base_bandwidth", 0) or 0),
        bool(request.get("console_access")),
        int(request.get("reaction_modifier", 0) or 0),
        bool(request.get("physical_trace_immune")),
    )
    if profile not in _JACKPOINT_PROFILES:
        raise HTTPException(400, "Invalid jackpoint profile")
    if profile[-1] and not deck.get("satlink"):
        raise HTTPException(400, "Satellite jackpoint requires a Satlink Interface")

    damage = deck.get("damage") or {}
    mpcp = max(1, int(damage.get("mpcp", values["mpcp"]) or 1))
    utilities: dict[str, int] = {}
    storage_programs: list[dict] = []
    program_sizes: dict[str, int] = {}
    program_options: dict[str, dict] = {}
    one_shot_active: dict[str, int] = {}
    one_shot_signatures: dict[str, tuple] = {}
    option_rank: dict[str, int] = {}
    normal_types: set[str] = set()
    active_used = 0
    storage_used = 0
    for item in selected_items:
        if not isinstance(item, dict):
            continue
        key = _program_key(item)
        rating = max(0, int(item.get("baseRating", 0) or 0))
        if not key or rating <= 0:
            continue
        if rating > mpcp:
            raise HTTPException(400, f"{_action_label(key)}-{rating} exceeds MPCP {mpcp}")
        target = str(item.get("target") or "active").lower()
        squeezed = bool(item.get("squeezed")) or bool(re.search(r"\bSqueeze\b", str(item.get("mods") or ""), re.I))
        stored_size = _program_actual_size(item, key, rating)
        full_size = stored_size * 2 if squeezed else stored_size
        options = _program_options_from_item(item, rating)
        if options["one_shot"]:
            signature = (
                rating, stored_size, full_size, squeezed,
                tuple(sorted(options.items())),
            )
            prior = one_shot_signatures.setdefault(key, signature)
            if prior != signature:
                raise HTTPException(
                    400,
                    f"All One-Shot {_action_label(key)} copies in a loadout must use the same build",
                )
        elif key in normal_types:
            raise HTTPException(400, f"Duplicate non-One-Shot utility: {_action_label(key)}")
        else:
            normal_types.add(key)
        active = target in {"active", "both"}
        if not options["one_shot"] or not active:
            storage_used += stored_size
        program_sizes[key] = max(program_sizes.get(key, 0), full_size)
        if active:
            active_used += full_size
            utilities[key] = max(utilities.get(key, 0), rating)
            if options["one_shot"]:
                one_shot_active[key] = one_shot_active.get(key, 0) + 1
        else:
            storage_programs.append({
                "name": key, "rating": rating, "size": full_size, "squeezed": squeezed,
            })
        rank = 2 if active else 1
        if rank > option_rank.get(key, 0):
            program_options[key] = options
            option_rank[key] = rank

    active_memory = int(values["active_memory"])
    offline_storage = int(values["storage"])
    if active_memory and active_used > active_memory:
        raise HTTPException(400, "Persisted loadout exceeds deck active memory")
    if offline_storage and storage_used > offline_storage:
        raise HTTPException(400, "Persisted loadout exceeds deck storage")

    result = {
        "deck_name": deck_name,
        "loadout_name": loadout_name,
        "mpcp": mpcp,
        "deck_mode": values["mode"],
        "iccm": bool(deck.get("iccm")),
        "reality_filter": values["reality_filter"],
        "hardening": values["hardening"],
        "response_increase": values["response"],
        "active_memory": active_memory,
        "io_speed": values["io_speed"],
        "storage_free_mp": max(0, offline_storage - storage_used) if offline_storage else -1,
        "utilities": utilities,
        "storage_programs": storage_programs,
        "program_sizes": program_sizes,
        "program_options": program_options,
        "one_shot_active": one_shot_active,
        "mpcp_infections": copy.deepcopy(deck.get("mpcp_infections") or []),
        "trace_factor": profile[0], "access_modifier": profile[1],
        "base_bandwidth": profile[2], "console_access": profile[3],
        "reaction_modifier": profile[4], "physical_trace_immune": profile[5],
        "bandwidth_modifier": 0,
        "persona_mode": request.get("persona_mode", "none"),
        "linked_passcode": bool(request.get("linked_passcode")),
    }
    for key, field in {"bod": "pBod", "evasion": "pEvasion", "masking": "pMasking", "sensor": "pSensor"}.items():
        result[key] = max(1, int(damage.get(field, values[key]) or 1))
    return result


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
    composite_errors = _host_composite_errors(host.config_json or {})
    if composite_errors:
        raise HTTPException(400, "Host is not run-ready: " + "; ".join(composite_errors))
    state = _initial_state(decker_dict, host)
    # RAW: an Exploding Scramble is linked to a data bomb (defuse it before decrypting, or the
    # decrypt detonates it). Seed that linked bomb so it can be found + defused during the run.
    _link_exploding_scramble_bombs(state)
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
        stored = deck.get("mpcp_infections")
        existing = [
            {**inf, "variant": variant}
            for inf in (stored if isinstance(stored, list) else [])
            if isinstance(inf, dict)
            if (variant := _worm_variant(inf.get("variant"))) is not None
        ]
        seen = {inf.get("ic_id") for inf in existing if isinstance(inf, dict)}
        for inf in infections:
            if not isinstance(inf, dict):
                continue
            variant = _worm_variant(inf.get("variant"))
            if variant is None:
                continue
            iid = inf.get("ic_id")
            if iid and iid in seen:
                continue
            existing.append({
                "variant": variant,
                "rating": int(inf.get("rating", 6) or 6),
                "ic_id": str(iid or ""),
            })
            if iid:
                seen.add(iid)
        if existing:
            deck["mpcp_infections"] = existing
            changed = True
        elif "mpcp_infections" in deck:
            deck.pop("mpcp_infections")
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


def _is_evaluate_program(entry: dict) -> bool:
    """True when a stored program / loadout item is an Evaluate utility. Prefers the explicit
    ``programTypeKey``; falls back to the display ``utilName``."""
    if not isinstance(entry, dict):
        return False
    ptk = str(entry.get("programTypeKey") or "").strip().lower()
    if ptk:
        return ptk == "evaluate"
    return str(entry.get("utilName") or "").strip().lower() == "evaluate"


async def _apply_evaluate_degradation(db: AsyncSession, run: MatrixRun, auth: dict) -> None:
    """SR2 VR2 (p.1486): at the END of each run, roll 1D3 and reduce the rating of ALL of the
    decker's Evaluate programs by that result (floor 0). This fires every run regardless of whether
    Evaluate was used.

    Degrades the rating in BOTH persisted stores so the deck the decker takes on the next run
    reflects the burned-out rating: the software-library master (``sr2_compiled_programs_v1``) and
    every loadout's embedded copy (``sr2_loadouts_v1`` -- what a run actually reads). Source code
    (``sr2_program_sources_v1``) is deliberately left untouched: that is the rebuild/upgrade path
    ("deckers with source copies can upgrade per standard rules"). No-op when the character can't be
    resolved, the caller doesn't own it, or degradation already ran (idempotent via
    ``state["evaluate_degraded"]``)."""
    state = run.state_json or {}
    if state.get("evaluate_degraded"):
        return
    decker = run.decker_json or {}
    char_id = decker.get("character_id")
    if not char_id:
        return
    char = await db.get(Character, char_id)
    if char is None:
        return
    # Only the character's owner (or an admin) may mutate its program stores.
    if not auth.get("is_admin"):
        tok = auth.get("user_token")
        if not tok or char.owner_token != hash_token(tok):
            return

    roll = random.randint(1, 3)

    dbs = copy.deepcopy(char.deck_builder_state or {})
    stores = dbs.get("stores")
    changed = False
    affected = 0

    if isinstance(stores, dict):
        # 1) Software-library master copies (the workshop's coded/owned Evaluate programs).
        compiled = stores.get("sr2_compiled_programs_v1")
        if isinstance(compiled, list):
            for entry in compiled:
                if not _is_evaluate_program(entry):
                    continue
                old = max(0, int(entry.get("baseRating", 0) or 0))
                new = max(0, old - roll)
                if new == old:
                    continue
                entry["baseRating"] = new
                eff = max(0, int(entry.get("effectiveRating", old) or old))
                entry["effectiveRating"] = max(0, eff - roll)
                entry["name"] = (
                    f"{entry.get('utilName') or 'Evaluate'}-{new}"
                    f" v{entry.get('sourceVersion', 1)} | {entry.get('mods') or 'None'}"
                )
                changed = True
                affected += 1

        # 2) Every loadout's embedded copy -- this is the rating a run consumes at start-of-run.
        loadouts = stores.get("sr2_loadouts_v1")
        if isinstance(loadouts, list):
            for loadout in loadouts:
                items = loadout.get("items") if isinstance(loadout, dict) else None
                if not isinstance(items, list):
                    continue
                for item in items:
                    if not _is_evaluate_program(item):
                        continue
                    old = max(0, int(item.get("baseRating", 0) or 0))
                    new = max(0, old - roll)
                    if new == old:
                        continue
                    item["baseRating"] = new
                    changed = True
                    affected += 1

    if changed:
        char.deck_builder_state = dbs
        await db.commit()

    state = copy.deepcopy(run.state_json or {})
    state["evaluate_degraded"] = True
    state["evaluate_degrade_roll"] = roll
    if isinstance(state.get("event_log"), list):
        _append_event(state, {
            "type": "alert",
            "level": "passive",
            "text": (
                f"Evaluate degradation (end of run): rolled 1D3 = {roll}. "
                + (f"Reduced {affected} Evaluate program copy(ies)."
                   if affected else "No Evaluate programs to degrade.")
            ),
        })
    run.state_json = state
    await db.commit()


@router.post("/{run_id}/apply-deck-damage", response_model=MatrixRunRead)
async def apply_deck_damage(
    run_id: int,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Stamp a finished run's hardware consequences (MPCP damage, Ripper chip burn, Worm
    infections) onto the owning character's saved deck, then apply end-of-run Evaluate degradation
    (1D3 rating loss on all Evaluate programs). Both are idempotent and only fire once the run has
    ended. The client calls this once when it detects the run is over."""
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if not (run.state_json or {}).get("run_ended"):
        raise HTTPException(409, "Run has not ended")
    await _apply_run_damage_to_deck(db, run, auth)
    await _apply_evaluate_degradation(db, run, auth)
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
                          sec_code: str, sec_value: int, logon_completed: bool = False,
                          effect_type: str | None = None, effect_rating: int | None = None) -> None:
    """Pause an IC's standard cybercombat strike so the decker can allocate Hacking Pool dice to the
    icon's damage resistance before it resolves. Stashes everything ``_resolve_ic_cybercombat`` needs
    to finish the SAME strike later -- the already-rolled to-hit is reused verbatim, so no dice are
    re-rolled -- and emits a ``defense_pending`` event carrying the attacker's successes so the
    client can show them before the player chooses. The parked IC already has ``acted_pass`` set, so
    resuming the pass skips it: only the resolution is deferred, not the action."""
    effect_type = effect_type or ic["type"]
    effect_rating = int(effect_rating if effect_rating is not None else ic["rating"])
    power = (effect_rating + ic.get("cascade_rating_bonus", 0)
             + atk_power_delta + _deathworm_tn_bonus(state))
    label = (f"Construct ({effect_type}-{effect_rating})"
             if ic.get("type") == "Construct" else f"{effect_type}-{effect_rating}")
    state["pending_defense"] = {
        "ic_id": ic["id"],
        "attacker_label": label,
        "attack_successes": to_hit.get("successes", 0),
        "to_hit_roll": to_hit,
        "power": power,
        "hp_available": state.get("hackingPool_remaining", 0),
        "resume_logon_completed": bool(logon_completed),
        "acting_init": state.get("_acting_init"),
        "acting_count": state.get("_acting_count"),
        "ctx": {
            "ic_attack_pool": ic_attack_pool,
            "ic_target_status": ic_target_status,
            "atk_power_delta": atk_power_delta,
            "atk_tn_delta": atk_tn_delta,
            "cluster_penalty": cluster_penalty,
            "ic_category": ic_category,
            "sec_code": sec_code,
            "sec_value": sec_value,
            "effect_type": effect_type,
            "effect_rating": effect_rating,
        },
    }
    _append_event(state, {
        "type": "defense_pending",
        "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
        "description": (
            f"{label} strikes your icon -- {_successes(to_hit.get('successes', 0))}, "
            f"Power {power}."
        ),
        "attack_roll": to_hit,
        "hp_available": state.get("hackingPool_remaining", 0),
    })


def _resolve_ic_cybercombat(state: dict, decker: dict, ic: dict, *, ic_attack_pool: int,
                            ic_target_status: str, eff: dict, atk_power_delta: int,
                            atk_tn_delta: int, cluster_penalty: int, ic_category: str,
                            sec_code: str, sec_value: int,
                            precomputed_attack_roll: dict | None = None,
                            defender_bonus_dice: int = 0,
                            effect_type: str | None = None,
                            effect_rating: int | None = None) -> bool:
    """Resolve one standard (non-black) IC cybercombat strike -- Killer / Blaster / Sparky /
    Construct -- against the decker's persona icon: damage resistance, Armor wear, Simsense overload,
    and persona-crash consequences (Blaster/Sparky MPCP burn + dump shock).

    Split out of ``_advance_npc_pass`` so the interactive-defense flow can resolve the SAME strike
    after the decker allocates Hacking Pool dice: the caller rolls the to-hit first and passes it as
    ``precomputed_attack_roll`` (reused verbatim -- RNG-identical to the old inline roll), and
    ``defender_bonus_dice`` adds the decker's chosen Hacking Pool dice to the icon's Bod resistance.
    Returns True when the strike ended the run (caller must stop the pass); False otherwise.
    """
    effect_type = effect_type or ic["type"]
    effect_rating = int(effect_rating if effect_rating is not None else ic["rating"])
    armor          = _effective_armor(decker, state)
    cascade_power  = effect_rating + ic.get("cascade_rating_bonus", 0)
    # Shield parry: fired ONLY if the attack lands; net successes then cancel attacker damage
    # successes before staging (vr2). A clean miss rolls no Shield and wears nothing.
    ic_skill       = _ic_test_pool(ic, sec_value, defense=False)
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
        shield_parry=lambda: _shield_parry(
            state, decker, attacker_skill=ic_skill, context=effect_type, source_ic=ic),
        precomputed_attack_roll=precomputed_attack_roll,
        defender_bonus_dice=defender_bonus_dice,
    )
    final_dmg = attack["resistance"]["final_damage_level"]
    boxes = attack["resistance"]["boxes"]
    net_successes = (
        int(attack["resistance"].get("attacker_successes", 0) or 0)
        - int(attack["resistance"]["resist_roll"].get("successes", 0) or 0)
    )
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
            f"{('Construct ' if ic['type'] == 'Construct' else '')}{effect_type}-{effect_rating} attacks: "
            f"{attack['attack_roll']['successes']} attack successes vs "
            f"{attack['resistance']['resist_roll']['successes']} resist. "
            f"Net Successes: {net_successes}. "
            f"Damage: {final_dmg} ({boxes} box{'es' if boxes != 1 else ''}). "
            f"Persona: {state['condition_monitor']['persona_boxes']}/10"
        ),
        "attack_roll": attack["attack_roll"],
        "resist_roll": attack["resistance"]["resist_roll"],
        "net_successes": net_successes,
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
            "description": "Persona crashed -- decker dumped from the Matrix!",
        })

        # Blaster: MPCP damage test on persona crash (1 per 2 successes)
        if effect_type == "Blaster":
            mpcp_hit, b_roll = _roll_mpcp_damage(state, decker, effect_rating)
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
        elif effect_type == "Sparky":
            mpcp_hit, s_roll = _roll_mpcp_damage(state, decker, effect_rating, tn_bonus=2)
            # VR2 "Sparky": (IC Rating)M physical -- stage up per Sparky-test successes,
            # then the decker RESISTS with Body vs Power (IC rating, reduced by Hardening).
            hardening = decker.get("hardening", 0)
            sparky_staged = eng.stage_damage("Moderate", s_roll["successes"], 1)
            sparky_power = max(1, effect_rating - hardening)
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


def _hostile_action_schedule(
    state: dict,
    *,
    upper_count: int | None,
    lower_count: int,
) -> list[tuple[int, str, dict, int]]:
    """Return pending hostile actions in global descending initiative-count order.

    ``lower_count < count <= upper_count`` selects the actors whose segments occur after the
    player count being closed and before the next player count. ``upper_count=None`` selects every
    remaining positive count for the end-of-round flush. Action ordinals are tracked per hostile,
    independent of the decker's pass ordinal.
    """
    scheduled: list[tuple[int, str, dict, int]] = []

    def add(actor: dict, kind: str, effective_initiative: int, passes: int) -> None:
        taken = max(0, int(actor.get("actions_taken_turn", 0) or 0))
        if "actions_taken_turn" not in actor and actor.get("acted_pass") is not None:
            taken = min(passes, max(0, int(actor.get("acted_pass", 0) or 0)))
        for action_index in range(taken + 1, passes + 1):
            count = effective_initiative - 10 * (action_index - 1)
            if count <= lower_count or (upper_count is not None and count > upper_count):
                continue
            scheduled.append((count, kind, actor, action_index))

    for ic in state.get("active_ic", []):
        if not isinstance(ic, dict) or ic.get("status") != "active" or ic.get("suppressed"):
            continue
        acting_type = (_construct_component(ic) or {}).get("type", ic.get("type"))
        info = rules.IC_CATALOG.get(_canonical_ic_type(acting_type), {})
        if (info.get("ic_type") != "proactive" and info.get("subtype") != "trace") or acting_type == "Probe":
            continue
        effective = int(ic.get("initiative", 0) or 0) - _ic_wound_mod(ic)
        add(ic, "ic", effective, _ic_passes(ic))

    for enemy in state.get("enemy_deckers", []):
        if not isinstance(enemy, dict) or enemy.get("status") != "active":
            continue
        effective = int(enemy.get("initiative", 0) or 0) - _enemy_wound_mod(enemy)
        add(enemy, "enemy", effective, _enemy_passes(enemy))

    return sorted(scheduled, key=lambda item: item[0], reverse=True)


def _advance_npc_count_window(
    state: dict,
    decker: dict,
    run,
    *,
    eff: dict,
    sec_code: str,
    sec_value: int,
    det_factor: int,
    upper_count: int | None,
    lower_count: int,
    allow_defense_pause: bool = False,
) -> None:
    """Resolve one globally ordered hostile initiative-count window.

    An interactive defense can interrupt the window after its attacker has been marked as acted.
    Store the inclusive current count so ``/defend`` can resume same-count ties and every lower
    count without repeating the parked attacker.
    """
    for count, kind, actor, action_index in _hostile_action_schedule(
        state, upper_count=upper_count, lower_count=lower_count,
    ):
        if state.get("run_ended"):
            break
        _advance_npc_pass(
            state, decker, run,
            eff=eff, sec_code=sec_code, sec_value=sec_value, det_factor=det_factor,
            scheduled_kind=kind, scheduled_actor_id=actor.get("id"),
            scheduled_action_index=action_index, scheduled_count=count,
            allow_defense_pause=allow_defense_pause,
        )
        if state.get("pending_defense"):
            state["pending_defense"]["resume_count_window"] = {
                "upper_count": count,
                "lower_count": lower_count,
            }
            break


def _advance_npc_pass(state: dict, decker: dict, run, *, eff: dict, sec_code: str,
                      sec_value: int, det_factor: int, logon_completed: bool = False,
                      allow_defense_pause: bool = False,
                      scheduled_kind: str | None = None,
                      scheduled_actor_id: str | None = None,
                      scheduled_action_index: int | None = None,
                      scheduled_count: int | None = None) -> None:
    """Drive app-controlled hostiles selected by the shared initiative-count scheduler.

    With ``scheduled_*`` arguments, exactly one IC or enemy decker acts at its own count and action
    index. The unscheduled compatibility path retains the legacy current-pass gating for Logon and
    persisted runs that already contain ordinal ``acted_pass`` markers.

    There is no human GM -- this is the app-as-GM action resolver. Probe IC (which test per System
    Test, not per initiative count) are handled by the caller. ``logon_completed`` carries the
    player's just-resolved Logon through the compatibility path. Mutates ``state`` (and
    ``run.status`` on a kill/dump); does not commit.
    """
    # Active IC attacks (proactive IC + trace IC that has already activated, in initiative order)
    for ic in sorted(state.get("active_ic", []), key=lambda x: x.get("initiative", 0), reverse=True):
        if scheduled_kind == "enemy" or (scheduled_actor_id and ic.get("id") != scheduled_actor_id):
            continue
        if ic["status"] != "active" or ic.get("suppressed"):
            continue
        if ic.get("spawn_pending_pass") == state.get("current_pass", 1):
            continue
        construct_component = _construct_component(ic) if ic.get("type") == "Construct" else None
        acting_type = construct_component["type"] if construct_component else ic["type"]
        acting_rating = construct_component["rating"] if construct_component else ic["rating"]
        ic_info = rules.IC_CATALOG.get(_canonical_ic_type(acting_type), {})
        ic_category = ic_info.get("category", "white")
        ic_subtype = ic_info.get("subtype", "")

        # Trace IC is classified "reactive" in the catalog but acts every turn on
        # its initiative (hunt -> locate -> trigger), so let it through here.
        if ic_info.get("ic_type") != "proactive" and ic_subtype != "trace":
            continue
        if acting_type == "Probe":
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
        if scheduled_action_index is None:
            if cur_pass > effective_passes or ic.get("acted_pass") == cur_pass:
                continue
            ic["acted_pass"] = cur_pass
        else:
            if scheduled_action_index > effective_passes:
                continue
            ic["actions_taken_turn"] = scheduled_action_index
            ic["acted_pass"] = cur_pass
        # Stamp every event this IC logs with its own initiative count (vr2: init is rolled once
        # per encounter, so this is stable). Reset to the decker's init when the driver finishes.
        state["_acting_init"] = ic.get("initiative")
        state["_acting_count"] = scheduled_count

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
                trace_tn = _compute_trace_tn(state, decker, acting_rating, eff, ic)
                hunt = eng.trace_hunt_cycle_attack(sec_value, trace_tn)
                if int((decker.get("utilities") or {}).get("camo", 0) or 0) > 0:
                    _spend_one_shot(state, decker, "camo")
                if hunt["hit"]:
                    hunt_successes = max(1, hunt["roll"]["successes"])
                    locate_turns = max(1, 10 // hunt_successes)
                    ic["trace_phase"] = "locate"
                    ic["trace_locate_remaining"] = locate_turns
                    _append_event(state, {
                        "type": "ic_attack",
                        "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                        "description": (
                            f"Trace IC has your data trail. {locate_turns} "
                            f"round{'s' if locate_turns != 1 else ''} until jackpoint located."
                        ),
                        "trace_phase": "hunt_hit",
                        "hunt_roll": hunt["roll"],
                    })
                else:
                    _append_event(state, {
                        "type": "ic_attack",
                        "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                        "description": "Trace IC is hunting your data trail.",
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
                        "description": "Trace spoofed for one turn.",
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
                                "Satlink traced. Physical location unknown. "
                                "-1 to all Proactive IC TNs, +1 to all Security Tally increases."
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
                                "Jackpoint traced, physical location reported. "
                                "-1 to all Proactive IC TNs, +1 to all Security Tally increases."
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
                            f"Trace continues. {remaining} "
                            f"round{'s' if remaining != 1 else ''} until jackpoint located."
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
            attr_key = _CRIPPLER_TARGET.get(_canonical_ic_type(acting_type), "bod")
            if _ic_detection_level(ic) < 2:
                ic["observed_type"] = _CRIPPLER_OBSERVED_TYPE[attr_key]
                ic["detection_level"] = 2
            target_attr = eff.get(attr_key, 4)
            # Shield parry: fired ONLY if the crippler lands (net successes then ADD to the decker's
            # opposed defence, vr2). A resisted/whiffed crippler rolls no Shield and wears nothing.
            # Same shared resolver the decker uses vs enemy icons (only the label differs by actor).
            result = _resolve_attribute_attack(
                state,
                attacker_pool=sec_value,
                resist_tn=acting_rating,
                target_attr_rating=target_attr,
                attr=attr_key,
                sec_code=sec_code,
                target_status=ic_target_status,
                target_kind="pc",
                target_decker=decker,
                causing_rating=acting_rating,
                shield_parry=lambda: _shield_parry(
                    state, decker, attacker_skill=sec_value, context=acting_type, source_ic=ic),
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
            shield_succ = int(result.get("shield_successes", 0) or 0)
            total_defense = def_succ + shield_succ
            net_succ = int(result.get("net_successes", 0) or 0)
            defense_margin = max(0, total_defense - atk_succ)
            desc = (
                f"{acting_type}-{acting_rating} Construct component vs {attr_key.title()}: "
                f"{atk_succ} attack / {total_defense} total defense "
                f"({def_succ} persona + {shield_succ} Shield). "
                f"Net Successes: {net_succ}. Defense Margin: {defense_margin}. "
                f"{attr_key.title()} -{reduction}."
            )
            if ic_subtype == "ripper" and result.get("chip_damage", 0) > 0:
                chip = result["chip_damage"]
                desc += f" {attr_key.title()} permanently reduced by {chip}."
            _append_event(state, {
                "type": "ic_attack",
                "ic_id": ic["id"], "ic_type": ic["type"], "ic_rating": ic["rating"],
                "description": desc,
                "attack_roll": result["attack_roll"],
                "defense_roll": result["defense_roll"],
                "attack_successes": atk_succ,
                "defense_successes": total_defense,
                "shield_successes": shield_succ,
                "net_successes": net_succ,
                "defense_margin": defense_margin,
                "attribute_target": attr_key,
                "attribute_reduction": reduction,
            })
            continue

        # -- Standard cybercombat: Killer, Blaster, Sparky, Construct, Black IC
        # A tortoise deck has no ASIST/simsense link, so Black IC cannot reach the operator at all:
        # it behaves like ordinary attack IC (icon damage only -- no biofeedback, no jack-out
        # Willpower gate, no dump shock, no MPCP burn). So drop the "black" treatment for a tortoise
        # and let it fall through to the standard icon-only cybercombat path below.
        is_black        = acting_type == "Black IC" and decker.get("deck_mode") != "tortoise"
        # Hot decks take lethal (Physical) biofeedback; a cool deck takes non-lethal (Stun).
        is_non_lethal   = is_black and (
            ic.get("mode") == "non_lethal" or decker.get("deck_mode") == "cool"
        )
        cluster_penalty = _cluster_size(state, ic.get("cluster_id"))
        ic_attack_pool = _ic_test_pool(ic, sec_value, defense=False)
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
                power=acting_rating + atk_power_delta + _deathworm_tn_bonus(state),
                hardening=hardening,
                icon_bod=eff["bod"],
                icon_armor=armor,
                tn_modifier=cluster_penalty + atk_tn_delta + _ic_wound_mod(ic) - _completed_trace_count(state),
                shield_parry=lambda: _shield_parry(
                    state, decker, attacker_skill=sec_value, context="Black IC", source_ic=ic),
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
                down_line = ("Physical Monitor full: the decker flatlines" if phys_full
                             else "Stun Monitor full: the decker blacks out, connection dropping")
                _append_event(state, {
                    "type": "persona_crash",
                    "description": f"Black IC biofeedback overwhelms the decker. {down_line}.",
                })
                mpcp_hit, bl_roll = _roll_mpcp_damage(state, decker, acting_rating, pool_multiplier=2)
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
                        "The IC crashes your icon and increases its rating (now "
                        f"{ic['rating']}). Jack out now!"
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
                effect_type=acting_type, effect_rating=acting_rating,
            )
            return
        if _resolve_ic_cybercombat(
            state, decker, ic,
            ic_attack_pool=ic_attack_pool, ic_target_status=ic_target_status, eff=eff,
            atk_power_delta=atk_power_delta, atk_tn_delta=atk_tn_delta,
            cluster_penalty=cluster_penalty, ic_category=ic_category,
            sec_code=sec_code, sec_value=sec_value, precomputed_attack_roll=_to_hit,
            effect_type=acting_type, effect_rating=acting_rating,
        ):
            break

    # Handle logon completion (player-action result; parameterized so new_turn's flush skips it).
    if logon_completed:
        _complete_logon(state, decker, det_factor)

    # Enemy deckers act automatically (app-as-GM), once per pass on the passes their OWN
    # initiative reaches (ceil(init/10) passes) -- they rolled initiative once when they entered.
    cur_pass = state.get("current_pass", 1)
    for enemy in list(state.get("enemy_deckers", [])):
        if scheduled_kind == "ic" or (scheduled_actor_id and enemy.get("id") != scheduled_actor_id):
            continue
        if state.get("run_ended"):
            break
        enemy_passes = _enemy_passes(enemy)
        eligible = (
            enemy.get("status") == "active"
            and enemy.get("spawn_pending_pass") != cur_pass
            and (
                (scheduled_action_index is None
                 and cur_pass <= enemy_passes
                 and enemy.get("acted_pass") != cur_pass)
                or (scheduled_action_index is not None
                    and scheduled_action_index <= enemy_passes)
            )
        )
        if eligible:
            if scheduled_action_index is not None:
                enemy["actions_taken_turn"] = scheduled_action_index
            enemy["acted_pass"] = cur_pass
            state["_acting_init"] = enemy.get("initiative")
            state["_acting_count"] = scheduled_count
            _enemy_decker_take_pass(state, decker, run, enemy)
    # Restore the decker's initiative as the acting context: any events logged after the driver
    # (e.g. a structural new_pass/new_turn line, or a follow-up player action) belong to the decker.
    state["_acting_init"] = _decker_effective_initiative(state)
    state.pop("_acting_count", None)


def _run_reactive_security_followup(
    state: dict,
    decker: dict,
    *,
    action_type: str,
    utility_rating: int,
    sec_code: str,
    det_factor: int,
    preexisting_ic_ids: set[str],
) -> None:
    """Resolve sheaf, Tar, and preexisting Probe reactions in event order."""
    _check_and_activate_sheaf(state, sec_code)
    _run_reactive_activation_sensor_checks(state, decker)
    _autofire_lurking_tar(state, decker, action_type, utility_rating)

    for ic in state.get("active_ic", []):
        if ic["status"] != "active" or ic.get("suppressed"):
            continue
        if ic["type"] != "Probe" or ic.get("id") not in preexisting_ic_ids:
            continue

        probe = eng.probe_test(ic["rating"], det_factor)
        level = _secret_sensor_test(state, decker, ic)
        if probe["tally_increase"] > 0:
            increase = _bump_security_tally(state, probe["tally_increase"])
            tally = state["security_tally"]
            if level >= 3:
                description = (
                    f"Probe-{ic['rating']} IC is examining your data trail and "
                    f"reporting to host security. Tally +{increase} -> {tally}"
                )
            elif level == 2:
                description = (
                    "Probe IC is examining your data trail and notifying security... "
                    f"Tally +{increase} -> {tally}"
                )
            elif level == 1:
                description = (
                    "A hidden IC is quietly probing your actions and alerting the host. "
                    f"Tally +{increase} -> {tally}"
                )
            else:
                description = f"Something is examining your data trail. Tally +{increase} -> {tally}"
            event = {"type": "probe_ic", "description": description, "tally_increase": increase}
            if level >= 1:
                event["ic_id"] = ic["id"]
            _append_event(state, event)
        elif level >= 1 or ic.get("analyzed"):
            _append_event(state, {
                "type": "probe_ic",
                "ic_id": ic["id"],
                "description": (
                    f"The Probe-{ic['rating']} finds no evidence of your actions this turn."
                ),
            })
        _check_and_activate_sheaf(state, sec_code)


def _hold_back_new_hostiles(
    state: dict,
    preexisting_ic_ids: set[str],
    preexisting_enemy_ids: set[str],
) -> None:
    """Keep new hostiles out of the spawning action while preserving initiative order.

    A hostile whose current count is still below the decker's count may act when End Turn closes
    the pass. One whose count is equal or higher has already missed its segment this round.
    """
    current_pass = state.get("current_pass", 1)
    decker_count = _decker_action_count(state)

    def hold(hostile: dict, *, is_ic: bool) -> None:
        wound_mod = _ic_wound_mod(hostile) if is_ic else _enemy_wound_mod(hostile)
        effective = max(0, int(hostile.get("initiative", 0) or 0) - wound_mod)
        passes = _init_passes(effective)
        passed_actions = sum(
            1 for action_index in range(1, passes + 1)
            if effective - 10 * (action_index - 1) >= decker_count
        )
        if passed_actions:
            hostile["actions_taken_turn"] = passed_actions
            hostile["acted_pass"] = current_pass
        if passed_actions < passes:
            hostile["spawn_pending_pass"] = current_pass

    for ic in state.get("active_ic", []):
        if ic.get("id") not in preexisting_ic_ids and "acted_pass" not in ic:
            hold(ic, is_ic=True)
    for enemy in state.get("enemy_deckers", []):
        if enemy.get("id") not in preexisting_enemy_ids and "acted_pass" not in enemy:
            hold(enemy, is_ic=False)


def _release_spawned_hostiles_for_pass(state: dict, current_pass: int) -> None:
    """Allow hostiles with still-upcoming counts to act when the decker ends this pass."""
    for hostile in [*(state.get("active_ic") or []), *(state.get("enemy_deckers") or [])]:
        if hostile.get("spawn_pending_pass") == current_pass:
            hostile.pop("spawn_pending_pass", None)


async def _apply_analysis_action_result(
    state: dict,
    decker: dict,
    run: MatrixRun,
    body: RunActionInput,
    test: dict,
    db: AsyncSession,
) -> None:
    """Apply successful or failed Analyze operation side effects."""
    if body.action_type == "analyze_ic" and test["success"]:
        # A discovered Scramble can be Analyzed to learn its RATING (= the Decrypt target number).
        # Its variant (Poison vs Exploding) was already revealed when the Scramble was discovered
        # (Analyze Icon on the file, or Analyze Subsystem for a subsystem-wide Scramble).
        scr_ref = body.target_ic_id or ""
        scramble = None
        for index, s in enumerate(state.get("scrambles") or []):
            if not isinstance(s, dict) or not s.get("discovered"):
                continue
            if scr_ref and (_scramble_ref(index) == scr_ref or s.get("target_key") == scr_ref):
                scramble = s
                break
        if scramble is not None:
            scramble["rating_revealed"] = True
            _append_event(state, {
                "type": "ic_analyzed",
                "description": f"Scramble analyzed -- Rating {int(scramble.get('rating', 0) or 0)}.",
            })
            return
        active = [
            ic for ic in [*(state.get("active_ic") or []), *(state.get("lurking_ic") or [])]
            if ic.get("status") in ("active", "lurking") and _ic_detection_level(ic) > 0
        ]
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

    if body.action_type == "analyze_icon" and test["success"]:
        _apply_analyze_icon(state, target_file=body.target_file or "")

    if body.action_type == "analyze_subsystem" and test["success"]:
        subsystem = body.subsystem
        analyzed_subsystems = set(state.get("analyzed_subsystems") or [])
        analyzed_subsystems.add(subsystem)
        state["analyzed_subsystems"] = sorted(analyzed_subsystems)
        for door in [
            item for item in (state.get("trap_doors") or [])
            if not item.get("discovered") and item.get("subsystem", "slave") == subsystem
        ]:
            door["discovered"] = True
            source_piece = door.get("source_piece") or ""
            _append_event(state, {
                "type": "trap_door_found",
                "trap_door_id": door.get("id"),
                "subsystem": subsystem,
                "source_piece": source_piece,
                "description": (
                    f"Concealed port detected on the {subsystem.capitalize()} subsystem"
                    + (f" ({source_piece})" if source_piece else "")
                    + " -- Destination unknown."
                ),
            })

        for scramble_index, scramble in [
            (index, item) for index, item in enumerate(state.get("scrambles") or [])
            if not item.get("discovered")
            and _scramble_subsystem(item.get("target_key", "")) == subsystem
            # An individual-file Scramble (files::file::<id>) rides a specific file icon, so it is an
            # Analyze ICON finding (which also reveals its variant + any linked bomb). Analyze
            # Subsystem surfaces only node-level scrambles: the whole Files datastore (files::entire)
            # and Access-subsystem/piece scrambles.
            and not str(item.get("target_key", "")).startswith("files::file::")
        ]:
            scramble["discovered"] = True
            scramble["variant_revealed"] = True
            player_label = _scramble_player_label(state, scramble.get("target_key", ""))
            is_exploding = scramble.get("variant") == "exploding"
            _append_event(state, {
                "type": "scramble_found",
                "scramble_ref": _scramble_ref(scramble_index),
                "subsystem": subsystem,
                "variant": scramble.get("variant"),
                "description": (
                    f"{'Exploding' if is_exploding else 'Poison'} Scramble IC found on the "
                    f"{subsystem.capitalize()} subsystem ({player_label}). "
                    + ("Defuse its linked data bomb first, then decrypt."
                       if is_exploding else
                       "Decrypt it before operating on the protected data.")
                ),
            })
            if is_exploding:
                linked = _armed_bomb_on_file(state, scramble)
                if linked is not None and not linked.get("discovered"):
                    linked["discovered"] = True
                    _append_event(state, {
                        "type": "data_bomb_found",
                        "subsystem": subsystem,
                        "description": (
                            "Analyze Subsystem -- the Exploding Scramble's linked data bomb is armed "
                            "on this datastore. Defuse it before you decrypt or download."
                        ),
                    })

        # Standalone subsystem-wide Data Bombs (planted directly in the designer, not linked to a
        # Scramble) surface on the same Analyze Subsystem that reveals the subsystem's other
        # defenses: the Files datastore bomb on a Files analyze, an Access-subsystem bomb on an
        # Access analyze. (Per-file bombs stay an Analyze Icon finding.)
        for bomb in (state.get("data_bombs") or []):
            if not isinstance(bomb, dict) or bomb.get("discovered"):
                continue
            bscope, bname = _data_bomb_scope_name(bomb.get("target", ""))
            reveal = (
                (subsystem == "files" and bscope == "files" and bname == "__entire__")
                or (subsystem == "access" and bscope == "access")
            )
            if not reveal:
                continue
            bomb["discovered"] = True
            _append_event(state, {
                "type": "data_bomb_found",
                "subsystem": subsystem,
                "description": (
                    f"Analyze Subsystem -- a data bomb is armed on the {subsystem.capitalize()} "
                    "subsystem. Defuse it before you "
                    + ("download or edit a file."
                       if subsystem == "files" else
                       "log off, transit a trap door, or validate a passcode.")
                ),
            })

        if subsystem == "access" and not state.get("host_ltg_revealed"):
            state["host_ltg_revealed"] = True
            host = await _get_host_or_404(db, run.host_id)
            address = str(getattr(host, "ltg_address", "") or "").strip()
            if address:
                if not host.is_visible_to_players:
                    host.is_visible_to_players = True
                    await sync_host_reveal_to_org(db, host)
                state["host_has_ltg"] = True
                state["host_ltg_address"] = address
                _append_event(state, {
                    "type": "host_ltg_revealed",
                    "has_ltg": True,
                    "ltg_address": address,
                    "description": (
                        f"Access subsystem analyzed -- this host has dedicated LTG access at {address}."
                    ),
                })
            else:
                state["host_has_ltg"] = False
                _append_event(state, {
                    "type": "host_ltg_revealed",
                    "has_ltg": False,
                    "description": "Access subsystem analyzed -- this host has no LTG access.",
                })

    if (
        body.action_type == "analyze_subsystem"
        and not test["success"]
        and body.subsystem == "access"
        and not state.get("host_ltg_revealed")
    ):
        _append_event(state, {
            "type": "access_analysis_blocked",
            "description": (
                "Access subsystem analysis failed -- the host blocked the discovery attempt."
            ),
        })

    if body.action_type == "analyze_host" and test["success"]:
        security_was_revealed = bool(state.get("host_security_revealed"))
        _apply_analyze_host(state, test["decker_roll"]["successes"])
        if state.get("host_security_revealed") and not security_was_revealed:
            host = await _get_host_or_404(db, run.host_id)
            await sync_host_security_to_org(db, host, mark_revealed=True)

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
                f"alert status {snapshot['alert'].capitalize()} (as of round {snapshot['turn']})."
            ),
        })


def _apply_control_action_result(
    state: dict,
    decker: dict,
    run: MatrixRun,
    body: RunActionInput,
    test: dict,
) -> None:
    """Apply control and status operation side effects."""
    if body.action_type == "crash_host" and test["success"]:
        successes = int(test["decker_roll"]["successes"])
        turns = -(-10 // successes)
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

    if body.action_type == "validate_passcode" and test["success"]:
        state["has_legitimate_status"] = True
        _append_event(state, {
            "type": "validate_passcode",
            "success": True,
            "description": "Validate Passcode successful -- Legitimate status granted.",
        })
        # A successful Validate Passcode is an Access operation -- an undefused Access-subsystem
        # Exploding Scramble's linked bomb goes off now (analyze + defuse first to be safe).
        _trigger_access_subsystem_bomb(state, decker, op_label="validate passcode")
    elif body.action_type == "validate_passcode":
        _append_event(state, {
            "type": "validate_passcode",
            "success": False,
            "description": "Validate Passcode failed -- the host rejects your injected passcode.",
        })

    if body.action_type == "invalidate_passcode" and test["success"]:
        whole_list = body.target_ic_id == _INVALIDATE_ALL
        flipped = _invalidate_passcodes(state, None if whole_list else body.target_ic_id)
        if whole_list:
            description = (
                "Host passcode table erased -- every host IC on the system is treated as an intruder "
                "(revised to-hit TN), including any IC that activates later this run."
            )
        elif not flipped:
            description = (
                "Invalidate Passcode succeeded, but no Legitimate security icon was affected "
                "(target already Intruding, crashed, or gone)."
            )
        else:
            description = (
                f"Invalidate Passcode successful -- {flipped[0]}'s passcode is erased; it flips "
                "to Intruding (revised to-hit TN) for the rest of the run."
            )
        _append_event(state, {
            "type": "invalidate_passcode",
            "success": True,
            "whole_list": whole_list,
            "flipped": flipped,
            "description": description,
        })
    elif body.action_type == "invalidate_passcode":
        _append_event(state, {
            "type": "invalidate_passcode",
            "success": False,
            "description": "The host rejected your attempt to delete the passcode table.",
        })

    if body.action_type == "decoy" and test["success"]:
        successes = test["decker_roll"]["successes"]
        state["decoy_successes"] = successes
        state["decoy_hp"] = 0
        _append_event(state, {
            "type": "decoy_deployed",
            "description": (
                f"Decoy deployed with {_successes(successes)}. Each proactive IC attack: roll "
                "1D6 -- if result <= successes, IC hits decoy (10-box CM)."
            ),
            "successes": successes,
        })

    if body.action_type == "relocate" and test["success"]:
        eligible = [
            ic for ic in state.get("active_ic", [])
            if ic["status"] == "active"
            and _ic_is_trace(ic)
            and ic.get("trace_phase") == "locate"
        ]
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
                        f"Relocate: {target['type']}-{target['rating']} is already suppressed."
                    ),
                })
            elif _base_detection_factor(state, decker) - _suppressed_count(state) <= 1:
                target["trace_spoofed_turn"] = state.get("current_turn", 1)
                target["relocate_suppress_pending"] = True
                _append_event(state, {
                    "type": "relocate",
                    "ic_id": target["id"],
                    "description": (
                        f"Relocate succeeded -- {target['type']}-{target['rating']} spoofed for this "
                        "turn. Suppress is held: Detection Factor is at its minimum."
                    ),
                })
            else:
                target["suppressed"] = True
                target["suppress_mode"] = "trace"
                state["detection_factor"] = _effective_detection_factor(state, decker)
                _append_event(state, {
                    "type": "ic_suppressed",
                    "ic_id": target["id"],
                    "description": (
                        f"Relocate succeeded -- {target['type']}-{target['rating']} suppressed "
                        "(trace paused in place; -1 Detection Factor; resumes if released)."
                    ),
                })
        else:
            target["trace_spoofed_turn"] = state.get("current_turn", 1)
            _append_event(state, {
                "type": "relocate",
                "ic_id": target["id"],
                "description": f"{target['type']}-{target['rating']} spoofed for this turn.",
            })

    if body.action_type == "redirect_datatrail" and test["success"]:
        state["redirects_placed"] = 1
        _append_event(state, {
            "type": "redirect_placed",
            "description": "Host redirect successfully placed. Trace Factor +1.",
            "redirects_total": state["redirects_placed"],
        })


def _apply_file_action_result(
    state: dict,
    decker: dict,
    run: MatrixRun,
    body: RunActionInput,
    test: dict,
) -> None:
    """Apply discovery, file-editing, and download operation side effects."""
    if body.action_type == "locate_paydata" and test["success"]:
        # Locate Paydata is the RANDOM loot sweep (vr2 L1888). It deliberately never surfaces
        # KEY/target files -- those are mission data you must know to look for, found only via
        # Locate File (Browse). So is_key files are excluded from the pool here.
        pool = [
            paydata for paydata in (state.get("paydata") or [])
            if not paydata.get("located") and not paydata.get("destroyed")
            and not paydata.get("is_key")
        ]
        if pool:
            net_successes = int(test["decker_net_successes"])
            already_located = sum(
                1 for paydata in (state.get("paydata") or [])
                if paydata.get("located") and not paydata.get("is_key")
            )
            seed = (
                (int(getattr(run, "id", 0) or 0) * 1_000_003)
                ^ (int(state.get("current_turn", 0) or 0) * 8191)
                ^ (int(state.get("security_tally", 0) or 0) * 131)
                ^ (already_located * 17)
            )
            newly_located = random.Random(seed).sample(pool, min(net_successes, len(pool)))
            parts, files_payload = [], []
            for paydata in newly_located:
                paydata["located"] = True
                # Locate reveals only the file's NAME. Its size (Mp) and whether it is encrypted stay
                # hidden until the decker runs an Analyze Icon on it (see C) -- do not leak them here.
                disp = str(paydata.get("name", "?"))
                parts.append(disp)
                files_payload.append({"name": disp, "is_key": bool(paydata.get("is_key"))})
            all_found = not any(
                not paydata.get("located") and not paydata.get("destroyed")
                and not paydata.get("is_key")
                for paydata in (state.get("paydata") or [])
            )
            _append_event(state, {
                "type": "paydata_located",
                "description": "Paydata located: " + ", ".join(parts) + "."
                    + (" All paydata on this host is now located." if all_found else ""),
                "all_located": all_found,
                "files": files_payload,
            })
        else:
            _append_event(state, {
                "type": "paydata_located",
                "description": "Search complete -- no further paydata found.",
            })

    if body.action_type == "locate_file" and test["success"]:
        # Locate File (Index / Browse, vr2 L1885): finds specific KNOWN target files -- the mission
        # data the decker came for -- which the random Locate Paydata sweep never surfaces. A
        # success reveals every not-yet-located target (is_key) file on the host.
        targets = [
            paydata for paydata in (state.get("paydata") or [])
            if paydata.get("is_key") and not paydata.get("located")
            and not paydata.get("destroyed")
        ]
        if targets:
            parts, files_payload = [], []
            for paydata in targets:
                paydata["located"] = True
                # Name only -- size + encryption stay hidden until an Analyze Icon on the file (see C).
                disp = str(paydata.get("name", "?"))
                parts.append(disp)
                files_payload.append({"name": disp, "is_key": True})
            _append_event(state, {
                "type": "file_located",
                "description": "Target file located: " + ", ".join(parts) + ".",
                "files": files_payload,
            })
        else:
            _append_event(state, {
                "type": "file_located",
                "description": "Search complete -- no target file found for that search goal.",
            })

    if body.action_type == "locate_ic":
        _apply_locate_ic(
            state,
            test_success=test["success"],
            target_ic_id=body.target_ic_id or "",
        )

    if body.action_type == "locate_decker":
        _apply_locate_decker(
            state,
            decker,
            test_success=test["success"],
            scanner=_effective_program_rating(decker, state, "scanner"),
        )

    if body.action_type == "edit_file" and test["success"] and body.target_file:
        paydata = _paydata_for_target(state, body.target_file)
        if paydata is not None and paydata.get("destroyed"):
            paydata = None
        if paydata is not None:
            if (body.edit_mode or "erase").strip().lower() == "modify":
                paydata["tampered"] = True
                _append_event(state, {
                    "type": "file_modified",
                    "file_name": paydata.get("name"),
                    "description": f"File \"{paydata.get('name')}\" altered on the host successfully.",
                })
            else:
                paydata["destroyed"] = True
                _append_event(state, {
                    "type": "file_deleted",
                    "file_name": paydata.get("name"),
                    "description": f"File \"{paydata.get('name')}\" erased from the host.",
                })

    if body.action_type == "download_data" and test["success"] and body.target_file:
        paydata = _paydata_for_target(state, body.target_file)
        if paydata is not None and paydata.get("destroyed"):
            paydata = None
        if paydata is not None and not paydata.get("downloaded"):
            density = max(0, int(paydata.get("density", 0) or 0))
            compressor = _effective_compressor(decker)
            stored, compressible = _compressed_store_size(compressor, density)
            turns = _download_turns(decker, stored)
            if turns <= 1:
                _complete_download(state, decker, paydata)
            else:
                state["active_download"] = {
                    "file_id": paydata.get("id"),
                    "file": paydata.get("name"),
                    "stored_mp": stored,
                    "full_mp": density,
                    "compressed": compressible,
                    "is_key": bool(paydata.get("is_key")),
                    "turns_total": turns,
                    "turns_left": turns - 1,
                    "started_turn": state.get("current_turn", 1),
                }
                _append_event(state, {
                    "type": "download_started",
                    "file_name": paydata.get("name"),
                    "size_mp": stored,
                    "turns_total": turns,
                    "turns_left": turns - 1,
                    "description": f"Downloading of \"{paydata.get('name')}\" beginning. {turns} turns until completion.",
                })
        elif paydata is not None:
            _append_event(state, {
                "type": "data_downloaded",
                "file_name": paydata.get("name"),
                "description": (
                    f"\"{paydata.get('name')}\" already downloaded -- no additional storage used."
                ),
            })


def _apply_direct_action(
    state: dict,
    decker: dict,
    body: RunActionInput,
    *,
    eff: dict,
    subsystem_rating: int,
    decker_pool: int,
    sec_code: str,
    sec_value: int,
    det_factor: int,
) -> tuple[bool, dict | None]:
    """Resolve an action that must not enter the generic System Test pipeline."""
    if body.action_type in {"swap_memory", "unload_program"}:
        new_decker = copy.deepcopy(decker)
        if body.action_type == "swap_memory":
            changed, description = _apply_swap_memory(
                state,
                new_decker,
                target_program=body.target_program,
                swap_out_program="",
            )
        else:
            changed, description = _apply_swap_memory(
                state,
                new_decker,
                target_program="",
                swap_out_program=body.target_program,
            )
        _append_event(state, {"type": "swap_memory", "description": description})
        return True, new_decker if changed else None

    if body.action_type == "medic":
        _apply_medic(state, decker, hacking_pool_dice=body.hacking_pool_dice)
        return True, None

    if body.action_type == "restore":
        _apply_restore(
            state, decker, target=body.target_program,
            hacking_pool_dice=body.hacking_pool_dice,
        )
        return True, None

    if body.action_type == "disinfect":
        _apply_disinfect(
            state,
            decker,
            subsystem=body.subsystem,
            subsystem_rating=subsystem_rating,
            decker_pool=decker_pool,
            sec_value=sec_value,
            det_factor=det_factor,
            target_ic_id=body.target_ic_id,
        )
        return True, None

    if body.action_type == "defuse_data_bomb":
        defuse_subsystem = _defuse_target_subsystem(state, body.target_file) or body.subsystem
        _apply_defuse_bomb(
            state,
            decker,
            eff,
            subsystem=defuse_subsystem,
            subsystem_rating=_subsystem_rating(state, defuse_subsystem),
            decker_pool=decker_pool,
            sec_value=sec_value,
            sec_code=sec_code,
            target_file=body.target_file,
        )
        return True, None

    if body.action_type == "steamroller":
        _apply_steamroller(
            state,
            decker,
            sec_code=sec_code,
            decker_pool=decker_pool,
            target_ic_id=body.target_ic_id,
        )
        return True, None

    if body.action_type == "slow":
        _apply_slow(
            state,
            decker,
            sec_code=sec_code,
            decker_pool=decker_pool,
            target_ic_id=body.target_ic_id,
        )
        return True, None

    if body.action_type == "decompress_file":
        # Decompress applies ONLY to a Squeezed program held in active memory -- never to a
        # downloaded paydata file (a compressed file rides out compressed; the buyer expands it).
        new_decker = copy.deepcopy(decker)
        changed = _apply_decompress_program(
            state, new_decker, target_program=body.target_program)
        return True, new_decker if changed else None

    if body.action_type == "dinab":
        _apply_dinab(
            state,
            decker,
            util=body.target_program,
            sec_code=sec_code,
            sec_value=sec_value,
            subsystem=body.subsystem,
            subsystem_rating=subsystem_rating,
            det_factor=det_factor,
            target_ic_id=body.target_ic_id,
            target_file=body.target_file,
        )
        return True, None

    if body.action_type == "purge_hog":
        all_infections = state.get("hog_infections") or []
        infections = [
            infection for infection in all_infections
            if infection.get("target_id", "pc") == "pc"
        ]
        if not infections:
            _append_event(state, {"type": "purge_hog", "description": "No Hog virus to purge."})
        else:
            infection = next(
                (
                    item for item in infections
                    if item.get("id") == body.target_program
                ),
                infections[0],
            )
            program_damage = state.setdefault("program_damage", {})
            name, _ = _highest_running_utility(decker, program_damage)
            base_rating = (decker.get("utilities") or {}).get(name, 0) if name else 0
            purge = eng.hog_purge_test(
                computer_skill=decker_pool,
                hog_rating=infection.get("rating", 4),
                infected_program_rating=base_rating,
                hardening=decker.get("hardening", 0),
            )
            if purge["purged"]:
                state["hog_infections"] = [
                    item for item in all_infections if item is not infection
                ]
                if name:
                    program_damage[name] = base_rating
                description = (
                    f"Purged Hog-{infection.get('rating')} (TN {purge['tn']}) -- virus removed; "
                    f"the {_action_label(name) if name else 'infected'} program is "
                    "wiped (reload via Swap Memory)."
                )
            else:
                description = "You are unable to purge the Hog virus from your deck."
            _append_event(state, {
                "type": "purge_hog",
                "decker_roll": purge["roll"],
                "description": description,
            })
        return True, None

    if body.action_type != "decrypt_file":
        return False, None

    scrambles = state.get("scrambles") or []
    discovered = [
        (index, scramble) for index, scramble in enumerate(scrambles)
        if scramble.get("discovered")
    ]
    scramble = None
    if body.target_file:
        scramble = next(
            (item for index, item in discovered
             if _scramble_ref(index) == body.target_file or item.get("target_key") == body.target_file),
            None,
        )
        if scramble is None:
            wanted = _target_file_name(body.target_file).strip().lower()
            scramble = next(
                (
                    item for _, item in discovered
                    if _target_file_name(item.get("target_key", "")).strip().lower() == wanted
                ),
                None,
            )
    if scramble is None:
        _append_event(state, {
            "type": "decrypt",
            "success": False,
            "description": (
                "No discovered scramble on that target -- Analyze the Files/Slave subsystem first."
            ),
        })
        return True, None

    decrypt_test = eng.scramble_decrypt_test(
        decker_pool=decker_pool,
        scramble_rating=scramble.get("rating", 6),
        decrypt_utility=_effective_program_rating(decker, state, "decrypt"),
    )
    decrypted = decrypt_test["decrypted"]

    # Exploding Scramble (vr2 L491): "if decrypted OR crashed without defusing first: boom." The
    # linked data bomb detonates on ANY decrypt attempt -- success OR failure -- unless it was
    # DEFUSED first (Analyze Icon to find it, then Defuse Data Bomb). Defuse it, then decrypt safe.
    if scramble.get("variant") == "exploding":
        linked_bomb = _armed_bomb_on_file(state, scramble)
        if decrypted:
            state["scrambles"] = [item for item in scrambles if item is not scramble]
        if linked_bomb is not None:
            state["data_bombs"] = [
                b for b in (state.get("data_bombs") or []) if b is not linked_bomb
            ]
            _append_event(state, {
                "type": "decrypt",
                "success": bool(decrypted),
                "decker_roll": decrypt_test["roll"],
                "description": (
                    "Decrypt succeeded -- and the attached data bomb detonates!" if decrypted else
                    "Decrypt failed -- and the attached data bomb detonates!"
                ),
            })
            _detonate_data_bomb(
                state, decker, eff,
                ic_rating=linked_bomb.get("rating", scramble.get("rating", 6)),
                sec_value=sec_value, sec_code=sec_code,
                headline="Exploding Scramble's linked data bomb",
            )
        else:
            _append_event(state, {
                "type": "decrypt",
                "success": bool(decrypted),
                "decker_roll": decrypt_test["roll"],
                "description": (
                    "Scramble decrypted -- protected data accessible." if decrypted else
                    "Decrypt failed -- the Scramble holds. Try again."
                ),
            })
        return True, None

    # Poison Scramble: a SUCCESSFUL decrypt clears it; a FAILED decrypt lets the IC make its Poison
    # Test (IC rating vs your Computer skill) -- a success destroys the protected data.
    if decrypted:
        state["scrambles"] = [item for item in scrambles if item is not scramble]
        _append_event(state, {
            "type": "decrypt",
            "success": True,
            "decker_roll": decrypt_test["roll"],
            "description": "Scramble decrypted -- protected data accessible.",
        })
        return True, None

    target_key = scramble.get("target_key", "")
    protected_files = _scramble_protected_files(state, scramble)
    any_key = any(bool(f.get("is_key")) for f in protected_files)
    consequence = eng.scramble_failure_consequence(
        variant=scramble["variant"],
        is_key=any_key,
        scramble_rating=scramble.get("rating", 6),
        decker_computer_skill=decker.get("computer_skill", 6),
    )
    destroyed = bool(consequence.get("data_destroyed"))
    if destroyed:
        for f in protected_files:
            f["destroyed"] = True
    entire = target_key == "files::entire"
    _append_event(state, {
        "type": "decrypt",
        "success": False,
        "decker_roll": decrypt_test["roll"],
        "key_data_lost": consequence.get("key_data_lost", False),
        "data_destroyed": destroyed,
        "file_name": (protected_files[0].get("name") if (protected_files and not entire) else None),
        "files_destroyed": ([f.get("name") for f in protected_files] if destroyed else []),
        "description": (
            "Decrypt failed and the Poison IC has erased all files on the host."
            if (entire and destroyed) else consequence["message"]
        ),
    })
    return True, None


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
    state["_acting_init"] = _decker_effective_initiative(state)

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
    if body.action_type != "logon_to_host":
        _assert_logged_on(state)

    _assert_known_action_target(state, body)
    _assert_hp_eligible(body.action_type, body.hacking_pool_dice)

    # Graceful Logoff is its own Access Test (not a generic subsystem op), so resolve it via
    # the shared helper and return -- mirroring POST /{run_id}/logoff. Without this the
    # graceful_logoff action fell through to the generic test below and never actually ended
    # the run.
    if body.action_type == "graceful_logoff":
        _spend_pass_action(state, "graceful_logoff")   # vr2: Graceful Logoff is a Complex Action
        success = _apply_graceful_logoff(
            state, decker,
            hacking_pool_dice=body.hacking_pool_dice,
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
    # player isn't charged a pass for an impossible download. storage_free_mp < 0 = untracked. A
    # still-encrypted file is skipped here -- the attempt won't transfer any data (it only reveals
    # the Scramble / trips its bomb), so storage is irrelevant to it.
    if body.action_type == "download_data" and body.target_file:
        free = state.get("storage_free_mp", -1)
        if (free is not None and free >= 0
                and _file_scramble_for_target(state, body.target_file) is None):
            pd = _paydata_for_target(state, body.target_file)
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
                f"{_dl.get('turns_left')} round"
                f"{'s' if _dl.get('turns_left') != 1 else ''} left). "
                "Finish or abandon it before starting another.")
        raise HTTPException(
            400,
            f"Download in progress (\"{_dl.get('file')}\", {_dl.get('turns_left')} round"
            f"{'s' if _dl.get('turns_left') != 1 else ''} left) -- "
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

    # Download / Edit of a file still covered by an undecrypted Scramble IC (vr2): the decker MAY
    # attempt it, but the encrypted data is unreadable -- the attempt only DISCOVERS the Scramble
    # (the file's card now offers Decrypt) and, for an undefused EXPLODING Scramble, trips its
    # linked data bomb. Resolve it here and return, so it never runs the normal Files System Test.
    if body.action_type in ("download_data", "edit_file") and body.target_file:
        _cover = _file_scramble_for_target(state, body.target_file)
        if _cover is not None:
            _spend_pass_action(state, body.action_type)
            _apply_scrambled_file_access(state, decker, body, _cover)
            if state.get("run_ended"):
                run.status = state.get("end_reason", "crashed")
            run.state_json = state
            await db.commit()
            await db.refresh(run)
            return _serialize_run(run, auth)

    # Action economy: spend this action's cost from the current initiative phase. End Turn advances
    # the shared clock; an exhausted budget blocks until then. vr2: 2 Simple OR 1 Complex + 1 Free.
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
        _spend_hp(state, body.hacking_pool_dice)
        _apply_maneuver(state, decker, eff, body)
        run.decker_json = copy.deepcopy(decker)
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
    utility_rating = _effective_action_utility(decker, state, body.action_type)
    tn_modifier = -utility_rating
    # Analyze Icon (Control test) is uniquely sharpened by the decker's gear: vr2 reduces its TN
    # by the Sensor rating IN ADDITION to the Analyze utility (already applied above). The rules
    # floor of "minimum TN of 2" is enforced by system_test's max(2, ...) clamp.
    if body.action_type == "analyze_icon":
        tn_modifier -= eff.get("sensor", 0)

    # Invalidate Passcode: erasing the ENTIRE host passcode list at once (the "__all__" target) is a
    # +4 TN Control test (vr2 L1879); erasing a single passcode runs at the base TN.
    if body.action_type == "invalidate_passcode" and body.target_ic_id == _INVALIDATE_ALL:
        tn_modifier += 4

    direct_event_start = len(state.get("event_log") or [])
    handled, replacement_decker = _apply_direct_action(
        state,
        decker,
        body,
        eff=eff,
        subsystem_rating=subsystem_rating,
        decker_pool=pool,
        sec_code=sec_code,
        sec_value=sec_value,
        det_factor=det_factor,
    )
    if handled:
        emitted_host_test = any(
            isinstance(event, dict) and event.get("host_system_test")
            for event in (state.get("event_log") or [])[direct_event_start:]
        )
        if emitted_host_test:
            _run_reactive_security_followup(
                state,
                decker,
                action_type=body.action_type,
                utility_rating=_effective_action_utility(
                    decker, state, body.action_type, body.target_program),
                sec_code=sec_code,
                det_factor=det_factor,
                preexisting_ic_ids=_preexisting_ic_ids,
            )
        else:
            _run_reactive_activation_sensor_checks(state, decker)
        if replacement_decker is not None:
            run.decker_json = replacement_decker
        else:
            run.decker_json = copy.deepcopy(decker)
        run.state_json = state
        await db.commit()
        await db.refresh(run)
        return _serialize_run(run, auth)

    # Console access additionally halves the host Security Value for Access Tests (vr2).
    test_sec_value = sec_value
    if body.subsystem == "access" and state.get("console_access"):
        test_sec_value = -(-sec_value // 2)
    # Stolen linked passcode + a Deception utility: -2 TN to Logon to Host (vr2).
    if (body.action_type == "logon_to_host" and utility_rating > 0
            and state.get("linked_passcode")):
        tn_modifier -= 2

    test = eng.system_test(
        decker_pool=pool,
        subsystem_rating=subsystem_rating,
        security_value=test_sec_value,
        det_factor=det_factor,
        extra_tn_modifier=tn_modifier,
    )
    # Locate Paydata requires positive net successes: each one locates one additional Paydata
    # Point, and repeated uses accumulate until every point on the host has been located.
    if body.action_type == "locate_paydata" and test["decker_net_successes"] <= 0:
        test["success"] = False

    # Update tally (accelerated by any completed Trace)
    applied = _bump_security_tally(state, test["tally_increase"])

    # Human label for the event log. Analyze Subsystem names its targeted subsystem (e.g.
    # "Analyze Subsystem - Files") so the player can easily re-reference which one they probed.
    action_label = _action_label(body.action_type)
    if body.action_type == "analyze_subsystem" and body.subsystem:
        action_label += f" - {body.subsystem.replace('_', ' ').title()}"

    player_success_action = body.action_type in ("analyze_host", "crash_host")
    result_detail = (
        f"Player Successes: {test['decker_roll']['successes']}."
        if player_success_action
        else f"Net Successes: {test['decker_net_successes']}."
    )
    log_entry: dict[str, Any] = {
        "type": "action",
        "host_system_test": True,
        "action": body.action_type,
        "action_label": action_label,
        "subsystem": body.subsystem,
        "description": (
            f"{action_label} -- "
            f"{'SUCCESS' if test['success'] else 'FAILED'} "
            f"({test['decker_roll']['successes']} vs {test['host_roll']['successes']} successes). "
            f"{result_detail} "
            f"Tally +{applied} -> {state['security_tally']}."
        ),
        "success": test["success"],
        "net_successes": test["decker_net_successes"],
        "target_number": test["decker_roll"].get("tn"),
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
    await _apply_analysis_action_result(state, decker, run, body, test, db)
    _apply_control_action_result(state, decker, run, body, test)
    _apply_file_action_result(state, decker, run, body, test)

    # Data Bomb trigger (vr2_rules.md L473): a SUCCESSFUL access (Download/Edit/Upload) of a file
    # or Slave device that still carries an UNDEFUSED bomb sets it off -- the decker gets the
    # access AND eats the blast. A FAILED access does NOT trigger it, and a bomb already disarmed
    # (via the Defuse Data Bomb action) is inert. Detonation adds the bomb's rating to the tally.
    _trigger_access_data_bomb(
        state, decker, eff, action_type=body.action_type, target_file=body.target_file or "",
        test_success=test["success"], sec_value=sec_value, sec_code=sec_code)

    _run_reactive_security_followup(
        state,
        decker,
        action_type=body.action_type,
        utility_rating=utility_rating,
        sec_code=sec_code,
        det_factor=det_factor,
        preexisting_ic_ids=_preexisting_ic_ids,
    )
    if _prog_key:
        _spend_one_shot(state, decker, _prog_key)

    # vr2 initiative: any IC that first appeared DURING this action (a sheaf trigger, a trap-door
    # reveal, etc. -- its ID is absent from _preexisting_ic_ids) has not yet reached its own
    # initiative segment, so it must not act in the pass it spawned. Stamp it as already-acted THIS
    # pass so the NPC driver below holds it back; new_turn clears acted_pass, so it takes its first
    # real action on its next pass/turn. Mirrors the Probe rule that a just-spawned Probe does not
    # test the action that created it.
    _hold_back_new_hostiles(state, _preexisting_ic_ids, _preexisting_enemy_ids)

    # Logon is the entry step, not one of the player's Round 1 actions. Establish the session and
    # refresh its action budget, then run only hostile counts ABOVE the player's effective first
    # count. Ties and lower counts wait until the player closes the phase, just as in later rounds.
    logon_completed = body.action_type == "logon_to_host" and test["success"]
    if logon_completed:
        _complete_logon(state, decker, det_factor)
        _advance_npc_count_window(
            state, decker, run,
            eff=eff, sec_code=sec_code, sec_value=sec_value, det_factor=det_factor,
            upper_count=None, lower_count=_decker_action_count(state),
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
    run.decker_json = copy.deepcopy(decker)
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
    # Keep the parked strike on its attacker's original initiative count.
    state["_acting_init"] = pending.get("acting_init", _decker_effective_initiative(state))
    state["_acting_count"] = pending.get("acting_count")
    sec_code = state["host_security_code"]
    sec_value = state["host_security_value"]
    det_factor = _effective_detection_factor(state, decker)
    eff = _get_decker_effective(decker, state)

    ctx = pending.get("ctx", {})
    # Hacking Pool dice applied to the icon's resistance. Reject an over-request (block, don't
    # clamp) to match every other spendable-resource path in the app -- _spend_hp raises 400 when
    # the pool is short. 0 = resist with Bod alone / decline the offer.
    hp = int(body.hacking_pool_dice or 0)
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
            effect_type=ctx.get("effect_type"),
            effect_rating=ctx.get("effect_rating"),
        )
    else:
        # The parked IC vanished (crashed/suppressed between park and defend) -- nothing to resolve;
        # just resume the pass so the remaining hostiles still act.
        run_ended = bool(state.get("run_ended"))

    # Resume the remaining globally ordered count window. Legacy/logon prompts predate count-window
    # scheduling and retain the old pass resume so existing runs remain compatible.
    if not run_ended:
        phase_transition = pending.get("resume_phase_transition")
        resume_window = pending.get("resume_count_window")
        if isinstance(resume_window, dict):
            _advance_npc_count_window(
                state, decker, run,
                eff=eff, sec_code=sec_code, sec_value=sec_value, det_factor=det_factor,
                upper_count=resume_window.get("upper_count"),
                lower_count=int(resume_window.get("lower_count", 0) or 0),
                allow_defense_pause=True,
            )
        else:
            _advance_npc_pass(
                state, decker, run,
                eff=eff, sec_code=sec_code, sec_value=sec_value, det_factor=det_factor,
                logon_completed=bool(pending.get("resume_logon_completed")),
                allow_defense_pause=True,
            )
        if state.get("pending_defense") and phase_transition:
            state["pending_defense"]["resume_phase_transition"] = phase_transition
        elif not state.get("pending_defense") and isinstance(phase_transition, dict):
            transition_kind = phase_transition.get("kind")
            if transition_kind == "next_pass":
                _open_next_decker_pass(
                    state,
                    int(phase_transition["current_pass"]),
                    int(phase_transition["total_passes"]),
                )
            elif transition_kind == "next_round":
                state = _begin_next_combat_round(state, decker, run, sec_code)
            elif transition_kind == "announce_round":
                _announce_new_combat_round(
                    state,
                    int(phase_transition.get("old_hp", 0) or 0),
                )

    if state.get("run_ended"):
        run.status = state.get("end_reason", "crashed")
    # A run that ends mid-transfer corrupts the in-progress download (a partial copy is worthless).
    if state.get("run_ended") and state.get("active_download"):
        _corrupt_active_download(state)

    run.decker_json = copy.deepcopy(decker)
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
    visibility rule (vr2 Trace IC). A trace is visible and vulnerable while running its Hunt
    Cycle. The instant it hits and enters its Location Cycle it vanishes and becomes reactive;
    only Relocate can affect it then. Non-trace IC: this helper is not used."""
    phase = ic.get("trace_phase", "hunt")
    if phase in ("hunt", "hunting", "hunt_hit"):
        return True
    return False



def _spawn_trap_hidden(state: dict, source_ic: dict, sec_code: str) -> dict | None:
    """Reveal + activate the hidden IC concealed behind a Trap IC (vr2 Trap IC). Spawns a fresh
    active IC (new initiative roll) and logs the trap-trigger. Returns the new IC dict, or None if
    ``source_ic`` carried no ``trap_hidden``. Shared by the cybercombat-crash paths (white/gray trap)
    and the Trace location-cycle-completion path (trace trap)."""
    trap_hidden = source_ic.get("trap_hidden")
    if not trap_hidden:
        return None
    hidden = _normalized_ic_payload(trap_hidden, default_type="Blaster")
    h_type   = hidden["type"]
    h_rating = hidden["rating"]
    options = [str(option).lower() for option in hidden.get("options", [])]
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
        "shield": "shielding" in options or "shield" in options,
        "shift": "shifting" in options or "shift" in options,
        "options": hidden.get("options", []),
        "cascading": bool(hidden.get("cascading")),
        "expert": hidden.get("expert"),
        "mode": hidden.get("mode"),
    }
    state["active_ic"].append(new_ic)
    _append_event(state, {
        "type": "ic_activation",
        "ic_id": new_id,
        "ic_type": h_type,
        "ic_rating": h_rating,
        "is_trap_reveal": True,
        "description": (
            f"Trap triggered -- hidden {h_type}-{h_rating} revealed! "
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
            f"{target_ic['type']}-{target_ic['rating']} crashed. "
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
    _assert_logged_on(state)
    sec_code = state["host_security_code"]
    sec_value = state["host_security_value"]

    if state.get("icon_crashed"):
        raise HTTPException(400, "Your icon is crashed by Black IC -- you can only jack out")
    target_ic = next((ic for ic in state.get("active_ic", []) if ic["id"] == body.target_ic_id), None)
    if not target_ic:
        raise HTTPException(404, f"IC {body.target_ic_id} not found or not active")
    if target_ic["status"] != "active":
        raise HTTPException(400, f"IC {body.target_ic_id} is already {target_ic['status']}")
    # A trace IC that has begun its Location Cycle has vanished and become reactive. It can only
    # be attacked during its Hunt Cycle; Relocate is the operation that affects it while locating.
    if _ic_is_trace(target_ic) and not _trace_is_targetable(target_ic):
        raise HTTPException(
              400, "That trace IC has vanished into its location cycle -- it can only be attacked "
                  "during its hunt cycle; use Relocate while it is locating.")
    # Limit option (vr2): an Attack utility Limited to deckers is useless against IC.
    if (((decker.get("program_options") or {}).get("attack") or {}).get("limit_target")) == "decker":
        raise HTTPException(400, "This Attack utility is Limited to deckers -- it cannot target IC.")
    _one_shot_block(state, decker, "attack")  # a spent One-Shot Attack cannot fire again until reloaded
    _spend_pass_action(state, "attack")        # vr2: a cybercombat attack is a Simple Action
    _assert_not_dinab_locked(state, "attack")  # DINAB per-pass lock: can't hand-fire an Attack DINAB ran
    _record_manual_program(state, "attack")

    _spend_hp(state, body.hacking_pool_dice)
    attack_rating = _effective_program_rating(decker, state, "attack")
    if attack_rating <= 0:
        raise HTTPException(400, "No usable Attack program is loaded")
    attack_pool = attack_rating + body.hacking_pool_dice
    run_trace.trace(
        f"PC attacks {target_ic['type']}-{target_ic['rating']} ({body.target_ic_id}); "
        f"pool {attack_pool} = {attack_rating} attack + {body.hacking_pool_dice} hacking"
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
    # Legitimate host residents, so the PC hits them on the Legitimate column -- unless a
    # whole-system Invalidate Passcode erased the host passcode table (then every IC is Intruding).
    tgt_status = _combat_target_status(target_ic, ic_state=state)
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
    ic_resist_pool = _ic_test_pool(target_ic, sec_value, defense=True)
    ic_armor       = (2 + (2 if opt_area > 0 else 0)) if _ic_has_armor(target_ic) else 0
    # NOTE: cluster_penalty is folded into Power to preserve Party-IC resistance behavior;
    # with no Party cluster it is 0.
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
    net_successes = attack_roll["successes"] - resist_roll["successes"]
    final_dmg   = attack["resistance"]["final_damage_level"]
    boxes       = attack["resistance"]["boxes"]
    run_trace.trace(
        f"damage: {attack_roll['successes']} attack successes vs Power {attack_power} "
        f"(Armor {ic_armor}) -> {resist_roll['successes']} succ -> {final_dmg} ({boxes} boxes)"
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
                f"{target_ic['type']}-{target_ic['rating']} crashed. "
                f"Attack {attack_roll['successes']} vs Resist {resist_roll['successes']}. "
                f"Net Successes: {net_successes}. "
                f"Tally +{applied} -> {state['security_tally']}{skulk_note}"
            ),
            "tally_increase": applied,
            "attack_roll": attack_roll,
            "resist_roll": resist_roll,
            "net_successes": net_successes,
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
                f"Attack {attack_roll['successes']} vs Resist {resist_roll['successes']}. "
                f"Net Successes: {net_successes}. "
                + ("Target resisted all damage." if boxes <= 0
                   else f"Dealt {final_dmg} ({boxes} boxes).")
                + f" IC: {target_ic['boxes']}/10"
            ),
            "attack_roll": attack_roll,
            "resist_roll": resist_roll,
            "net_successes": net_successes,
            "final_damage_level": final_dmg,
            "boxes": boxes,
            "ic_boxes": target_ic["boxes"],
        })

    _spend_one_shot(state, decker, "attack")
    _run_reactive_activation_sensor_checks(state, decker)
    run.state_json = state
    await db.commit()
    await db.refresh(run)
    return _serialize_run(run, auth)


@router.post("/{run_id}/scramble/attack", response_model=MatrixRunRead,
             dependencies=[Depends(trace_action)])
async def crash_scramble(
    run_id: int,
    body: RunScrambleAttackInput,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Crash a DISCOVERED Scramble IC in cybercombat instead of Decrypting it. vr2 L495: crashing a
    Scramble with an Attack program ADDS its rating to the security tally (unlike the quiet Decrypt).
    A POISON Scramble reacts to EACH attack (hit or miss) with its Poison Test, which may erase the
    protected data; an EXPLODING Scramble's linked data bomb detonates when the scramble is crashed
    unless it was defused first (vr2 L491-492)."""
    run = await _get_run_or_404(db, run_id)
    _assert_run_access(run, auth)
    if run.status != "active":
        raise HTTPException(400, "Run is not active")

    state = copy.deepcopy(run.state_json)
    decker = run.decker_json
    _assert_logged_on(state)
    sec_code = state["host_security_code"]
    sec_value = state["host_security_value"]
    if state.get("icon_crashed"):
        raise HTTPException(400, "Your icon is crashed by Black IC -- you can only jack out")

    scrambles = state.get("scrambles") or []
    scramble = None
    for index, s in enumerate(scrambles):
        if not isinstance(s, dict) or not s.get("discovered"):
            continue
        if _scramble_ref(index) == body.scramble_ref or s.get("target_key") == body.scramble_ref:
            scramble = s
            break
    if scramble is None:
        raise HTTPException(404, "No discovered Scramble matches that reference")

    if (((decker.get("program_options") or {}).get("attack") or {}).get("limit_target")) == "decker":
        raise HTTPException(400, "This Attack utility is Limited to deckers -- it cannot target IC.")
    _one_shot_block(state, decker, "attack")
    _spend_pass_action(state, "attack")
    _assert_not_dinab_locked(state, "attack")
    _record_manual_program(state, "attack")
    _spend_hp(state, body.hacking_pool_dice)

    eff = _get_decker_effective(decker, state)
    attack_rating = _effective_program_rating(decker, state, "attack")
    if attack_rating <= 0:
        raise HTTPException(400, "No usable Attack program is loaded")
    attack_pool = attack_rating + body.hacking_pool_dice
    variant = scramble.get("variant")
    rating = int(scramble.get("rating", 6) or 6)
    wound = _decker_wound_mod(state)

    # A Scramble is a plain reactive lock: it resists with the host Security Value (like IC), has no
    # Shield/Shift/Armor/Party mechanics, and is hit on the Legitimate column (host resident).
    attack = eng.cybercombat_attack(
        attacker_pool=attack_pool,
        security_code=sec_code,
        target_status="legitimate",
        target_bod=sec_value,
        armor_rating=0,
        ic_rating=attack_rating,
        attacker_is_ic=False,
        tn_modifier=wound,
        base_damage_level=_attack_damage_level(decker, sec_code),
    )
    attack_roll = attack["attack_roll"]
    resist_roll = attack["resistance"]["resist_roll"]
    net_successes = attack_roll["successes"] - resist_roll["successes"]
    boxes = attack["resistance"]["boxes"]
    scramble["boxes"] = int(scramble.get("boxes", 0) or 0) + boxes
    crashed = scramble["boxes"] >= 10

    _spend_one_shot(state, decker, "attack")

    _append_event(state, {
        "type": "scramble_attack",
        "scramble_ref": body.scramble_ref,
        "success": crashed,
        "attack_roll": attack_roll,
        "resist_roll": resist_roll,
        "net_successes": net_successes,
        "boxes": boxes,
        "scramble_boxes": min(10, scramble["boxes"]),
        "description": (
            f"Attacked Scramble IC: Attack {attack_roll['successes']} vs Resist "
            f"{resist_roll['successes']}. "
            + ("No damage." if boxes <= 0 else f"Dealt {boxes} boxes.")
            + f" Scramble: {min(10, scramble['boxes'])}/10."
        ),
    })

    # vr2 L493 / user ruling: a POISON Scramble reacts to EVERY attack against it (hit or miss) with
    # its erase test -- crashing it is not a clean escape.
    if variant == "poison":
        _scramble_poison_react(state, decker, scramble)

    if crashed:
        state["scrambles"] = [s for s in scrambles if s is not scramble]
        applied = _bump_security_tally(state, rating)
        sup_id = None
        if applied > 0:
            sup = _register_suppression(
                state, source="scramble_crash",
                label=f"Crashed Scramble IC (rating {rating})", rating=applied)
            sup_id = sup.get("id")
        _append_event(state, {
            "type": "scramble_crashed",
            "scramble_ref": body.scramble_ref,
            "tally_increase": applied,
            "suppression_id": sup_id,
            "description": f"Scramble IC crashed. Tally +{applied} -> {state['security_tally']}.",
        })
        # vr2 L491-492: crashing an EXPLODING Scramble sets off its linked data bomb unless defused.
        if variant == "exploding":
            linked = _armed_bomb_on_file(state, scramble)
            if linked is not None:
                state["data_bombs"] = [
                    b for b in (state.get("data_bombs") or []) if b is not linked]
                _detonate_data_bomb(
                    state, decker, eff,
                    ic_rating=int(linked.get("rating", rating) or rating),
                    sec_value=sec_value, sec_code=sec_code,
                    headline="Exploding Scramble's linked data bomb")
        _check_and_activate_sheaf(state, sec_code)

    _run_reactive_activation_sensor_checks(state, decker)
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
        3. Reload a crashed/degraded *active* regular program from its retained storage copy
            (restore its rating after Hog / Tar Baby / degraded Armor-Shield).

     Regular active programs keep a retained storage copy. One-Shot copies are literal inventory:
     loading one removes it from storage, and unloading an unused one returns that copy to storage.
     Raises 400 if active or storage capacity is insufficient.
    """
    utils   = decker.setdefault("utilities", {})
    storage = state.setdefault("storage_programs", [])
    sizes   = state.setdefault("program_sizes", {})
    pd      = state.setdefault("program_damage", {})
    squeezed_active = state.setdefault("squeezed_active", [])
    squeeze_keys = set(state.get("squeeze_keys") or [])
    cap     = int(state.get("active_memory_cap", 0) or 0)

    def _pretty(n: str) -> str:
        return _action_label(n)

    def _active_used() -> int:
        # Usable loaded utilities at full footprint PLUS squeezed (still-compressed) programs at
        # HALF footprint -- they occupy active memory even while unusable, and Decompress pays the
        # rest. Shared with _apply_decompress_program via the module helper.
        return _active_memory_used(state, decker)

    def _store_append(name: str, rating: int, size: int) -> None:
        # A squeezed program returns to storage still flagged so its footprint stays halved and a
        # later reload needs another decompress.
        storage.append({"name": name, "rating": int(rating or 0), "size": int(size or 0),
                        "squeezed": name in squeeze_keys})

    def _storage_footprint(name: str, size: int) -> int:
        full = max(0, int(size or 0))
        return (full + 1) // 2 if name in squeeze_keys else full

    def _release_one_shot_storage(name: str, size: int) -> None:
        free = state.get("storage_free_mp", -1)
        if isinstance(free, int) and free >= 0 and _is_one_shot(decker, name):
            state["storage_free_mp"] = free + _storage_footprint(name, size)

    def _reserve_one_shot_storage(name: str, size: int) -> None:
        free = state.get("storage_free_mp", -1)
        if not isinstance(free, int) or free < 0 or not _is_one_shot(decker, name):
            return
        footprint = _storage_footprint(name, size)
        remaining = max(0, free - int(state.get("storage_used_mp", 0) or 0))
        if footprint > remaining:
            raise HTTPException(
                400,
                f"Not enough deck storage to unload {_pretty(name)}: needs {footprint} Mp but "
                f"only {remaining} Mp remains after downloaded files.",
            )
        state["storage_free_mp"] = free - footprint

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
            active_counts = state.get("one_shot_active")
            if isinstance(active_counts, dict) and _is_one_shot(decker, name):
                count = max(0, int(active_counts.get(name, 0) or 0))
                if count <= 0:
                    return ""
                size = int(sizes.get(name, 0) or 0)
                _reserve_one_shot_storage(name, size)
                _store_append(name, utils.get(name, 0), size)
                active_counts[name] = count - 1
                if active_counts[name] <= 0:
                    utils[name] = 0
                    pd.pop(name, None)
                return f" (swapped one {_pretty(name)} copy out to storage)"
            _store_append(name, utils.get(name, 0), sizes.get(name, 0))
            utils[name] = 0
            pd.pop(name, None)
            return f" (swapped {_pretty(name)} out to storage)"
        ent = _pop_squeezed_active(name)
        if ent is not None:
            _reserve_one_shot_storage(name, int(ent.get("size", 0) or 0))
            _store_append(name, ent.get("rating", 0), ent.get("size", 0))
            return f" (swapped compressed {_pretty(name)} out to storage)"
        return ""

    target   = (target_program or "").strip().lower()
    swap_out = (swap_out_program or "").strip().lower()
    store_entry = next((p for p in storage
                        if str(p.get("name", "")).strip().lower() == target), None)

    # A successful Tar Pit corruption removes EVERY on-deck copy, so refuse an explicit reload by
    # name too. Tar Baby never adds this marker: it destroys active copies but leaves stored copies.
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
        # A squeezed program parks in active memory at HALF its footprint until it is decompressed;
        # a plain program takes its full size. Block the load if it will not fit.
        charge = _squeezed_active_footprint(in_size) if is_squeezed else in_size
        if cap > 0 and _active_used() + charge > cap:
            used = _active_used()
            raise HTTPException(
                400,
                f"Not enough active memory to load {_pretty(target)}: needs {charge} Mp but "
                f"only {max(0, cap - used)} Mp free ({used}/{cap} Mp used). Swap a program out "
                "to free active memory."
            )
        storage.remove(store_entry)
        _release_one_shot_storage(target, in_size)
        if is_squeezed:
            # Parks at HALF its footprint but stays UNUSABLE (out of decker.utilities) until a
            # Decompress action expands it to full (which needs the other half free).
            squeezed_active.append({"name": target,
                                    "rating": int(store_entry.get("rating", 0) or 0),
                                    "size": in_size})
            return True, (f"Swap Memory -- loaded {_pretty(target)} into active memory still "
                          f"COMPRESSED{note}. Decompress it (Complex Action) before use.")
        utils[target] = int(store_entry.get("rating", 0) or 0)
        sizes[target] = in_size
        pd.pop(target, None)   # fresh storage copy -- no accrued damage
        active_counts = state.get("one_shot_active")
        if isinstance(active_counts, dict) and _is_one_shot(decker, target):
            active_counts[target] = int(active_counts.get(target, 0) or 0) + 1
        return True, (f"Swap Memory -- loaded {_pretty(target)} (rating {utils[target]}) into "
                      f"active memory{note}.")

    if swap_out:
        # Mode 2: push an active program to storage (no incoming program) -- usable or compressed.
        if (utils.get(swap_out, 0) or 0) > 0:
            note = _push_active_out(swap_out)
            return True, f"Swap Memory -- moved {_pretty(swap_out)} from active memory to storage."
        ent = _pop_squeezed_active(swap_out)
        if ent is not None:
            _reserve_one_shot_storage(swap_out, int(ent.get("size", 0) or 0))
            _store_append(swap_out, ent.get("rating", 0), ent.get("size", 0))
            return True, (f"Swap Memory -- moved compressed {_pretty(swap_out)} from active memory "
                          "back to storage.")

    # Mode 3: reload a crashed/degraded active program from its storage copy.
    reload_target = target or next((k for k, v in pd.items() if v > 0 and k not in wiped), None)
    if reload_target and pd.get(reload_target, 0) > 0:
        pd[reload_target] = 0
        active_counts = state.get("one_shot_active")
        if isinstance(active_counts, dict) and _is_one_shot(decker, reload_target):
            active_counts[reload_target] = int(active_counts.get(reload_target, 0) or 0) + 1
        return False, (f"Swap Memory -- reloaded {_pretty(reload_target)} from storage; "
                       "rating restored.")
    return False, "Swap Memory -- no program to load or reload."


def _force_resolve_pending_defense(state: dict, decker: dict, run: MatrixRun) -> bool:
    """Immediately resolve a parked IC strike with NO Hacking Pool allocation (Bod resistance
    only). Used when the decker ends the run (graceful logoff / jack out) while a defense is
    pending: the to-hit already landed, so the hit still resolves before the run ends -- the decker
    cannot dodge a landed strike's permanent consequences (MPCP burn / physical damage / dump
    shock) by bailing out. Reuses the parked to-hit verbatim (no re-roll) and does NOT resume the
    rest of the NPC pass (the decker is leaving). Returns True if resolving the strike ended the
    run."""
    pending = state.get("pending_defense")
    if not pending:
        return bool(state.get("run_ended"))
    state["_acting_init"] = _decker_effective_initiative(state)
    eff = _get_decker_effective(decker, state)
    ctx = pending.get("ctx", {})
    sec_code = state.get("host_security_code")
    sec_value = state.get("host_security_value")
    state["pending_defense"] = None
    ic = next((x for x in state.get("active_ic", []) if x.get("id") == pending.get("ic_id")), None)
    if ic is None:
        return bool(state.get("run_ended"))
    return _resolve_ic_cybercombat(
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
        defender_bonus_dice=0,
    )


def _apply_graceful_logoff(
    state: dict,
    decker: dict,
    *,
    hacking_pool_dice: int,
    finalize_run: bool = True,
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

    # Check for operational Trace IC -- suppressed traces are paused and add no direct TN penalty.
    trace_tn_bonus = 0
    trace_tn_concealed = False
    for ic in state.get("active_ic", []):
        if (ic["status"] == "active" and not ic.get("suppressed")
                and "Trace" in ic.get("type", "")):
            trace_tn_bonus = max(trace_tn_bonus, ic["rating"])
            trace_tn_concealed = trace_tn_concealed or _ic_detection_level(ic) < 3

    hp_dice = max(0, int(hacking_pool_dice or 0))
    if "hackingPool_remaining" in state:
        hp_dice = min(hp_dice, max(0, int(state.get("hackingPool_remaining", 0) or 0)))
    _spend_hp(state, hp_dice)
    pool = decker.get("computer_skill", 4) + hp_dice
    deception_base = int((decker.get("utilities") or {}).get("deception", 0) or 0)
    deception_damage = int((state.get("program_damage") or {}).get("deception", 0) or 0)
    deception_utility = max(0, deception_base - deception_damage)
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
        # A successful Access Test is exactly what an undefused Access-subsystem Exploding Scramble's
        # linked bomb waits for -- the decker eats the blast on the way out unless they analyzed and
        # defused it first (a trap-door transit runs this same graceful logoff, so it is covered).
        _trigger_access_subsystem_bomb(state, decker, op_label="graceful logoff")
        state["run_ended"] = True
        state["end_reason"] = "graceful_logoff"
        if finalize_run:
            _finalize_run_end(state)
        state.pop("has_legitimate_status", None)  # Host deletes passcode on logoff
        state["decoy_successes"] = 0
        state["decoy_hp"] = 0
        _append_event(state, {
            "type": "logoff_success",
            "action_label": "Graceful Logoff",
            "subsystem": "access",
            "success": True,
            "net_successes": test["decker_net_successes"],
            "target_number": test["decker_roll"].get("tn"),
            "target_number_concealed": trace_tn_concealed,
            "description": "You complete your logoff from the host. Run complete.",
            "decker_roll": test["decker_roll"],
            "host_roll": test["host_roll"],
            "tally_increase": tally_increase,
        })
    else:
        _append_event(state, {
            "type": "logoff_fail",
            "action_label": "Graceful Logoff",
            "subsystem": "access",
            "success": False,
            "net_successes": test["decker_net_successes"],
            "target_number": test["decker_roll"].get("tn"),
            "target_number_concealed": trace_tn_concealed,
            "description": "The host rejected your logoff request.",
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
    _assert_logged_on(state)
    if state.get("icon_crashed"):
        raise HTTPException(400, "Your icon is crashed by Black IC -- you can only jack out")
    # A parked IC strike resolves before the decker can leave -- you cannot dodge a landed hit's
    # permanent consequences (MPCP burn / physical / dump shock) by logging off. If it ends the
    # run, the logoff is moot.
    if _force_resolve_pending_defense(state, decker, run):
        run.status = state.get("end_reason", "crashed")
        if state.get("active_download"):
            _corrupt_active_download(state)
        run.state_json = state
        await db.commit()
        await db.refresh(run)
        return _serialize_run(run, auth)
    _spend_pass_action(state, "graceful_logoff")   # vr2: Graceful Logoff is a Complex Action
    success = _apply_graceful_logoff(
        state, decker,
        hacking_pool_dice=body.hacking_pool_dice,
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

    _run_reactive_activation_sensor_checks(state, decker)
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
    fresh["hog_infections"] = copy.deepcopy([
        infection for infection in (state.get("hog_infections") or [])
        if infection.get("target_id", "pc") == "pc"
    ])
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
    parent_host_infections = [
        infection for infection in (parent.get("hog_infections") or [])
        if infection.get("target_id", "pc") != "pc"
    ]
    current_pc_infections = [
        infection for infection in (state.get("hog_infections") or [])
        if infection.get("target_id", "pc") == "pc"
    ]
    parent["hog_infections"] = copy.deepcopy(parent_host_infections + current_pc_infections)
    parent["host_stack"] = stack
    parent["run_ended"] = False
    parent["end_reason"] = None
    child_name = state.get("_stack_current_host_name", "the deeper host")
    _append_event(parent, {
        "type": "trap_door_return",
        "description": f"Logged off \"{child_name}\", returned to \"{parent_name}\".",
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
    """Enter a DISCOVERED trap door (vr2). The action resolves a Graceful Logoff through the
    concealing subsystem, then -- on success -- the current host is SUSPENDED onto the run's
    trap-door stack
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
    _assert_logged_on(state)
    door = next((d for d in (state.get("trap_doors") or []) if str(d.get("id")) == str(td_id)), None)
    if door is None:
        raise HTTPException(404, "Trap door not found")
    if not door.get("discovered"):
        raise HTTPException(400, "Trap door has not been discovered yet (Analyze Subsystem first)")

    # ENTER: graceful logoff through the concealing subsystem, then arrive on the destination.
    dest_id = door.get("destination_host_id")
    if not dest_id:
        raise HTTPException(400, "This trap door has no linked destination host.")
    if len(state.get("host_stack") or []) >= HOST_STACK_CAP:
        raise HTTPException(
            400,
            f"Trap-door stack is at its practical depth limit ({HOST_STACK_CAP}). "
            "Log off a host before diving deeper.",
        )
    dest_host = await _get_host_or_404(db, dest_id)
    src_host = await _get_host_or_404(db, run.host_id) if run.host_id else None

    if _force_resolve_pending_defense(state, run.decker_json, run):
        run.status = state.get("end_reason", "crashed")
        run.state_json = state
        await db.commit()
        await db.refresh(run)
        return _serialize_run(run, auth)
    _spend_pass_action(state, "trap_door_enter")

    success = _apply_graceful_logoff(
        state, run.decker_json,
        hacking_pool_dice=body.hacking_pool_dice,
        finalize_run=False,
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


def _complete_host_crash(state: dict, decker: dict) -> None:
    """Resolve a completed Crash Host: the host goes down and dumps every online decker.
    RAW applies Dump Shock because this is a forced disconnect, not a Graceful Logoff."""
    sec_code = state.get("host_security_code", "Green")
    sec_value = int(state.get("host_security_value", 6) or 6)
    dump_shock = _apply_dump_shock(state, decker, sec_code, sec_value)
    state.pop("crash_host_countdown", None)
    state["run_ended"] = True
    state["end_reason"] = "host_crashed"
    # A forced dump terminates every suspended trap-door session. The current frame already
    # carries the cumulative persona and download ledgers, so discard only the host snapshots
    # before finalizing the surviving haul.
    state.pop("host_stack", None)
    _finalize_run_end(state)
    state.pop("has_legitimate_status", None)   # host is gone -- any passcode goes with it
    state["decoy_successes"] = 0
    state["decoy_hp"] = 0
    _append_event(state, {
        "type": "crash_host_complete",
        "dump_shock": dump_shock,
        "description": (
            "Host crashed, dumped -- System Offline. Dump Shock: "
            f"{dump_shock['final_level']} ({dump_shock['boxes']} boxes). Run complete."
        ),
    })


def _process_crash_countdown(state: dict, decker: dict) -> None:
    """End-of-turn Crash Host processing: re-assert the IC penalty on any newly active IC, roll
    the host's abort test (Security Value vs decker MPCP -- any success aborts), then decrement or
    resolve the countdown. On completion the host crashes and dumps the decker with Dump Shock
    (see _complete_host_crash)."""
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
                f"Host aborted the crash (Security Value {sec_value} vs MPCP {mpcp}: "
                f"{_successes(abort_roll['successes'])}). IC ratings restored; countdown cancelled."
            ),
        })
        return
    cd["turns_remaining"] = int(cd.get("turns_remaining", 1)) - 1
    if cd["turns_remaining"] <= 0:
        _complete_host_crash(state, decker)
    else:
        _append_event(state, {
            "type": "crash_host_tick",
            "turns_remaining": cd["turns_remaining"],
            "description": (
                f"Host crash countdown: {cd['turns_remaining']} round"
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
                "Host shutdown, dumped -- System Offline. Dump Shock: "
                f"{ds['final_level']} ({ds['boxes']} boxes). Run complete."
            ),
        })
        return

    if not cd.get("known"):
        if cd["elapsed"] >= int(cd.get("final_warning_turn", 1) or 1):
            cd["known"] = True
            _append_event(state, {
                "type": "shutdown_warning", "turns_remaining": remaining,
                "description": (
                    f"FINAL WARNING -- the host announces it is shutting down. {remaining} "
                    f"round{'s' if remaining != 1 else ''} until every decker is dumped. "
                    "Grab paydata and get out."
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
                    f"Your Sensors catch it: the host is shutting down -- roughly {remaining} "
                    f"round{'s' if remaining != 1 else ''} until you are dumped. Get out."
                ),
            })
        else:
            _append_event(state, {
                "type": "shutdown_tick", "gm_only": True, "turns_remaining": remaining,
                "description": (
                    f"(GM) Host shutdown in progress: {remaining} round"
                    f"{'s' if remaining != 1 else ''} left; the decker's "
                    f"secret Sensor Test (TN {max(2, remaining)}) failed -- still unaware."
                ),
            })
        return

    _append_event(state, {
        "type": "shutdown_tick", "turns_remaining": remaining,
        "description": (
            f"Host shutdown: {remaining} round{'s' if remaining != 1 else ''} "
            "until you are dumped."
        ),
    })


def _open_next_decker_pass(state: dict, current_pass: int, total_passes: int) -> None:
    """Open the player's next initiative count after every intervening hostile count resolves."""
    state["current_pass"] = current_pass + 1
    _reset_pass_budget(state)
    _append_event(state, {
        "type": "new_pass",
        "description": (
            f"Turn {current_pass + 1}/{total_passes} begins -- Hacking Pool restored."
        ),
    })


def _announce_new_combat_round(state: dict, old_hp: int) -> None:
    """Announce the player's first count after all faster round-opening actors have acted."""
    hacking_pool_total = state.get("hackingPool_total", 0)
    _append_event(state, {
        "type": "new_turn",
        "description": (
            f"Round {state['current_turn']} begins. "
            f"Hacking Pool ({old_hp} -> {hacking_pool_total})."
        ),
    })


def _apply_round_end_status(state: dict, run: MatrixRun) -> dict:
    """Apply host-crash/shutdown status after round-boundary processing."""
    if state.get("run_ended"):
        end_reason = state.get("end_reason")
        if end_reason in ("host_crashed", "host_shutdown"):
            run.status = "dumped"
        else:
            run.status = end_reason or "crashed"
    if state.get("run_ended") and state.get("active_download"):
        _corrupt_active_download(state)
    return state


def _begin_next_combat_round(
    state: dict,
    decker: dict,
    run: MatrixRun,
    security_code: str | None,
) -> dict:
    """Run round-boundary effects, then advance faster hostiles to the player's first count."""
    hacking_pool_total = state.get("hackingPool_total", 0)
    old_hp = state.get("hackingPool_remaining", hacking_pool_total)
    state["hackingPool_remaining"] = hacking_pool_total
    state["current_turn"] = state.get("current_turn", 1) + 1
    _complete_pending_bouncer(state)
    state["initiative_passes"] = _init_passes(_decker_effective_initiative(state))
    state["current_pass"] = 1
    state["actions_this_turn"] = 0
    _reset_pass_budget(state)
    for ic in state.get("active_ic", []):
        ic.pop("acted_pass", None)
        ic.pop("actions_taken_turn", None)
        if not ic.get("suppressed"):
            ic.pop("actions_lost", None)
            ic.pop("slow_turn", None)
            ic.pop("hung_turn", None)
    for enemy in state.get("enemy_deckers", []):
        enemy.pop("acted_pass", None)
        enemy.pop("actions_taken_turn", None)

    _sweep_evade_expiry(state)
    _drain_all_hog_infections(state, decker)
    active_download = state.get("active_download")
    if active_download and not state.get("run_ended"):
        _tick_active_download(state, decker, active_download)
    _process_crash_countdown(state, decker)
    _process_host_shutdown_countdown(state, decker)

    if not state.get("run_ended") and security_code is not None:
        _check_and_activate_sheaf(state, security_code)
        _run_reactive_activation_sensor_checks(state, decker)
        _advance_npc_count_window(
            state, decker, run,
            eff=_get_decker_effective(decker, state),
            sec_code=security_code, sec_value=state["host_security_value"],
            det_factor=_effective_detection_factor(state, decker),
            upper_count=None, lower_count=_decker_action_count(state),
            allow_defense_pause=True,
        )
    if state.get("pending_defense"):
        state["pending_defense"]["resume_phase_transition"] = {
            "kind": "announce_round", "old_hp": old_hp,
        }
    elif not state.get("run_ended"):
        _announce_new_combat_round(state, old_hp)
    return _apply_round_end_status(state, run)


@router.post("/{run_id}/new-turn", response_model=MatrixRunRead, dependencies=[Depends(trace_action)])
async def new_turn(
    run_id: int,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """End the decker's current initiative pass ("End Turn" / "End Pass" in the UI).

    If the decker still has initiative counts left this Combat Turn, this closes its current phase:
    the shared clock descends through every intervening hostile count, then the decker's action
    budget and Hacking Pool refresh at its next count. Initiative is rolled once per encounter.

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
    state["_acting_init"] = _decker_effective_initiative(state)

    npc_decker = copy.deepcopy(run.decker_json)
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
        _release_spawned_hostiles_for_pass(state, cur_pass)
        _check_and_activate_sheaf(state, npc_sec_code)
        _run_reactive_activation_sensor_checks(state, npc_decker)
        current_count = _decker_action_count(state)
        next_count = max(0, current_count - 10)
        _advance_npc_count_window(
            state, npc_decker, run,
            eff=_get_decker_effective(npc_decker, state),
            sec_code=npc_sec_code, sec_value=npc_sec_value,
            det_factor=_effective_detection_factor(state, npc_decker),
            upper_count=current_count, lower_count=next_count,
            allow_defense_pause=True,
        )
        if state.get("pending_defense"):
            state["pending_defense"]["resume_phase_transition"] = {
                "kind": "next_pass",
                "current_pass": cur_pass,
                "total_passes": total_passes,
            }
            run.decker_json = copy.deepcopy(npc_decker)
            run.state_json = state
            await db.commit()
            await db.refresh(run)
            return _serialize_run(run, auth)
        if state.get("run_ended"):
            # A hostile on the pass being left killed the decker -- end the run here.
            run.status = state.get("end_reason", "crashed")
            if state.get("active_download"):
                _corrupt_active_download(state)
            run.decker_json = copy.deepcopy(npc_decker)
            run.state_json = state
            await db.commit()
            await db.refresh(run)
            return _serialize_run(run, auth)
        _open_next_decker_pass(state, cur_pass, total_passes)
        run.decker_json = copy.deepcopy(npc_decker)
        run.state_json = state
        await db.commit()
        await db.refresh(run)
        return _serialize_run(run, auth)

    # -- END TURN: the decker is on its last pass -> finish hostile passes, then next Combat Turn -
    # -- End-of-turn NPC pass flush (app-as-GM) --------------------------------------------------
    # On the player's final count, descend the shared clock to zero before the round resets. This
    # gives faster hostiles any extra lower counts and still acts when the player ends without
    # spending an action. Per-hostile action indexes make the flush idempotent.
    if npc_sec_code is not None:
        npc_sec_value = state["host_security_value"]
        _release_spawned_hostiles_for_pass(state, state.get("current_pass", 1))
        _check_and_activate_sheaf(state, npc_sec_code)
        _run_reactive_activation_sensor_checks(state, npc_decker)
        _advance_npc_count_window(
            state, npc_decker, run,
            eff=_get_decker_effective(npc_decker, state),
            sec_code=npc_sec_code, sec_value=npc_sec_value,
            det_factor=_effective_detection_factor(state, npc_decker),
            upper_count=None, lower_count=0,
            allow_defense_pause=True,
        )
        if state.get("pending_defense"):
            state["pending_defense"]["resume_phase_transition"] = {"kind": "next_round"}
            run.decker_json = copy.deepcopy(npc_decker)
            run.state_json = state
            await db.commit()
            await db.refresh(run)
            return _serialize_run(run, auth)
        if state.get("run_ended"):
            # A flushed hostile pass killed the decker -- end the run here; do NOT advance the turn.
            run.status = state.get("end_reason", "crashed")
            if state.get("active_download"):
                _corrupt_active_download(state)
            run.decker_json = copy.deepcopy(npc_decker)
            run.state_json = state
            await db.commit()
            await db.refresh(run)
            return _serialize_run(run, auth)

    state = _begin_next_combat_round(state, npc_decker, run, npc_sec_code)

    run.decker_json = copy.deepcopy(npc_decker)
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
    variant payload take effect (Deathworm cybercombat penalty / Tapeworm paydata erasure). An
    infected worm is recorded in ``state["mpcp_infections"]`` --
    a PERSISTENT deck status that carries across runs until the MPCP chip is replaced -- and removed
    from ``lurking_ic``; a repelled worm stays lurking to try again on the next System Test against
    its subsystem. Mutates ``state``; appends a ``worm_resolved`` event. Called from
    ``_trigger_subsystem_worms`` when the decker makes a System Test against the worm's subsystem.
    """
    hardening = decker.get("hardening", 0)
    variant = _worm_variant(lurking.get("variant"))
    if variant is None:
        return
    _sub_label = (subsystem or lurking.get("subsystem", "") or "").strip()
    _where = f" on the {_sub_label.title()} subsystem" if _sub_label else ""
    wr = eng.worm_attack(
        security_value=state.get("host_security_value", 1),
        mpcp_rating=decker.get("mpcp", 1),
        hardening=hardening,
    )
    raw_successes = int(wr["roll"].get("successes", 0) or 0)
    net_successes = int(wr.get("net_successes", raw_successes - hardening) or 0)
    # An infection attempt identifies the threat as Worm IC, but its rating and variant still
    # require Analyze IC. A repelled Worm remains visible while it continues lurking.
    lurking["detection_level"] = max(2, _ic_detection_level(lurking))
    if wr["mpcp_infected"]:
        state["mpcp_infected"] = True
        state["chip_replacement_required"] = True
        # Record the infection as a persistent deck status keyed by variant (carried across runs
        # via the decker payload until the chip is replaced). Deathworm -> ongoing cybercombat
        # penalty; Tapeworm -> paydata erasure at every run end.
        state.setdefault("mpcp_infections", []).append({
            "variant": variant, "rating": lurking.get("rating", 6), "ic_id": lurking["id"],
        })
        state["lurking_ic"] = [
            ic for ic in state.get("lurking_ic", []) if ic["id"] != lurking["id"]]
        resolved_worm = dict(lurking)
        resolved_worm["status"] = "resolved"
        resolved_worm["suppression_released"] = True
        state.setdefault("active_ic", []).append(resolved_worm)
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
                f"{wr['tn']} scored {_successes(raw_successes)}; Hardening-{hardening} reduced "
                f"that to {net_successes} net success{'es' if net_successes != 1 else ''}."
            ),
        })
    else:
        _rlabel = {"deathworm": "Deathworm", "tapeworm": "Tapeworm"}.get(variant, "Worm")
        _append_event(state, {
            "type": "worm_resolved", "ic_id": lurking["id"], "ic_type": "Worm",
            "outcome": "repelled", "roll": wr["roll"], "subsystem": _sub_label,
            "description": (
                f"A {_rlabel}-{lurking['rating']}{_where} tried to infect your MPCP but was "
                f"repelled. Infection Test scored {_successes(raw_successes)}; Hardening-"
                f"{hardening} reduced that to {net_successes} net "
                f"success{'es' if net_successes != 1 else ''}. Worm still lurking."
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
                "delete_roll": n_delete,
                "description": "The Tapeworm was unable to delete any data.",
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
                f"Tapeworm-{_wm.get('rating')} corrupts your haul on jack-out: "
                f"{len(destroyed)} file(s) erased ({', '.join(destroyed)})"
                + (" -- key data lost." if key_erased else ".")
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
        paydata = _paydata_for_target(state, f.get("id") or f.get("name", ""))
        if paydata is not None:
            paydata["compressed"] = False
        total_mp += full
        secured.append({
            "id": f.get("id"), "name": f.get("name"), "size_mp": full,
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


def _finalize_enemy_decker_aar(state: dict) -> None:
    """GM run-AAR line for every security decker dispatched this run: its handle and final
    disposition (killed / knocked out / crashed / fled / evaded / still active). GM-only, so a
    player never learns a decker was dispatched. Idempotent (``enemy_aar_finalized``); skipped while
    a trap-door host stack is still suspended, so it fires only at the true run end."""
    if state.get("enemy_aar_finalized") or state.get("host_stack"):
        return
    enemies = state.get("enemy_deckers") or []
    if not enemies:
        return
    state["enemy_aar_finalized"] = True

    def _disposition(e: dict) -> str:
        outcome = e.get("outcome")
        if outcome == "killed":
            return "killed (physical biofeedback)"
        if outcome == "knocked_out":
            return "knocked out (stun biofeedback)"
        if outcome == "dumped" or e.get("status") == "crashed":
            return "crashed (icon dumped)"
        if e.get("status") == "fled":
            return "fled (jacked out)"
        if e.get("evaded"):
            return "evaded (hidden at run end)"
        return "still active at run end"

    dispositions = [
        {"enemy_id": e.get("id"), "handle": e.get("handle"), "disposition": _disposition(e)}
        for e in enemies
    ]
    lines = "; ".join(f"{_enemy_gm_name(e)} -- {_disposition(e)}" for e in enemies)
    _append_event(state, {
        "type": "enemy_decker_aar", "gm_only": True, "count": len(enemies),
        "dispositions": dispositions,
        "description": (
            f"GM AAR -- {len(enemies)} security decker(s) dispatched this run: {lines}."
        ),
    })


def _finalize_run_end(state: dict) -> None:
    """Single run-end hook: resolve Tapeworm payload loss, secure the surviving paydata haul
    (directive #6), then log the GM enemy-decker AAR. All steps are idempotent, so calling this on
    any run-end path is safe."""
    _apply_tapeworm_run_end(state)
    _finalize_paydata_haul(state)
    _finalize_enemy_decker_aar(state)


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
                         else f"All active copies of {utility_name} wiped.")
            ),
        })
        if is_tar_pit and result.get("all_copies_corrupted"):
            _append_event(state, {
                "type": "tar_pit_corruption",
                "utility": _normalize_util_name(utility_name),
                "description": f"All copies of {utility_name} lost.",
                "tar_pit_roll": result.get("tar_pit_roll"),
            })
            # Viral corruption of every copy (active + storage): the program is gone for the run.
            _wipe_all_copies(state, decker, utility_name)
        else:
            # Tar Baby targets active memory: every active copy of the named utility is wiped,
            # including duplicate One-Shots, while storage copies remain untouched.
            _wipe_active_copies(state, decker, utility_name)
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
    return f"{_action_label(name)} -{applied}{' (CRASHED)' if crashed else ''}"


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

    def current_rating(self, name: str) -> int:
        """Current effective (running) rating of a named program after any drain, floored at 0."""
        for k, eff in self._running_pairs():
            if k == name:
                return max(0, eff)
        return 0


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
            label = _action_label(name)
            frag = f"{label} -{applied} (crashed)" if crashed else f"{label} -{applied} (now {target.current_rating(name)})"
            if target.id == "pc":
                _append_event(state, {
                    "type": "enemy_decker", "outcome": "hog",
                    "description": f"Hog-{inf.get('rating')} virus drains your deck: {frag}.",
                })
            else:
                _append_event(state, {
                    "type": "enemy_decker", "outcome": "hog", "enemy_id": target.id,
                    "gm_only": True,
                    "description": f"Your Hog virus drains {target.name}'s program: {frag}.",
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
            "description": f"{_enemy_display_name(enemy)} purges your Hog program from their deck.",
        })
    else:
        _append_event(state, {
            "type": "enemy_decker", "outcome": "purge_hog", "enemy_id": enemy.get("id"),
            "description": (
                f"{_enemy_display_name(enemy)} unsuccessfully attempts to purge your "
                "Hog program from their deck."
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
        pretty = ", ".join(_action_label(n) for n in restored)
        _append_event(state, {
            "type": "enemy_decker", "outcome": "swap_memory", "enemy_id": enemy.get("id"),
            "description": f"{_enemy_display_name(enemy)} reloads {pretty}.",
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
        "description": f"{_enemy_display_name(enemy)} analyzes your icon and learns your weaknesses.",
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
                    "description": (
                        f"{_enemy_display_name(enemy)} re-emerges from hiding to resume the hunt."
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
                "description": "A hostile decker is hunting your icon.",
            })
        if loc["located"]:
            enemy["located"] = True
            _append_event(state, {
                "type": "enemy_decker", "outcome": "located", "enemy_id": enemy["id"],
                "description": f"{_enemy_display_name(enemy)} has located your position.",
            })
        else:
            _append_event(state, {
                "type": "enemy_decker", "outcome": "probing", "enemy_id": enemy["id"],
                "gm_only": True,
                "description": (
                    f"{_enemy_display_name(enemy)} has failed to locate you this turn."
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
            frag = (f"{_action_label(res['drained'])} -{res['applied']}"
                    f"{' (crashed)' if res['crashed'] else ''}") if res["drained"] else "no running program left"
            desc = (f"Hog -- {_enemy_display_name(enemy)}'s virus takes hold (drains {res['reduction']}/turn): "
                    f"{frag}. Purge it or reload via Swap Memory.")
        else:
            desc = f"Hog -- {_enemy_display_name(enemy)}'s virus fails to take hold this turn."
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
            target_decker=decker,
            causing_rating=attack_rating,
            shield_parry=lambda: _shield_parry(state, decker, attacker_skill=enemy["computer_skill"], context=program),
            tn_modifier=atk_tn_delta + _enemy_wound_mod(enemy))
        if cr["reduction"] > 0:
            now = max(1, decker.get(attr, 4) - cm["persona_damage"][attr])
            desc = (f"{program} -- {_enemy_display_name(enemy)} cripples your {attr.title()} by "
                    f"{cr['reduction']} (now {now}, until logoff).")
        else:
            desc = f"{program} -- {_enemy_display_name(enemy)}'s crippler attack is resisted."
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
            "description": f"Persona Crashed by {_enemy_display_name(enemy)} -- dumped (dump shock: {shock}).{mpcp_note}",
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
    _assert_logged_on(state)
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
    util = decker.get("utilities") or {}
    program_rating = _effective_program_rating(decker, state, body.program)
    if program_rating <= 0:
        raise HTTPException(400, f"No usable {_action_label(body.program)} program is loaded")
    pool = program_rating + body.hacking_pool_dice
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
        hog_rating = program_rating
        res = _resolve_hog(
            state, _hog_target_for_enemy(state, enemy), attacker_id="pc",
            attacker_pool=pool, hog_rating=hog_rating, sec_code=sec_code,
            target_status=_combat_target_status(enemy), tn_modifier=tgt_tn_delta + _decker_wound_mod(state))
        if res["infected"]:
            desc = (f"Hog -- your virus takes hold on {_enemy_display_name(enemy)}: it will drain "
                    f"{res['reduction']} off its highest running program each Combat Turn "
                    f"until it purges or crashes.")
        else:
            desc = f"Hog -- your virus fails to take hold on {_enemy_display_name(enemy)} this turn."
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
        carried = program_rating
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
                fate = (f"{label} crashes {_enemy_display_name(enemy)}'s icon -- the hostile decker is dumped and "
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
    _assert_logged_on(state)
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
    _assert_logged_on(state)
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
                 if isinstance(ic, dict) and ic.get("status") == "active"
                 and not (_ic_is_trace(ic) and not _trace_is_targetable(ic))}
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
    attack_util_rating = _effective_program_rating(decker, state, "attack")
    if attack_util_rating <= 0:
        raise HTTPException(400, "No usable Attack program is loaded")
    attack_pool = attack_util_rating + body.hacking_pool_dice
    # vr2 L2028: hit the TARGET's status column. Area targets are IC and/or enemy deckers -- all
    # Legitimate host residents -- so the burst uses the Legitimate column for every target.
    base_tn = rules.COMBAT_TN[sec_code][_combat_target_status()]
    wound_mod = _decker_wound_mod(state)
    # The Attack utility carries its OWN base Damage Level (Attack-6L/-6M/-6S/-6D), not the host
    # IC Damage Table; every target in the burst resists against that single program severity.
    base_dmg = _attack_damage_level(decker, sec_code)
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
            ic_resist_pool = _ic_test_pool(obj, sec_value, defense=True)
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
        head = (f"Area strike ({attack_roll['successes']} successes) hits {n_targets} icons "
                f"[+{area_penalty} to-hit]")
    else:
        head = f"Attack ({attack_roll['successes']} successes)"
    parts = [f"{r['label']} {r['final']} ({r['boxes']}b{'; crashed' if r['crashed'] else ''})"
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
    _run_reactive_activation_sensor_checks(state, run.decker_json)

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
    _assert_logged_on(state)
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
        shield_parry=lambda: _shield_parry(
            state, decker, attacker_skill=sec_value, context="Black IC", source_ic=ic),
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
            f"Black IC-{ic['rating']} lands one final attack as you jack out: "
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

    # Resolve any parked IC strike first (Bod-only, no Hacking Pool) -- you cannot jack out to
    # dodge a landed hit's permanent consequences. If it ends the run, that IS the outcome.
    if _force_resolve_pending_defense(state, decker, run):
        run.status = state.get("end_reason", "crashed")
        if state.get("active_download"):
            _corrupt_active_download(state)
        run.state_json = state
        await db.commit()
        await db.refresh(run)
        return _serialize_run(run, auth)

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
                "description": "You are unable to sever your connection to the host as the Black IC grabs your icon and holds fast.",
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
                f"Willpower Test (TN {tn}) succeeds ({wp_roll['successes']} success"
                f"{'es' if wp_roll['successes'] != 1 else ''}) -- you tear free, but Black IC-"
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
