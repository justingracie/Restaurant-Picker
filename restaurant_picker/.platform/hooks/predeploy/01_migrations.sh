#!/bin/bash

source /var/app/venv/*/bin/activate
cd /var/app/current

python manage.py makemigrations
python manage.py migrate
python manage.py shell < ./generate_qa_fixtures.py
python manage.py loaddata setup_qa
python manage.py collectstatic --noinput