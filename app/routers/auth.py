from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.auth.core import (
    verify_admin_token, verify_user_token, is_default_admin_password,
    generate_token, hash_token, get_token_record,
)
from app.auth.dependencies import get_admin_token, get_any_token
from app.auth.rate_limit import enforce_rate_limit, record_failure, record_success
from app.models.auth import UserToken
from app.models.character import Character
from app.schemas.auth import (
    VerifyRequest, VerifyResponse, UserTokenCreate,
    UserTokenRead, UserTokenCreateResponse, UserTokenLabelUpdate,
)

router = APIRouter()


# ── Verify ───────────────────────────────────────────────────────────────────

@router.post("/verify", response_model=VerifyResponse, dependencies=[Depends(enforce_rate_limit)])
async def verify(body: VerifyRequest, request: Request, db: AsyncSession = Depends(get_db)):
    is_admin = bool(body.admin_token and await verify_admin_token(db, body.admin_token))
    is_user = is_admin or bool(body.user_token and await verify_user_token(db, body.user_token))

    if not is_admin and not is_user:
        record_failure(request)
        raise HTTPException(status_code=401, detail="No valid token")

    record_success(request)
    used_token = body.admin_token if is_admin else body.user_token
    token_record = await get_token_record(db, used_token) if used_token else None

    return VerifyResponse(
        is_admin=is_admin,
        is_user=is_user,
        is_default_password=is_admin and await is_default_admin_password(db),
        user_token=body.user_token if (is_user and not is_admin) else None,
        token_label=token_record.label if token_record else None,
    )


# ── Token management ──────────────────────────────────────────────────────────

@router.post("/tokens", response_model=UserTokenCreateResponse)
async def create_token(
    body: UserTokenCreate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    plaintext = generate_token(24)
    ut = UserToken(token_hash=hash_token(plaintext), label=body.label, is_admin=body.is_admin)
    db.add(ut)
    await db.commit()
    await db.refresh(ut)
    # Return the plaintext token once; it's never stored or retrievable again
    return UserTokenCreateResponse(
        id=ut.id,
        token=plaintext,
        label=ut.label,
        is_admin=ut.is_admin,
        created_at=ut.created_at,
    )


@router.get("/tokens", response_model=list[UserTokenRead])
async def list_tokens(db: AsyncSession = Depends(get_db), _: str = Depends(get_admin_token)):
    result = await db.execute(
        select(UserToken).order_by(UserToken.is_admin.desc(), UserToken.created_at.desc())
    )
    return result.scalars().all()


@router.patch("/tokens/me", response_model=UserTokenRead)
async def rename_own_token(
    body: UserTokenLabelUpdate,
    db: AsyncSession = Depends(get_db),
    ctx: dict = Depends(get_any_token),
):
    ut = await get_token_record(db, ctx["user_token"])
    if not ut:
        raise HTTPException(status_code=404, detail="Token not found")
    ut.label = body.label
    await db.commit()
    await db.refresh(ut)
    return ut


@router.patch("/tokens/{token_id}", response_model=UserTokenRead)
async def rename_token(
    token_id: int,
    body: UserTokenLabelUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    result = await db.execute(select(UserToken).where(UserToken.id == token_id))
    ut = result.scalars().first()
    if not ut:
        raise HTTPException(status_code=404, detail="Token not found")
    ut.label = body.label
    await db.commit()
    await db.refresh(ut)
    return ut


@router.post("/tokens/{token_id}/regenerate", response_model=UserTokenCreateResponse)
async def regenerate_token(
    token_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    result = await db.execute(select(UserToken).where(UserToken.id == token_id))
    ut = result.scalars().first()
    if not ut:
        raise HTTPException(status_code=404, detail="Token not found")
    # Re-point any characters owned by the old hash to the new hash
    plaintext = generate_token(24)
    new_hash = hash_token(plaintext)
    char_result = await db.execute(
        select(Character).where(Character.owner_token == ut.token_hash)
    )
    for char in char_result.scalars().all():
        char.owner_token = new_hash
    ut.token_hash = new_hash
    await db.commit()
    await db.refresh(ut)
    return UserTokenCreateResponse(
        id=ut.id,
        token=plaintext,
        label=ut.label,
        is_admin=ut.is_admin,
        created_at=ut.created_at,
    )


@router.delete("/tokens/{token_id}", status_code=204)
async def revoke_token(
    token_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    result = await db.execute(select(UserToken).where(UserToken.id == token_id))
    ut = result.scalars().first()
    if not ut:
        raise HTTPException(status_code=404, detail="Token not found")
    # Unclaim any characters owned by this token's hash before deleting it
    char_result = await db.execute(
        select(Character).where(Character.owner_token == ut.token_hash)
    )
    for char in char_result.scalars().all():
        char.owner_token = None
    await db.delete(ut)
    await db.commit()
