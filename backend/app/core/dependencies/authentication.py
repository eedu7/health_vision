from typing import Annotated

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class AuthenticationRequired:
    def __init__(
        self, request: Request, _: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer(auto_error=False))]
    ):
        if not request.state.user.id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authorization credentials were not provided.",
            )
