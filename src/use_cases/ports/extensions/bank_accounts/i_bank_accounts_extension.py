from abc import abstractmethod

from src.domain.models.bank_account_model import BankAccountModel


class IBankAccountsExtension:

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
