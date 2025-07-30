"""
Custom Gunicorn application wrapper for running a FastAPI app.

Provides dynamic configuration of Gunicorn options such as host, port, workers, timeout, and logging level.
Enables running FastAPI with Uvicorn workers under Gunicorn.

- get_app_options: Returns Gunicorn configuration dictionary.
- Application: Subclass of Gunicorn's BaseApplication that loads FastAPI app and applies config options.
"""

# -- Imports

from fastapi import FastAPI
from gunicorn.app.base import BaseApplication


# --


def get_app_options(
    host: str,
    port: int,
    timeout: int,
    workers: int,
    log_level: str,
) -> dict:
    """Generate Gunicorn configuration options dictionary."""

    return {
        "accesslog": "-",
        "errorlog": "-",
        "bind": f"{host}:{port}",
        "loglevel": log_level,
        "timeout": timeout,
        "workers": workers,
        "worker_class": "uvicorn.workers.UvicornWorker",
    }


class Application(BaseApplication):
    """Gunicorn application wrapper to run FastAPI with custom configuration."""

    def __init__(
        self,
        application: FastAPI,
        options: dict | None = None,
    ):
        self.options = options or {}
        self.application = application
        super().__init__()

    def load(self):
        return self.application

    @property
    def config_options(self) -> dict:
        """Filter options to those valid in Gunicorn config settings."""

        return {
            # pair
            k: v
            # for each option
            for k, v in self.options.items()
            # not empty key / value
            if k in self.cfg.settings and v is not None
        }

    def load_config(self):
        """Set Gunicorn configuration using filtered options."""

        for key, value in self.config_options.items():
            self.cfg.set(key.lower(), value)
