from sqlalchemy.orm import Session
from app.models.investment import Investment
from app.schemas.investment import InvestmentCreate, InvestmentUpdate

def create_investment(db: Session, investment: InvestmentCreate, user_id: int):
    db_investment = Investment(**investment.dict(), user_id=user_id)
    db.add(db_investment)
    db.commit()
    db.refresh(db_investment)
    return db_investment

def get_investments(db: Session, user_id: int):
    return db.query(Investment).filter(Investment.user_id == user_id).all()

def get_investment(db: Session, investment_id: int):
    return db.query(Investment).filter(Investment.id == investment_id).first()

def update_investment(db: Session, db_obj: Investment, update_data: InvestmentUpdate):
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_investment(db: Session, db_obj: Investment):
    db.delete(db_obj)
    db.commit()
