from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_or_404, apply_update
from app.models.adventure_log import AdventureLog
from app.models.character import Character
from app.models.reputation import Reputation, OrgStanding
from app.schemas.reputation import (
    ReputationCreate, ReputationUpdate, ReputationRead,
    OrgStandingCreate, OrgStandingUpdate, OrgStandingRead,
)

router = APIRouter()


def _current_tick(db: Session) -> int:
    return db.query(func.sum(AdventureLog.tick_count)).scalar() or 0


# --- Reputation (Street Cred / Notoriety / Public Awareness) ---

@router.get("/", response_model=list[ReputationRead])
def list_reputations(
    character_id: int | None = Query(None),
    db: Session = Depends(get_db),
):
    q = db.query(Reputation)
    if character_id is not None:
        q = q.filter(Reputation.character_id == character_id)
    return q.all()


@router.post("/", response_model=ReputationRead, status_code=201)
def create_reputation(body: ReputationCreate, db: Session = Depends(get_db)):
    existing = db.query(Reputation).filter(Reputation.character_id == body.character_id).first()
    if existing:
        raise HTTPException(status_code=409, detail="Reputation record already exists for this character")
    rep = Reputation(**body.model_dump())
    db.add(rep)
    db.commit()
    db.refresh(rep)
    return rep


@router.patch("/{rep_id}", response_model=ReputationRead)
def update_reputation(rep_id: int, body: ReputationUpdate, db: Session = Depends(get_db)):
    rep = get_or_404(db, Reputation, rep_id)
    apply_update(db, rep, body)
    # Auto-stamp timestamps + ticks when values change (if caller didn't provide one)
    if body.public_awareness is not None and body.pa_updated_at is None:
        rep.pa_updated_at = date.today()
        rep.pa_stamped_tick = _current_tick(db)
    if body.heat is not None and body.heat_updated_at is None:
        rep.heat_updated_at = date.today()
        rep.heat_stamped_tick = _current_tick(db)
    db.commit()
    db.refresh(rep)
    return rep


@router.delete("/{rep_id}", status_code=204)
def delete_reputation(rep_id: int, db: Session = Depends(get_db)):
    rep = get_or_404(db, Reputation, rep_id)
    db.delete(rep)
    db.commit()


# --- Org Standings ---

@router.get("/standings", response_model=list[OrgStandingRead])
def list_org_standings(
    character_id: int | None = Query(None),
    organization_id: int | None = Query(None),
    db: Session = Depends(get_db),
):
    q = db.query(OrgStanding)
    if character_id is not None:
        q = q.filter(OrgStanding.character_id == character_id)
    if organization_id is not None:
        q = q.filter(OrgStanding.organization_id == organization_id)
    return q.all()


@router.post("/standings", response_model=OrgStandingRead, status_code=201)
def create_org_standing(body: OrgStandingCreate, db: Session = Depends(get_db)):
    existing = db.query(OrgStanding).filter(
        OrgStanding.character_id == body.character_id,
        OrgStanding.organization_id == body.organization_id,
    ).first()
    if existing:
        raise HTTPException(status_code=409, detail="Standing already exists for this character/org pair")
    standing = OrgStanding(**body.model_dump())
    db.add(standing)
    db.commit()
    db.refresh(standing)
    return standing


@router.patch("/standings/{standing_id}", response_model=OrgStandingRead)
def update_org_standing(standing_id: int, body: OrgStandingUpdate, db: Session = Depends(get_db)):
    standing = get_or_404(db, OrgStanding, standing_id)
    apply_update(db, standing, body)
    if body.standing is not None:
        standing.standings_updated_at = date.today()
        standing.standings_stamped_tick = _current_tick(db)
        db.commit()
        db.refresh(standing)
    return standing


@router.delete("/standings/{standing_id}", status_code=204)
def delete_org_standing(standing_id: int, db: Session = Depends(get_db)):
    standing = get_or_404(db, OrgStanding, standing_id)
    db.delete(standing)
    db.commit()


# --- Admin Utilities ---

@router.post("/reset-pc-data", status_code=200)
def reset_all_pc_data(db: Session = Depends(get_db)):
    """Reset all PC heat, reputation, and org standings to baseline (for testing)."""
    pc_ids = [c.id for c in db.query(Character).filter(Character.is_pc == True).all()]
    if pc_ids:
        for rep in db.query(Reputation).filter(Reputation.character_id.in_(pc_ids)).all():
            rep.street_cred = 0
            rep.notoriety = 0
            rep.public_awareness = 0
            rep.pa_updated_at = None
            rep.heat = 0
            rep.heat_updated_at = None
        db.query(OrgStanding).filter(OrgStanding.character_id.in_(pc_ids)).delete(
            synchronize_session="fetch"
        )
    db.commit()
    return {"reset": len(pc_ids), "message": f"Reset reputation data for {len(pc_ids)} PCs"}
