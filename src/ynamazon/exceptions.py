class YnabSetupError(Exception):
    """Custom exception for YNAB setup errors."""


class MissingOpenAIAPIKey(Exception):
    """Raised when OpenAI API key is required but not found."""


class InvalidOpenAIAPIKey(Exception):
    """Raised when OpenAI API key is invalid or authentication fails."""


class OpenAIEmptyResponseError(Exception):
    """Raised when OpenAI returns an empty or invalid response."""
