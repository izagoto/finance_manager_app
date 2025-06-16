from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    SECRET_KEY: str = "supersecretkeythatyouknowforsure"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    PRODUCTION: bool = False

    BASE_DIR: Path
    DB_PATH: Path | None = None
    DATABASE_URL: str = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.BASE_DIR:
            raise ValueError("BASE_DIR tidak ditemukan di .env")

        if not self.DB_PATH:
            self.DB_PATH = self.BASE_DIR / "finance.db"

        if not self.DATABASE_URL:
            self.DATABASE_URL = f"sqlite:///{self.DB_PATH}"

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
