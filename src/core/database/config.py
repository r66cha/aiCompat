"""
Configuration module for the database connection.

Defines a Pydantic settings class that constructs a full async SQLAlchemy-compatible database URL.
"""

# -- Imports

from pydantic_settings import BaseSettings, SettingsConfigDict


# --


class DB_URL(BaseSettings):
    """
    Pydantic settings class for configuring database connection parameters.\n
    Reads values from an environment file and builds a complete async database URL.
    """

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    dialect: str = "postgresql+asyncpg"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    @property
    def get_DB_URL(self) -> str:
        """Construct the full database connection URL string."""

        return f"{self.dialect}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


db_url = DB_URL()


__all__ = ["db_url"]
