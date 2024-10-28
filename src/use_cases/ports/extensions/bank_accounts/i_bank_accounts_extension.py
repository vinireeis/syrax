from abc import abstractmethod, ABC

from src.domain.models.bank_account_model import BankAccountModel
from src.use_cases.data_types.dtos.bank_account_dto import BankAccountDto
from src.use_cases.data_types.responses.bank_account.list_accounts_response import (
    ListAccountsResponse,
)


class IBankAccountsExtension(ABC):

    @staticmethod
    @abstractmethod
    def from_database_result_to_model(result: dict) -> BankAccountModel:
        pass

    @staticmethod
    @abstractmethod
    def from_database_result_list_to_model_list(
        result_list: list[dict],
    ) -> list[BankAccountModel]:
        pass

    @staticmethod
    @abstractmethod
    def from_model_list_to_dto_list(
        models: list[BankAccountModel],
    ) -> list[BankAccountDto]:
        pass

    @staticmethod
    @abstractmethod
    def from_model_to_dto(model: BankAccountModel) -> BankAccountDto:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_list_to_response(dtos: list[BankAccountDto]) -> ListAccountsResponse:
        pass
