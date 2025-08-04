"""User-Router instance and handlers."""

# -- Imports

from faststream.redis import RedisRouter
from src.core.settings.log_conf import log
from faststream import Depends, Path
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database.db_manager import db_api_manager
from src.core.services.mail.send_welcome_email import send_welcome_email as send_welcome


# --

router = RedisRouter()


@router.subscriber("users.{user_name}.info")
async def send_welcome_email(
    user_name: Annotated[str, Path()],
    session: Annotated[
        AsyncSession,
        Depends(db_api_manager.get_session),
    ],
) -> None:
    """
    DO:
     - Send Welcome email to user.
     - Write logs.
    """

    log.info(f"Welcome: {user_name}")

    await send_welcome()
