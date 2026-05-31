# Shadowrun World Engine -- Copilot Reference

> **Adding code? Read [`AGENTS.md`](../AGENTS.md) first** -- the working guide for
> check-first / validate-after practices and common pitfalls (inline styles vs. style.css,
> JSON-column updates, server-side GM redaction, migrations + startup guards, etc.).
> This file is the *reference* for what the code is; AGENTS.md is *how to change it*.

## Stack
- **Backend**: FastAPI (async), SQLAlchemy 2.x async ORM, Pydantic v2, aiosqlite, Alembic
- **Database**: SQLite via `sqlite+aiosqlite:///./data/shadowrun.db` -- WAL mode, QueuePool (NOT NullPool -- causes Windows crash under load)
- **AI**: Anthropic Claude (model via `CLAUDE_MODEL` env var) -- lazy-imported only on `/runs/parse-narrative`
- **Frontend**: Static HTML/CSS/JS mounted at `/ui/` via FastAPI `StaticFiles` -- no build step, no framework
- **Auth**: SHA-256 hashed tokens, two roles: Admin (`X-Admin-Token`) and User (`X-User-Token`)
- **Python**: 3.14 locally (3.12 in Docker image)

## Project Layout
```
app/
  main.py          -- FastAPI app, lifespan, router registration, StaticFiles mount
  dependencies.py  -- get_db, get_or_404, apply_update
  auth/            -- core.py (hash/verify/generate), dependencies.py (FastAPI deps), rate_limit.py
  db/              -- base.py (DeclarativeBase), session.py (engine + async_session)
  models/          -- SQLAlchemy ORM models (adventure_log, auth, character, contact, location,
                     matrix_host, matrix_run, organization, reputation, rtg, associations)
  routers/         -- one file per resource; all world-data routes require get_any_token
                     (matrix_runs.py = SR2 run engine, prefix /matrix-runs2; matrix_hosts.py = SR1 topology)
  schemas/         -- Pydantic v2 models (Create/Update/Read per resource)
  services/        -- campaign.py, consequence_engine.py, heat_calculator.py,
                     matrix_engine.py, matrix_generator.py, matrix_rules.py,
                     narrative_parser.py, secrets.py
  data/            -- consequence_tags.py (SINGLE_TAG_RULES, COMPOUND_TAG_RULES)
alembic/           -- env.py uses async engine; versions/ holds the migration chain (keep a single head)
tests/             -- pytest + pytest-asyncio; conftest.py is empty (no shared fixtures yet)
frontend/          -- static files served at /ui/
data/              -- world_seed.json, shadowrun.db (gitignored)
seed.py            -- populates DB via API; uses httpx.Client; accepts --admin-token CLI arg
decay_sim.py       -- standalone CLI tool; imports from app.services.heat_calculator
```

## Auth Rules
- `BOOTSTRAP_ADMIN_KEY` env var (default: `shadowrunner`) accepted as admin password **only** when no admin tokens exist in DB yet
- All world-data API routes require at least a valid user token (`get_any_token`)
- Admin-only actions use `get_admin_token`
- Tokens stored as SHA-256 hex (64 chars); plaintext shown once at creation
- Rate limiter is in `app/auth/rate_limit.py` -- exponential backoff per IP, in-memory state

## Environment Variables
| Var | Default | Notes |
|-----|---------|-------|
| `DATABASE_URL` | `sqlite+aiosqlite:///./data/shadowrun.db` | sync prefix auto-replaced |
| `BOOTSTRAP_ADMIN_KEY` | `shadowrunner` | bootstrap only; ignored once admin tokens exist |
| `ANTHROPIC_API_KEY` | -- | optional; 503 returned if missing when parsing |
| `CLAUDE_MODEL` | `claude-sonnet-4-6` | model string passed to Anthropic client |
| `CORS_ORIGINS` | `*` | comma-separated; open for local dev |

## API Key Resolution (secrets.py)
1. Windows Credential Manager via `keyring.get_password("shadowrun-world", "ANTHROPIC_API_KEY")`
2. `ANTHROPIC_API_KEY` environment variable
3. Returns `None` -> parse endpoint returns 503 (not a crash)

## Key Patterns
- **Async everywhere**: all DB calls use `await db.execute(...)`, `AsyncSession`, `async_sessionmaker`
- **M2M relations**: set relationship attrs on transient objects *before* `db.add()` to avoid MissingGreenlet
- **Alembic**: `alembic upgrade head` -- env.py uses `create_async_engine` with run_sync
- **ORM startup**: `app.models` imported in `main.py` and `alembic/env.py` to register all models with `Base.metadata`
- **Decay**: tick-based (1 tick = 1 day); exponential half-life decay for heat, PA, org standings

## Testing
- Runner: `pytest -v` (or via `localdev.ps1` option 2)
- All tests are sync; no async test fixtures currently
- `test_seed.py` mocks `httpx.Client` directly -- does NOT patch urllib
- `test_consequence_engine.py` uses tag names from `SINGLE_TAG_RULES` / `COMPOUND_TAG_RULES`

## Local Dev (no Docker)
- venv: `.venv\Scripts\python` (Python 3.14, created with `py -3.14 -m venv .venv`)
- Start: `.\localdev.ps1` -- interactive menu; NOT committed to git
- Seed: requires server running; uses `BOOTSTRAP_ADMIN_KEY` by default
- `data/shadowrun.db` and `.venv/` are gitignored

## Response Conventions
- **Show only changed lines** -- when editing a file, output only the modified lines plus minimal context; do not reprint entire functions or files
- **Skip explanations for mechanical tasks** -- adding a field, renaming a symbol, fixing a type annotation: make the change and confirm briefly, no prose walkthrough

## Source Encoding Policy (Frontend)
- All source files must be saved as **UTF-8 (no BOM)**.
- For `frontend/*.html`, `frontend/*.js`, and `frontend/*.css`, prefer **ASCII-only literals** when practical.
- Do not paste smart punctuation or symbols directly when an ASCII form is acceptable (`--`, `...`, `x`, `>=`, `<=`, etc.).
- If a visible symbol is required in HTML, use an entity (`&mdash;`, `&ndash;`, `&times;`, `&ge;`, `&le;`, `&yen;`) rather than pasting Unicode glyphs.
- After frontend text edits, scan the changed files for mojibake markers like ``, ``, and `` and fix before finishing.
- Detailed checklist: `.github/instructions/frontend-encoding.instructions.md`.
