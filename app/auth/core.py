import secrets
from sqlalchemy.orm import Session

from app.models.auth import UserToken

DEFAULT_ADMIN_PASSWORD = "shadowrunner"


def generate_token(nbytes: int = 24) -> str:
    return secrets.token_hex(nbytes)


def _active_admin_exists(db: Session) -> bool:
    return db.query(UserToken).filter(
        UserToken.is_admin == True,  # noqa: E712
    ).first() is not None


def verify_admin_token(db: Session, token: str) -> bool:
    """Returns True if token matches any admin token, or the bootstrap default."""
    result = db.query(UserToken).filter(
        UserToken.token == token,
        UserToken.is_admin == True,  # noqa: E712
    ).first()
    if result:
        return True
    # Fall back to bootstrap default only when no admin tokens exist yet
    if not _active_admin_exists(db):
        return secrets.compare_digest(token, DEFAULT_ADMIN_PASSWORD)
    return False


def is_default_admin_password(db: Session) -> bool:
    """True if no admin tokens have been created yet — user needs to set one."""
    return not _active_admin_exists(db)


def get_token_record(db: Session, token: str) -> UserToken | None:
    """Returns the token record for any token string."""
    return db.query(UserToken).filter(UserToken.token == token).first()


def verify_user_token(db: Session, token: str) -> UserToken | None:
    """Returns the token record if it exists."""
    return db.query(UserToken).filter(UserToken.token == token).first()
