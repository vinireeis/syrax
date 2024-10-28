from abc import ABC, abstractmethod

from pydantic import UUID4

from src.domain.entities.bank_account_entity import BankAccountEntity
from src.domain.entities.transaction_entity import TransactionEntity
from src.domain.models.bank_account_model import BankAccountModel
from src.domain.models.transaction_model import TransactionModel


class IBankAccountsRepository(ABC):

    @classmethod
    @abstractmethod
    async def insert_new_account(cls, bank_account_entity: BankAccountEntity):
        pass

    @classmethod
    @abstractmethod
    async def list_accounts(cls) -> list[BankAccountModel]:
        pass

    @classmethod
    @abstractmethod
    async def insert_new_transaction(cls, transaction_entity: TransactionEntity):
        pass

    @classmethod
    @abstractmethod
    async def get_transactions_by_account_id(
        cls, account_id: UUID4
    ) -> list[TransactionModel]:
        pass
