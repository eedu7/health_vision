from typing import Annotated

from fastapi import APIRouter, Depends

from app.controllers import AuthController
from app.core.dependencies import AuthenticationRequired
from app.core.factory import get_auth_controller

router = APIRouter(
    dependencies=[Depends(AuthenticationRequired)],
)


@router.get("/me")
async def get_current_user(service: Annotated[AuthController, Depends(get_auth_controller)]):
    raise NotImplementedError("Get current user functionality is not implemented yet.")


@router.put("/me")
async def update_current_user(service: Annotated[AuthController, Depends(get_auth_controller)]):
    raise NotImplementedError("Update current user functionality is not implemented yet.")
