from http import HTTPStatus

from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from src.use_cases.exceptions.use_case_exceptions_reasons_enum import (
    UseCaseExceptionsReasonsEnum,
)


class UseCaseUnexpectedException(UseCaseBaseException):
    _reason = UseCaseExceptionsReasonsEnum.UNEXPECTED_EXCEPTION
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR
