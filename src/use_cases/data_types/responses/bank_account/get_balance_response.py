from decimal import Decimal

from pydantic import BaseModel

from src.use_cases.data_types.responses.base_api_response import BaseApiResponse


class GetBalancePayload(BaseModel):
    current_balance: Decimal


class GetBalanceResponse(BaseApiResponse):
    payload: GetBalancePayload
