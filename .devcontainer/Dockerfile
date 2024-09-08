FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y curl build-essential libpq-dev
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry install --no-root
