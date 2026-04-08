# Shadowrun World Tracker

A FastAPI + SQLite campaign management tool for **Shadowrun 2nd Edition** GMs. Tracks characters, contacts, organizations, locations, run logs, heat, faction standing, reputation, and public awareness across a living campaign world.

---

## Setup

### Requirements
- Python 3.11+
- Docker (optional, for containerized deployment)

### Local install

```bash
pip install -r requirements.txt
```

Set the Anthropic API key if you want AI narrative parsing:

```bash
set ANTHROPIC_API_KEY=sk-ant-...
```

Start the server:

```bash
uvicorn app.main:app --reload
```

Open `frontend/index.html` in a browser (or serve it from a local web server).

### Environment Variables

| Variable | Default | Description |
|---|---|---|
| `BOOTSTRAP_ADMIN_KEY` | `shadowrunner` | Initial admin password used by `seed.py` and for first login |
| `ANTHROPIC_API_KEY` | *(none)* | Anthropic API key for AI narrative parsing |
| `CLAUDE_MODEL` | `claude-sonnet-4-6` | Claude model name used by the narrative parser |
| `CORS_ORIGINS` | `*` | Comma-separated allowed origins for CORS |
| `DATABASE_URL` | `sqlite+aiosqlite:///./data/shadowrun.db` | SQLAlchemy async database URL |

### Docker

```bash
docker compose up --build
```

---

## Date Display

All dates are stored as real-world calendar dates in the database. The frontend shifts the displayed year by `YEAR_OFFSET = 24` (defined in `manage-runs.html` and `world-state.html`) so runs appear set in the 2050s Sixth World. The DB is never touched — `srDate()` is display-only.

---

## Run Logging

### Creating a Run

Runs can be logged two ways:
1. **Manual entry** — fill the form fields directly
2. **AI narrative parse** — paste a free-form GM narrative; Claude extracts structured data and proposes world-state changes

### Run Outcomes

| Value | Description |
|---|---|
| `success` | Team achieved objective cleanly |
| `partial_success` | Objective met with complications |
| `failure` | Run failed, team extracted |
| `critical_failure` | Catastrophic — deaths, blown covers, or major blowback |
| `abandoned` | Run called off before completion |

### Consequence Tags

Tags feed directly into the **heat formula** (see below). Stack multiples for compounding exposure.

| Tag | Heat Bonus | Notes |
|---|---|---|
| `witnesses` | +1 | Credible eyewitnesses to runner activity |
| `collateral_damage` | +2 | Civilian property or bystander harm |
| `public_scene` | +2 | Visible incident in a public area |
| `media_attention` | +3 | Newscast, social feeds, official press |
| `casualties` | +1 | Non-wetwork deaths — bystanders, guards |
| `wetwork` | +1 | Sanctioned kill; the death was the job |
| `assassination` | +1 | High-profile targeted killing |
| `magic_use` | +1 | Visible/documented spell use or conjuring |
| `vehicle_chase` | +1 | High-speed pursuit drawing police attention |
| `data_theft` | 0 | Clean extraction, no physical evidence |
| `extraction` | 0 | Person extraction; heat only if blown |
| `bribery` | 0 | Greased palms — leaves no public trace |
| `false_flag` | 0 | Framed another party; reduces blowback |
| `stealth` | 0 | Ghost run — no witnesses, no trace |

---

## Heat System

**Heat** (0–10) represents how much law enforcement, corp security, and shadow community attention is currently focused on a runner.

### Heat formula

```
heat = outcome_base + sum(tag_bonuses) + employer_tier_bonus + employer_type_bonus
```

**Outcome base:**
| Outcome | Base heat |
|---|---|
| success | 0 |
| partial_success | 1 |
| failure | 2 |
| critical_failure | 3 |
| abandoned | 1 |

**Employer tier bonus:**
| Tier | Bonus |
|---|---|
| 1–2 | 0 |
| 3–4 | +1 |
| 5 | +2 |
| 6 | +3 |

**Employer type bonus:**
| Org type | Bonus |
|---|---|
| megacorp | +1 |
| law_enforcement | +2 |
| government | +1 |
| Others | 0 |

### Heat decay (exponential, half-life by tier)

| Heat range | Label | Half-life |
|---|---|---|
| 0 | Neutral | ∞ (no decay) |
| 1–2 | Noticed | 3 days |
| 3–4 | Flagged | 7 days |
| 5–6 | Wanted | 14 days |
| 7–8 | Hot | 21 days |
| 9–10 | Nova Hot | 30 days |

**Inactive PCs (lying low)** decay at `2×` the normal rate — their heat, PA, and org standings all drop twice as fast.

---

## Reputation

Each PC has three reputation tracks:

| Track | Description |
|---|---|
| `street_cred` | Earned by successful, skillful runs |
| `notoriety` | Earned by atrocities, betrayals, collateral horror |
| `public_awareness` | How recognizable you are to ordinary citizens |

**Net Rep** = `20 + street_cred − notoriety` (clamped 0–40). Displayed as a tier label (Unknown → Street Legend).

**PA decay** uses exponential half-life; PA 1–3 has a 30-day half-life, PA 7–9 has 120 days, PA 10 is permanent.

---

## Faction Standing

Each character has a standing with each org, from −10 (Hunted) to +10 (Trusted Ally).

**Ripple effect:** A standing change with org X propagates at `40%` magnitude (capped at ±2) to X's documented allies and enemies. Allies of X gain 40% of your gain; enemies of X lose 40%.

**Standing decay** toward 0 using exponential half-life. Positive standings decay slower (loyalty takes longer to fade) than negative (grudges fade faster in the shadows).

---

## AI Narrative Parsing

Requires `ANTHROPIC_API_KEY`. Paste a GM session narrative and the parser extracts:
- Run title, objective, result, outcome, employer
- Consequence tags
- Proposed world changes (street_cred, notoriety, public_awareness, heat, org_standing)

Changes are **proposed only** — the GM reviews and applies them manually via the review panel.

---

## Frontend Pages

| Page | Purpose |
|---|---|
| `world-state.html` | Live view: party stats, faction rep, all characters |
| `manage-runs.html` | Log runs, AI narrative parse, run history |
| `manage-characters.html` | Create/edit player characters |
| `manage-organizations.html` | Create/edit orgs, set ally/enemy links |
| `manage-locations.html` | Location management |
| `manage-rtgs.html` | Rating-tier grid for orgs |
| `manage-tokens.html` | Manage admin/user access tokens |

---

## Database Migrations

Migration scripts are in the project root. Run with `python <script>.py` after backing up your DB.

| Script | Purpose |
|---|---|
| `add_standing_timestamps.py` | Adds `standings_updated_at` to `org_standings` |
| `drop_character_stat_columns.py` | Removes nuyen/attributes/skills/augmentations/gear columns |
| `fix_characters_schema.py` | Emergency repair if PK was dropped by early migration |

> **SQLite note:** Column operations require `CREATE TABLE … INSERT … DROP … RENAME`. Never use `CREATE TABLE AS SELECT` — it strips the PRIMARY KEY.
