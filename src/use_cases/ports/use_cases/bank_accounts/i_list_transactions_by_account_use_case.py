from abc import ABC, abstractmethod

from pydantic.v1 import UUID4

from src.use_cases.data_types.dtos.transaction_dto import TransactionDto


class IListTransactionsByAccountUseCase(ABC):

    @abstractmethod
    async def list_by_account(self, account_id: UUID4) -> list[TransactionDto]:
        pass
