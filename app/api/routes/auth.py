from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.models import models
from app.deps import get_db
from app.schemas.auth import LoginSchema, Token
from app.schemas.users import UserOut, UserCreate, UserUpdate
from app.schemas.response import ResponseSchema
from app.core.security import verify_password, create_access_token, get_password_hash


router = APIRouter()


@router.post("/login", response_model=ResponseSchema[Token])
def login(form_data: LoginSchema, db: Session = Depends(get_db)):
    try:
        user = (
            db.query(models.User).filter(models.User.email == form_data.email).first()
        )
        if not user or not verify_password(form_data.password, user.hashed_password):
            return ResponseSchema(
                status=404, message="Invalid email or password", data=None
            )
        token = create_access_token({"sub": user.email})
        return ResponseSchema(
            status=200,
            message="Login successful",
            data={"access_token": token, "token_type": "bearer"},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Login failed: {e}")
