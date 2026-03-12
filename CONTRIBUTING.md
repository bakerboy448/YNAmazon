# Contributing to YNAmazon

## Getting Started

```bash
git clone https://github.com/bakerboy448/YNAmazon.git
cd YNAmazon
uv sync --dev
uv run pre-commit install
```

## Development Workflow

1. Create a feature branch from `main`
2. Make your changes
3. Run the test suite: `uv run pytest -v`
4. Run pre-commit hooks: `uv run pre-commit run --all-files`
5. Commit with [conventional commits](https://www.conventionalcommits.org/)
6. Open a pull request against `main`

## Commit Messages

This project uses [conventional commits](https://www.conventionalcommits.org/) enforced by pre-commit hooks. Format:

```
<type>: <description>

[optional body]
```

Types: `feat`, `fix`, `perf`, `refactor`, `docs`, `style`, `test`, `build`, `ci`, `chore`

- `feat` triggers a minor version bump
- `fix`, `perf`, `refactor` trigger a patch version bump

## Testing

```bash
# Run all tests
uv run pytest -v

# Run specific test file
uv run pytest tests/test_error_handling.py -v

# Run with coverage
uv run pytest --cov=ynamazon
```

Tests for optional dependencies (e.g., OpenAI) are automatically skipped when those packages aren't installed.

## Pre-commit Hooks

The project uses these pre-commit hooks:

- **ruff-check** with `--fix`: linting and auto-fixing (including unused import removal)
- **ruff-format**: code formatting
- **deptry**: dependency checking
- **gitleaks**: secret detection
- **conventional-pre-commit**: commit message validation
- **uv-lock** / **uv-export**: lockfile consistency

**Important**: ruff runs with `--fix` and will auto-remove unused imports. Ensure all imports are used in the same commit where they're added.

## Project Structure

```
src/ynamazon/
  cli/            # Typer CLI commands (cli.py, utils.py)
  amazon_transactions.py  # Amazon order retrieval
  exceptions.py   # Typed exception hierarchy
  main.py         # Core transaction matching logic
  retry.py        # Retry utility with exponential backoff
  settings.py     # Pydantic settings
  ynab_memo.py    # AI memo processing (optional)
  ynab_transactions.py    # YNAB API interaction
tests/
  amazon/         # Amazon-specific tests
  ynab/           # YNAB-specific tests
  test_error_handling.py  # Exception and retry tests
```

## Error Handling

The project uses a typed exception hierarchy:

- `TransientSyncError` — retryable errors (network timeouts, 5xx). Retried automatically with exponential backoff.
- `FatalSyncError` — non-retryable errors (auth failures, bad config). Reported immediately.

Both exceptions accept an optional `sync_result` parameter to carry partial progress for notifications.

When adding new external API calls, wrap them appropriately:
- Network/timeout errors -> `TransientSyncError`
- Auth/config errors -> `FatalSyncError`
- Non-critical failures -> log and continue with `result.errors.append()`

## Releases

Releases are automated via [python-semantic-release](https://python-semantic-release.readthedocs.io/). Merging to `main` triggers version bumping, changelog generation, and Docker image builds based on commit message types.
