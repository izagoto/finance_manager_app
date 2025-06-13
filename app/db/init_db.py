from app.db.session import engine, Base
from app.models import user, transaction, investment

def init_db():
    Base.metadata.create_all(bind=engine)
