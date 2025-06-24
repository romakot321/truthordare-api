from uuid import UUID

from src.truth.application.interfaces.truth_uow import ITruthUnitOfWork
from src.truth.domain.entities import TruthUpdate


class LikeTruthUseCase:
    def __init__(self, uow: ITruthUnitOfWork):
        self.uow = uow

    async def execute(self, truth_id: UUID) -> None:
        command = TruthUpdate(like_increment=True)
        async with self.uow:
            await self.uow.truths.update_by_pk(truth_id, command)
            await self.uow.commit()
