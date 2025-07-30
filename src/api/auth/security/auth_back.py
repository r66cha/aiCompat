"""Authentication backend setup using FastAPI Users."""

# -- Imports

from fastapi_users.authentication import AuthenticationBackend
from src.api.auth.security.transport import cookie_transport
from src.core.dependencies.auth_dep.token_strategy_jwt_dep import get_jwt_strategy

# --

# JWT strategy + cookie
authentication_backend_jwt_cookie = AuthenticationBackend(
    name="aiCompat-access-jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
