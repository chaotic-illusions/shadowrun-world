"""Tests for seed.py error handling."""
import json
import urllib.error
from unittest.mock import patch, MagicMock
import pytest

from seed import post


class TestPost:
    def test_successful_post(self):
        response_data = {"id": 1, "name": "test"}
        mock_resp = MagicMock()
        mock_resp.read.return_value = json.dumps(response_data).encode()
        mock_resp.__enter__ = lambda s: s
        mock_resp.__exit__ = MagicMock(return_value=False)

        with patch("urllib.request.urlopen", return_value=mock_resp):
            result = post("http://localhost:8000", "/test/", {"name": "test"})
        assert result == response_data

    def test_http_error_raises_runtime(self):
        error = urllib.error.HTTPError(
            url="http://localhost:8000/test/",
            code=409,
            msg="Conflict",
            hdrs={},
            fp=MagicMock(read=lambda: b'{"detail":"already exists"}'),
        )
        with patch("urllib.request.urlopen", side_effect=error):
            with pytest.raises(RuntimeError, match="ERROR 409"):
                post("http://localhost:8000", "/test/", {"name": "dup"})

    def test_url_error_raises_runtime(self):
        error = urllib.error.URLError(reason="Connection refused")
        with patch("urllib.request.urlopen", side_effect=error):
            with pytest.raises(RuntimeError, match="Connection failed"):
                post("http://localhost:8000", "/test/", {"name": "x"})
