"""FastStream app instance."""

# -- Imports

import logging
from faststream import FastStream
from src.core.tasks.fs.broker.redis_broker import broker
from src.core.tasks.fs.routers.users import router
from src.core.config import settings

# --

app = FastStream(broker=broker)

broker.include_router(router=router)


@app.after_startup
async def conf_logging():
    logging.basicConfig(
        level=settings.logging.log_level_value,
        format=settings.logging.log_format,
    )
