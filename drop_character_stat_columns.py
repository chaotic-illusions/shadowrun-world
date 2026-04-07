#!/usr/bin/env python3
"""
One-shot migration: drop attributes, skills, augmentations, gear, and nuyen
columns from the characters table.

SQLite does not support DROP COLUMN before 3.35 so we recreate the table.

Run once after pulling this change:
    python drop_character_stat_columns.py
"""
import sqlite3
import os

DB_PATH = os.getenv("DATABASE_URL", "sqlite:///./data/shadowrun.db")
if DB_PATH.startswith("sqlite:///"):
    DB_PATH = DB_PATH[len("sqlite:///"):]

conn = sqlite3.connect(DB_PATH)
cur  = conn.cursor()

# Check which columns currently exist
cur.execute("PRAGMA table_info(characters)")
existing_cols = [row[1] for row in cur.fetchall()]

cols_to_drop = {"attributes", "skills", "augmentations", "gear", "nuyen"}
present      = cols_to_drop & set(existing_cols)

if not present:
    print("Nothing to drop — columns already absent.")
    conn.close()
    exit(0)

print(f"Dropping columns: {', '.join(sorted(present))}")

# Build explicit CREATE TABLE — never use CREATE TABLE AS SELECT in SQLite;
# it strips PRIMARY KEY, NOT NULL, and DEFAULT constraints.
# Derive the keep set as the full current schema minus dropped columns.
cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='characters'")
original_sql = cur.fetchone()[0]

# Map col name → original declaration line (for type/constraint fidelity)
# We rebuild a minimal correct schema for the columns we keep.
keep_ddl = {
    "id":              "id              INTEGER  PRIMARY KEY AUTOINCREMENT",
    "name":            "name            VARCHAR(200) NOT NULL",
    "is_pc":           "is_pc           BOOLEAN  NOT NULL DEFAULT 1",
    "archetype":       "archetype       VARCHAR(100)",
    "title":           "title           VARCHAR(200)",
    "race":            "race            VARCHAR(50) DEFAULT 'Human'",
    "nationality":     "nationality     VARCHAR(100)",
    "gender":          "gender          VARCHAR(50)",
    "age":             "age             INTEGER",
    "description":     "description     TEXT",
    "background":      "background      TEXT",
    "show_background": "show_background BOOLEAN DEFAULT 0",
    "contact_skills":  "contact_skills  JSON DEFAULT '[]'",
    "connection":      "connection      INTEGER DEFAULT 1",
    "organization_id": "organization_id INTEGER REFERENCES organizations(id)",
    "karma_total":     "karma_total     INTEGER DEFAULT 0",
    "karma_current":   "karma_current   INTEGER DEFAULT 0",
    "is_active":       "is_active       BOOLEAN DEFAULT 1",
    "notes":           "notes           TEXT",
    "owner_token":     "owner_token     VARCHAR(64)",
    "created_at":      "created_at      DATETIME",
    "updated_at":      "updated_at      DATETIME",
}

col_defs = ",\n        ".join(keep_ddl[c] for c in keep if c in keep_ddl)
keep_sql = ", ".join(keep)

cur.executescript(f"""
    PRAGMA foreign_keys = OFF;

    CREATE TABLE characters_new (
        {col_defs}
    );

    INSERT INTO characters_new ({keep_sql})
        SELECT {keep_sql} FROM characters;

    DROP TABLE characters;
    ALTER TABLE characters_new RENAME TO characters;

    CREATE INDEX IF NOT EXISTS ix_characters_name        ON characters (name);
    CREATE INDEX IF NOT EXISTS ix_characters_owner_token ON characters (owner_token);

    PRAGMA foreign_keys = ON;
""")

conn.commit()
print("✓ Migration complete.")
conn.close()
