import hashlib
import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

from seed import export_world_data


ROOT = Path(__file__).resolve().parent.parent
SOURCE_DATABASE = ROOT / "data" / "prod-snapshot" / "2026-09-15" / "shadowrun_prod.db"
WORLD_SEED = ROOT / "data" / "world_seed.json"
EXPECTED_SOURCE_SHA256 = "0bbaa01dc98cbcb877818c0d3d68ea1d68f2ad51bb52864f2fe72c65880679e9"


def _portable_content(data):
    return {
        key: value
        for key, value in data.items()
        if key != "_source_database_sha256"
    }


def _table_counts(database_path):
    with sqlite3.connect(database_path) as database:
        return {
            table: database.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
            for table in (
                "organizations",
                "locations",
                "characters",
                "contacts",
                "reputations",
                "org_standings",
                "rtgs",
                "matrix_hosts",
                "matrix_runs",
                "adventure_logs",
                "log_characters",
                "log_locations",
                "log_organizations",
                "campaign_state",
            )
        }


def test_complete_world_seed_round_trip_excludes_only_pc_owned_data(tmp_path):
    source_hash = hashlib.sha256(SOURCE_DATABASE.read_bytes()).hexdigest()
    assert source_hash == EXPECTED_SOURCE_SHA256

    expected = json.loads(WORLD_SEED.read_text(encoding="utf-8"))
    assert expected == export_world_data(SOURCE_DATABASE)
    target_database = tmp_path / "seeded-world.db"

    script = r'''
import contextlib
import io
import json
import os
from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app
from seed import _seed_data

seed_data = json.loads(Path(os.environ["SEED_FILE"]).read_text(encoding="utf-8"))
with TestClient(app) as client:
    client.headers.update({"X-Admin-Token": os.environ["BOOTSTRAP_ADMIN_KEY"]})
    with contextlib.redirect_stdout(io.StringIO()):
        _seed_data(client, seed_data, {}, {}, {}, {})
print("seed complete")
'''
    environment = os.environ.copy()
    environment["DATABASE_URL"] = (
        f"sqlite+aiosqlite:///{target_database.resolve().as_posix()}"
    )
    environment["BOOTSTRAP_ADMIN_KEY"] = "full-world-seed-test-admin"
    environment["SEED_FILE"] = str(WORLD_SEED.resolve())
    result = subprocess.run(
        [sys.executable, "-c", script],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    assert result.returncode == 0, (
        f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )

    actual = export_world_data(target_database)
    assert _portable_content(actual) == _portable_content(expected)

    source_counts = _table_counts(SOURCE_DATABASE)
    target_counts = _table_counts(target_database)
    assert source_counts == {
        "organizations": 821,
        "locations": 1183,
        "characters": 872,
        "contacts": 11,
        "reputations": 7,
        "org_standings": 6,
        "rtgs": 67,
        "matrix_hosts": 7,
        "matrix_runs": 0,
        "adventure_logs": 1,
        "log_characters": 2,
        "log_locations": 1,
        "log_organizations": 1,
        "campaign_state": 1,
    }
    assert target_counts == {
        **source_counts,
        "characters": 862,
        "contacts": 0,
        "reputations": 0,
        "org_standings": 0,
        "log_characters": 0,
    }

    with sqlite3.connect(target_database) as database:
        assert database.execute(
            "SELECT COUNT(*) FROM characters WHERE is_pc = 1"
        ).fetchone()[0] == 0
        assert database.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
        assert database.execute("PRAGMA foreign_key_check").fetchall() == []

    assert hashlib.sha256(SOURCE_DATABASE.read_bytes()).hexdigest() == source_hash
