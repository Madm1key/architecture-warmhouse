FROM python:3.14.2-alpine3.23 AS builder

WORKDIR /app
COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==2.2.1 \
    && poetry config virtualenvs.in-project true \
    && poetry install --no-interaction --no-ansi

FROM python:3.14.2-alpine3.23

COPY --from=builder /app /app
COPY app.py ./

CMD ["/app/.venv/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081"]
