import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List
import json

load_dotenv()


def parse_allowed_origins(env_value: str) -> List[str]:
    try:
        # Coba parse string JSON list
        return json.loads(env_value)
    except Exception:
        # Jika bukan format list, coba split koma
        return [origin.strip() for origin in env_value.split(",") if origin.strip()]


class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkeythatyouknowforsure")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
    SQLITE_DB: str = os.getenv("SQLITE_DB", "sqlite:///./finance.db")

    ALLOWED_ORIGINS: List[str] = Field(
        default_factory=lambda: parse_allowed_origins(os.getenv("ALLOWED_ORIGINS", ""))
    )

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
