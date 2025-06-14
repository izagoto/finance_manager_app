from app.api.routes.auth import router as auth_route
from app.api.routes.users import router as users_route
from fastapi import APIRouter

router = APIRouter()

router.include_router(auth_route, prefix="/api/auth", tags=["Authentication"])
router.include_router(users_route, prefix="/api/users", tags=["Data Users"])
