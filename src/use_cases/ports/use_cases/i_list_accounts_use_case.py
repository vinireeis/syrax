from abc import ABC, abstractmethod

from src.use_cases.data_types.dtos.bank_account_dto import BankAccountDto


class IListAccountsUseCase(ABC):

    @abstractmethod
    async def list_accounts(self) -> list[BankAccountDto]:
        pass
