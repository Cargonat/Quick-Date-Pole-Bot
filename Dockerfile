FROM python:3.11 as base

WORKDIR /app

RUN PIP_CACHE_DIR=/app/.pip-cache pip install poetry
RUN poetry config virtualenvs.in-project true

COPY pyproject.toml poetry.lock README.md ./
COPY qdpb/bot.py qdpb/bot.py

RUN poetry install --without dev

FROM python:3.11-slim

WORKDIR /app
COPY --from=base /app /app
RUN PIP_CACHE_DIR=/app/.pip-cache pip install poetry
RUN rm -rf PIP_CACHE_DIR

ENTRYPOINT [ "poetry", "run", "bot" ]
