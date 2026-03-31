from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from app.db.base import Base


class UserToken(Base):
    """
    Tokens distributed to players (is_admin=False) or used as admin credentials (is_admin=True).
    Admin tokens are generated once and stored here as plaintext hex — no bcrypt needed.
    Bootstrap: if no active admin token exists in this table, 'shadowrunner' is accepted.
    """
    __tablename__ = "auth_user_tokens"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(64), unique=True, nullable=False, index=True)
    label = Column(String(200), nullable=True)
    is_admin = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
