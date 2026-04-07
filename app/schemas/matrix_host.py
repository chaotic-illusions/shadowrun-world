from typing import Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MatrixHostConfig(BaseModel):
    """Generation parameters stored in config_json."""
    complexity: int = 2          # 1–5
    base_rating: str = "Orange-6"  # e.g. "Green-4", "Orange-6", "Red-8", "Black-12"
    ic_lethality: str = "gray"   # "white", "gray", "black"
    has_private_subnet: bool = False
    owner_hint: str = "corp"     # "corp", "government", "criminal", "military", "unknown"
    seed: Optional[int] = None
    name: str = "Unnamed Host"
    owner_org_id: Optional[int] = None
    location_id: Optional[int] = None
    notes: Optional[str] = None


class MatrixHostCreate(BaseModel):
    name: str
    owner_org_id: Optional[int] = None
    location_id: Optional[int] = None
    config_json: Optional[dict[str, Any]] = None
    topology_json: Optional[dict[str, Any]] = None
    notes: Optional[str] = None


class MatrixHostUpdate(BaseModel):
    name: Optional[str] = None
    owner_org_id: Optional[int] = None
    location_id: Optional[int] = None
    config_json: Optional[dict[str, Any]] = None
    topology_json: Optional[dict[str, Any]] = None
    notes: Optional[str] = None
    is_visible_to_players: Optional[bool] = None


class MatrixHostRead(BaseModel):
    id: int
    name: str
    owner_org_id: Optional[int] = None
    location_id: Optional[int] = None
    config_json: Optional[dict[str, Any]] = None
    topology_json: Optional[dict[str, Any]] = None
    notes: Optional[str] = None
    is_visible_to_players: bool = False
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)


class MatrixHostSummary(BaseModel):
    id: int
    name: str
    owner_org_id: Optional[int] = None
    location_id: Optional[int] = None
    is_visible_to_players: bool = False
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
