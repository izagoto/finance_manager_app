from app.api.routes.auth_routes import router as auth_router
from app.api.routes.user_routes import router as user_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(auth_router, prefix="/api", tags=["Authentication"])
router.include_router(user_router, prefix="/api", tags=["User Management"])
