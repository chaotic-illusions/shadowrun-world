from datetime import datetime, UTC
from typing import Optional
from sqlalchemy import String, Text, Integer, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.associations import log_characters


class Character(Base):
    __tablename__ = "characters"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), index=True)
    is_pc: Mapped[bool] = mapped_column(default=True)
    archetype: Mapped[str | None] = mapped_column(String(100), default=None)
    title: Mapped[str | None] = mapped_column(String(200), default=None)
    race: Mapped[str] = mapped_column(String(50), default="Human")
    nationality: Mapped[str | None] = mapped_column(String(100), default=None)
    gender: Mapped[str | None] = mapped_column(String(50), default=None)
    age: Mapped[int | None] = mapped_column(Integer, default=None)
    description: Mapped[str | None] = mapped_column(Text, default=None)
    background: Mapped[str | None] = mapped_column(Text, default=None)
    show_background: Mapped[bool] = mapped_column(default=False)

    # Services/skills this NPC can provide as a contact
    contact_skills: Mapped[list] = mapped_column(JSON, default=list)

    # NPC connection rating (1-6); not applicable to PCs
    connection: Mapped[int] = mapped_column(Integer, default=1)

    organization_id: Mapped[int | None] = mapped_column(ForeignKey("organizations.id"), default=None)

    karma_total: Mapped[int] = mapped_column(Integer, default=0)
    karma_current: Mapped[int] = mapped_column(Integer, default=0)

    is_active: Mapped[bool] = mapped_column(default=True)
    notes: Mapped[str | None] = mapped_column(Text, default=None)
    # SHA-256 hash of the owning player's token
    owner_token: Mapped[str | None] = mapped_column(String(64), default=None, index=True)

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )

    organization: Mapped[Optional["Organization"]] = relationship(
        "Organization", foreign_keys=[organization_id]
    )

    @property
    def organization_name(self) -> str | None:
        return self.organization.name if self.organization else None

    @property
    def is_claimed(self) -> bool:
        return self.owner_token is not None

    contacts: Mapped[list["Contact"]] = relationship(
        "Contact", foreign_keys="Contact.owner_id", back_populates="owner", cascade="all, delete-orphan"
    )
    reputation: Mapped[Optional["Reputation"]] = relationship(
        "Reputation", back_populates="character", uselist=False, cascade="all, delete-orphan"
    )
    org_standings: Mapped[list["OrgStanding"]] = relationship(
        "OrgStanding", back_populates="character", cascade="all, delete-orphan"
    )
    adventure_logs: Mapped[list["AdventureLog"]] = relationship(
        "AdventureLog", secondary=log_characters, back_populates="participants"
    )
