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
        record_failure(request, "admin")
        raise HTTPException(status_code=403, detail="Admin token required")
    record_success(request, "admin")
    return x_admin_token


async def get_any_token(
    request: Request,
    x_admin_token: str | None = Header(default=None, alias="X-Admin-Token"),
    x_user_token: str | None = Header(default=None, alias="X-User-Token"),
    x_runner_view: str | None = Header(default=None, alias="X-Runner-View"),
    db: AsyncSession = Depends(get_db),
    _rl: None = Depends(enforce_rate_limit),
) -> dict:
    # Presentation-only preview flag: an admin can request the exact PLAYER payload by sending
    # X-Runner-View (set by the UI "runner view" toggle). It ONLY forces GM-data redaction in the
    # serializers -- authorization is unchanged (is_admin stays true, so access checks and
    # admin-only guards still hold), and it can only ever REDUCE what is returned, never escalate.
    view_as_player = x_runner_view not in (None, "", "0", "false", "False")
    if x_admin_token and await verify_admin_token(db, x_admin_token):
        record_success(request, "admin")
        return {"is_admin": True, "is_user": True, "user_token": x_admin_token,
                "view_as_player": view_as_player}
    if x_admin_token:
        record_failure(request, "admin")
    if x_user_token and await verify_user_token(db, x_user_token):
        record_success(request, "user")
        return {"is_admin": False, "is_user": True, "user_token": x_user_token,
                "view_as_player": view_as_player}
    record_failure(request, "user")
    raise HTTPException(status_code=401, detail="Valid token required")
