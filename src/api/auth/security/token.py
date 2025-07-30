"""Access (for refresh) Token generate module."""

# -- Imports

from fastapi_users.authentication import JWTStrategy
from src.core.database.models.auth import User
from src.core.config import settings

# --


async def create_access_token(user: User) -> str:
    """Access-token func."""

    strategy = JWTStrategy(
        secret=settings.access_token.reset_password_token_secret,
        lifetime_seconds=settings.access_token.lifetime_second,
    )

    return await strategy.write_token(user=user)
