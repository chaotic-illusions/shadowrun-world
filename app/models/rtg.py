from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class RTG(Base):
    __tablename__ = "rtgs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # e.g. "NA/UCAS-SEA"
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    region: Mapped[str] = mapped_column(String(200))
    political_entity: Mapped[str | None] = mapped_column(String(200), default=None)
    continent: Mapped[str | None] = mapped_column(String(100), default=None)
    # e.g. "Green-4", "Orange-5"
    rtg_security_rating: Mapped[str | None] = mapped_column(String(20), default=None)
    # True = from SR source material; False = campaign-created
    canonical: Mapped[bool] = mapped_column(default=True)
    notes: Mapped[str | None] = mapped_column(Text, default=None)
