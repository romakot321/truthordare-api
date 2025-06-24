from typing import Annotated

from fastapi import Depends

from src.dare.infrastructure.db.unit_of_work import DareUnitOfWork
from src.dare.application.interfaces.dare_uow import IDareUnitOfWork


def get_dare_uow() -> IDareUnitOfWork:
    return DareUnitOfWork()


DareUoWDepend = Annotated[IDareUnitOfWork, Depends(get_dare_uow)]
