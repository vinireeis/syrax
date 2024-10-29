from abc import ABC, abstractmethod

from src.use_cases.data_types.dtos.bank_account_dto import BankAccountDto
from src.use_cases.data_types.requests.bank_accounts.create_new_account_request import (
    CreateNewAccountRequest,
)


class ICreateNewAccountUseCase(ABC):

    @abstractmethod
    async def create_new_account(
        self, request: CreateNewAccountRequest
    ) -> BankAccountDto:
        pass
