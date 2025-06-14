from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verify_password, create_access_token, decode_access_token
from app.crud import crud_user
from app.api.deps import get_db
from app.models.user import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = crud_user.get_user_by_username(db, username)
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except Exception:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    try:
        user = crud_user.get_user_by_username(db, username)

        if not user or not verify_password(password, user.hashed_password):
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
        return {"status": 500, "message": f"Internal Server Error: {str(e)}", "data": None}

@router.get("/get-all-users/")
def get_users(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin only")
    try:
        users = crud_user.get_all_users(db)
        return {
            "status": 200,
            "message": "Success",
            "data": [{
                "id": u.id,
                "username": u.username,
                "email": u.email,
                "is_active": u.is_active,
                "is_admin": u.is_admin
            } for u in users]
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
