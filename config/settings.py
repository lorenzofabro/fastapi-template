from functools import lru_cache

from dotenv import dotenv_values
from pydantic import BaseSettings

env = dotenv_values(".env")


class APISettings(BaseSettings):
    # Configs
    DEBUG: bool = env.get('DEBUG', True)
    ENVIRONMENT: str = env.get('ENVIRONMENT', 'local')
    SENTRY_DSN: str = env.get('SENTRY_DSN', '')
    REDIS_URL: str = env.get('REDIS_URL', 'redis://localhost:6379')
    SENTRY_ENVIRONMENT: str = env.get('SENTRY_ENVIRONMENT', 'local')

    # LOGGING
    LOGGING = 'fastapi'


@lru_cache()
def get_settings() -> APISettings:
    return APISettings()
