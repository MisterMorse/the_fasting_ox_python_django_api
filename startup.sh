#!/bin/bash
python3 manage.py collectstatic && gunicorn --workers 2 the_fasting_ox_python_django_api.wsgi.application
