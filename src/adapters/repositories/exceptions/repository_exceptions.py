from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.adapters.repositories.exceptions.repository_exceptions_reasons_enum import (
    RepositoryExceptionsReasonsEnum,
)


class RepositoryUnexpectedException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.UNEXPECTED_ERROR


class ExtensionConversionException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.EXTENSION_CONVERSION_ERROR


class FailToInsertInformationException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.INSERT_ERROR


class InvalidOperationInsufficientBalanceException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.INVALID_OPERATION_ERROR


class FailToRetrieveInformationException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.RETRIEVE_INFORMATION_ERROR


class FailToUpdateInformationException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.UPDATE_ERROR
