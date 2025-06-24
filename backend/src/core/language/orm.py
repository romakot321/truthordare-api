from sqlalchemy.orm import Mapped, relationship

from src.db.base import BaseMixin, Base


class LanguageDB(BaseMixin, Base):
    __tablename__ = "languages"

    title: Mapped[str]

    dares: Mapped[list["DareDB"]] = relationship(back_populates="language", lazy="noload")
    truths: Mapped[list["TruthDB"]] = relationship(back_populates="language", lazy="noload")

    def __str__(self):
        return self.title