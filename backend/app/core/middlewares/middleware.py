from typing import List, cast

from fastapi.middleware import Middleware
from starlette.types import ASGIApp

from .authentication import AuthenticationMiddleware
from .cors import CORS_MIDDLEWARE


def make_middleware() -> List[Middleware]:
    return [Middleware(cast(type[ASGIApp], AuthenticationMiddleware)), CORS_MIDDLEWARE]
