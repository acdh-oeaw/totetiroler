from .base import *

SECRET_KEY = '!i%7s@1+v&asdf*kljuke=ddsecxx-3dtms()pw^et!we'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SOCIAL_AUTH_FACEBOOK_KEY = 'KEY'
SOCIAL_AUTH_FACEBOOK_SECRET = 'SECRET_KEY'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'KEY'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'SECRET_KEY'
