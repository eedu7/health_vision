from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.repositories import UserRepository
from app.services import AuthService


# TODO: Pass session instead of repository
def get_auth_service(session: Annotated[AsyncSession, Depends(get_async_session)]) -> AuthService:
    repository = UserRepository(session)
    return AuthService(repository)
