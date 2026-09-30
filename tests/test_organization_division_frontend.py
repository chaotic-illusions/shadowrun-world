"""The org editors' division helpers in frontend/shared.js, run for real under Node.

Both editors (manage-organizations.html and world-state.js) build and read division rows with
the shared divisionRowHtml/readDivisionRow/sortDivisions helpers, so exercising those covers the
round trip. A fake row object stands in for the DOM row readDivisionRow walks.
"""
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from app.schemas.organization import OrganizationDivision

ROOT = Path(__file__).resolve().parent.parent

pytestmark = pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")

_HARNESS = r"""
const vm = require('vm'), fs = require('fs');
const noop = () => {};
const el = () => ({addEventListener: noop, appendChild: noop, style: {}, setAttribute: noop,
                   classList: {add: noop, remove: noop, contains: () => false}});
const ctx = {console, window: {addEventListener: noop, matchMedia: () => ({matches: false})},
  document: {addEventListener: noop, createElement: el, getElementById: () => null,
             querySelector: () => null, querySelectorAll: () => [], head: el(), body: el()},
  localStorage: {getItem: () => null}, sessionStorage: {getItem: () => null},
  setInterval: noop, setTimeout: noop, navigator: {}};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(process.argv[1], 'utf8'), ctx);
const input = JSON.parse(process.argv[2]);
const out = vm.runInContext(`(${input.fn})`, ctx)(input.arg);
process.stdout.write(JSON.stringify(out));
"""


def _run(fn: str, arg):
    result = subprocess.run(
        ["node", "-e", _HARNESS, str(ROOT / "frontend" / "shared.js"), json.dumps({"fn": fn, "arg": arg})],
        capture_output=True, text=True, check=True,
    )
    return json.loads(result.stdout)


_STORED = {
    "id": "6f1c6f2e-4a55-4b8e-9a8e-0d6f7b8c9a01", "name": "Old Name", "kind": "division", "tier": 3,
    "source_adventure": "Queen Euphoria", "leadership": [{"name": "Boss"}], "ally_ids": [4],
    "visibility": "listed", "revealed": False, "notes": "old gm note",
}


def test_read_division_row_merges_edits_over_hidden_fields():
    # The editor shows name/kind/reveal/intel/notes; everything else rides along in _divisionData.
    fn = """(stored) => readDivisionRow({
      _divisionData: stored,
      querySelectorAll: () => [
        {dataset: {field: 'id'}, type: 'hidden', value: stored.id},
        {dataset: {field: 'name'}, type: 'text', value: '  New Name '},
        {dataset: {field: 'kind'}, type: 'select-one', value: 'subsidiary'},
        {dataset: {field: 'revealed'}, type: 'checkbox', checked: true},
        {dataset: {field: 'description'}, type: 'textarea', value: ''},
        {dataset: {field: 'notes'}, type: 'textarea', value: 'new gm note'},
      ],
    })"""
    division = _run(fn, _STORED)

    assert division["name"] == "New Name"
    assert division["kind"] == "subsidiary"
    assert division["description"] is None
    assert division["notes"] == "new gm note"
    # Reveal is the only switch: saved as unlisted + the checkbox.
    assert division["visibility"] == "unlisted" and division["revealed"] is True
    # Hidden fields survive the round trip, and the payload is one the API accepts.
    assert division["source_adventure"] == "Queen Euphoria"
    assert division["leadership"] == [{"name": "Boss"}] and division["ally_ids"] == [4]
    OrganizationDivision.model_validate(division)


def test_division_row_html_escapes_and_starts_from_listed_or_revealed():
    html = _run("(d) => divisionRowHtml(d, d.id, '<option value=\"division\">division</option>', 'noop()')",
                {**_STORED, "name": '<img src=x onerror=alert(1)>'})
    assert "<img" not in html and "&lt;img" in html
    assert 'data-field="revealed" checked' in html  # listed legacy entry starts revealed
    assert 'value="division" selected' in html


def test_sort_divisions_revealed_first_then_name():
    order = _run("(ds) => sortDivisions(ds).map(d => d.name)", [
        {"name": "b hidden", "visibility": "unlisted", "revealed": False},
        {"name": "z shown", "visibility": "unlisted", "revealed": True},
        {"name": "a hidden", "visibility": "unlisted"},
        {"name": "m listed", "visibility": "listed"},
    ])
    assert order == ["m listed", "z shown", "a hidden", "b hidden"]
