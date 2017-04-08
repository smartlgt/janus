"""
Django settings for janus project.

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b!z(^o(#z-%2m(izt*!wi(b%9i(oh$&o*n(*-hk3(^q8m#dd90'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_python3_ldap',

    'oauth2_provider',
    'corsheaders',

    'janus',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    #'oauth2_provider.middleware.OAuth2TokenMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# noinspection PyUnresolvedReferences
STATIC_ROOT = "/static/"

########################################
## OAUTH2
########################################

OAUTH2_PROVIDER_APPLICATION_MODEL = 'oauth2_provider.Application'

OAUTH2_PROVIDER = {
    'OAUTH2_VALIDATOR_CLASS': 'janus.oauth2_validators.OAuth2Validator',
}

CORS_ORIGIN_ALLOW_ALL = False


########################################
## LDAP
########################################

# The URL of the LDAP server.
LDAP_AUTH_URL = "ldap.exmaple.com"

# Initiate TLS on connection.
LDAP_AUTH_USE_TLS = True

# The LDAP search base for looking up users.
LDAP_AUTH_SEARCH_BASE = "OU=people,DC=example,DC=com"

# The LDAP class that represents a user.
LDAP_AUTH_OBJECT_CLASS = "inetOrgPerson"

# A tuple of django model fields used to uniquely identify a user.
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)

# enable this to set superuser, staff, activ and profile activ by drinks.ldap.sync_user_relations on every login
LDAP_AUTH_SYNC_PERMISSIONS = False


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'django_python3_ldap.auth.LDAPBackend', #disabled by default, enable if you need an ldap authentifiaction
)



try:
    from .local_settings import *
except:
    print("can't load local_settings.py or an error occurred while loading")