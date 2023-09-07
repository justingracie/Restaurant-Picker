"""
Django settings for production instance of restaurant_picker project
"""
import os
import socket



DEBUG = False

print("using prod settings")

SECRET_KEY = os.environ["SECRET_KEY"]


if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

_hostname = socket.gethostname()
_local_ip = socket.gethostbyname(_hostname)

ALLOWED_HOSTS = [
    "whereshouldweeattoday.com",
    "*.us-east-2.elasticbeanstalk.com",
    _local_ip,
]


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
USE_X_FORWARDED_PORT = True

# Logging Config
LOGGING = {
    'version': 1,
    'formatters': {
        'timeFormat': {
            'format': '[%(asctime)s] [%(name)s:line%(lineno)d] [%(levelname)s] %(message)s',
            'datefmt': '%m/%d/%Y %I:%M:%S%p',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'timeFormat',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        # empty string defaults to root logger
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
