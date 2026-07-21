"""Save / restore a single matrix_runs row as a JSON snapshot.

Dev utility for pinning a run's state so it can be reloaded after code changes.

Usage:
    python tools/snapshot_run.py save 1
    python tools/snapshot_run.py save 1 data/backups/run_1_before_change.json
    python tools/snapshot_run.py restore 1
    python tools/snapshot_run.py restore 1 data/backups/run_1_before_change.json
    python tools/snapshot_run.py show 1

Notes:
- Reads/writes data/shadowrun.db directly (raw sqlite3). Stop the server before
  `restore` so the reloaded state is the one the next request sees.
- `restore` bypasses the ORM optimistic-lock check on purpose (direct UPDATE),
  so it can rewind `version` to the snapshot value.
- Snapshot files default to data/backups/run_<id>_snapshot.json (gitignored).
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
from datetime import datetime, UTC
from pathlib import Path

# Columns to capture. decker_json / state_json are stored as JSON text by
# SQLAlchemy; parse them for readability and re-serialize on restore.
_COLUMNS = [
    "id",
    "host_id",
    "owner_token_hash",
    "decker_json",
    "state_json",
    "status",
    "version",
    "created_at",
    "updated_at",
]
_JSON_COLUMNS = {"decker_json", "state_json"}


def _db_path() -> Path:
    url = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./data/shadowrun.db")
    # Strip the SQLAlchemy driver prefix down to a filesystem path.
    for prefix in ("sqlite+aiosqlite:///", "sqlite:///"):
        if url.startswith(prefix):
            return Path(url[len(prefix):])
    return Path("data/shadowrun.db")


def _default_snapshot_path(run_id: int) -> Path:
    return Path("data/backups") / f"run_{run_id}_snapshot.json"


def _connect() -> sqlite3.Connection:
    db = _db_path()
    if not db.exists():
        raise SystemExit(f"database not found: {db}")
    conn = sqlite3.connect(str(db))
    conn.row_factory = sqlite3.Row
    return conn


def save(run_id: int, path: Path) -> None:
    conn = _connect()
    try:
        cols = ", ".join(_COLUMNS)
        row = conn.execute(
            f"SELECT {cols} FROM matrix_runs WHERE id = ?", (run_id,)
        ).fetchone()
    finally:
        conn.close()
    if row is None:
        raise SystemExit(f"run {run_id} not found")

    data: dict = {}
    for col in _COLUMNS:
        val = row[col]
        if col in _JSON_COLUMNS and isinstance(val, str):
            try:
                val = json.loads(val)
            except (TypeError, ValueError):
                pass
        data[col] = val

    payload = {
        "_snapshot_ts": datetime.now(UTC).isoformat(),
        "_source_db": str(_db_path()),
        "row": data,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    state = data.get("state_json") or {}
    events = state.get("event_log") or []
    print(f"saved run {run_id} -> {path}")
    print(f"  status={data.get('status')} version={data.get('version')} "
          f"host_id={data.get('host_id')} events={len(events)}")


def restore(run_id: int, path: Path) -> None:
    if not path.exists():
        raise SystemExit(f"snapshot not found: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    row = payload.get("row") or {}
    if int(row.get("id", run_id)) != run_id:
        raise SystemExit(
            f"snapshot is for run {row.get('id')}, not {run_id}"
        )

    set_cols = [c for c in _COLUMNS if c != "id"]
    values = []
    for col in set_cols:
        val = row.get(col)
        if col in _JSON_COLUMNS and not isinstance(val, str):
            val = json.dumps(val)
        values.append(val)

    conn = _connect()
    try:
        exists = conn.execute(
            "SELECT 1 FROM matrix_runs WHERE id = ?", (run_id,)
        ).fetchone()
        if exists is None:
            raise SystemExit(
                f"run {run_id} no longer exists; insert-restore not supported"
            )
        assignments = ", ".join(f"{c} = ?" for c in set_cols)
        conn.execute(
            f"UPDATE matrix_runs SET {assignments} WHERE id = ?",
            (*values, run_id),
        )
        conn.commit()
    finally:
        conn.close()

    state = row.get("state_json") or {}
    events = state.get("event_log") or []
    print(f"restored run {run_id} <- {path}")
    print(f"  status={row.get('status')} version={row.get('version')} "
          f"events={len(events)}")


def show(run_id: int, path: Path) -> None:
    if not path.exists():
        raise SystemExit(f"snapshot not found: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    row = payload.get("row") or {}
    state = row.get("state_json") or {}
    events = state.get("event_log") or []
    print(f"snapshot: {path}")
    print(f"  taken:   {payload.get('_snapshot_ts')}")
    print(f"  run id:  {row.get('id')}")
    print(f"  status:  {row.get('status')}")
    print(f"  version: {row.get('version')}")
    print(f"  host_id: {row.get('host_id')}")
    print(f"  events:  {len(events)}")


def main(argv: list[str]) -> None:
    if len(argv) < 2:
        raise SystemExit(__doc__)
    action = argv[0]
    try:
        run_id = int(argv[1])
    except ValueError:
        raise SystemExit(f"run id must be an integer, got {argv[1]!r}")
    path = Path(argv[2]) if len(argv) > 2 else _default_snapshot_path(run_id)

    if action == "save":
        save(run_id, path)
    elif action == "restore":
        restore(run_id, path)
    elif action == "show":
        show(run_id, path)
    else:
        raise SystemExit(f"unknown action {action!r}; use save|restore|show")


if __name__ == "__main__":
    main(sys.argv[1:])
