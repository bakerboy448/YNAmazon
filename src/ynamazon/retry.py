import time
from collections.abc import Callable
from typing import TypeVar

from loguru import logger

from ynamazon.exceptions import TransientSyncError

_T = TypeVar("_T")


def retry_on_transient(
    func: Callable[[], _T],
    *,
    max_retries: int = 3,
    base_delay: float = 5.0,
    description: str = "operation",
) -> _T:
    """Retry a callable on TransientSyncError with exponential backoff.

    Non-transient exceptions propagate immediately.
    After exhausting retries, re-raises the last TransientSyncError.

    Args:
        func: Zero-arg callable to retry.
        max_retries: Maximum number of retry attempts.
        base_delay: Base delay in seconds (doubles each attempt).
        description: Human-readable label for log messages.

    Returns:
        The return value of func on success.

    Raises:
        TransientSyncError: After all retries exhausted.
    """
    last_error: TransientSyncError | None = None
    for attempt in range(max_retries + 1):
        try:
            return func()
        except TransientSyncError as e:
            last_error = e
            if attempt < max_retries:
                delay = base_delay * (2**attempt)
                logger.warning(
                    f"{description} failed (attempt {attempt + 1}/{max_retries + 1}): {e}. "
                    f"Retrying in {delay:.0f}s"
                )
                time.sleep(delay)
            else:
                logger.error(f"{description} failed after {max_retries + 1} attempts: {e}")

    raise last_error  # type: ignore[misc]
