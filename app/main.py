from fastapi import FastAPI
from app.db.session import engine, Base
from app.models import user, transaction, investment

def create_tables():
    Base.metadata.create_all(bind=engine)

def create_app() -> FastAPI:
    app = FastAPI(title="Finance Manager API")

    # Buat tabel saat aplikasi dimulai
    @app.on_event("startup")
    def startup_event():
        create_tables()

    @app.get("/")
    def read_root():
        return {"message": "Finance Manager API is running"}

    return app

app = create_app()
