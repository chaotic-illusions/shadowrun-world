from datetime import datetime, UTC
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class UserToken(Base):
    """
    Tokens distributed to players (is_admin=False) or used as admin credentials (is_admin=True).
    Tokens are stored as SHA-256 hashes -- the plaintext is shown only at creation time.
    Bootstrap: if no active admin token exists in this table, the BOOTSTRAP_ADMIN_KEY env var is accepted.
    """
    __tablename__ = "auth_user_tokens"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    token_hash: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
    label: Mapped[str | None] = mapped_column(String(200), default=None)
    is_admin: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
