from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from pydantic import UUID4

from src.domain.enums.cash_flow.enum import CashFlowEnum
from src.domain.enums.operations.enum import AccountOperationsEnum


@dataclass(slots=True)
class BankAccountDto:
    transaction_id: UUID4
    account_id: UUID4
    amount: Decimal
    operation: AccountOperationsEnum
    cash_flow: CashFlowEnum
    reference_id: UUID4
    transaction_date: datetime = None
