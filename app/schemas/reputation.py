from typing import Optional
from datetime import date
from pydantic import BaseModel, ConfigDict


class ReputationBase(BaseModel):
    street_cred: int = 0
    notoriety: int = 0
    public_awareness: int = 0
    heat: int = 0
    pa_updated_at: Optional[date] = None
    notes: Optional[str] = None


class ReputationCreate(ReputationBase):
    character_id: int


class ReputationUpdate(BaseModel):
    street_cred: Optional[int] = None
    notoriety: Optional[int] = None
    public_awareness: Optional[int] = None
    heat: Optional[int] = None
    pa_updated_at: Optional[date] = None
    notes: Optional[str] = None


class ReputationRead(ReputationBase):
    id: int
    character_id: int
    model_config = ConfigDict(from_attributes=True)


class OrgStandingBase(BaseModel):
    character_id: int
    organization_id: int
    standing: int = 0
    notes: Optional[str] = None


class OrgStandingCreate(OrgStandingBase):
    pass


class OrgStandingUpdate(BaseModel):
    standing: Optional[int] = None
    notes: Optional[str] = None


class OrgStandingRead(OrgStandingBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
