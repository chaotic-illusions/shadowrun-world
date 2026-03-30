from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base


class Reputation(Base):
    """SR2 reputation tracks for a player character."""
    __tablename__ = "reputations"

    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False, unique=True)

    street_cred = Column(Integer, default=0)       # Positive rep in the shadows
    notoriety = Column(Integer, default=0)         # Negative rep / infamy
    public_awareness = Column(Integer, default=0)  # How well-known to the public
    pa_updated_at = Column(Date, nullable=True)    # When PA was last changed (for decay)

    notes = Column(Text)

    character = relationship("Character", back_populates="reputation")


class OrgStanding(Base):
    """How a specific character stands with a specific organization."""
    __tablename__ = "org_standings"

    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)

    # -10 (openly hunted) to +10 (trusted ally)
    standing = Column(Integer, default=0)
    notes = Column(Text)

    __table_args__ = (
        UniqueConstraint("character_id", "organization_id", name="uq_org_standing_char_org"),
    )

    character = relationship("Character", back_populates="org_standings")
    organization = relationship("Organization", back_populates="org_standings")
