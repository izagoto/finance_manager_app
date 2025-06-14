from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"

class TransactionBase(BaseModel):
    amount: float
    type: TransactionType
    description: Optional[str] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    id: int
    timestamp: datetime
    user_id: int

    class Config:
        orm_mode = True