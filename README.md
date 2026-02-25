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
AMAZON_OTP_SECRET_KEY=your-totp-secret  # For automatic 2FA (TOTP secret from authenticator setup)
MATCH_EMPTY_MEMO=true              # Match "Amazon" payee with empty memo (default: true)
AMAZON_FULL_DETAILS=true           # Fetch item prices (slower, default: true)
AMAZON_DEBUG=false                 # Enable debug logging
YNAB_PAYEE_NAME_PROCESSING_COMPLETED=Amazon  # Payee name for processed transactions
YNAB_APPROVED_STATUSES=["approved","unapproved"]  # Which approval statuses to match (default: both)
AUTO_ACCEPT_DATE_MISMATCH=true     # Auto-accept date mismatches without prompting (default: false)
DATE_MISMATCH_TOLERANCE_DAYS=2     # Allow date differences up to N days (default: 0 = exact match)
NON_INTERACTIVE=true               # Skip all confirmation prompts (default: false, for daemon mode)
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

## Daemon Mode

Run as a long-lived daemon that syncs on a schedule:

```bash
# Run every 20 hours (default)
yna daemon

# Custom interval (min 12h, max 48h)
yna daemon --interval 24

# Use time windows for random scheduling (e.g., 6-8am and 6-8pm)
yna daemon --windows "6-8,18-20"

# Daemon with dry-run (preview only, no changes)
yna daemon --dry-run
```

Daemon mode runs immediately on start, then at the configured interval or within time windows.

### Docker Daemon

```yaml
services:
  ynamazon:
    image: ghcr.io/bakerboy448/ynamazon:latest
    command: ["yna", "daemon", "--interval", "20"]
    environment:
      - YNAB_API_KEY=${YNAB_API_KEY}
      - YNAB_BUDGET_ID=${YNAB_BUDGET_ID}
      - AMAZON_USER=${AMAZON_USER}
      - AMAZON_PASSWORD=${AMAZON_PASSWORD}
      - NON_INTERACTIVE=true
    restart: unless-stopped
```

## Notifications (Apprise)

Get notified when syncs complete or fail using [Apprise](https://github.com/caronc/apprise):

```bash
# Comma-separated Apprise URLs
APPRISE_URLS=discord://webhook_id/webhook_token,tgram://bot_token/chat_id
```

Apprise supports 100+ notification services including Discord, Telegram, Slack, Email, Pushover, and more. See the [Apprise wiki](https://github.com/caronc/apprise/wiki) for URL formats.

Notifications are sent for:
- Successful syncs (with match/update counts)
- Failed syncs (with error type)
- No matches found (warning)

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

## Two-Factor Authentication

If your Amazon account has 2FA enabled, set `AMAZON_OTP_SECRET_KEY` to your TOTP secret:

1. Go to Amazon > Account & Lists > Login & Security > Two-Step Verification
2. Add a new authenticator app
3. Click "Can't scan the barcode?" to reveal the secret key
4. Use this secret key as `AMAZON_OTP_SECRET_KEY`

The program will automatically generate OTP codes for login.

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
