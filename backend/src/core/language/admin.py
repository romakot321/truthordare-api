from sqladmin.models import ModelView

from src.core.language.orm import LanguageDB


class LanguageAdmin(ModelView, model=LanguageDB):
    name = "Language"
    column_list = [LanguageDB.title]