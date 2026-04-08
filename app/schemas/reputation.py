from typing import Optional
from datetime import date
from pydantic import BaseModel, ConfigDict, Field


class ReputationBase(BaseModel):
    street_cred: int = Field(default=0, ge=0)
    notoriety: int = Field(default=0, ge=0)
    public_awareness: int = Field(default=0, ge=0)
    heat: int = Field(default=0, ge=0, le=10)
    pa_updated_at: Optional[date] = None
    heat_updated_at: Optional[date] = None
    pa_stamped_tick: int = Field(default=0, ge=0)
    heat_stamped_tick: int = Field(default=0, ge=0)
    notes: Optional[str] = None


class ReputationCreate(ReputationBase):
    character_id: int


class ReputationUpdate(BaseModel):
    street_cred: Optional[int] = Field(default=None, ge=0)
    notoriety: Optional[int] = Field(default=None, ge=0)
    public_awareness: Optional[int] = Field(default=None, ge=0)
    heat: Optional[int] = Field(default=None, ge=0, le=10)
    pa_updated_at: Optional[date] = None
    heat_updated_at: Optional[date] = None
    pa_stamped_tick: Optional[int] = Field(default=None, ge=0)
    heat_stamped_tick: Optional[int] = Field(default=None, ge=0)
    notes: Optional[str] = None


class ReputationRead(ReputationBase):
    id: int
    character_id: int
    model_config = ConfigDict(from_attributes=True)


class OrgStandingBase(BaseModel):
    character_id: int
    organization_id: int
    standing: int = 0
    standings_updated_at: Optional[date] = None
    standings_stamped_tick: int = 0
    notes: Optional[str] = None


class OrgStandingCreate(OrgStandingBase):
    pass


class OrgStandingUpdate(BaseModel):
    standing: Optional[int] = None
    standings_updated_at: Optional[date] = None
    standings_stamped_tick: Optional[int] = None
    notes: Optional[str] = None


class OrgStandingRead(OrgStandingBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
