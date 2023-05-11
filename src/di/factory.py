import logging
from typing import Literal, Callable

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from settings.postgres import SettingsPostgres

logger = logging.getLogger(__name__)


class ConfigFactory:
    def __init__(self):
        self.postgres = SettingsPostgres()


class EngineFactory:
    ENGINE_TYPES: dict[Literal["sync", "async"], Callable] = {
        "sync": create_engine,
        "async": create_async_engine,
    }

    def __init__(
        self,
        config: SettingsPostgres,
        mode: Literal["sync", "async"],
    ):
        engine_builder = self.ENGINE_TYPES.get(mode)

        if mode == "async":
            self.engine = engine_builder(
                config.dsn(mode=mode),
                future=True,
                echo=True,
                connect_args={"timeout": 30},
                pool_size=6,
                max_overflow=2,
            )
        else:
            self.engine = engine_builder(
                config.dsn(mode=mode),
            )


class SessionFactory:
    def __init__(self, engine: AsyncEngine):
        self.session_factory = async_sessionmaker(
            engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )
