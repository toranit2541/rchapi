from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()  # loads .env into os.environ


BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"


DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"
ALLOW_INTERNAL_HTTP = os.getenv("ALLOW_INTERNAL_HTTP", "false").lower() == "true"

if DEBUG or ALLOW_INTERNAL_HTTP:
    # Development or internal access
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_SSL_REDIRECT = False
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
    # CORS_ALLOW_ALL_ORIGINS = True
else:
    # Production
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = False
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    # CORS_ALLOW_ALL_ORIGINS = False
    # CORS_ALLOWED_ORIGINS = [
    #     "https://www.ruamchai.com",
    #     "https://ruamchai.com",
    # ]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
        "https://www.ruamchai.com",
        "https://ruamchai.com",
        "http://localhost:8000"
]

CSRF_TRUSTED_ORIGINS = [
    "https://www.ruamchai.com",
    "https://ruamchai.com",
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]


INTERNAL_IPS = ['192.168.0.254','192.168.26.9']

# Fix this
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'fallback-key-change-this')


ALLOWED_HOSTS = [
    'ruamchai.com',
    'www.ruamchai.com',
    '192.168.0.254',
    '192.168.26.9',
    '192.168.10.111',
    '127.0.0.1',
    'localhost',
]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account.apps.AccountConfig',
    'rchdata.apps.RchdataConfig',
    'rchnews.apps.RchnewsConfig',
    'rchpopulation.apps.RchpopulationConfig',
    'rchpackage.apps.RchpackageConfig',
    'rcharticle.apps.RcharticleConfig',
    'rcheven.apps.RchevenConfig',
    'rchpromotion.apps.RchpromotionConfig',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'versatileimagefield',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

ROOT_URLCONF = 'rchapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'rchapi.wsgi.application'

DATABASES = {
    "default": {
        'ENGINE': 'mssql',
        'NAME': os.getenv('DB_NAME', 'Ruamchai'),
        'USER': os.getenv('DB_USER', 'sa'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', '1433'),
        "OPTIONS": {
            "driver": os.getenv('DB_DRIVER', 'ODBC Driver 17 for SQL Server'),
        },
    },
}


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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = '/static/'
APPEND_SLASH = False
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
