from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field


class OrganizationBase(BaseModel):
    name: str = Field(max_length=200)
    org_type: Optional[str] = Field(default=None, max_length=100)
    tier: int = Field(default=1, ge=1, le=6)
    description: Optional[str] = None
    headquarters: Optional[str] = Field(default=None, max_length=200)
    leadership: list[dict[str, Any]] = []
    # Each entry is one of:
    #   telecom:     {type, number, description, visibility}
    #   matrix_host: {type, rtg, ltg, id_code, description, visibility, san_access_rating, notes?}
    ltgs: list[dict[str, Any]] = []
    ally_ids: list[int] = []
    enemy_ids: list[int] = []
    revealed_ally_ids: list[int] = []
    revealed_enemy_ids: list[int] = []
    is_active: bool = True
    notes: Optional[str] = None


OrganizationCreate = OrganizationBase


class OrganizationUpdate(BaseModel):
    name: Optional[str] = Field(default=None, max_length=200)
    org_type: Optional[str] = Field(default=None, max_length=100)
    tier: Optional[int] = Field(default=None, ge=1, le=6)
    description: Optional[str] = None
    headquarters: Optional[str] = Field(default=None, max_length=200)
    leadership: Optional[list[dict[str, Any]]] = None
    ltgs: Optional[list[dict[str, Any]]] = None
    ally_ids: Optional[list[int]] = None
    enemy_ids: Optional[list[int]] = None
    revealed_ally_ids: Optional[list[int]] = None
    revealed_enemy_ids: Optional[list[int]] = None
    is_active: Optional[bool] = None
    notes: Optional[str] = None


class OrganizationRead(OrganizationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class LtgSecurityUpdate(BaseModel):
    rtg: str
    ltg: str
    san_access_rating: str


class OrganizationSummary(BaseModel):
    id: int
    name: str
    org_type: Optional[str] = None
    tier: int
    is_active: bool
    model_config = ConfigDict(from_attributes=True)
