from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.associations import log_characters


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    is_pc = Column(Boolean, nullable=False, default=True)
    archetype = Column(String(100))   # Street Samurai, Decker, Mage, Shaman, Rigger, Face, etc.
    race = Column(String(50), default="Human")  # Human, Elf, Dwarf, Ork, Troll
    gender = Column(String(50))
    age = Column(Integer)
    description = Column(Text)
    background = Column(Text)

    # SR2 core attributes stored as dict: body, quickness, strength, charisma, intelligence,
    # willpower, essence, magic (if awakened), reaction (derived), initiative_dice
    attributes = Column(JSON, default=dict)

    # List of {name, rating, specialization, category} dicts
    skills = Column(JSON, default=list)

    # List of {name, type, essence_cost, rating, notes} dicts
    augmentations = Column(JSON, default=list)

    # List of {name, category, rating, quantity, notes} dicts
    gear = Column(JSON, default=list)

    # Services/skills this NPC can provide as a contact (e.g. "Equipment Acquisition")
    contact_skills = Column(JSON, default=list)

    # NPC connection rating (1–6); not applicable to PCs
    connection = Column(Integer, default=1)

    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)

    karma_total = Column(Integer, default=0)
    karma_current = Column(Integer, default=0)
    nuyen = Column(Integer, default=0)

    is_active = Column(Boolean, default=True)
    notes = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    organization = relationship("Organization", foreign_keys=[organization_id])

    @property
    def organization_name(self):
        return self.organization.name if self.organization else None
    contacts = relationship("Contact", foreign_keys="Contact.owner_id", back_populates="owner", cascade="all, delete-orphan")
    reputation = relationship("Reputation", back_populates="character", uselist=False, cascade="all, delete-orphan")
    org_standings = relationship("OrgStanding", back_populates="character", cascade="all, delete-orphan")
    adventure_logs = relationship("AdventureLog", secondary=log_characters, back_populates="participants")
