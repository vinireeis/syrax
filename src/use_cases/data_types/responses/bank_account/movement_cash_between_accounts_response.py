from pydantic import UUID4

from src.use_cases.data_types.responses.bank_account.base.base_payloads import (
    BaseMovementCashPayload,
)
from src.use_cases.data_types.responses.base_api_response import BaseApiResponse


class MovementCashBetweenAccountsPayload(BaseMovementCashPayload):
    target_account_id: UUID4


class MovementCashBetweenAccountsResponse(BaseApiResponse):
    payload: MovementCashBetweenAccountsPayload
