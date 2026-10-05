from pydantic import BaseModel, ConfigDict, Field


class ClockRead(BaseModel):
    """Current campaign clock state (absolute tick total; 1 tick = 1 day)."""
    current_tick: int


class AdvanceClockRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    days: int = Field(ge=1, le=3650)


class AdvanceClockResult(BaseModel):
    current_tick: int
    days_advanced: int


class TeamKarma(BaseModel):
    """The team's Karma Pool (SR2 p.191)."""
    model_config = ConfigDict(extra="forbid")
    team_karma: int = Field(ge=0, le=999)
