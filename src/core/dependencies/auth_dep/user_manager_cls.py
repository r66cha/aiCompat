"""
Custom user manager using FastAPI Users.

This module defines a user manager that handles user-related events such as:
- Registration
- Email verification
- Password reset

It uses secrets from the application settings for token generation.
"""

# -- Imports

from typing import Optional, TYPE_CHECKING
from fastapi_users import BaseUserManager, IntegerIDMixin
from src.core.database.models.auth import User
from src.core.settings.log_conf import log
from src.core.config import settings

if TYPE_CHECKING:
    from fastapi import Request


# --


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        "Called after a user is successfully registered."

        log.warning(f"User: {user.id} was registered")

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        "Called after a user requests email verification."

        log.warning(f"Verification request from:\n\tUser: {user.id}\n\tToken: {token}")

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        "Called after a user initiates a password reset."

        log.warning(f"User {user.id} has forgot their password. Reset token: {token}")
