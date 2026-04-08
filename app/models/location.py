from typing import Optional
from sqlalchemy import String, Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.associations import log_locations


class Location(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), index=True)
    # bar, corp_facility, gang_turf, safehouse, district, government, shop, warehouse, matrix_node, other
    location_type: Mapped[str | None] = mapped_column(String(100), default=None)
    city: Mapped[str | None] = mapped_column(String(100), default=None)
    district: Mapped[str | None] = mapped_column(String(100), default=None)
    description: Mapped[str | None] = mapped_column(Text, default=None)
    # open, guarded, secure, ultraviolet
    security_level: Mapped[str | None] = mapped_column(String(50), default=None)
    notes: Mapped[str | None] = mapped_column(Text, default=None)

    controlling_org_id: Mapped[int | None] = mapped_column(ForeignKey("organizations.id"), default=None)

    controlling_org: Mapped[Optional["Organization"]] = relationship("Organization", back_populates="locations")
    contacts: Mapped[list["Contact"]] = relationship("Contact", back_populates="location")
    adventure_logs: Mapped[list["AdventureLog"]] = relationship(
        "AdventureLog", secondary=log_locations, back_populates="locations_involved"
    )
