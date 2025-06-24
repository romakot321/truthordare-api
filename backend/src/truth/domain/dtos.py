import inspect
from uuid import UUID
from typing import Type

from fastapi import Form
from pydantic import BaseModel, HttpUrl


class TruthReadDTO(BaseModel):
    id: UUID
    text: str


class TruthRandomParamsDTO(BaseModel):
    count: int = 1