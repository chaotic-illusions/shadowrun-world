#!/usr/bin/env python3
"""
One-shot migration: add `heat` column to the reputations table.

Run once after pulling this change:
    python add_heat_column.py
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
cur.execute("PRAGMA table_info(reputations)")
cols = [row[1] for row in cur.fetchall()]

if "heat" not in cols:
    cur.execute("ALTER TABLE reputations ADD COLUMN heat INTEGER DEFAULT 0 NOT NULL")
    conn.commit()
    print("✓ Added 'heat' column to reputations table.")
else:
    print("'heat' column already exists — nothing to do.")

conn.close()
