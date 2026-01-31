# YNAmazon

A program to annotate YNAB transactions with Amazon order info.

## Features

- Automatically matches YNAB transactions to Amazon orders by amount
- Generates detailed memos with item names, prices, and order numbers
- Supports dry-run mode to preview changes before applying
- Docker support for easy deployment
- Optional AI summarization with OpenAI

## Quick Start

### Docker (Recommended)

```bash
docker run --rm \
  -e YNAB_API_KEY=your-key \
  -e YNAB_BUDGET_ID=your-budget-id \
  -e AMAZON_USER=your-email \
  -e AMAZON_PASSWORD=your-password \
  ghcr.io/bakerboy448/ynamazon:latest
```

Or with docker-compose:

```yaml
services:
  ynamazon:
    image: ghcr.io/bakerboy448/ynamazon:latest
    environment:
      - YNAB_API_KEY=${YNAB_API_KEY}
      - YNAB_BUDGET_ID=${YNAB_BUDGET_ID}
      - AMAZON_USER=${AMAZON_USER}
      - AMAZON_PASSWORD=${AMAZON_PASSWORD}
    volumes:
      - ./config:/app/config:ro
```

### Local Installation

```bash
# Install uv if needed: https://github.com/astral-sh/uv
uv sync

# Run
uv run yna --help
```

## Configuration

Create a `.env` file or set environment variables:

```bash
# Required
YNAB_API_KEY=your-ynab-api-key
YNAB_BUDGET_ID=your-budget-id
AMAZON_USER=your-amazon-email
AMAZON_PASSWORD=your-amazon-password

# Optional
MATCH_EMPTY_MEMO=true              # Match "Amazon" payee with empty memo (default: true)
AMAZON_FULL_DETAILS=true           # Fetch item prices (slower, default: true)
AMAZON_DEBUG=false                 # Enable debug logging
YNAB_PAYEE_NAME_PROCESSING_COMPLETED=Amazon  # Payee name for processed transactions
```

Config loading order (later overrides earlier):
1. `/app/config/.env` (Docker)
2. `.env` (current directory)
3. Environment variables

## CLI Usage

```bash
# Default: match and update transactions interactively
yna ynamazon

# Preview changes without modifying anything
yna ynamazon --dry-run

# Process all transactions (including those with existing memos)
yna ynamazon --force --dry-run

# Limit lookback period (max 31 days due to Amazon API)
yna ynamazon --days 14

# Print YNAB transactions
yna print-ynab

# Print Amazon transactions
yna print-amazon
```

## Memo Format

Memos are formatted as: `Item A ($XX.XX), Item B ($XX.XX) | Order #XXX-XXXXXXX-XXXXXXX`

For partial orders (when Amazon splits shipments):
`[Partial - order total $XX.XX] Item A, Item B | Order #XXX-XXXXXXX-XXXXXXX`

## YNAB Setup

1. Create a payee named `Amazon` (or your preferred name)
2. Create a rename rule to rename Amazon transactions to this payee
3. The program will match transactions with empty memos and this payee

## AI Summarization (Optional)

```bash
uv sync --extra ai
```

Set in `.env`:
```bash
USE_AI_SUMMARIZATION=true
OPENAI_API_KEY=your-openai-api-key
```

## Limitations

- Only supports amazon.com (US)
- Amazon API returns ~31 days of transaction history
- Relies on web scraping which may break with Amazon changes

## Development

```bash
# Install dev dependencies
uv sync --dev

# Run tests
uv run pytest

# Lint
uv run ruff check src/
uv run ruff format src/

# Type check
uv run pyright src/
```

## License

MIT
