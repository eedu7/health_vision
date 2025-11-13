from typing import Annotated

from fastapi import APIRouter, Depends

from app.controllers import AuthController
from app.core.factory import get_auth_controller

router = APIRouter()


@router.post("/verify-email")
async def verify_email(service: Annotated[AuthController, Depends(get_auth_controller)]):
    raise NotImplementedError("Email verification functionality is not implemented yet.")


@router.post("/resend-verification")
async def resend_verification(service: Annotated[AuthController, Depends(get_auth_controller)]):
    raise NotImplementedError("Resend verification functionality is not implemented yet.")
