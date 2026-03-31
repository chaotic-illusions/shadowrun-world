import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.db.base import Base
from app.db.session import engine
import app.models  # noqa: F401 — registers all ORM models with Base.metadata

from app.routers import (
    characters, contacts, locations, organizations,
    reputation, adventure_logs, house_rules, consequences, rtgs,
)
from app.routers import auth as auth_router
from app.auth.dependencies import get_any_token


@asynccontextmanager
async def lifespan(app: FastAPI):
    os.makedirs("data", exist_ok=True)
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Shadowrun World Engine",
    description=(
        "GM toolkit for Shadowrun 2nd Edition. "
        "Track characters, contacts, locations, organizations, reputation, "
        "adventure logs, consequence suggestions, and house rules."
    ),
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*", "X-Admin-Token", "X-User-Token"],
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
app.include_router(house_rules.router,    prefix="/house-rules",   tags=["House Rules"],        dependencies=_auth)
app.include_router(consequences.router,   prefix="/consequences",  tags=["Consequence Engine"], dependencies=_auth)
app.include_router(rtgs.router,           prefix="/rtgs",          tags=["RTGs"],               dependencies=_auth)

app.mount("/ui", StaticFiles(directory="frontend", html=True), name="frontend")


@app.get("/", tags=["Info"])
def root():
    return {
        "name": "Shadowrun World Engine",
        "edition": "2nd Edition",
        "version": "0.1.0",
        "docs": "/docs",
        "redoc": "/redoc",
    }
