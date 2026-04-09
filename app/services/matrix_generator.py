"""
Matrix host static reference data for Shadowrun 2nd Edition.

Provides IC type metadata (IC_INFO) and the canonical node connection rules
(VALID_CONNECTIONS) used by the frontend topology editor.
"""

# ── Connection matrix ───────────────────────────────────────────────────────
# VALID_CONNECTIONS[source_type] = set of valid target types
VALID_CONNECTIONS: dict[str, set[str]] = {
    "CPU":  {"DS", "IOP", "SN", "SPU", "SAN"},
    "DS":   {"CPU", "DS", "SPU"},
    "IOP":  {"CPU", "SPU"},
    "SN":   {"CPU", "SPU"},
    "SPU":  {"CPU", "DS", "IOP", "SN", "SPU", "SAN"},
    "SAN":  {"CPU", "DS", "SPU"},
}

# ── IC catalogue ────────────────────────────────────────────────────────────
IC_BY_LETHALITY: dict[str, list[str]] = {
    "white": ["Access", "Barrier", "Scramble"],
    "gray":  ["Blaster", "Killer", "Tar Baby", "Tar Pit",
              "Trace & Report", "Trace & Dump", "Trace & Burn"],
    "black": ["Black"],
}

IC_CATEGORY: dict[str, str] = {}
for _cat, _types in IC_BY_LETHALITY.items():
    for _t in _types:
        IC_CATEGORY[_t] = _cat

# IC tooltips: { type: { "summary": str, "flavor": str } }
IC_INFO: dict[str, dict[str, str]] = {
    "Access": {
        "summary": "Probes the intruder's access code. Failed probe triggers immediate counter-intrusion.",
        "flavor": "Manifests as a security guard icon scanning the node entry point.",
    },
    "Barrier": {
        "summary": "On trigger, raises the host's effective security rating by its own rating for the remainder of the run.",
        "flavor": "Appears as a crackling energy wall or hardened vault door sealing across the datapath.",
    },
    "Scramble": {
        "summary": "Disconnects the decker from the host immediately. Causes no damage but terminates the run.",
        "flavor": "A sudden static burst — the Matrix dissolves into white noise and the decker is expelled.",
    },
    "Blaster": {
        "summary": "Deals Stun damage to the decker via biofeedback. Can incapacitate if damage accumulates.",
        "flavor": "An arc of blue-white electricity that strikes the decker's icon before grounding out.",
    },
    "Killer": {
        "summary": "Deals Physical damage directly to the decker. Lethal if not crashed quickly.",
        "flavor": "Appears as a bladed weapon or predatory animal — fast, aggressive, relentless.",
    },
    "Tar Baby": {
        "summary": "Freezes movement — the decker cannot jack out or relocate until the IC is crashed.",
        "flavor": "A viscous, jet-black mass that encases the decker's icon, pulsing as it tightens.",
    },
    "Tar Pit": {
        "summary": "Reduces the decker's initiative by its rating while active. Does not freeze but slows all actions.",
        "flavor": "The surrounding Matrix geometry thickens and distorts — every movement costs twice the effort.",
    },
    "Trace & Report": {
        "summary": "Traces the decker's physical location and reports the address to the system operator. No immediate disconnect.",
        "flavor": "A bloodhound icon circling the decker's persona, nose to the datastream.",
    },
    "Trace & Dump": {
        "summary": "Traces the decker's location, then forcibly ejects them from the host.",
        "flavor": "The bloodhound locks on — then detonates, hurling the decker's icon out of the system.",
    },
    "Trace & Burn": {
        "summary": "Traces the decker's location, then destroys the deck's MPCP on a successful trace roll.",
        "flavor": "Leaves a searing afterimage as it burns the decker's access path back to the hardware.",
    },
    "Black": {
        "summary": "Deals Physical damage (occasionally Stun, GM discretion). Most lethal IC in the host. No sub-type.",
        "flavor": "Unknown. Changes form each time it manifests. Some deckers report it wearing their own face.",
    },
}

