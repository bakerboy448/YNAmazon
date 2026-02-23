# YNAmazon — YNAB + Amazon Order Annotation

Source: `src/ynamazon/`, Tests: `tests/`, CI: `.github/workflows/`

## Dev
```bash
uv sync --dev          # install deps
uv run yna --help      # run locally
uv run pytest          # tests
uv run ruff check src/ --fix && uv run ruff format src/  # lint
uv run pyright src/    # typecheck
```

## Docker
`docker build -t ynamazon:local . && docker run --rm -v /path/.env:/app/config/.env:ro ynamazon:local ynamazon --dry-run`

## Config (env vars)
Required: YNAB_API_KEY, YNAB_BUDGET_ID, AMAZON_USER, AMAZON_PASSWORD, AMAZON_OTP_SECRET_KEY
Optional: MATCH_EMPTY_MEMO (true), AMAZON_FULL_DETAILS (true), AMAZON_DEBUG

## CI/CD
CI: PRs only (lint, typecheck, build). Release: manual dispatch → GitHub release + GHCR.

## Known Issues
- Lint/typecheck errors inherited from upstream
- amazonorders prompts for OTP interactively if not configured
- Cache dir permissions need setup in Docker
