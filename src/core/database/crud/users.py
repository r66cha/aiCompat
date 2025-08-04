"""CRUD module"""

# ---

from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database.models.db_models import User
from src.core.schemas.user import UserBaseData

# --


async def get_user(
    session: AsyncSession,
    user_id: int,
) -> User | None:
    return await session.get(User, user_id)


async def create_user(
    session: AsyncSession,
    user_base_data: UserBaseData,
) -> User:
    user = User(**user_base_data.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
