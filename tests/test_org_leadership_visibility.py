"""Unlisted leaders (future office holders, later-adventure NPCs) stay hidden from players."""
from types import SimpleNamespace

from app.routers.organizations import _serialize_org


_PLAYER = {"is_admin": False, "view_as_player": False}
_ADMIN = {"is_admin": True, "view_as_player": False}
_ADMIN_PREVIEW = {"is_admin": True, "view_as_player": True}

_LEADERS = [
    {"name": "Legacy", "title": "President/CEO", "notes": "No visibility key"},
    {"name": "Listed", "title": "Chairman", "visibility": "listed", "notes": "Secret"},
    {"name": "Future", "title": "Chairman", "visibility": "unlisted", "notes": "Takes the chair in 2054"},
    {"name": "Revealed", "title": "Fixer", "visibility": "unlisted", "revealed": True},
    {"name": "Black", "title": "Handler", "visibility": "black"},
]


def _org(leadership, divisions=None):
    return SimpleNamespace(
        id=1, name="Ares Macrotechnology", org_type="megacorp", tier=5,
        description=None, headquarters=None, leadership=leadership, divisions=divisions or [],
        ltgs=[], ally_ids=[], enemy_ids=[], revealed_ally_ids=[], revealed_enemy_ids=[],
        is_active=True, notes=None,
    )


def _names(entries):
    return [entry["name"] for entry in entries]


def test_players_see_only_listed_or_revealed_leaders_without_notes():
    leaders = _serialize_org(_org(_LEADERS), _PLAYER)["leadership"]

    assert _names(leaders) == ["Legacy", "Listed", "Revealed"]
    assert all("notes" not in leader for leader in leaders)


def test_admin_preview_matches_the_player_view():
    leaders = _serialize_org(_org(_LEADERS), _ADMIN_PREVIEW)["leadership"]

    assert _names(leaders) == ["Legacy", "Listed", "Revealed"]


def test_admin_sees_every_leader_with_notes():
    leaders = _serialize_org(_org(_LEADERS), _ADMIN)["leadership"]

    assert _names(leaders) == [leader["name"] for leader in _LEADERS]
    assert leaders[2]["notes"] == "Takes the chair in 2054"


def test_division_leaders_follow_the_same_rule():
    division = {
        "id": "6f1c2b1e-3a1d-4c55-9a7e-2f0b8d4e1c90", "name": "Ares Arms", "kind": "division", "visibility": "listed",
        "revealed": False, "leadership": _LEADERS,
    }

    leaders = _serialize_org(_org([], [division]), _PLAYER)["divisions"][0]["leadership"]

    assert _names(leaders) == ["Legacy", "Listed", "Revealed"]
