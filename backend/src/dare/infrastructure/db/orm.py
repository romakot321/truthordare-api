from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from src.core.language.orm import LanguageDB
from src.db.base import Base, BaseMixin


class DareDB(BaseMixin, Base):
    __tablename__ = "dares"

    text: Mapped[str]
    language_id: Mapped[UUID] = mapped_column(ForeignKey("languages.id", ondelete="CASCADE"))
    likes: Mapped[int] = mapped_column(server_default="0", default=0)
    dislikes: Mapped[int] = mapped_column(server_default="0", default=0)

    language: Mapped["LanguageDB"] = relationship(back_populates="dares", lazy="selectin")

    def __str__(self):
        return self.text