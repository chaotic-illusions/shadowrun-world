"""Executable regression tests for the shared frontend polling helper."""

import json
import shutil
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SHARED_JS = ROOT / "frontend" / "shared.js"
MANAGE_ORGS_HTML = ROOT / "frontend" / "manage-organizations.html"


def test_polling_helper_uses_a_floor_at_zero_pause_depth():
    source = SHARED_JS.read_text(encoding="utf-8")

    assert "let _pollPauseDepth = 0;" in source
    assert "function pausePoll()  { _pollPauseDepth++; }" in source
    assert "Math.max(0, _pollPauseDepth - 1)" in source
    assert "if (_pollPauseDepth === 0) loadFn();" in source


def test_organization_hydration_discards_stale_responses_and_errors():
    source = MANAGE_ORGS_HTML.read_text(encoding="utf-8")

    assert "const requestId = ++orgEditRequestId;" in source
    assert "loadOrgForEdit(id, requestId);" in source
    assert "function closeModal() {\n  orgEditRequestId++;" in source
    assert source.count("if (requestId !== orgEditRequestId) return;") == 2


@pytest.mark.skipif(shutil.which("node") is None, reason="Node.js is required")
def test_polling_remains_paused_until_all_nested_pauses_resume():
    source = SHARED_JS.read_text(encoding="utf-8")
    helper = source[source.index("let _pollPauseDepth"):source.index("// -- Auth constants")]
    script = f"""
let tick;
function setInterval(fn) {{ tick = fn; }}
{helper}
let calls = 0;
startPolling(() => calls++);
pausePoll();
pausePoll();
tick();
resumePoll();
tick();
resumePoll();
tick();
resumePoll();
tick();
console.log(JSON.stringify({{ calls, depth: _pollPauseDepth }}));
"""

    result = subprocess.run(
        ["node", "-e", script],
        check=True,
        capture_output=True,
        text=True,
    )

    assert json.loads(result.stdout) == {"calls": 2, "depth": 0}