# YNAmazon

A program to annotate YNAB transactions with Amazon order info.

## Quick Reference

| Component | Path |
|-----------|------|
| Source code | `src/ynamazon/` |
| Tests | `tests/` |
| Docker | `Dockerfile` |
| CI/CD | `.github/workflows/` |
| Pre-commit | `.pre-commit-config.yaml` |

## Development

```bash
# Install dependencies
uv sync --dev

# Run locally
uv run yna --help
uv run yna ynamazon --dry-run

# Run tests
uv run pytest

# Lint & format
uv run ruff check src/ --fix
uv run ruff format src/

# Type check
uv run pyright src/
```

## Docker

```bash
# Build
docker build -t ynamazon:local .

# Run
docker run --rm -v /path/to/.env:/app/config/.env:ro ynamazon:local ynamazon --dry-run
```

## Configuration

Required environment variables:
- `YNAB_API_KEY` - YNAB API key
- `YNAB_BUDGET_ID` - YNAB budget ID
- `AMAZON_USER` - Amazon email
- `AMAZON_PASSWORD` - Amazon password
- `AMAZON_OTP_SECRET_KEY` - Amazon TOTP secret (base32)

Optional:
- `MATCH_EMPTY_MEMO` - Match empty memo transactions (default: true)
- `AMAZON_FULL_DETAILS` - Fetch item prices (default: true)
- `AMAZON_DEBUG` - Enable debug logging

## CI/CD

- **CI**: Runs on PRs only (lint, typecheck, build)
- **Release**: Manual dispatch only - creates GitHub release + pushes to GHCR

## Known Issues

1. Lint/typecheck errors exist in upstream code (inherited from original project)
2. amazonorders library prompts for OTP interactively if not configured
3. Cache directory permissions need proper setup in Docker

## Architecture

```
src/ynamazon/
├── cli/           # Typer CLI commands
├── amazon_transactions.py  # Amazon API integration
├── ynab_transactions.py    # YNAB API integration
├── main.py        # Core transaction matching logic
└── settings.py    # Pydantic settings
```
