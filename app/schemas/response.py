from pydantic import BaseModel
from typing import List, Optional, Union
from app.schemas.user import UserOut


class ResponseSchema(BaseModel):
    status: int
    message: str
    data: Optional[Union[List[UserOut], dict, None]] = None
