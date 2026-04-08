from typing import Any, Literal, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

IC_LETHALITY = Literal["white", "gray", "black"]
OWNER_HINT = Literal["corp", "government", "criminal", "military", "unknown"]


class MatrixHostConfig(BaseModel):
    """Generation parameters stored in config_json."""
    complexity: int = Field(default=2, ge=1, le=5)
    base_rating: str = Field(default="Orange-6", max_length=50)
    ic_lethality: IC_LETHALITY = "gray"
    has_private_subnet: bool = False
    owner_hint: OWNER_HINT = "corp"
    seed: Optional[int] = None
    name: str = Field(default="Unnamed Host", max_length=200)
    owner_org_id: Optional[int] = None
    location_id: Optional[int] = None
    notes: Optional[str] = None


class MatrixHostCreate(BaseModel):
    name: str = Field(max_length=200)
    owner_org_id: Optional[int] = None
    location_id: Optional[int] = None
    config_json: Optional[dict[str, Any]] = None
    topology_json: Optional[dict[str, Any]] = None
    notes: Optional[str] = None


class MatrixHostUpdate(BaseModel):
    name: Optional[str] = Field(default=None, max_length=200)
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
