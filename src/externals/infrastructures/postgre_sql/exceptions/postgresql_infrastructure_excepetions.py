from src.externals.infrastructures.postgre_sql.exceptions.postgresql_base_infrastructure_exception import (
    PostgresqlBaseInfrastructureException,
)
from src.externals.infrastructures.postgre_sql.exceptions.postgresql_infrastructure_exceptions_reasons_enum import (
    PostgresqlInfrastructureExceptionsReasonsEnum,
)


class PostgresqlInfrastructureInterfaceErrorException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.INTERFACE_ERROR


class PostgresqlInfrastructureDatabaseErrorException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.DATABASE_ERROR


class PostgresqlInfrastructureDataErrorException(PostgresqlBaseInfrastructureException):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.DATA_ERROR


class PostgresqlInfrastructureOperationalErrorException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.OPERATIONAL_ERROR


class PostgresqlInfrastructureIntegrityErrorException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.INTEGRITY_ERROR


class PostgresqlInfrastructureInternalErrorException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.INTERNAL_ERROR


class PostgresqlInfrastructureProgrammingErrorException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.PROGRAMMING_ERROR


class PostgresqlInfrastructureNotSupportedErrorException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.NOT_SUPPORTED_ERROR


class PostgresqlInfrastructureConnectionTimeoutException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.CONNECTION_TIMEOUT


class PostgresqlInfrastructureAttributeErrorException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.ATTRIBUTE_ERROR


class PostgresqlInfrastructureUnexpectedErrorException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.UNEXPECTED_ERROR
