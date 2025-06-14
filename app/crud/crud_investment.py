from sqlalchemy.orm import Session
from app.models.investment import Investment
from app.schemas.investment import InvestmentCreate

def create_investment(db: Session, investment: InvestmentCreate, user_id: int):
    db_investment = Investment(**investment.dict(), user_id=user_id)
    db.add(db_investment)
    db.commit()
    db.refresh(db_investment)
    return db_investment


def get_investments(db: Session, user_id: int):
    return db.query(Investment).filter(Investment.user_id == user_id).all()