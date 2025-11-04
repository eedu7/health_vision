from app.repositories import UserRepository


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register(self, email: str, password: str):
        user = await self.repository.register(email, password)
        return user
