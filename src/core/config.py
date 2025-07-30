"""Application configuration module."""

# -- Imports

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.core.schemas import (
    DatabaseConfigSchema,
    ApiSchema,
    LoggingConfigSchema,
    RunConfigSchema,
    GunicornConfigSchema,
    AccessTokenSchema,
)


# --


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """Main application settings."""

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=(BASE_DIR / ".env"),
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )

    access_token: AccessTokenSchema = AccessTokenSchema()
    db: DatabaseConfigSchema = DatabaseConfigSchema()
    api: ApiSchema = ApiSchema()
    logging: LoggingConfigSchema = LoggingConfigSchema()
    run: RunConfigSchema = RunConfigSchema()
    gunicorn: GunicornConfigSchema = GunicornConfigSchema()


settings = Settings()

__all__ = ["settings"]
