"""User Routers module."""

# -- Imports

import os
import jwt
import json
import logging
from fastapi import (
    APIRouter,
    status,
    Request,
    Response,
    UploadFile,
    HTTPException,
    Depends,
    Header,
    Body,
    Form,
    Cookie,
    File,
)
from src.core.schemas.user import (
    AgeEnum,
    UserDescription,
    Gender,
    Zodiacs,
    UserBaseData,
)
from typing import Annotated
from src.core.config import settings
from typing import TYPE_CHECKING, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.tasks.fs.broker.redis_broker import broker, user_info
from src.core.database.db_manager import db_api_manager
from src.core.database.crud.users import create_user
from src.core.settings.log_conf import log

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=settings.logging.log_level_value,
    format=settings.logging.log_format,
)


KEY_SECRET = settings.access_token.reset_password_token_secret
ALGORITHM = settings.access_token.algorithm

# if TYPE_CHECKING:
#     from fastapi import Request

# --

user_router = APIRouter(
    prefix=settings.api.user,
    tags=["User"],
)


# Set Base-Info router
@user_router.post(
    "/me/set-info",
    status_code=status.HTTP_201_CREATED,
    response_model=UserBaseData,
    name="set-info",
)
async def set_info_about_me(
    session: Annotated[AsyncSession, Depends(db_api_manager.get_session)],
    request: Request,
    name: Annotated[str, Form(...)],
    age: Annotated[AgeEnum, Form(...)],
    gender: Annotated[Gender, Form(...)],
    zodiac: Annotated[Zodiacs, Form(...)],
    height: Annotated[int, Form()] = None,
    weight: Annotated[int, Form()] = None,
    # access_token: Annotated[str | None, Cookie(alias="aiCompat-access-jwt")] = None,
):
    """Router for set-info data"""

    access_token = request.cookies.get("aiCompat-access-jwt")

    if access_token is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Access token not found",
        )

    try:
        payload: dict = jwt.decode(
            jwt=access_token,
            key=KEY_SECRET,
            algorithms=[ALGORITHM],
            audience="fastapi-users:auth",
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token",
        )

    auth_id = payload.get("sub")
    if auth_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload: missing user_auth_id",
        )

    log.info(f"user_auth_id: {auth_id}")

    data = {
        "auth_id": auth_id,
        "name": name,
        "age": age.value,
        "gender": gender.value,
        "zodiac": zodiac.value,
        "height": height,
        "weight": weight,
    }

    user_base_data = UserBaseData(**data)

    print(user_base_data)

    await create_user(
        session=session,
        user_base_data=user_base_data,
    )

    await broker.publish(
        channel=f"users.{name}.info",
        message=name,
    )

    return data


# Set Description router
@user_router.post(
    "/me/set-description",
    status_code=status.HTTP_201_CREATED,
    name="set-description",
)
async def set_info_about_me(
    description: UserDescription,
    request: Request,
    cookie: Annotated[str, Cookie()] = None,
):
    """Router for set-description data"""

    print(f"description: {description}\n")

    return {"msg": "Data accepted"}


# Set Profile photo router
@user_router.post(
    "/me/set-photo",
    status_code=status.HTTP_201_CREATED,
    name="set-photo",
)
async def set_info_about_me(
    request: Request,
    cookie: str = Cookie(default=None),
    profile_photo: UploadFile = File(default=None),
):
    """Router for set-photo data"""

    return {"msg": "Data accepted"}


# Set contacts router
@user_router.post(
    "/me/set-contacts",
    status_code=status.HTTP_201_CREATED,
    name="set-contacts",
)
async def set_info_about_me(
    request: Request,
    cookie: str = Cookie(default=None),
    contacts: str = Form(...),
):
    """Router for set-contacts data"""

    return {"msg": "Data accepted"}


@user_router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    name="get-me",
)
async def get_info_about_me(
    request: Request,
    cookie: Annotated[str, Cookie()] = None,
):
    """Return info about user"""


@user_router.get(
    "compat/user/{user_id}",
    status_code=status.HTTP_200_OK,
    name="get-compat",
)
async def get_info_about_compatibility(
    request: Request,
    user_id: int,
    cookie: Annotated[str, Cookie()] = None,
):
    """Return percentage compatibility with other user."""


@user_router.patch(
    "/me/update",
    status_code=status.HTTP_200_OK,
    name="update-me",
)
async def update_info_about_me(
    request: Request,
    name: Annotated[str | None, Form()] = None,
    age: Annotated[AgeEnum | None, Form()] = None,
    gender: Annotated[Gender | None, Form()] = None,
    zodiac: Annotated[Zodiacs | None, Form()] = None,
    height: Annotated[int | None, Form()] = None,
    weight: Annotated[int | None, Form()] = None,
    cookie: Annotated[str, Cookie()] = None,
):
    """Partial update for user info"""

    return {"msg": "Fields updated"}


@user_router.put(
    "/me/full-update",
    status_code=status.HTTP_200_OK,
    name="full-update-me",
)
async def update_info_about_me(
    request: Request,
    description: UserBaseData,
    cookie: Annotated[str, Cookie()] = None,
):
    """Full update for user info"""

    return {"msg": "Description updated"}


@user_router.delete(
    "/me/photo",
    status_code=status.HTTP_200_OK,
    name="delete-profile-photo",
)
async def delete_profile_photo(
    request: Request,
    cookie: Annotated[str, Cookie()] = None,
):
    """Delete user profile photo"""

    return {"msg": "User profile photo deleted"}


@user_router.delete(
    "/me/profile",
    status_code=status.HTTP_200_OK,
    name="delete-me-profile",
)
async def delete_user(
    request: Request,
    cookie: Annotated[str, Cookie()] = None,
):
    """Delete user account"""

    return {"msg": "User deleted"}


# --


# === FastAPI источники данных и зависимости ===

# | Источник данных           | Зависимость FastAPI     | Пример использования                    |
# |---------------------------|--------------------------|------------------------------------------|
# | JSON body                 | Body(...)                | user: User = Body(...)                   |
# | HTML-форма или curl -F    | Form(...)                | name: str = Form(...)                    |
# | Файл                      | File(...)                | file: UploadFile = File(...)             |
# | Query-параметры URL       | Query(...)               | page: int = Query(1)                     |
# | Заголовки (headers)       | Header(...)              | token: str = Header(...)                 |
# | Cookie                    | Cookie(...)              | session_id: str = Cookie(...)            |
# | Параметры пути (path)     | Path(...)                | item_id: int = Path(...)                 |

# Пример:
# curl -X POST http://localhost/api/user \
#      -F "name=Ruslan" -F "file=@photo.png"

# FastAPI endpoint:
# async def upload_user(name: str = Form(...), file: UploadFile = File(...))


# --


# {
#   "hobbies": [
#     "Coding", "Training", "StartApp's", "PS", "Gaming", "Building"
#   ],
#   "profession": "Architect and IT Engenier",
#   "bio": "I burn in Vladicaucas, living in Moscow now and try working and do some startups",
#   "goals": "make a more mooney and build a couple of houses at the different place in the World",
#   "preferences": "I seek like-minded people for change the world make mooney and do interesting things"
# }
