from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.adapters.repositories.exceptions.repository_exceptions_reasons_enum import (
    RepositoryExceptionsReasonsEnum,
)


class RepositoryUnexpectedException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.UNEXPECTED_EXCEPTION


class ExtensionConversionException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.EXTENSION_CONVERSION_EXCEPTION


class FailToInsertInformationException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.INSERT_EXCEPTION


class FailToRetrieveInformationException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.RETRIEVE_INFORMATION_EXCEPTION


class FailToUpdateInformationException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.UPDATE_EXCEPTION
