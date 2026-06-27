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


class MemoryProgram(BaseModel):
    """A program the decker carries that Swap Memory can move between storage and active
    memory mid-run. size is its active-memory footprint in Mp."""
    name:   str = Field("", max_length=40)   # utility key, e.g. "analyze", "read_write"
    rating: int = Field(0, ge=0, le=50)
    size:   int = Field(0, ge=0)


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
    bandwidth_modifier: int = Field(0, ge=-6, le=6)  # legacy frozen BW Trace mod (fallback only)
    base_bandwidth:    int = Field(0, ge=0, le=200)  # jackpoint base BW (Mp); 0 = console/unlimited
    # Jackpoint Access side (vr2 Jackpoint table): Legal -2 / Illegal 0 / Satellite +2 /
    # Workstation -4 / Remote +4. Console halves Access Rating & Security Value.
    access_modifier:   int = Field(0, ge=-6, le=6)
    console_access:    bool = False
    # Satellite uplink (SATLINK): -2 Reaction (slower initiative) but the decker's physical
    # location cannot be physically traced. reaction_modifier feeds _decker_reaction;
    # physical_trace_immune is checked by the Trace IC report branch.
    reaction_modifier:     int = Field(0, ge=-6, le=6)
    physical_trace_immune: bool = False
    # Free deck storage (Mp) for downloaded paydata. -1 = untracked/unlimited (legacy default);
    # 0 = a real cap that is full (blocks all downloads); >0 = that many free Mp.
    storage_free_mp:       int = Field(-1, ge=-1)
    persona_mode:      Literal["none", "bod", "evasion", "masking", "sensor"] = "none"
    linked_passcode:   bool = False   # stolen linked passcode: -2 TN to Logon w/ Deception (vr2)
    utilities:         DeckerUtilities = Field(default_factory=DeckerUtilities)
    # Programs sitting in storage memory (NOT active at logon). Swap Memory can load one of
    # these into active memory mid-run (and push an active program back to storage).
    storage_programs:  list[MemoryProgram] = Field(default_factory=list)
    # util key -> active-memory size (Mp) for every program carried (active + storage), so the
    # engine can enforce the active-memory cap when swapping a program in.
    program_sizes:     dict[str, int] = Field(default_factory=dict)


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
    "swap_memory", "purge_hog",
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
    target_program: str = Field("", max_length=40)  # Swap Memory / Purge Hog: utility key (blank = first relevant)
    swap_out_program: str = Field("", max_length=40)  # Swap Memory: active program to push to storage to free memory


class RunAttackInput(BaseModel):
    target_ic_id: str = Field(..., max_length=64)
    attack_pool: int = Field(..., ge=1, le=40)
    hacking_pool_dice: int = Field(0, ge=0, le=40)
    armor_utility: int = Field(0, ge=0, le=50)
    penetration: bool = Field(False)  # defeats Shield; extra-effective vs Shift
    chaser: bool = Field(False)       # defeats Shift; extra-effective vs Shield


class RunLogoffInput(BaseModel):
    hacking_pool_dice: int = Field(0, ge=0, le=40)
    deception_utility: int = Field(0, ge=0, le=50)


class RunTrapDoorInput(BaseModel):
    # "enter": graceful logoff through the concealing subsystem, then arrive on the destination
    # host (a fresh linked run; destination revealed only on arrival).
    # "file":  record the door for intel -- reveals only whether the destination has LTG access.
    action: Literal["enter", "file"]
    hacking_pool_dice: int = Field(0, ge=0, le=40)   # enter only: dice for the logoff Access Test
    deception_utility: int = Field(0, ge=0, le=50)   # enter only: Deception utility for the logoff


class RunReactiveInput(BaseModel):
    ic_id: str = Field(..., max_length=64)
    utility_name: str = Field(..., max_length=80)
    utility_rating: int = Field(..., ge=1, le=50)


class RunSuppressInput(BaseModel):
    ic_id: str = Field(..., max_length=64)
    release: bool = Field(False)  # False = suppress (DF -1); True = release (restore DF, +tally)


class RunEnemyDeckerInput(BaseModel):
    name: str = Field("", max_length=80)
    intent: Literal["", "boot", "dump", "kill"] = ""  # blank = use the tier default


class RunEnemyActInput(BaseModel):
    enemy_id: str = Field(..., max_length=64)
    program: str = Field("", max_length=32)  # force a program (Attack/Hog/Poison/Restrict/Reveal/Black Hammer/Killjoy); blank = intent default


class RunEnemyAttackInput(BaseModel):
    enemy_id: str = Field(..., max_length=64)
    attack_pool: int = Field(..., ge=1, le=40)
    hacking_pool_dice: int = Field(0, ge=0, le=40)


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
