from enum import StrEnum
from pathlib import Path

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
    ENVIRONMENT: EnvironmentType = EnvironmentType.DEVELOPMENT

    # Database Configuration
    POSTGRES_DB: str = "postgres_db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

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
