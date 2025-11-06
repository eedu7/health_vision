from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.dependencies import get_auth_service
from app.services import AuthService

router = APIRouter()


@router.post("/forgot-password")
async def forgot_password(service: Annotated[AuthService, Depends(get_auth_service)]):
    raise NotImplementedError("Forgot password functionality is not implemented yet.")


@router.post("/reset-password")
async def reset_password(service: Annotated[AuthService, Depends(get_auth_service)]):
    raise NotImplementedError("Password reset functionality is not implemented yet.")


@router.post("/change-password")
async def change_password(service: Annotated[AuthService, Depends(get_auth_service)]):
    raise NotImplementedError("Password change functionality is not implemented yet.")
