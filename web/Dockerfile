FROM python:3.7-slim

# Set environment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . /usr/src/app
