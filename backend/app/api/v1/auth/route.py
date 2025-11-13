from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.controllers import AuthController
from app.core.factory import get_auth_controller
from app.schemas.auth import AuthResponse, UserCreate, UserLogin

router = APIRouter()


@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register(data: UserCreate, service: Annotated[AuthController, Depends(get_auth_controller)]):
    return await service.register(data.email, data.password)


@router.post("/login", response_model=AuthResponse, status_code=status.HTTP_200_OK)
async def login(data: UserLogin, service: Annotated[AuthController, Depends(get_auth_controller)]):
    return await service.login(data.email, data.password)


@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout(service: Annotated[AuthController, Depends(get_auth_controller)]):
    raise NotImplementedError("Logout functionality is not implemented yet.")


@router.post("/refresh", status_code=status.HTTP_200_OK)
async def refresh(service: Annotated[AuthController, Depends(get_auth_controller)]):
    raise NotImplementedError("Token refresh functionality is not implemented yet.")
