# Matrix Host Generator -- Implementation Plan

Branch: `matrix-host`  
Edition: Shadowrun 2nd (geometric nodes, target numbers, Green/Blue/Orange/Red/Black security ratings)  
Status: **Spec locked -- ready to implement**

---

## Design Decisions Locked In

| Decision | Choice |
|---|---|
| Architecture | Backend generator service + frontend SVG renderer |
| Generation logic | Python service (`app/services/matrix_generator.py`) |
| Storage | New `MatrixHost` DB table, two JSON blobs per record |
| Visual output | Pure SVG, isometric 3D shapes, no external libraries |
| Node repositioning | Native SVG mouse events (drag nodes + drag-to-rewire edges) |
| Navigation | New page `frontend/manage-matrix.html` in existing nav |
| IC badges | Colored badge per IC on node; hover tooltip with mechanics + flavor |
| Edge rewiring | Click edge -> drag endpoint handle -> drop on valid node |

---

## Node Types -- Confirmed SR2 Canonical

| Code | Full Name | SR2 Flat Shape | 3D SVG Representation | Color Token |
|---|---|---|---|---|
| CPU | Central Processing Unit | Double-wall hexagon (hex inside hex) | Walled hex prism (outer hex ring + inner raised hex) | `--green` |
| SPU | Sub-Processing Unit | Hexagon | Hexagonal prism (flat-top hex with isometric depth) | `--cyan` |
| SN | Slave Node | Circle | Sphere (radial gradient + highlight) | `--amber` |
| SAN | System Access Node | Rectangle | Cuboid / box (isometric 3-face rect) | `--blue` |
| I/OP | Input/Output Port | Triangle | Pyramid (isometric 3-face triangle) | `--purple` |
| DS | Datastore | Square | Cube (isometric 3-face square) | `--text-dim` tinted |

### Valid Connection Matrix

Rows = source node type. Columns = allowed target types.

| From \ To | CPU | DS | I/OP | SN | SPU | SAN |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **CPU** | -- | [ok] | [ok] | [ok] | [ok] | [ok] |
| **DS** | [ok] | [ok] | -- | -- | [ok] | -- |
| **I/OP** | [ok] | -- | -- | -- | [ok] | -- |
| **SN** | [ok] | -- | -- | -- | [ok] | -- |
| **SPU** | [ok] | [ok] | [ok] | [ok] | [ok] | [ok] |
| **SAN** | [ok] | [ok] | -- | -- | [ok] | -- |

**Key structural rules:**
- **SPU is the universal hub** -- connects to all types including other SPUs
- **SAN is the only valid entry point** -- I/OP and SN cannot connect to SAN; all external access must route through a SAN
- **DS can chain** -- DS->DS is legal (tiered storage)
- **I/OP and SN are dead-ends** -- only route outward to CPU or SPU
- The generator enforces this matrix for both generation and drag-to-rewire validation

---

## IC Types -- Confirmed

All IC entries stored as: `{ "type": "Killer", "category": "gray", "rating": 6, "active": true }`

### White IC (non-lethal)
| Type | Mechanic summary |
|---|---|
| Access | Probes the decker's access code; kicked by failed probe |
| Barrier | Raises the host's security rating against the decker for the remainder of the run |
| Scramble | Disconnects the decker from the host immediately on trigger |

### Gray IC (conditionally lethal -- can deal damage)
| Type | Mechanic summary |
|---|---|
| Blaster | Deals Stun damage to decker's biofeedback; can KO |
| Killer | Deals Physical damage directly to decker; lethal if unaddressed |
| Tar Baby | Freezes decker in place (cannot jack out or move); must be crashed to escape |
| Tar Pit | Slows all decker actions (initiative penalty) while active |
| Trace & Report | Traces decker's physical location; reports address to system operator |
| Trace & Dump | Traces decker; forcibly disconnects (dumps) them from the host |
| Trace & Burn | Traces decker; destroys their cyberdeck's MPCP on successful trace |

**Note:** "Trace" is the parent program type. All Trace IC must carry a triggered action (Report, Dump, or Burn) -- bare "Trace" IC does not exist as a standalone type.

### Black IC (lethal)
No sub-type. Deals Physical damage (occasionally Stun at GM discretion). Typically the most aggressive and damaging IC in the host. Stored as: `{ "type": "Black", "category": "black", "rating": 8, "active": true }`

### IC Badge Visual Scheme
| Category | Badge color | Ring glow |
|---|---|---|
| White | `#e8e8e8` | None |
| Gray | `#aaaaaa` / charcoal | Faint amber |
| Black | `#ff2222` | Red pulse |

Each node shows stacked IC badges (small colored dots/rings near the node edge). Hovering an IC badge opens a tooltip showing: type name, category, rating, mechanic summary, and a one-line flavor description.

---

## Node Shape SVG Implementation

All shapes rendered at a nominal 44px bounding box, isometric projection (approx 30 deg angle).

| Type | SVG Approach |
|---|---|
| **CPU** | Outer hex ring (`<polygon>`) + inner offset hex (`<polygon>`) -- both using isometric hex prism lines for the 3D top/sides; outer ring gets a darker fill to show the "wall" |
| **SPU** | Single hexagonal prism -- top face `<polygon>` + two parallelogram side faces |
| **SN** | Sphere -- `<circle>` with radial gradient (highlight at top-left, dark at bottom-right) |
| **SAN** | Cuboid -- three `<polygon>` faces (top, left side, right side) with distinct lightness |
| **I/OP** | Pyramid -- triangular top `<polygon>` + two trapezoidal side faces |
| **DS** | Cube -- three `<polygon>` faces (top, left, right) equal-sized, isometric orientation |

All shapes use a `<defs>` gradient per color token. Selected nodes get a bright outer glow ring. IC badges are `<circle r="5">` elements positioned around the node perimeter, color-coded by lethality.

---

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
| Complexity | 1-5 | Simple / Standard / Complex / Major Corp / Black Site | Controls node count (see table) |
| Base Rating | select | Green-4 ... Black-20 | Sets IC/node ratings, colors the whole diagram |
| IC Lethality | select | White / Gray / Black | White = non-lethal only; Black = anything goes |
| Private Subnet | toggle | yes / no | Adds a second isolated cluster linked to main via a single access node |
| Owner Hint | select | Corp / Government / Criminal / Military / Unknown | Biases IC types and node flavors |
| Seed | number (optional) | any integer | Reproducible generation; blank = random |
| Name | text | -- | Host name (e.g. "Aztechnology - Seattle Payroll") |
| Owner Org | FK select | from orgs list | Optional link to organization record |
| Location | FK select | from locations list | Optional link to location record |

### Complexity -> Node Count Ranges

| Level | Name | Node Count | Notes |
|---|---|---|---|
| 1 | Simple | 5-8 | Single access node, minimal IC |
| 2 | Standard | 9-14 | Typical corporate host |
| 3 | Complex | 15-20 | Major facility or secure system |
| 4 | Major Corp | 21-30 | AAA megacorp, government |
| 5 | Black Site | 31-45 | Military, black ops, research |

---

## Open Questions / Future Ideas

```
matrix_generator.generate(config) -> topology_json
```

Steps:
1. Seed the RNG (`random.seed(config.seed or random.randint(0, 99999))`)
2. Determine total node count from complexity band (random within range)
3. Place mandatory nodes: 1x CPU at center
4. Add SPUs: `floor(node_count / 5)` minimum 1
5. Add Access Nodes based on owner_hint + has_private_subnet
6. Fill remaining budget with Storage Pools, Slave Controllers, I/O Ports weighted by owner_hint
7. Wire edges following valid connection rules; ensure the graph is fully connected
8. Place IC on nodes: Security Nodes guaranteed IC; CPU has IC above complexity 2; others by rating band
9. Calculate initial positions (radial layout -- see below)
10. If has_private_subnet: repeat steps 3-9 for private cluster; link via one access node

### Initial Node Placement (Radial Layers)
- Layer 0 (center): CPU
- Layer 1 (inner ring, r~120px): SPUs
- Layer 2 (middle ring, r~240px): Storage Pools, Slave Controllers
- Layer 3 (outer ring, r~360px): Access Nodes, I/O Ports
- Private subnet cluster: offset +/-500px from center, own identical radial layout
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

Each type is drawn with SVG primitives (isometric 3D, 44px bounding box). See "Node Shape SVG Implementation" above for full detail.

IC badges: small colored `<circle>` elements stacked around the node edge, one per IC entry, color-coded by lethality (white/gray/black). Hover tooltip shows mechanics + flavor.

---

## Node Drag / Edge Rewire (SVG Mouse Events)

No libraries needed. Two interaction modes, toggled by an "Edit Layout" button.

### Node Dragging
```js
let _drag = null; // { nodeId, offsetX, offsetY }

node.addEventListener('mousedown', e => {
  e.stopPropagation();
  const pos = svgPoint(e);
  _drag = { nodeId: id, offsetX: pos.x - node.cx, offsetY: pos.y - node.cy };
});
svg.addEventListener('mousemove', e => {
  if (!_drag) return;
  const pos = svgPoint(e);
  moveNode(_drag.nodeId, pos.x - _drag.offsetX, pos.y - _drag.offsetY);
  redrawEdges();
});
svg.addEventListener('mouseup', () => { if (_drag) { savePositions(); _drag = null; } });
```

### Edge Rewiring
Each edge `<path>` has an invisible 12px-wide hit area. Clicking an edge:
1. Selects it -- shows a drag handle circle at each endpoint
2. User drags either handle; valid drop targets highlight green, invalid targets red
3. Validation runs against the connection matrix (same table used by generator)
4. Drop on valid node -> rewires edge; drop on invalid target or empty space -> snaps back

Right-click context menu on nodes: **Add connection** (draw mode to second node) and **Delete connection** (on edge right-click, with confirm).

`savePositions()` / `saveEdges()` PATCH `/matrix-hosts/{id}` with updated `topology_json`.  
`svgPoint(e)` converts MouseEvent to SVG coordinate space (handles zoom/pan transform).

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

1. [x] Node types, shapes, connection matrix confirmed by user
2. [x] IC types and categories confirmed by user
3. [ ] Alembic migration for `matrix_hosts` table
4. [ ] `app/models/matrix_host.py`
5. [ ] `app/schemas/matrix_host.py`
6. [ ] `app/services/matrix_generator.py` -- generation algorithm
7. [ ] `app/routers/matrix_hosts.py` -- CRUD + `/generate`
8. [ ] Register router in `app/main.py`
9. [ ] `frontend/manage-matrix.html` -- form, SVG canvas, host list, drag/rewire
10. [ ] `frontend/style.css` -- isometric node styles, subnet box, IC badge colors, print media query
11. [ ] Add "Matrix" nav link to all existing HTML pages
12. [ ] Error check all modified Python files
13. [ ] Commit and push to `matrix-host` branch
14. [ ] Merge to `main` when stable

---

## Open Questions / Future Ideas

- **Claude name generation**: Optional call to generate thematic node labels (e.g. "AEGIS-CORE-7", "VAULT-DELTA") using the existing Anthropic integration -- toggle in the config form.
- **Export to print**: A "Print View" button that opens an `<iframe>` with a stripped-down version for table use.
- **Link to LTG records**: A Matrix host could be associated with an existing LTG record (host appears in the RTG viewer).
- **Multiple access nodes to a private subnet**: If complexity >= 4, allow 2 bridge nodes between public and private.
- **IC patrol paths**: Advanced -- define which IC roves between nodes rather than sitting static.
