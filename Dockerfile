# Используем базовый образ Python с Poetry
FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN curl -sSL https://install.python-poetry.org | python -
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev --no-root

WORKDIR /app

COPY . /app/

CMD poetry run python manage.py migrate && poetry run python manage.py fill_database_with_data && poetry run python manage.py runserver 0.0.0.0:1111
