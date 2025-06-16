from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import get_db
from app.crud import user as crud_user
from app.schemas.response import ResponseSchema
import traceback
from app.schemas.user import UserCreate, UserUpdate, UserOut


router = APIRouter()


@router.post("/create-user", response_model=ResponseSchema)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = crud_user.get_user_by_username(db, user.username)
        if db_user:
            return {
                "status": 400,
                "message": "Username already registered",
                "data": None,
            }

        created_user = crud_user.create_user(db, user)

        if not created_user:
            return {
                "status": 404,
                "message": "Failed to create user",
                "data": None,
            }

        user_out = UserOut.model_validate(created_user).model_dump()

        return {
            "status": 200,
            "message": "User registered successfully",
            "data": [user_out],
        }

    except SQLAlchemyError as e:
        print(f"SQLAlchemy error: {e}")
        return {
            "status": 500,
            "message": "Internal server error",
            "data": None,
        }

    except Exception as e:
        print(f"Unhandled error: {e}")
        return {
            "status": 500,
            "message": "Unexpected server error",
            "data": None,
        }


@router.get("/get-users", response_model=ResponseSchema)
def get_all_users(db: Session = Depends(get_db)):
    try:
        users = crud_user.get_all_users(db)

        if isinstance(users, list) and len(users) == 0:
            return {
                "status": 404,
                "message": "Users not found",
                "data": [],
            }

        return {
            "status": 200,
            "message": "All users fetched successfully",
            "data": users,
        }

    except SQLAlchemyError as e:
        print(f"SQLAlchemy error: {e}")
        traceback.print_exc()
        return {
            "status": 500,
            "message": "Internal server error",
            "data": None,
        }

    except ValueError as e:
        return {"status": 400, "message": f"Bad Request: {str(e)}", "data": None}


@router.put("/update-users/{user_id}", response_model=ResponseSchema)
def update_user(user_id: int, updated_data: UserUpdate, db: Session = Depends(get_db)):
    try:
        user = crud_user.update_user(db, user_id, updated_data)

        if not user:
            return {
                "status": 404,
                "message": f"User with id {user_id} not found",
                "data": None,
            }

        user_out = UserOut.model_validate(user).model_dump()

        return {
            "status": 200,
            "message": f"User with id {user_id} updated successfully",
            "data": [user_out],
        }

    except SQLAlchemyError as e:
        print(f"SQLAlchemy error: {e}")
        return {
            "status": 500,
            "message": "Internal server error",
            "data": None,
        }


@router.delete("/delete-users/{user_id}", response_model=ResponseSchema)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        deleted = crud_user.delete_user(db, user_id)
        if not deleted:
            return {
                "status": 404,
                "message": f"User with id {user_id} not found",
            }

        return {
            "status": 200,
            "message": f"User with id {user_id} deleted successfully",
        }

    except SQLAlchemyError as e:
        print(f"SQLAlchemy error: {e}")
        return {
            "status": 500,
            "message": "Internal server error",
        }
