"""Configuration schemas for application runtime and Gunicorn server."""

# -- Imports

from pydantic import BaseModel

# --


class RunConfigSchema(BaseModel):
    """Configuration for running the application."""

    host: str = "0.0.0.0"
    port: int = 8000


class GunicornConfigSchema(BaseModel):
    """Configuration for Gunicorn server."""

    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 1
    timeout: int = 900
