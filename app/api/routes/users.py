from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models import models
from app.deps import get_db
from app.schemas.users import UserOut, UserCreate, UserUpdate
from app.schemas.response import ResponseSchema
from app.core.security import get_password_hash


router = APIRouter()


@router.get("/get-users", response_model=ResponseSchema[List[UserOut]])
def get_users(db: Session = Depends(get_db)):
    try:
        users = db.query(models.User).all()
        if not users:
            return ResponseSchema(status=404, message="No users found", data=[])
        return ResponseSchema(
            status=200, message="Successfully retrieved users", data=users
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve users: {e}")


@router.post("/create-users", response_model=ResponseSchema[UserOut])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        existing_user = (
            db.query(models.User).filter(models.User.email == user.email).first()
        )
        if existing_user:
            return ResponseSchema(status=400, message="email already exists", data=None)
        db_user = models.User(
            username=user.username,
            full_name=user.full_name,
            email=user.email,
            hashed_password=get_password_hash(user.password),
            is_active=user.is_active,
            is_admin=user.is_admin,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return ResponseSchema(
            status=200, message="User created successfully", data=db_user
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create user: {e}")


@router.put("/update-users/{user_id}", response_model=ResponseSchema[UserOut])
def update_user(user_id: int, updates: UserUpdate, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            return ResponseSchema(status=404, message="User not found", data=None)

        if updates.full_name is not None:
            user.full_name = updates.full_name
        if updates.email is not None:
            user.email = updates.email
        if updates.password is not None:
            user.hashed_password = get_password_hash(updates.password)
        if updates.is_active is not None:
            user.is_active = updates.is_active
        if updates.is_admin is not None:
            user.is_admin = updates.is_admin

        db.commit()
        db.refresh(user)
        return ResponseSchema(
            status=200, message="User updated successfully", data=user
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update user: {e}")


@router.delete("/delete-users/{user_id}", response_model=ResponseSchema[dict])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            return ResponseSchema(status=404, message="User not found", data=None)
        db.delete(user)
        db.commit()
        return ResponseSchema(
            status=200,
            message="User deleted successfully",
            data={"deleted_user_id": user_id},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete user: {e}")
