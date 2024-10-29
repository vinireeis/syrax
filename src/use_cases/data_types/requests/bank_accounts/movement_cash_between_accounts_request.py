from pydantic import UUID4

from src.use_cases.data_types.requests.bank_accounts.base_movement_cash_request import (
    BaseMovementCashRequest,
)


class MovementCashBetweenAccountsRequest(BaseMovementCashRequest):
    target_account_id: UUID4
