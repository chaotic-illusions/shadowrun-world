from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.auth.core import verify_admin_token, verify_user_token


def get_admin_token(
    x_admin_token: str | None = Header(default=None, alias="X-Admin-Token"),
    db: Session = Depends(get_db),
) -> str:
    if not x_admin_token or not verify_admin_token(db, x_admin_token):
        raise HTTPException(status_code=403, detail="Admin token required")
    return x_admin_token


def get_any_token(
    x_admin_token: str | None = Header(default=None, alias="X-Admin-Token"),
    x_user_token: str | None = Header(default=None, alias="X-User-Token"),
    db: Session = Depends(get_db),
) -> dict:
    if x_admin_token and verify_admin_token(db, x_admin_token):
        return {"is_admin": True, "is_user": True, "user_token": x_admin_token}
    if x_user_token and verify_user_token(db, x_user_token):
        return {"is_admin": False, "is_user": True, "user_token": x_user_token}
    raise HTTPException(status_code=401, detail="Valid token required")
