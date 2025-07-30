"""User-related Pydantic schemas for API input/output serialization."""

# -- Imports

from fastapi_users import schemas
from pydantic import BaseModel


# --


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class UserRegistrationNotification(BaseModel):
    user: UserRead
    time_second: int
