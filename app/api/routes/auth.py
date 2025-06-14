from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verify_password, create_access_token
from app.crud import crud_user
from app.api.deps import get_db
from app.models.user import User
from jose import jwt, JWTError
from app.core.config import settings
from app.api.deps import get_current_user

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        user = crud_user.get_user_by_username(db, form_data.username)

        if not user or not verify_password(form_data.password, user.hashed_password):
            return {
                "status": 400,
                "message": "Invalid credentials",
                "data": None
            }

        if not user.is_active:
            return {
                "status": 403,
                "message": "Account is inactive. Please contact administrator.",
                "data": None
            }

        token = create_access_token({"sub": user.username})

        return {
            "status": 200,
            "message": "Login successful",
            "data": {
                "access_token": token,
                "token_type": "bearer"
            }
        }

    except Exception as e:
        return {
            "status": 500,
            "message": f"Internal Server Error: {str(e)}",
            "data": None
        }

@router.get("/me")
def read_users_me(current_user: User = Depends(get_current_user)):
    return {
        "status": 200,
        "message": "User info",
        "data": [{
            "id": current_user.id,
            "username": current_user.username,
            "email": current_user.email,
            "is_active": current_user.is_active,
            "is_admin": current_user.is_admin
        }]
    }
