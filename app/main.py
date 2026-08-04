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


async def _ensure_sqlite_column(table: str, column: str, definition: str) -> bool:
    """Ensure a legacy SQLite column exists and verify the postcondition.

    Two app processes may observe the missing column concurrently. The loser may
    receive a duplicate-column error; re-reading the schema distinguishes that
    harmless race from a migration failure.
    """
    async with engine.begin() as conn:
        rows = await conn.exec_driver_sql(f"PRAGMA table_info({table})")
        if column in {row[1] for row in rows.fetchall()}:
            return False
        try:
            await conn.exec_driver_sql(
                f"ALTER TABLE {table} ADD COLUMN {column} {definition}"
            )
        except Exception:
            rows = await conn.exec_driver_sql(f"PRAGMA table_info({table})")
            if column not in {row[1] for row in rows.fetchall()}:
                raise

        rows = await conn.exec_driver_sql(f"PRAGMA table_info({table})")
        if column not in {row[1] for row in rows.fetchall()}:
            raise RuntimeError(f"startup schema guard did not create {table}.{column}")
    return True


async def _ensure_character_deck_builder_state_column():
    """Startup safety migration for deck_builder_state on SQLite deployments.

    Some local/container setups may run newer app code against older DB files
    before Alembic is applied. Add the JSON column in place when missing.
    """
    if await _ensure_sqlite_column(
        "characters", "deck_builder_state", "JSON NOT NULL DEFAULT '{}'"
    ):
        print("[startup] Added characters.deck_builder_state column")


async def _ensure_character_math_spu_columns():
    """Startup safety migration for the Math SPU cyberware columns on SQLite deployments.

    create_all only creates missing tables; it won't add columns to an existing characters
    table. Add them in place when an older DB file predates them. Idempotent.
    """
    if await _ensure_sqlite_column(
        "characters", "math_spu_enabled", "BOOLEAN NOT NULL DEFAULT 0"
    ):
        print("[startup] Added characters.math_spu_enabled column")
    if await _ensure_sqlite_column(
        "characters", "math_spu_rating", "INTEGER NOT NULL DEFAULT 0"
    ):
        print("[startup] Added characters.math_spu_rating column")


async def _ensure_matrix_run_version_column():
    """Startup safety migration for the matrix_runs optimistic-lock column.

    create_all only creates missing tables; it won't add a column to an existing
    matrix_runs table. Add it in place when an older DB file predates the column.
    """
    if await _ensure_sqlite_column(
        "matrix_runs", "version", "INTEGER NOT NULL DEFAULT 0"
    ):
        print("[startup] Added matrix_runs.version column")


async def _ensure_matrix_run_owner_token_hash_column():
    """Startup safety migration for the matrix_runs owner_token_hash column.

    create_all only creates missing tables; it won't add a column to an existing
    matrix_runs table. A DB created before owner-scoping was added lacks this column,
    and since the model selects it on every query, EVERY matrix-run request 500s until
    it exists. Add the column (and its declared index) in place, idempotently.
    """
    added = await _ensure_sqlite_column(
        "matrix_runs", "owner_token_hash", "VARCHAR(64)"
    )
    async with engine.begin() as conn:
        # The model declares this column indexed; mirror that so reflection/create_all and
        # owner lookups match the ORM intent (idempotent via IF NOT EXISTS).
        await conn.exec_driver_sql(
            "CREATE INDEX IF NOT EXISTS ix_matrix_runs_owner_token_hash "
            "ON matrix_runs (owner_token_hash)"
        )
        rows = await conn.exec_driver_sql("PRAGMA index_list(matrix_runs)")
        if "ix_matrix_runs_owner_token_hash" not in {row[1] for row in rows.fetchall()}:
            raise RuntimeError("startup schema guard did not create matrix owner index")
    if added:
        print("[startup] Added matrix_runs.owner_token_hash column")


async def _ensure_matrix_run_aar_acknowledged_column():
    """Startup safety migration for the matrix_runs after-action-report gate column.

    create_all only creates missing tables; it won't add a column to an existing matrix_runs table.
    The run-start gate and the GM AAR review view both read this column, so an older DB file that
    predates it would 500 on those paths until it exists. Add it in place, idempotently.
    """
    if await _ensure_sqlite_column(
        "matrix_runs", "aar_acknowledged", "BOOLEAN NOT NULL DEFAULT 0"
    ):
        print("[startup] Added matrix_runs.aar_acknowledged column")


async def _ensure_matrix_host_id_code_column():
    """Startup safety migration for matrix_hosts.id_code on SQLite deployments.

    create_all only creates missing tables; it won't add a column to an existing
    matrix_hosts table. Add it in place when an older DB file predates the column.
    """
    if await _ensure_sqlite_column("matrix_hosts", "id_code", "VARCHAR(20)"):
        print("[startup] Added matrix_hosts.id_code column")


async def _ensure_matrix_host_trap_dest_column():
    """Startup safety migration for matrix_hosts.is_trap_door_dest on SQLite deployments.

    create_all only creates missing tables; it won't add a column to an existing
    matrix_hosts table. Add it in place when an older DB file predates the column.
    """
    added = await _ensure_sqlite_column(
        "matrix_hosts", "is_trap_door_dest", "BOOLEAN NOT NULL DEFAULT 0"
    )
    if added:
        print("[startup] Added matrix_hosts.is_trap_door_dest column")
    async with engine.begin() as conn:
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


async def _ensure_adventure_run_number_schema():
    """Establish atomic run allocation invariants on legacy SQLite databases."""
    async with engine.begin() as conn:
        await conn.exec_driver_sql(
            """
            WITH duplicate_rows AS (
                SELECT id,
                       ROW_NUMBER() OVER (ORDER BY run_number, id) AS offset
                  FROM adventure_logs
                 WHERE id NOT IN (
                           SELECT MIN(id)
                             FROM adventure_logs
                            WHERE run_number IS NOT NULL
                            GROUP BY run_number
                       )
                   AND run_number IS NOT NULL
            ), maximum AS (
                SELECT COALESCE(MAX(run_number), 0) AS value FROM adventure_logs
            )
            UPDATE adventure_logs
               SET run_number = (SELECT value FROM maximum)
                                + (SELECT offset FROM duplicate_rows WHERE duplicate_rows.id = adventure_logs.id)
             WHERE id IN (SELECT id FROM duplicate_rows)
            """
        )
        await conn.exec_driver_sql(
            "CREATE UNIQUE INDEX IF NOT EXISTS ux_adventure_logs_run_number "
            "ON adventure_logs (run_number)"
        )
        rows = await conn.exec_driver_sql("PRAGMA index_list(adventure_logs)")
        indexes = {row[1]: bool(row[2]) for row in rows.fetchall()}
        if not indexes.get("ux_adventure_logs_run_number"):
            raise RuntimeError("startup schema guard did not create unique adventure run index")
        await conn.exec_driver_sql(
            "INSERT INTO adventure_run_counter (id, last_run_number) VALUES "
            "(1, (SELECT COALESCE(MAX(run_number), 0) FROM adventure_logs)) "
            "ON CONFLICT(id) DO UPDATE SET last_run_number = "
            "MAX(adventure_run_counter.last_run_number, excluded.last_run_number)"
        )
        row = await conn.exec_driver_sql(
            "SELECT last_run_number FROM adventure_run_counter WHERE id = 1"
        )
        if row.scalar_one_or_none() is None:
            raise RuntimeError("startup schema guard did not seed adventure run counter")


async def _ensure_campaign_state():
    """Seed the single CampaignState row at startup for timeline continuity.

    create_all builds the table on fresh DBs; this seeds its one row from the
    legacy per-log tick total so decay stamps stay continuous on existing DBs.
    """
    async with async_session() as db:
        await get_campaign_state(db)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        os.makedirs("data", exist_ok=True)
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        # Column guards MUST run before any full-ORM query below: a select(Character) emits every
        # mapped column, so a new column that a guard adds would otherwise raise "no such column"
        # on an existing DB before the guard has a chance to add it.
        await _ensure_character_deck_builder_state_column()
        await _ensure_character_math_spu_columns()
        await _ensure_matrix_run_version_column()
        await _ensure_matrix_run_owner_token_hash_column()
        await _ensure_matrix_run_aar_acknowledged_column()
        await _ensure_matrix_host_id_code_column()
        await _ensure_matrix_host_trap_dest_column()
        await _migrate_plaintext_owner_tokens()
        await _ensure_adventure_run_number_schema()
        await _ensure_campaign_state()
        yield
    finally:
        await engine.dispose()


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
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "X-Admin-Token", "X-User-Token", "X-Runner-View"],
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
