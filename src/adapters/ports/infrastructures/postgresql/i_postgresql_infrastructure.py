from abc import ABC, abstractmethod

from src.adapters.ports.infrastructures.postgresql.i_postgresql_connection_pool import (
    IPostgresqlConnectionPool,
)


class IPostgresqlInfrastructure(ABC):
    @abstractmethod
    def get_pool(self, uri: str, database: str) -> IPostgresqlConnectionPool:
        pass
