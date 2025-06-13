from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InvestmentBase(BaseModel):
    name: str
    amount: float
    return_rate: Optional[float] = 0.0

class InvestmentCreate(InvestmentBase):
    pass

class InvestmentUpdate(InvestmentBase):
    pass

class InvestmentInDB(InvestmentBase):
    id: int
    date: datetime
    user_id: int

    class Config:
        orm_mode = True
