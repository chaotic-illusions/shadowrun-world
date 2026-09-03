from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class LocationBase(BaseModel):
    name: str = Field(max_length=200)
    location_type: Optional[str] = Field(default=None, max_length=100)
    city: Optional[str] = Field(default=None, max_length=100)
    district: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = None
    security_level: Optional[str] = Field(default=None, max_length=50)
    is_active: bool = True
    notes: Optional[str] = None
    controlling_org_id: Optional[int] = None
    source_adventure: Optional[str] = Field(default=None, max_length=100)


class LocationCreate(LocationBase):
    model_config = ConfigDict(extra="forbid")


class LocationUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: Optional[str] = Field(default=None, max_length=200)
    location_type: Optional[str] = Field(default=None, max_length=100)
    city: Optional[str] = Field(default=None, max_length=100)
    district: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = None
    security_level: Optional[str] = Field(default=None, max_length=50)
    is_active: Optional[bool] = None
    notes: Optional[str] = None
    controlling_org_id: Optional[int] = None
    source_adventure: Optional[str] = Field(default=None, max_length=100)


class LocationRead(LocationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class LocationSummary(BaseModel):
    id: int
    name: str
    location_type: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    is_active: bool
    model_config = ConfigDict(from_attributes=True)
