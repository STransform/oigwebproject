
import os
from pathlib import Path
from django.contrib.admin.options import ModelAdmin as DEFAULT_MODEL_ADMIN

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vl1osx-&@rl##2ogt%^kv$dri#h)tppm8)&5qg1f+i233$g$2$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# lists of allowed hosts
ALLOWED_HOSTS = ['localhost',  '127.0.0.1', ]
CSRF_COOKIE_SECURE = True

# Application definition

INSTALLED_APPS = [
    # Core Django apps (required for auth and contenttypes)
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    # Your custom app with the UserProfile model
    'accounts',  # Must come before apps that depend on AUTH_USER_MODEL

    # Third-party apps
    'djangocms_admin_style',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'djangocms_alias',
    'djangocms_versioning',
    'filer',
    'easy_thumbnails',
    'djangocms_text_ckeditor',
    'djangocms_frontend',
    'djangocms_frontend.contrib.accordion',
    'djangocms_frontend.contrib.alert',
    'djangocms_frontend.contrib.badge',
    'djangocms_frontend.contrib.card',
    'djangocms_frontend.contrib.carousel',
    'djangocms_frontend.contrib.collapse',
    'djangocms_frontend.contrib.content',
    'djangocms_frontend.contrib.grid',
    'djangocms_frontend.contrib.image',
    'djangocms_frontend.contrib.jumbotron',
    'djangocms_frontend.contrib.link',
    'djangocms_frontend.contrib.listgroup',
    'djangocms_frontend.contrib.media',
    'djangocms_frontend.contrib.tabs',
    'djangocms_frontend.contrib.utilities',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_googlemap',
    'djangocms_snippet',
    'djangocms_style',

    # Your other custom apps
    'about_us',
    'news',
    'dashboard',
    'task_manager',
    'blogs',
    'core',
    'services',

    # Admin (should come last)
    'django.contrib.admin',
]

CUSTOM_INSTALLED_APPS = [
    'about_us',
    # 'documents',
    'news',
    'dashboard',
    'blogs',
    'accounts',
    'core',
]

#  to process requests and responses before and after they reach the view.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    
    
    # cms
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    
]

ROOT_URLCONF = 'oigwebproject.urls'

# template directory
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
                'core.context_processors.stgs',
                # cms
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                
            ],
        },
    },
]


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

# specifies the full path to the Django's runserver command
WSGI_APPLICATION = 'oigwebproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oig',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# password validator
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

# default language
LANGUAGE_CODE = 'en'

# other languages
LANGUAGES = [
    ('en', ('English')),
    ('ax', ('Amharic')),
    ('ox', ('Afaan Oromoo')),
    
]






LOCALE_PATHS = [ os.path.join(BASE_DIR,'locale'), ]

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True

USE_TZ = True

GRAPH_MODELS ={
    'all_applications': True,
    'graph_models': True,
    }

# static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR, "static"]

# media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# settings.py

AUTH_USER_MODEL = 'accounts.UserProfile'

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# send email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'stemesgent@gmail.com'
EMAIL_HOST_PASSWORD = 'bjatascgxcuiwzlb'  # App-specific password,
EMAIL_FROM = 'Simon <stemesgent@gmail.com>'

# Package settings

## cms settings
SITE_ID = 1

# cms template settings
CMS_TEMPLATES = (
    ("front/cms_bases/cms_base.html", ("Cms Base Template")),
    ("front/cms_bases/cms_home_base.html", ("Homepage Template")),
)


CMS_CONFIRM_VERSION4 = True
# Allow admin sidebar to open admin URLs | Allow embedding from the same origin
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Enable inline editing with djangocms-text-ckeditor
# https://github.com/django-cms/djangocms-text-ckeditor#inline-editing-feature
TEXT_INLINE_EDITING = True
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

INTERNAL_IPS = ["127.0.0.1",]

DJANGOCMS_VERSIONING_ALLOW_DELETING_VERSIONS = True


CORS_ORIGIN_ALLOW_ALL = True
CSP_MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',

]

# Allow resources from the same origin
CSP_DEFAULT_SRC = ("'self'",)  

# Allow embedding from specific domains
CSP_FRAME_SRC = ("'self'",)

# implement the search field for filer package 
DEFAULT_MODEL_ADMIN.search_fields = ['']

## Security Settings

# A custom setting to set maximum allowed concurrent session for a user
MAX_ALLOWED_CONCURRENT_SESSIONS = 2

SESSION_MINS = 60 # The length of minutes for user sessions to expire
SESSION_COOKIE_AGE = SESSION_MINS * 60 # Expire user sessions after 30 mins
SESSION_EXPIRE_AT_BROWSER_CLOSE = True # Logout if the user closes the browser

# After SSL is configured
# SECURE_SSL_REDIRECT = True # Redirect all requests to SSl
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True # Use ssl for subdomains too
# CSRF_COOKIE_SECURE = True # No csrf for http requests
# SESSION_COOKIE_SECURE = True # No Session for http request




