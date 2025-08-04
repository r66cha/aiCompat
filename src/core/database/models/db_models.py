"""Database models module"""

# -- Imports


from sqlalchemy import Integer, String, Enum as SqlEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from src.core.database.mixin.mx import IdIntPkMixin
from src.core.schemas.user import PydanticJsonType, UserDescription, Gender, Zodiacs
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

# --


class Base(DeclarativeBase):
    pass


class User(Base, IdIntPkMixin):
    """User database model"""

    __tablename__ = "users"

    auth_id: Mapped[int] = mapped_column(Integer, nullable=False)

    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    gender: Mapped[str] = mapped_column(SqlEnum(Gender), nullable=False)
    zodiac: Mapped[str] = mapped_column(SqlEnum(Zodiacs), nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=True)
    weight: Mapped[int] = mapped_column(Integer, nullable=True)
    description: Mapped[UserDescription] = mapped_column(
        JSONB,
        nullable=True,
    )
    profile_photo_url: Mapped[str] = mapped_column(String, nullable=True)
    contacts: Mapped[str] = mapped_column(String, nullable=True)

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        """Returns an instance of UserDatabaseClass."""
