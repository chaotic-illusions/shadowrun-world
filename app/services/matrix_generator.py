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
        "summary": "Probes the intruder's access code. Invalid access code triggers immediate counter-intrusion response.",
        "flavor": "Manifests as a security guard icon scanning the node entry point, or a shimmering doorway leading further into the system.",
    },
    "Barrier": {
        "summary": "Blocks data signals to the node, unless permission is given from outside the system.  Must be crashed/sleazed to pass.",
        "flavor": "Appears as a crackling energy wall or hardened vault door sealing across the datapath.",
    },
    "Scramble": {
        "summary": "Destructive IC that protects data. Crash it or copy the file with it.  Fail, and the file is gone.",
        "flavor": "A halo of light, or a tightly coiled snake wrapped around the datastore.",
    },
    "Blaster": {
        "summary": "Don't let this stuff your Persona or it can burn out your decks MPCP chips.",
        "flavor": "A warrior, soldier, attack drone, or thunderstorm imagery are common. They have big weapons, and bright lightning",
    },
    "Killer": {
        "summary": "This IC attacks and damages your Persona, trying to crash you out.",
        "flavor": "A warrior, soldier, attack drone, or thunderstorm imagery are common — fast, aggressive, relentless.",
    },
    "Tar Baby": {
        "summary": "Trap IC.  It'll self-crash and take your program with it.",
        "flavor": "Concealed until activation, then a trap, pit, pool, or snare imagery.",
    },
    "Tar Pit": {
        "summary": "Trap IC.  It'll self-crash like Tar Baby, but also corrupt every copy of your program on your deck.",
        "flavor": "Concealed until activation, then a trap, pit, pool, or snare imagery.",
    },
    "Trace & Report": {
        "summary": "Traces the decker's physical location and reports the address to the system operator before going dormant.",
        "flavor": "A bloodhound circling the decker's persona, nose to the datastream.",
    },
    "Trace & Dump": {
        "summary": "Traces the decker's physical location, then forcibly ejects them from the system.",
        "flavor": "A bloodhound that circles the decker's persona, locks on — then detonates, exploding your view in spectacular white static as you're dumped out of the system.",
    },
    "Trace & Burn": {
        "summary": "Traces the decker's location, then attacks the deck's MPCP at the node of entry.  Hope you brought backup.",
        "flavor": "A wolf sniffing the datastream.  A pack manifests at your entry point, destroying your Matrix tether.",
    },
    "Black": {
        "summary": "Deals Physical damage (occasionally Stun, GM discretion). Most lethal IC in the host. No sub-type.",
        "flavor": "Unknown. Changes form each time it manifests. Some deckers report it wearing their own face, pursuing them relentlessly through the system.",
    },
}

