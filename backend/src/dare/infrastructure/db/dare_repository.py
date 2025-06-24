from uuid import UUID

from sqlalchemy import update, func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.exceptions import DBModelConflictException, DBModelNotFoundException
from src.dare.domain.entities import Dare, DareUpdate
from src.dare.infrastructure.db.orm import DareDB
from src.dare.application.interfaces.dare_repository import IDareRepository


class PGDareRepository(IDareRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def _flush(self):
        try:
            await self.session.flush()
        except IntegrityError as e:
            detail = "Model can't be created. " + str(e)
            raise DBModelConflictException(detail)

    async def get_by_pk(self, pk: UUID) -> Dare:
        model = await self.session.get(DareDB, pk)
        if model is None:
            raise DBModelNotFoundException()
        return self._to_domain(model)

    async def update_by_pk(self, pk: UUID, data: DareUpdate) -> Dare:
        update_data = data.model_dump(exclude_unset=True)
        if "like_increment" in update_data:
            update_data.pop("like_increment")
            update_data["likes"] = DareDB.likes + 1
        if "dislike_increment" in update_data:
            update_data.pop("dislike_increment")
            update_data["dislikes"] = DareDB.dislikes + 1

        query = update(DareDB).where(DareDB.id == pk).values(**update_data)
        await self.session.execute(query)
        await self._flush()
        return await self.get_by_pk(pk)

    async def get_random(self, count: int) -> list[Dare]:
        query = select(DareDB).order_by(func.random()).limit(count)
        models = await self.session.scalars(query)
        return [self._to_domain(model) for model in models]

    @staticmethod
    def _to_domain(model: DareDB) -> Dare:
        return Dare(
            id=model.id,
            text=model.text,
            likes=model.likes,
            dislikes=model.dislikes,
        )
