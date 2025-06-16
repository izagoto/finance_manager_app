import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if settings.DATABASE_URL.startswith("sqlite"):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

connect_args = (
    {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}
)
engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    try:
        from app.models.model_user import Base as ModelBase

        Base.metadata.create_all(bind=engine)
        ModelBase.metadata.create_all(bind=engine)

        logger.info("Database berhasil diinisialisasi.")
    except Exception as e:
        logger.error(f"Gagal menginisialisasi database: {e}")
        raise
