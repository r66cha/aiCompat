"""Redis-broker instance init."""

# -- Imports

from faststream.redis import RedisBroker
from src.core.config import settings

# --

broker = RedisBroker(settings.fstream.redis_url)

user_info = broker.publisher(
    "users.{user_name}.info",
)
