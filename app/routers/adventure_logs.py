import os
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
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


# ── Narrative parsing schemas ─────────────────────────────────
class NarrativeParseRequest(BaseModel):
    narrative: str


class ChangeItem(BaseModel):
    type: str                          # nuyen | street_cred | notoriety | public_awareness | org_standing
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

    # Auto-generate consequence suggestions from tags
    if data.get("outcome_tags"):
        data["consequences_suggested"] = suggest(data["outcome_tags"])

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
        "characters":    [{"id": c.id, "name": c.name, "is_pc": c.is_pc, "nuyen": c.nuyen or 0} for c in chars],
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

    return result


@router.post("/apply-changes")
def apply_world_changes(body: ApplyChangesRequest, db: Session = Depends(get_db)):
    """Apply a reviewed set of world-state changes (nuyen, reputation, org standings)."""
    applied = []
    errors  = []

    for ch in body.changes:
        try:
            if ch.type == "nuyen":
                char = db.query(Character).filter(Character.id == ch.character_id).first()
                if not char:
                    errors.append(f"Character {ch.character_id} not found"); continue
                char.nuyen = max(0, (char.nuyen or 0) + ch.delta)
                applied.append({"desc": f"{ch.character_name or char.name}: nuyen {ch.delta:+,} → ¥{char.nuyen:,}", "reason": ch.reason})

            elif ch.type in ("street_cred", "notoriety", "public_awareness"):
                rep = db.query(Reputation).filter(Reputation.character_id == ch.character_id).first()
                if not rep:
                    errors.append(f"No reputation record for character {ch.character_id}"); continue
                old = getattr(rep, ch.type, 0) or 0
                setattr(rep, ch.type, max(0, old + ch.delta))
                applied.append({"desc": f"{ch.character_name or ch.character_id}: {ch.type} {ch.delta:+}", "reason": ch.reason})

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
