#!/bin/sh
python /usr/src/app/manage.py makemigrations todo
python /usr/src/app/manage.py migrate
python /usr/src/app/manage.py collectstatic --noinput
/usr/local/bin/gunicorn docker_django.wsgi:application -w 2 -b :8000
