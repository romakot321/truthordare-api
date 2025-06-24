from fastapi import FastAPI

from src.core.category.admin import CategoryAdmin
from src.core.language.admin import LanguageAdmin
from src.db.engine import engine
from src.truth.api.rest import router as truth_router
from src.dare.api.rest import router as dare_router
import src.core.logging_setup
from src.core.logging_setup import setup_fastapi_logging

app = FastAPI(title="TruthOrDare API")
setup_fastapi_logging(app)

app.include_router(truth_router, tags=["Truth"], prefix="/api/truth")
app.include_router(dare_router, tags=["Dare"], prefix="/api/dare")

from sqladmin import Admin
from src.core.admin import authentication_backend
from src.truth.api.admin import TruthAdmin
from src.dare.api.admin import DareAdmin

admin = Admin(app, engine=engine, authentication_backend=authentication_backend)
admin.add_view(TruthAdmin)
admin.add_view(DareAdmin)
admin.add_view(LanguageAdmin)
admin.add_view(CategoryAdmin)
