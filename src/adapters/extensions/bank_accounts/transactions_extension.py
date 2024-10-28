from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionsUnexpectedException,
)
from src.domain.models.transaction_model import TransactionModel
from src.use_cases.data_types.dtos.bank_account_dto import BankAccountDto
from src.use_cases.data_types.dtos.transaction_dto import TransactionDto
from src.use_cases.data_types.responses.bank_account.list_accounts_response import (
    ListAccountsResponse,
    AccountPayload,
)
from src.use_cases.ports.extensions.bank_accounts.i_transactions_extension import (
    ITransactionsExtension,
)


class TransactionsExtension(ITransactionsExtension):

    @staticmethod
    def from_database_result_to_model(result: dict) -> TransactionModel:
        try:
            transaction_model = TransactionModel(**result)
            return transaction_model

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected error trying to get transaction model",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_database_result_list_to_model_list(
        result_list: list[dict],
    ) -> list[TransactionModel]:
        transaction_models = [
            TransactionsExtension.from_database_result_to_model(result=result)
            for result in result_list
        ]

        return transaction_models

    @staticmethod
    def from_model_to_dto(model: TransactionModel) -> TransactionDto:
        try:
            transaction_model = TransactionDto(
                transaction_id=model.transaction_id,
                account_id=model.account_id,
                amount=model.amount,
                operation=model.operation,
                cash_flow=model.cash_flow,
                reference_id=model.reference_id,
                transaction_date=model.transaction_date,
            )
            return transaction_model

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected error trying to get transaction dto",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_model_list_to_dto_list(
        models: list[TransactionModel],
    ) -> list[TransactionDto]:
        transaction_models = [
            TransactionsExtension.from_model_to_dto(model=transaction_model)
            for transaction_model in models
        ]

        return transaction_models

    @staticmethod
    def from_dto_list_to_response(dtos: list[BankAccountDto]) -> ListAccountsResponse:
        try:
            payload = [
                AccountPayload(
                    account_id=dto.account_id,
                    balance_end_of_day=dto.balance,
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
