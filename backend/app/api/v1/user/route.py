from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.dependencies import get_auth_service
from app.services import AuthService

router = APIRouter()


@router.get("/me")
async def get_current_user(service: Annotated[AuthService, Depends(get_auth_service)]):
    raise NotImplementedError("Get current user functionality is not implemented yet.")


@router.put("/me")
async def update_current_user(service: Annotated[AuthService, Depends(get_auth_service)]):
    raise NotImplementedError("Update current user functionality is not implemented yet.")
