from datetime import datetime
from decimal import Decimal

from pydantic import UUID4, BaseModel

from src.use_cases.data_types.responses.base_api_response import BaseApiResponse


class AccountWithdrawPayload(BaseModel):
    account_id: UUID4
    amount: Decimal
    transaction_datetime: datetime = None


class WithdrawResponse(BaseApiResponse):
    payload: None
