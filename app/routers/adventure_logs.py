import os
from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.orm import Session, selectinload
from app.dependencies import get_db
from app.models.adventure_log import AdventureLog
from app.models.character import Character
from app.models.location import Location
from app.models.organization import Organization
from app.models.reputation import Reputation, OrgStanding
from app.schemas.adventure_log import (
    AdventureLogCreate, AdventureLogUpdate, AdventureLogRead, AdventureLogSummary
)
from app.services.consequence_engine import suggest
from app.services.heat_calculator import (
    compute_heat, compute_ripple, heat_label, standing_label,
    decay_pa, decay_standing, decay_heat, pc_rep_label, team_rep_label, pa_label,
    LYING_LOW_DECAY_ACCEL,
)


# ── Narrative parsing schemas ─────────────────────────────────
class NarrativeParseRequest(BaseModel):
    narrative: str


class ChangeItem(BaseModel):
    type: str                          # street_cred | notoriety | public_awareness | heat | org_standing
    character_id: int
    character_name: Optional[str] = None
    delta: int
    org_id: Optional[int] = None
    org_name: Optional[str] = None
    reason: Optional[str] = None


class ApplyChangesRequest(BaseModel):
    changes: list[ChangeItem]

router = APIRouter()

_LOAD_OPTS = [
    selectinload(AdventureLog.participants),
    selectinload(AdventureLog.locations_involved),
    selectinload(AdventureLog.orgs_involved),
]


def _get_or_404(db: Session, log_id: int) -> AdventureLog:
    log = db.query(AdventureLog).options(*_LOAD_OPTS).filter(AdventureLog.id == log_id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Adventure log not found")
    return log


def _resolve_relations(db: Session, log: AdventureLog, participant_ids, location_ids, org_ids):
    if participant_ids is not None:
        log.participants = db.query(Character).filter(Character.id.in_(participant_ids)).all()
    if location_ids is not None:
        log.locations_involved = db.query(Location).filter(Location.id.in_(location_ids)).all()
    if org_ids is not None:
        log.orgs_involved = db.query(Organization).filter(Organization.id.in_(org_ids)).all()


@router.get("/party-stats")
def party_stats(db: Session = Depends(get_db)):
    """
    Return party-wide heat (decayed, across all PCs) and team reputation
    (average of active PCs only).
    """
    today = date.today()

    # ── All PCs: active ones for party stats, inactive for lying-low decay ──
    all_pcs = db.query(Character).filter(Character.is_pc == True).all()
    active_pcs = [c for c in all_pcs if c.is_active]
    pc_ids = [c.id for c in all_pcs]

    rep_scores = []
    pa_scores  = []
    heat_values = []
    char_rep_map = {}   # char_id -> {net_rep, net_rep_tier, pa, pa_tier}
    if pc_ids:
        reps = db.query(Reputation).filter(Reputation.character_id.in_(pc_ids)).all()
        rep_by_char = {r.character_id: r for r in reps}
        for pc in all_pcs:
            accel = LYING_LOW_DECAY_ACCEL if not pc.is_active else 1.0
            r = rep_by_char.get(pc.id)
            sc   = (r.street_cred       if r else 0) or 0
            not_ = (r.notoriety         if r else 0) or 0
            pa_raw = (r.public_awareness if r else 0) or 0
            heat_raw = (r.heat or 0) if r else 0
            # Decay PA if we have a timestamp for when it was last set
            if r and r.pa_updated_at:
                days_since = (today - r.pa_updated_at).days
                pa_eff = max(0, round(decay_pa(pa_raw, days_since, accel)))
            else:
                pa_eff = pa_raw  # no timestamp → no decay
            # Decay heat — use pa_updated_at as proxy (both updated together)
            if r and r.pa_updated_at:
                days_since = (today - r.pa_updated_at).days
                heat_eff = max(0, round(decay_heat(heat_raw, days_since, accel)))
            else:
                heat_eff = heat_raw
            net_rep = max(0, min(40, 20 + sc - not_))
            # Only active PCs count toward party aggregates
            if pc.is_active:
                rep_scores.append(net_rep)
                pa_scores.append(pa_eff)
                heat_values.append(heat_eff)
            char_rep_map[pc.id] = {
                "net_rep":      net_rep,
                "net_rep_tier": pc_rep_label(net_rep),
                "pa":           pa_eff,
                "pa_tier":      pa_label(pa_eff),
                "heat":         heat_eff,
                "heat_label":   heat_label(heat_eff),
                "is_active":    pc.is_active,
            }

    # ── Fetch org standings for all PCs (active + inactive) ─────────────────────
    # Build a quick is_active lookup for per-PC accel
    pc_active_map = {c.id: c.is_active for c in all_pcs}
    all_standings = db.query(OrgStanding).filter(OrgStanding.character_id.in_(pc_ids)).all() if pc_ids else []
    org_ids_needed = {s.organization_id for s in all_standings}
    org_name_map: dict[int, str] = {}
    if org_ids_needed:
        orgs_q = db.query(Organization).filter(Organization.id.in_(org_ids_needed)).all()
        org_name_map = {o.id: o.name for o in orgs_q}
    standings_by_char: dict[int, list] = {}
    for s in all_standings:
        raw = s.standing or 0
        s_accel = 1.0 if pc_active_map.get(s.character_id, True) else LYING_LOW_DECAY_ACCEL
        if s.standings_updated_at:
            days_since = (today - s.standings_updated_at).days
            eff = round(decay_standing(raw, days_since, s_accel))
        else:
            eff = raw  # no timestamp → no decay
        standings_by_char.setdefault(s.character_id, []).append({
            "id":       s.id,
            "org_id":   s.organization_id,
            "org_name": org_name_map.get(s.organization_id, f"Org #{s.organization_id}"),
            "standing": eff,
            "label":    standing_label(eff),
        })
    for pc_id in char_rep_map:
        char_rep_map[pc_id]["standings"] = sorted(
            standings_by_char.get(pc_id, []),
            key=lambda x: x["org_name"].lower(),  # alphabetical — stable order in editor
        )

    # Party heat = highest individual heat among active runners
    party_heat = max(heat_values) if heat_values else 0

    team_score = round(sum(rep_scores) / len(rep_scores)) if rep_scores else 20
    avg_pa     = round(sum(pa_scores)  / len(pa_scores))  if pa_scores  else 0

    return {
        "heat":           party_heat,
        "heat_label":     heat_label(party_heat),
        "team_rep_score": team_score,
        "team_rep_tier":  team_rep_label(team_score),
        "avg_pa":         avg_pa,
        "pa_tier":        pa_label(avg_pa),
        "char_rep":       char_rep_map,
    }


@router.get("/", response_model=list[AdventureLogSummary])
def list_logs(
    outcome: str | None = Query(None),
    db: Session = Depends(get_db),
):
    q = db.query(AdventureLog)
    if outcome:
        q = q.filter(AdventureLog.outcome == outcome)
    return q.order_by(AdventureLog.session_date.desc(), AdventureLog.run_number.desc()).all()


@router.post("/", response_model=AdventureLogRead, status_code=201)
def create_log(body: AdventureLogCreate, db: Session = Depends(get_db)):
    data = body.model_dump(exclude={"participant_ids", "location_ids", "org_ids"})

    # Auto-assign run number (max existing + 1)
    max_run = db.query(func.max(AdventureLog.run_number)).scalar() or 0
    data["run_number"] = max_run + 1

    # Auto-generate consequence suggestions from tags
    if data.get("outcome_tags"):
        data["consequences_suggested"] = suggest(data["outcome_tags"])

    # Heat = average of PC heat changes applied on this run (falls back to 0)
    heat_deltas = [
        ch["delta"] for ch in (data.get("changes_applied") or [])
        if ch.get("type") == "heat" and isinstance(ch.get("delta"), (int, float))
    ]
    data["heat"] = round(sum(heat_deltas) / len(heat_deltas)) if heat_deltas else 0

    log = AdventureLog(**data)
    db.add(log)
    db.flush()  # get ID before resolving relations

    _resolve_relations(db, log, body.participant_ids, body.location_ids, body.org_ids)

    db.commit()
    return _get_or_404(db, log.id)


@router.post("/parse-narrative")
def parse_run_narrative(body: NarrativeParseRequest, db: Session = Depends(get_db)):
    """Use Claude to parse a GM narrative into structured run data + proposed world changes."""
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise HTTPException(status_code=503, detail="ANTHROPIC_API_KEY is not configured on the server")

    from app.services.narrative_parser import parse_narrative

    chars = db.query(Character).filter(Character.is_active == True).all()
    orgs  = db.query(Organization).filter(Organization.is_active == True).all()
    reps  = db.query(Reputation).all()
    standings = db.query(OrgStanding).all()

    world_context = {
        "characters":    [{"id": c.id, "name": c.name, "is_pc": c.is_pc} for c in chars],
        "organizations": [{"id": o.id, "name": o.name, "org_type": o.org_type} for o in orgs],
        "reputation":    [{"character_id": r.character_id, "street_cred": r.street_cred,
                           "notoriety": r.notoriety, "public_awareness": r.public_awareness} for r in reps],
        "standings":     [{"character_id": s.character_id, "org_id": s.organization_id,
                           "standing": s.standing} for s in standings],
    }

    try:
        result = parse_narrative(body.narrative, world_context)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Narrative parsing failed: {e}")

    # ── Heat calculation ──────────────────────────────────────────
    # Look up employer org by name (case-insensitive) to get tier/type
    employer_name = (result.get("employer") or "").strip().lower()
    employer_org  = next((o for o in orgs if o.name.lower() == employer_name), None)
    heat = compute_heat(
        outcome          = result.get("outcome"),
        outcome_tags     = result.get("outcome_tags"),
        employer_tier    = employer_org.tier    if employer_org else None,
        employer_org_type= employer_org.org_type if employer_org else None,
    )
    result["heat"]       = heat
    result["heat_label"] = heat_label(heat)

    # ── Faction ripple ────────────────────────────────────────────
    # Build a lightweight org map for ripple lookups
    org_map = {
        o.id: {"name": o.name, "ally_ids": o.ally_ids or [], "enemy_ids": o.enemy_ids or []}
        for o in orgs
    }
    # Deduplicate ripple: keep the largest-magnitude entry per (character_id, org_id)
    ripple_index: dict[tuple, dict] = {}
    for ch in result.get("proposed_changes", []):
        if ch.get("type") == "org_standing" and ch.get("org_id") and ch.get("delta"):
            for rpl in compute_ripple(ch["org_id"], ch["delta"], org_map):
                rpl["character_id"]   = ch["character_id"]
                rpl["character_name"] = ch.get("character_name")
                key = (rpl["character_id"], rpl["org_id"])
                if key not in ripple_index or abs(rpl["delta"]) > abs(ripple_index[key]["delta"]):
                    ripple_index[key] = rpl
    result["proposed_changes"] = result.get("proposed_changes", []) + list(ripple_index.values())

    return result


@router.post("/apply-changes")
def apply_world_changes(body: ApplyChangesRequest, db: Session = Depends(get_db)):
    """Apply a reviewed set of world-state changes (nuyen, reputation, org standings)."""
    applied = []
    errors  = []

    for ch in body.changes:
        try:
            if ch.type in ("street_cred", "notoriety", "public_awareness"):
                rep = db.query(Reputation).filter(Reputation.character_id == ch.character_id).first()
                if not rep:
                    errors.append(f"No reputation record for character {ch.character_id}"); continue
                old = getattr(rep, ch.type, 0) or 0
                setattr(rep, ch.type, max(0, old + ch.delta))
                if ch.type == "public_awareness":
                    rep.pa_updated_at = date.today()
                applied.append({"desc": f"{ch.character_name or ch.character_id}: {ch.type} {ch.delta:+}", "reason": ch.reason})

            elif ch.type == "heat":
                rep = db.query(Reputation).filter(Reputation.character_id == ch.character_id).first()
                if not rep:
                    errors.append(f"No reputation record for character {ch.character_id}"); continue
                rep.heat = min(10, max(0, (rep.heat or 0) + ch.delta))
                applied.append({"desc": f"{ch.character_name or ch.character_id}: heat {ch.delta:+} → {rep.heat}", "reason": ch.reason})

            elif ch.type == "org_standing":
                if not ch.org_id:
                    errors.append("org_id required for org_standing change"); continue
                standing = db.query(OrgStanding).filter(
                    OrgStanding.character_id == ch.character_id,
                    OrgStanding.organization_id == ch.org_id,
                ).first()
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
                applied.append({"desc": f"{ch.character_name or ch.character_id} ↔ {ch.org_name or ch.org_id}: standing {ch.delta:+}", "reason": ch.reason})

            else:
                errors.append(f"Unknown change type: {ch.type}")
        except Exception as e:
            errors.append(f"Error on {ch.type} for char {ch.character_id}: {e}")

    db.commit()
    return {"applied": applied, "errors": errors}


@router.get("/{log_id}", response_model=AdventureLogRead)
def get_log(log_id: int, db: Session = Depends(get_db)):
    return _get_or_404(db, log_id)


@router.patch("/{log_id}", response_model=AdventureLogRead)
def update_log(log_id: int, body: AdventureLogUpdate, db: Session = Depends(get_db)):
    log = _get_or_404(db, log_id)
    data = body.model_dump(exclude_unset=True, exclude={"participant_ids", "location_ids", "org_ids"})

    # Regenerate suggestions if tags changed
    if "outcome_tags" in data:
        data["consequences_suggested"] = suggest(data["outcome_tags"])

    for field, value in data.items():
        setattr(log, field, value)

    _resolve_relations(
        db, log,
        body.participant_ids if body.participant_ids is not None else None,
        body.location_ids if body.location_ids is not None else None,
        body.org_ids if body.org_ids is not None else None,
    )

    db.commit()
    return _get_or_404(db, log.id)


@router.delete("/{log_id}", status_code=204)
def delete_log(log_id: int, db: Session = Depends(get_db)):
    log = _get_or_404(db, log_id)
    db.delete(log)
    db.commit()


@router.post("/{log_id}/refresh-consequences", response_model=AdventureLogRead)
def refresh_consequences(log_id: int, db: Session = Depends(get_db)):
    """Regenerate consequence suggestions for an existing log (useful after updating tags)."""
    log = _get_or_404(db, log_id)
    log.consequences_suggested = suggest(log.outcome_tags or [])
    db.commit()
    return _get_or_404(db, log_id)
