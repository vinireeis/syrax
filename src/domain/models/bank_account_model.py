from dataclasses import dataclass
from decimal import Decimal

from psycopg.types import datetime
from pydantic import UUID4


@dataclass(slots=True)
class BankAccountModel:
    account_id: UUID4
    balance_end_of_day: Decimal
    created_at: datetime
