from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionsUnexpectedException,
)
from src.domain.models.bank_account_model import BankAccountModel
from src.use_cases.data_types.dtos.bank_account_dto import BankAccountDto
from src.use_cases.data_types.responses.bank_account.list_accounts_response import (
    ListAccountsResponse,
    AccountPayload,
)
from src.use_cases.ports.extensions.bank_accounts.i_bank_accounts_extension import (
    IBankAccountsExtension,
)


class BankAccountsExtension(IBankAccountsExtension):

    @staticmethod
    def from_database_result_to_model(result: dict) -> BankAccountModel:
        try:
            bank_account_model = BankAccountModel(**result)
            return bank_account_model

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected error trying to get bank account model",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_database_result_list_to_model_list(
        result_list: list[dict],
    ) -> list[BankAccountModel]:
        bank_account_models = [
            BankAccountsExtension.from_database_result_to_model(result=result)
            for result in result_list
        ]

        return bank_account_models

    @staticmethod
    def from_model_to_dto(model: BankAccountModel) -> BankAccountDto:
        try:
            bank_account_model = BankAccountDto(
                account_id=model.account_id,
                balance_end_of_day=model.balance_end_of_day,
                created_at=model.created_at,
            )
            return bank_account_model

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected error trying to get bank accounts dto",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_model_list_to_dto_list(
        models: list[BankAccountModel],
    ) -> list[BankAccountDto]:
        bank_account_models = [
            BankAccountsExtension.from_model_to_dto(model=bank_account_model)
            for bank_account_model in models
        ]

        return bank_account_models

    @staticmethod
    def from_dto_list_to_response(dtos: list[BankAccountDto]) -> ListAccountsResponse:
        try:
            payload = [
                AccountPayload(
                    account_id=dto.account_id,
                    balance_end_of_day=dto.balance_end_of_day,
                    created_at=dto.created_at,
                )
                for dto in dtos
            ]

            response = ListAccountsResponse(
                payload=payload,
                status=True,
            )

            return response

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected error trying to get list accounts response",
                original_error=original_exception,
            ) from original_exception
