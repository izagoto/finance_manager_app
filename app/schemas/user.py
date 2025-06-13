from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    is_active: Optional[bool]
    is_admin: Optional[bool]

class UserInDB(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True
