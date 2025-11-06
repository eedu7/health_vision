from fastapi import HTTPException, status

from app.models import User
from app.repositories import UserRepository
from app.utils import Password


class AuthService:
    # TODO: Pass session instead of repository
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register(self, email: str, password: str):
        exists = await self.repository.get_by_email(email)
        if exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists.",
            )

        hashed_password = Password.hash_password(password)
        user: User = await self.repository.register(email, hashed_password)
        return user

    async def login(self, email: str, password: str):
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

        return user
