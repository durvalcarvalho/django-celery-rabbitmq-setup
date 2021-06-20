#!/usr/bin/env bash

pip install -r requirements.txt

python3 manage.py migrate

python3 manage.py wait_for_db

python manage.py runserver 0.0.0.0:8000