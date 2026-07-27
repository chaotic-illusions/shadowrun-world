from __future__ import annotations

import pytest
from pydantic import ValidationError
from types import SimpleNamespace

from app.routers import matrix_hosts as hosts_router
from app.routers import matrix_runs as runs_router
from app.schemas.matrix_host import MatrixHostCreate, MatrixHostUpdate
from app.services.matrix_host_config import normalize_host_config


def test_duplicate_paydata_names_receive_distinct_stable_ids_and_defenses():
    config = {
        "paydata": [
            {
                "name": "Payroll",
                "defense": {"data_bomb_rating": 5, "scramble_rating": None},
            },
            {
                "name": "Payroll",
                "defense": {
                    "data_bomb_rating": None,
                    "scramble_rating": 7,
                    "scramble_variant": "poison",
                },
            },
        ],
    }

    normalized = normalize_host_config(config)
    first, second = normalized["paydata"]

    assert first["id"].startswith("pd_")
    assert second["id"].startswith("pd_")
    assert first["id"] != second["id"]
    assert normalized["data_bombs"] == [
        {"target": f"files::{first['id']}", "rating": 5}
    ]
    assert normalized["scrambles"] == [{
        "target_key": f"files::file::{second['id']}",
        "rating": 7,
        "variant": "poison",
    }]


def test_update_without_ids_preserves_existing_ids_by_row():
    existing = normalize_host_config({
        "paydata": [{"name": "Same"}, {"name": "Same"}],
    })
    updated = normalize_host_config({
        "paydata": [{"name": "Renamed"}, {"name": "Same"}],
    }, existing)

    assert [item["id"] for item in updated["paydata"]] == [
        item["id"] for item in existing["paydata"]
    ]


def test_legacy_file_defense_arrays_are_converted_not_dropped():
    normalized = normalize_host_config({
        "paydata": [{"name": "Archive"}],
        "data_bombs": [{"target": "files::Archive", "rating": 4}],
        "scrambles": [{
            "target_key": "files::file::Archive", "rating": 6, "variant": "exploding",
        }],
    })
    paydata_id = normalized["paydata"][0]["id"]

    assert normalized["data_bombs"][0]["target"] == f"files::{paydata_id}"
    assert normalized["scrambles"][0]["target_key"] == f"files::file::{paydata_id}"


def test_unsupported_scramble_variants_are_dropped():
    normalized = normalize_host_config({
        "paydata": [],
        "scrambles": [
            {"target_key": "files::file::old", "rating": 6, "variant": "standard"},
            {"target_key": "files::file::bomb", "rating": 6, "variant": "exploding"},
            {"target_key": "files::file::poison", "rating": 6, "variant": "poison"},
        ],
    })

    assert [item["variant"] for item in normalized["scrambles"]] == [
        "exploding", "poison",
    ]


def test_duplicate_name_target_id_selects_only_requested_row():
    state = {"paydata": [
        {"id": "pd_first", "name": "Payroll", "located": True},
        {"id": "pd_second", "name": "Payroll", "located": True},
    ]}

    selected = runs_router._paydata_for_target(state, "pd_second")

    assert selected is state["paydata"][1]


class _Result:
    def __init__(self, rows):
        self.rows = rows

    def scalars(self):
        return self

    def first(self):
        return self.rows[0] if self.rows else None

    def all(self):
        return self.rows


class _DeleteDB:
    def __init__(self, target, parents):
        self.results = [_Result([target]), _Result(parents)]
        self.deleted = None
        self.committed = False

    async def execute(self, _query):
        return self.results.pop(0)

    async def delete(self, row):
        self.deleted = row

    async def flush(self):
        pass

    async def commit(self):
        self.committed = True


@pytest.mark.asyncio
async def test_delete_host_prunes_inbound_trap_door_edges():
    target = SimpleNamespace(id=7, trap_doors_json=None)
    parent = SimpleNamespace(
        id=2,
        trap_doors_json=[
            {"id": "keep", "destination_host_id": 9},
            {"id": "remove", "destination_host_id": 7},
        ],
    )
    db = _DeleteDB(target, [parent])

    await hosts_router.delete_host(7, db=db)

    assert parent.trap_doors_json == [{"id": "keep", "destination_host_id": 9}]
    assert db.deleted is target
    assert db.committed is True


@pytest.mark.parametrize("schema", [MatrixHostCreate, MatrixHostUpdate])
def test_trap_destination_flag_is_not_client_writable(schema):
    with pytest.raises(ValidationError):
        schema(name="Host", is_trap_door_dest=True)