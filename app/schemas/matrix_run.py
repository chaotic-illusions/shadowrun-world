from __future__ import annotations

from datetime import datetime
from typing import Any, Literal
from pydantic import BaseModel, Field


# -- Decker input ---------------------------------------------------------------

class DeckerUtilities(BaseModel):
    # Stealth / detection
    sleaze:     int = Field(0, ge=0)
    camo:       int = Field(0, ge=0)
    scanner:    int = Field(0, ge=0)   # Locate Decker: Sensor-aided search for hostile deckers
    # Operations
    deception:  int = Field(0, ge=0)
    analyze:    int = Field(0, ge=0)
    evaluate:   int = Field(0, ge=0)
    decrypt:    int = Field(0, ge=0)
    defuse:     int = Field(0, ge=0)   # reduces the TN to defuse data bombs (Files/Slave rating - Defuse)
    crash:      int = Field(0, ge=0)
    mirrors:    int = Field(0, ge=0)
    validate_pgm: int = Field(0, ge=0)
    read_write: int = Field(0, ge=0)
    relocate:   int = Field(0, ge=0)
    # Combat / defense
    attack:     int = Field(0, ge=0)
    poison:     int = Field(0, ge=0)   # offensive crippler vs an enemy decker's Bod (Acid analog)
    restrict:   int = Field(0, ge=0)   # offensive crippler vs an enemy decker's Evasion (Binder analog)
    reveal:     int = Field(0, ge=0)   # offensive crippler vs an enemy decker's Masking (Marker analog)
    black_hammer: int = Field(0, ge=0) # lethal offensive (Physical) vs enemy deckers; max rating = ceil(Computer/2)
    killjoy:    int = Field(0, ge=0)   # lethal offensive (Stun) vs enemy deckers; max rating = ceil(Computer/2)
    steamroller: int = Field(0, ge=0)  # anti-tar: inflicts (Rating)D to a Tar Baby/Tar Pit IC; immune to the tar crash-backlash
    slow:       int = Field(0, ge=0)   # anti-proactive-IC: opposed test makes a proactive IC lose actions / HANG for the turn
    armor:      int = Field(0, ge=0)
    shield:     int = Field(0, ge=0)
    restore:    int = Field(0, ge=0)
    medic:      int = Field(0, ge=0)
    disinfect:  int = Field(0, ge=0)   # anti-worm: destroys worm IC; raises the worm-infection TN (passive defense)
    compressor: int = Field(0, ge=0)   # special: halves a downloaded file's stored size (cap Rating*100 Mp); decompress before use


class MemoryProgram(BaseModel):
    """A program the decker carries that Swap Memory can move between storage and active
    memory mid-run. size is its active-memory footprint in Mp."""
    name:   str = Field("", max_length=40)   # utility key, e.g. "analyze", "read_write"
    rating: int = Field(0, ge=0, le=50)
    size:   int = Field(0, ge=0)


class ProgramOptions(BaseModel):
    """Run-relevant program options carried from the Deck Workshop into a run, keyed by
    utility type (e.g. "attack"). Build-time-only options (Optimization / Squeeze / Limit)
    affect size/cost in the workshop and are intentionally NOT carried here."""
    skulk:       int = Field(0, ge=0, le=50)   # crashing IC: reduce the tally increase by this
    area:        int = Field(0, ge=0, le=50)   # attack copes with an IC cluster (offsets its TN penalty)
    dinab:       int = Field(0, ge=0, le=50)   # "Decker In A Box": Free action runs this program autonomously at skill = rating
    targeting:   bool = False                  # -2 to-hit TN on attacks made with this utility
    penetration: bool = False                  # defeats Shield (Shift then adds +2)
    chaser:      bool = False                  # defeats Shift (Shield then adds +2)
    one_shot:    bool = False                  # single-use copy: consumed on use (reload via Swap Memory; Tar IC wipes every copy)


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
    # util key -> run-relevant program options (Skulk / Targeting / Penetration / Chaser / Area
    # / etc.), read automatically by the engine instead of asking the player each action.
    program_options:   dict[str, ProgramOptions] = Field(default_factory=dict)


# -- Run creation ---------------------------------------------------------------

class MatrixRunCreate(BaseModel):
    host_id: int
    decker: DeckerStats


# -- Action input --------------------------------------------------------------

ActionType = Literal[
    "logon_to_host", "logon_to_ltg",
    "analyze_host", "analyze_ic", "analyze_icon", "analyze_security", "analyze_subsystem",
    "locate_paydata", "locate_ic", "locate_decker",
    "download_data", "edit_file",
    "null_operation", "graceful_logoff", "crash_host",
    "validate_passcode", "decoy",
    "redirect_datatrail", "relocate", "decrypt_file",
    "swap_memory", "purge_hog", "medic", "restore", "disinfect",
    "defuse_data_bomb", "steamroller", "slow", "decompress_file",
    "dinab",
    # Combat maneuvers (vr2 L1982) -- Simple Actions, opposed Evasion/Sensor tests
    "evade_detection", "parry_attack", "position_attack",
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
    target_program: str = Field("", max_length=40)  # Swap Memory / Purge Hog: utility key; Restore: BEMS attribute to repair (blank = first relevant / most-damaged)
    swap_out_program: str = Field("", max_length=40)  # Swap Memory: active program to push to storage to free memory
    # Combat maneuvers: which opposing icon to maneuver against (active IC id or revealed
    # enemy-decker id); blank = first eligible target.
    maneuver_target: str = Field("", max_length=64)
    # Position Attack only: "tn" (reduce next-attack TN) or "power" (raise next-attack Power).
    # Anything other than "power" is treated as "tn" by the router.
    position_choice: str = Field("tn", max_length=8)


class RunAttackInput(BaseModel):
    target_ic_id: str = Field(..., max_length=64)
    attack_pool: int = Field(..., ge=1, le=40)
    hacking_pool_dice: int = Field(0, ge=0, le=40)
    armor_utility: int = Field(0, ge=0, le=50)
    # Penetration / Chaser / Skulk / Targeting / Area are now read automatically from the
    # Attack program's options (decker.program_options["attack"]) -- no manual entry.


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


class RunRevealHostRatingsInput(BaseModel):
    # Two-phase Analyze Host: when a successful Analyze Host banked fewer net successes than there
    # are still-hidden ACIFS ratings, the decker chooses which subsystems to reveal (one per banked
    # credit). subsystems = the chosen ACIFS names ("access"/"control"/"index"/"files"/"slave").
    subsystems: list[str] = Field(..., min_length=1, max_length=5)


class RunEnemyAttackInput(BaseModel):
    enemy_id: str = Field(..., max_length=64)
    attack_pool: int = Field(..., ge=1, le=40)
    hacking_pool_dice: int = Field(0, ge=0, le=40)
    # "attack" (default) crashes the enemy icon; the three cripplers attack the enemy's
    # Bod / Evasion / Masking respectively (Poison / Restrict / Reveal). Black Hammer
    # (lethal Physical) / Killjoy (lethal Stun) "function like black IC but from a decker":
    # on an icon crash they burn the enemy's MPCP (blaster at DOUBLE the program rating).
    # All of these target enemy DECKERS only -- never routed through IC.
    program: Literal["attack", "poison", "restrict", "reveal",
                     "black_hammer", "killjoy"] = "attack"


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
