FROM python:3.10-slim as builder
WORKDIR /app
## Install poetry
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
ENV PATH=$PATH:/etc/poetry/bin

##
ADD ./poetry.lock ./pyproject.toml ./
RUN poetry config virtualenvs.in-project true
RUN poetry install --only main

CMD python manage.py migrate && python manage.py fill_database_with_data && python manage.py runserver 0.0.0.0:1111
