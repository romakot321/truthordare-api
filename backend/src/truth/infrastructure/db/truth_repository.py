from uuid import UUID

from sqlalchemy import update, func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.exceptions import DBModelConflictException, DBModelNotFoundException
from src.truth.domain.entities import Truth, TruthUpdate
from src.truth.infrastructure.db.orm import TruthDB
from src.truth.application.interfaces.truth_repository import ITruthRepository


class PGTruthRepository(ITruthRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def _flush(self):
        try:
            await self.session.flush()
        except IntegrityError as e:
            detail = "Model can't be created. " + str(e)
            raise DBModelConflictException(detail)

    async def get_by_pk(self, pk: UUID) -> Truth:
        model = await self.session.get(TruthDB, pk)
        if model is None:
            raise DBModelNotFoundException()
        return self._to_domain(model)

    async def update_by_pk(self, pk: UUID, data: TruthUpdate) -> Truth:
        update_data = data.model_dump(exclude_unset=True)
        if "like_increment" in update_data:
            update_data.pop("like_increment")
            update_data["likes"] = TruthDB.likes + 1
        if "dislike_increment" in update_data:
            update_data.pop("dislike_increment")
            update_data["dislikes"] = TruthDB.dislikes + 1

        query = update(TruthDB).where(TruthDB.id == pk).values(**update_data)
        await self.session.execute(query)
        await self._flush()
        return await self.get_by_pk(pk)

    async def get_random(self, count: int) -> list[Truth]:
        query = select(TruthDB).order_by(func.random()).limit(count)
        models = await self.session.scalars(query)
        return [self._to_domain(model) for model in models]

    @staticmethod
    def _to_domain(model: TruthDB) -> Truth:
        return Truth(
            id=model.id,
            text=model.text,
            likes=model.likes,
            dislikes=model.dislikes,
        )
