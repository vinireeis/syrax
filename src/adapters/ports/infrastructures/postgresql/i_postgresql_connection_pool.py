from abc import ABC, abstractmethod
from typing import AsyncIterator

from psycopg import AsyncConnection


class IPostgresqlConnectionPool(ABC):
    @abstractmethod
    async def get_connection(self) -> AsyncIterator[AsyncConnection]:
        pass
