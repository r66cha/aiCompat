"""FastAPI Users core setup."""

# -- Imports

from fastapi_users import FastAPIUsers
from src.core.database.models.auth import User
from src.core.dependencies.auth_dep.user_manager_dep import get_user_manager
from src.api.auth.security.auth_back import (
    authentication_backend_jwt_cookie,
)


# --


# FastAPIUsers instance jwt and cookie
fastapi_users_jwt_strategy = FastAPIUsers[User, int](
    get_user_manager=get_user_manager,
    auth_backends=[
        authentication_backend_jwt_cookie,
    ],
)

# Dependencies for user access jwt
current_active_user_jwt = fastapi_users_jwt_strategy.current_user(active=True)
current_active_superuser_jwt = fastapi_users_jwt_strategy.current_user(
    active=True,
    superuser=True,
)
