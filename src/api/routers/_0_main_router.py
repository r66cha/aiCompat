"""Main app router"""

# -- Imports

from fastapi import APIRouter, Depends
from src.api.routers.user_router import user_router
from src.api.routers.auth_jwt_cookie import auth_jwt_cookie_router
from src.core.config import settings

# --

main_router = APIRouter(prefix=settings.api.prefix)
main_router.include_router(auth_jwt_cookie_router)
main_router.include_router(user_router)
