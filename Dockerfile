FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pipenv
WORKDIR /usr/src/app/

COPY Pipfile Pipfile.lock /usr/src/app/
RUN pipenv install --system --deploy

COPY . /usr/src/app/
