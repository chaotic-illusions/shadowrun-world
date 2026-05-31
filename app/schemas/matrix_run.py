from __future__ import annotations

from datetime import datetime
from typing import Any, Literal
from pydantic import BaseModel, Field


# -- Decker input ---------------------------------------------------------------

class DeckerUtilities(BaseModel):
    # Stealth / detection
    sleaze:     int = Field(0, ge=0)
    camo:       int = Field(0, ge=0)
    # Operations
    deception:  int = Field(0, ge=0)
    browse:     int = Field(0, ge=0)
    analyze:    int = Field(0, ge=0)
    evaluate:   int = Field(0, ge=0)
    decrypt:    int = Field(0, ge=0)
    crash:      int = Field(0, ge=0)
    mirrors:    int = Field(0, ge=0)
    validate_pgm: int = Field(0, ge=0)
    read_write: int = Field(0, ge=0)
    spoof:      int = Field(0, ge=0)
    relocate:   int = Field(0, ge=0)
    # Combat / defense
    attack:     int = Field(0, ge=0)
    armor:      int = Field(0, ge=0)
    shield:     int = Field(0, ge=0)
    restore:    int = Field(0, ge=0)
    medic:      int = Field(0, ge=0)
    cloak:      int = Field(0, ge=0)
    lock_on:    int = Field(0, ge=0)


class DeckerStats(BaseModel):
    name: str = "Ghost"
    # Deck persona programs
    mpcp:              int = Field(..., ge=1, le=50)
    bod:               int = Field(..., ge=1, le=50)
    evasion:           int = Field(..., ge=1, le=50)
    masking:           int = Field(..., ge=1, le=50)
    sensor:            int = Field(..., ge=1, le=50)
    # Character attributes
    computer_skill:    int = Field(..., ge=1, le=50)
    intelligence:      int = Field(..., ge=1, le=50)
    quickness:         int = Field(4, ge=1, le=12)   # Reaction = ceil((Q+I)/2)
    willpower:         int = Field(4, ge=1, le=50)
    body:              int = Field(4, ge=1, le=12)    # physical body for dump shock
    # Hardware options
    deck_mode:         Literal["hot", "cool", "tortoise"] = "hot"
    iccm:              bool = False
    hardening:         int = Field(0, ge=0)
    response_increase: int = Field(0, ge=0, le=3)
    active_memory:     int = Field(0, ge=0)          # Mp; limits loaded utilities
    io_speed:          int = Field(0, ge=0)          # Mp/ct; feeds bandwidth modifier
    # Trace Factor components (fixed inputs; Evasion and Camo are dynamic)
    trace_factor:      int = Field(0, ge=-6, le=6)   # jackpoint modifier
    bandwidth_modifier: int = Field(0, ge=-6, le=6)  # I/O speed relative to icon BW
    utilities:         DeckerUtilities = Field(default_factory=DeckerUtilities)


# -- Run creation ---------------------------------------------------------------

class MatrixRunCreate(BaseModel):
    host_id: int
    decker: DeckerStats


# -- Action input --------------------------------------------------------------

ActionType = Literal[
    "logon_to_host", "logon_to_ltg",
    "analyze_host", "analyze_ic", "analyze_security", "analyze_subsystem",
    "locate_file", "locate_paydata", "locate_ic", "locate_slave",
    "download_data", "edit_file", "upload_data",
    "control_slave", "monitor_slave", "edit_slave",
    "null_operation", "graceful_logoff", "crash_host",
    "validate_passcode", "invalidate_passcode", "decoy",
    "redirect_datatrail", "relocate", "decrypt_file",
]

SubsystemType = Literal["access", "control", "index", "files", "slave"]


class RunActionInput(BaseModel):
    action_type: ActionType
    subsystem: SubsystemType
    utility_rating: int = Field(0, ge=0, le=50)
    hacking_pool_dice: int = Field(0, ge=0, le=40)
    extra_tn_modifier: int = Field(0, ge=-6, le=6)
    note: str = Field("", max_length=500)
    target_ic_id: str = Field("", max_length=64)  # Analyze IC: which IC to reveal (blank = first unknown)
    target_file: str = Field("", max_length=160)   # Decrypt File: scramble target_key / paydata name (blank = first scramble)


class RunAttackInput(BaseModel):
    target_ic_id: str = Field(..., max_length=64)
    attack_pool: int = Field(..., ge=1, le=40)
    hacking_pool_dice: int = Field(0, ge=0, le=40)
    armor_utility: int = Field(0, ge=0, le=50)


class RunLogoffInput(BaseModel):
    hacking_pool_dice: int = Field(0, ge=0, le=40)
    deception_utility: int = Field(0, ge=0, le=50)


class RunReactiveInput(BaseModel):
    ic_id: str = Field(..., max_length=64)
    utility_name: str = Field(..., max_length=80)
    utility_rating: int = Field(..., ge=1, le=50)


class RunSuppressInput(BaseModel):
    ic_id: str = Field(..., max_length=64)
    release: bool = Field(False)  # False = suppress (DF -1); True = release (restore DF, +tally)


# -- Sheaf + Host designer -----------------------------------------------------

class SheafEvent(BaseModel):
    type: str  # ic, passive_alert, active_alert, shutdown, trap_ic, construct, party_ic
    # Normal IC
    ic_type: str | None = None
    rating: int | None = None
    # Trap IC
    surface_ic_type: str | None = None
    surface_ic_rating: int | None = None
    hidden_ic_type: str | None = None
    hidden_ic_rating: int | None = None
    # Construct / Party IC
    threat_rating: int | None = None
    components: list[dict] | None = None
    defenses: list[str] | None = None


class SheafStep(BaseModel):
    trigger: int
    events: list[SheafEvent]


class SheaveSaveInput(BaseModel):
    sheaf: list[SheafStep]
    security_code: str
    security_value: int
    acifs: list[int] = Field(default_factory=list)  # [A, C, I, F, S]
    owner_type: str = "corp"


class SheafGenerateInput(BaseModel):
    security_code: str
    security_value: int
    owner_type: str = "corp"
    step_count: int | None = None
    seed: int | None = None


# -- Read schemas --------------------------------------------------------------

class MatrixRunSummary(BaseModel):
    id: int
    host_id: int | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class MatrixRunRead(BaseModel):
    id: int
    host_id: int | None
    decker_json: dict[str, Any]
    state_json: dict[str, Any]
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
