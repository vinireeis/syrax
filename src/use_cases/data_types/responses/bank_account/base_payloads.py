from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, UUID4

from src.domain.enums.cash_flow.enum import CashFlowEnum
from src.domain.enums.operations.enum import AccountOperationsEnum


class BaseTransactionPayload(BaseModel):
    amount: Decimal
    account_id: UUID4
    cash_flow: CashFlowEnum
    operation: AccountOperationsEnum
    transaction_datetime: datetime = None


class BaseMovementCashPayload(BaseModel):
    amount: Decimal
    account_id: UUID4
    operation: AccountOperationsEnum
    transaction_datetime: datetime = None
