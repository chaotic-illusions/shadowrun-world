from types import SimpleNamespace

from scripts.adventure_ingest.loader import Loader, _append, _merge_division


class _RecordingApi:
    base = "test"

    def __init__(self):
        self.posts = []

    def post(self, path, body):
        self.posts.append((path, body))
        return {"id": len(self.posts), **body}


def test_create_payloads_default_to_adventure_scope_and_preserve_explicit_scope():
    api = _RecordingApi()
    spec = SimpleNamespace(
        ADVENTURE="Example",
        ORGS=[{"name": "Default Org"}, {"name": "Reference Org", "catalog_scope": "reference"}],
        LOCATIONS=[
            {"name": "Default Location"},
            {"name": "Reference Location", "catalog_scope": "reference"},
        ],
        NPCS=[
            {"name": "Default NPC"},
            {"name": "Reference NPC", "catalog_scope": "reference"},
        ],
    )
    loader = Loader(api, spec)
    loader._create_orgs()
    loader._create_locations()
    loader._create_npcs()

    payloads = {body["name"]: body for _, body in api.posts}
    assert payloads["Reference Org"]["catalog_scope"] == "reference"
    assert payloads["Reference Location"]["catalog_scope"] == "reference"
    assert "city" not in payloads["Reference Location"]
    assert payloads["Reference NPC"]["catalog_scope"] == "reference"
    assert loader.report["skipped"] == [
        "org archived: Default Org",
        "location archived: Default Location",
        "npc archived: Default NPC",
    ]


def test_append_skips_legacy_text_already_present():
    assert _append("Existing source text plus later detail.", "Example", "Existing source text") is None


def test_append_skips_existing_adventure_marker():
    assert _append("-- Example --\nExisting text", "Example", "Replacement text") is None


def test_append_adds_new_marked_source_block():
    assert _append("Existing text", "Example", "New text") == (
        "Existing text\n\n-- Example --\nNew text"
    )


def test_merge_division_preserves_structure_and_appends_later_source():
    existing = {
        "id": "11111111-1111-4111-8111-111111111111",
        "name": "Unit 13",
        "kind": "unit",
        "description": "Earlier description",
        "notes": "Earlier notes",
        "leadership": [],
        "ally_ids": [8],
    }
    addition = {
        **existing,
        "description": "Later description",
        "notes": "Later notes",
        "leadership": [{"name": "Nell Miyamoto", "title": "Field team leader"}],
        "ally_ids": [333],
        "enemy_ids": [1],
    }

    merged = _merge_division(existing, addition, "Survival of the Fittest")

    assert merged["description"].endswith(
        "-- Survival of the Fittest --\nLater description"
    )
    assert merged["leadership"] == [
        {"name": "Nell Miyamoto", "title": "Field team leader"}
    ]
    assert merged["ally_ids"] == [8, 333]
    assert merged["enemy_ids"] == [1]


def test_merge_division_does_not_materialize_absent_empty_arrays():
    existing = {
        "id": "11111111-1111-4111-8111-111111111111",
        "name": "Tagmatic",
        "kind": "division",
        "ally_ids": [],
        "enemy_ids": [],
    }

    merged = _merge_division(existing, dict(existing), "Sprawl Sites")

    assert merged == existing
    assert "ltgs" not in merged
    assert "revealed_ally_ids" not in merged