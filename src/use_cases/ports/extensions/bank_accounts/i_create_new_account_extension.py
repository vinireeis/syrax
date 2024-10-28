from abc import abstractmethod

from src.domain.entities.bank_account_entity import BankAccountEntity
from src.use_cases.data_types.dtos.bank_account_dto import BankAccountDto
from src.use_cases.data_types.requests.checking_account.create_new_account_request import (
    CreateNewAccountRequest,
)
from src.use_cases.data_types.responses.checking_account.create_new_account_response import (
    CreateNewAccountResponse,
)


class ICreateNewAccountExtension:

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
