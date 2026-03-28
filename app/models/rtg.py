from sqlalchemy import Column, Integer, String, Boolean, Text
from app.db.base import Base


class RTG(Base):
    __tablename__ = "rtgs"

    id = Column(Integer, primary_key=True, index=True)
    # e.g. "NA/UCAS-SEA"
    code = Column(String(50), nullable=False, unique=True, index=True)
    region = Column(String(200), nullable=False)
    political_entity = Column(String(200))
    continent = Column(String(100))
    # e.g. "Green-4", "Orange-5" — target number / successes to manipulate the node
    host_rating = Column(String(20))
    # True = from SR source material; False = campaign-created
    canonical = Column(Boolean, default=True)
    notes = Column(Text)
