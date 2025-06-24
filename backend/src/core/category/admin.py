from sqladmin.models import ModelView

from src.core.category.orm import CategoryDB


class CategoryAdmin(ModelView, model=CategoryDB):
    name = "Category"
    name_plural = "Categories"
    column_list = [CategoryDB.title]