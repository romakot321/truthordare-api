import abc
from uuid import UUID

from src.dare.domain.entities import Dare, DareUpdate


class IDareRepository(abc.ABC):
    @abc.abstractmethod
    async def get_by_pk(self, pk: UUID) -> Dare: ...

    @abc.abstractmethod
    async def update_by_pk(self, pk: UUID, data: DareUpdate) -> Dare: ...

    @abc.abstractmethod
    async def get_random(self, count: int) -> list[Dare]: ...
