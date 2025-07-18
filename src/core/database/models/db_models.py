from fastapi_users.db import SQLAlchemyBaseOAuthAccountTable, SQLAlchemyUserDatabase

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)

from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.mixin import IdIntPkMixin

# --

IntPK = Annotated[
    int,
    mapped_column(Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False),
]


# --


class Base(DeclarativeBase):
    pass


class User(Base, IdIntPkMixin, SQLAlchemyBaseAccessTokenTable[int]):

    __tablename__ = "users"

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[int]):

    __tablename__ = "accesstokens"

    user_id: IntPK

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
