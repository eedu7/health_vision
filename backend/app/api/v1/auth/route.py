from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.dependencies import get_auth_service
from app.schemas.auth import UserCreate, UserLogin
from app.services import AuthService

router = APIRouter()


@router.post("/register")
async def register(data: UserCreate, service: Annotated[AuthService, Depends(get_auth_service)]):
    return await service.register(data.email, data.password)


@router.post("/login")
async def login(data: UserLogin, service: Annotated[AuthService, Depends(get_auth_service)]):
    return await service.login(data.email, data.password)


@router.post("/logout")
async def logout(service: Annotated[AuthService, Depends(get_auth_service)]):
    raise NotImplementedError("Logout functionality is not implemented yet.")


@router.post("/refresh")
async def refresh(service: Annotated[AuthService, Depends(get_auth_service)]):
    raise NotImplementedError("Token refresh functionality is not implemented yet.")
