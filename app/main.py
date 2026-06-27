import logging
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from sqlalchemy import select, func
from sqlalchemy.orm.exc import StaleDataError
from app.db.base import Base
from app.db.session import engine, async_session
from app.auth.core import hash_token
from app.models.character import Character
import app.models  # noqa: F401 -- registers all ORM models with Base.metadata

from app.routers import (
    characters, contacts, locations, organizations,
    reputation, adventure_logs, consequences, rtgs,
    matrix_hosts, matrix_runs, campaign,
)
from app.routers import auth as auth_router
from app.auth.dependencies import get_any_token
from app.services.campaign import get_campaign_state


async def _migrate_plaintext_owner_tokens():
    """One-time migration: hash any pre-existing plaintext owner_token values.

    SHA-256 hex digests are exactly 64 chars. Anything shorter is plaintext
    left over from before the token-hashing change and needs to be hashed.
    """
    async with async_session() as db:
        result = await db.execute(
            select(Character).where(
                Character.owner_token.isnot(None),
                func.length(Character.owner_token) != 64,
            )
        )
        rows = result.scalars().all()
        if not rows:
            return
        for char in rows:
            char.owner_token = hash_token(char.owner_token)
        await db.commit()
        print(f"[startup] Hashed {len(rows)} plaintext owner_token(s)")


async def _ensure_character_deck_builder_state_column():
    """Startup safety migration for deck_builder_state on SQLite deployments.

    Some local/container setups may run newer app code against older DB files
    before Alembic is applied. Add the JSON column in place when missing.
    """
    async with engine.begin() as conn:
        rows = await conn.exec_driver_sql("PRAGMA table_info(characters)")
        cols = {row[1] for row in rows.fetchall()}
        if "deck_builder_state" in cols:
            return
        await conn.exec_driver_sql(
            "ALTER TABLE characters ADD COLUMN deck_builder_state JSON NOT NULL DEFAULT '{}'"
        )
        print("[startup] Added characters.deck_builder_state column")


async def _ensure_matrix_run_version_column():
    """Startup safety migration for the matrix_runs optimistic-lock column.

    create_all only creates missing tables; it won't add a column to an existing
    matrix_runs table. Add it in place when an older DB file predates the column.
    """
    async with engine.begin() as conn:
        rows = await conn.exec_driver_sql("PRAGMA table_info(matrix_runs)")
        cols = {row[1] for row in rows.fetchall()}
        if "version" in cols:
            return
        await conn.exec_driver_sql(
            "ALTER TABLE matrix_runs ADD COLUMN version INTEGER NOT NULL DEFAULT 0"
        )
        print("[startup] Added matrix_runs.version column")


async def _ensure_matrix_run_owner_token_hash_column():
    """Startup safety migration for the matrix_runs owner_token_hash column.

    create_all only creates missing tables; it won't add a column to an existing
    matrix_runs table. A DB created before owner-scoping was added lacks this column,
    and since the model selects it on every query, EVERY matrix-run request 500s until
    it exists. Add the column (and its declared index) in place, idempotently.
    """
    async with engine.begin() as conn:
        rows = await conn.exec_driver_sql("PRAGMA table_info(matrix_runs)")
        cols = {row[1] for row in rows.fetchall()}
        if "owner_token_hash" not in cols:
            await conn.exec_driver_sql(
                "ALTER TABLE matrix_runs ADD COLUMN owner_token_hash VARCHAR(64)"
            )
            print("[startup] Added matrix_runs.owner_token_hash column")
        # The model declares this column indexed; mirror that so reflection/create_all and
        # owner lookups match the ORM intent (idempotent via IF NOT EXISTS).
        await conn.exec_driver_sql(
            "CREATE INDEX IF NOT EXISTS ix_matrix_runs_owner_token_hash "
            "ON matrix_runs (owner_token_hash)"
        )


async def _ensure_matrix_host_id_code_column():
    """Startup safety migration for matrix_hosts.id_code on SQLite deployments.

    create_all only creates missing tables; it won't add a column to an existing
    matrix_hosts table. Add it in place when an older DB file predates the column.
    """
    async with engine.begin() as conn:
        rows = await conn.exec_driver_sql("PRAGMA table_info(matrix_hosts)")
        cols = {row[1] for row in rows.fetchall()}
        if "id_code" in cols:
            return
        await conn.exec_driver_sql(
            "ALTER TABLE matrix_hosts ADD COLUMN id_code VARCHAR(20)"
        )
        print("[startup] Added matrix_hosts.id_code column")


async def _ensure_matrix_host_trap_dest_column():
    """Startup safety migration for matrix_hosts.is_trap_door_dest on SQLite deployments.

    create_all only creates missing tables; it won't add a column to an existing
    matrix_hosts table. Add it in place when an older DB file predates the column.
    """
    async with engine.begin() as conn:
        rows = await conn.exec_driver_sql("PRAGMA table_info(matrix_hosts)")
        cols = {row[1] for row in rows.fetchall()}
        if "is_trap_door_dest" not in cols:
            await conn.exec_driver_sql(
                "ALTER TABLE matrix_hosts ADD COLUMN is_trap_door_dest BOOLEAN NOT NULL DEFAULT 0"
            )
            print("[startup] Added matrix_hosts.is_trap_door_dest column")
        # Reconcile is_trap_door_dest to the canonical truth: a host is a trap-door destination IFF
        # some host's trap_doors_json names it. The flag is fully derived now (the manual toggles
        # were removed), so flip BOTH directions -- set it on referenced hosts and clear it on
        # hosts no longer referenced (e.g. stale legacy/manual flags). The WHERE guard keeps it
        # idempotent: only rows whose flag disagrees with the derived truth are touched.
        ref_subquery = """
                SELECT DISTINCT json_extract(td.value, '$.destination_host_id')
                FROM matrix_hosts mh,
                     json_each(CASE WHEN json_valid(mh.trap_doors_json)
                                    THEN mh.trap_doors_json ELSE '[]' END) td
                WHERE json_extract(td.value, '$.destination_host_id') IS NOT NULL
        """
        result = await conn.exec_driver_sql(
            f"""
            UPDATE matrix_hosts
               SET is_trap_door_dest = CASE WHEN id IN ({ref_subquery}) THEN 1 ELSE 0 END
             WHERE is_trap_door_dest <> CASE WHEN id IN ({ref_subquery}) THEN 1 ELSE 0 END
            """
        )
        if result.rowcount and result.rowcount > 0:
            print(f"[startup] Reconciled {result.rowcount} trap-door destination flag(s)")


async def _ensure_campaign_state():
    """Seed the single CampaignState row at startup for timeline continuity.

    create_all builds the table on fresh DBs; this seeds its one row from the
    legacy per-log tick total so decay stamps stay continuous on existing DBs.
    """
    async with async_session() as db:
        await get_campaign_state(db)


@asynccontextmanager
async def lifespan(app: FastAPI):
    os.makedirs("data", exist_ok=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        await _migrate_plaintext_owner_tokens()
    except Exception:
        logging.getLogger(__name__).exception("owner-token migration failed")
    try:
        await _ensure_character_deck_builder_state_column()
    except Exception:
        logging.getLogger(__name__).exception("deck-builder-state migration failed")
    try:
        await _ensure_matrix_run_version_column()
    except Exception:
        logging.getLogger(__name__).exception("matrix-run version-column migration failed")
    try:
        await _ensure_matrix_run_owner_token_hash_column()
    except Exception:
        logging.getLogger(__name__).exception("matrix-run owner-token-hash-column migration failed")
    try:
        await _ensure_matrix_host_id_code_column()
    except Exception:
        logging.getLogger(__name__).exception("matrix-host id_code-column migration failed")
    try:
        await _ensure_matrix_host_trap_dest_column()
    except Exception:
        logging.getLogger(__name__).exception("matrix-host trap-dest-column migration failed")
    try:
        await _ensure_campaign_state()
    except Exception:
        logging.getLogger(__name__).exception("campaign-state seed failed")
    yield


app = FastAPI(
    title="Shadowrun World Engine",
    description=(
        "GM toolkit for Shadowrun 2nd Edition. "
        "Track characters, contacts, locations, organizations, reputation, "
        "adventure logs, and consequence suggestions."
    ),
    version="0.1.0",
    lifespan=lifespan,
)

# CORS -- configurable via CORS_ORIGINS env var (comma-separated).
# Local dev default: * (open). Production: set to your server's URL, e.g.
#   CORS_ORIGINS=https://yourserver.example.com
# Since the frontend is served from the same FastAPI origin, CORS mainly
# protects against cross-site requests from other domains.
_cors_raw = os.environ.get("CORS_ORIGINS", "*")
_cors_origins = [o.strip() for o in _cors_raw.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "X-Admin-Token", "X-User-Token"],
)


@app.exception_handler(StaleDataError)
async def _stale_data_handler(request: Request, exc: StaleDataError):
    """A concurrent writer bumped the optimistic-lock version mid-request.

    Surfaces as 409 so the client can reload current state and retry rather than
    silently clobbering the other writer's update.
    """
    return JSONResponse(
        status_code=409,
        content={"detail": "This record was modified by another request. Reload and retry."},
    )


# Auth routes are unprotected (verify, set-password handle their own validation)
app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])

# All world-data routes require a valid token (admin or user)
_auth = [Depends(get_any_token)]
app.include_router(characters.router,     prefix="/characters",    tags=["Characters"],        dependencies=_auth)
app.include_router(contacts.router,       prefix="/contacts",      tags=["Contacts"],           dependencies=_auth)
app.include_router(locations.router,      prefix="/locations",     tags=["Locations"],          dependencies=_auth)
app.include_router(organizations.router,  prefix="/organizations", tags=["Organizations"],      dependencies=_auth)
app.include_router(reputation.router,     prefix="/reputation",    tags=["Reputation"],         dependencies=_auth)
app.include_router(adventure_logs.router, prefix="/runs",          tags=["Adventure Logs"],     dependencies=_auth)
app.include_router(consequences.router,   prefix="/consequences",  tags=["Consequence Engine"], dependencies=_auth)
app.include_router(rtgs.router,           prefix="/rtgs",          tags=["RTGs"],               dependencies=_auth)
app.include_router(matrix_hosts.router,   prefix="/matrix-hosts",  tags=["Matrix Hosts"],       dependencies=_auth)
app.include_router(matrix_runs.router,    prefix="/matrix-runs2",  tags=["Matrix Runs SR2"],    dependencies=_auth)
app.include_router(campaign.router,       prefix="/campaign",      tags=["Campaign Clock"],     dependencies=_auth)

app.mount("/ui", StaticFiles(directory="frontend", html=True), name="frontend")


@app.get("/", tags=["Info"], include_in_schema=False)
async def root():
    return RedirectResponse(url="/ui/")
