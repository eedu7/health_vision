from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def register(self, email: str, password: str) -> User:
        user = User(email=email, password=password)
        await self.create(user)
        await self.session.commit()
        return user
