from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.dependencies import get_db
from app.models.adventure_log import AdventureLog
from app.models.character import Character
from app.models.location import Location
from app.models.organization import Organization
from app.models.reputation import Reputation, OrgStanding
from app.schemas.adventure_log import (
    AdventureLogCreate, AdventureLogUpdate, AdventureLogRead, AdventureLogSummary,
)
from app.services.campaign import current_tick
from app.services.consequence_engine import suggest
from app.services.heat_calculator import (
    compute_ripple, heat_label, standing_label,
    decay_pa, decay_standing, decay_heat, pc_rep_label, team_rep_label, pa_label,
    LYING_LOW_DECAY_ACCEL,
)
from app.auth.dependencies import get_admin_token


# -- Narrative parsing schemas ---------------------------------
class NarrativeParseRequest(BaseModel):
    narrative: str


class ChangeItem(BaseModel):
    type: str
    character_id: int
    character_name: Optional[str] = None
    delta: int
    org_id: Optional[int] = None
    org_name: Optional[str] = None
    reason: Optional[str] = None


class ApplyChangesRequest(BaseModel):
    changes: list[ChangeItem]
    tick_count: int = 0


router = APIRouter()

_LOAD_OPTS = [
    selectinload(AdventureLog.participants),
    selectinload(AdventureLog.locations_involved),
    selectinload(AdventureLog.orgs_involved),
]


async def _get_or_404(db: AsyncSession, log_id: int) -> AdventureLog:
    result = await db.execute(
        select(AdventureLog).options(*_LOAD_OPTS).where(AdventureLog.id == log_id)
    )
    log = result.scalars().first()
    if not log:
        raise HTTPException(status_code=404, detail="Adventure log not found")
    return log


async def _resolve_relations(
    db: AsyncSession, log: AdventureLog,
    participant_ids: list[int] | None,
    location_ids: list[int] | None,
    org_ids: list[int] | None,
):
    """Resolve M2M relation IDs to ORM objects, raising 422 for any missing IDs."""
    if participant_ids is not None:
        result = await db.execute(select(Character).where(Character.id.in_(participant_ids)))
        found = result.scalars().all()
        if len(found) != len(participant_ids):
            found_ids = {c.id for c in found}
            missing = sorted(set(participant_ids) - found_ids)
            raise HTTPException(status_code=422, detail=f"Unknown character IDs: {missing}")
        log.participants = found

    if location_ids is not None:
        result = await db.execute(select(Location).where(Location.id.in_(location_ids)))
        found = result.scalars().all()
        if len(found) != len(location_ids):
            found_ids = {loc.id for loc in found}
            missing = sorted(set(location_ids) - found_ids)
            raise HTTPException(status_code=422, detail=f"Unknown location IDs: {missing}")
        log.locations_involved = found

    if org_ids is not None:
        result = await db.execute(select(Organization).where(Organization.id.in_(org_ids)))
        found = result.scalars().all()
        if len(found) != len(org_ids):
            found_ids = {o.id for o in found}
            missing = sorted(set(org_ids) - found_ids)
            raise HTTPException(status_code=422, detail=f"Unknown organization IDs: {missing}")
        log.orgs_involved = found


@router.get("/party-stats")
async def party_stats(db: AsyncSession = Depends(get_db)):
    """Return party-wide heat and team reputation (active PCs only)."""
    tick = await current_tick(db)

    all_pcs_result = await db.execute(
        select(Character).where(Character.is_pc == True)  # noqa: E712
    )
    all_pcs = all_pcs_result.scalars().all()
    pc_ids = [c.id for c in all_pcs]

    rep_scores = []
    pa_scores = []
    heat_values = []
    char_rep_map: dict[int, dict] = {}

    if pc_ids:
        reps_result = await db.execute(
            select(Reputation).where(Reputation.character_id.in_(pc_ids))
        )
        rep_by_char = {r.character_id: r for r in reps_result.scalars().all()}

        for pc in all_pcs:
            accel = LYING_LOW_DECAY_ACCEL if not pc.is_active else 1.0
            r = rep_by_char.get(pc.id)
            sc = (r.street_cred if r else 0) or 0
            not_ = (r.notoriety if r else 0) or 0
            pa_raw = (r.public_awareness if r else 0) or 0
            heat_raw = (r.heat or 0) if r else 0

            pa_elapsed = tick - ((r.pa_stamped_tick or 0) if r else 0)
            heat_elapsed = tick - ((r.heat_stamped_tick or 0) if r else 0)
            pa_eff = max(0, round(decay_pa(pa_raw, pa_elapsed, accel)))
            heat_eff = max(0, round(decay_heat(heat_raw, heat_elapsed, accel)))
            net_rep = max(0, min(40, 20 + sc - not_))

            if pc.is_active:
                rep_scores.append(net_rep)
                pa_scores.append(pa_eff)
                heat_values.append(heat_eff)

            char_rep_map[pc.id] = {
                "net_rep": net_rep,
                "net_rep_tier": pc_rep_label(net_rep),
                "pa": pa_eff,
                "pa_tier": pa_label(pa_eff),
                "heat": heat_eff,
                "heat_label": heat_label(heat_eff),
                "is_active": pc.is_active,
            }

    # Org standings for all PCs
    pc_active_map = {c.id: c.is_active for c in all_pcs}
    standings_result = await db.execute(
        select(OrgStanding).where(OrgStanding.character_id.in_(pc_ids))
    ) if pc_ids else None
    all_standings = standings_result.scalars().all() if standings_result else []

    org_ids_needed = {s.organization_id for s in all_standings}
    org_name_map: dict[int, str] = {}
    if org_ids_needed:
        orgs_result = await db.execute(
            select(Organization).where(Organization.id.in_(org_ids_needed))
        )
        org_name_map = {o.id: o.name for o in orgs_result.scalars().all()}

    standings_by_char: dict[int, list] = {}
    for s in all_standings:
        raw = s.standing or 0
        s_accel = 1.0 if pc_active_map.get(s.character_id, True) else LYING_LOW_DECAY_ACCEL
        s_elapsed = tick - (s.standings_stamped_tick or 0)
        eff = round(decay_standing(raw, s_elapsed, s_accel))
        standings_by_char.setdefault(s.character_id, []).append({
            "id": s.id,
            "org_id": s.organization_id,
            "org_name": org_name_map.get(s.organization_id, f"Org #{s.organization_id}"),
            "standing": eff,
            "label": standing_label(eff),
        })

    for pc_id in char_rep_map:
        char_rep_map[pc_id]["standings"] = sorted(
            standings_by_char.get(pc_id, []),
            key=lambda x: x["org_name"].lower(),
        )

    party_heat = max(heat_values) if heat_values else 0
    team_score = round(sum(rep_scores) / len(rep_scores)) if rep_scores else 20
    avg_pa = round(sum(pa_scores) / len(pa_scores)) if pa_scores else 0

    return {
        "heat": party_heat,
        "heat_label": heat_label(party_heat),
        "team_rep_score": team_score,
        "team_rep_tier": team_rep_label(team_score),
        "avg_pa": avg_pa,
        "pa_tier": pa_label(avg_pa),
        "char_rep": char_rep_map,
    }


@router.get("/", response_model=list[AdventureLogSummary])
async def list_logs(
    outcome: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    q = select(AdventureLog)
    if outcome:
        q = q.where(AdventureLog.outcome == outcome)
    result = await db.execute(
        q.order_by(AdventureLog.session_date.desc(), AdventureLog.run_number.desc())
    )
    return result.scalars().all()


@router.post("/", response_model=AdventureLogRead, status_code=201)
async def create_log(
    body: AdventureLogCreate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    data = body.model_dump(exclude={"participant_ids", "location_ids", "org_ids"})

    max_run_result = await db.execute(select(func.max(AdventureLog.run_number)))
    max_run = max_run_result.scalar() or 0
    data["run_number"] = max_run + 1

    if data.get("outcome_tags"):
        data["consequences_suggested"] = suggest(data["outcome_tags"])

    participant_count = len(body.participant_ids)
    heat_deltas = [
        ch["delta"] for ch in (data.get("changes_applied") or [])
        if ch.get("type") == "heat" and isinstance(ch.get("delta"), (int, float))
    ]
    data["heat"] = round(sum(heat_deltas) / participant_count) if participant_count and heat_deltas else 0

    log = AdventureLog(**data)

    # Resolve M2M relations on the transient object BEFORE db.add().
    # Setting relationship attributes on a post-flush persistent object triggers
    # a sync lazy load, which is illegal in async SQLAlchemy (MissingGreenlet).
    await _resolve_relations(db, log, body.participant_ids, body.location_ids, body.org_ids)

    db.add(log)
    await db.commit()
    return await _get_or_404(db, log.id)


@router.post("/parse-narrative")
async def parse_run_narrative(
    body: NarrativeParseRequest,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    """Use Claude to parse a GM narrative into structured run data + proposed world changes."""
    from app.services.secrets import get_api_key
    if not get_api_key():
        raise HTTPException(status_code=503, detail="Anthropic API key is not configured")

    from app.services.narrative_parser import parse_narrative

    chars_result = await db.execute(
        select(Character).where(Character.is_active == True)  # noqa: E712
    )
    orgs_result = await db.execute(
        select(Organization).where(Organization.is_active == True)  # noqa: E712
    )
    reps_result = await db.execute(select(Reputation))
    standings_result = await db.execute(select(OrgStanding))

    chars = chars_result.scalars().all()
    orgs = orgs_result.scalars().all()
    reps = reps_result.scalars().all()
    standings = standings_result.scalars().all()

    world_context = {
        "characters": [{"id": c.id, "name": c.name, "is_pc": c.is_pc} for c in chars],
        "organizations": [{"id": o.id, "name": o.name, "org_type": o.org_type} for o in orgs],
        "reputation": [{"character_id": r.character_id, "street_cred": r.street_cred,
                         "notoriety": r.notoriety, "public_awareness": r.public_awareness} for r in reps],
        "standings": [{"character_id": s.character_id, "org_id": s.organization_id,
                        "standing": s.standing} for s in standings],
    }

    try:
        result = await parse_narrative(body.narrative, world_context)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Narrative parsing failed: {e}")

    # Faction ripple
    org_map = {
        o.id: {"name": o.name, "ally_ids": o.ally_ids or [], "enemy_ids": o.enemy_ids or []}
        for o in orgs
    }
    ripple_index: dict[tuple, dict] = {}
    for ch in result.get("proposed_changes", []):
        if ch.get("type") == "org_standing" and ch.get("org_id") and ch.get("delta"):
            for rpl in compute_ripple(ch["org_id"], ch["delta"], org_map):
                rpl["character_id"] = ch["character_id"]
                rpl["character_name"] = ch.get("character_name")
                key = (rpl["character_id"], rpl["org_id"])
                if key not in ripple_index or abs(rpl["delta"]) > abs(ripple_index[key]["delta"]):
                    ripple_index[key] = rpl
    result["proposed_changes"] = result.get("proposed_changes", []) + list(ripple_index.values())

    return result


@router.post("/apply-changes")
async def apply_world_changes(
    body: ApplyChangesRequest,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    """Apply a reviewed set of world-state changes (reputation, org standings)."""
    applied = []
    errors = []
    # Stamp decay at the current campaign clock; logging a run no longer advances
    # time -- only the Downtime control moves the clock.
    tick = await current_tick(db)

    for ch in body.changes:
        try:
            if ch.type in ("street_cred", "notoriety", "public_awareness"):
                result = await db.execute(
                    select(Reputation).where(Reputation.character_id == ch.character_id)
                )
                rep = result.scalars().first()
                if not rep:
                    errors.append(f"No reputation record for character {ch.character_id}")
                    continue
                old = getattr(rep, ch.type, 0) or 0
                setattr(rep, ch.type, max(0, old + ch.delta))
                if ch.type == "public_awareness":
                    rep.pa_updated_at = date.today()
                    rep.pa_stamped_tick = tick
                applied.append({"desc": f"{ch.character_name or ch.character_id}: {ch.type} {ch.delta:+}", "reason": ch.reason})

            elif ch.type == "heat":
                result = await db.execute(
                    select(Reputation).where(Reputation.character_id == ch.character_id)
                )
                rep = result.scalars().first()
                if not rep:
                    errors.append(f"No reputation record for character {ch.character_id}")
                    continue
                rep.heat = min(10, max(0, (rep.heat or 0) + ch.delta))
                rep.heat_updated_at = date.today()
                rep.heat_stamped_tick = tick
                applied.append({"desc": f"{ch.character_name or ch.character_id}: heat {ch.delta:+} -> {rep.heat}", "reason": ch.reason})

            elif ch.type == "org_standing":
                if not ch.org_id:
                    errors.append("org_id required for org_standing change")
                    continue
                result = await db.execute(
                    select(OrgStanding).where(
                        OrgStanding.character_id == ch.character_id,
                        OrgStanding.organization_id == ch.org_id,
                    )
                )
                standing = result.scalars().first()
                if standing:
                    standing.standing = max(-10, min(10, (standing.standing or 0) + ch.delta))
                else:
                    standing = OrgStanding(
                        character_id=ch.character_id,
                        organization_id=ch.org_id,
                        standing=max(-10, min(10, ch.delta)),
                        notes=ch.reason,
                    )
                    db.add(standing)
                standing.standings_updated_at = date.today()
                standing.standings_stamped_tick = tick
                applied.append({"desc": f"{ch.character_name or ch.character_id} <-> {ch.org_name or ch.org_id}: standing {ch.delta:+}", "reason": ch.reason})

            else:
                errors.append(f"Unknown change type: {ch.type}")
        except Exception as e:
            errors.append(f"Error on {ch.type} for char {ch.character_id}: {e}")

    await db.commit()
    return {"applied": applied, "errors": errors}


@router.get("/{log_id}", response_model=AdventureLogRead)
async def get_log(log_id: int, db: AsyncSession = Depends(get_db)):
    return await _get_or_404(db, log_id)


@router.patch("/{log_id}", response_model=AdventureLogRead)
async def update_log(
    log_id: int,
    body: AdventureLogUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    log = await _get_or_404(db, log_id)
    data = body.model_dump(exclude_unset=True, exclude={"participant_ids", "location_ids", "org_ids"})

    if "outcome_tags" in data:
        data["consequences_suggested"] = suggest(data["outcome_tags"])

    for field, value in data.items():
        if hasattr(log, field):
            setattr(log, field, value)

    await _resolve_relations(
        db, log,
        body.participant_ids if body.participant_ids is not None else None,
        body.location_ids if body.location_ids is not None else None,
        body.org_ids if body.org_ids is not None else None,
    )

    await db.commit()
    return await _get_or_404(db, log.id)


@router.delete("/{log_id}", status_code=204)
async def delete_log(
    log_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    log = await _get_or_404(db, log_id)
    await db.delete(log)
    await db.commit()


@router.post("/{log_id}/refresh-consequences", response_model=AdventureLogRead)
async def refresh_consequences(
    log_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    """Regenerate consequence suggestions for an existing log."""
    log = await _get_or_404(db, log_id)
    log.consequences_suggested = suggest(log.outcome_tags or [])
    await db.commit()
    return await _get_or_404(db, log.id)
