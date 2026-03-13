"""Tests for YNAB API rate limit retry logic."""

from unittest.mock import MagicMock, patch

import pytest
from ynab.exceptions import ApiException, UnauthorizedException

from ynamazon.ynab_transactions import ynab_rate_limit_retry


@ynab_rate_limit_retry
def _mock_api_call(mock: MagicMock) -> str:
    """Test function decorated with rate limit retry."""
    return mock()


class TestRateLimitRetry:
    def test_success_on_first_try(self):
        mock = MagicMock(return_value="ok")
        assert _mock_api_call(mock) == "ok"
        assert mock.call_count == 1

    @patch("ynamazon.ynab_transactions.time.sleep")
    def test_retries_on_429(self, mock_sleep: MagicMock):
        mock = MagicMock()
        exc_429 = ApiException(status=429, reason="Too Many Requests")
        mock.side_effect = [exc_429, "ok"]

        result = _mock_api_call(mock)
        assert result == "ok"
        assert mock.call_count == 2
        mock_sleep.assert_called_once_with(60)

    @patch("ynamazon.ynab_transactions.time.sleep")
    def test_retries_multiple_429s(self, mock_sleep: MagicMock):
        mock = MagicMock()
        exc_429 = ApiException(status=429, reason="Too Many Requests")
        mock.side_effect = [exc_429, exc_429, "ok"]

        result = _mock_api_call(mock)
        assert result == "ok"
        assert mock.call_count == 3
        assert mock_sleep.call_count == 2
        mock_sleep.assert_any_call(60)
        mock_sleep.assert_any_call(120)

    @patch("ynamazon.ynab_transactions.time.sleep")
    def test_exhausts_retries_then_propagates(self, mock_sleep: MagicMock):
        mock = MagicMock()
        exc_429 = ApiException(status=429, reason="Too Many Requests")
        mock.side_effect = exc_429  # always 429

        with pytest.raises(ApiException) as exc_info:
            _mock_api_call(mock)
        assert exc_info.value.status == 429
        # 3 retries + 1 final attempt = 4 calls
        assert mock.call_count == 4
        assert mock_sleep.call_count == 3

    def test_non_429_api_error_not_retried(self):
        mock = MagicMock()
        exc_500 = ApiException(status=500, reason="Server Error")
        mock.side_effect = exc_500

        with pytest.raises(ApiException) as exc_info:
            _mock_api_call(mock)
        assert exc_info.value.status == 500
        assert mock.call_count == 1

    def test_unauthorized_not_retried(self):
        mock = MagicMock()
        mock.side_effect = UnauthorizedException(status=401, reason="Unauthorized")

        with pytest.raises(UnauthorizedException):
            _mock_api_call(mock)
        assert mock.call_count == 1

    def test_non_api_exception_propagates(self):
        mock = MagicMock()
        mock.side_effect = ValueError("something broke")

        with pytest.raises(ValueError, match="something broke"):
            _mock_api_call(mock)
        assert mock.call_count == 1
