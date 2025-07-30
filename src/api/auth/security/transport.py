"""
Authentication transport configurations for FastAPI Users.

This module defines multiple transport mechanisms used for delivering authentication tokens:
- Bearer transport (header-based)
- Cookie transport (session-style, frontend friendly)
"""

# -- Imports

from fastapi_users.authentication import CookieTransport
from src.core.config import settings

# --

cookie_transport = CookieTransport(
    cookie_name="aiCompat-access-jwt",  # Name of the cookie
    cookie_max_age=settings.access_token.lifetime_second,  # Lifetime in seconds
    cookie_secure=False,  # Use True in production with HTTPS
    cookie_httponly=True,  # Prevent JS access to cookie
    cookie_samesite="lax",  # CSRF protection
)
