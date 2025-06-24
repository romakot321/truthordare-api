from io import BytesIO
from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class Dare(BaseModel):
    id: UUID
    text: str
    likes: int
    dislikes: int


class DareUpdate(BaseModel):
    like_increment: bool | None = None
    dislike_increment: bool | None = None
