from sqlalchemy.orm import Mapped, relationship

from src.db.base import BaseMixin, Base


class CategoryDB(BaseMixin, Base):
    __tablename__ = "categories"

    title: Mapped[str]

    dares: Mapped[list["DareDB"]] = relationship(back_populates="category", lazy="noload")
    truths: Mapped[list["TruthDB"]] = relationship(back_populates="category", lazy="noload")

    def __str__(self):
        return self.title