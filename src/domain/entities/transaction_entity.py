from datetime import datetime
from decimal import Decimal
from typing import Type
from uuid import uuid4

from decouple import config
from pydantic import UUID4

from src.domain.enums.cash_flow.enum import CashFlowEnum, CashFlowOperator
from src.domain.enums.operations.enum import AccountOperationEnum


class TransactionEntity:
    def __init__(
        self,
        account_id: UUID4,
        operation: AccountOperationEnum,
        cash_flow: CashFlowEnum,
        amount: float,
        target_account_id: UUID4 = None,
        transaction_id: int = None,
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
        self.__target_account_id = target_account_id

    @property
    def account_id(self) -> UUID4:
        return self.__account_id

    @property
    def amount(self) -> Decimal:
        return self.to_decimal(self.__amount)

    @property
    def operation(self) -> AccountOperationEnum:
        return self.__operation

    @property
    def cash_flow(self) -> CashFlowEnum:
        return self.__cash_flow

    @property
    def reference_id(self) -> UUID4:
        return self.__reference_id

    @property
    def target_account_id(self) -> UUID4:
        return self.__target_account_id

    @property
    def transaction_datetime(self) -> datetime:
        return self.__transaction_datetime

    def generate_reference_id(self):
        _id = self._generate_uuid()
        self.__reference_id = _id

    @property
    def cash_flow_operator(self) -> Type[CashFlowOperator]:
        return CashFlowOperator[self.__cash_flow]

    @staticmethod
    def _generate_uuid() -> uuid4:
        _id = uuid4()
        return _id

    @staticmethod
    def to_decimal(amount: float) -> Decimal:
        amount_formated = Decimal(amount).quantize(Decimal(config("DECIMAL_PRECISION")))
        return amount_formated

    def _transaction_document_to_insert(self):
        row_to_insert = {
            "account_id": self.account_id,
            "amount": self.amount,
            "operation": self.operation.value,
            "cash_flow": self.cash_flow.value,
            "reference_id": self.reference_id,
        }
        return row_to_insert

    def _transaction_document_to_target_account(self):
        row_to_insert = {
            "account_id": self.target_account_id,
            "amount": self.amount,
            "operation": self.operation.value,
            "cash_flow": CashFlowEnum.CASH_IN.value,
            "reference_id": self.reference_id,
        }
        return row_to_insert

    def _amount_document_to_insert(self):
        row_to_insert = {
            "account_id": self.account_id,
            "amount": self.amount,
        }
        return row_to_insert
