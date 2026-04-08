from datetime import date
from sqlalchemy import String, Text, Integer, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class Reputation(Base):
    """SR2 reputation tracks for a player character."""
    __tablename__ = "reputations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    character_id: Mapped[int] = mapped_column(ForeignKey("characters.id"), unique=True)

    street_cred: Mapped[int] = mapped_column(Integer, default=0)
    notoriety: Mapped[int] = mapped_column(Integer, default=0)
    public_awareness: Mapped[int] = mapped_column(Integer, default=0)
    pa_updated_at: Mapped[date | None] = mapped_column(Date, default=None)
    heat: Mapped[int] = mapped_column(Integer, default=0)
    heat_updated_at: Mapped[date | None] = mapped_column(Date, default=None)
    heat_stamped_tick: Mapped[int] = mapped_column(Integer, default=0)
    pa_stamped_tick: Mapped[int] = mapped_column(Integer, default=0)

    notes: Mapped[str | None] = mapped_column(Text, default=None)

    character: Mapped["Character"] = relationship("Character", back_populates="reputation")


class OrgStanding(Base):
    """How a specific character stands with a specific organization."""
    __tablename__ = "org_standings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    character_id: Mapped[int] = mapped_column(ForeignKey("characters.id"))
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))

    # -10 (openly hunted) to +10 (trusted ally)
    standing: Mapped[int] = mapped_column(Integer, default=0)
    standings_updated_at: Mapped[date | None] = mapped_column(Date, default=None)
    standings_stamped_tick: Mapped[int] = mapped_column(Integer, default=0)
    notes: Mapped[str | None] = mapped_column(Text, default=None)

    __table_args__ = (
        UniqueConstraint("character_id", "organization_id", name="uq_org_standing_char_org"),
    )

    character: Mapped["Character"] = relationship("Character", back_populates="org_standings")
    organization: Mapped["Organization"] = relationship("Organization", back_populates="org_standings")
