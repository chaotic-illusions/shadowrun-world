import os
import subprocess
import sys


FORMER_HEAD = "d5f2a3c81b47"
CURRENT_HEAD = "6b1e4d8a2c73"


def _alembic(database_path, *arguments):
    env = os.environ.copy()
    env["DATABASE_URL"] = f"sqlite+aiosqlite:///{database_path.as_posix()}"
    return subprocess.run(
        [sys.executable, "-m", "alembic", *arguments],
        check=True,
        capture_output=True,
        text=True,
        env=env,
    )


def test_empty_database_upgrades_to_head(tmp_path):
    database = tmp_path / "empty.db"
    _alembic(database, "upgrade", "head")
    current = _alembic(database, "current")
    assert f"{CURRENT_HEAD} (head)" in current.stdout


def test_former_head_database_upgrades_without_replaying_baseline(tmp_path):
    database = tmp_path / "former-head.db"
    _alembic(database, "upgrade", FORMER_HEAD)

    upgraded = _alembic(database, "upgrade", "head")
    assert f"Running upgrade {FORMER_HEAD} -> {CURRENT_HEAD}" in upgraded.stderr
    assert "pre_matrix_baseline" not in upgraded.stderr

    current = _alembic(database, "current")
    assert f"{CURRENT_HEAD} (head)" in current.stdout