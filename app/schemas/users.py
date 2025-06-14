from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    username: str
    full_name: str
    email: str
    is_active: bool
    is_admin: bool

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    full_name: str
    email: str
    password: str
    is_active: bool = True
    is_admin: bool = False


class UserUpdate(BaseModel):
    full_name: str | None = None
    email: str | None = None
    password: str | None = None
    is_active: bool | None = None
    is_admin: bool | None = None
