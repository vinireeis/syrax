from abc import ABC, abstractmethod

from src.use_cases.data_types.dtos.bank_account_dto import BankAccountDto
from src.use_cases.data_types.requests.checking_account.create_new_account_request import (
    CreateNewAccountRequest,
)


class ICreateNewAccountUseCase(ABC):

    @classmethod
    @abstractmethod
    async def create_new_account(
        cls, request: CreateNewAccountRequest
    ) -> BankAccountDto:
        pass
