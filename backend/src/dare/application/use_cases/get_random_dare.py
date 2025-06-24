from src.dare.application.interfaces.dare_uow import IDareUnitOfWork
from src.dare.domain.dtos import DareRandomParamsDTO, DareReadDTO
from src.dare.domain.entities import Dare


class GetRandomDareUseCase:
    def __init__(self, uow: IDareUnitOfWork):
        self.uow = uow

    async def execute(self, params: DareRandomParamsDTO) -> list[DareReadDTO]:
        async with self.uow:
            models = await self.uow.dares.get_random(params.count)
        return [DareReadDTO.model_validate(m.model_dump()) for m in models]
