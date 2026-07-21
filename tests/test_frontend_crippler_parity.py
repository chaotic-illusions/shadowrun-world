"""Frontend <-> backend parity for the attribute-crippling family (drift guard).

No Node build step exists, so this is a STATIC text gate: it reads the shipped frontend
files and asserts that every decker attribute-attack program the backend recognises
(``mr._PROGRAM_ATTR``: poison/restrict/reveal) is exposed identically on every UI surface,
and -- critically -- that the Strike Back label's attribute matches the backend table
(``mr._ATTRIBUTE_ATTACK``). If the backend mapping changes without the UI following (or
vice versa), this fails instead of shipping a silent gap.

Surfaces checked:
  1. matrix-run.html  -- runtime Strike Back <option>, with the correct "(vs Attr)" label
  2. matrix-run.html  -- deck-config utility input (cfg-u-<program>)
  3. matrix-run.html  -- UTIL_FIELD_MAP program -> field id
  4. deck-workshop.html -- program catalog entry (name: "<Program>")
"""
from __future__ import annotations

from pathlib import Path

from app.routers import matrix_runs as mr

_FRONTEND = Path(__file__).resolve().parents[1] / "frontend"
_RUN_HTML = (_FRONTEND / "matrix-run.html").read_text(encoding="utf-8")
_WORKSHOP_HTML = (_FRONTEND / "deck-workshop.html").read_text(encoding="utf-8")


def test_strike_back_offers_every_backend_attribute_program():
    """Each poison/restrict/reveal program is a Strike Back option whose label names the SAME
    attribute the backend table attacks (poison->Bod, restrict->Evasion, reveal->Masking)."""
    for program, attr in mr._PROGRAM_ATTR.items():
        assert f'<option value="{program}"' in _RUN_HTML, (
            f"Strike Back UI is missing an option for '{program}'")
        label = f"{program.capitalize()} (vs {attr.capitalize()})"
        assert label in _RUN_HTML, (
            f"Strike Back label for '{program}' must read '{label}' to match the backend "
            f"_ATTRIBUTE_ATTACK mapping ({program} -> {attr})")


def test_config_and_field_map_expose_every_attribute_program():
    """Each program has a deck-config rating input AND a UTIL_FIELD_MAP entry (so the pool-prompt
    default and the loadout read both resolve)."""
    for program in mr._PROGRAM_ATTR:
        assert f'id="cfg-u-{program}"' in _RUN_HTML, (
            f"deck-config is missing the cfg-u-{program} rating input")
        assert f"{program}: 'cfg-u-{program}'" in _RUN_HTML, (
            f"UTIL_FIELD_MAP is missing the '{program}' -> 'cfg-u-{program}' mapping")


def test_deck_workshop_catalog_lists_every_attribute_program():
    """Each program appears in the deck-workshop build catalog so a decker can actually load it."""
    for program in mr._PROGRAM_ATTR:
        assert f'name: "{program.capitalize()}"' in _WORKSHOP_HTML, (
            f"deck-workshop program catalog is missing '{program.capitalize()}'")
