from typing import Any, Optional
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict
from app.schemas.character import CharacterSummary
from app.schemas.location import LocationSummary
from app.schemas.organization import OrganizationSummary


class AdventureLogBase(BaseModel):
    title: str
    session_date: date
    run_number: Optional[int] = None
    objective: str
    result: str
    outcome: Optional[str] = None  # success, partial_success, failure, critical_failure, abandoned
    payout: Optional[str] = None
    casualties: Optional[str] = None
    outcome_tags: list[str] = []
    consequences_active: list[str] = []
    gm_notes: Optional[str] = None


class AdventureLogCreate(AdventureLogBase):
    participant_ids: list[int] = []
    location_ids: list[int] = []
    org_ids: list[int] = []


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
    gm_notes: Optional[str] = None
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
    model_config = ConfigDict(from_attributes=True)
