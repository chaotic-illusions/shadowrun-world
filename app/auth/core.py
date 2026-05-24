import hashlib
import os
import secrets
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.auth import UserToken

DEFAULT_ADMIN_PASSWORD = os.environ.get("BOOTSTRAP_ADMIN_KEY", "shadowrunner")


def hash_token(token: str) -> str:
    """SHA-256 hash a plaintext token for storage / comparison."""
    return hashlib.sha256(token.encode()).hexdigest()


def generate_token(nbytes: int = 24) -> str:
    """Return a cryptographically random hex token (plaintext)."""
    return secrets.token_hex(nbytes)


async def _active_admin_exists(db: AsyncSession) -> bool:
    result = await db.execute(
        select(UserToken).where(UserToken.is_admin == True).limit(1)  # noqa: E712
    )
    return result.scalars().first() is not None


async def verify_admin_token(db: AsyncSession, token: str) -> bool:
    """Returns True if token matches any admin token, or the bootstrap default."""
    h = hash_token(token)
    result = await db.execute(
        select(UserToken).where(UserToken.token_hash == h, UserToken.is_admin == True)  # noqa: E712
    )
    if result.scalars().first():
        return True
    # Fall back to bootstrap default only when no admin tokens exist yet
    if not await _active_admin_exists(db):
        return secrets.compare_digest(token, DEFAULT_ADMIN_PASSWORD)
    return False


async def is_default_admin_password(db: AsyncSession) -> bool:
    """True if no admin tokens have been created yet -- user needs to set one."""
    return not await _active_admin_exists(db)


async def get_token_record(db: AsyncSession, token: str) -> UserToken | None:
    """Returns the token record for any plaintext token string."""
    h = hash_token(token)
    result = await db.execute(select(UserToken).where(UserToken.token_hash == h))
    return result.scalars().first()


async def verify_user_token(db: AsyncSession, token: str) -> UserToken | None:
    """Returns the token record if the hash matches."""
    h = hash_token(token)
    result = await db.execute(select(UserToken).where(UserToken.token_hash == h))
    return result.scalars().first()
