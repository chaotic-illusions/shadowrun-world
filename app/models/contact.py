from sqlalchemy import Column, Integer, String, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    profession = Column(String(100))
    race = Column(String(50))
    loyalty = Column(Integer, default=1)      # 1–6 per SR2 rules
    connection = Column(Integer, default=1)   # 1–6 per SR2 rules
    description = Column(Text)
    notes = Column(Text)

    # The PC who has this contact
    owner_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    # If this contact is a fully fleshed NPC, link to their character entry
    npc_id = Column(Integer, ForeignKey("characters.id"), nullable=True)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)

    __table_args__ = (
        CheckConstraint("loyalty >= 1 AND loyalty <= 6", name="ck_contact_loyalty"),
        CheckConstraint("connection >= 1 AND connection <= 6", name="ck_contact_connection"),
    )

    owner = relationship("Character", foreign_keys=[owner_id], back_populates="contacts")
    npc = relationship("Character", foreign_keys=[npc_id])
    location = relationship("Location", back_populates="contacts")
    organization = relationship("Organization", back_populates="contacts")
