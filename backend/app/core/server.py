from typing import List

from fastapi import FastAPI
from fastapi.middleware import Middleware

from app.api import router
from app.core.middlewares import CORS_MIDDLEWARE, AuthenticationMiddleware


def make_middleware() -> List[Middleware]:
    return [Middleware(AuthenticationMiddleware), CORS_MIDDLEWARE]


def create_app():
    app_ = FastAPI(
        title="Health Vision API",
        description="API for Health Vision application",
        version="1.0.0",
        middleware=make_middleware(),
    )
    app_.include_router(router)
    return app_


app = create_app()
