"""Dependency module for providing a user database adapter."""

# -- Imports

from fastapi import Depends
from typing import TYPE_CHECKING, Annotated
from src.core.database.db_manager import db_auth_manager
from src.core.database.models.auth import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


# --


async def get_user_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_auth_manager.get_session),
    ],
):
    """
    Dependency that provides the user database adapter.

    Args:
        session (AsyncSession): Asynchronous SQLAlchemy session.

    Yields:
        SQLAlchemyUserDatabase: User repository for performing operations
        on the user table.
    """

    yield User.get_db(session=session)
