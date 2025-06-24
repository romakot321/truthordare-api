from io import BytesIO
from uuid import UUID

from fastapi import File, Depends, APIRouter, UploadFile, BackgroundTasks

from src.dare.application.use_cases.dislike_dare import DislikeDareUseCase
from src.dare.application.use_cases.get_random_dare import GetRandomDareUseCase
from src.dare.application.use_cases.like_dare import LikeDareUseCase
from src.dare.domain.dtos import DareReadDTO, DareRandomParamsDTO
from src.dare.api.dependencies import DareUoWDepend
from src.dare.application.use_cases.get_dare import GetDareUseCase

router = APIRouter()


@router.get("/random", response_model=list[DareReadDTO])
async def get_random_dare(uow: DareUoWDepend, params: DareRandomParamsDTO = Depends()):
    return await GetRandomDareUseCase(uow).execute(params)


@router.post("/{dare_id}/like", status_code=204)
async def like_dare(dare_id: UUID, uow: DareUoWDepend):
    return await LikeDareUseCase(uow).execute(dare_id)


@router.post("/{dare_id}/dislike", status_code=204)
async def dislike_dare(dare_id: UUID, uow: DareUoWDepend):
    return await DislikeDareUseCase(uow).execute(dare_id)


@router.get("/{task_id}", response_model=DareReadDTO)
async def get_dare(task_id: UUID, uow: DareUoWDepend):
    return await GetDareUseCase(uow).execute(task_id)
