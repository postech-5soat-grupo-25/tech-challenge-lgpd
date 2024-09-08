FROM python:3.11-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y curl build-essential libpq-dev
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root
COPY source /app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]