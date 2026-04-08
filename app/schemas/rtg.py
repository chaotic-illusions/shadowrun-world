from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class RTGBase(BaseModel):
    code: str = Field(max_length=50)
    region: str = Field(max_length=200)
    political_entity: Optional[str] = Field(default=None, max_length=200)
    continent: Optional[str] = Field(default=None, max_length=100)
    rtg_security_rating: Optional[str] = Field(default=None, max_length=20)
    canonical: bool = True
    notes: Optional[str] = None


RTGCreate = RTGBase


class RTGUpdate(BaseModel):
    code: Optional[str] = Field(default=None, max_length=50)
    region: Optional[str] = Field(default=None, max_length=200)
    political_entity: Optional[str] = Field(default=None, max_length=200)
    continent: Optional[str] = Field(default=None, max_length=100)
    rtg_security_rating: Optional[str] = Field(default=None, max_length=20)
    canonical: Optional[bool] = None
    notes: Optional[str] = None


class RTGRead(RTGBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
