import inspect
from uuid import UUID
from typing import Type

from fastapi import Form
from pydantic import BaseModel, HttpUrl


class DareReadDTO(BaseModel):
    id: UUID
    text: str


class DareRandomParamsDTO(BaseModel):
    count: int = 1