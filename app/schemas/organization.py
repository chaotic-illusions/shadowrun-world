from typing import Any, Literal, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator


class OrganizationDivision(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    id: str
    name: str = Field(min_length=1, max_length=200)
    kind: Literal["division", "subsidiary", "department", "unit", "branch"]
    tier: int = Field(default=1, ge=1, le=6)
    description: Optional[str] = None
    notes: Optional[str] = None
    source_adventure: Optional[str] = Field(default=None, max_length=100)
    leadership: list[dict[str, Any]] = Field(default_factory=list)
    ltgs: list[dict[str, Any]] = Field(default_factory=list)
    ally_ids: list[int] = Field(default_factory=list)
    enemy_ids: list[int] = Field(default_factory=list)
    revealed_ally_ids: list[int] = Field(default_factory=list)
    revealed_enemy_ids: list[int] = Field(default_factory=list)
    visibility: Literal["listed", "unlisted", "black"] = "unlisted"
    revealed: bool = False

    @field_validator("id")
    @classmethod
    def validate_id(cls, value: str) -> str:
        try:
            canonical = str(UUID(value))
        except ValueError as exc:
            raise ValueError("division id must be a UUID") from exc
        if value != canonical:
            raise ValueError("division id must use canonical lowercase UUID format")
        return value


def _validate_unique_division_ids(
    divisions: list[OrganizationDivision] | None,
) -> list[OrganizationDivision] | None:
    if divisions is None:
        return None
    ids = [division.id for division in divisions]
    if len(ids) != len(set(ids)):
        raise ValueError("division ids must be unique within an organization")
    return divisions


class OrganizationBase(BaseModel):
    name: str = Field(max_length=200)
    org_type: Optional[str] = Field(default=None, max_length=100)
    # "Gang" or "Tribe" -> runners can be affiliated with this org (linking spawns a contact of this
    # type). None -> not a gang/tribe, so the runner-affiliation link is hidden.
    affiliation_contact_type: Optional[Literal["Gang", "Tribe"]] = None
    tier: int = Field(default=1, ge=1, le=6)
    description: Optional[str] = None
    headquarters: Optional[str] = Field(default=None, max_length=200)
    leadership: list[dict[str, Any]] = []
    divisions: list[OrganizationDivision] = Field(default_factory=list, max_length=100)
    # Each entry is one of:
    #   telecom:     {type, number, description, visibility}
    #   matrix_host: {type, rtg, ltg, id_code, description, visibility, san_access_rating, san_revealed?, notes?}
    # san_access_rating is a decker secret redacted from non-admin GETs until san_revealed is
    # set (flipped when a decker discovers the host's security in a run; see host_visibility).
    ltgs: list[dict[str, Any]] = []
    ally_ids: list[int] = []
    enemy_ids: list[int] = []
    revealed_ally_ids: list[int] = []
    revealed_enemy_ids: list[int] = []
    catalog_scope: Literal["core", "reference", "adventure"] = "reference"
    is_active: bool = True
    notes: Optional[str] = None
    source_adventure: Optional[str] = Field(default=None, max_length=100)

    @field_validator("divisions")
    @classmethod
    def validate_divisions(cls, value: list[OrganizationDivision]) -> list[OrganizationDivision]:
        return _validate_unique_division_ids(value) or []


class OrganizationCreate(OrganizationBase):
    model_config = ConfigDict(extra="forbid")


class OrganizationUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: Optional[str] = Field(default=None, max_length=200)
    org_type: Optional[str] = Field(default=None, max_length=100)
    affiliation_contact_type: Optional[Literal["Gang", "Tribe"]] = None
    tier: Optional[int] = Field(default=None, ge=1, le=6)
    description: Optional[str] = None
    headquarters: Optional[str] = Field(default=None, max_length=200)
    leadership: Optional[list[dict[str, Any]]] = None
    divisions: Optional[list[OrganizationDivision]] = Field(default=None, max_length=100)
    ltgs: Optional[list[dict[str, Any]]] = None
    ally_ids: Optional[list[int]] = None
    enemy_ids: Optional[list[int]] = None
    revealed_ally_ids: Optional[list[int]] = None
    revealed_enemy_ids: Optional[list[int]] = None
    catalog_scope: Optional[Literal["core", "reference", "adventure"]] = None
    is_active: Optional[bool] = None
    notes: Optional[str] = None
    source_adventure: Optional[str] = Field(default=None, max_length=100)

    @field_validator("divisions")
    @classmethod
    def validate_divisions(
        cls, value: list[OrganizationDivision] | None
    ) -> list[OrganizationDivision] | None:
        return _validate_unique_division_ids(value)


class OrganizationRead(OrganizationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class LtgSecurityUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    rtg: str
    ltg: str
    san_access_rating: str


class AffiliateRunnerRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    character_id: int


class OrganizationSummary(BaseModel):
    id: int
    name: str
    org_type: Optional[str] = None
    affiliation_contact_type: Optional[str] = None
    tier: int
    catalog_scope: Literal["core", "reference", "adventure"]
    is_active: bool
    model_config = ConfigDict(from_attributes=True)
