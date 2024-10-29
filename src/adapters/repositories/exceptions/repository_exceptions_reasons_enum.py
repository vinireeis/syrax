from enum import IntEnum


class RepositoryExceptionsReasonsEnum(IntEnum):
    # ExtensionExceptionsCodes  600-799

    RETRIEVE_INFORMATION_ERROR = 600
    INSERT_ERROR = 601
    EXTENSION_CONVERSION_ERROR = 602
    UNEXPECTED_ERROR = 603
    UPDATE_ERROR = 604
    INVALID_OPERATION_ERROR = 605
