from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.associations import log_locations


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    # bar, corp_facility, gang_turf, safehouse, district, government, shop, warehouse, matrix_node, other
    location_type = Column(String(100))
    city = Column(String(100))
    district = Column(String(100))
    description = Column(Text)
    # open, guarded, secure, ultraviolet
    security_level = Column(String(50))
    notes = Column(Text)

    controlling_org_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)

    controlling_org = relationship("Organization", back_populates="locations")
    contacts = relationship("Contact", back_populates="location")
    adventure_logs = relationship("AdventureLog", secondary=log_locations, back_populates="locations_involved")
