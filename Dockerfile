# Build stage
FROM python:3.12-slim AS builder

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files first (better layer caching)
COPY pyproject.toml uv.lock ./

# Install dependencies to virtual env
RUN uv sync --frozen --no-dev --no-install-project

# Copy source code
COPY src/ ./src/

# Install the project itself
RUN uv sync --frozen --no-dev

# Runtime stage
FROM python:3.12-slim

# Install Chrome dependencies only (not full Chrome - use chromium)
RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Chrome environment
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /app

# Copy virtual env from builder
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src
COPY --from=builder /app/pyproject.toml /app/

# Add venv to PATH
ENV PATH="/app/.venv/bin:$PATH"
ENV VIRTUAL_ENV="/app/.venv"

# Environment variables (override via docker run -e or compose)
ENV YNAB_API_KEY=""
ENV YNAB_BUDGET_ID=""
ENV AMAZON_USER=""
ENV AMAZON_PASSWORD=""
ENV AMAZON_OTP_SECRET_KEY=""
ENV MATCH_EMPTY_MEMO="true"
ENV AMAZON_DEBUG="false"
ENV AMAZON_FULL_DETAILS="true"

# Non-root user for security
RUN useradd -m -u 1000 ynamazon && chown -R ynamazon:ynamazon /app
USER ynamazon

ENTRYPOINT ["yna"]
CMD ["ynamazon"]
