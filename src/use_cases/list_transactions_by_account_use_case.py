from pydantic.v1 import UUID4
from witch_doctor import WitchDoctor


from src.adapters.extensions.exceptions.extensions_base_exception import (
    ExtensionsBaseException,
)
from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.domain.models.transaction_model import TransactionModel
from src.use_cases.data_types.dtos.transaction_dto import TransactionDto
from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from src.use_cases.exceptions.use_case_exceptions import (
    UnableToRetrieveTransactionsException,
    UseCaseUnexpectedException,
)
from src.use_cases.ports.extensions.bank_accounts.i_transactions_extension import (
    ITransactionsExtension,
)
from src.use_cases.ports.repositories.postrgresql.i_bank_accounts_repository import (
    IBankAccountsRepository,
)

from src.use_cases.ports.use_cases.i_list_transactions_by_account_use_case import (
    IListTransactionsByAccountUseCase,
)


class ListTransactionsByAccountUseCase(IListTransactionsByAccountUseCase):

    @WitchDoctor.injection
    def __init__(
        self,
        transactions_extension: ITransactionsExtension,
        bank_accounts_repository: IBankAccountsRepository,
    ):
        self.bank_accounts_extension = transactions_extension
        self.bank_accounts_repository = bank_accounts_repository

    async def list_by_account(self, account_id: UUID4) -> list[TransactionDto]:
        try:
            transaction_models = await self.__get_transactions_by_account_id(
                account_id=account_id
            )
            dto = self.__create_dto(transaction_models=transaction_models)
            return dto

        except UseCaseBaseException as original_exceptiom:
            raise original_exceptiom

        except Exception as original_exception:
            raise UseCaseUnexpectedException(
                message="Unexpected use case exception error.",
                original_error=original_exception,
            ) from original_exception

    async def __get_transactions_by_account_id(
        self, account_id: UUID4
    ) -> list[TransactionModel | None]:
        try:
            transaction_models = (
                await self.bank_accounts_repository.get_transactions_by_account_id(
                    account_id=account_id
                )
            )
            return transaction_models

        except RepositoryBaseException as original_exception:
            raise UnableToRetrieveTransactionsException(
                message="Unable to retrieve transactions.",
                original_error=original_exception.original_error,
            ) from original_exception

        except ExtensionsBaseException as original_exception:
            raise UnableToRetrieveTransactionsException(
                message="Unable to retrieve transactions.",
                original_error=original_exception.original_error,
            ) from original_exception

    def __create_dto(
        self, transaction_models: list[TransactionModel | None]
    ) -> list[TransactionDto | None]:
        try:
            dto = self.bank_accounts_extension.from_model_list_to_dto_list(
                models=transaction_models
            )

            return dto

        except ExtensionsBaseException as original_exception:
            raise UnableToRetrieveTransactionsException(
                message="Error trying to create transaction dtos.",
                original_error=original_exception,
            ) from original_exception
