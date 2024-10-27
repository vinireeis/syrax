from enum import IntEnum


class UseCaseExceptionsReasonsEnum(IntEnum):
    # ExtensionExceptionsCodes  400-499

    UNEXPECTED_EXCEPTION = 400
    EXTENSION_CONVERSION_ERROR = 401
    REPOSITORY_EXCEPTION = 402
