from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.auth.core import verify_admin_token, verify_user_token, is_default_admin_password, generate_token, get_token_record
from app.auth.dependencies import get_admin_token, get_any_token
from app.models.auth import UserToken
from app.models.character import Character
from app.schemas.auth import VerifyRequest, VerifyResponse, UserTokenCreate, UserTokenRead, UserTokenLabelUpdate

router = APIRouter()


# ── Verify ───────────────────────────────────────────────────────────────────

@router.post("/verify", response_model=VerifyResponse)
def verify(body: VerifyRequest, db: Session = Depends(get_db)):
    is_admin = bool(body.admin_token and verify_admin_token(db, body.admin_token))
    # Admin tokens also grant user access; player tokens grant user-only
    is_user = is_admin or bool(body.user_token and verify_user_token(db, body.user_token))

    if not is_admin and not is_user:
        raise HTTPException(status_code=401, detail="No valid token")

    used_token = body.admin_token if is_admin else body.user_token
    record = get_token_record(db, used_token) if used_token else None

    return VerifyResponse(
        is_admin=is_admin,
        is_user=is_user,
        is_default_password=is_admin and is_default_admin_password(db),
        user_token=body.user_token if (is_user and not is_admin) else None,
        token_label=record.label if record else None,
    )


# ── Token management ──────────────────────────────────────────────────────────

@router.post("/tokens", response_model=UserTokenRead)
def create_token(
    body: UserTokenCreate,
    db: Session = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    token = generate_token(24)
    ut = UserToken(token=token, label=body.label, is_admin=body.is_admin)
    db.add(ut)
    db.commit()
    db.refresh(ut)
    return ut


@router.get("/tokens", response_model=list[UserTokenRead])
def list_tokens(db: Session = Depends(get_db), _: str = Depends(get_admin_token)):
    return db.query(UserToken).order_by(UserToken.is_admin.desc(), UserToken.created_at.desc()).all()


@router.patch("/tokens/me", response_model=UserTokenRead)
def rename_own_token(
    body: UserTokenLabelUpdate,
    db: Session = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    ut = get_token_record(db, ctx["user_token"])
    if not ut:
        raise HTTPException(status_code=404, detail="Token not found")
    ut.label = body.label
    db.commit()
    db.refresh(ut)
    return ut


@router.patch("/tokens/{token_id}", response_model=UserTokenRead)
def rename_token(
    token_id: int,
    body: UserTokenLabelUpdate,
    db: Session = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    ut = db.query(UserToken).filter(UserToken.id == token_id).first()
    if not ut:
        raise HTTPException(status_code=404, detail="Token not found")
    ut.label = body.label
    db.commit()
    db.refresh(ut)
    return ut


@router.delete("/tokens/{token_id}", status_code=204)
def revoke_token(
    token_id: int,
    db: Session = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    ut = db.query(UserToken).filter(UserToken.id == token_id).first()
    if not ut:
        raise HTTPException(status_code=404, detail="Token not found")
    # Unclaim any characters owned by this token before deleting it
    db.query(Character).filter(Character.owner_token == ut.token).update({"owner_token": None})
    db.delete(ut)
    db.commit()
