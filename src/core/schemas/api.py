"""Schema configuration for constructing API endpoint paths."""

# -- Imports

from pydantic import BaseModel


# --


class ApiSchema(BaseModel):
    """Configuration schema for base API endpoints."""

    prefix: str = "/api"
    user: str = "/user"
    set_data: str = "/set-data"

    auth_jwt_cookie: str = "/auth/jwt/cookie"

    users: str = "/users"

    @property
    def set_data_url(self) -> str:
        """Full path for set data route."""

        return f"{self.prefix}{self.user}{self.set_data}"
