# Adventure spec contract (compact)

One Python module per adventure in `scripts/adventure_ingest/specs/<slug>.py`. ASCII only (no em dashes, curly quotes, currency glyphs, accents, ellipsis characters; write `--` and "nuyen"). Module-level names:

```
ADVENTURE = "<exact title from frontend/shared.js ADVENTURE_ORDER>"
ORDER = <int>            # campaign order
SOURCE = "<pdf name>, pp. a-b"
YEAR = "2053 (May)"      # in-world date; year alone if unsure
SYNOPSIS = """markdown, 2-4 paragraphs, bold the key names"""
TIMELINE = """markdown bullets"""
ORGS = [ {...} ]          # created rows
LOCATIONS = [ {...} ]
NPCS = [ {...} ]
ORG_UPDATES = { "<exact existing name>": {...} }   # appends to existing rows
LOC_UPDATES = { ... }
NPC_UPDATES = { ... }
TAG_EXISTING = {}         # leave empty
MATRIX_HOSTS = """markdown: one node table per mapped system (node | function | color-rating | IC)"""
NOT_BUILT = """markdown bullets: name-drops and stat blocks folded into other rows"""
PLAY_NOTES = """markdown bullets for the GM"""
```

## Row dicts (all strings ASCII; omit keys you do not need)

ORG: `name` (<=200), `org_type` (<=100; e.g. corporation, go-gang, gang, policlub, cult, tribe, nation-state, government agency, media, mystical fellowship), `affiliation_contact_type` (optional, e.g. "Gang"), `tier` (1 street .. 5 megacorp/nation), `headquarters` (<=200), `summary` (one line), `description` (paragraph), `leadership` ([{"name","title","notes"}]), `notes` (stat blocks, plot role, aftermath), `allies` / `enemies` (lists of org names).

LOCATION: `name` (<=200), `location_type` (<=100; prefer: nightclub, bar, restaurant, casino, btl den, brothel, corporate facility, corporate headquarters, corporate megastructure, research lab, data center, corporate arcology, commercial district, convenience store, mall, street market, pawn shop, black market, residential community, apartment complex, squatter camp, subterranean community, penthouse, government building, military installation, police station, hospital, transportation hub, power plant, gang territory, safehouse, smugglers den, underground bunker, landmark / restaurant, landmark / monument, ruins, hotel, shop; short custom strings allowed), `city` (<=100; default Seattle), `district` (<=100), `security_level` (one of: "Corporate Extraterritorial", "Corporate High Security", "Corporate Standard", "Patrolled / Commercial", "Low Security", "No Security / Barrens", "Zero Zone -- Lethal Response"), `controlling_org` (org name), `summary`, `description`, `notes`.

NPC: `name` (<=200), `role` (one line, doc only), `archetype` (<=100), `title` (<=200), `race` (<=50), `gender` (<=50), `age` (int), `nationality` (<=100), `organization` (org name; omitted = independent), `connection` (1-6), `description`, `background`, `notes` (short stat summary: attributes line, key skills, cyberware, gear, spells, Threat/Force), `contact_skills` (list of strings).

## Update dicts (append-only; prefix appended text with "<Adventure>: ")

ORG_UPDATES value keys: `notes_append`, `description_append`, `leadership_add` (list of {name,title,notes}; deduped by name), `allies_add`, `enemies_add` (lists of org names), `set` (verbatim field overrides -- only to fix a clear error).
LOC_UPDATES value keys: `notes_append`, `description_append`, `set`. Do not relink `controlling_org`.
NPC_UPDATES value keys: `notes_append`, `background_append`, `description_append`, `contact_skills_add`, `set`. Do not relink `organization`.

## Depth checklist (the campaign owner compares every spec against the early ones)
- NPC `description`: looks, dress, manner, speech, and a quote where the book gives one (typically 250-400 chars).
- NPC `background`: present for everyone the book gives any history to.
- NPC `notes`: opens with the short stat summary (attributes line, key skills, cyberware, gear, spells, Threat/Force), then plot role, tactics, aftermath (typically 400-600 chars).
- Location `description`: the full paragraph the book gives -- layout, atmosphere, staff, security (typically 500-800 chars); `notes` carry map references, security stats, plot use.
- Org `description` + `notes`: what it is, who runs it, stat blocks of its typical members, its role and aftermath.
- Generosity: named single-scene people and places still get short, real rows; only nameless archetypes go to NOT_BUILT.

## Rules
- Be generous: any named person with a role and a place gets an NPC row; named bars/hotels/shops/facilities get location rows; gangs/corps/cults/agencies/tribes/nations get org rows. Pure name-drops go in NOT_BUILT.
- Earlier books are canon. Contradictions with existing rows go into notes_append as a flagged discrepancy, never a rewrite.
- Existing rows (see the production name dump) are updated by exact name, never re-created. Orgs/locations created by other specs in `specs/` count as existing.
- Matrix hosts are documented in MATRIX_HOSTS, never built.
- Note the book's own editing inconsistencies in a header comment and on the affected rows.

## Validate (repo root; env `SR_ADMIN_TOKEN` set)
```
python scripts/adventure_ingest/run.py <slug> --dry     # "org not found: X" for orgs the spec/other specs create is expected
python scripts/adventure_ingest/check_lengths.py <slug>
```
Then eyeball `docs/adventure-prep/<NN>-<slug>.md`. Do not load without --dry, commit, or push.
