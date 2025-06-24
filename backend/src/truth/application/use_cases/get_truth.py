from uuid import UUID

from fastapi import HTTPException

from src.db.exceptions import DBModelNotFoundException
from src.truth.domain.dtos import TruthReadDTO
from src.truth.application.interfaces.truth_uow import ITruthUnitOfWork


class GetTruthUseCase:
    def __init__(self, uow: ITruthUnitOfWork):
        self.uow = uow

    async def execute(self, task_id: UUID) -> TruthReadDTO:
        async with self.uow:
            try:
                task = await self.uow.truths.get_by_pk(task_id)
            except DBModelNotFoundException:
                raise HTTPException(404)
        return TruthReadDTO(**task.model_dump())
