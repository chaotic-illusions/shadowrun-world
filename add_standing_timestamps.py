#!/usr/bin/env python3
"""
One-shot migration: add `standings_updated_at` column to the org_standings table.

Run once after pulling this change:
    python add_standing_timestamps.py
"""
import sqlite3
import os

DB_PATH = os.getenv("DATABASE_URL", "sqlite:///./data/shadowrun.db")
# Strip the sqlite:/// prefix
if DB_PATH.startswith("sqlite:///"):
    DB_PATH = DB_PATH[len("sqlite:///"):]

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check if column already exists
cur.execute("PRAGMA table_info(org_standings)")
cols = [row[1] for row in cur.fetchall()]

if "standings_updated_at" not in cols:
    cur.execute("ALTER TABLE org_standings ADD COLUMN standings_updated_at DATE")
    conn.commit()
    print("✓ Added 'standings_updated_at' column to org_standings table.")
else:
    print("'standings_updated_at' column already exists — nothing to do.")

conn.close()
