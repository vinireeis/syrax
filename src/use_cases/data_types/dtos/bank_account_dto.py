from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from pydantic import UUID4


@dataclass(slots=True)
class BankAccountDto:
    account_id: UUID4
    balance_end_of_day: Decimal = None
    created_at: datetime = None
