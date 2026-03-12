"""Tests for error handling exceptions and retry logic."""

from unittest.mock import patch

import pytest

from ynamazon.exceptions import FatalSyncError, TransientSyncError
from ynamazon.main import SyncResult
from ynamazon.retry import retry_on_transient


class TestExceptionClasses:
    def test_transient_sync_error_message(self):
        e = TransientSyncError("network timeout")
        assert str(e) == "network timeout"

    def test_transient_sync_error_default_sync_result(self):
        e = TransientSyncError("fail")
        assert e.sync_result is None

    def test_transient_sync_error_with_sync_result(self):
        result = SyncResult(ynab_count=5, amazon_count=3, matched=2)
        e = TransientSyncError("fail", sync_result=result)
        assert e.sync_result is result
        assert e.sync_result.matched == 2

    def test_fatal_sync_error_message(self):
        e = FatalSyncError("auth failed")
        assert str(e) == "auth failed"

    def test_fatal_sync_error_default_sync_result(self):
        e = FatalSyncError("fail")
        assert e.sync_result is None

    def test_fatal_sync_error_with_sync_result(self):
        result = SyncResult(updated=1, errors=["bad request"])
        e = FatalSyncError("fail", sync_result=result)
        assert e.sync_result is result
        assert e.sync_result.errors == ["bad request"]


class TestRetryOnTransient:
    def test_succeeds_first_try(self):
        result = retry_on_transient(lambda: 42, max_retries=3, description="test")
        assert result == 42

    @patch("ynamazon.retry.time.sleep")
    def test_succeeds_on_retry(self, mock_sleep):
        attempts = {"count": 0}

        def flaky():
            attempts["count"] += 1
            if attempts["count"] < 3:
                raise TransientSyncError("transient")
            return "ok"

        result = retry_on_transient(flaky, max_retries=3, base_delay=1.0, description="test")
        assert result == "ok"
        assert attempts["count"] == 3
        assert mock_sleep.call_count == 2

    @patch("ynamazon.retry.time.sleep")
    def test_exhausts_retries(self, mock_sleep):
        def always_fails():
            raise TransientSyncError("always fails")

        with pytest.raises(TransientSyncError, match="always fails"):
            retry_on_transient(always_fails, max_retries=2, base_delay=1.0, description="test")

        assert mock_sleep.call_count == 2

    @patch("ynamazon.retry.time.sleep")
    def test_exponential_backoff(self, mock_sleep):
        attempts = {"count": 0}

        def fails_twice():
            attempts["count"] += 1
            if attempts["count"] <= 2:
                raise TransientSyncError("fail")
            return "done"

        retry_on_transient(fails_twice, max_retries=3, base_delay=5.0, description="test")
        delays = [call.args[0] for call in mock_sleep.call_args_list]
        assert delays == [5.0, 10.0]

    def test_non_transient_propagates_immediately(self):
        def raises_value_error():
            raise ValueError("not transient")

        with pytest.raises(ValueError, match="not transient"):
            retry_on_transient(raises_value_error, max_retries=3, description="test")

    def test_fatal_sync_error_propagates_immediately(self):
        def raises_fatal():
            raise FatalSyncError("auth failed")

        with pytest.raises(FatalSyncError, match="auth failed"):
            retry_on_transient(raises_fatal, max_retries=3, description="test")
