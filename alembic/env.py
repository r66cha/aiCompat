from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from src.core.database.models.auth import Base as AuthBase
from src.core.database.models.db_models import Base as ApiBase

import os
from dotenv import load_dotenv

load_dotenv()

user_auth = os.getenv("DB_USER_AUTH")
password_auth = os.getenv("DB_PASSWORD_AUTH")
host_auth = os.getenv("DB_HOST_AUTH")
port_auth = os.getenv("DB_PORT_AUTH")
db_auth = os.getenv("DB_NAME_AUTH")

# --

user_api = os.getenv("DB_USER_API")
password_api = os.getenv("DB_PASSWORD_API")
host_api = os.getenv("DB_HOST_API")
port_api = os.getenv("DB_PORT_API_LOCAL")
db_api = os.getenv("DB_NAME_API")

# --

url_auth = f"postgresql+psycopg2://{user_auth}:{password_auth}@{host_auth}:{port_auth}/{db_auth}"
url_api = (
    f"postgresql+psycopg2://{user_api}:{password_api}@{host_api}:{port_api}/{db_api}"
)


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

config.set_main_option("sqlalchemy.url", url_api)


# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = ApiBase.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
