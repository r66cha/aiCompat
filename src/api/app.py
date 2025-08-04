"""FastAPI application instance."""

# -- Imports

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.middleware.base_mdw import CustomHeaderMiddleware
from .description import title, description, version
from src.api.routers._0_main_router import main_router
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi.responses import ORJSONResponse

from src.core.tasks.fs.broker.redis_broker import broker
from src.core.database.db_manager import db_api_manager, db_auth_manager

# from src.core.models import db_helper

log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    log.info("Starting FastStream broker and DB connection")
    await broker.start()
    yield
    log.info("Stopping DB connection and FastStream broker")
    await db_api_manager.dispose()
    await db_auth_manager.dispose()
    await broker.stop()


def create_app() -> FastAPI:
    app = FastAPI(
        title=title,
        description=description,
        version=version,
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Routers
    app.include_router(main_router)

    # Middleware
    app.add_middleware(
        middleware_class=CORSMiddleware,
        allow_origins=["*"],
    )

    app.add_middleware(middleware_class=CustomHeaderMiddleware)

    return app


app = create_app()
