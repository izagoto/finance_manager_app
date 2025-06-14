from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.transaction import TransactionCreate, TransactionOut
from app.crud import crud_transaction
from app.api.deps import get_db, get_current_user
from app.models.user import User
from typing import List

router = APIRouter()

@router.post("/", response_model=TransactionOut)
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_transaction.create_transaction(db, transaction, current_user.id)

@router.get("/", response_model=List[TransactionOut])
def get_transactions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_transaction.get_transactions(db, current_user.id)
