from contextlib import asynccontextmanager
from typing import AsyncIterator


from psycopg import (
    AsyncConnection,
    InterfaceError,
    DatabaseError,
)
from psycopg.errors import ConnectionTimeout
from psycopg_pool import AsyncConnectionPool

from src.adapters.ports.infrastructures.postgresql.i_postgresql_connection_pool import (
    IPostgresqlConnectionPool,
)
from src.externals.infrastructures.postgre_sql.exceptions.postgresql_infrastructure_excepetions import (
    PostgresqlInfrastructureUnexpectedErrorException,
    PostgresqlInfrastructureInterfaceErrorException,
    PostgresqlInfrastructureDatabaseErrorException,
    PostgresqlInfrastructureConnectionTimeoutException,
)


class PostgresqlConnectionPool(IPostgresqlConnectionPool):
    def __init__(self, uri: str, database: str):
        self.__uri = uri
        self.__database = database

    @asynccontextmanager
    async def get_connection(self) -> AsyncIterator[AsyncConnection]:
        try:
            connection_info = f"{self.__uri}/{self.__database}"

            async with AsyncConnectionPool(
                conninfo=connection_info
            ) as connection_pool, connection_pool.connection() as connection:
                yield connection

        except InterfaceError as original_exception:
            raise PostgresqlInfrastructureInterfaceErrorException(
                message="Postgresql interface error.",
                original_error=original_exception,
            ) from original_exception

        except DatabaseError as original_exception:
            raise PostgresqlInfrastructureDatabaseErrorException(
                message="Postgresql database error.",
                original_error=original_exception,
            ) from original_exception

        except ConnectionTimeout as original_exception:
            raise PostgresqlInfrastructureConnectionTimeoutException(
                message="Postgresql connection timeout.",
                original_error=original_exception,
            ) from original_exception

        except Exception as original_exception:
            raise PostgresqlInfrastructureUnexpectedErrorException(
                message="Unexpected Postgresql error.",
                original_error=original_exception,
            ) from original_exception
