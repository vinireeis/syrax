from abc import abstractmethod

from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionsUnexpectedException,
)
from src.domain.models.bank_account_model import BankAccountModel
from src.use_cases.ports.extensions.bank_accounts.i_bank_accounts_extension import (
    IBankAccountsExtension,
)


class BankAccountsExtension(IBankAccountsExtension):

    @staticmethod
    @abstractmethod
    def from_database_result_to_model(result: dict) -> BankAccountModel:
        try:
            bank_account_model = BankAccountModel(**result)
            return bank_account_model

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected exception trying to get bank account model",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    @abstractmethod
    def from_database_result_list_to_model_list(
        result_list: list[dict],
    ) -> list[BankAccountModel]:
        bank_account_models = [
            BankAccountsExtension.from_database_result_to_model(result=result)
            for result in result_list
        ]

        return bank_account_models
