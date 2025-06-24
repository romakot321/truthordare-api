from typing import Annotated

from fastapi import Depends

from src.truth.infrastructure.db.unit_of_work import TruthUnitOfWork
from src.truth.application.interfaces.truth_uow import ITruthUnitOfWork


def get_truth_uow() -> ITruthUnitOfWork:
    return TruthUnitOfWork()


TruthUoWDepend = Annotated[ITruthUnitOfWork, Depends(get_truth_uow)]
