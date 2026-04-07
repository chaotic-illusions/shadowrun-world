#!/usr/bin/env python3
"""
Fix migration: rebuild the characters table with correct PRIMARY KEY and type constraints.

The previous drop_character_stat_columns.py used CREATE TABLE ... AS SELECT,
which drops all PRIMARY KEY / NOT NULL / DEFAULT constraints in SQLite.
This script recreates the table using an explicit CREATE TABLE statement.

Run once:
    python fix_characters_schema.py
"""
import sqlite3
import os

DB_PATH = os.getenv("DATABASE_URL", "sqlite:///./data/shadowrun.db")
if DB_PATH.startswith("sqlite:///"):
    DB_PATH = DB_PATH[len("sqlite:///"):]

conn = sqlite3.connect(DB_PATH)
cur  = conn.cursor()

cur.execute("PRAGMA table_info(characters)")
cols = {row[1] for row in cur.fetchall()}

if "id" not in cols:
    print("characters table not found — nothing to fix.")
    conn.close()
    exit(0)

# Check whether it already has a proper PRIMARY KEY
cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='characters'")
row = cur.fetchone()
if row and "PRIMARY KEY" in (row[0] or "").upper():
    print("characters table already has PRIMARY KEY — nothing to do.")
    conn.close()
    exit(0)

print("Rebuilding characters table with correct schema...")

cur.executescript("""
    PRAGMA foreign_keys = OFF;

    CREATE TABLE characters_fixed (
        id              INTEGER  PRIMARY KEY AUTOINCREMENT,
        name            VARCHAR(200) NOT NULL,
        is_pc           BOOLEAN  NOT NULL DEFAULT 1,
        archetype       VARCHAR(100),
        title           VARCHAR(200),
        race            VARCHAR(50) DEFAULT 'Human',
        nationality     VARCHAR(100),
        gender          VARCHAR(50),
        age             INTEGER,
        description     TEXT,
        background      TEXT,
        show_background BOOLEAN  DEFAULT 0,
        contact_skills  JSON     DEFAULT '[]',
        connection      INTEGER  DEFAULT 1,
        organization_id INTEGER  REFERENCES organizations(id),
        karma_total     INTEGER  DEFAULT 0,
        karma_current   INTEGER  DEFAULT 0,
        is_active       BOOLEAN  DEFAULT 1,
        notes           TEXT,
        owner_token     VARCHAR(64),
        created_at      DATETIME,
        updated_at      DATETIME
    );

    INSERT INTO characters_fixed
        (id, name, is_pc, archetype, title, race, nationality, gender, age,
         description, background, show_background, contact_skills, connection,
         organization_id, karma_total, karma_current, is_active, notes,
         owner_token, created_at, updated_at)
    SELECT
        id, name, is_pc, archetype, title, race, nationality, gender, age,
        description, background, show_background, contact_skills, connection,
        organization_id, karma_total, karma_current, is_active, notes,
        owner_token, created_at, updated_at
    FROM characters;

    DROP TABLE characters;
    ALTER TABLE characters_fixed RENAME TO characters;

    CREATE INDEX IF NOT EXISTS ix_characters_name        ON characters (name);
    CREATE INDEX IF NOT EXISTS ix_characters_owner_token ON characters (owner_token);

    PRAGMA foreign_keys = ON;
""")

conn.commit()
print("✓ Characters table rebuilt with correct schema.")
conn.close()
