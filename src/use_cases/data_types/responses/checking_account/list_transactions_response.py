from decimal import Decimal

from pydantic import BaseModel, UUID4

from src.use_cases.data_types.responses.base_api_response import BaseApiResponse
from src.use_cases.data_types.responses.enums.cash_flow.enum import CashFlowEnum


class TransactionPayload(BaseModel):
    amount: Decimal
    origin_account: UUID4
    description: str
    cash_flow: CashFlowEnum


class GetTransactionsPayload(BaseModel):
    transactions: list[TransactionPayload] = None


class ListTransactionsByAccountResponse(BaseApiResponse):
    payload: GetTransactionsPayload
