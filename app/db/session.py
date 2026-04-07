import os
from sqlalchemy import event
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import NullPool

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./data/shadowrun.db")

# If the env var uses the sync driver prefix, swap it for aiosqlite
if DATABASE_URL.startswith("sqlite:///"):
    DATABASE_URL = DATABASE_URL.replace("sqlite:///", "sqlite+aiosqlite:///", 1)

# NullPool: create a fresh connection per request and close it immediately after.
# This avoids pool-exhaustion under concurrent async requests — SQLite has
# negligible connection overhead, so there's no performance penalty.
engine = create_async_engine(DATABASE_URL, echo=False, poolclass=NullPool)


@event.listens_for(engine.sync_engine, "connect")
def set_sqlite_pragmas(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA journal_mode=WAL")
    cursor.execute("PRAGMA busy_timeout=5000")  # wait up to 5s if DB is locked
    cursor.close()


async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
