from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.routes.main_routes import router
from app.db.database import init_db
from fastapi.middleware.cors import CORSMiddleware

init_db()

app = FastAPI(
    title="Finance Managements APP",
    version="1.0",
    description="API untuk finance management app",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def home():
    print("Redirecting to /docs")
    return RedirectResponse(url="/docs")
