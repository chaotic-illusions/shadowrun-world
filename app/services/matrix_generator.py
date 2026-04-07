"""
Matrix Host Generator for Shadowrun 2nd Edition.

Generates a topology_json dict describing nodes, edges, and subnets for a matrix host,
following SR2 canonical node types and the validated connection matrix.
"""
import random
import math
from typing import Any

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

# ── Complexity bands ─────────────────────────────────────────────────────────
COMPLEXITY_BANDS = {
    1: (5,  8),   # Simple
    2: (9,  14),  # Standard
    3: (15, 20),  # Complex
    4: (21, 30),  # Major Corp
    5: (31, 45),  # Black Site
}

# ── Owner hint biases for node type distribution ─────────────────────────────
# Weights for filling non-mandatory nodes (after CPU, SPU, SAN placed)
FILL_NODE_WEIGHTS: dict[str, dict[str, int]] = {
    "corp":       {"DS": 35, "SN": 25, "IOP": 15, "SPU": 15, "SAN": 10},
    "government": {"DS": 25, "SN": 30, "IOP": 20, "SPU": 10, "SAN": 15},
    "criminal":   {"DS": 20, "SN": 15, "IOP": 30, "SPU": 20, "SAN": 15},
    "military":   {"DS": 20, "SN": 35, "IOP": 15, "SPU": 15, "SAN": 15},
    "unknown":    {"DS": 25, "SN": 20, "IOP": 20, "SPU": 20, "SAN": 15},
}

# ── Rating string → numeric ──────────────────────────────────────────────────
def _parse_rating(base_rating: str) -> int:
    """Extract the numeric rating from strings like 'Orange-6'."""
    try:
        return int(base_rating.split("-")[-1])
    except (ValueError, IndexError):
        return 6


def _rating_color(base_rating: str) -> str:
    tier = base_rating.split("-")[0].lower()
    return {
        "green":  "#00cc33",
        "blue":   "#3388ff",
        "orange": "#ff8800",
        "red":    "#ff2222",
        "black":  "#cc00ff",
    }.get(tier, "#00cc33")


# ── IC selection ─────────────────────────────────────────────────────────────
def _available_ic(ic_lethality: str) -> list[str]:
    """Return all IC types available for a given max lethality."""
    pool = list(IC_BY_LETHALITY["white"])
    if ic_lethality in ("gray", "black"):
        pool += IC_BY_LETHALITY["gray"]
    if ic_lethality == "black":
        pool += IC_BY_LETHALITY["black"]
    return pool


def _pick_ic(rng: random.Random, rating: int, ic_lethality: str,
             node_type: str, complexity: int) -> list[dict]:
    """Return 0–2 IC entries for a node based on type and complexity."""
    pool = _available_ic(ic_lethality)
    ic_list = []

    # CPU always gets IC at complexity ≥ 2
    if node_type == "CPU" and complexity >= 2:
        count = min(2, 1 + (complexity // 3))
    # SANs (entry points) always get at least one IC
    elif node_type == "SAN":
        count = 1 + (1 if complexity >= 3 else 0)
    # DS and SPU get IC at higher complexities
    elif node_type in ("DS", "SPU") and complexity >= 3:
        count = 1 if rng.random() < 0.5 else 0
    elif node_type in ("SN", "IOP") and complexity >= 4:
        count = 1 if rng.random() < 0.4 else 0
    else:
        count = 0

    # Prefer higher-lethality IC for CPU/SAN on lethal hosts
    if ic_lethality == "black" and node_type in ("CPU", "SAN"):
        preferred = [t for t in pool if IC_CATEGORY.get(t) in ("gray", "black")]
        if preferred:
            pool = preferred

    seen = set()
    for _ in range(count):
        candidates = [t for t in pool if t not in seen]
        if not candidates:
            break
        ic_type = rng.choice(candidates)
        seen.add(ic_type)
        ic_list.append({
            "type": ic_type,
            "category": IC_CATEGORY.get(ic_type, "white"),
            "rating": rating,
            "active": True,
        })
    return ic_list


# ── Isometric radial layout ──────────────────────────────────────────────────
def _radial_positions(nodes: list[dict], cx: float = 500, cy: float = 400) -> None:
    """Assign x/y to nodes using a layered radial layout."""
    layers: dict[str, list[dict]] = {"CPU": [], "SPU": [], "MID": [], "OUTER": []}
    for n in nodes:
        t = n["type"]
        if t == "CPU":
            layers["CPU"].append(n)
        elif t == "SPU":
            layers["SPU"].append(n)
        elif t in ("DS", "SN"):
            layers["MID"].append(n)
        else:  # SAN, IOP
            layers["OUTER"].append(n)

    radii = {"CPU": 0, "SPU": 130, "MID": 260, "OUTER": 390}

    for layer_key, layer_nodes in layers.items():
        r = radii[layer_key]
        count = len(layer_nodes)
        if count == 0:
            continue
        if r == 0:
            layer_nodes[0]["x"] = cx
            layer_nodes[0]["y"] = cy
            continue
        for i, node in enumerate(layer_nodes):
            angle = (2 * math.pi * i / count) - math.pi / 2
            node["x"] = round(cx + r * math.cos(angle))
            node["y"] = round(cy + r * math.sin(angle))


def _subnet_radial_positions(nodes: list[dict], cx: float = 1100, cy: float = 400) -> None:
    """Same layout for the private subnet cluster, offset to the right."""
    _radial_positions(nodes, cx=cx, cy=cy)


# ── Graph connectivity ───────────────────────────────────────────────────────
def _wire_edges(rng: random.Random, nodes: list[dict]) -> list[dict[str, str]]:
    """
    Build a connected edge list following VALID_CONNECTIONS.
    Strategy:
    1. Build a spanning tree from CPU outward via SPU hubs
    2. Add extra edges to ensure each node has at least one connection
    """
    id_map = {n["id"]: n for n in nodes}
    edges: list[dict[str, str]] = []
    connected: set[str] = set()

    def add_edge(a: str, b: str) -> bool:
        ta, tb = id_map[a]["type"], id_map[b]["type"]
        if tb in VALID_CONNECTIONS.get(ta, set()) and \
           ta in VALID_CONNECTIONS.get(tb, set()):
            edge = {"from": a, "to": b}
            rev  = {"from": b, "to": a}
            if edge not in edges and rev not in edges:
                edges.append(edge)
                connected.add(a)
                connected.add(b)
                return True
        return False

    cpu_nodes  = [n for n in nodes if n["type"] == "CPU"]
    spu_nodes  = [n for n in nodes if n["type"] == "SPU"]
    san_nodes  = [n for n in nodes if n["type"] == "SAN"]
    rest       = [n for n in nodes if n["type"] not in ("CPU", "SPU", "SAN")]

    # CPU ↔ each SPU
    for spu in spu_nodes:
        add_edge(cpu_nodes[0]["id"], spu["id"])

    # SAN ↔ CPU
    for san in san_nodes:
        add_edge(san["id"], cpu_nodes[0]["id"])
        # SAN also gets a SPU link if available
        if spu_nodes:
            add_edge(san["id"], rng.choice(spu_nodes)["id"])

    # Remaining nodes: attach to CPU or random SPU that accepts them
    hubs = cpu_nodes + spu_nodes
    rng.shuffle(rest)
    for node in rest:
        rng.shuffle(hubs)
        for hub in hubs:
            if add_edge(node["id"], hub["id"]):
                break

    # Ensure fully connected — any orphan gets linked to a random valid hub
    for node in nodes:
        if node["id"] not in connected:
            rng.shuffle(hubs)
            for hub in hubs:
                if hub["id"] != node["id"] and add_edge(node["id"], hub["id"]):
                    break

    return edges


# ── Node label generation ─────────────────────────────────────────────────────
_LABEL_PREFIXES: dict[str, list[str]] = {
    "CPU":  ["CORE", "NEXUS", "APEX", "MAINFRAME", "SYSTEM"],
    "SPU":  ["PROC", "UNIT", "ENGINE", "MODULE", "CLUSTER"],
    "DS":   ["VAULT", "ARCHIVE", "STORE", "REPO", "BANK"],
    "SAN":  ["ACCESS", "GATE", "PORTAL", "ENTRY", "NODE"],
    "IOP":  ["PORT", "LINK", "BRIDGE", "RELAY", "CHANNEL"],
    "SN":   ["SLAVE", "PUPPET", "PROXY", "DEVICE", "AGENT"],
}

def _make_label(rng: random.Random, node_type: str, index: int) -> str:
    prefix = rng.choice(_LABEL_PREFIXES.get(node_type, ["NODE"]))
    return f"{prefix}-{index:02d}"


# ── Main generator ────────────────────────────────────────────────────────────
def generate(config: dict[str, Any]) -> dict[str, Any]:
    """
    Generate a topology_json dict from a config_json dict.

    Args:
        config: MatrixHostConfig-shaped dict

    Returns:
        topology_json: { nodes, edges, subnets }
    """
    rng = random.Random(config.get("seed") or random.randint(0, 999999))

    complexity   = max(1, min(5, int(config.get("complexity", 2))))
    base_rating  = config.get("base_rating", "Orange-6")
    ic_lethality = config.get("ic_lethality", "gray")
    has_private  = bool(config.get("has_private_subnet", False))
    owner_hint   = config.get("owner_hint", "corp")

    rating       = _parse_rating(base_rating)
    rating_color = _rating_color(base_rating)
    lo, hi       = COMPLEXITY_BANDS[complexity]
    node_count   = rng.randint(lo, hi)

    weights      = FILL_NODE_WEIGHTS.get(owner_hint, FILL_NODE_WEIGHTS["unknown"])
    fill_types   = list(weights.keys())
    fill_weights = list(weights.values())

    # ── Build public subnet nodes ──────────────────────────────────────────
    public_nodes: list[dict] = []
    counters: dict[str, int] = {}

    def make_node(ntype: str, subnet: str) -> dict:
        counters[ntype] = counters.get(ntype, 0) + 1
        idx = counters[ntype]
        return {
            "id":     f"{ntype.lower().replace('/', '')}-{idx}",
            "type":   ntype,
            "label":  _make_label(rng, ntype, idx),
            "rating": rating,
            "subnet": subnet,
            "ic":     _pick_ic(rng, rating, ic_lethality, ntype, complexity),
            "x":      0,
            "y":      0,
        }

    # Mandatory: 1 CPU
    public_nodes.append(make_node("CPU", "public"))

    # SPUs: floor(node_count / 5), minimum 1
    n_spu = max(1, node_count // 5)
    for _ in range(n_spu):
        public_nodes.append(make_node("SPU", "public"))

    # At least 1 SAN (entry point)
    n_san = 1 + (1 if complexity >= 3 else 0)
    for _ in range(n_san):
        public_nodes.append(make_node("SAN", "public"))

    # Fill remaining budget
    budget = node_count - len(public_nodes)
    for _ in range(budget):
        t = rng.choices(fill_types, weights=fill_weights, k=1)[0]
        public_nodes.append(make_node(t, "public"))

    # Positions + edges
    _radial_positions(public_nodes)
    public_edges = _wire_edges(rng, public_nodes)

    subnets = [{"id": "public", "label": "Public System", "color": rating_color}]

    all_nodes = list(public_nodes)
    all_edges = list(public_edges)

    # ── Optional private subnet ────────────────────────────────────────────
    if has_private:
        priv_lo, priv_hi = max(3, lo // 2), max(5, hi // 2)
        priv_count = rng.randint(priv_lo, priv_hi)

        private_nodes: list[dict] = []
        private_nodes.append(make_node("CPU", "private"))
        n_priv_spu = max(1, priv_count // 5)
        for _ in range(n_priv_spu):
            private_nodes.append(make_node("SPU", "private"))
        priv_budget = priv_count - len(private_nodes)
        for _ in range(priv_budget):
            t = rng.choices(fill_types, weights=fill_weights, k=1)[0]
            private_nodes.append(make_node(t, "private"))

        _subnet_radial_positions(private_nodes)
        private_edges = _wire_edges(rng, private_nodes)

        # Bridge: one SAN in the public subnet connects to the private CPU
        pub_sans = [n for n in public_nodes if n["type"] == "SAN"]
        bridge_san = rng.choice(pub_sans) if pub_sans else public_nodes[0]
        priv_cpu   = next(n for n in private_nodes if n["type"] == "CPU")
        bridge_edge = {"from": bridge_san["id"], "to": priv_cpu["id"], "bridge": True}

        all_nodes  += private_nodes
        all_edges  += private_edges + [bridge_edge]
        subnets.append({"id": "private", "label": "Private Subnet", "color": "#bb44ff"})

    return {
        "nodes":   all_nodes,
        "edges":   all_edges,
        "subnets": subnets,
    }
