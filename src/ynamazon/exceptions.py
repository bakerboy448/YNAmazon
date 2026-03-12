class YnabSetupError(Exception):
    """Custom exception for YNAB setup errors."""


class MissingOpenAIAPIKey(Exception):
    """Raised when OpenAI API key is required but not found."""


class InvalidOpenAIAPIKey(Exception):
    """Raised when OpenAI API key is invalid or authentication fails."""


class OpenAIEmptyResponseError(Exception):
    """Raised when OpenAI returns an empty or invalid response."""


class TransientSyncError(Exception):
    """Retryable error (network timeout, 5xx)."""

    def __init__(self, message: str, *, sync_result: object | None = None) -> None:
        super().__init__(message)
        self.sync_result = sync_result


class FatalSyncError(Exception):
    """Non-retryable error requiring human intervention (auth, bad config)."""

    def __init__(self, message: str, *, sync_result: object | None = None) -> None:
        super().__init__(message)
        self.sync_result = sync_result
