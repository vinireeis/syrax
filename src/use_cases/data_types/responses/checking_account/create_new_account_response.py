from uuid import uuid4

from pydantic import BaseModel

from src.use_cases.data_types.responses.base_api_response import BaseApiResponse


class CreateNewAccountPayload(BaseModel):
    account_id: uuid4


class CreateNewAccountResponse(BaseApiResponse):
    payload: CreateNewAccountPayload
