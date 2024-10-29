from src.use_cases.data_types.responses.bank_account.base.base_payloads import (
    BaseMovementCashPayload,
)
from src.use_cases.data_types.responses.base_api_response import BaseApiResponse


class MovementCashPayload(BaseMovementCashPayload):
    pass


class MovementCashResponse(BaseApiResponse):
    payload: MovementCashPayload
