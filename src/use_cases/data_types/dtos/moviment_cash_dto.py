from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from pydantic import UUID4

from src.domain.enums.cash_flow.enum import CashFlowEnum
from src.domain.enums.operations.enum import AccountOperationEnum


@dataclass(slots=True)
class MovementCashDto:
    account_id: UUID4
    amount: Decimal
    operation: AccountOperationEnum
    cash_flow: CashFlowEnum
    reference_id: UUID4 = None
    transaction_datetime: datetime = None
