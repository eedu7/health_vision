from fastapi import FastAPI

from app.api import router


def create_app():
    app_ = FastAPI()
    app_.include_router(router)
    return app_


app = create_app()
