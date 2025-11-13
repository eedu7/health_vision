from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers import AuthController
from app.core.db import get_async_session


def get_auth_controller(session: Annotated[AsyncSession, Depends(get_async_session)]) -> AuthController:
    return AuthController(session)
