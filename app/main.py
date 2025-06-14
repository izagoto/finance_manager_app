from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import transactions, investments, users, exports

def create_app() -> FastAPI:
    app = FastAPI(
        title="Finance Manager API",
        version="1.0",
        description="API for managing personal finance including transactions, investments, and export features."
    )

    # CORS configuration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routers
    app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
    app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["Transactions"])
    app.include_router(investments.router, prefix="/api/v1/investments", tags=["Investments"])
    app.include_router(exports.router, prefix="/api/v1/exports", tags=["Exports"])

    return app

app = create_app()
