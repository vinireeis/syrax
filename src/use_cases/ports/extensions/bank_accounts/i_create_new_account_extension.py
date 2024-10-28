from abc import abstractmethod, ABC

from src.domain.entities.bank_account_entity import BankAccountEntity
from src.domain.entities.transaction_entity import TransactionEntity
from src.use_cases.data_types.dtos.bank_account_dto import BankAccountDto
from src.use_cases.data_types.requests.bank_accounts.create_new_account_request import (
    CreateNewAccountRequest,
)
from src.use_cases.data_types.responses.bank_account.create_new_account_response import (
    CreateNewAccountResponse,
)


class ICreateNewAccountExtension(ABC):

    @staticmethod
    @abstractmethod
    def from_request_to_entity(request: CreateNewAccountRequest) -> BankAccountEntity:
        pass

    @staticmethod
    @abstractmethod
    def from_entity_to_dto(entity: BankAccountEntity) -> BankAccountDto:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_to_response(dto: BankAccountDto) -> CreateNewAccountResponse:
        pass

    @staticmethod
    @abstractmethod
    def create_transaction_entity(
        bank_account_entity: BankAccountEntity,
    ) -> TransactionEntity:
        pass
