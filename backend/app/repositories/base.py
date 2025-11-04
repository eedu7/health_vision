from typing import Generic, Type, TypeVar
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def create(self, obj_in: ModelType) -> ModelType:
        self.session.add(obj_in)
        await self.session.flush()  # Assigns ID but doesn't commit
        await self.session.refresh(obj_in)
        return obj_in

    async def get_by_id(self, _id: UUID) -> ModelType | None:
        stmt = select(self.model).where(self.model.id == _id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
