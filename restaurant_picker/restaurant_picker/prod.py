"""
Django settings for production instance of restaurant_picker project
"""

from restaurant_picker.settings import *

DEBUG = False

import os
from pathlib import Path

from dotenv import load_dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DOTENV = os.path.join(BASE_DIR, '.env.development')
load_dotenv(dotenv_path=DOTENV)


SECRET_KEY = os.environ["SECRET_KEY"]


if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }


ALLOWED_HOSTS = [
    "whereshouldweeattoday.com",
    "*.us-east-1.elasticbeanstalk.com",
]


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

