"""Schema defining configuration settings for access tokens."""

# -- Imports

import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# --

RESET_SECRET = os.getenv("RESET_PASSWORD_TOKEN_SECRET")
VERIFY_TOKEN_SECRET = os.getenv("VERIFICATION_TOKEN_SECRET")
ALGORITHM = os.getenv("ALGORITHM")


class AccessTokenSchema(BaseModel):
    lifetime_second: int = 3600
    reset_password_token_secret: str = RESET_SECRET
    verification_token_secret: str = VERIFY_TOKEN_SECRET
    algorithm: str = ALGORITHM
