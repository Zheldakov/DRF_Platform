"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yhty6^$sjeg*!q1&c^xyb(5hx0mpvr*r)49wk=z#tit9cn0wi('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # base apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # installed apps
    'rest_framework',
    'django_filters',  # безопасное способ фильтрации данных через удобные для человека urls
    'rest_framework_simplejwt',  # авторизация по Токину (jason web token)
    'corsheaders',  # ограничение доступа к ресурсам на домене
    'drf_yasg',  # создание документации
    'redis',

    # project apps
    'users',

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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database указывает на работу с базой данных
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# Меняем настройки ДБ (в данном примере MS SQL Server)
load_dotenv()
USER = os.getenv('MS_SQL_USER')
PASSWORD = os.getenv('MS_SQL_KEY')
HOST = os.getenv('MS_SQL_SERVER')
DATABASE = os.getenv('MS_SQL_DATABASE')
SU_DJANGO_PASSWORD = os.getenv('SU_DJANGO_PASSWORD')
MS_SQL_DRIVER = os.getenv('MS_SQL_DRIVER')

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': DATABASE,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': '',
        'OPTIONS': {
            'driver': MS_SQL_DRIVER
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
        BASE_DIR / 'static',  # Путь к статическим файлам
)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# добавлена авторизована модель пользователя
AUTH_USER_MODEL = 'users.User'

# Путь, куда попадают не авторизованные пользователи, при использовании функций для авторизованных пользователей
LOGIN_URL = '/users/'

# Размещение и активация КЕШа
cache_status = os.getenv('CACHE_ENABLED')
CACHE_ENABLED = cache_status
if CACHE_ENABLED:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': os.getenv('CACHE_LOCATION'),
        }
    }

    REST_FRAMEWORK = {
        'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend',],
        'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication',],
        # 'DEFAULT_PERMISSION_CLASSES': ['rest_framework_permission.IsAuthenticated',],
        'DEFAULT_PERMISSION_CLASSES': ['rest_framework_permission.AllowAny',],
                }
    SIMPLE_JWT ={
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180),
        'REFRESH_TOKEN_LIFETIME': timedelta(minutes=30),
    }

    CORS_ALLOWED_ORIGINS = [
        'https://read-only.exemple.com',
        'https://read-and-write.exemple.com',
    ]

    CSRF_TRUSTED_ORIGINS = [
        'https://read-and-write.exemple.com',
    ]