from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.dependencies import get_auth_service
from app.schemas.users import UserIn
from app.services import AuthService

router = APIRouter()


@router.post("/register")
async def register(data: UserIn, service: Annotated[AuthService, Depends(get_auth_service)]):
    return {"message": "User registered successfully"}
