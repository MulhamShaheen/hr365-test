FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY ./karnaukhov /app
WORKDIR /app

RUN apk update \
    && apk add gcc python3-dev postgresql-dev

RUN pip3 install -r requirements.txt

RUN python manage.py collectstatic --noinput
