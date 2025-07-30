"""Dependency provider for the custom UserManager."""

# -- Import

from fastapi import Depends
from typing import Annotated, TYPE_CHECKING

from src.core.dependencies.auth_dep.user_manager_cls import UserManager
from src.core.dependencies.auth_dep.user_db_dep import get_user_db

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


# --


async def get_user_manager(
    user_db: Annotated[
        "SQLAlchemyUserDatabase",
        Depends(get_user_db),
    ],
):
    """Dependency that yields a custom UserManager instance.

    Args:
        user_db (SQLAlchemyUserDatabase): Database adapter for user table.

    Yields:
        UserManager: Instance of the custom UserManager.
    """

    yield UserManager(user_db=user_db)
