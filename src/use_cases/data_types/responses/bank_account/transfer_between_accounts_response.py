from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, UUID4

from src.use_cases.data_types.responses.base_api_response import BaseApiResponse


class TransferBetweenAccountsPayload(BaseModel):
    from_account_id: UUID4
    amount: Decimal
    target_account_id: UUID4
    transaction_datetime: datetime = None


class TransferBetweenAccountsResponse(BaseApiResponse):
    payload: TransferBetweenAccountsPayload
