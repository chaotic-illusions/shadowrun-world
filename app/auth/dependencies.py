from fastapi import Depends, Header, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.auth.core import verify_admin_token, verify_user_token
from app.auth.rate_limit import enforce_rate_limit, record_failure, record_success


async def get_admin_token(
    request: Request,
    x_admin_token: str | None = Header(default=None, alias="X-Admin-Token"),
    db: AsyncSession = Depends(get_db),
    _rl: None = Depends(enforce_rate_limit),
) -> str:
    if not x_admin_token or not await verify_admin_token(db, x_admin_token):
        record_failure(request)
        raise HTTPException(status_code=403, detail="Admin token required")
    record_success(request)
    return x_admin_token


async def get_any_token(
    request: Request,
    x_admin_token: str | None = Header(default=None, alias="X-Admin-Token"),
    x_user_token: str | None = Header(default=None, alias="X-User-Token"),
    db: AsyncSession = Depends(get_db),
    _rl: None = Depends(enforce_rate_limit),
) -> dict:
    if x_admin_token and await verify_admin_token(db, x_admin_token):
        record_success(request)
        return {"is_admin": True, "is_user": True, "user_token": x_admin_token}
    if x_user_token and await verify_user_token(db, x_user_token):
        record_success(request)
        return {"is_admin": False, "is_user": True, "user_token": x_user_token}
    record_failure(request)
    raise HTTPException(status_code=401, detail="Valid token required")
