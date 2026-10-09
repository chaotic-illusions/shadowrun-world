# Shadowrun World Tracker

A FastAPI + SQLite campaign management tool for **Shadowrun 2nd Edition** GMs. Tracks characters, contacts, organizations, locations, run logs, heat, faction standing, reputation, public awareness, and Matrix hosts across a living campaign world.

---

## Getting Started

These steps take you from a fresh clone to a running world with the published 2050 Seattle
setting loaded, ready for your own campaign.

### Requirements

- Git
- Docker with Docker Compose (recommended), or Python 3.12+ to run without Docker (the version the Docker image uses)

### 1. Clone the repository

```bash
git clone https://github.com/chaotic-illusions/shadowrun-world.git
cd shadowrun-world
```

### 2. Configure

Configuration comes from environment variables. With Docker Compose, the easiest way to set them
is a `.env` file next to `docker-compose.yml` (it is git-ignored, so your secrets stay local):

```bash
# .env
BOOTSTRAP_ADMIN_KEY=choose-a-first-login-password
ANTHROPIC_API_KEY=sk-ant-...        # optional, only for the AI run-narrative parser
```

| Variable | Default | Description |
|---|---|---|
| `BOOTSTRAP_ADMIN_KEY` | `shadowrunner` in Docker Compose; none when run directly | First-login admin password. `seed.py` also uses it when `--admin-token` is omitted. It stops working once the first real admin token exists. |
| `ANTHROPIC_API_KEY` | *(none)* | Anthropic API key for AI narrative parsing. Everything else works without it. |
| `CLAUDE_MODEL` | `claude-opus-5` | Claude model for the narrative parser. Docker Compose does not pass this through; add it to `docker-compose.yml` to change it there. |
| `CORS_ORIGINS` | `*` | Comma-separated allowed origins for CORS. |
| `TRUST_PROXY_HEADERS` | *(off)* | Set to `1` only behind a reverse proxy that overwrites `X-Forwarded-For` (used by the login rate limiter). |
| `DATABASE_URL` | `sqlite+aiosqlite:///./data/shadowrun.db` | SQLAlchemy async database URL. |

### 3. Start the server

```bash
docker compose up --build -d
```

The container serves the API and the web UI on port 8000, bound to `127.0.0.1` only. The database
lives in `./data/shadowrun.db` on the host, so it survives rebuilds; the tables are created on
first start. To reach it from other machines, put a reverse proxy (Apache, nginx) in front of it.

### 4. Load the world seed

A new database is empty. `data/world_seed.json` holds the starting world: the Seattle setting as
of 2050, with organizations, locations, NPCs, Regional Telecommunication Grids, and Matrix hosts,
plus their GM notes and hidden future developments. It contains no player characters.

Load it into the running container **before you log in for the first time**:

```bash
docker compose exec shadowrun-world python3 seed.py
```

The seed script authenticates with `BOOTSTRAP_ADMIN_KEY`. If you have already logged in (which
creates your real admin token and retires the bootstrap password), pass that token instead:

```bash
docker compose exec shadowrun-world python3 seed.py --admin-token YOUR_ADMIN_TOKEN
```

Only seed an empty database. Seeding adds records; it does not merge with a world you have
already been playing in.

**`reseed.sh`** (Linux) and **`reseed.bat`** (Windows) wrap this in a menu: option 1 rebuilds and
restarts the container, and option 2 **deletes the database** and reseeds from scratch.

### 5. Log in and set up access

1. Open http://localhost:8000 and log in with your `BOOTSTRAP_ADMIN_KEY` (`shadowrunner` if you
   did not set one).
2. The app replaces that password with a newly generated admin token and shows it once. Save it:
   it is your GM login from now on.
3. Create player tokens on the **Manage Tokens** page and hand them out. Players then build or
   claim their characters.

### Running without Docker

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export BOOTSTRAP_ADMIN_KEY=choose-a-first-login-password   # Windows PowerShell: $env:BOOTSTRAP_ADMIN_KEY="..."
uvicorn app.main:app --port 8000
```

Then, in a second terminal with the same `BOOTSTRAP_ADMIN_KEY` set, load the seed:

```bash
python seed.py --url http://localhost:8000
```

Without Docker there is no default bootstrap password, so set `BOOTSTRAP_ADMIN_KEY` before the
first start or you will not be able to log in.

### Updating

```bash
git pull
docker compose up --build -d
```

Your world lives in `./data/shadowrun.db` and is kept across updates. Schema changes are applied
automatically at startup. Do not reseed a world you are playing in; that wipes it. To back up,
stop the container and copy `data/shadowrun.db`.

### Maintaining the seed

Regenerate the portable seed from a trusted SQLite database with:

```bash
python seed.py --export-db data/your_world.db --file data/world_seed.json
```

The export contains the complete in-universe world state but deliberately excludes player
characters, PC-owned contacts, PC reputation and organization-standing rows, authentication data,
and transient Matrix runs. Relationships are stored by stable names and remapped to fresh IDs.

Seed order: RTGs -> Organizations -> Locations -> NPCs (+ any NPC reputation records) -> organization
relationships/divisions -> Matrix hosts -> non-PC contacts -> non-PC org standings -> Adventure Logs
-> campaign settings.

Audit descriptions, backgrounds, field notes, and nested organization prose for ingest shorthand,
source citations, raw rule blocks, and editorial instructions with:

```bash
python scripts/audit_copyable_world_text.py
```

The audit excludes player-authored PC data and PC-associated records.

### Contributing: encoding guardrails

This repo enforces text hygiene to prevent mojibake and encoding drift. One-time setup per clone:

```powershell
powershell -ExecutionPolicy Bypass -File tools/install-hooks.ps1
```

This points git's hooks path at `.githooks` and enables a pre-commit check that blocks commits if
staged text files contain a UTF-8 BOM, invalid UTF-8, mojibake markers (`\u00e2`, `\u00c3`,
`\u00c2`, replacement char), or any non-ASCII characters (strict policy). Run it manually with:

```powershell
python tools/check_text_hygiene.py --root .
```

VS Code workspace settings also set `files.encoding = utf8` and `files.autoGuessEncoding = false`.

---

## Authentication

Token-based access control with two roles:

| Role | Header | Capabilities |
|---|---|---|
| **Admin** | `X-Admin-Token` | Full read/write on all data; manage tokens; see all characters, hidden Matrix hosts, GM notes |
| **Player** | `X-User-Token` | Read-only on most data; edit own characters; see visible Matrix hosts only |

On first boot, an explicitly configured `BOOTSTRAP_ADMIN_KEY` is accepted as the admin password. After the first admin token is created, the bootstrap key is ignored. GMs create named tokens via the Manage Tokens page. Tokens are stored as SHA-256 hashes -- the plaintext is shown once at creation and never again.

Characters can be claimed by player tokens. Regenerating a token automatically reassigns all claimed characters to the new hash.

---

## Date Display

All dates are stored as real-world calendar dates. The frontend shifts the displayed year by `YEAR_OFFSET = 24` (defined in `manage-runs.html`, `world-state.js`, `deck-workshop.html`, and `matrix-designer.html`) so runs appear set in the 2050s Sixth World. The DB is never touched -- `srDate()` is display-only.

---

## Run Logging

Runs (adventure logs) can be created two ways:

1. **AI Narrative Parse** -- Paste a free-form GM session narrative. Claude extracts the title, objective, result, outcome, consequence tags, and proposes world-state changes (street cred, notoriety, PA, heat, org standings). All proposed changes are reviewed by the GM before being applied.
2. **Manual Entry** -- Fill in form fields directly: outcome, tags, participants, locations, orgs, GM notes, and world-state changes.

### Run Outcomes

| Value | Description |
|---|---|
| `success` | Team achieved objective cleanly |
| `partial_success` | Objective met with complications |
| `failure` | Run failed, team extracted |
| `critical_failure` | Catastrophic -- deaths, blown covers, major blowback |
| `abandoned` | Run called off before completion |

### Consequence Tags

Tags are narrative flavor applied to runs. They feed the **consequence engine** which generates GM-facing suggestions (e.g., "Lone Star opens investigation," "Street doc demands double rate"). Tags do not directly compute heat -- heat values are set by the GM through world-state changes on the run log or directly on the character record.

Available tags: `witnesses`, `collateral_damage`, `public_scene`, `media_attention`, `casualties`, `wetwork`, `assassination`, `magic_use`, `vehicle_chase`, `data_theft`, `extraction`, `bribery`, `false_flag`, `stealth`.

## Consequence Engine

Given a set of consequence tags from a run, the engine returns ordered GM-facing suggestions ranked by severity. It supports both single-tag triggers (e.g., `witnesses` alone) and compound triggers (e.g., `witnesses` + `public_scene` together produce a more specific consequence). Duplicate suggestions are deduplicated across rules.

This is a flavor/narrative tool -- it does not modify any game state.

### Tick System

The campaign clock counts ticks (one tick = one day in the game world). Only the GM's Downtime control advances it; logging a run does not. Ticks drive heat and public-awareness decay.

---

## Heat System

**Heat** (0-10) represents how much attention -- from law enforcement, corp security, and the shadow community -- is focused on a runner. Heat is applied directly per character by the GM via world-state changes on adventure logs or through the manage-characters page.

### Heat Tiers

| Heat | Label | Decay Half-Life |
|---|---|---|
| 0 | Neutral | inf (no decay) |
| 1-2 | Noticed | 7 days |
| 3-4 | Flagged | 10 days |
| 5-6 | Wanted | 16 days |
| 7-8 | Hot | 21 days |
| 9-10 | Nova Hot | 30 days |

Heat decays exponentially based on the current tier's half-life. Higher tiers linger longer. **Inactive PCs (lying low)** decay at 2x the normal rate.

Heat is rounded to the nearest whole value. New heat from a run adds to the *decayed* value (heat 3 that has decayed to 1, plus 2, is 3) and decay restarts from that point.

---

## Reputation

Each PC tracks three reputation values:

| Track | Range | Description |
|---|---|---|
| **Street Cred** | 0-20 | Earned by successful, skillful runs |
| **Notoriety** | 0-20 | Earned by atrocities, betrayals, collateral horror |
| **Public Awareness** | 0-13 | How recognizable you are to ordinary citizens |

**Net Rep** = `20 + street_cred - notoriety` (clamped 0-40), displayed as a tier label:

| Net Rep | Label |
|---|---|
| 0 | Infamous |
| 1 | Pariah |
| 2-4 | Feared |
| 5-7 | Dangerous |
| 8-11 | Dirty |
| 12-15 | Shady |
| 16-19 | Questionable |
| 20 | Nobody |
| 21-23 | Tested |
| 24-26 | Proven |
| 27-30 | Seasoned |
| 31-33 | Dependable |
| 34-36 | Professional |
| 37-39 | Trusted |
| 40 | Legend |

### PA Decay

Public awareness decays exponentially. The half-life depends on the current PA tier:

| PA | Label | Half-Life |
|---|---|---|
| 0 | Shadow | inf |
| 1-3 | Seen | 10 days |
| 4-7 | Recognized | 14 days |
| 8-12 | In the Spotlight | 21 days |
| 13+ | Burned | 30 days |

PA is rounded to the nearest whole value and, like heat, new PA adds to the decayed value.

---

## Faction Standing

Each character has a standing (-10 to +10) with each organization:

| Standing | Label |
|---|---|
| -10 to -7 | Hostile |
| -6 to -3 | Unfriendly |
| -2 to +2 | Neutral |
| +3 to +6 | Friendly |
| +7 to +10 | Allied |

### Ripple Effect

A standing change with org X propagates at **40%** magnitude (capped at +/-2) to X's documented allies and enemies. Allies of X gain a fraction of your delta; enemies of X lose a fraction.

### No Standing Decay

Standings don't decay with time, even for a runner who is lying low. They change only when a run changes them.

---

## AI Narrative Parsing

Requires `ANTHROPIC_API_KEY`. The parser sends the GM's narrative to Claude along with the current world context (active characters, orgs, locations) and a reference document (`docs/ai_parser_reference.md`) defining Shadowrun 2nd Edition mechanics.

Claude extracts:
- Run title, objective, result, outcome, employer
- Consequence tags
- Proposed world-state changes: `street_cred`, `notoriety`, `public_awareness`, `heat`, `org_standing` -- with per-character deltas and reasoning

All changes are **proposed only**. The GM reviews each suggestion and can accept, modify, or discard before committing the run log.

---

## Matrix Host System

The Matrix host designer generates and edits host network topologies for Shadowrun 2nd Edition's virtual reality Matrix.

### Node Types

| Abbreviation | Full Name | Role |
|---|---|---|
| CPU | Central Processing Unit | Core system controller |
| SPU | Sub-Processor Unit | Interconnect / routing |
| SAN | System Access Node | Entry point (always present) |
| DS | Datastore | File storage |
| SN | Slave Node | Device control |
| IOP | I/O Port | External interface |

The editor enforces valid connection rules between node types, and includes a chart showing valid connections between nodes (e.g., CPU connects to DS, IOP, SN, SPU, SAN; DS cannot connect directly to IOP).

### IC (Intrusion Countermeasures)

11 IC types across lethality tiers:

- **White** (defensive): Access, Barrier, Scramble
- **Gray** (damaging): Blaster, Killer, Tar Baby, Tar Pit, Trace (Trace IC has 3 subtypes; Burn, Dump, Report)
- **Black** (lethal): Black IC

In a typical system IC assignment scales with complexity and is weighted by host area -- CPUs and SANs receive more (and potentially more lethal) IC coverage.

### Host Designer

The `matrix-designer.html` page is the Matrix host editor: define each host's security code/value, intrusion difficulty, ACIFS subsystem ratings, IC sheaf (the ordered list of triggered IC), and paydata. Admins can toggle host visibility to control what players see.

---

## Frontend Pages

| Page | Description |
|---|---|
| **Login** | Authentication page -- enter access token to log in. |  *Only shown when no valid token is detected.
| **World State** | Main dashboard. Displays team heat, runner count, contacts, active orgs, locations. PC cards show reputation (street cred, notoriety, PA, heat) and faction standings. NPC/org/location cards open detail modals. Faction standings editor lets GMs adjust per-PC standings. Location cards have expandable descriptions. Admin view shows full controls; player view is scoped to owned characters. |
| **Manage Characters** | Character database. Create/edit PCs and NPCs. PCs have archetype selection (Street Samurai, Decker, Mage, etc.), reputation fields (street cred, notoriety, PA, heat), and org standings. NPCs have connection rating and contact skills. Archetype is hidden when creating NPCs. |
| **Manage Organizations** | Organization registry. Create factions with type (megacorp, syndicate, gang, government, cult, fixer network, other), threat tier (1-6), command structure, political relationships (ally/enemy links). Org type determines card border color and modal theming. |
| **Manage Locations** | Location database. Sites with security level, controlling org, district info, and descriptions. |
| **Manage RTGs** | Regional Telecommunications Grid registry. Canonical (source-book) and campaign-created nodes with security ratings (Green-3 through Black-10). Used as backbone references for Matrix host placement. |
| **Manage Runs** | Adventure log manager. Create runs via AI narrative parser or manual form. Select participants, locations, orgs. Add consequence tags and world-state changes. Browse run history with full details. |
| **Matrix Designer** | Matrix host editor. Define each host's security code/value, intrusion difficulty, ACIFS subsystem ratings, IC sheaf, and paydata. Toggle player visibility per host. |
| **Matrix Run** | Player-facing Matrix intrusion. Launch a decking run against a designed host and resolve it through the SR2 run engine, tracking persona and deck state. |
| **Manage Tokens** | Access control panel. GMs create, rename, regenerate, and revoke admin and player tokens. Token plaintext shown once at creation. |

---

## Decay Simulator

A local testing tool for verifying decay behavior:

```bash
python decay_sim.py --heat 8 --pa 7 --standing -5 --ticks 60 --step 7
python decay_sim.py --heat 6 --lying-low --ticks 30 --step 3
```

Shows per-tick (per-day) evolution of heat, PA, and standing values with tier labels, progress bars, delta arrows, and tier crossing summaries.

---

## Tech Stack

| Component | Technology |
|---|---|
| Backend | FastAPI, SQLAlchemy (async), Pydantic v2 |
| Database | SQLite via aiosqlite |
| AI Parser | Anthropic Claude (Opus 5 by default; set `CLAUDE_MODEL`) |
| Frontend | Vanilla HTML/JS/CSS -- no framework |
| Deployment | Docker + reverse proxy (Apache/nginx) |
| Auth | SHA-256 hashed tokens, rate-limited |
