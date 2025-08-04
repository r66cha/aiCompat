"""Send welcome module."""

# --

from src.core.database.models.db_models import User
from src.core.services.mail.mailing import send_email

# --


async def send_welcome_email(user: User = None) -> None:
    await send_email(
        recipient="r66cha@gmail.com",
        subject="Welcome to our site!",
        body=f"Dear Ruslan,\n\nWelcome to our site!",
    )
