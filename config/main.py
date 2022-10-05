from logging.config import dictConfig

import sentry_sdk
from config import settings as config
from fastapi import FastAPI

from .logger_config import LogConfig

app = FastAPI()

settings = config.get_settings()

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    environment=settings.SENTRY_ENVIRONMENT,
    traces_sample_rate=1.0,
)

# Logger
dictConfig(LogConfig().dict())
