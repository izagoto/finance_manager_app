from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.crud import crud_user
from app.api.deps import get_db

router = APIRouter()

@router.post("/create-users/")
def create_user(username: str = Body(...), email: str = Body(...), password: str = Body(...), is_active: bool = Body(default=True), is_admin: bool = Body(default=False), db: Session = Depends(get_db)):
    try:
        user_data = {
            "username": username,
            "email": email,
            "password": password,
            "is_active": is_active,
            "is_admin": is_admin
        }

        created_user = crud_user.create_user(db, user_data)
        return {
            "status": 200,
            "message": "User created successfully",
            "data": [{
                "id": created_user.id,
                "username": created_user.username,
                "email": created_user.email,
                "is_active": created_user.is_active,
                "is_admin": created_user.is_admin
            }]
        }
    except Exception as e:
        return {"status": 500, "message": f"Internal Server Error: {str(e)}", "data": None}

@router.get("/get-all-users/")
def get_users(db: Session = Depends(get_db)):
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


@router.get("/get-users-by/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = crud_user.get_user_by_id(db, user_id)
        if not user:
            return {"status": 404, "message": "User not found", "data": None}
        return {
            "status": 200,
            "message": "Success",
            "data": [{
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "is_active": user.is_active,
                "is_admin": user.is_admin
            }]
        }
    except Exception as e:
        return {
            "status": 500,
            "message": f"Internal Server Error: {str(e)}",
            "data": None
        }


@router.put("/update-users/{user_id}")
def update_user(user_id: int, username: str = Body(None), email: str = Body(None), password: str = Body(None), is_active: bool = Body(None), is_admin: bool = Body(None), db: Session = Depends(get_db)):
    try:
        data = {
            "username": username,
            "email": email,
            "password": password,
            "is_active": is_active,
            "is_admin": is_admin
        }

        update_data = {k: v for k, v in data.items() if v is not None}

        updated_user = crud_user.update_user(db, user_id, update_data)
        if not updated_user:
            return {"status": 404, "message": "User not found", "data": None}

        return {
            "status": 200,
            "message": "User updated successfully",
            "data": [{
                "id": updated_user.id,
                "username": updated_user.username,
                "email": updated_user.email,
                "is_active": updated_user.is_active,
                "is_admin": updated_user.is_admin
            }]
        }

    except Exception as e:
        return {
            "status": 500,
            "message": f"Internal Server Error: {str(e)}",
            "data": None
        }

@router.delete("/delete-users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        deleted_user = crud_user.delete_user(db, user_id)
        if not deleted_user:
            return {"status": 404, "message": "User not found", "data": None}
        return {
            "status": 200,
            "message": "User deleted successfully",
            "data": [{
                "id": deleted_user.id,
                "username": deleted_user.username,
                "email": deleted_user.email,
                "is_active": deleted_user.is_active,
                "is_admin": deleted_user.is_admin
            }]
        }
    except Exception as e:
        return {
            "status": 500,
            "message": f"Internal Server Error: {str(e)}",
            "data": None
        }
