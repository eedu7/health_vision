from enum import StrEnum
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvironmentType(StrEnum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TESTING = "testing"


BASE_PATH = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_PATH / ".env"


class Config(BaseSettings):
    ENVIRONMENT: EnvironmentType = EnvironmentType.DEVELOPMENT

    model_config: SettingsConfigDict = SettingsConfigDict(env_file=ENV_FILE, env_file_encoding="utf-8", extra="ignore")


config: Config = Config()

print(config.ENVIRONMENT)
