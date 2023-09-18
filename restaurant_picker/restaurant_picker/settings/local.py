import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DOTENV = os.path.join(BASE_DIR, '.env.development')
if not os.path.exists(DOTENV):
    raise ImportError
load_dotenv(dotenv_path=DOTENV)

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", 'django-insecure-zgca&_yo8=*e80*)8ck6g_d)#%3n%9q6x-xvopsuzwsn*hh*3&')

ALLOWED_HOST = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

