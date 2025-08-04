"""FastStreamConfigSchema schema."""

# -- Imports

from pydantic import BaseModel, RedisDsn
from src.core.schemas.log import LOG_DEFAULT_FORMAT

# --


class FastStreamConfigSchema(BaseModel):
    redis_url: RedisDsn = f"redis://localhost:6379"
    log_format: str = LOG_DEFAULT_FORMAT
