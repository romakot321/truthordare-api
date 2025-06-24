from io import BytesIO
from uuid import UUID

from fastapi import File, Depends, APIRouter, UploadFile, BackgroundTasks

from src.truth.application.use_cases.dislike_truth import DislikeTruthUseCase
from src.truth.application.use_cases.get_random_truth import GetRandomTruthUseCase
from src.truth.application.use_cases.like_truth import LikeTruthUseCase
from src.truth.domain.dtos import TruthReadDTO, TruthRandomParamsDTO
from src.truth.api.dependencies import TruthUoWDepend
from src.truth.application.use_cases.get_truth import GetTruthUseCase

router = APIRouter()


@router.get("/random", response_model=list[TruthReadDTO])
async def get_random_truth(uow: TruthUoWDepend, params: TruthRandomParamsDTO = Depends()):
    return await GetRandomTruthUseCase(uow).execute(params)


@router.post("/{truth_id}/like", status_code=204)
async def like_truth(truth_id: UUID, uow: TruthUoWDepend):
    return await LikeTruthUseCase(uow).execute(truth_id)


@router.post("/{truth_id}/dislike", status_code=204)
async def dislike_truth(truth_id: UUID, uow: TruthUoWDepend):
    return await DislikeTruthUseCase(uow).execute(truth_id)


@router.get("/{task_id}", response_model=TruthReadDTO)
async def get_truth(task_id: UUID, uow: TruthUoWDepend):
    return await GetTruthUseCase(uow).execute(task_id)
