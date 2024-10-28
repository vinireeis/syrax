from src.domain.exceptions.track_base_exception import TrackBaseException
from src.externals.infrastructures.postgre_sql.exceptions.postgresql_infrastructure_exceptions_reasons_enum import (
    PostgresqlInfrastructureExceptionsReasonsEnum,
)


class PostgresqlBaseInfrastructureException(TrackBaseException):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum
