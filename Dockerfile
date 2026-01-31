FROM python:3.12-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential zlib1g-dev libjpeg-dev && \
    rm -rf /var/lib/apt/lists/*
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-dev --no-install-project
COPY src/ ./src/
RUN uv sync --frozen --no-dev

FROM python:3.12-slim
RUN apt-get update && \
    apt-get install -y --no-install-recommends chromium chromium-driver && \
    rm -rf /var/lib/apt/lists/*
RUN useradd -m ynamazon
WORKDIR /app
RUN mkdir -p /app/output /app/config && chown -R ynamazon:ynamazon /app
COPY --from=builder --chown=ynamazon:ynamazon /app/.venv /app/.venv
COPY --from=builder --chown=ynamazon:ynamazon /app/src /app/src
ENV PATH="/app/.venv/bin:$PATH" \
    VIRTUAL_ENV="/app/.venv" \
    CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER_PATH=/usr/bin/chromedriver \
    MATCH_EMPTY_MEMO="true" \
    AMAZON_DEBUG="false" \
    AMAZON_FULL_DETAILS="true"
USER ynamazon
ENTRYPOINT ["yna"]
CMD ["ynamazon"]
