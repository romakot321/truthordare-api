from uuid import UUID

from src.dare.application.interfaces.dare_uow import IDareUnitOfWork
from src.dare.domain.entities import DareUpdate


class DislikeDareUseCase:
    def __init__(self, uow: IDareUnitOfWork):
        self.uow = uow

    async def execute(self, dare_id: UUID) -> None:
        command = DareUpdate(dislike_increment=True)
        async with self.uow:
            await self.uow.dares.update_by_pk(dare_id, command)
            await self.uow.commit()
