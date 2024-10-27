from http import HTTPStatus

from src.adapters.extensions.exceptions.extension_exceptions_reasons_enum import (
    ExtensionExceptionsReasonsEnum,
)
from src.adapters.extensions.exceptions.extensions_base_exception import (
    ExtensionsBaseException,
)


class ExtensionsUnexpectedException(ExtensionsBaseException):
    _reason = ExtensionExceptionsReasonsEnum.UNEXPECTED_EXCEPTION
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR


class EntityCreationException(ExtensionsBaseException):
    _reason = ExtensionExceptionsReasonsEnum.ENTITY_CREATION_ERROR
    _http_status_code = HTTPStatus.BAD_REQUEST
