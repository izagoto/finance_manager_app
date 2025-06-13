from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    amount: float
    type: str
    category: Optional[str]
    description: Optional[str]

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class TransactionInDB(TransactionBase):
    id: int
    date: datetime
    user_id: int

    class Config:
        orm_mode = True
