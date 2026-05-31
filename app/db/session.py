import os
from sqlalchemy import event
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./data/shadowrun.db")

# If the env var uses the sync driver prefix, swap it for aiosqlite
if DATABASE_URL.startswith("sqlite:///"):
    DATABASE_URL = DATABASE_URL.replace("sqlite:///", "sqlite+aiosqlite:///", 1)

# Use the default connection pool (QueuePool) so connections are reused across
# requests. NullPool caused server crashes on Windows under concurrent load by
# opening too many simultaneous SQLite connections.
engine = create_async_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})


@event.listens_for(engine.sync_engine, "connect")
def set_sqlite_pragmas(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA busy_timeout=5000")  # must be set BEFORE journal_mode
    cursor.execute("PRAGMA journal_mode=WAL")
    cursor.execute("PRAGMA foreign_keys=ON")  # SQLite ignores FK/ondelete rules unless enabled per connection
    cursor.close()


async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
