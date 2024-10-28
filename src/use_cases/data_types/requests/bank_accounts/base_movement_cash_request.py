from pydantic import BaseModel, UUID4


class BaseMovementCashRequest(BaseModel):
    amount: float
    account_id: UUID4
