from dataclasses import dataclass
from decimal import Decimal

from psycopg.types import datetime
from pydantic import UUID4

from src.domain.enums.cash_flow.enum import CashFlowEnum
from src.domain.enums.operations.enum import AccountOperationEnum


@dataclass(slots=True)
class TransactionModel:
    transaction_id: int
    account_id: UUID4
    amount: Decimal
    operation: AccountOperationEnum
    cash_flow: CashFlowEnum
    created_at: datetime
    reference_id: UUID4 = None
    transaction_datetime: datetime = None
