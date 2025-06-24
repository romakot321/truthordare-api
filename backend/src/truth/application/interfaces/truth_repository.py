import abc
from uuid import UUID

from src.truth.domain.entities import Truth, TruthUpdate


class ITruthRepository(abc.ABC):
    @abc.abstractmethod
    async def get_by_pk(self, pk: UUID) -> Truth: ...

    @abc.abstractmethod
    async def update_by_pk(self, pk: UUID, data: TruthUpdate) -> Truth: ...

    @abc.abstractmethod
    async def get_random(self, count: int) -> list[Truth]: ...
