from src.adapters.ports.infrastructures.postgresql.i_postgresql_connection_pool import (
    IPostgresqlConnectionPool,
)
from src.adapters.ports.infrastructures.postgresql.i_postgresql_infrastructure import (
    IPostgresqlInfrastructure,
)
from src.externals.infrastructures.postgre_sql.postgresql_connection_pool import (
    PostgresqlConnectionPool,
)


class PostgresqlInfrastructure(IPostgresqlInfrastructure):
    def get_pool(self, uri: str, database: str) -> IPostgresqlConnectionPool:
        return PostgresqlConnectionPool(database=database, uri=uri)
