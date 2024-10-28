from abc import ABC, abstractmethod

from src.domain.entities.bank_account_entity import BankAccountEntity
from src.domain.models.bank_account_model import BankAccountModel


class IBankAccountsRepository(ABC):

    @classmethod
    @abstractmethod
    async def insert_new_account(cls, bank_account_entity: BankAccountEntity):
        pass

    @classmethod
    @abstractmethod
    async def list_accounts(cls) -> list[BankAccountModel]:
        pass
