"""
* Django settings for src project.

* Generated by "django-admin startproject" using Django 3.1.

* For more information on this file, see
? https://docs.djangoproject.com/en/3.1/topics/settings/

* For the full list of settings and their values, see
? https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# * Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# * Django environ
# ? https://django-environ.readthedocs.io/en/latest/


# * Application definition

SHARED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.admin",
    "django_tenants",
    "apps.customers",
    "tenant_users.permissions",
    "tenant_users.tenants",
    "apps.users",
    "graphene_django",
    "corsheaders",
    "reversion",
    "guardian",
]

TENANT_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "tenant_users.permissions",
]

INSTALLED_APPS = SHARED_APPS + [app for app in TENANT_APPS if app not in SHARED_APPS]

MIDDLEWARE = [
    "django_tenants.middleware.main.TenantMainMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "src.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "src.wsgi.application"


# * Database
# ? https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASE_ROUTERS = ["django_tenants.routers.TenantSyncRouter"]


# * Password validation
# ? https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# * Password hashes
# ? https://docs.djangoproject.com/en/3.1/topics/auth/passwords/#using-argon2-with-django

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]


# * Internationalization
# ? https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# * Static files (CSS, JavaScript, Images)
# ? https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"


# * Auth settings

AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    "tenant_users.permissions.backend.UserBackend",
    "guardian.backends.ObjectPermissionBackend",
]


# * Tetants settings

TENANT_MODEL = "customers.Client"
TENANT_DOMAIN_MODEL = "customers.Domain"


# * Cors configuration

CORS_ORIGIN_ALLOW_ALL = True
