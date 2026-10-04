"""Post-chargen skill improvement in frontend/shared.js, run for real under Node.

The play sheet's Manage Skills prices raises and new Concentrations/Specializations with these
helpers; the expected numbers are SR2 p.190's own worked examples.
"""
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from tests.test_adept_power_cost_frontend import _HARNESS

ROOT = Path(__file__).resolve().parent.parent

pytestmark = pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")


def _run(fn: str, arg):
    result = subprocess.run(
        ["node", "-e", _HARNESS, str(ROOT / "frontend" / "shared.js"), json.dumps({"fn": fn, "arg": arg})],
        capture_output=True, text=True, check=True,
    )
    return json.loads(result.stdout)


# Iris: Firearms 1, Pistols 3, Beretta 101T 5 (SR2 p.190).
IRIS = {"name": "Firearms", "group": "combat", "rating": 1,
        "concs": [{"name": "Pistols", "rating": 3}],
        "specs": [{"name": "Beretta 101T", "rating": 5, "conc": "Pistols"}]}


def _cost(skill, tier, new_rating):
    return _run("(a) => skillKarmaCost(a.s, a.tier, a.r)", {"s": skill, "tier": tier, "r": new_rating})


def test_raises_cost_what_the_book_charges():
    assert _cost(IRIS, "general", 2) == 4     # Firearms 1 -> 2
    assert _cost(IRIS, "conc", 4) == 6        # Pistols 3 -> 4
    assert _cost(IRIS, "spec", 6) == 6        # Beretta 101T 5 -> 6
    assert _cost({"name": "Spanish", "group": "language", "rating": 3}, "general", 4) == 4


def test_new_concentration_starts_above_the_general_skill_without_lowering_it():
    # Firearms 4 wanting Pistols at 5 costs 5 x 1.5, rounded up to 8.
    skill = {"name": "Firearms", "rating": 4, "concs": [], "specs": []}
    assert _run("(s) => newConcRating(s)", skill) == 5
    assert _cost(skill, "conc", 5) == 8
    # A second Concentration on a skill that already has one prices the same way.
    assert _run("(s) => newConcRating(s)", IRIS) == 2


def test_new_specialization_builds_on_its_concentration_or_the_general_skill():
    # Without an appropriate Concentration it's based on the general skill: Firearms 4 ->
    # Remington Roomsweeper at 5 for 5 karma.
    skill = {"name": "Firearms", "rating": 4, "concs": [], "specs": []}
    assert _run("(s) => newSpecRating(s, 'Shotguns')", skill) == 5
    assert _cost(skill, "spec", 5) == 5
    # With the Concentration, one above it.
    assert _run("(s) => newSpecRating(s, 'Pistols')", IRIS) == 4


def test_skill_parts_list_each_specialization_after_its_concentration():
    skill = {"name": "Bike", "rating": 2,
             "concs": [{"name": "Two-wheeler", "rating": 4}, {"name": "Racing", "rating": 3}],
             "specs": [{"name": "Rapier", "rating": 3, "conc": "Three-wheeler"},
                       {"name": "Honda Viking", "rating": 6, "conc": "Two-wheeler"}]}
    parts = _run("(s) => skillParts(s).map(p => p.tier + ':' + p.name + ' ' + p.rating)", skill)
    assert parts == ["general:Bike 2", "conc:Two-wheeler 4", "spec:Honda Viking 6",
                     "conc:Racing 3", "spec:Rapier 3"]
