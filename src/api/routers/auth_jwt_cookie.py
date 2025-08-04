"""Authentication router with JWT + Cookie."""

# -- Imports

from fastapi import APIRouter
from src.api.auth._0_fastapi_users import (
    fastapi_users_jwt_strategy,
    authentication_backend_jwt_cookie,
)
from src.core.config import settings
from src.core.schemas.user_auth import UserRead, UserCreate

# --


# Router instance
auth_jwt_cookie_router = APIRouter(
    prefix=settings.api.auth_jwt_cookie,
    tags=["Auth-JWT-Cookie"],
)

# /register
auth_jwt_cookie_router.include_router(
    router=fastapi_users_jwt_strategy.get_register_router(
        user_schema=UserRead,
        user_create_schema=UserCreate,
    ),
)


# /login
# /logout
auth_jwt_cookie_router.include_router(
    router=fastapi_users_jwt_strategy.get_auth_router(
        backend=authentication_backend_jwt_cookie,
        # requires_verification=True,
    ),
)


# /request-verify-token
# /verify
auth_jwt_cookie_router.include_router(
    router=fastapi_users_jwt_strategy.get_verify_router(
        user_schema=UserRead,
    ),
)


# /forgot-password
# /reset-password
auth_jwt_cookie_router.include_router(
    router=fastapi_users_jwt_strategy.get_reset_password_router(),
)
