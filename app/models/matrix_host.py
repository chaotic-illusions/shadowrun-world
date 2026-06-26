from __future__ import annotations

from datetime import datetime, UTC
from sqlalchemy import Boolean, String, Text, Integer, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class MatrixHost(Base):
    __tablename__ = "matrix_hosts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200))

    # Optional FK links
    owner_org_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("organizations.id", ondelete="SET NULL"), nullable=True
    )
    location_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("locations.id", ondelete="SET NULL"), nullable=True
    )

    # Generation parameters (complexity, base_rating, ic_lethality, etc.)
    config_json: Mapped[dict | None] = mapped_column(JSON, default=None)

    # Rendered topology (nodes list, edges list, subnets list)
    topology_json: Mapped[dict | None] = mapped_column(JSON, default=None)

    notes: Mapped[str | None] = mapped_column(Text, default=None)
    is_visible_to_players: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    # SR universe linkage
    ltg_address: Mapped[str | None] = mapped_column(String(100), default=None)

    # Optional host identifier code (e.g. "ID001"); parallels the org LTG entry id_code.
    id_code: Mapped[str | None] = mapped_column(String(20), default=None)

    # Whether this host can be chosen as a trap-door destination from another host. A host may be
    # matrix-accessible (has ltg_address), a trap-door destination, or both; an off-grid host (no
    # LTG) is reachable only by following another host's trap door.
    is_trap_door_dest: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    # Trap doors to other hosts (list of dicts)
    trap_doors_json: Mapped[list | None] = mapped_column(JSON, default=None)

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )

    owner_org: Mapped[Organization | None] = relationship(
        "Organization", foreign_keys=[owner_org_id]
    )
    location: Mapped[Location | None] = relationship(
        "Location", foreign_keys=[location_id]
    )

    @property
    def san_rating(self) -> str | None:
        """System access rating ("Color-Value", e.g. "Orange-5") derived from config_json,
        exposed on list summaries so the host registry can color a host's rating without
        loading its full config. Mirrors the org catalog's san_access_rating."""
        cfg = self.config_json or {}
        code = cfg.get("security_code")
        val = cfg.get("security_value")
        if code and val is not None:
            return f"{code}-{val}"
        return str(code) if code else None
