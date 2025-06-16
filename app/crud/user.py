from sqlalchemy.orm import Session
from app.models.model_user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_all_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        full_name=user.full_name,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, updated_data: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    for field, value in updated_data.model_dump(exclude_unset=True).items():
        if field == "password":
            value = get_password_hash(value)
            setattr(user, "hashed_password", value)
        else:
            setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return False

    db.delete(user)
    db.commit()
    return True
