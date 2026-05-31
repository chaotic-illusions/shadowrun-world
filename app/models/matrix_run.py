from __future__ import annotations

from datetime import datetime, UTC
from sqlalchemy import Integer, String, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class MatrixRun(Base):
    __tablename__ = "matrix_runs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    host_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("matrix_hosts.id", ondelete="SET NULL"),
        nullable=True, index=True,
    )

    # SHA-256 of the user token that started this run. Mutations require admin or matching owner.
    owner_token_hash: Mapped[str | None] = mapped_column(String(64), index=True, default=None)

    # Decker character stats + utilities at run start
    decker_json: Mapped[dict] = mapped_column(JSON, default=dict)

    # Full mutable run state (tally, IC, condition monitors, event log)
    state_json: Mapped[dict] = mapped_column(JSON, default=dict)

    # active | escaped | crashed | shutdown
    status: Mapped[str] = mapped_column(String(20), default="active", nullable=False)

    # Optimistic-lock counter (declared as version_id_col below). SQLAlchemy adds
    # `WHERE version = :old` to every UPDATE and raises StaleDataError if a
    # concurrent writer already bumped it -- preventing lost updates to state_json.
    version: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )

    host: Mapped[MatrixHost | None] = relationship("MatrixHost", foreign_keys=[host_id])  # noqa: F821

    __mapper_args__ = {"version_id_col": version}
