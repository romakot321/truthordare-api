import abc

from src.truth.application.interfaces.truth_repository import ITruthRepository


class ITruthUnitOfWork(abc.ABC):
    truths: ITruthRepository

    async def commit(self):
        return await self._commit()

    @abc.abstractmethod
    async def _commit(self): ...

    @abc.abstractmethod
    async def _rollback(self): ...

    async def __aenter__(self):
        return self

    async def __aexit__(self, *excinfo):
        await self._rollback()
