import logging
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from sqlalchemy import select, func
from app.db.base import Base
from app.db.session import engine, async_session
from app.auth.core import hash_token
from app.models.character import Character
import app.models  # noqa: F401 -- registers all ORM models with Base.metadata

from app.routers import (
    characters, contacts, locations, organizations,
    reputation, adventure_logs, consequences, rtgs,
    matrix_hosts, matrix_runs,
)
from app.routers import auth as auth_router
from app.auth.dependencies import get_any_token


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


@asynccontextmanager
async def lifespan(app: FastAPI):
    os.makedirs("data", exist_ok=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        await _migrate_plaintext_owner_tokens()
    except Exception:
        logging.getLogger(__name__).exception("owner-token migration failed")
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

app.mount("/ui", StaticFiles(directory="frontend", html=True), name="frontend")


@app.get("/", tags=["Info"], include_in_schema=False)
async def root():
    return RedirectResponse(url="/ui/")
