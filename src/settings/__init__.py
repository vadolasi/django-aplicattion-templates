import environ

env = environ.Env()
environ.Env.read_env()

if env("SETTINGS") == "development":
    from src.settings.development import *
else:
    from src.settings.production import *
