from pydantic import BaseModel


class CreateNewAccountRequest(BaseModel):
    balance: float
