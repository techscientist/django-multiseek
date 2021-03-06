# Django settings for test_project project.

import os, sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEMPLATE_CONTEXT_PROCESSORS = (
      'django.core.context_processors.request',
      'django.core.context_processors.static',
      'django.contrib.auth.context_processors.auth',
      'django.core.context_processors.i18n'
)

ADMINS = (
    ('Your Name', 'root@localhost'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '', '../db.sqlite')),
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "../", "static"))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(_163dr0#ijuk2=13)wlkc#cqdnj&f^uy@vuo)$@&tz%d1jand'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

if 'test' in sys.argv:
    # XXX IMPORTANT XXX Remove LocaleMiddleware in case of testing
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES[:-1]

ROOT_URLCONF = 'test_project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'test_project.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'test_app',
    'multiseek',
    #'django_nose',
    'djangobower'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

MULTISEEK_REGISTRY = 'test_app.multiseek_registry'

#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

SELENIUM_DRIVER = "Remote"
SELENIUM_CAPABILITIES = {"browser": "firefox"}

# django-multiseek needs jquery, jquery-ui
BOWER_INSTALLED_APPS = (
    'jquery',
    'jqueryui',
    'datetimepicker',

    # You don't need foundation for multiseek, only jquery.
    # Foundation is used in test_project only
    'foundation',
    'foundation-datepicker',
    'font-awesome',

    # For nice jQuery calendar
    'https://raw.githubusercontent.com/taitems/Aristo-jQuery-UI-Theme/master/css/Aristo/Aristo.css',

    # for translated jQuery calendar
    'https://jquery-ui.googlecode.com/svn-history/r3243/trunk/ui/i18n/jquery.ui.datepicker-pl.js'
)

BOWER_COMPONENTS_ROOT = os.path.join(os.path.dirname(__file__), '..', 'components')
