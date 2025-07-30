"""Application entry point for development using Uvicorn."""

# -- Imports

import uvicorn
from src.core.config import settings

# --

# Entry point
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
