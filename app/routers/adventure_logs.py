from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, selectinload
from app.dependencies import get_db
from app.models.adventure_log import AdventureLog
from app.models.character import Character
from app.models.location import Location
from app.models.organization import Organization
from app.schemas.adventure_log import (
    AdventureLogCreate, AdventureLogUpdate, AdventureLogRead, AdventureLogSummary
)
from app.services.consequence_engine import suggest

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
