"""Dependency that returns a configured JWTStrategy instance."""

# -- Imports

from src.core.config import settings
from fastapi_users.authentication import JWTStrategy

# --


# JWT access token strategy (tokens stored in memory, no DB)
def get_jwt_strategy() -> JWTStrategy:
    """
    Returns a configured JWT strategy for access token authentication.

    Returns:
        JWTStrategy instance.
    """

    return JWTStrategy(
        secret=settings.access_token.reset_password_token_secret,
        lifetime_seconds=settings.access_token.lifetime_second,
    )
