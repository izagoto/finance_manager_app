from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.response import ResponseSchema
from app.schemas.user import Token
from app.db.database import get_db
from app.crud import user as crud_user
from app.core.security import (
    verify_password,
    create_access_token,
    decode_token,
    token_blacklist,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")


router = APIRouter()


@router.post("/login", response_model=Token)
def login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    try:
        db_user = crud_user.get_user_by_username(db, form_data.username)

        if not db_user:
            raise HTTPException(status_code=401, detail="Invalid username or password")

        hashed_password = getattr(db_user, "hashed_password", None)

        if not hashed_password or not verify_password(
            form_data.password, hashed_password
        ):
            raise HTTPException(status_code=401, detail="Invalid username or password")

        token = create_access_token(data={"sub": db_user.username})

        if request.headers.get("accept") == "application/json":
            return {
                "access_token": token,
                "token_type": "bearer",
            }

        return JSONResponse(
            status_code=200,
            content={
                "status": 200,
                "message": "Login successful",
                "data": {
                    "access_token": token,
                    "token_type": "bearer",
                },
            },
        )

    except Exception as e:
        print(f"Login error: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "message": "Internal server error",
                "data": None,
            },
        )


@router.get("/decode", response_model=ResponseSchema)
def decode_token_data(token: str = Depends(oauth2_scheme)):
    try:
        if token in token_blacklist:
            return JSONResponse(
                status_code=401,
                content={
                    "status": 401,
                    "message": "Token has been revoked",
                    "data": None,
                },
            )

        decoded = decode_token(token)
        if not decoded:
            return JSONResponse(
                status_code=400,
                content={
                    "status": 400,
                    "message": "Invalid token",
                    "data": None,
                },
            )

        return {
            "status": 200,
            "message": "Token decoded successfully",
            "data": decoded,
        }

    except Exception as e:
        print(f"Decode error: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "message": "Error decoding token",
                "data": None,
            },
        )


@router.post("/logout", response_model=ResponseSchema)
def logout_user(token: str = Depends(oauth2_scheme)):
    try:
        decoded = decode_token(token)
        if not decoded:
            return JSONResponse(
                status_code=400,
                content={
                    "status": 400,
                    "message": "Invalid token",
                    "data": None,
                },
            )

        token_blacklist.add(token)

        return {
            "status": 200,
            "message": "Logout successful",
            "data": None,
        }

    except Exception as e:
        print(f"Logout error: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "message": "Internal server error",
                "data": None,
            },
        )
