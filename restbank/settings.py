import os
import environ
import dj_database_url
from django.conf.global_settings import DATETIME_INPUT_FORMATS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()


if "SECRET_KEY" in os.environ:
    SECRET_KEY = os.environ.get('SECRET_KEY')

else:
    SECRET_KEY = "TestDjango"

DEBUG = env("DEBUG")




ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'rest_framework',
    'rest_framework.authtoken',
    'daterange_filter',
    'storages',
    'home',
    'core',
    'user',
    'portfolio',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restbank.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'restbank.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# LOCALIZATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
DATETIME_INPUT_FORMATS += ('%Y-%m-%d %H:%M %p',)


# Get User model
AUTH_USER_MODEL = 'core.User'


# STATIC & MEDIA
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)



# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }

# - PGUSER = postgres
# - PGHOST = postgres
# - PGDATABASE = postgres
# - PGPASSWORD = postgres_password
# - PGPORT = 5432

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres_password",
        "HOST": "postgres",
        "PORT": 5432,
    }
}


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 500
}



if not DEBUG and "SECRET_KEY" in os.environ:
    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")

    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

    # s3 static settings

    STATIC_LOCATION = "static"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
    STATICFILES_STORAGE = "restbank.storage_backends.StaticStorage"




