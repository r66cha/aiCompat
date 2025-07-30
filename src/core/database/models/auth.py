"""
Database models for user and access token management using FastAPI Users.

This module defines the ORM models required for authentication and user handling:
- `Base`: Declarative base for all ORM models.
- `User`: Model for storing user data.
- `AccessToken`: Model for storing access tokens (used in DB strategy).
"""

# -- Imports

from datetime import datetime
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from fastapi_users_db_sqlalchemy.generics import TIMESTAMPAware
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from typing import TYPE_CHECKING
from src.core.database.mixin.mx import IdIntPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


# --


class Base(DeclarativeBase):
    """The basic declarative class for all ORM models of the project."""

    pass


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    """User database model."""

    __tablename__ = "users"

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        """Returns an instance of SQLAlchemyUserDatabase for working with the user's model."""

        return SQLAlchemyUserDatabase(session, cls)


class RefreshToken(Base):
    """Refresh tokens model"""

    __tablename__ = "refresh_tokens"

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="cascade",
        ),
    )
    expires_at: Mapped[datetime] = mapped_column(
        TIMESTAMPAware(timezone=True), nullable=False
    )
