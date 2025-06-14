from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")


class ResponseSchema(BaseModel, Generic[T]):
    status: int
    message: str
    data: Optional[T] = None

    model_config = {"from_attributes": True}
