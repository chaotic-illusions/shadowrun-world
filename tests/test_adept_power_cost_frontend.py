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


def test_mystic_armor_costs_half_a_point_per_level_even_on_older_lines():
    # House rule (SR3 core): 0.5 PP per level. A line bought at the old 1 PP still prices at 0.5.
    assert _cost("Mystic Armor", {"rated": True, "lvl": 3, "ppEach": 1}) == 1.5


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
    assert {"Combat Sense", "Killing Hands", "Pain Resistance", "Improved Physical Attributes",
            "Improved Ability"} <= rated
    # Improved Physical Senses is one line per sense: its "per level"-style text must not win.
    assert not {"Astral Perception", "Quick Draw", "Improved Physical Senses"} & rated


def test_improved_ability_is_priced_by_its_skill():
    # SR2 p.125: Athletics/Stealth 0.25, melee/throwing/projectile 0.5, Firearms/Gunnery 1 per die.
    line = {"rated": True, "lvl": 3, "ppEach": 0.25}
    assert _cost("Improved Ability", {**line, "skill": "Stealth"}) == 0.75
    assert _cost("Improved Ability", {**line, "skill": "Unarmed Combat"}) == 1.5
    assert _cost("Improved Ability", {**line, "skill": "Firearms"}) == 3
    # Every skill the power offers has a price, and every capped (Combat) skill is one it offers.
    pw = _power("Improved Ability")
    assert set(pw["skillCap"]) <= set(pw["skillChoice"])


def test_improved_ability_line_from_before_the_skill_pick_keeps_its_price():
    # Saved as a single 0.25 PP rank, with no skill and no rated flag.
    assert _cost("Improved Ability", {"rated": False, "lvl": 1, "ppEach": 0.25, "pp": 0.25}) == 0.25


def test_second_of_killing_hands_and_distance_strike_costs_double():
    # AWK p.116: whichever of the two is bought second costs double.
    assert _cost("Distance Strike", {"rated": False, "lvl": 1, "ppEach": 2, "doubled": True}) == 4
    assert _cost("Killing Hands", {"rated": True, "lvl": 3, "ppEach": 0.5, "doubled": True}) == 4
    assert _power("Killing Hands")["doublesWith"] == "Distance Strike"
    assert _power("Distance Strike")["doublesWith"] == "Killing Hands"


def test_improved_physical_senses_line_saved_in_levels_keeps_its_price():
    # Before it became one line per sense it was bought in levels: the sheet still shows what was paid.
    assert _cost("Improved Physical Senses", {"rated": True, "lvl": 3, "ppEach": 0.25}) == 0.75
    assert _cost("Improved Physical Senses", {"rated": False, "lvl": 1, "ppEach": 0.25, "pick": "Low-Light Vision"}) == 0.25


def test_fetish_is_owned_by_spell_category():
    # A fetish isn't tied to a spell: owning one of the category is enough.
    gear = {"gear": [
        {"n": "Expendable Fetish (Combat)", "spellCat": "combat"},
        {"n": "Medkit"},
    ]}
    owns = lambda c: _run("(a) => ownsFetishFor(a.gear, a.cat)", {"gear": gear, "cat": c})
    assert owns("combat") is True
    assert owns("health") is False
    fetish = next(g for g in cat.get_catalog("gear") if g["n"] == "Reusable Fetish (Healing)")
    assert (fetish["cost"], fetish["avail"], fetish["index"]) == (500, "3/24 hrs", 1)
    assert _run("(it) => makeGearLine(it, 'gear').spellCat", fetish) == "health"


def test_fetish_and_ritual_material_prices_match_the_table():
    gear = {g["n"]: g for g in cat.get_catalog("gear")}
    expendable = {"Combat": 20, "Detection": 5, "Healing": 50, "Illusion": 10, "Manipulation": 30}
    for label, cost in expendable.items():
        assert gear[f"Expendable Fetish ({label})"]["cost"] == cost
        assert gear[f"Reusable Fetish ({label})"]["cost"] == cost * 10
    ritual = {"Detection": 100, "Healing": 500, "Illusion": 100, "Manipulation": 1000}
    for label, per in ritual.items():
        assert gear[f"Ritual Sorcery Materials ({label})"]["costTbl"][3] == per * 4   # Force 4
    assert "Ritual Sorcery Materials (Combat)" not in gear
    assert gear["Elemental Conjuring Materials"]["costTbl"][5] == 6000              # Force 6
    assert "Spell Lock" not in gear                                                 # it's a focus, not gear


def test_spell_foci_bind_to_real_picks():
    foci = {f["n"]: f for f in cat.get_rules()["foci"]}
    spells = [{"name": "Stunbolt"}, {"name": "Heal"}]
    opts = lambda name: _run("(a) => focusTargetOptions(a.def, a.spells, a.spirits)",
                             {"def": foci[name], "spells": spells, "spirits": ["Fire", "Air"]})
    assert [o["value"] for o in opts("Specific Spell Focus")] == ["Heal", "Stunbolt"]
    assert [o["value"] for o in opts("Spell Lock")] == ["Heal", "Stunbolt"]
    assert [o["label"] for o in opts("Spell Category Focus")] == ["Combat", "Detection", "Healing", "Illusion", "Manipulation"]
    assert [o["value"] for o in opts("Spirit Focus")] == ["Air", "Fire"]
    assert opts("Power Focus") is None


def test_medicine_lodge_costs_500_per_force():
    lodge = next(g for g in cat.get_catalog("gear") if g["n"] == "Medicine Lodge")
    assert lodge["cat"] == "magical" and lodge["pg"] == 123
    line = _run("(it) => { const l = makeGearLine(it, 'gear'); l.rating = 4; return gearLineCost(l); }", lodge)
    assert line == 2000
