#!/usr/bin/env bash

pip install -r requirements.txt

celery -A config worker -l INFO