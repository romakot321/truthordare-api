from src.truth.application.interfaces.truth_uow import ITruthUnitOfWork
from src.truth.domain.dtos import TruthRandomParamsDTO, TruthReadDTO
from src.truth.domain.entities import Truth


class GetRandomTruthUseCase:
    def __init__(self, uow: ITruthUnitOfWork):
        self.uow = uow

    async def execute(self, params: TruthRandomParamsDTO) -> list[TruthReadDTO]:
        async with self.uow:
            models = await self.uow.truths.get_random(params.count)
        return [TruthReadDTO.model_validate(m.model_dump()) for m in models]
