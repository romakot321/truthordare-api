from sqladmin import ModelView

from src.truth.infrastructure.db.orm import TruthDB


class TruthAdmin(ModelView, model=TruthDB):
    name = "Truth"
    column_list = [TruthDB.language, TruthDB.text, TruthDB.likes, TruthDB.dislikes]
    page_size = 50
    column_sortable_list = ["likes", "dislikes"]
    form_excluded_columns = [TruthDB.dislikes, TruthDB.likes]
