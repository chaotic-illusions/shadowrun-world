"""Tests for seed.py error handling."""
import pytest
from unittest.mock import MagicMock
import httpx

from seed import post, get_json, upsert_rtgs


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
