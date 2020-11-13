
import os
import dj_database_url
import django_heroku


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.herokuapp.com',  'kyotoman-app.herokuapp.com']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'sns',
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    
]

ROOT_URLCONF = 'django_app2.urls'

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
                'social_django.context_processors.backends', 
                'social_django.context_processors.login_redirect',
            ]
        },
    },
]

WSGI_APPLICATION = 'django_app2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_app2',
        'USER':'postgres',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#ファイルの文字コード
FILE_CHARSET = 'UTF-8'

#カスタムユーザを使用
AUTH_USER_MODEL = 'account.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/sns/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# メール送信の設定
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'heiheibonbon20120426@gmail.com'
#EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
#エラーの内容を送信
ADMINS = (('kyotoman', 'heiheibonbon20120426@gmail.com'),)
MANAGERS = ADMINSEMAIL_HOST = 'host'
SEND_BROKEN_LINK_EMAILS=True

#ログイン関連の設定
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'

#soxial-auth-app-django用
SOCIAL_AUTH_URL_NAMESPACE = 'social'
AUTHENTICATION_BACKENDS = [
    'social_core.backends.twitter.TwitterOAuth',    
    'django.contrib.auth.backends.ModelBackend',    
]

#リダイレクトURL
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index'

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

#githubに上げたくないものはlocal_settingsから持ってくる
try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:    
   SECRET_KEY = os.environ['SECRET_KEY']
   EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
   SOCIAL_AUTH_TWITTER_KEY = os.environ['SOCIAL_AUTH_TWITTER_KEY']
   SOCIAL_AUTH_TWITTER_SECRET = os.environ['SOCIAL_AUTH_TWITTER_SECRET']
   AUTHENTICATION_TOKEN = os.environ['AUTHENTICATION_TOKEN']
   AUTHENTICATION_SECRET = os.environ['AUTHENTICATION_SECRET']
   django_heroku.settings(locals())


import environ

ROOT_DIR = environ.Path(__file__) - 3  # (modern-django/config/settings/base.py - 3 = modern-django/)

env = environ.Env()

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR.path('.env')))