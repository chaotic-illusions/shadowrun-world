"""Catalog data-integrity and book-filtering tests."""

import pytest

from app.data import catalog as cat
from app.schemas.catalog import BookSettingsUpdate

# Item counts frozen from the committed catalog JSON (see tools/build_catalog.py).
# Cyberware is intentionally omitted -- it is actively curated, so it is checked with a
# resilient floor in test_cyberware_and_bioware_split_by_cost_type instead of an exact count.
EXPECTED_COUNTS = {
    "weapons": 526,
    "armor": 35,
    "bioware": 25,
    "gear": 118,
    "spells": 217,
    "adept_powers": 37,
    "vehicles": 169,
}


@pytest.mark.parametrize("name,count", EXPECTED_COUNTS.items())
def test_catalog_loads_expected_counts(name, count):
    items = cat.get_catalog(name)
    assert len(items) == count
    assert all("src" in item for item in items)


def test_every_item_src_is_a_known_book():
    known = {cat.CORE_BOOK} | set(cat.OFFICIAL_BOOKS) | set(cat.FAN_BOOKS)
    # VR2 appears in the raw gear pull (decks/programs) but is intentionally not a
    # character-builder book; it is never enable-able, so it is excluded by filtering.
    known.add("VR2")
    for name in cat.ITEM_CATALOGS:
        srcs = {item.get("src") for item in cat.get_catalog(name)}
        assert srcs <= known, f"{name} has unexpected src codes: {srcs - known}"


def test_cyberware_and_bioware_split_by_cost_type():
    cyber = cat.get_catalog("cyberware")
    bio = cat.get_catalog("bioware")
    # Bioware costs Body Index (bio == true); cyberware costs Essence (no bio flag).
    assert all(item.get("bio") for item in bio)
    assert not any(item.get("bio") for item in cyber)
    # Cyberware is actively curated; guard against a broken/empty load with a floor, not an exact count.
    assert len(cyber) >= 150
    # Cyberware and bioware are a clean partition (no shared names).
    assert not ({i["n"] for i in cyber} & {i["n"] for i in bio})


def test_rules_bundle_has_core_sections():
    rules = cat.get_rules()
    for key in ("priority", "metatypes", "totems", "skills", "foci", "archetypes", "chargen"):
        assert key in rules
    assert "pdfmap" not in rules  # reference-site-only, intentionally excluded


def test_resolve_src_codes_always_includes_core():
    assert cat.resolve_src_codes([]) == {"SR2"}
    assert cat.resolve_src_codes(None) == {"SR2"}
    assert cat.resolve_src_codes(["SSC"]) == {"SR2", "SSC"}


def test_fan_toggle_expands_to_fan_books():
    codes = cat.resolve_src_codes(["FAN"])
    assert codes == {"SR2", "BSW", "RG"}


def test_filter_catalog_core_only_excludes_expansions_and_vr2():
    weapons = cat.filter_catalog("weapons", [])
    assert weapons, "core weapons should be present"
    assert {w["src"] for w in weapons} == {"SR2"}

    # Vehicles are RIG2-gated: none appear until RIG2 is enabled.
    assert cat.filter_catalog("vehicles", []) == []
    assert len(cat.filter_catalog("vehicles", ["RIG2"])) == EXPECTED_COUNTS["vehicles"]


def test_filter_catalog_ssc_adds_only_ssc_items():
    core = cat.filter_catalog("weapons", [])
    with_ssc = cat.filter_catalog("weapons", ["SSC"])
    assert len(with_ssc) > len(core)
    assert {w["src"] for w in with_ssc} == {"SR2", "SSC"}


def test_fan_content_only_via_fan_toggle():
    with_fan = cat.filter_catalog("weapons", ["FAN"])
    assert any(w["src"] == "BSW" for w in with_fan)
    # Enabling an official book must not pull in fan content.
    official = cat.filter_catalog("weapons", ["SSC", "FOF"])
    assert not any(w["src"] in cat.FAN_BOOKS for w in official)


def test_normalize_enabled_orders_and_drops_unknown():
    result = cat.normalize_enabled(["FAN", "RIG2", "SSC", "BOGUS", "SSC"])
    assert result == ["SSC", "RIG2", "FAN"]


def test_book_settings_update_rejects_unknown_codes():
    BookSettingsUpdate(enabled=["SSC", "FAN"])  # ok
    with pytest.raises(ValueError):
        BookSettingsUpdate(enabled=["SR2"])  # SR2 is implicit, not toggleable
    with pytest.raises(ValueError):
        BookSettingsUpdate(enabled=["NOPE"])
