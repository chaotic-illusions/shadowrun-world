from typing import Any, Literal, Optional
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field
from app.schemas.character import CharacterSummary
from app.schemas.location import LocationSummary
from app.schemas.organization import OrganizationSummary

OUTCOME_VALUES = Literal["success", "partial_success", "failure", "critical_failure", "abandoned"]


class AdventureLogBase(BaseModel):
    title: str = Field(max_length=300)
    session_date: date
    run_number: Optional[int] = None
    objective: str
    result: str
    outcome: Optional[OUTCOME_VALUES] = None
    payout: Optional[str] = Field(default=None, max_length=300)
    casualties: Optional[str] = None
    outcome_tags: list[str] = []
    consequences_active: list[str] = []
    heat: int = Field(default=0, ge=0, le=10)
    tick_count: int = Field(default=1, ge=0)
    employer: Optional[str] = Field(default=None, max_length=200)
    gm_notes: Optional[str] = None
    changes_applied: list[dict[str, Any]] = []
    changes_excluded: list[dict[str, Any]] = []


class AdventureLogCreate(AdventureLogBase):
    participant_ids: list[int] = Field(default=[], max_length=50)
    location_ids: list[int] = Field(default=[], max_length=50)
    org_ids: list[int] = Field(default=[], max_length=50)


class AdventureLogUpdate(BaseModel):
    title: Optional[str] = None
    session_date: Optional[date] = None
    run_number: Optional[int] = None
    objective: Optional[str] = None
    result: Optional[str] = None
    outcome: Optional[str] = None
    payout: Optional[str] = None
    casualties: Optional[str] = None
    outcome_tags: Optional[list[str]] = None
    consequences_active: Optional[list[str]] = None
    heat: Optional[int] = None
    tick_count: Optional[int] = None
    employer: Optional[str] = None
    gm_notes: Optional[str] = None
    changes_applied: Optional[list[dict[str, Any]]] = None
    changes_excluded: Optional[list[dict[str, Any]]] = None
    participant_ids: Optional[list[int]] = None
    location_ids: Optional[list[int]] = None
    org_ids: Optional[list[int]] = None


class AdventureLogRead(AdventureLogBase):
    id: int
    consequences_suggested: list[dict[str, Any]]
    participants: list[CharacterSummary]
    locations_involved: list[LocationSummary]
    orgs_involved: list[OrganizationSummary]
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)


class AdventureLogSummary(BaseModel):
    id: int
    title: str
    session_date: date
    run_number: Optional[int] = None
    outcome: Optional[str] = None
    heat: int = 0
    employer: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
