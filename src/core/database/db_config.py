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

    # -- Auth

    DB_HOST_AUTH: str
    DB_PORT_AUTH: int
    DB_USER_AUTH: str
    DB_PASSWORD_AUTH: str
    DB_NAME_AUTH: str

    # -- API

    DB_HOST_API: str
    DB_PORT_API_LOCAL: int
    DB_USER_API: str
    DB_PASSWORD_API: str
    DB_NAME_API: str

    # --

    dialect: str = "postgresql+asyncpg"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    @property
    def get_DB_URL_AUTH(self) -> str:
        """Construct the full database connection URL string."""

        return f"{self.dialect}://{self.DB_USER_AUTH}:{"pass"}@{self.DB_HOST_AUTH}:{self.DB_PORT_AUTH}/{self.DB_NAME_AUTH}"

    @property
    def get_DB_URL_API(self) -> str:
        """Construct the full database connection URL string."""

        return f"{self.dialect}://{self.DB_USER_API}:{self.DB_PASSWORD_API}@{self.DB_HOST_API}:{self.DB_PORT_API_LOCAL}/{self.DB_NAME_API}"


db_url = DB_URL()


__all__ = ["db_url"]
