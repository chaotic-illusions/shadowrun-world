from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.reputation import Reputation, OrgStanding
from app.schemas.reputation import (
    ReputationCreate, ReputationUpdate, ReputationRead,
    OrgStandingCreate, OrgStandingUpdate, OrgStandingRead,
)

router = APIRouter()


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
    rep = db.query(Reputation).filter(Reputation.id == rep_id).first()
    if not rep:
        raise HTTPException(status_code=404, detail="Reputation record not found")
    for field, value in body.model_dump(exclude_unset=True).items():
        setattr(rep, field, value)
    db.commit()
    db.refresh(rep)
    return rep


@router.delete("/{rep_id}", status_code=204)
def delete_reputation(rep_id: int, db: Session = Depends(get_db)):
    rep = db.query(Reputation).filter(Reputation.id == rep_id).first()
    if not rep:
        raise HTTPException(status_code=404, detail="Reputation record not found")
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
    standing = db.query(OrgStanding).filter(OrgStanding.id == standing_id).first()
    if not standing:
        raise HTTPException(status_code=404, detail="Standing not found")
    for field, value in body.model_dump(exclude_unset=True).items():
        setattr(standing, field, value)
    db.commit()
    db.refresh(standing)
    return standing


@router.delete("/standings/{standing_id}", status_code=204)
def delete_org_standing(standing_id: int, db: Session = Depends(get_db)):
    standing = db.query(OrgStanding).filter(OrgStanding.id == standing_id).first()
    if not standing:
        raise HTTPException(status_code=404, detail="Standing not found")
    db.delete(standing)
    db.commit()
