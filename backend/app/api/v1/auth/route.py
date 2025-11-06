from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.core.dependencies import get_auth_service
from app.schemas.auth import AuthResponse, UserCreate, UserLogin
from app.services import AuthService

router = APIRouter()


@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register(data: UserCreate, service: Annotated[AuthService, Depends(get_auth_service)]):
    return await service.register(data.email, data.password)


@router.post("/login", response_model=AuthResponse, status_code=status.HTTP_200_OK)
async def login(data: UserLogin, service: Annotated[AuthService, Depends(get_auth_service)]):
    return await service.login(data.email, data.password)


@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout(service: Annotated[AuthService, Depends(get_auth_service)]):
    raise NotImplementedError("Logout functionality is not implemented yet.")


@router.post("/refresh", status_code=status.HTTP_200_OK)
async def refresh(service: Annotated[AuthService, Depends(get_auth_service)]):
    raise NotImplementedError("Token refresh functionality is not implemented yet.")
