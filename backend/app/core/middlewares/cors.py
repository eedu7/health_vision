from typing import cast

from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.types import ASGIApp

from app.core.config import config

CORS_MIDDLEWARE = Middleware(
    cast(type[ASGIApp], CORSMiddleware),
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=config.CORS_ALLOW_CREDENTIALS,
    allow_methods=config.CORS_ALLOW_METHODS,
    allow_headers=config.CORS_ALLOW_HEADERS,
)
