"""Adept power pricing in frontend/shared.js, run for real under Node.

The character builder and the play sheet both price an owned power with adeptPowerCost and decide
"bought in levels" with adeptPowerIsRated, so the sheet can't show a different cost than chargen
charged.
"""
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from app.data import catalog as cat

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
process.stdout.write(JSON.stringify(out === undefined ? null : out));
"""


def _run(fn: str, arg):
    result = subprocess.run(
        ["node", "-e", _HARNESS, str(ROOT / "frontend" / "shared.js"), json.dumps({"fn": fn, "arg": arg})],
        capture_output=True, text=True, check=True,
    )
    return json.loads(result.stdout)


def _power(name):
    return next(p for p in cat.get_catalog("adept_powers") if p["n"] == name)


def _cost(name, line, tier_base=None):
    return _run("(a) => adeptPowerCost(a.line, a.pw, a.base)",
                {"line": {"name": name, **line}, "pw": _power(name), "base": tier_base})


def test_table_priced_power_costs_its_level_entry():
    # Increased Reflexes is 1 / 4 / 6 PP, not level x 1 -- what the play sheet used to show.
    assert _cost("Increased Reflexes", {"rated": True, "lvl": 3, "ppEach": 1}) == 6
    assert _cost("Killing Hands", {"rated": True, "lvl": 2, "ppEach": 0.5}) == 1


def test_per_level_power_multiplies():
    assert _cost("Pain Resistance", {"rated": True, "lvl": 3, "ppEach": 0.5}) == 1.5
    assert _cost("Astral Perception", {"rated": False, "lvl": 1, "ppEach": 2}) == 2


def test_tier_priced_power_needs_the_builder_or_the_stored_cost():
    line = {"rated": True, "lvl": 3, "ppEach": 0.5, "attr": "strength"}
    # Strength 2, Racial Maximum 6: ratings 3 (half max), 4 and 5 cost 0.5 + 1 + 1.
    assert _cost("Improved Physical Attributes", line, [2, 6]) == 2.5
    # The play sheet has no Racial Maximum: it reads the cost the builder stored, else can't tell.
    assert _cost("Improved Physical Attributes", {**line, "pp": 2.5}) == 2.5
    assert _cost("Improved Physical Attributes", line) is None


def test_rated_rule_is_one_function_for_shop_and_kits():
    powers = [{k: p.get(k) for k in ("n", "pp", "tiers", "rated")} for p in cat.get_catalog("adept_powers")]
    rated = set(_run("(ps) => ps.filter(adeptPowerIsRated).map(p => p.n)", powers))
    assert {"Combat Sense", "Killing Hands", "Pain Resistance", "Improved Physical Attributes"} <= rated
    assert not {"Astral Perception", "Improved Ability", "Quick Draw"} & rated
