FROM python:3.8.19-slim-bullseye

# Set environment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD Pipfile /usr/src/app
ADD Pipfile.lock /usr/src/app

RUN python -m pip install --upgrade pip

RUN python -m pip install pipenv

COPY requirements.txt requirements.txt
RUN pipenv install --system

COPY . /usr/src/app
