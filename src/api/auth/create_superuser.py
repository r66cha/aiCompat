"""Superuser create module."""

# -- Imports


import asyncio
import contextlib
from os import getenv
from src.core.dependencies.auth_dep.user_db_dep import get_user_db
from src.core.dependencies.auth_dep.user_manager_dep import get_user_manager
from src.core.dependencies.auth_dep.user_manager_cls import UserManager
from src.core.database.models.auth import User
from src.core.database.db_manager import db_auth_manager
from src.core.schemas.user_auth import UserCreate


# --

get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

default_email = getenv("DEFAULT_EMAIL", "admin@admin.com")
default_password = getenv("DEFAULT_PASSWORD", "password")


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(
    email: str = default_email,
    password: str = default_password,
    is_active: bool = True,
    is_superuser: bool = True,
    is_verified: bool = True,
):
    """Create superuser (admin) func"""

    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )

    async with db_auth_manager.get_session() as session:
        async with get_user_db_context(session) as user_db:
            async with get_user_manager_context(user_db) as user_manager:
                return await create_user(
                    user_manager=user_manager,
                    user_create=user_create,
                )


if __name__ == "__main__":
    asyncio.run(create_superuser())
