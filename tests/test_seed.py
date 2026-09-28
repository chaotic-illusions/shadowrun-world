"""Tests for seed.py error handling and portable world exports."""
import json
from pathlib import Path

import pytest
from unittest.mock import MagicMock
import httpx

from seed import get_json, post, put, resolve_admin_token, upsert_rtgs


ROOT = Path(__file__).resolve().parent.parent
WORLD_SEED = ROOT / "data" / "world_seed.json"


class TestResolveAdminToken:
    def test_explicit_token_overrides_environment(self, monkeypatch):
        monkeypatch.setenv("BOOTSTRAP_ADMIN_KEY", "environment-token")

        assert resolve_admin_token("explicit-token") == "explicit-token"

    def test_uses_explicit_bootstrap_environment(self, monkeypatch):
        monkeypatch.setenv("BOOTSTRAP_ADMIN_KEY", "bootstrap-token")

        assert resolve_admin_token() == "bootstrap-token"

    def test_missing_credential_fails_closed(self, monkeypatch):
        monkeypatch.delenv("BOOTSTRAP_ADMIN_KEY", raising=False)

        with pytest.raises(RuntimeError, match="Admin credential required"):
            resolve_admin_token()


class TestPost:
    def test_successful_post(self):
        response_data = {"id": 1, "name": "test"}
        mock_client = MagicMock()
        mock_resp = MagicMock()
        mock_resp.json.return_value = response_data
        mock_resp.raise_for_status.return_value = None
        mock_client.post.return_value = mock_resp

        result = post(mock_client, "/test/", {"name": "test"})

        assert result == response_data
        mock_client.post.assert_called_once_with("/test/", json={"name": "test"})

    def test_http_error_raises_runtime(self):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 409
        mock_response.text = '{"detail":"already exists"}'
        error = httpx.HTTPStatusError("409 Conflict", request=MagicMock(), response=mock_response)
        mock_client.post.return_value.raise_for_status.side_effect = error

        with pytest.raises(RuntimeError, match="ERROR 409"):
            post(mock_client, "/test/", {"name": "dup"})

    def test_url_error_raises_runtime(self):
        mock_client = MagicMock()
        mock_client.post.side_effect = httpx.ConnectError("Connection refused")

        with pytest.raises(RuntimeError, match="Connection failed"):
            post(mock_client, "/test/", {"name": "x"})


class TestGetJson:
    def test_successful_get(self):
        response_data = [{"id": 1, "code": "NA/UCAS-SEA"}]
        mock_client = MagicMock()
        mock_resp = MagicMock()
        mock_resp.json.return_value = response_data
        mock_resp.raise_for_status.return_value = None
        mock_client.get.return_value = mock_resp

        result = get_json(mock_client, "/rtgs/")

        assert result == response_data
        mock_client.get.assert_called_once_with("/rtgs/", params=None)


class TestPut:
    def test_successful_put(self):
        response_data = {"enabled": ["GRIM", "AWK"]}
        mock_client = MagicMock()
        mock_resp = MagicMock()
        mock_resp.content = b"{}"
        mock_resp.json.return_value = response_data
        mock_resp.raise_for_status.return_value = None
        mock_client.put.return_value = mock_resp

        result = put(mock_client, "/catalog/books", response_data)

        assert result == response_data
        mock_client.put.assert_called_once_with(
            "/catalog/books", json=response_data
        )


def test_world_seed_artifact_is_pc_free():
    data = json.loads(WORLD_SEED.read_text(encoding="utf-8"))

    assert data["_format_version"] == 2
    assert data["campaign_state"] == {
        "current_tick": 1,
        "enabled_books": ["GRIM", "AWK"],
    }
    assert {
        "rtgs": len(data["rtgs"]),
        "organizations": len(data["organizations"]),
        "locations": len(data["locations"]),
        "characters": len(data["characters"]),
        "contacts": len(data["contacts"]),
        "org_standings": len(data["org_standings"]),
        "matrix_hosts": len(data["matrix_hosts"]),
        "adventure_logs": len(data["adventure_logs"]),
    } == {
        "rtgs": 67,
        "organizations": 821,
        "locations": 1183,
        "characters": 862,
        "contacts": 0,
        "org_standings": 0,
        "matrix_hosts": 7,
        "adventure_logs": 1,
    }
    assert all(character["is_pc"] is False for character in data["characters"])
    assert all(log["participant_names"] == [] for log in data["adventure_logs"])


class TestUpsertRtgs:
    def test_updates_existing_rtg_by_code(self):
        mock_client = MagicMock()

        get_resp = MagicMock()
        get_resp.raise_for_status.return_value = None
        get_resp.json.return_value = [{"id": 7, "code": "NA/UCAS-SEA"}]

        patch_resp = MagicMock()
        patch_resp.raise_for_status.return_value = None

        mock_client.get.return_value = get_resp
        mock_client.patch.return_value = patch_resp

        data = {
            "rtgs": [
                {
                    "code": "NA/UCAS-SEA",
                    "region": "UCAS Pacific Northwest",
                    "rtg_security_rating": "Green-4",
                }
            ]
        }

        rtg_ids = {}
        upsert_rtgs(mock_client, data, rtg_ids)

        assert rtg_ids["NA/UCAS-SEA"] == 7
        mock_client.patch.assert_called_once_with(
            "/rtgs/7",
            json=data["rtgs"][0],
        )
        mock_client.post.assert_not_called()

    def test_creates_missing_rtg(self):
        mock_client = MagicMock()

        get_resp = MagicMock()
        get_resp.raise_for_status.return_value = None
        get_resp.json.return_value = []

        post_resp = MagicMock()
        post_resp.raise_for_status.return_value = None
        post_resp.json.return_value = {"id": 11, "code": "NA/UCAS-SEA"}

        mock_client.get.return_value = get_resp
        mock_client.post.return_value = post_resp

        data = {
            "rtgs": [
                {
                    "code": "NA/UCAS-SEA",
                    "region": "UCAS Pacific Northwest",
                    "rtg_security_rating": "Green-4",
                }
            ]
        }

        rtg_ids = {}
        upsert_rtgs(mock_client, data, rtg_ids)

        assert rtg_ids["NA/UCAS-SEA"] == 11
        mock_client.post.assert_called_once_with(
            "/rtgs/",
            json=data["rtgs"][0],
        )
        mock_client.patch.assert_not_called()
