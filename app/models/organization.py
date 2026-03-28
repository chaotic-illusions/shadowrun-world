from sqlalchemy import Column, Integer, String, Text, Boolean, JSON
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.associations import log_organizations


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    # megacorp, gang, government, fixer_network, cult, syndicate, other
    org_type = Column(String(100))
    # 1=street level, 5=AAA megacorp / major power
    tier = Column(Integer, default=1)
    description = Column(Text)
    headquarters = Column(String(200))

    # List of {name, title, character_id (nullable), notes} dicts
    leadership = Column(JSON, default=list)

    # Lists of organization IDs (int); no FK constraint for flexibility
    ally_ids = Column(JSON, default=list)
    enemy_ids = Column(JSON, default=list)

    is_active = Column(Boolean, default=True)
    notes = Column(Text)

    locations = relationship("Location", back_populates="controlling_org")
    contacts = relationship("Contact", back_populates="organization")
    org_standings = relationship("OrgStanding", back_populates="organization", cascade="all, delete-orphan")
    adventure_logs = relationship("AdventureLog", secondary=log_organizations, back_populates="orgs_involved")
