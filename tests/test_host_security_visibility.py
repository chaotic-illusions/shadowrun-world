"""Server-side hiding of matrix-host Security Ratings (SC/SV) on the org pages.

A matrix_host LTG entry's ``san_access_rating`` (e.g. "Red-9") is a decker secret: it must
stay hidden from players on the organizations / world-state intel pages until a decker
discovers the host's security in a run (Analyze Host). Discovery flips a persistent
``san_revealed`` flag on the entry; admins always see the rating.

Covers the three seams that enforce this:

  * ``host_visibility.sync_host_security_to_org(..., mark_revealed=...)`` -- only a decker
    discovery (mark_revealed=True) flips ``san_revealed``; a plain value sync never does.
  * ``organizations._serialize_org`` -- redacts ``san_access_rating`` from non-admin GET
    payloads for entries that are not yet ``san_revealed``; admins and revealed entries keep it.
  * ``organizations._preserve_san_revealed`` -- a GM edit (which never sends the flag) must
    not wipe a prior discovery.
"""
from __future__ import annotations

import asyncio
from datetime import datetime, UTC
from types import SimpleNamespace

from app.routers.organizations import _serialize_org, _preserve_san_revealed
from app.routers.matrix_hosts import list_hosts, ltg_catalog
from app.schemas.organization import OrganizationRead
from app.services.host_visibility import sync_host_security_to_org


# -- helpers ---------------------------------------------------------------

def _org_obj(ltgs, org_id=1, is_active=True, name="Ares Macrotechnology"):
    """A minimal object exposing every OrganizationRead field for model_validate."""
    return SimpleNamespace(
        id=org_id, name=name, org_type="megacorp", tier=5,
        description=None, headquarters=None, leadership=[],
        ltgs=ltgs, ally_ids=[], enemy_ids=[],
        revealed_ally_ids=[], revealed_enemy_ids=[],
        is_active=is_active, notes=None,
    )


class _FakeResult:
    def __init__(self, items):
        self._items = items

    def scalars(self):
        return self

    def all(self):
        return self._items


class _FakeDB:
    def __init__(self, orgs):
        self._orgs = orgs

    async def execute(self, _query):
        return _FakeResult(self._orgs)


def _host(addr="RTG-SEA 1234", code="Red", val=9):
    return SimpleNamespace(
        ltg_address=addr,
        config_json={"security_code": code, "security_value": val},
    )


def _host_row(name="Test", visible=True, code="Green", val=6, trap=None, host_id=1):
    """A SimpleNamespace exposing every MatrixHostSummary field (san_rating pre-derived)."""
    return SimpleNamespace(
        id=host_id, name=name, owner_org_id=None, location_id=None,
        is_visible_to_players=visible, ltg_address="NA/ALM B6170", id_code=None,
        san_rating=(f"{code}-{val}" if code else None),
        is_trap_door_dest=False, trap_doors_json=(trap if trap is not None else []),
        created_at=datetime.now(UTC),
    )


# Auth-context dicts as returned by get_any_token.
_PLAYER = {"is_admin": False, "view_as_player": False}
_ADMIN = {"is_admin": True, "view_as_player": False}
_ADMIN_PREVIEW = {"is_admin": True, "view_as_player": True}


# -- _serialize_org redaction ---------------------------------------------

def test_non_admin_rating_hidden_until_revealed():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Red-9", "visibility": "listed"},
    ])
    data = _serialize_org(org, _PLAYER)
    assert "san_access_rating" not in data["ltgs"][0]
    # Payload must still validate against the response_model.
    OrganizationRead.model_validate(data)


def test_non_admin_rating_shown_when_revealed():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Red-9", "san_revealed": True, "visibility": "listed"},
    ])
    data = _serialize_org(org, _PLAYER)
    assert data["ltgs"][0]["san_access_rating"] == "Red-9"


def test_admin_always_sees_rating():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Red-9", "visibility": "listed"},
    ])
    data = _serialize_org(org, _ADMIN)
    assert data["ltgs"][0]["san_access_rating"] == "Red-9"


def test_admin_runner_view_preview_redacts():
    # An admin previewing the player payload (UI "runner view" -> X-Runner-View) must see the
    # SAME redaction a player does, even though the admin token is still sent.
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Red-9", "visibility": "listed"},
    ])
    data = _serialize_org(org, _ADMIN_PREVIEW)
    assert "san_access_rating" not in data["ltgs"][0]


def test_redaction_leaves_telecom_entries_untouched():
    org = _org_obj([
        {"type": "telecom", "number": "206-555-0100", "description": "front desk",
         "visibility": "listed"},
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Red-9", "visibility": "listed"},
    ])
    data = _serialize_org(org, _PLAYER)
    telecom, host = data["ltgs"]
    assert telecom["number"] == "206-555-0100"
    assert "san_access_rating" not in host


# -- _preserve_san_revealed (GM edit round-trip) --------------------------

def test_preserve_carries_flag_across_gm_edit():
    old = [{"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
            "san_access_rating": "Red-9", "san_revealed": True}]
    # GM editor re-submits the entry WITHOUT san_revealed.
    new = [{"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
            "san_access_rating": "Red-9"}]
    merged = _preserve_san_revealed(old, new)
    assert merged[0]["san_revealed"] is True


def test_preserve_does_not_invent_flag():
    old = [{"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
            "san_access_rating": "Red-9"}]
    new = [{"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
            "san_access_rating": "Red-9"}]
    merged = _preserve_san_revealed(old, new)
    assert "san_revealed" not in merged[0]


def test_preserve_matches_on_address_not_position():
    old = [{"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234", "san_revealed": True}]
    # Same slot, but the GM renamed the LTG -- treat it as a new (undiscovered) host.
    new = [{"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "9999"}]
    merged = _preserve_san_revealed(old, new)
    assert "san_revealed" not in merged[0]


# -- sync_host_security_to_org(mark_revealed=...) -------------------------

def test_discovery_marks_revealed():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Green-6"},
    ])
    asyncio.run(sync_host_security_to_org(_FakeDB([org]), _host(), mark_revealed=True))
    entry = org.ltgs[0]
    assert entry["san_access_rating"] == "Red-9"
    assert entry["san_revealed"] is True


def test_plain_sync_does_not_reveal():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Green-6"},
    ])
    asyncio.run(sync_host_security_to_org(_FakeDB([org]), _host()))
    entry = org.ltgs[0]
    assert entry["san_access_rating"] == "Red-9"
    assert "san_revealed" not in entry


# -- ltg_catalog endpoint redaction ---------------------------------------
# The org LTG catalog (used by the Matrix Hosts registry + the player Systems list) must mirror
# the org-card rule: hide each entry's SC/SV until it is san_revealed, unless the caller is a
# real admin who is NOT previewing runner view.

def test_ltg_catalog_hides_rating_from_player_until_revealed():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Red-9", "visibility": "listed"},
    ])
    entries = asyncio.run(ltg_catalog(auth=_PLAYER, db=_FakeDB([org])))
    assert entries[0]["san_access_rating"] == ""


def test_ltg_catalog_shows_revealed_rating_to_player():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Red-9", "san_revealed": True, "visibility": "listed"},
    ])
    entries = asyncio.run(ltg_catalog(auth=_PLAYER, db=_FakeDB([org])))
    assert entries[0]["san_access_rating"] == "Red-9"


def test_ltg_catalog_admin_sees_unrevealed_rating():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Red-9", "visibility": "listed"},
    ])
    entries = asyncio.run(ltg_catalog(auth=_ADMIN, db=_FakeDB([org])))
    assert entries[0]["san_access_rating"] == "Red-9"


def test_ltg_catalog_admin_runner_view_hides_unrevealed_rating():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Red-9", "visibility": "listed"},
    ])
    entries = asyncio.run(ltg_catalog(auth=_ADMIN_PREVIEW, db=_FakeDB([org])))
    assert entries[0]["san_access_rating"] == ""


# -- ltg_catalog org concealment (is_active) and unlisted-entry redaction -
# A GM-concealed org (is_active=False) must never leak its name/address via the catalog, and
# an unlisted/black-disposition entry must be redacted the same way organizations._serialize_org
# already redacts it on the org-card payload.

def test_ltg_catalog_hides_inactive_org_from_player():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Orange-4", "visibility": "listed"},
    ], is_active=False, name="Shigeda-gumi")
    entries = asyncio.run(ltg_catalog(auth=_PLAYER, db=_FakeDB([org])))
    assert entries == []


def test_ltg_catalog_admin_sees_inactive_org():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Orange-4", "visibility": "listed"},
    ], is_active=False, name="Shigeda-gumi")
    entries = asyncio.run(ltg_catalog(auth=_ADMIN, db=_FakeDB([org])))
    assert entries[0]["org_name"] == "Shigeda-gumi"


def test_ltg_catalog_hides_unlisted_entry_from_player():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Red-9", "visibility": "unlisted"},
    ])
    entries = asyncio.run(ltg_catalog(auth=_PLAYER, db=_FakeDB([org])))
    assert entries == []


def test_ltg_catalog_shows_revealed_unlisted_entry_to_player():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Red-9", "visibility": "unlisted", "revealed": True},
    ])
    entries = asyncio.run(ltg_catalog(auth=_PLAYER, db=_FakeDB([org])))
    assert len(entries) == 1


def test_ltg_catalog_admin_sees_unlisted_entry():
    org = _org_obj([
        {"type": "matrix_host", "rtg": "RTG-SEA", "ltg": "1234",
         "san_access_rating": "Red-9", "visibility": "unlisted"},
    ])
    entries = asyncio.run(ltg_catalog(auth=_ADMIN, db=_FakeDB([org])))
    assert len(entries) == 1


# -- list_hosts endpoint redaction ----------------------------------------
# The /matrix-hosts/ summary must not leak a host's SC/SV (san_rating) or trap-door edges to
# players -- or to an admin previewing runner view. A real admin keeps the full row.

def test_list_hosts_redacts_rating_and_trapdoors_for_player():
    host = _host_row(code="Green", val=6, trap=[{"destination_host_id": 2}])
    result = asyncio.run(list_hosts(auth=_PLAYER, db=_FakeDB([host])))
    assert result[0].san_rating is None
    assert result[0].trap_doors_json is None


def test_list_hosts_admin_keeps_rating():
    host = _host_row(code="Green", val=6, trap=[{"destination_host_id": 2}])
    result = asyncio.run(list_hosts(auth=_ADMIN, db=_FakeDB([host])))
    assert result[0].san_rating == "Green-6"
    assert result[0].trap_doors_json == [{"destination_host_id": 2}]


def test_list_hosts_admin_runner_view_redacts_rating():
    host = _host_row(code="Green", val=6, trap=[{"destination_host_id": 2}])
    result = asyncio.run(list_hosts(auth=_ADMIN_PREVIEW, db=_FakeDB([host])))
    assert result[0].san_rating is None
    assert result[0].trap_doors_json is None
