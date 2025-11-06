from fastapi import status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.schemas.current_user import CurrentUser
from app.utils import JWTHandler


class AuthenticationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, dispatch=None):
        super().__init__(app, dispatch)
        self.jwt_handler = JWTHandler()

    async def dispatch(self, request, call_next):
        request.state.user = CurrentUser()
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return await call_next(request)

        parts = auth_header.split(" ")
        if len(parts) != 2:
            return await call_next(request)

        schema, token = parts
        if schema.lower() != "bearer":
            return await call_next(request)

        try:
            payload = self.jwt_handler.decode(token, expected_type="access")
        except ValueError as e:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": str(e)},
            )

        user_id = payload.get("sub")
        request.state.user.id = user_id

        return await call_next(request)
