from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class MatrixHostCreate(BaseModel):
    name: str = Field(max_length=200)
    owner_org_id: Optional[int] = None
    location_id: Optional[int] = None
    config_json: Optional[dict[str, Any]] = None
    topology_json: Optional[dict[str, Any]] = None
    notes: Optional[str] = None
    ltg_address: Optional[str] = Field(default=None, max_length=100)
    trap_doors_json: Optional[list[dict[str, Any]]] = None


class MatrixHostUpdate(BaseModel):
    name: Optional[str] = Field(default=None, max_length=200)
    owner_org_id: Optional[int] = None
    location_id: Optional[int] = None
    config_json: Optional[dict[str, Any]] = None
    topology_json: Optional[dict[str, Any]] = None
    notes: Optional[str] = None
    is_visible_to_players: Optional[bool] = None
    ltg_address: Optional[str] = Field(default=None, max_length=100)
    trap_doors_json: Optional[list[dict[str, Any]]] = None


class MatrixHostRead(BaseModel):
    id: int
    name: str
    owner_org_id: Optional[int] = None
    location_id: Optional[int] = None
    config_json: Optional[dict[str, Any]] = None
    topology_json: Optional[dict[str, Any]] = None
    notes: Optional[str] = None
    is_visible_to_players: bool = False
    ltg_address: Optional[str] = None
    trap_doors_json: Optional[list[dict[str, Any]]] = None
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)


class MatrixHostSummary(BaseModel):
    id: int
    name: str
    owner_org_id: Optional[int] = None
    location_id: Optional[int] = None
    is_visible_to_players: bool = False
    ltg_address: Optional[str] = None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
