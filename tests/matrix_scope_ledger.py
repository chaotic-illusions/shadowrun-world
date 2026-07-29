"""Canonical scope + exclusions ledger for the VR2 Matrix reconciliation.

This module is the *machine-checked* definition of "what must be reconciled" for the
Matrix subsystem. It is imported by the reconciliation contract tests
(``test_matrix_reconciliation.py``) and the numeric oracle
(``test_matrix_numeric_oracle.py``); it is NOT a test module itself (no ``test_``
functions), so pytest does not collect it directly.

Why it exists
-------------
The reconciliation must prove, for every *buildable* program / option / IC / host
mechanic, that it is (1) present in schema/catalog, (2) reachable via an endpoint AND
a run-UI control, (3) numerically correct in success AND failure against a cited VR2
rule, (4) resolved through ONE shared resolver for every actor, and (5) guarded so
future additions cannot skip any of the above.

To make "no gaps" *provable* rather than asserted, the scope must be a defined,
enumerated set with an explicit exclusions ledger. This module is that set. The
"source of truth for buildable" is the two frontend builders:

  * ``frontend/deck-workshop.html``   -- programs + program options (const UTILITIES / OPTION_DEFS)
  * ``frontend/matrix-designer.html`` -- IC types + host mechanics

Every entry below was verified against the code on 2026-07-07 (see the module-level
line references). When a builder gains a new program/option/IC/mechanic, it must be
added here (or to EXCLUSIONS with a rationale) or the contract test fails -- that is
requirement (5).

Field conventions
-----------------
Reachability tokens are literal substrings / keys the contract test searches for in
``frontend/matrix-run.html`` (the run UI). ``invoke`` kinds:

  console   -- an entry in ACTION_CATALOG (``v: 'key'``); posts to /action
  enemy_opt -- an ``<option value="key">`` in the enemy-decker attack modal (/enemy-decker/attack)
  endpoint  -- a literal URL substring for a dedicated control (e.g. "/attack", "/area-attack")
  raw       -- any literal substring (e.g. a control function name like "doLogon")

A program with an empty ``invoke`` list is *passive/automatic*: the player brings it
into the run via its config field and the engine applies it without an explicit action
(e.g. Sleaze feeds Detection Factor, Armor/Shield resolve on incoming attacks). Its
reachability is proven by the config field alone.
"""

from __future__ import annotations

# The frontend builder catalogs this ledger reconciles against (for provenance).
SOURCE_OF_TRUTH = {
    "programs_and_options": "frontend/deck-workshop.html (const UTILITIES L747, OPTION_DEFS L785)",
    "ic_and_host_mechanics": "frontend/matrix-designer.html (IC arrays L601+, host config_json)",
    "run_ui": "frontend/matrix-run.html (ACTION_CATALOG L1782, cfg-u-* fields L211+)",
    "rules": "vr2_rules.md",
}

# Actors the rules allow to use a shared mechanic. Requirement (4) is that every mechanic
# usable by more than one of these resolves through ONE engine primitive.
ACTORS = ("pc_decker", "enemy_decker", "ic", "dinab")


# =============================================================================
# PROGRAMS  --  the 30 buildable deck utilities (deck-workshop.html UTILITIES, L747)
# =============================================================================
# key   = workshop display name (verbatim)
# slot  = schema DeckerUtilities field (app/schemas/matrix_run.py)
# cat   = workshop category (Operational / Special / Offensive / Defensive)
# cfg   = run-UI config field id in matrix-run.html (id="cfg-u-...")
# invoke= list of {kind,key} run-UI controls that fire it ([] = passive/automatic)
# resolver = engine primitive (app/services/matrix_engine.py) or "system_test" (TN-reducer)
#            or "passive" (no test of its own)
# vr2   = vr2_rules.md line for the governing rule
PROGRAMS: dict[str, dict] = {
    # --- Operational (13): reduce the TN of / enable a System Operation -----------
    "Analyze":    {"slot": "analyze",      "cat": "Operational", "cfg": "cfg-u-analyze",
                   "invoke": [{"kind": "raw", "key": "analyzeIC"}],
                   "resolver": "system_test", "vr2": 1447},
    "Browse":     {"slot": "browse",       "cat": "Operational", "cfg": "cfg-u-browse",
                   "invoke": [{"kind": "console", "key": "locate_file"}],
                   "resolver": "system_test", "vr2": 1885},
    "Crash":      {"slot": "crash",        "cat": "Operational", "cfg": "cfg-u-crash",
                   "invoke": [{"kind": "console", "key": "crash_host"}],
                   "resolver": "system_test", "vr2": 1447},
    "Defuse":     {"slot": "defuse",       "cat": "Operational", "cfg": "cfg-u-defuse",
                   "invoke": [{"kind": "raw", "key": "defuseBomb"}],
                   "resolver": "data_bomb_defuse", "vr2": 1447},
    "Deception":  {"slot": "deception",    "cat": "Operational", "cfg": "cfg-u-deception",
                   "invoke": [{"kind": "raw", "key": "doLogon"}],
                   "resolver": "system_test", "vr2": 1447},
    "Decrypt":    {"slot": "decrypt",      "cat": "Operational", "cfg": "cfg-u-decrypt",
                   "invoke": [{"kind": "raw", "key": "decryptScramble"}],
                   "resolver": "scramble_decrypt_test", "vr2": 1447},
    "Disinfect":  {"slot": "disinfect",    "cat": "Operational", "cfg": "cfg-u-disinfect",
                   "invoke": [{"kind": "console", "key": "disinfect"}],
                   "resolver": "disinfect_test", "vr2": 1447},
    "Evaluate":   {"slot": "evaluate",     "cat": "Operational", "cfg": "cfg-u-evaluate",
                   "invoke": [{"kind": "console", "key": "locate_paydata"}],
                   "resolver": "system_test", "vr2": 1447},
    "Mirrors":    {"slot": "mirrors",      "cat": "Operational", "cfg": "cfg-u-mirrors",
                   "invoke": [{"kind": "console", "key": "decoy"}],
                   "resolver": "system_test", "vr2": 1447},
    "Read/Write": {"slot": "read_write",   "cat": "Operational", "cfg": "cfg-u-read-write",
                   "invoke": [{"kind": "console", "key": "download_data"}],
                   "resolver": "system_test", "vr2": 1447},
    "Relocate":   {"slot": "relocate",     "cat": "Operational", "cfg": "cfg-u-relocate",
                   "invoke": [{"kind": "console", "key": "relocate"}],
                   "resolver": "system_test", "vr2": 1447},
    "Scanner":    {"slot": "scanner",      "cat": "Operational", "cfg": "cfg-u-scanner",
                   "invoke": [{"kind": "console", "key": "locate_decker"}],
                   "resolver": "pc_locate_decker_test", "vr2": 1447},
    "Validate":   {"slot": "validate_pgm", "cat": "Operational", "cfg": "cfg-u-validate",
                   "invoke": [{"kind": "console", "key": "validate_passcode"},
                              {"kind": "console", "key": "invalidate_passcode"}],
                   "resolver": "system_test", "vr2": 1447},

    # --- Special (2): passive / download-size only (no options per RAW) -----------
    "Compressor": {"slot": "compressor",   "cat": "Special", "cfg": "cfg-u-compressor",
                   "invoke": [{"kind": "console", "key": "decompress_file"}],
                   "resolver": "passive", "vr2": 1510},
    "Sleaze":     {"slot": "sleaze",       "cat": "Special", "cfg": "cfg-u-sleaze",
                   "invoke": [],
                   "resolver": "detection_factor", "vr2": 1510},

    # --- Offensive (10) -----------------------------------------------------------
    "Attack":       {"slot": "attack",       "cat": "Offensive", "cfg": "cfg-u-attack",
                     "invoke": [{"kind": "endpoint", "key": "/attack"}],
                     "resolver": "cybercombat_attack", "vr2": 2010},
    "Black Hammer": {"slot": "black_hammer",  "cat": "Offensive", "cfg": "cfg-u-black-hammer",
                     "invoke": [{"kind": "enemy_opt", "key": "black_hammer"}],
                     "resolver": "black_attack", "vr2": 1526},
    "Hog":          {"slot": "hog",           "cat": "Offensive", "cfg": "cfg-u-hog",
                     "invoke": [{"kind": "enemy_opt", "key": "hog"}],
                     "resolver": "hog_attack", "vr2": 1526},
    "Killjoy":      {"slot": "killjoy",       "cat": "Offensive", "cfg": "cfg-u-killjoy",
                     "invoke": [{"kind": "enemy_opt", "key": "killjoy"}],
                     "resolver": "black_attack", "vr2": 1526},
    "Lock-On":      {"slot": "lock_on",       "cat": "Offensive", "cfg": "cfg-u-lock-on",
                     "invoke": [],
                     "resolver": "maneuver_test", "vr2": 1587},
    "Poison":       {"slot": "poison",        "cat": "Offensive", "cfg": "cfg-u-poison",
                     "invoke": [{"kind": "enemy_opt", "key": "poison"}],
                     "resolver": "attribute_attack_core", "vr2": 1526},
    "Restrict":     {"slot": "restrict",      "cat": "Offensive", "cfg": "cfg-u-restrict",
                     "invoke": [{"kind": "enemy_opt", "key": "restrict"}],
                     "resolver": "attribute_attack_core", "vr2": 1526},
    "Reveal":       {"slot": "reveal",        "cat": "Offensive", "cfg": "cfg-u-reveal",
                     "invoke": [{"kind": "enemy_opt", "key": "reveal"}],
                     "resolver": "attribute_attack_core", "vr2": 1526},
    "Slow":         {"slot": "slow",          "cat": "Offensive", "cfg": "cfg-u-slow",
                     "invoke": [{"kind": "console", "key": "slow"}],
                     "resolver": "slow_test", "vr2": 1526},
    "Steamroller":  {"slot": "steamroller",   "cat": "Offensive", "cfg": "cfg-u-steamroller",
                     "invoke": [{"kind": "console", "key": "steamroller"}],
                     "resolver": "steamroller_attack", "vr2": 1526},

    # --- Defensive (6) ------------------------------------------------------------
    "Armor":   {"slot": "armor",   "cat": "Defensive", "cfg": "cfg-u-armor",
                "invoke": [], "resolver": "damage_resistance", "vr2": 1587},
    "Camo":    {"slot": "camo",    "cat": "Defensive", "cfg": "cfg-u-camo",
                "invoke": [], "resolver": "passive", "vr2": 1587},
    "Cloak":   {"slot": "cloak",   "cat": "Defensive", "cfg": "cfg-u-cloak",
                "invoke": [], "resolver": "maneuver_test", "vr2": 1587},
    "Medic":   {"slot": "medic",   "cat": "Defensive", "cfg": "cfg-u-medic",
                "invoke": [{"kind": "console", "key": "medic"}],
                "resolver": "medic_heal", "vr2": 1587},
    "Restore": {"slot": "restore", "cat": "Defensive", "cfg": "cfg-u-restore",
                "invoke": [{"kind": "console", "key": "restore"}],
                "resolver": "restore_repair", "vr2": 1587},
    "Shield":  {"slot": "shield",  "cat": "Defensive", "cfg": "cfg-u-shield",
                "invoke": [], "resolver": "shield_parry", "vr2": 1587},
}


# =============================================================================
# PROGRAM OPTIONS  --  the 10 buildable options (deck-workshop.html OPTION_DEFS, L785)
# =============================================================================
# key      = workshop option id
# schema   = ProgramOptions field carried into the run, or None if build-time-only
# carried  = whether the option has a run-time effect (is read by the engine)
# consumer = where the effect is applied
# vr2      = vr2_rules.md line
OPTIONS: dict[str, dict] = {
    "area":         {"schema": "area",         "carried": True,
                     "consumer": "attack / area_attack: hit up to [Area] targets, offset TN penalty",
                     "vr2": 1629},
    "chaser":       {"schema": "chaser",       "carried": True,
                     "consumer": "attack: negates Shift penalty (Shield then +2)", "vr2": 1629},
    "dinab":        {"schema": "dinab",        "carried": True,
                     "consumer": "DINAB: autonomous Free-action run at skill = rating", "vr2": 1629},
    "limit":        {"schema": "limit_target", "carried": True,
                     "consumer": "restricts a utility to one target type ('ic'/'decker')",
                     "vr2": 1629},
    "oneshot":      {"schema": "one_shot",     "carried": True,
                     "consumer": "single-use copy consumed on use (reload via Swap Memory)",
                     "vr2": 1629},
    "penetration":  {"schema": "penetration",  "carried": True,
                     "consumer": "attack: negates Shield penalty (Shift then +2)", "vr2": 1629},
    "skulk":        {"schema": "skulk",        "carried": True,
                     "consumer": "crashing IC: reduce the tally increase by [Skulk]", "vr2": 1629},
    "targeting":    {"schema": "targeting",    "carried": True,
                     "consumer": "attack: -2 to-hit TN", "vr2": 1629},
    # Intrinsic (non-toggle) carried field: the Attack utility's OWN coded base Damage Level
    # (Attack-6L/-6M/-6S/-6D), chosen inline with the program's rating in the workshop -- NOT an
    # OPTION_DEFS toggle. Carried in program_options so the engine damages icons at the program's
    # severity instead of the host IC Damage Table. ``intrinsic`` excludes it from the 1:1
    # workshop-toggle mirror while still counting as a carried ProgramOptions field.
    "attack_damage": {"schema": "damage_level", "carried": True, "intrinsic": True,
                     "consumer": "attack: the utility's own coded base Damage Level (not host table)",
                     "vr2": 2052},
    # Build-time-only: affect design/actual SIZE and cost in the workshop, never read at run time.
    "optimization": {"schema": None,           "carried": False,
                     "consumer": "build-time size/cost only (design x2.0, actual x0.5)", "vr2": 1655},
    "squeeze":      {"schema": "squeeze",      "carried": True,
                     "consumer": "half storage footprint; must decompress (Complex Action) after a mid-run swap into active memory",
                     "vr2": 1673},
}


# =============================================================================
# IC  --  the 19 catalog entries (matrix_rules.IC_CATALOG L191) buildable in the designer
# =============================================================================
# key      = IC_CATALOG key
# designer = how it is placed in matrix-designer.html (white/gray/black group + display)
# resolver = engine primitive that resolves its action
# vr2      = vr2_rules.md line
IC: dict[str, dict] = {
    # White
    "Probe":     {"designer": "white / Probe (reactive)",       "resolver": "probe_test",            "vr2": 481},
    "Killer":    {"designer": "white / Killer",                 "resolver": "cybercombat_attack",    "vr2": 439},
    "Acid":      {"designer": "white / Crippler (Acid=Bod)",    "resolver": "crippler_attack",       "vr2": 431},
    "Binder":    {"designer": "white / Crippler (Binder=Evasion)", "resolver": "crippler_attack",    "vr2": 431},
    "Jammer":    {"designer": "white / Crippler (Jammer=Sensor)",  "resolver": "crippler_attack",    "vr2": 431},
    "Marker":    {"designer": "white / Crippler (Marker=Masking)", "resolver": "crippler_attack",    "vr2": 431},
    "Tar Baby":  {"designer": "white / Tar Baby (reactive)",    "resolver": "tar_baby_test",         "vr2": 497},
    "Data Bomb": {"designer": "host config dataBombs[] (file/slave)", "resolver": "data_bomb_defuse", "vr2": 457},
    "Scramble":  {"designer": "host config scrambles[] (access/file/slave)", "resolver": "scramble_decrypt_test", "vr2": 487},
    # Gray
    "Blaster":   {"designer": "gray / Blaster",                 "resolver": "cybercombat_attack",    "vr2": 517},
    "Sparky":    {"designer": "gray / Sparky",                  "resolver": "cybercombat_attack",    "vr2": 527},
    "Acid-rip":  {"designer": "gray / Ripper (Acid-rip=Bod)",   "resolver": "crippler_attack",       "vr2": 523},
    "Bind-rip":  {"designer": "gray / Ripper (Bind-rip=Evasion)", "resolver": "crippler_attack",     "vr2": 523},
    "Jam-rip":   {"designer": "gray / Ripper (Jam-rip=Sensor)", "resolver": "crippler_attack",       "vr2": 523},
    "Mark-rip":  {"designer": "gray / Ripper (Mark-rip=Masking)", "resolver": "crippler_attack",     "vr2": 523},
    "Tar Pit":   {"designer": "gray / Tar Pit (reactive)",      "resolver": "tar_baby_test",         "vr2": 536},
    "Worm":      {"designer": "host config worms[] (ACIFS)",    "resolver": "worm_attack",           "vr2": 544},
    "Trace":     {"designer": "gray / Trace (reactive)",        "resolver": "trace_hunt_cycle_attack", "vr2": 560},
    # Black
    "Black IC":  {"designer": "black / Black IC (Lethal + Non-Lethal)", "resolver": "black_attack",  "vr2": 603},
}


# =============================================================================
# HOST MECHANICS  --  the 11 in-scope host-level mechanics (matrix-designer.html config_json)
# =============================================================================
# key     = mechanic id
# schema  = the Pydantic symbol (attribute path on a schema class) proving it is modelled
# handler = a verified module-qualified symbol ("mr.foo" / "eng.bar" / "rules.BAZ") that
#           resolves or tabulates it (existence asserted by the contract test)
# endpoint= a run endpoint (matrix_runs.py handler symbol on mr) that exercises it
# vr2     = vr2_rules.md line
HOST_MECHANICS: dict[str, dict] = {
    "security_code_value": {"schema": "SheaveSaveInput.security_code",
                            "handler": "rules.COMBAT_TN", "endpoint": "mr.start_run", "vr2": 258},
    "acifs_ratings":       {"schema": "SheaveSaveInput.acifs",
                            "handler": "rules.HOST_DIFFICULTY", "endpoint": "mr.perform_action", "vr2": 35},
    "sheaf_steps_triggers": {"schema": "SheafStep.trigger",
                            "handler": "mr._activate_sheaf_step", "endpoint": "mr.new_turn", "vr2": 817},
    "alerts":              {"schema": "SheafEvent.type",
                            "handler": "rules.SHEAF_ALERT_TABLE", "endpoint": "mr.new_turn", "vr2": 835},
    "scramble_ic":         {"schema": "SheafEvent.type",
                            "handler": "eng.scramble_failure_consequence", "endpoint": "mr.perform_action", "vr2": 487},
    "data_bomb":           {"schema": "SheafEvent.type",
                            "handler": "eng.data_bomb_detonate", "endpoint": "mr.perform_action", "vr2": 457},
    "worm_ic":             {"schema": "SheafEvent.type",
                            "handler": "eng.worm_attack", "endpoint": "mr.perform_action", "vr2": 544},
    "trap_ic":             {"schema": "SheafEvent.surface_ic_type",
                            "handler": "mr._activate_sheaf_step", "endpoint": "mr.new_turn", "vr2": 684},
    "constructs_party_ic": {"schema": "SheafEvent.components",
                            "handler": "mr._activate_sheaf_step", "endpoint": "mr.new_turn", "vr2": 718},
    "bouncer":             {"schema": "SheafEvent.new_security_code",
                            "handler": "mr._activate_sheaf_step", "endpoint": "mr.new_turn", "vr2": 300},
    "trap_doors":          {"schema": "RunTrapDoorInput.action",
                            "handler": "mr.trap_door_action", "endpoint": "mr.trap_door_action", "vr2": 312},
    "paydata_economy":     {"schema": "SheaveSaveInput.acifs",
                            "handler": "rules.PAYDATA_TABLE", "endpoint": "mr.perform_action", "vr2": 986},
}


# =============================================================================
# EXCLUSIONS  --  everything deliberately OUT of scope, with a rationale
# =============================================================================
# This is what makes "no gaps" provable: the union of (in-scope surfaces) and
# (exclusions) must cover the entire VR2 program/option/IC/mechanic space we chose to
# model. Each entry names WHY it is excluded so the boundary is auditable.
# kind: option | program | actor | mechanic | variant | feature
EXCLUSIONS: dict[str, dict] = {
    # --- Program options in VR2 that the deck workshop deliberately does NOT offer ---
    "Sensitive (option)": {"kind": "option",
        "reason": "VR2 option not offered by the deck workshop (absent from OPTION_DEFS); "
                  "there is no way to build a program carrying it, so nothing to reconcile in-run.",
        "vr2": 1629},
    # --- VR2 utilities / programs the app intentionally does not model ---------------
    "Commlink (program)": {"kind": "program",
        "reason": "Culled operational utility; not modelled (no comm-relay play in the run engine).",
        "vr2": 1447},
    "Spoof (program)": {"kind": "program",
        "reason": "Culled operational utility and its slave-spoof operations are not modelled.",
        "vr2": 1447},
    "Track (program)": {"kind": "program",
        "reason": "Not modelled; PC-side trace-back play is out of scope for the run engine.",
        "vr2": 1447},
    # --- Actors / constructs not modelled -------------------------------------------
    "Frames": {"kind": "actor",
        "reason": "Semi-autonomous agent programs (VR2 Frames) are not modelled as run actors; "
                  "DINAB covers single-program autonomy instead. Scanner's 'Locate Frame' clause is "
                  "therefore inert.", "vr2": 1694},
    # --- Sub-variants that the engine treats identically (flavor only) ---------------
    "Dataworm variant": {"kind": "variant",
        "reason": "Dataworm reporting is narrative-only. Deathworm and Tapeworm are modeled as "
                  "persistent MPCP infections with distinct runtime effects and test coverage.",
        "vr2": 554},
    "Psychotropic Black IC": {"kind": "variant",
        "reason": "VR2 psychotropic Black IC (L649) is not a separate buildable option; the designer "
                  "offers only Lethal + Non-Lethal Black IC, both resolved by black_attack.", "vr2": 649},
    # --- Advanced/optional host features not in the buildable surface ---------------
    "UV Hosts / Reality Filters / Command Sets": {"kind": "feature",
        "reason": "Advanced optional VR2 systems with no builder surface and no run control; "
                  "out of the defined scope.", "vr2": 383},
}


# =============================================================================
# DOCUMENTED DIVERGENCES  --  found by the audit; require a USER RULING (stop-and-ask)
# =============================================================================
# These are NOT auto-fixed. They are code-vs-rules or shared-resolver divergences that
# may be intentional house rules. The contract test asserts this registry is non-drifting
# (each id is still present in the code at the cited location), so a divergence cannot be
# silently "resolved" by deleting the evidence.
# status: open (awaiting ruling) | accepted (house rule) | fixed
DIVERGENCES: list[dict] = [
    {"id": "dinab_attack_ic_bypass", "kind": "shared_resolver", "status": "fixed",
     "location": "app/routers/matrix_runs.py :: _dinab_attack_ic",
     "vr2": 2010,
     "summary": "A DINAB running the Attack program against an IC hand-rolls the strike via "
                "eng.roll_dice + eng.stage_damage instead of the shared eng.cybercombat_attack. "
                "DINAB is an in-scope actor, so this is a requirement-4 (one-resolver) divergence: "
                "DINAB->IC attack can drift from PC->IC / IC->PC / decker->PC cybercombat.",
     "resolution": "Fixed: _dinab_attack_ic now resolves the strike through eng.cybercombat_attack "
                   "(attacker pool = eff, Power = eff + cluster, IC resists with Security Value +/- "
                   "Expert vs Power, Armor reduces Power), so DINAB->IC uses the identical resolver "
                   "as every other attack direction. Ruling: route DINAB Attack-vs-IC through the seam."},
    {"id": "area_attack_cybercombat_bypass", "kind": "shared_resolver", "status": "fixed",
     "location": "app/routers/matrix_runs.py :: area_attack",
     "vr2": 2010,
     "summary": "The Area-option burst resolves multi-target IC/enemy damage with its own "
                "eng.roll_dice + eng.damage_resistance math instead of eng.cybercombat_attack, and "
                "does NOT invoke _enemy_shield_parry for enemy targets. Two requirement-4 bypasses "
                "(cybercombat + enemy shield) in one endpoint.",
     "resolution": "Fixed: the vr2 Area rule (L1663) mandates ONE Attack Test for all targets, so "
                   "the endpoint keeps the single shared attack roll and routes EACH target's damage "
                   "through eng.damage_resistance -- the identical resistance stage "
                   "eng.cybercombat_attack uses internally. IC now resists on the Power model (like "
                   "/attack + DINAB) instead of a hand-rolled combat-TN roll, and enemy targets now "
                   "parry via _enemy_shield_parry (successes fed in as shield_successes). Ruling: "
                   "resolve each target via the shared cybercombat resolver + honor the enemy shield."},
    {"id": "bouncer_inert", "kind": "buildable_not_resolved", "status": "fixed",
     "location": "frontend/matrix-designer.html (builds bouncer) vs app/routers/matrix_runs.py "
                 ":: _activate_sheaf_step (no bouncer branch)",
     "vr2": 300,
     "summary": "The host designer builds a Bouncer sheaf event (type='bouncer', new_security_code, "
                "new_security_value) -- a real VR2 rule (L300) that upgrades the host security "
                "code/value mid-run. _activate_sheaf_step only handles ic/trap_ic/construct/party_ic, "
                "and SheafEvent lacks the new_security_* fields, so a triggered Bouncer is silently "
                "inert. Buildable but unreconciled: needs a run-engine handler + schema fields, or "
                "the designer control should be removed.",
     "resolution": "Fixed: SheafEvent now carries new_security_code / new_security_value (so the "
                   "designer payload survives model_dump persistence), and _activate_sheaf_step gained "
                   "a 'bouncer' branch that upgrades state host_security_code / host_security_value for "
                   "the rest of the run and logs the shift. A triggered Bouncer now hardens the host. "
                   "Ruling: implement the SheafEvent fields + the bouncer branch."},
    {"id": "logon_to_ltg_unsurfaced", "kind": "backend_only", "status": "fixed",
     "location": "app/schemas/matrix_run.py ActionType 'logon_to_ltg' vs frontend/matrix-run.html "
                 "(no control)",
     "vr2": 174,
     "summary": "logon_to_ltg is a valid ActionType with subsystem/utility map entries but no run-UI "
                "control (a run starts already on a host, so LTG-logon is not separately surfaced). "
                "Either surface a control or retire the vestigial action -- a ruling, not a silent gap."},
]


# =============================================================================
# UI-REACHABILITY GAPS  --  pure wiring gaps to be FIXED (per remediation policy)
# =============================================================================
# Unlike DIVERGENCES (which need a ruling), these are fully-implemented backend actions
# with no run-UI control -- a pure reachability gap the policy says to auto-fix. Each is
# tracked here until its control is added, at which point it moves out of this set and the
# reachability test enforces the control's presence with no exception.
# status: open (no control yet) | fixed (control added)
UI_REACHABILITY_GAPS: dict[str, dict] = {
    "purge_hog": {"status": "fixed",
        "backend": "app/routers/matrix_runs.py perform_action 'purge_hog' branch (eng.hog_purge_test)",
        "gap": "No run-UI control POSTs action_type='purge_hog', so a player infected by an enemy "
               "Hog cannot invoke the defensive purge. cfg-u-hog (offensive Hog) and the enemy-decker "
               "'hog' option exist, but the purge counter-action is unreachable.",
        "fix": "Add a 'Purge Hog' control (ACTION_CATALOG entry gated on an active infection).",
        "resolved": "frontend/matrix-run.html: ACTION_CATALOG 'purge_hog' entry (Complex) gated on "
                    "_pcHogInfections(state); the selected infection id is POSTed as target_program."},
}


# ----------------------------------------------------------------------------- accessors
def all_program_slots() -> set[str]:
    """Schema DeckerUtilities fields covered by in-scope programs."""
    return {p["slot"] for p in PROGRAMS.values()}


def carried_option_fields() -> set[str]:
    """ProgramOptions fields that in-scope options map to (run-carried options only)."""
    return {o["schema"] for o in OPTIONS.values() if o["carried"] and o["schema"]}


def toggle_option_keys() -> set[str]:
    """Workshop TOGGLE option ids (OPTION_DEFS). Excludes intrinsic program attributes such as the
    Attack utility's coded Damage Level, which is chosen inline with the program's rating rather
    than via a toggle, so it has no OPTION_DEFS row even though it IS a carried ProgramOptions field."""
    return {k for k, o in OPTIONS.items() if not o.get("intrinsic")}


def active_programs() -> dict[str, dict]:
    """Programs with at least one explicit run-UI invoke control (not passive/automatic)."""
    return {name: p for name, p in PROGRAMS.items() if p["invoke"]}


def open_divergences() -> list[dict]:
    return [d for d in DIVERGENCES if d["status"] == "open"]


def open_ui_gaps() -> dict[str, dict]:
    return {k: v for k, v in UI_REACHABILITY_GAPS.items() if v["status"] == "open"}
