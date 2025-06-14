from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.routes import auth
from app.models import models
from app.db import engine
from app.api.routes.main_routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Management App",
    description="API for personal finance management including income, expenses, investments, and more.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(router)


@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/docs")
