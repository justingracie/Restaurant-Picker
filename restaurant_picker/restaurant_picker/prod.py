"""
Django settings for production instance of restaurant_picker project
"""

import os
from restaurant_picker.settings import *

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]


if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }


ALLOWED_HOSTS = [
    "whereshouldweeattoday.com",
    "*.us-east-2.elasticbeanstalk.com",
]


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

