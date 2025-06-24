from sqlalchemy.ext.asyncio import AsyncSession

from src.db.engine import async_session_maker
from src.truth.application.interfaces.truth_uow import ITruthUnitOfWork
from src.truth.infrastructure.db.truth_repository import PGTruthRepository


class TruthUnitOfWork(ITruthUnitOfWork):
    def __init__(self, session_getter=async_session_maker) -> None:
        super().__init__()
        self.session_getter = session_getter

    async def __aenter__(self):
        self.session: AsyncSession = self.session_getter()
        self.truths = PGTruthRepository(self.session)
        return await super().__aenter__()

    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        await self.session.close()

    async def _commit(self):
        await self.session.commit()

    async def _rollback(self):
        await self.session.rollback()
