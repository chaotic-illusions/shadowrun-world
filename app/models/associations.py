"""
All M2M association tables live here to avoid circular imports.
These are plain Table objects — no mapped classes.
"""
from sqlalchemy import Column, Integer, ForeignKey, Table
from app.db.base import Base

log_characters = Table(
    "log_characters",
    Base.metadata,
    Column("log_id", Integer, ForeignKey("adventure_logs.id", ondelete="CASCADE"), primary_key=True),
    Column("character_id", Integer, ForeignKey("characters.id", ondelete="CASCADE"), primary_key=True),
)

log_locations = Table(
    "log_locations",
    Base.metadata,
    Column("log_id", Integer, ForeignKey("adventure_logs.id", ondelete="CASCADE"), primary_key=True),
    Column("location_id", Integer, ForeignKey("locations.id", ondelete="CASCADE"), primary_key=True),
)

log_organizations = Table(
    "log_organizations",
    Base.metadata,
    Column("log_id", Integer, ForeignKey("adventure_logs.id", ondelete="CASCADE"), primary_key=True),
    Column("organization_id", Integer, ForeignKey("organizations.id", ondelete="CASCADE"), primary_key=True),
)
