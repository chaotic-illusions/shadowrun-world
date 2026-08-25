import os
import subprocess
import sys
from pathlib import Path

from alembic.config import Config
from alembic.script import ScriptDirectory


# Derived from the actual migration graph rather than hardcoded -- a hardcoded revision ID here
# went stale (and both tests failed) every time a new migration landed without this file being
# updated to match. CURRENT_HEAD is whatever `alembic heads` reports right now; FORMER_HEAD is its
# immediate parent, so "upgrade from FORMER_HEAD to head" always exercises exactly the most recent
# migration step, whatever that happens to be.
_REPO_ROOT = Path(__file__).resolve().parent.parent
_ALEMBIC_CFG = Config(str(_REPO_ROOT / "alembic.ini"))
# alembic.ini's script_location is a bare relative path ("alembic"), resolved against the process's
# cwd rather than the ini file's own directory -- pin it absolute so this works regardless of where
# pytest is invoked from.
_ALEMBIC_CFG.set_main_option("script_location", str(_REPO_ROOT / "alembic"))
_SCRIPTS = ScriptDirectory.from_config(_ALEMBIC_CFG)
CURRENT_HEAD = _SCRIPTS.get_current_head()
FORMER_HEAD = _SCRIPTS.get_revision(CURRENT_HEAD).down_revision


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