from enum import StrEnum


class AccountOperationEnum(StrEnum):
    TRANSFER = "transfer"
    WITHDRAW = "withdraw"
    DEPOSIT = "deposit"
