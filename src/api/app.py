"""FastAPI application instance."""

# -- Imports

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.middleware.base_mdw import CustomHeaderMiddleware
from .description import title, description, version
from src.api.routers._0_main_router import main_router

# --


# Application instance
app = FastAPI(
    title=title,
    description=description,
    version=version,
)

# Routers
app.include_router(main_router)


# Middleware
app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["*"],
)

app.add_middleware(middleware_class=CustomHeaderMiddleware)
