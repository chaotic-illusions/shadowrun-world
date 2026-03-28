from typing import Optional
from pydantic import BaseModel, ConfigDict


class RTGBase(BaseModel):
    code: str
    region: str
    political_entity: Optional[str] = None
    continent: Optional[str] = None
    host_rating: Optional[str] = None
    canonical: bool = True
    notes: Optional[str] = None


class RTGCreate(RTGBase):
    pass


class RTGUpdate(BaseModel):
    code: Optional[str] = None
    region: Optional[str] = None
    political_entity: Optional[str] = None
    continent: Optional[str] = None
    host_rating: Optional[str] = None
    canonical: Optional[bool] = None
    notes: Optional[str] = None


class RTGRead(RTGBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
