from typing import Optional
from sqlalchemy import String, Text, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), index=True)
    profession: Mapped[str | None] = mapped_column(String(100), default=None)
    race: Mapped[str | None] = mapped_column(String(50), default=None)
    loyalty: Mapped[int] = mapped_column(Integer, default=1)
    connection: Mapped[int] = mapped_column(Integer, default=1)
    description: Mapped[str | None] = mapped_column(Text, default=None)
    notes: Mapped[str | None] = mapped_column(Text, default=None)

    owner_id: Mapped[int] = mapped_column(ForeignKey("characters.id"))
    npc_id: Mapped[int | None] = mapped_column(ForeignKey("characters.id"), default=None)
    location_id: Mapped[int | None] = mapped_column(ForeignKey("locations.id"), default=None)
    organization_id: Mapped[int | None] = mapped_column(ForeignKey("organizations.id"), default=None)
    is_active: Mapped[bool] = mapped_column(default=True)

    __table_args__ = (
        CheckConstraint("loyalty >= 1 AND loyalty <= 6", name="ck_contact_loyalty"),
        CheckConstraint("connection >= 1 AND connection <= 6", name="ck_contact_connection"),
    )

    owner: Mapped["Character"] = relationship("Character", foreign_keys=[owner_id], back_populates="contacts")
    npc: Mapped[Optional["Character"]] = relationship("Character", foreign_keys=[npc_id])
    location: Mapped[Optional["Location"]] = relationship("Location", back_populates="contacts")
    organization: Mapped[Optional["Organization"]] = relationship("Organization", back_populates="contacts")
