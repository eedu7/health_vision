from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import config

CORS_MIDDLEWARE = Middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=config.CORS_ALLOW_CREDENTIALS,
    allow_methods=config.CORS_ALLOW_METHODS,
    allow_headers=config.CORS_ALLOW_HEADERS,
)
