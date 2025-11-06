from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.repositories import UserRepository
from app.schemas.auth import AuthResponse
from app.schemas.user import UserOut
from app.utils import JWTHandler, Password


class AuthService:
    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)
        self.jwt = JWTHandler()

    async def register(self, email: str, password: str) -> AuthResponse:
        exists = await self.repository.get_by_email(email)
        if exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists.",
            )

        hashed_password = Password.hash_password(password)
        user: User = await self.repository.register(email, hashed_password)

        token = self.jwt.create_token_pair(
            user_id=str(user.id),
            issuer="health_vision",
            roles=[],
        )

        return AuthResponse(
            user=UserOut.model_validate(user),
            token=token,
        )

    async def login(self, email: str, password: str) -> AuthResponse:
        user = await self.repository.get_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        if not Password.verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )
        token = self.jwt.create_token_pair(
            user_id=str(user.id),
            issuer="health_vision",
            roles=[],
        )

        return AuthResponse(
            user=UserOut.model_validate(user),
            token=token,
        )
