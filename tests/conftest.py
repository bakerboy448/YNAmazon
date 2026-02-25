"""Root conftest providing dummy environment variables for testing.

Settings() is eagerly instantiated at module import time and requires
these env vars. We monkeypatch them at the session level so that test
collection doesn't blow up.
"""

import os

# Must be set BEFORE any ynamazon module is imported
os.environ.setdefault("YNAB_API_KEY", "test-ynab-api-key")
os.environ.setdefault("YNAB_BUDGET_ID", "test-budget-id")
os.environ.setdefault("AMAZON_USER", "test@example.com")
os.environ.setdefault("AMAZON_PASSWORD", "test-password")
