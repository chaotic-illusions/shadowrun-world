from datetime import datetime, UTC
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class HouseRule(Base):
    __tablename__ = "house_rules"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(300))
    # combat, magic, decking, rigging, skills, character_creation, gear, vehicles, other
    category: Mapped[str | None] = mapped_column(String(100), default=None)
    source_reference: Mapped[str | None] = mapped_column(String(200), default=None)
    original_rule: Mapped[str | None] = mapped_column(Text, default=None)
    modification: Mapped[str] = mapped_column(Text)
    reason: Mapped[str | None] = mapped_column(Text, default=None)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )
