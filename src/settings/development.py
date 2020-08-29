from src.settings.common import *

SECRET_KEY = "y4efc%jc#vm#pr5$4pie2h-9mw)ua_1=rw$v6&o&9_kvhajw$h"

DEBUG = True

INSTALLED_APPS += "debug_toolbar"

MIDDLEWARE.insert(2, "debug_toolbar.middleware.DebugToolbarMiddleware")

DATABASES = {
    "default": {
        "ENGINE": "django_tenants.postgresql_backend",
        "NAME": "default",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

TENANT_USERS_DOMAIN = "localhost"
