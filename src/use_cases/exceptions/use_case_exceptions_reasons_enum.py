from enum import IntEnum


class UseCaseExceptionsReasonsEnum(IntEnum):
    # ExtensionExceptionsCodes  400-499

    UNEXPECTED_EXCEPTION_ERROR = 400
    EXTENSION_CONVERSION_ERROR = 401
    REPOSITORY_EXCEPTION_ERROR = 402
    UNABLE_TO_RETRIEVE_BANK_ACCOUNTS_ERROR = 403
    UNABLE_TO_RETRIEVE_TRANSACTIONS_ERROR = 404
    UNABLE_TO_CREATE_BANK_ACCOUNT_ERROR = 405
    UNABLE_TO_REGISTER_TRANSACTION_ERROR = 406
    BENEFICIARY_ACCOUNT_NOT_FOUND_ERROR = 407
    TARGET_ACCOUNT_NOT_FOUND_ERROR = 408
    INSUFFICIENT_BALANCE_ERROR = 409
    UNABLE_TO_UPDATE_BALANCE_ERROR = 410
    UNABLE_TO_ACCOUNT_DEPOSIT_ERROR = 411
    UNABLE_TO_ACCOUNT_WITHDRAW_ERROR = 412
    UNABLE_TO_TRANSFER_BETWEEN_ACCOUNTS_ERROR = 413
