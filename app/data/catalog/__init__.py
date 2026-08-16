"""SR2 reference catalogs (weapons, armor, cyberware, gear, spells, adept
powers, vehicles) plus the chargen rules bundle.

Data lives as committed JSON siblings in this package, generated from the
reference material under ``docs/reference-data/`` by ``tools/build_catalog.py``.
Loading is lazy and cached. The per-campaign book toggle (stored on
``CampaignState.enabled_books``) filters item catalogs by each item's ``src``
book code; ``SR2`` core is always included.
"""
from __future__ import annotations

import json
import threading
from functools import lru_cache
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent

# Item catalogs that carry a per-item ``src`` book code and are book-filtered.
# Cyberware (Essence cost) and bioware (Body Index cost) are separate catalogs.
ITEM_CATALOGS = (
    "weapons", "armor", "cyberware", "bioware", "gear", "spells", "adept_powers", "vehicles",
)

# SR2 core is always on and cannot be toggled off.
CORE_BOOK = "SR2"
CORE_BOOK_NAME = "Shadowrun, Second Edition"

# Toggleable official sourcebooks, in display order (see plan doc S7).
OFFICIAL_BOOKS = {
    "SSC": "Street Samurai Catalog",
    "FOF": "Fields of Fire",
    "SHADOW": "Shadowtech",
    "CYB": "Cybertechnology",
    "GRIM": "Grimoire 2nd Edition",
    "AWK": "Awakenings",
    "RIG2": "Rigger 2",
}

# A single "Fan Content" toggle expands to these non-canon fan works (default off).
FAN_TOGGLE = "FAN"
FAN_TOGGLE_NAME = "Fan Content"
FAN_BOOKS = {
    "BSW": "Blackhand's Street Weapons 2057",
    "RG": "Running Gear",
}

# Everything a campaign may switch on (SR2 is implicit and excluded here).
TOGGLEABLE_CODES = set(OFFICIAL_BOOKS) | {FAN_TOGGLE}


@lru_cache(maxsize=None)
def _load(name: str) -> object:
    with (_DATA_DIR / f"{name}.json").open(encoding="utf-8") as fh:
        return json.load(fh)


def get_catalog(name: str) -> list[dict]:
    """Return the full, unfiltered item list for ``name`` (one of ITEM_CATALOGS)."""
    if name not in ITEM_CATALOGS:
        raise KeyError(name)
    return _load(name)  # type: ignore[return-value]


def get_rules() -> dict:
    """Return the SR2 chargen rules bundle (priorities, metatypes, totems, ...)."""
    return _load("builder")  # type: ignore[return-value]


def get_skills() -> list[dict]:
    """Return the raw skill definitions (name, attr, group, optional conc) from the rules bundle."""
    return list(get_rules().get("skills", []))  # type: ignore[union-attr]


def get_skill_specs() -> dict:
    """Return the curated skill -> concentration -> [specializations] overlay.

    This layer lives beside the generated catalogs so a ``build_catalog.py``
    rebuild never clobbers it. It is read-only at runtime (the builder consumes
    it); the committed ``skill_specs.json`` is the source of truth.
    """
    return _load("skill_specs")  # type: ignore[return-value]


def get_vehicle_classes() -> dict:
    """Return the curated vehicle-name -> {skill, conc} classification overlay.

    A GM assigns each vehicle a parent piloting skill + concentration; the
    committed ``vehicle_classes.json`` is the source of truth and drives the
    character builder's ``(SV)`` specialization expansion.
    """
    return _load("vehicle_classes")  # type: ignore[return-value]


_CYBERWARE_FILE = _DATA_DIR / "cyberware.json"
_CYBERWARE_WRITE_LOCK = threading.Lock()


def append_cyberware(item: dict) -> dict:
    """Append one item to the committed cyberware catalog and drop the load cache
    so it is visible immediately (no restart).

    The file is rewritten in the existing one-object-per-line array style. Raises
    ``ValueError`` if an item with the same (case-insensitive) name already exists.
    The write is serialized under a process lock and re-reads the file fresh inside
    the critical section, so concurrent appends don't lose each other (single-process
    dev/admin tool -- not safe across multiple worker processes or an ephemeral fs).
    """
    name = str(item.get("n", "")).strip().lower()
    with _CYBERWARE_WRITE_LOCK:
        with _CYBERWARE_FILE.open(encoding="utf-8") as fh:
            items = json.load(fh)
        if any(str(it.get("n", "")).strip().lower() == name for it in items):
            raise ValueError(f"Cyberware named {item.get('n')!r} already exists")
        items.append(item)
        body = "[\n" + ",\n".join(json.dumps(it, ensure_ascii=False) for it in items) + "\n]\n"
        with _CYBERWARE_FILE.open("w", encoding="utf-8") as fh:
            fh.write(body)
        _load.cache_clear()
    return item


def resolve_src_codes(enabled: list[str] | None) -> set[str]:
    """Expand a campaign's enabled toggles into the set of allowed ``src`` codes.

    ``SR2`` is always included; ``FAN`` expands to the individual fan-book codes.
    """
    enabled_set = set(enabled or [])
    codes = {CORE_BOOK}
    codes |= enabled_set & set(OFFICIAL_BOOKS)
    if FAN_TOGGLE in enabled_set:
        codes |= set(FAN_BOOKS)
    return codes


def filter_catalog(name: str, enabled: list[str] | None) -> list[dict]:
    """Return the items of catalog ``name`` whose ``src`` is in an enabled book."""
    allowed = resolve_src_codes(enabled)
    return [item for item in get_catalog(name) if item.get("src") in allowed]


def normalize_enabled(codes: list[str] | None) -> list[str]:
    """Drop unknown codes and dedupe, returning official books in display order
    followed by the FAN toggle when present."""
    code_set = set(codes or [])
    ordered = [code for code in OFFICIAL_BOOKS if code in code_set]
    if FAN_TOGGLE in code_set:
        ordered.append(FAN_TOGGLE)
    return ordered
