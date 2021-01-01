from .base import *

INSTALLED_APPS += (
    'debug_toolbar', # and other apps for local development
)

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASE_URL = env('DATEBASE_URL')
DATABASES = {
    'default' : env.db(),
}

# メール送信の設定
EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')

#twitter関連
SOCIAL_AUTH_TWITTER_KEY = env('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = env('SOCIAL_AUTH_TWITTER_SECRET')
AUTHENTICATION_TOKEN = env('AUTHENTICATION_TOKEN')
AUTHENTICATION_SECRET = env('AUTHENTICATION_SECRET')