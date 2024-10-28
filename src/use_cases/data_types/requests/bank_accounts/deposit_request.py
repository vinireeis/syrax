from pydantic import UUID4

from src.use_cases.data_types.requests.bank_accounts.base_movement_cash_request import (
    BaseMovementCashRequest,
)


class TransferBetweenAccountsRequest(BaseMovementCashRequest):
    beneficiary_account_id: UUID4
