import os
from decouple import config
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # optional

    # Third-party
    'crispy_forms',
    'allauth',  #
    'allauth.account',  #

    # local app
    'users.apps.UsersConfig',
    'home.apps.HomeConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',#
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kurdish_language.urls'

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

WSGI_APPLICATION = 'kurdish_language.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432
    }
}

"""
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
"""

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# links to detail
# https://medium.com/fueled-engineering/becoming-a-multilingual-super-hero-in-django-part-1-a000101514dd
# https://simpleisbetterthancomplex.com/tips/2016/10/17/django-tip-18-translations.html

# Provide a lists of languages which your site supports.
LANGUAGES = (
    # Translators: Language name.
    # Translators: ناوی زمان.
    ('en', _('English')),
    # Translators: Language name.
    # Translators: ناوی زمان.
    ('ku', _('Kurdish')),
    # Translators: Language name.
    # Translators: ناوی زمان.
    ('ar', _('Arabic')),
    # Translators: Language name.
    # Translators: ناوی زمان.
    ('tr', _('Turkey')),
    # Translators: Language name.
    # Translators: ناوی زمان.
    ('fa', _('Farsi')),
    # Translators: Kurdish dialect name.
    # Translators: ناوی دیالێکتی زمان.
    # ('ku-Kr', _('Kurdish Kirmanci')),
    # Translators: Kurdish dialect name.
    # Translators: ناوی دیالێکتی زمان.
    # ('ku-So', _('Kurdish Sorani')),
    # Translators: Kurdish dialect name.
    # Translators: ناوی دیالێکتی زمان.
    # ('ku-Sd', _('Kurdish Standard')),
)


# Set the default language for your site.
LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'ku'

TIME_ZONE = 'UTC'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery. Make sure it is set to
# True if you want to support localization
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# This sets the URL that we can use to use to reference static files.
# Note that it is important to include a trailing slash / at the end of the directory name.
STATIC_URL = '/static/'

# defines the location of static files in local development.
# In our project these will all live within a top-level static directory.
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]  #

# is the location of static files for production so it must be set to a different name,
# typically staticfiles. When it comes time to deploy a Django project,
# the collectstatic command will automatically compile all available static files
# throughout the entire project into a single directory.
# This is far faster than having static files sprinkled across the project as is the case in local development.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  #

# it tells Django how to look for static file directories.
# It is implicitly set for us and although this is an optional step,
# I prefer to make it explicit in all projects.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


# ##################
# my codes

# it will cause our project to use CustomUser instead of the default User model.
AUTH_USER_MODEL = 'users.CustomUser'  #

# normally django redirect user after login to /accounts/profile, but we want redirect to home page
LOGIN_REDIRECT_URL = 'home'  #

# like login , also determine where to go after logout, normally it goes to logout page of admin site
LOGOUT_REDIRECT_URL = 'home'  #


# django-crispy-forms
# it will provide pre-styled forms for us
CRISPY_TEMPLATE_PACK = 'bootstrap4'  #


# django-allauth config
SITE_ID = 1  # new

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',  #
)



