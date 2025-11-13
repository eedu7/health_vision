from typing import Annotated

from fastapi import APIRouter, Depends

from app.controllers import AuthController
from app.core.factory import get_auth_controller

router = APIRouter()


@router.post("/forgot-password")
async def forgot_password(service: Annotated[AuthController, Depends(get_auth_controller)]):
    raise NotImplementedError("Forgot password functionality is not implemented yet.")


@router.post("/reset-password")
async def reset_password(service: Annotated[AuthController, Depends(get_auth_controller)]):
    raise NotImplementedError("Password reset functionality is not implemented yet.")


@router.post("/change-password")
async def change_password(service: Annotated[AuthController, Depends(get_auth_controller)]):
    raise NotImplementedError("Password change functionality is not implemented yet.")
