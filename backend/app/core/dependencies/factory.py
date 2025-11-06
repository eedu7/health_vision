from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.services import AuthService


def get_auth_service(session: Annotated[AsyncSession, Depends(get_async_session)]) -> AuthService:
    return AuthService(session)
