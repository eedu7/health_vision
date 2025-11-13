from fastapi import FastAPI

from app.api import router

from .middlewares import make_middleware


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
