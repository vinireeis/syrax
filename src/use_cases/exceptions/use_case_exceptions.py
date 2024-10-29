from http import HTTPStatus

from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from src.use_cases.exceptions.use_case_exceptions_reasons_enum import (
    UseCaseExceptionsReasonsEnum,
)


class UseCaseUnexpectedException(UseCaseBaseException):
    _reason = UseCaseExceptionsReasonsEnum.UNEXPECTED_EXCEPTION_ERROR
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR


class UnableToRetrieveBankAccountsException(UseCaseUnexpectedException):
    _reason = UseCaseExceptionsReasonsEnum.UNABLE_TO_RETRIEVE_BANK_ACCOUNTS_ERROR
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR


class UnableToRetrieveTransactionsException(UseCaseUnexpectedException):
    _reason = UseCaseExceptionsReasonsEnum.UNABLE_TO_RETRIEVE_TRANSACTIONS_ERROR
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR


class UnableToCreateNewAccountException(UseCaseUnexpectedException):
    _reason = UseCaseExceptionsReasonsEnum.UNABLE_TO_CREATE_BANK_ACCOUNT_ERROR
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR


class UnableToAccountDepositException(UseCaseUnexpectedException):
    _reason = UseCaseExceptionsReasonsEnum.UNABLE_TO_ACCOUNT_DEPOSIT_ERROR
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR


class UnableToAccountWithdrawException(UseCaseUnexpectedException):
    _reason = UseCaseExceptionsReasonsEnum.UNABLE_TO_ACCOUNT_WITHDRAW_ERROR
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR


class UnableToTransferBetweenAccountsException(UseCaseUnexpectedException):
    _reason = UseCaseExceptionsReasonsEnum.UNABLE_TO_TRANSFER_BETWEEN_ACCOUNTS_ERROR
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR


class InsufficientBalanceException(UseCaseUnexpectedException):
    _reason = UseCaseExceptionsReasonsEnum.INSUFFICIENT_BALANCE_ERROR
    _http_status_code = HTTPStatus.BAD_REQUEST
