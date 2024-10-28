from pydantic import BaseModel, Field

from src.use_cases.data_types.responses.bank_account.base.base_payloads import (
    BaseTransactionPayload,
)
from src.use_cases.data_types.responses.base_api_response import BaseApiResponse


class ListTransactionsPayload(BaseModel):
    transactions: list[BaseTransactionPayload] = Field(default_factory=list)


class ListTransactionsByAccountResponse(BaseApiResponse):
    payload: ListTransactionsPayload
