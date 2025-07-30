"""Configuration schemas for application runtime and Gunicorn server."""

# -- Imports

from pydantic import BaseModel

# --


class RunConfigSchema(BaseModel):
    """Configuration for running the application."""

    host: str = "0.0.0.0"
    port: int = 8001


class GunicornConfigSchema(BaseModel):
    """Configuration for Gunicorn server."""

    host: str = "0.0.0.0"
    port: int = 8001
    workers: int = 1
    timeout: int = 900
