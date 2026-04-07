from sqlalchemy import String, Text, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.associations import log_organizations


class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), index=True)
    # megacorp, gang, government, fixer_network, cult, syndicate, other
    org_type: Mapped[str | None] = mapped_column(String(100), default=None)
    # 1=street level, 5=AAA megacorp / major power
    tier: Mapped[int] = mapped_column(Integer, default=1)
    description: Mapped[str | None] = mapped_column(Text, default=None)
    headquarters: Mapped[str | None] = mapped_column(String(200), default=None)

    # List of {name, title, character_id (nullable), notes} dicts
    leadership: Mapped[list] = mapped_column(JSON, default=list)

    # List of {type, visibility, ...} dicts
    ltgs: Mapped[list] = mapped_column(JSON, default=list)

    # Lists of organization IDs (int); no FK constraint for flexibility
    ally_ids: Mapped[list] = mapped_column(JSON, default=list)
    enemy_ids: Mapped[list] = mapped_column(JSON, default=list)
    # Subsets of ally_ids/enemy_ids revealed to players
    revealed_ally_ids: Mapped[list] = mapped_column(JSON, default=list)
    revealed_enemy_ids: Mapped[list] = mapped_column(JSON, default=list)

    is_active: Mapped[bool] = mapped_column(default=True)
    notes: Mapped[str | None] = mapped_column(Text, default=None)

    locations: Mapped[list["Location"]] = relationship("Location", back_populates="controlling_org")
    contacts: Mapped[list["Contact"]] = relationship("Contact", back_populates="organization")
    org_standings: Mapped[list["OrgStanding"]] = relationship(
        "OrgStanding", back_populates="organization", cascade="all, delete-orphan"
    )
    adventure_logs: Mapped[list["AdventureLog"]] = relationship(
        "AdventureLog", secondary=log_organizations, back_populates="orgs_involved"
    )
