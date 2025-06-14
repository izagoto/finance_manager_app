from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class InvestmentType(str, Enum):
    stock = "stock"
    crypto = "crypto"
    property = "property"
    other = "other"

class InvestmentBase(BaseModel):
    name: str
    amount: float
    type: InvestmentType

class InvestmentCreate(InvestmentBase):
    pass

class InvestmentOut(InvestmentBase):
    id: int
    timestamp: datetime
    user_id: int

    class Config:
        orm_mode = True