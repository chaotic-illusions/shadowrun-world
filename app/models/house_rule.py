from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from app.db.base import Base


class HouseRule(Base):
    __tablename__ = "house_rules"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300), nullable=False)
    # combat, magic, decking, rigging, skills, character_creation, gear, vehicles, other
    category = Column(String(100))
    source_reference = Column(String(200))  # e.g. "SR2 Core p.142"
    original_rule = Column(Text)
    modification = Column(Text, nullable=False)
    reason = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
