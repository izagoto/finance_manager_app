from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict
from dotenv import load_dotenv

load_dotenv()


class UserRole(str, Enum):
    admin = "admin"
    user = "user"


class UserBase(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    role: UserRole


class UserCreate(UserBase):
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    full_name: str
    email: EmailStr
    role: UserRole
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    username: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None


class Token(BaseModel):
    access_token: str
    token_type: str
