# Shadowrun World Tracker

A FastAPI + SQLite campaign management tool for **Shadowrun 2nd Edition** GMs. Tracks characters, contacts, organizations, locations, run logs, heat, faction standing, reputation, public awareness, and Matrix hosts across a living campaign world.

---

## Setup

### Requirements
- Python 3.11+
- Docker (recommended for deployment)

### Environment Variables

| Variable | Default | Description |
|---|---|---|
| `BOOTSTRAP_ADMIN_KEY` | `shadowrunner` | Initial admin password for first login and `seed.py` |
| `ANTHROPIC_API_KEY` | *(none)* | Anthropic API key for AI narrative parsing |
| `CLAUDE_MODEL` | `claude-sonnet-4-6` | Claude model for the narrative parser |
| `CORS_ORIGINS` | `*` | Comma-separated allowed origins for CORS |
| `DATABASE_URL` | `sqlite+aiosqlite:///./data/shadowrun.db` | SQLAlchemy async database URL |

### Docker (recommended)

```bash
docker compose up --build
```

The container runs uvicorn on port 8000, serves the frontend at `/ui/`, and stores the SQLite DB in `./data/`. Frontend files are mounted as a volume for live editing.

### Encoding Guardrails (Prevent Mojibake)

This repo enforces text hygiene to prevent mojibake and encoding drift.

One-time setup per clone:

```powershell
powershell -ExecutionPolicy Bypass -File tools/install-hooks.ps1
```

What this does:

- Configures git hooks path to `.githooks`
- Enables a pre-commit check that blocks commits if staged text files contain:
	- UTF-8 BOM
	- Invalid UTF-8
	- Mojibake markers (`\u00e2`, `\u00c3`, `\u00c2`, replacement char)
	- Any non-ASCII characters (strict policy)

Manual check (any time):

```powershell
python tools/check_text_hygiene.py --root .
```

VS Code workspace settings are also configured to reduce encoding issues:

- `files.encoding = utf8`
- `files.autoGuessEncoding = false`

### Local Development

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Seeding the Database

The seed script populates a fresh database from `data/world_seed.json`:

```bash
python seed.py [--url http://localhost:8000] [--file data/world_seed.json]
```

Seed order: RTGs -> Organizations (+ ally/enemy links) -> Locations -> Characters (+ reputation records) -> Contacts -> Org Standings -> Adventure Logs.

**`reseed.sh`** (Linux) and **`reseed.bat`** (Windows) provide a menu to either restart the container or do a full wipe-and-reseed. The Linux script runs `seed.py` inside the container so no host Python dependencies are needed.

---

## Authentication

Token-based access control with two roles:

| Role | Header | Capabilities |
|---|---|---|
| **Admin** | `X-Admin-Token` | Full read/write on all data; manage tokens; see all characters, hidden Matrix hosts, GM notes |
| **Player** | `X-User-Token` | Read-only on most data; edit own characters; see visible Matrix hosts only |

On first boot, the `BOOTSTRAP_ADMIN_KEY` env var is accepted as the admin password. After that, GMs create named tokens via the Manage Tokens page. Tokens are stored as SHA-256 hashes -- the plaintext is shown once at creation and never again.

Characters can be claimed by player tokens. Regenerating a token automatically reassigns all claimed characters to the new hash.

---

## Date Display

All dates are stored as real-world calendar dates. The frontend shifts the displayed year by `YEAR_OFFSET = 24` (defined in `manage-runs.html` and `world-state.html`) so runs appear set in the 2050s Sixth World. The DB is never touched -- `srDate()` is display-only.

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

Each run advances the campaign clock by 1-5 ticks (where each tick represents one day in the game world). Ticks drive all decay calculations -- the current campaign tick is the sum of all run `tick_count` values.

---

## Heat System

**Heat** (0-10) represents how much attention -- from law enforcement, corp security, and the shadow community -- is focused on a runner. Heat is applied directly per character by the GM via world-state changes on adventure logs or through the manage-characters page.

### Heat Tiers

| Heat | Label | Decay Half-Life |
|---|---|---|
| 0 | Neutral | inf (no decay) |
| 1-2 | Noticed | 3 days |
| 3-4 | Flagged | 7 days |
| 5-6 | Wanted | 14 days |
| 7-8 | Hot | 21 days |
| 9-10 | Nova Hot | 30 days |

Heat decays exponentially based on the current tier's half-life. Higher tiers linger longer. **Inactive PCs (lying low)** decay at 2x the normal rate.

For display purposes, heat values are floored -- a decayed value of 0.9 displays as 0 (Neutral).

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
| 1-3 | Seen | 7 days |
| 4-7 | Recognized | 14 days |
| 8-12 | In the Spotlight | 21 days |
| 13+ | Burned | 30 days |

PA values are floored for display -- 0.8 shows as Shadow.

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

### Standing Decay

Standings decay exponentially toward 0. Positive standings (loyalty) decay **1.5x slower** than negative (hostility fades faster in the shadows).

| Magnitude | Positive Half-Life | Negative Half-Life |
|---|---|---|
| +/-1-3 | 6 days | 4 days |
| +/-4-6 | 12 days | 8 days |
| +/-7-9 | 20 days | 13 days |
| +/-10 | 28 days | 19 days |

Standing values are ceiled for display -- a decayed +0.3 still reads as +1.

Lying-low PCs decay standings at 2x the normal rate.

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

### Visual Editor

The `manage-matrix.html` page provides an SVG canvas editor with drag-and-drop node placement, connection drawing, IC assignment, zone editing, and a node connection legend. Admins can toggle host visibility to control what players see.

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
| **Manage Matrix** | Matrix host topology editor. Generate hosts from configuration parameters, then edit visually on SVG canvas. Drag-and-drop nodes, draw connections, assign IC, define zones. Toggle player visibility per host. |
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
| AI Parser | Anthropic Claude (Sonnet) |
| Frontend | Vanilla HTML/JS/CSS -- no framework |
| Deployment | Docker + reverse proxy (Apache/nginx) |
| Auth | SHA-256 hashed tokens, rate-limited |
