from typing import Any, Optional
from pydantic import BaseModel, ConfigDict


class OrganizationBase(BaseModel):
    name: str
    org_type: Optional[str] = None
    tier: int = 1
    description: Optional[str] = None
    headquarters: Optional[str] = None
    leadership: list[dict[str, Any]] = []
    ally_ids: list[int] = []
    enemy_ids: list[int] = []
    is_active: bool = True
    notes: Optional[str] = None


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    org_type: Optional[str] = None
    tier: Optional[int] = None
    description: Optional[str] = None
    headquarters: Optional[str] = None
    leadership: Optional[list[dict[str, Any]]] = None
    ally_ids: Optional[list[int]] = None
    enemy_ids: Optional[list[int]] = None
    is_active: Optional[bool] = None
    notes: Optional[str] = None


class OrganizationRead(OrganizationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class OrganizationSummary(BaseModel):
    id: int
    name: str
    org_type: Optional[str] = None
    tier: int
    is_active: bool
    model_config = ConfigDict(from_attributes=True)
