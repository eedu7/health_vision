from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.dependencies import get_auth_service
from app.services import AuthService

router = APIRouter()


@router.post("/verify-email")
async def verify_email(service: Annotated[AuthService, Depends(get_auth_service)]):
    raise NotImplementedError("Email verification functionality is not implemented yet.")


@router.post("/resend-verification")
async def resend_verification(service: Annotated[AuthService, Depends(get_auth_service)]):
    raise NotImplementedError("Resend verification functionality is not implemented yet.")
