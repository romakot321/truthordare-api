from sqladmin import ModelView

from src.dare.infrastructure.db.orm import DareDB


class DareAdmin(ModelView, model=DareDB):
    name = "Dare"
    page_size = 50
    column_list = [DareDB.language, DareDB.text, DareDB.likes, DareDB.dislikes]
    column_sortable_list = ["language", "likes", "dislikes"]
    form_excluded_columns = [DareDB.dislikes, DareDB.likes]
