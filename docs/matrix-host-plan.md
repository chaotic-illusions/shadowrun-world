# Matrix Host Generator — Implementation Plan

Branch: `matrix-host`  
Edition: Shadowrun 2nd (geometric nodes, target numbers, Green/Blue/Orange/Red/Black security ratings)  
Status: **Planning — not yet implemented**

---

## Design Decisions Locked In

| Decision | Choice |
|---|---|
| Architecture | Option A: Backend generator service + frontend SVG renderer |
| Generation logic | Python service (`app/services/matrix_generator.py`) |
| Storage | New `MatrixHost` DB table, two JSON blobs per record |
| Visual output | Pure SVG, rendered in-browser, no external libraries |
| Node repositioning | Native SVG mouse events (see section below) |
| Navigation | New page `frontend/manage-matrix.html` in existing nav |

---

## Pending Input From User (Required Before Coding)

1. **Node type definitions** — geometric shape descriptions and valid connections to/from each type (user to provide)
2. **IC type list** — IC names, subtypes, and abilities relevant to the campaign (user to provide)

Until these are provided, the generator will use SR2-canonical defaults (see "Node Types — SR2 Defaults" below as a starting point to confirm or correct).

---

## Data Model

```python
# app/models/matrix_host.py
class MatrixHost(Base):
    __tablename__ = "matrix_hosts"

    id              = Column(Integer, primary_key=True)
    name            = Column(String(200), nullable=False)
    owner_org_id    = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    location_id     = Column(Integer, ForeignKey("locations.id"), nullable=True)
    config_json     = Column(JSON)   # generation parameters (see Config Parameters)
    topology_json   = Column(JSON)   # nodes, edges, subnet layout (see Topology Schema)
    notes           = Column(Text)
    created_at      = Column(DateTime, default=datetime.utcnow)
    updated_at      = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

### `config_json` schema
```json
{
  "complexity":      3,
  "base_rating":     "Orange-6",
  "ic_lethality":    "gray",
  "has_private_subnet": true,
  "owner_hint":      "megacorp",
  "seed":            48291
}
```

### `topology_json` schema
```json
{
  "nodes": [
    {
      "id":     "cpu-1",
      "type":   "CPU",
      "label":  "System Core",
      "rating": 6,
      "subnet": "public",
      "ic":     [{"type": "Killer", "rating": 6}],
      "x":      400,
      "y":      300
    }
  ],
  "edges": [
    { "from": "access-1", "to": "cpu-1" }
  ],
  "subnets": [
    { "id": "public",  "label": "Public System",  "color": "#00cc33" },
    { "id": "private", "label": "Private Subnet", "color": "#bb44ff" }
  ]
}
```

---

## Configuration Parameters (Frontend Form)

| Parameter | Type | Range / Options | Description |
|---|---|---|---|
| Complexity | 1–5 | Simple / Standard / Complex / Major Corp / Black Site | Controls node count (see table) |
| Base Rating | select | Green-4 … Black-20 | Sets IC/node ratings, colors the whole diagram |
| IC Lethality | select | White / Gray / Black | White = non-lethal only; Black = anything goes |
| Private Subnet | toggle | yes / no | Adds a second isolated cluster linked to main via a single access node |
| Owner Hint | select | Corp / Government / Criminal / Military / Unknown | Biases IC types and node flavors |
| Seed | number (optional) | any integer | Reproducible generation; blank = random |
| Name | text | — | Host name (e.g. "Aztechnology – Seattle Payroll") |
| Owner Org | FK select | from orgs list | Optional link to organization record |
| Location | FK select | from locations list | Optional link to location record |

### Complexity → Node Count Ranges

| Level | Name | Node Count | Notes |
|---|---|---|---|
| 1 | Simple | 5–8 | Single access node, minimal IC |
| 2 | Standard | 9–14 | Typical corporate host |
| 3 | Complex | 15–20 | Major facility or secure system |
| 4 | Major Corp | 21–30 | AAA megacorp, government |
| 5 | Black Site | 31–45 | Military, black ops, research |

---

## Node Types — SR2 Defaults

*To be confirmed/corrected/expanded by user before implementation.*

| Node Type | SR2 Shape | Color Token | Notes |
|---|---|---|---|
| CPU | Sphere | `--green` | One per system; heart of the host |
| SPU (Sub-Processing Unit) | Cube | `--red` | One or more; controls subsystems |
| Storage Pool | Cylinder | `--cyan` | Data files live here |
| Access Node | Inverted triangle / pyramid | `--amber` | Entry points; public-facing |
| I/O Port | Flat disc / torus | `--blue` | Physical-world interfaces |
| Slave Controller | Hexagon | `--purple` | Controls slave devices (cameras, doors, etc.) |
| Datastore | Rectangle | `--text-dim` | Active data; different from passive Storage Pool |
| Security Node | Octahedron / star | `--red` variant | Houses IC directly |

### Valid Connection Rules (SR2 defaults — confirm with user)
- Access Node → CPU, SPU
- CPU → SPU, Storage Pool, I/O Port, Slave Controller, Datastore
- SPU → Storage Pool, Slave Controller, I/O Port
- Storage Pool → CPU (read only)
- Private subnet connects to public only via one dedicated Access Node

---

## IC Types — SR2 Defaults

*To be confirmed/corrected/expanded by user before implementation.*

**White IC** (non-lethal)
- Probe — detects intruders
- Trace — locates decker
- Scramble — disconnects decker
- Tar Baby — halts/slows intrusion

**Gray IC** (conditionally lethal)
- Sparky — deals Stun damage
- Blaster — deals Physical damage
- Marker — marks/traces permanently

**Black IC** (lethal)
- Killer — deals Physical damage, can kill
- Blackout — crashes and destroys
- Hellhound — pursuit IC, follows decker
- Lethal Tar Baby — holds and escalates damage

Each IC entry in a node stores: `{ "type": "Killer", "rating": 6, "active": true }`

---

## Generation Algorithm (Backend Service)

```
matrix_generator.generate(config) → topology_json
```

Steps:
1. Seed the RNG (`random.seed(config.seed or random.randint(0, 99999))`)
2. Determine total node count from complexity band (random within range)
3. Place mandatory nodes: 1× CPU at center
4. Add SPUs: `floor(node_count / 5)` minimum 1
5. Add Access Nodes based on owner_hint + has_private_subnet
6. Fill remaining budget with Storage Pools, Slave Controllers, I/O Ports weighted by owner_hint
7. Wire edges following valid connection rules; ensure the graph is fully connected
8. Place IC on nodes: Security Nodes guaranteed IC; CPU has IC above complexity 2; others by rating band
9. Calculate initial positions (radial layout — see below)
10. If has_private_subnet: repeat steps 3–9 for private cluster; link via one access node

### Initial Node Placement (Radial Layers)
- Layer 0 (center): CPU
- Layer 1 (inner ring, r≈120px): SPUs
- Layer 2 (middle ring, r≈240px): Storage Pools, Slave Controllers
- Layer 3 (outer ring, r≈360px): Access Nodes, I/O Ports
- Private subnet cluster: offset ±500px from center, own identical radial layout
- Subnet boundary box auto-calculated from node positions + 60px padding

---

## SVG Renderer (Frontend)

File: `frontend/manage-matrix.html`  
No external libraries. Pure SVG + vanilla JS.

### Rendering
- SVG `<g>` elements per node, each containing shape + label + IC badges
- `<line>` or `<path>` per edge
- `<rect>` dashed outline per subnet boundary
- Zoom/pan: `transform="scale(z) translate(x,y)"` on root `<g>`, mouse wheel + click-drag on canvas background
- Print: `@media print` CSS hides controls, forces white-on-black or fitting

### Node Shape Rendering
Each type is drawn with SVG primitives (all sizes relative to a 40px radius):

| Type | SVG Element |
|---|---|
| CPU | `<circle>` with glow filter |
| SPU | `<rect>` (square, rotated 45° = diamond) |
| Storage Pool | `<rect>` tall-narrow (cylinder approximation) |
| Access Node | `<polygon points>` triangle |
| I/O Port | `<ellipse>` (disc) |
| Slave Controller | `<polygon points>` hexagon |
| Security Node | `<polygon points>` 8-point star |

IC badges: small colored rings `<circle stroke-only>` stacked around the node edge, one per IC entry, color-coded by lethality tier.

---

## Node Drag-and-Drop (SVG Mouse Events)

No libraries needed. Implementation pattern:

```js
let _drag = null; // { nodeId, offsetX, offsetY }

// On each node <g>:
node.addEventListener('mousedown', e => {
  e.stopPropagation();
  const pos = svgPoint(e);
  _drag = { nodeId: id, offsetX: pos.x - node.cx, offsetY: pos.y - node.cy };
});

// On SVG canvas:
svg.addEventListener('mousemove', e => {
  if (!_drag) return;
  const pos = svgPoint(e);
  moveNode(_drag.nodeId, pos.x - _drag.offsetX, pos.y - _drag.offsetY);
  redrawEdges(); // update all line endpoints
});

svg.addEventListener('mouseup', () => {
  if (_drag) { savePositions(); _drag = null; }
});
```

`savePositions()` PATCHes `/matrix-hosts/{id}` with updated `topology_json` (only x/y changed).  
`svgPoint(e)` converts MouseEvent coords to SVG coordinate space (handles zoom/pan).

Estimated implementation: ~100 lines of JS within the page.

---

## Backend Files to Create

| File | Purpose |
|---|---|
| `app/models/matrix_host.py` | SQLAlchemy model |
| `app/schemas/matrix_host.py` | Pydantic schemas (Create, Update, Read) |
| `app/routers/matrix_hosts.py` | CRUD + `/generate` endpoint |
| `app/services/matrix_generator.py` | Core generation algorithm |

### API Endpoints
```
GET    /matrix-hosts/           list all hosts
POST   /matrix-hosts/           create (manual, no generation)
POST   /matrix-hosts/generate   generate topology from config, save and return
GET    /matrix-hosts/{id}       get one host
PATCH  /matrix-hosts/{id}       update (used to save repositioned nodes)
DELETE /matrix-hosts/{id}       delete
```

### Router Registration
In `app/main.py`, add:
```python
from app.routers import matrix_hosts
app.include_router(matrix_hosts.router, prefix="/matrix-hosts", tags=["matrix-hosts"])
```

---

## Frontend Files to Create / Modify

| File | Change |
|---|---|
| `frontend/manage-matrix.html` | New page: generator form + SVG canvas + host list |
| `frontend/style.css` | Add matrix-specific CSS (node colors, subnet box, print styles) |
| `frontend/shared.js` | No changes expected |
| All HTML pages `<nav>` | Add `<a href="manage-matrix.html">Matrix</a>` link |

---

## Migration Required

A new migration script is needed to add the `matrix_hosts` table:

```python
# add_matrix_hosts.py  (run once, then delete)
conn.execute("""
    CREATE TABLE IF NOT EXISTS matrix_hosts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        owner_org_id INTEGER REFERENCES organizations(id) ON DELETE SET NULL,
        location_id INTEGER REFERENCES locations(id) ON DELETE SET NULL,
        config_json TEXT,
        topology_json TEXT,
        notes TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
```

---

## Implementation Order

1. [ ] Receive node type definitions from user — update "Node Types" section above
2. [ ] Receive IC type list from user — update "IC Types" section above
3. [ ] Run migration (`add_matrix_hosts.py`)
4. [ ] `app/models/matrix_host.py`
5. [ ] `app/schemas/matrix_host.py`
6. [ ] `app/services/matrix_generator.py` — generation algorithm
7. [ ] `app/routers/matrix_hosts.py` — CRUD + `/generate`
8. [ ] Register router in `app/main.py`
9. [ ] `frontend/manage-matrix.html` — form, SVG canvas, host list, drag-and-drop
10. [ ] `frontend/style.css` — matrix node/subnet styles, print media query
11. [ ] Add "Matrix" nav link to all existing HTML pages
12. [ ] Error check all modified Python files
13. [ ] Commit and push to `matrix-host` branch
14. [ ] Merge to `main` when stable

---

## Open Questions / Future Ideas

- **Claude name generation**: Optional call to generate thematic node labels (e.g. "AEGIS-CORE-7", "VAULT-DELTA") using the existing Anthropic integration — toggle in the config form.
- **Export to print**: A "Print View" button that opens an `<iframe>` with a stripped-down version for table use.
- **Link to LTG records**: A Matrix host could be associated with an existing LTG record (host appears in the RTG viewer).
- **Multiple access nodes to a private subnet**: If complexity ≥ 4, allow 2 bridge nodes between public and private.
- **IC patrol paths**: Advanced — define which IC roves between nodes rather than sitting static.
