from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, UUID4

from src.use_cases.data_types.responses.base_api_response import BaseApiResponse


class AccountPayload(BaseModel):
    account_id: UUID4
    balance: Decimal = None
    created_at: datetime = None


class ListAccountsResponse(BaseApiResponse):
    payload: list[AccountPayload] = None
