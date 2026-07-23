from __future__ import annotations

from datetime import datetime
from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator


# -- Decker input ---------------------------------------------------------------

class _StrictModel(BaseModel):
    """Base for request-body schemas: reject undeclared fields (extra='forbid') so a stale or
    renamed client field surfaces as a loud 422 instead of being silently dropped."""
    model_config = ConfigDict(extra="forbid")


class DeckerUtilities(_StrictModel):
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
    hog:        int = Field(0, ge=0)   # offensive virus vs an enemy decker: a persistent infection that drains its highest running program each Combat Turn until purged/crashed
    black_hammer: int = Field(0, ge=0) # lethal offensive (Physical) vs enemy deckers; max rating = ceil(Computer/2)
    killjoy:    int = Field(0, ge=0)   # lethal offensive (Stun) vs enemy deckers; max rating = ceil(Computer/2)
    steamroller: int = Field(0, ge=0)  # anti-tar: inflicts (Rating)D to a Tar Baby/Tar Pit IC; immune to the tar crash-backlash
    slow:       int = Field(0, ge=0)   # anti-proactive-IC: opposed test makes a proactive IC lose actions / HANG for the turn
    # Combat maneuvers (vr2 L1599-1605): Cloak aids the maneuvering icon, Lock-On the opposing icon
    cloak:      int = Field(0, ge=0)   # lowers the decker's Evasion-test TN when IT maneuvers (Evade/Parry/Position)
    lock_on:    int = Field(0, ge=0)   # lowers the decker's Sensor-test TN when an opposing icon maneuvers (holds the lock)
    armor:      int = Field(0, ge=0)
    shield:     int = Field(0, ge=0)
    restore:    int = Field(0, ge=0)
    medic:      int = Field(0, ge=0)
    disinfect:  int = Field(0, ge=0)   # anti-worm: destroys worm IC; raises the worm-infection TN (passive defense)
    compressor: int = Field(0, ge=0)   # special: halves a downloaded file's stored size (cap Rating*100 Mp); decompress before use


class MemoryProgram(_StrictModel):
    """A program the decker carries that Swap Memory can move between storage and active
    memory mid-run. size is its FULL (decompressed) active-memory footprint in Mp. A Squeezed
    program is stored at half that size but must be decompressed (Complex Action) to full size
    before it can be used once loaded into active memory (vr2 Squeeze option, L1673)."""
    name:   str = Field("", max_length=40)   # utility key, e.g. "analyze", "read_write"
    rating: int = Field(0, ge=0, le=50)
    size:   int = Field(0, ge=0, le=100000)  # full (decompressed) active footprint in Mp
    squeezed: bool = False                   # built with the Squeeze option: half storage, needs decompress after a swap-in


class ProgramOptions(_StrictModel):
    """Run-relevant program options carried from the Deck Workshop into a run, keyed by
    utility type (e.g. "attack"). Optimization stays build-time-only (pure size/cost); Squeeze
    IS carried (as ``squeeze``) because it changes run-time behaviour -- a squeezed program takes
    half storage but must be decompressed (Complex Action) before use after a mid-run swap-in.
    Limit is carried (as limit_target) because it restricts which target type the utility may
    affect at run time."""
    skulk:       int = Field(0, ge=0, le=50)   # crashing IC: reduce the tally increase by this
    area:        int = Field(0, ge=0, le=50)   # attack copes with an IC cluster (offsets its TN penalty)
    dinab:       int = Field(0, ge=0, le=50)   # "Decker In A Box": Free action runs this program autonomously at skill = rating
    targeting:   bool = False                  # -2 to-hit TN on attacks made with this utility
    penetration: bool = False                  # defeats Shield (Shift then adds +2)
    chaser:      bool = False                  # defeats Shift (Shield then adds +2)
    one_shot:    bool = False                  # single-use copy: consumed on use (reload via Swap Memory; Tar IC wipes every copy)
    squeeze:     bool = False                   # built compressed: half storage footprint; must be decompressed (Complex Action, no test) after a mid-run swap into active memory
    limit_target: str = Field("", max_length=8)  # Limit option: "" (none) / "ic" / "decker" -- the ONLY target type this utility may affect
    # Attack utility only: its OWN base Damage Level (vr2 Attack-6L/-6M/-6S/-6D), chosen at code
    # time and priced by level. Carried so the engine damages icons at the program's chosen
    # severity, NOT the host IC Damage Table. "" = legacy/unset -> the engine falls back to the host.
    damage_level: str = Field("", max_length=8)

    @field_validator("limit_target")
    @classmethod
    def _norm_limit_target(cls, v: str) -> str:
        v = (v or "").strip().lower()
        if v not in ("", "ic", "decker"):
            raise ValueError('limit_target must be "", "ic", or "decker"')
        return v

    @field_validator("damage_level")
    @classmethod
    def _norm_damage_level(cls, v: str) -> str:
        v = (v or "").strip().title()
        if v not in ("", "Light", "Moderate", "Serious", "Deadly"):
            raise ValueError('damage_level must be "", "Light", "Moderate", "Serious", or "Deadly"')
        return v


class MpcpInfection(_StrictModel):
    """A persistent Worm infection lodged in the deck's MPCP, carried across runs until the chip
    is replaced. variant drives the ongoing effect (deathworm = cybercombat-TN penalty; tapeworm =
    paydata erasure at run end; standard = chip degraded only)."""
    variant: Literal["standard", "deathworm", "tapeworm"] = "standard"
    rating:  int = Field(6, ge=1, le=50)
    ic_id:   str = Field("", max_length=40)



class DeckerStats(_StrictModel):
    name: str = "Ghost"
    # Deck provenance so run consequences (MPCP damage, chip burn, worm infection) can be written
    # back to the owning character's persisted deck at run end. Both are optional (legacy/ad-hoc
    # runs may omit them) -- damage write-back is skipped when either is missing.
    character_id: int | None = None
    deck_name:    str = Field("", max_length=120)
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
    # these into active memory mid-run (and push an active program back to storage). Capped to
    # keep the client-supplied payload bounded (mirrors mpcp_infections).
    storage_programs:  list[MemoryProgram] = Field(default_factory=list, max_length=64)
    # util key -> active-memory size (Mp) for every program carried (active + storage), so the
    # engine can enforce the active-memory cap when swapping a program in.
    program_sizes:     dict[str, int] = Field(default_factory=dict, max_length=128)
    # util key -> run-relevant program options (Skulk / Targeting / Penetration / Chaser / Area
    # / etc.), read automatically by the engine instead of asking the player each action.
    program_options:   dict[str, ProgramOptions] = Field(default_factory=dict, max_length=128)
    # Persistent MPCP infections carried on the deck from previous runs (Deathworm / Tapeworm).
    # An infection is permanent until the MPCP chip is replaced, so the client re-sends it every
    # run: a Deathworm keeps degrading cybercombat TNs and a Tapeworm keeps erasing paydata until
    # the chip is remediated in the Deck Workshop. Capped to keep the payload bounded.
    mpcp_infections:   list[MpcpInfection] = Field(default_factory=list, max_length=32)


# -- Run creation ---------------------------------------------------------------

class MatrixRunCreate(_StrictModel):
    host_id: int
    decker: DeckerStats


# -- Action input --------------------------------------------------------------

ActionType = Literal[
    "logon_to_host",
    "analyze_host", "analyze_ic", "analyze_icon", "analyze_security", "analyze_subsystem",
    "locate_paydata", "locate_ic", "locate_decker",
    "download_data", "edit_file",
    "null_operation", "graceful_logoff", "crash_host",
    "validate_passcode", "invalidate_passcode", "decoy",
    "redirect_datatrail", "relocate", "decrypt_file",
    "swap_memory", "unload_program", "purge_hog", "medic", "restore", "disinfect",
    "defuse_data_bomb", "steamroller", "slow", "decompress_file",
    "dinab",
    # Combat maneuvers (vr2 L1982) -- Simple Actions, opposed Evasion/Sensor tests
    "evade_detection", "parry_attack", "position_attack",
]

SubsystemType = Literal["access", "control", "index", "files", "slave"]


class RunActionInput(_StrictModel):
    action_type: ActionType
    subsystem: SubsystemType
    utility_rating: int = Field(0, ge=0, le=50)
    hacking_pool_dice: int = Field(0, ge=0, le=40)
    extra_tn_modifier: int = Field(0, ge=-6, le=6)
    note: str = Field("", max_length=500)
    target_ic_id: str = Field("", max_length=64)  # Analyze IC: which IC to reveal (blank = first unknown)
    target_file: str = Field("", max_length=160)   # Decrypt File: scramble target_key / paydata name (blank = first scramble)
    target_program: str = Field("", max_length=40)  # Swap Memory (load) / Unload Program: utility key; Purge Hog: utility key; Restore: BEMS attribute to repair (blank = first relevant / most-damaged)
    # Combat maneuvers: which opposing icon to maneuver against (active IC id or revealed
    # enemy-decker id); blank = first eligible target.
    maneuver_target: str = Field("", max_length=64)
    # Position Attack only: "tn" (reduce next-attack TN) or "power" (raise next-attack Power).
    # Anything other than "power" is treated as "tn" by the router.
    position_choice: str = Field("tn", max_length=8)
    # Edit File only: "erase" (destroy the located file) or "modify" (tamper with / corrupt the
    # host's copy in place). Anything other than "modify" is treated as "erase" by the router.
    edit_mode: str = Field("erase", max_length=8)
    # Relocate only: when True, a successful Relocate (won the opposed Control vs Security test)
    # SUPPRESSES the trace IC in place instead of merely spoofing it -- pausing its cycle for 1
    # Detection Factor (vr2 L588). A released trace resumes where it left off.
    suppress_trace: bool = False


class RunAttackInput(_StrictModel):
    target_ic_id: str = Field(..., max_length=64)
    attack_pool: int = Field(..., ge=1, le=40)
    hacking_pool_dice: int = Field(0, ge=0, le=40)
    armor_utility: int = Field(0, ge=0, le=50)
    # Penetration / Chaser / Skulk / Targeting / Area are now read automatically from the
    # Attack program's options (decker.program_options["attack"]) -- no manual entry.


class RunLogoffInput(_StrictModel):
    hacking_pool_dice: int = Field(0, ge=0, le=40)
    deception_utility: int = Field(0, ge=0, le=50)


class RunDefendInput(_StrictModel):
    # Hacking Pool dice the decker spends on the resist test surfaced by state["pending_defense"]
    # (the interactive per-attack defense flow). vr2: HP may be added to a defense test -- capped
    # server-side at the remaining pool; 0 = resist with Bod alone (or just decline the offer).
    hacking_pool_dice: int = Field(0, ge=0, le=40)


class RunTrapDoorInput(_StrictModel):
    # "enter": graceful logoff through the concealing subsystem, then arrive on the destination
    # host (a fresh linked run; destination revealed only on arrival).
    # "file":  record the door for intel -- reveals only whether the destination has LTG access.
    action: Literal["enter", "file"]
    hacking_pool_dice: int = Field(0, ge=0, le=40)   # enter only: dice for the logoff Access Test
    deception_utility: int = Field(0, ge=0, le=50)   # enter only: Deception utility for the logoff


class RunSuppressInput(_StrictModel):
    ic_id: str = Field(..., max_length=64)  # crashed/hung IC id OR a non-IC suppression entry id (data bomb)
    release: bool = Field(False)  # False = suppress (DF -1); True = release (restore DF, +tally)


class RunRevealHostRatingsInput(_StrictModel):
    # Two-phase Analyze Host: when a successful Analyze Host banked fewer net successes than there
    # are still-hidden items, the decker chooses which to reveal (one per banked credit). subsystems
    # = the chosen names: the ACIFS ratings ("access"/"control"/"index"/"files"/"slave") and/or
    # "security" (the host Security Rating -- a 6th revealable item).
    subsystems: list[str] = Field(..., min_length=1, max_length=6)


class RunEnemyAttackInput(_StrictModel):
    enemy_id: str = Field(..., max_length=64)
    attack_pool: int = Field(..., ge=1, le=40)
    hacking_pool_dice: int = Field(0, ge=0, le=40)
    # "attack" (default) crashes the enemy icon; the three cripplers attack the enemy's
    # Bod / Evasion / Masking respectively (Poison / Restrict / Reveal). Black Hammer
    # (lethal Physical) / Killjoy (lethal Stun) "function like black IC but from a decker":
    # on an icon crash they burn the enemy's MPCP (blaster at DOUBLE the program rating).
    # Hog is the offensive virus -- a persistent infection that drains the enemy's highest
    # running program each Combat Turn (the same one an enemy decker can plant on the PC).
    # All of these target enemy DECKERS only -- never routed through IC.
    program: Literal["attack", "poison", "restrict", "reveal", "hog",
                     "black_hammer", "killjoy"] = "attack"


class RunEnemyScanInput(_StrictModel):
    """Scan Icon vs a revealed enemy decker (vr2 L1895): a Computer Test vs the target's Masking
    (adjusted by the target's Sleaze minus the PC's Scanner). Each net success reveals one of the
    enemy's hidden ratings (MPCP / a Persona rating / Response Increase); 3+ successes reveal all.
    Decker-only target, so it doubles as the Analyze-Icon read for a hostile decker."""
    enemy_id: str = Field(..., max_length=64)
    hacking_pool_dice: int = Field(0, ge=0, le=40)


class RunAreaAttackInput(_StrictModel):
    """One Area-option Attack burst against several icons at once (vr2 Area utility). The
    ``target_ids`` mix active IC ids and revealed enemy-decker ids; the caller must keep the
    count within the Attack utility's Area rating (enforced server-side)."""
    target_ids: list[str] = Field(..., min_length=1, max_length=16)
    attack_pool: int = Field(..., ge=1, le=40)
    hacking_pool_dice: int = Field(0, ge=0, le=40)

    @field_validator("target_ids")
    @classmethod
    def _clean_target_ids(cls, v: list[str]) -> list[str]:
        seen: set[str] = set()
        out: list[str] = []
        for raw in v:
            t = (raw or "").strip()
            if not t:
                continue
            if len(t) > 64:
                raise ValueError("target id too long")
            if t not in seen:
                seen.add(t)
                out.append(t)
        if not out:
            raise ValueError("at least one target required")
        return out


# -- Sheaf + Host designer -----------------------------------------------------

class SheafEvent(BaseModel):
    type: str  # ic, passive_alert, active_alert, shutdown, trap_ic, construct, party_ic, bouncer
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
    # Bouncer -- upgrades the host security code/value mid-run (vr2 L300)
    new_security_code: str | None = None
    new_security_value: int | None = None


class SheafStep(BaseModel):
    trigger: int
    events: list[SheafEvent]


class SheaveSaveInput(BaseModel):
    sheaf: list[SheafStep] = Field(max_length=64)
    security_code: str
    security_value: int
    acifs: list[int] = Field(default_factory=list)  # [A, C, I, F, S]
    owner_type: str = "corp"


class SheafGenerateInput(BaseModel):
    security_code: str
    security_value: int
    owner_type: str = "corp"
    step_count: int | None = Field(default=None, ge=1, le=64)
    seed: int | None = None


# -- Read schemas --------------------------------------------------------------

class MatrixRunSummary(BaseModel):
    id: int
    host_id: int | None
    status: str
    aar_acknowledged: bool = False
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class MatrixRunRead(BaseModel):
    id: int
    host_id: int | None
    decker_json: dict[str, Any]
    state_json: dict[str, Any]
    status: str
    aar_acknowledged: bool = False
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class MatrixRunAAR(BaseModel):
    """GM after-action report for an ENDED run. Computed on demand from the run's frozen state --
    surfaces the consequences the GM must adjudicate (paydata haul, whether the decker was traced /
    physically located, injuries, lingering MPCP infections, alert level reached)."""
    run_id: int
    host_id: int | None
    status: str
    end_reason: str | None
    outcome: str
    escaped_clean: bool
    decker_name: str
    character_id: int | None
    paydata: dict[str, Any]
    traced: bool
    physical_location_found: bool
    physical_trace_immune: bool
    injuries: list[str]
    mpcp_damage: int
    persona_chip_burn: dict[str, int]
    mpcp_infections: list[dict[str, Any]]
    enemy_deckers: list[dict[str, Any]] = []
    trap_doors: list[dict[str, Any]] = []
    alert_status: str
    security_tally: int
    acknowledged: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
