from datetime import datetime
from decimal import Decimal

from decouple import config
from pydantic import UUID4

from src.domain.enums.cash_flow.enum import CashFlowEnum
from src.domain.enums.operations.enum import AccountOperationsEnum


class TransactionEntity:
    def __init__(
        self,
        account_id: UUID4,
        amount: float,
        operation: AccountOperationsEnum,
        cash_flow: CashFlowEnum,
        transaction_id: UUID4 = None,
        reference_id: UUID4 = None,
        transaction_datetime: datetime = None,
    ):
        self.__transaction_id = transaction_id
        self.__account_id = account_id
        self.__amount = amount
        self.__operation = operation
        self.__cash_flow = cash_flow
        self.__reference_id = reference_id
        self.__transaction_datetime = transaction_datetime

    @property
    def transaction_id(self) -> UUID4:
        return self.__transaction_id

    @property
    def account_id(self) -> UUID4:
        return self.__account_id

    @property
    def amount(self) -> Decimal:
        return self.to_decimal(self.__amount)

    @property
    def operation(self) -> AccountOperationsEnum:
        return self.__operation

    @property
    def cash_flow(self) -> CashFlowEnum:
        return self.__cash_flow

    @property
    def reference_id(self) -> UUID4:
        return self.__reference_id

    @property
    def transaction_datetime(self) -> datetime:
        return self.__transaction_datetime

    def _generate_transaction_id(self):
        _id = self._generate_uuid()
        self.__transaction_id = _id

    def generate_reference_id(self):
        _id = self._generate_uuid()
        self.__reference_id = _id

    @staticmethod
    def _generate_uuid() -> UUID4:
        _id = UUID4()
        return _id

    @staticmethod
    def to_decimal(amount: float) -> Decimal:
        amount_formated = Decimal(amount).quantize(Decimal(config("DECIMAL_PRECISION")))
        return amount_formated
