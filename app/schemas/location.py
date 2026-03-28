from typing import Optional
from pydantic import BaseModel, ConfigDict


class LocationBase(BaseModel):
    name: str
    location_type: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    description: Optional[str] = None
    security_level: Optional[str] = None
    notes: Optional[str] = None
    controlling_org_id: Optional[int] = None


class LocationCreate(LocationBase):
    pass


class LocationUpdate(BaseModel):
    name: Optional[str] = None
    location_type: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    description: Optional[str] = None
    security_level: Optional[str] = None
    notes: Optional[str] = None
    controlling_org_id: Optional[int] = None


class LocationRead(LocationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class LocationSummary(BaseModel):
    id: int
    name: str
    location_type: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
