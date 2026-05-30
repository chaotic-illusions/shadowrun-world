"""
VR2.0 (Shadowrun 2nd Edition) rules reference data.
All tables encoded from vr2_rules.md. Used by matrix_engine and frontend tooltips.
"""

from __future__ import annotations

#  Security codes 
SECURITY_CODES: list[str] = ["Blue", "Green", "Orange", "Red", "Black"]

SECURITY_CODE_ORDER: dict[str, int] = {c: i for i, c in enumerate(SECURITY_CODES)}

# Initiative dice added to IC rating by host security code
IC_INITIATIVE_DICE: dict[str, int] = {
    "Blue": 1, "Green": 2, "Orange": 3, "Red": 4, "Black": 5,
}

# Base IC damage level per host security code (before staging)
IC_DAMAGE_LEVEL: dict[str, str] = {
    "Blue": "Light", "Green": "Moderate", "Orange": "Moderate",
    "Red": "Serious", "Black": "Serious",
}

# Dump shock damage level per host security code
DUMP_SHOCK_LEVEL: dict[str, str] = {
    "Blue": "Light", "Green": "Moderate", "Orange": "Serious",
    "Red": "Deadly", "Black": "Deadly",
}

# Cybercombat attack target numbers by host security code and target status
COMBAT_TN: dict[str, dict[str, int]] = {
    "Blue":   {"intruding": 6, "legitimate": 3},
    "Green":  {"intruding": 5, "legitimate": 4},
    "Orange": {"intruding": 4, "legitimate": 5},
    "Red":    {"intruding": 5, "legitimate": 6},
    "Black":  {"intruding": 3, "legitimate": 8},
}

# Simsense overload willpower TN by damage level (hot deck + white/gray IC only)
SIMSENSE_OVERLOAD_TN: dict[str, int] = {
    "Light": 2, "Moderate": 3, "Serious": 5,
}

# Damage boxes filled per damage level
DAMAGE_BOXES: dict[str, int] = {
    "Light": 1, "Moderate": 2, "Serious": 3, "Deadly": 6,
}

DAMAGE_LEVELS: list[str] = ["Light", "Moderate", "Serious", "Deadly"]

#  Sheaf trigger intervals by security code 
# interval_range = (min_increment, max_increment) between trigger steps
# first_range = (min, max) for first trigger threshold
SHEAF_INTERVALS: dict[str, dict] = {
    "Blue":   {"first_range": (5, 7), "interval_range": (4, 6)},
    "Green":  {"first_range": (4, 6), "interval_range": (3, 5)},
    "Orange": {"first_range": (3, 5), "interval_range": (2, 4)},
    "Red":    {"first_range": (2, 4), "interval_range": (1, 3)},
    "Black":  {"first_range": (2, 4), "interval_range": (1, 3)},
}

#  VR2 Security Sheaf Allocation Tables
# Tables use inclusive dice ranges. Engine rolls once, then rerolls if the result is not
# legal for the host's current security code.
SHEAF_ALERT_TABLE: dict[str, list[tuple[tuple[int, int], str]]] = {
    "none": [
        ((1, 3), "reactive_white"),
        ((4, 5), "proactive_white"),
        ((6, 7), "reactive_gray"),
        ((8, 12), "passive_alert"),
    ],
    "passive": [
        ((1, 3), "proactive_white"),
        ((4, 5), "reactive_gray"),
        ((6, 7), "proactive_gray"),
        ((8, 12), "active_alert"),
    ],
    "active": [
        ((1, 3), "proactive_gray"),
        ((4, 5), "proactive_white"),
        ((6, 7), "black_ic"),
        ((8, 12), "shutdown"),
    ],
}

SHEAF_REACTIVE_WHITE_TABLE: list[tuple[tuple[int, int], str]] = [
    ((1, 2), "Probe"),
    ((3, 5), "Trace"),
    ((6, 6), "Tar Baby"),
]

SHEAF_PROACTIVE_WHITE_TABLE: list[tuple[tuple[int, int], str]] = [
    ((2, 5), "Crippler"),
    ((6, 8), "Killer"),
    ((9, 9), "Trap Trace"),
    ((10, 10), "Trap Probe"),
    ((11, 12), "Construct/Party IC"),
]

SHEAF_REACTIVE_GRAY_TABLE: list[tuple[tuple[int, int], str]] = [
    ((1, 2), "Trap Probe"),
    ((3, 5), "Trap Trace"),
    ((6, 6), "Tar Pit"),
]

SHEAF_PROACTIVE_GRAY_TABLE: list[tuple[tuple[int, int], str]] = [
    ((2, 5), "Rippers"),
    ((6, 8), "Blaster"),
    ((9, 10), "Sparky"),
    ((11, 12), "Construct/Party IC"),
]

SHEAF_BLACK_TABLE: list[tuple[tuple[int, int], str]] = [
    ((2, 4), "Lethal"),
    ((5, 9), "Non-Lethal"),
    ((10, 12), "Construct/Party IC"),
]

SHEAF_TRAP_IC_TABLE: list[tuple[tuple[int, int], str]] = [
    ((2, 5), "Blaster"),
    ((6, 8), "Killer"),
    ((9, 11), "Sparky"),
    ((12, 12), "Black IC"),
]

SHEAF_CRIPPLER_RIPPER_TARGET_TABLE: list[tuple[tuple[int, int], str]] = [
    ((1, 2), "Bod"),
    ((3, 3), "Evasion"),
    ((4, 5), "Masking"),
    ((6, 6), "Sensor"),
]

#  Host design ranges
# sv_formula / acif_formula are dice expressions used by the frontend designer's
# Quick-Fill button. Keep formula text aligned with the range so display tips and
# generated values stay consistent.
HOST_DIFFICULTY: dict[str, dict] = {
    "Easy": {
        "sv_range": (4, 6), "sv_formula": "1D3+3",
        "subsystem_range": (8, 10), "acif_formula": "1D3+7",
        "codes": ["Blue", "Green"],
        "description": "Friendly, high-traffic system.",
    },
    "Average": {
        "sv_range": (7, 9), "sv_formula": "1D3+6",
        "subsystem_range": (11, 15), "acif_formula": "2D3+9",
        "codes": ["Green", "Orange"],
        "description": "Standard corp/government system.",
    },
    "Hard": {
        "sv_range": (8, 12), "sv_formula": "2D3+6",
        "subsystem_range": (13, 18), "acif_formula": "1D6+12",
        "codes": ["Orange", "Red"],
        "description": "High-security or Top Secret system.",
    },
}

#  Complete IC catalog 
# category: white | gray | black
# ic_type: reactive | proactive | hybrid
# subtype: crippler | ripper | trace (optional)
IC_CATALOG: dict[str, dict] = {
    "Probe": {
        "category": "white", "ic_type": "reactive",
        "summary": (
            "Makes a Probe Test (IC rating vs. Detection Factor) for every System Test "
            "the decker makes. Successes are added to the security tally. Invisible  -"
            "decker only knows it's there if they get 1 success on a sensor test against it."
        ),
    },
    "Killer": {
        "category": "white", "ic_type": "proactive",
        "summary": (
            "Attacks decker icon in cybercombat. Power = IC Rating. Damage Level from host "
            "security code (Blue=L, Green/Orange=M, Red/Black=S). Stage up 1 level per 2 attack "
            "successes. Decker resists with Bod dice vs. Power (Armor reduces Power). "
            "Fills Condition Monitor boxes. Does NOT permanently damage deck ratings."
        ),
    },
    "Acid": {
        "category": "white", "ic_type": "proactive", "subtype": "crippler",
        "targets": "Bod",
        "summary": (
            "Crippler targeting Bod. Attack Test vs. Bod rating dice. "
            "Net successes - 2 (round down) reduces Bod until logoff. Cannot reduce below 1."
        ),
    },
    "Binder": {
        "category": "white", "ic_type": "proactive", "subtype": "crippler",
        "targets": "Evasion",
        "summary": (
            "Crippler targeting Evasion. Attack Test vs. Evasion rating dice. "
            "Net successes - 2 (round down) reduces Evasion until logoff. Cannot reduce below 1."
        ),
    },
    "Jammer": {
        "category": "white", "ic_type": "proactive", "subtype": "crippler",
        "targets": "Sensor",
        "summary": (
            "Crippler targeting Sensor. Attack Test vs. Sensor rating dice. "
            "Net successes - 2 (round down) reduces Sensor until logoff. Cannot reduce below 1."
        ),
    },
    "Marker": {
        "category": "white", "ic_type": "proactive", "subtype": "crippler",
        "targets": "Masking",
        "summary": (
            "Crippler targeting Masking. Attack Test vs. Masking rating dice. "
            "Net successes - 2 (round down) reduces Masking until logoff. Cannot reduce below 1."
        ),
    },
    "Tar Baby": {
        "category": "white", "ic_type": "reactive",
        "summary": (
            "Attacks operational utilities during System Tests. Tar Baby Test (IC rating vs. "
            "utility rating as TN). If Tar Baby wins: both it and the utility crash  -"
            "decker must reload via Swap Memory."
        ),
    },
    "Data Bomb": {
        "category": "white", "ic_type": "reactive",
        "summary": (
            "Booby trap on a file or Slave device. Defuse with Computer Test vs. "
            "(Subsystem Rating - Defuse utility). If decker succeeds on accessing the "
            "protected target without defusing: explodes for (IC rating)M damage. "
            "Adds IC rating to tally. Can be suppressed."
        ),
    },
    "Scramble": {
        "category": "white", "ic_type": "reactive",
        "summary": (
            "Protects Access, Files, or Slave subsystem elements. Poison variant destroys "
            "protected data on failed decrypt. Exploding variant links to a data bomb. "
            "Defeat by decrypting (no tally increase) or crashing (adds to tally)."
        ),
    },
    "Blaster": {
        "category": "gray", "ic_type": "proactive",
        "summary": (
            "Fights like Killer IC (Armor reduces damage). If Blaster dumps the decker, "
            "makes a Blaster Test (IC Rating vs. MPCP; Hardening raises TN). "
            "Reduces MPCP by 1 per 2 successes. Permanent deck damage."
        ),
    },
    "Sparky": {
        "category": "gray", "ic_type": "proactive",
        "summary": (
            "Fights like Blaster. On persona crash: Sparky Test vs. MPCP+2 (Hardening "
            "raises TN) reduces MPCP by 1 per 2 successes, then inflicts (IC rating)M "
            "physical damage to decker's real body. Stage up 1 level per 2 successes."
        ),
    },
    "Acid-rip": {
        "category": "gray", "ic_type": "proactive", "subtype": "ripper",
        "targets": "Bod",
        "summary": (
            "Ripper targeting Bod chip. Same attack as Acid crippler but damage is permanent "
            " Ripper Test (IC Rating vs. MPCP; Hardening raises TN) reduces Bod chip rating "
            "by 1 per success. Chip replacement required."
        ),
    },
    "Bind-rip": {
        "category": "gray", "ic_type": "proactive", "subtype": "ripper",
        "targets": "Evasion",
        "summary": "Ripper targeting Evasion chip. Same attack as Binder crippler but damage is permanent "
            " Ripper Test (IC Rating vs. MPCP; Hardening raises TN) reduces Evasion chip rating "
            "by 1 per success. Chip replacement required.",
    },
    "Jam-rip": {
        "category": "gray", "ic_type": "proactive", "subtype": "ripper",
        "targets": "Sensor",
        "summary": "Ripper targeting Sensor chip. Same attack as Jam crippler but damage is permanent "
            " Ripper Test (IC Rating vs. MPCP; Hardening raises TN) reduces Sensor chip rating "
            "by 1 per success. Chip replacement required.",
    },
    "Mark-rip": {
        "category": "gray", "ic_type": "proactive", "subtype": "ripper",
        "targets": "Masking",
        "summary": "Ripper targeting Masking chip. Same attack as Marker crippler but damage is permanent "
            " Ripper Test (IC Rating vs. MPCP; Hardening raises TN) reduces Masking chip rating "
            "by 1 per success. Chip replacement required.",
    },
    "Tar Pit": {
        "category": "gray", "ic_type": "reactive",
        "summary": (
            "Operates like Tar Baby but Tar Pit Test vs. MPCP (Hardening raises TN). "
            "On zero successes, act like Tar Baby. On 1+ successes, corrupts all copies "
            "of the triggered utility in active AND storage memory. "
            "Program lost for good unless offline backup exists."
        ),
    },
    "Worm": {
        "category": "gray", "ic_type": "reactive",
        "summary": (
            "Booby traps a subsystem. Any System Test against an infected subsystem: "
            "Security Value dice vs. MPCP (Hardening raises required successes). "
            "On success: MPCP infected. Chip must be replaced. Dataworm/Deathworm/Tapeworm variants exist."
        ),
    },
    "Trace": {
        "category": "white", "ic_type": "reactive", "subtype": "trace",
        "summary": (
            "Two-phase IC. Hunt Cycle: makes Attack Tests against the decker using Trace Factor as TN "
            "until it scores a success. Location Cycle: begins after that hit; the IC becomes reactive and "
            "counts down to completing the trace. On completion, the jackpoint/location is logged and "
            "security response can escalate. Can be defeated by attacking during hunt cycle, graceful logoff, "
            "or relocate actions during location cycle."
        ),
    },
    "Black IC": {
        "category": "black", "ic_type": "proactive",
        "non_lethal_summary": (
            "Fights like Killer IC with damage level by host security code. "
            "On each successful hit, the decker makes TWO resistance tests: "
            "Willpower (biofeedback stun damage to the decker) and Bod (icon/persona damage). "
            "If rendered unconscious, connection drops automatically and the IC makes one "
            "final MPCP attack as Blaster at double rating."
        ),
        "summary": (
            "Most lethal IC. Fights like Killer IC with damage level by host security code. "
            "On each successful hit, the decker makes TWO resistance tests: "
            "Body (physical biofeedback damage to the decker) and Bod (icon/persona damage). "
            "If the icon crashes before the decker dies, connection remains and Black IC effective "
            "rating increases by +2 while the decker can only attempt jack-out. "
            "If Black IC kills the decker, connection drops and it makes one final MPCP attack as "
            "Blaster at double rating."
        ),
    },
}

#  System Operations (summary for display)
# subsystem: access | control | index | files | slave | special
SYSTEM_OPERATIONS: list[dict] = [
    {"name": "Logon to Host",       "subsystem": "access",  "utility": "Deception", "action": "Complex",
     "tip": "Opposed Access Test vs. host Access Rating. Required before any host operations."},
    {"name": "Logon to LTG",        "subsystem": "access",  "utility": "Deception", "action": "Complex",
     "tip": "Entry to the local grid. Jackpoint Access modifier applies."},
    {"name": "Analyze Host",        "subsystem": "control", "utility": "Analyze",   "action": "Complex",
     "tip": "Each success reveals one piece of info: security rating, a subsystem rating, or VM status."},
    {"name": "Analyze IC",          "subsystem": "control", "utility": "Analyze",   "action": "Free",
     "tip": "Identifies IC type, rating, options. For trace IC: reveals phase and turns remaining."},
    {"name": "Analyze Security",    "subsystem": "control", "utility": "Analyze",   "action": "Simple",
     "tip": "Reveals current security rating, your tally, and alert status. GM includes tally from this test."},
    {"name": "Locate File",         "subsystem": "index",   "utility": "Browse",    "action": "Complex",
     "tip": "Interrogation operation: accumulate 5+ successes to find the file address."},
    {"name": "Locate Paydata",      "subsystem": "index",   "utility": "Evaluate",  "action": "Complex",
     "tip": "Ongoing op. Each net success = 1 Paydata Point. Must download once located."},
    {"name": "Download Data",       "subsystem": "files",   "utility": "Read/Write","action": "Simple",
     "tip": "Ongoing op. Copies file to deck at I/O bandwidth. Terminating early corrupts the copy."},
    {"name": "Edit File",           "subsystem": "files",   "utility": "Read/Write","action": "Simple",
     "tip": "Create/modify/erase a datafile. Computer Test (TN = Files -- 2 + Masking) to hide edits."},
    {"name": "Control Slave",       "subsystem": "slave",   "utility": "Spoof",     "action": "Complex",
     "tip": "Monitored op. Takes control of a remote device. Must maintain with a Free Action every action."},
    {"name": "Null Operation",      "subsystem": "control", "utility": "Deception", "action": "Complex",
     "tip": "Idle wait. Security Value modifier increases with time: <10s base; <1m +1; <1h +2; <12h +4."},
    {"name": "Graceful Logoff",     "subsystem": "access",  "utility": "Deception", "action": "Complex",
     "tip": "Safe exit. Clears your traces. Adds trace IC rating to TN if trace is running. "
             "On success: immune to trace IC after logoff."},
    {"name": "Crash Host",          "subsystem": "control", "utility": "Crash",     "action": "Complex",
     "tip": "Successes - 10 = turns before shutdown. Host makes SV Test vs. MPCP each turn to abort. "
             "All IC 2 rating during countdown."},
    {"name": "Validate Passcode",   "subsystem": "control", "utility": "Validate",  "action": "Complex",
     "tip": "Plants a fake passcode. Grants Legitimate status in combat (+2 TN for attackers). "
             "Lasts 1D6 -- successes days."},
    {"name": "Decoy",               "subsystem": "control", "utility": "Mirrors",   "action": "Complex",
     "tip": "Creates a decoy icon. Roll 1D6 when proactive IC attacks  if < successes, IC hits decoy instead."},
    {"name": "Locate IC",           "subsystem": "index",   "utility": "Analyze",   "action": "Complex",
     "tip": "System Test only  IC auto-located on success. IC can maneuver to evade."},
    {"name": "Attack IC",           "subsystem": "combat",  "utility": "Attack",    "action": "Simple",
     "tip": "Simple Action. Roll attack utility pool. TN = host security code -- target status. "
             "Stage damage up 1 level per 2 net successes."},
]

#  Subsystem descriptions (for designer tooltips) 
SUBSYSTEM_INFO: dict[str, dict] = {
    "Access": {
        "label": "Access (A)",
        "summary": "Resists unauthorized log-on attempts. TN for all Logon Tests.",
        "tip": "Higher = harder to get in. Does NOT affect authorized users.",
    },
    "Control": {
        "label": "Control (C)",
        "summary": "Resists unauthorized manipulation of host functions.",
        "tip": "Higher = harder to crash IC, crash host, validate passcodes, or analyze security.",
    },
    "Index": {
        "label": "Index (I)",
        "summary": "Resists unauthorized data searches and file/slave location.",
        "tip": "Higher = harder to find files, paydata, IC, or slaves.",
    },
    "Files": {
        "label": "Files (F)",
        "summary": "Resists unauthorized reading, writing, or deletion of data.",
        "tip": "Higher = harder to download/edit files and tap comcalls.",
    },
    "Slave": {
        "label": "Slave (S)",
        "summary": "Resists unauthorized control of remote devices.",
        "tip": "Higher = harder to take control of cameras, doors, machinery, etc.",
    },
}

#  IC Ratings Table (vr2_rules.md) 
# Roll 2D6; columns: SV4, SV 5-7, SV 8-10, SV 11+
# Each entry: ((roll_min, roll_max), [sv_col0, sv_col1, sv_col2, sv_col3])
IC_RATINGS_TABLE: list[tuple[tuple[int, int], list[int]]] = [
    ((2,  5),  [4,  5,  6,  8]),
    ((6,  8),  [5,  7,  8,  10]),
    ((9,  11), [6,  9,  10, 11]),
    ((12, 12), [7,  10, 12, 12]),
]

#  Paydata table 
PAYDATA_TABLE: dict[str, dict] = {
    "Blue":   {"points_roll": "1D6-1",  "density_roll": "2D6x20 Mp", "base_value": 5000},
    "Green":  {"points_roll": "2D6-2",  "density_roll": "2D6x15 Mp", "base_value": 5000},
    "Orange": {"points_roll": "2D6",    "density_roll": "2D6x10 Mp", "base_value": 5000},
    "Red":    {"points_roll": "2D6+2",  "density_roll": "2D6x5 Mp",  "base_value": 5000},
    "Black":  {"points_roll": "2D6+4",  "density_roll": "3D6x5 Mp",  "base_value": 5000},
}

