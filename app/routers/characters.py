from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, selectinload
from app.dependencies import get_db, get_or_404, apply_update
from app.models.character import Character
from app.models.reputation import Reputation
from app.schemas.character import CharacterCreate, CharacterUpdate, CharacterRead, CharacterSummary
from app.schemas.contact import ContactRead
from app.schemas.reputation import ReputationRead

router = APIRouter()


@router.get("/", response_model=list[CharacterRead])
def list_characters(
    is_pc: bool | None = Query(None, description="Filter by PC (true) or NPC (false)"),
    is_active: bool | None = Query(None),
    db: Session = Depends(get_db),
):
    q = db.query(Character)
    if is_pc is not None:
        q = q.filter(Character.is_pc == is_pc)
    if is_active is not None:
        q = q.filter(Character.is_active == is_active)
    return q.order_by(Character.name).all()


@router.post("/", response_model=CharacterRead, status_code=201)
def create_character(body: CharacterCreate, db: Session = Depends(get_db)):
    char = Character(**body.model_dump())
    db.add(char)
    db.commit()
    db.refresh(char)
    return char


@router.get("/{character_id}", response_model=CharacterRead)
def get_character(character_id: int, db: Session = Depends(get_db)):
    return get_or_404(db, Character, character_id)


@router.patch("/{character_id}", response_model=CharacterRead)
def update_character(character_id: int, body: CharacterUpdate, db: Session = Depends(get_db)):
    char = get_or_404(db, Character, character_id)
    apply_update(db, char, body)
    return char


@router.delete("/{character_id}", status_code=204)
def delete_character(character_id: int, db: Session = Depends(get_db)):
    char = get_or_404(db, Character, character_id)
    db.delete(char)
    db.commit()


@router.get("/{character_id}/contacts", response_model=list[ContactRead])
def get_character_contacts(character_id: int, db: Session = Depends(get_db)):
    char = db.query(Character).options(selectinload(Character.contacts)).filter(Character.id == character_id).first()
    if not char:
        raise HTTPException(status_code=404, detail="Character not found")  # needs eager load, can't use get_or_404
    return char.contacts


@router.get("/{character_id}/reputation", response_model=ReputationRead | None)
def get_character_reputation(character_id: int, db: Session = Depends(get_db)):
    get_or_404(db, Character, character_id)
    return db.query(Reputation).filter(Reputation.character_id == character_id).first()
