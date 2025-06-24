from uuid import UUID

from fastapi import HTTPException

from src.db.exceptions import DBModelNotFoundException
from src.dare.domain.dtos import DareReadDTO
from src.dare.application.interfaces.dare_uow import IDareUnitOfWork


class GetDareUseCase:
    def __init__(self, uow: IDareUnitOfWork):
        self.uow = uow

    async def execute(self, task_id: UUID) -> DareReadDTO:
        async with self.uow:
            try:
                task = await self.uow.dares.get_by_pk(task_id)
            except DBModelNotFoundException:
                raise HTTPException(404)
        return DareReadDTO(**task.model_dump())
