"""Tests for seed.py error handling."""
import pytest
from unittest.mock import MagicMock
import httpx

from seed import post


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
