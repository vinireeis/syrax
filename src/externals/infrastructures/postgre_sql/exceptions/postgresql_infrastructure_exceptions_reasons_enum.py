from enum import IntEnum


class PostgresqlInfrastructureExceptionsReasonsEnum(IntEnum):
    # PostgresqlInfrastructureExceptionsCodes 500-599

    INTERFACE_ERROR = 500
    DATABASE_ERROR = 501
    DATA_ERROR = 502
    OPERATIONAL_ERROR = 503
    INTEGRITY_ERROR = 504
    PROGRAMMING_ERROR = 505
    INTERNAL_ERROR = 506
    NOT_SUPPORTED_ERROR = 507
    CONNECTION_TIMEOUT = 508
    ATTRIBUTE_ERROR = 509
    UNEXPECTED_ERROR = 510
