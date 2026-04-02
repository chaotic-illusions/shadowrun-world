from fastapi import APIRouter, Depends, HTTPException, Query, Header
from sqlalchemy.orm import Session, selectinload
from app.dependencies import get_db, get_or_404, apply_update
from app.models.character import Character
from app.models.reputation import Reputation
from app.schemas.character import CharacterCreate, CharacterUpdate, CharacterRead, CharacterSummary
from app.schemas.contact import ContactRead
from app.schemas.reputation import ReputationRead
from app.auth.core import verify_user_token, verify_admin_token
from app.auth.dependencies import get_admin_token

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


# ── Claim / unclaim ───────────────────────────────────────────────────────────

@router.post("/{character_id}/claim", response_model=CharacterRead)
def claim_character(
    character_id: int,
    db: Session = Depends(get_db),
    x_user_token: str | None = Header(default=None, alias="X-User-Token"),
    x_admin_token: str | None = Header(default=None, alias="X-Admin-Token"),
):
    """Player or admin (in runner mode) claims a PC by writing their token onto it."""
    # Resolve whichever valid token was provided — user token takes priority
    if x_user_token and verify_user_token(db, x_user_token):
        claim_token = x_user_token
    elif x_admin_token and verify_admin_token(db, x_admin_token):
        claim_token = x_admin_token
    else:
        raise HTTPException(status_code=403, detail="Valid user token required to claim a character")
    char = get_or_404(db, Character, character_id)
    if not char.is_pc:
        raise HTTPException(status_code=400, detail="Only PC characters can be claimed")
    if char.owner_token and char.owner_token != claim_token:
        raise HTTPException(status_code=409, detail="Character is already claimed by another player")
    char.owner_token = claim_token
    db.commit()
    db.refresh(char)
    return char


@router.post("/{character_id}/unclaim", response_model=CharacterRead)
def unclaim_character(
    character_id: int,
    db: Session = Depends(get_db),
    x_admin_token: str | None = Header(default=None, alias="X-Admin-Token"),
    x_user_token: str | None = Header(default=None, alias="X-User-Token"),
):
    """Admin or the owning player can unclaim a character."""
    char = get_or_404(db, Character, character_id)
    is_admin = bool(x_admin_token and verify_admin_token(db, x_admin_token))
    is_owner = bool(x_user_token and char.owner_token == x_user_token)
    if not is_admin and not is_owner:
        raise HTTPException(status_code=403, detail="Only the owning player or an admin can unclaim")
    char.owner_token = None
    db.commit()
    db.refresh(char)
    return char
