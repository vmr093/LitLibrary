import os
from pathlib import Path
from dotenv import load_dotenv
import os
import dj_database_url

load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('%*0h7^v)!&v*xswt7(1uxhc=r&5w=)a)de#c0u-3419$p3g3!')

# SECURITY WARNING: don't run with debug turned on in production!
if not 'ON_HEROKU' in os.environ:
    DEBUG = True


ALLOWED_HOSTS = ["*"]
  


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books_app',  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookcase.urls'

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

WSGI_APPLICATION = 'bookcase.wsgi.application'

# ✅ PostgreSQL Database Configuration
DATABASES = {
    if 'ON_HEROKU' in os.environ:
    DATABASES = {
        "default": dj_database_url.config(
            env='DATABASE_URL',
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True,
        ),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'books_app',
            # The value of 'NAME' should match the value of 'NAME' you replaced.
        }
    }
 
        'USER': 'vr',
        'PASSWORD': 'Nala1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Static & Media Files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_DIRS = [os.path.join(BASE_DIR, "books_app/static"),]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ✅ Authentication settings
LOGIN_URL = '/login/'  
LOGIN_REDIRECT_URL = '/books/'  
LOGOUT_REDIRECT_URL = '/login/'  

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
