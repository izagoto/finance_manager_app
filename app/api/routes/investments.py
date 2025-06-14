from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.investment import InvestmentCreate, InvestmentOut
from app.crud import crud_investment
from app.api.deps import get_db, get_current_user
from app.models.user import User
from typing import List

router = APIRouter()

@router.post("/", response_model=InvestmentOut)
def create_investment(
    investment: InvestmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_investment.create_investment(db, investment, current_user.id)

@router.get("/", response_model=List[InvestmentOut])
def get_investments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_investment.get_investments(db, current_user.id)
