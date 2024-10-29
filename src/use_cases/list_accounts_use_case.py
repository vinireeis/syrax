from witch_doctor import WitchDoctor


from src.adapters.extensions.exceptions.extensions_base_exception import (
    ExtensionsBaseException,
)
from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.domain.models.bank_account_model import BankAccountModel
from src.use_cases.data_types.dtos.bank_account_dto import BankAccountDto
from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from src.use_cases.exceptions.use_case_exceptions import (
    UnableToCreateNewAccountException,
    UnableToRetrieveBankAccountsException,
    UseCaseUnexpectedException,
)
from src.use_cases.ports.extensions.bank_accounts.i_bank_accounts_extension import (
    IBankAccountsExtension,
)
from src.use_cases.ports.repositories.postrgresql.i_bank_accounts_repository import (
    IBankAccountsRepository,
)
from src.use_cases.ports.use_cases.i_list_accounts_use_case import (
    IListAccountsUseCase,
)


class ListAccountsUseCase(IListAccountsUseCase):

    @WitchDoctor.injection
    def __init__(
        self,
        bank_accounts_extension: IBankAccountsExtension,
        bank_accounts_repository: IBankAccountsRepository,
    ):
        self.bank_accounts_extension = bank_accounts_extension
        self.bank_accounts_repository = bank_accounts_repository

    async def list_accounts(self) -> list[BankAccountDto]:
        try:
            bank_account_models = await self.__get_bank_account_models()
            dto = self.__create_dto(bank_account_models=bank_account_models)
            return dto

        except UseCaseBaseException as original_exceptiom:
            raise original_exceptiom

        except Exception as original_exception:
            raise UseCaseUnexpectedException(
                message="Unexpected use case exception error.",
                original_error=original_exception,
            ) from original_exception

    async def __get_bank_account_models(self) -> list[BankAccountModel]:
        try:
            bank_account_models = await self.bank_accounts_repository.list_accounts()
            return bank_account_models

        except RepositoryBaseException as original_exception:
            raise UnableToRetrieveBankAccountsException(
                message="Unable to retrieve transactions.",
                original_error=original_exception.original_error,
            ) from original_exception

        except ExtensionsBaseException as original_exception:
            raise UnableToRetrieveBankAccountsException(
                message="Unable to retrieve bank accounts.",
                original_error=original_exception.original_error,
            ) from original_exception

    def __create_dto(
        self, bank_account_models: list[BankAccountModel]
    ) -> list[BankAccountDto]:
        try:
            dto = self.bank_accounts_extension.from_model_list_to_dto_list(
                models=bank_account_models
            )

            return dto

        except ExtensionsBaseException as original_exception:
            raise UnableToCreateNewAccountException(
                message="Error trying to create account dto.",
                original_error=original_exception,
            ) from original_exception
