from enum import StrEnum
from pathlib import Path
from typing import List

from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_PATH = Path(__file__).parent.parent.parent
ENV_FILE = BASE_PATH / ".env"

if not ENV_FILE.exists():
    raise FileNotFoundError(f"Environment file not found at {ENV_FILE}")


class EnvironmentType(StrEnum):
    STAGING = "staging"
    TESTING = "testing"
    PRODUCTION = "production"
    DEVELOPMENT = "development"


class Config(BaseSettings):
    # App Configuration
    PORT: int = 8000
    HOST: str = "localhost"
    ENVIRONMENT: EnvironmentType = EnvironmentType.DEVELOPMENT

    # Database Configuration
    POSTGRES_DB: str = "postgres_db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    # JWT Configuration
    JWT_PRIVATE_KEY_PATH: str = "keys/private.example.pem"
    JWT_PUBLIC_KEY_PATH: str = "keys/public.example.pem"
    JWT_ALGORITHM: str = "RS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS Configuration
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
    ]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
    CORS_ALLOW_HEADERS: List[str] = ["*"]

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+asyncpg",
                username=self.POSTGRES_USER,
                password=self.POSTGRES_PASSWORD,
                host=self.POSTGRES_HOST,
                port=self.POSTGRES_PORT,
                path=self.POSTGRES_DB,
            )
        )

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )


config = Config()
