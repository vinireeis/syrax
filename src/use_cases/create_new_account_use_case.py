from decimal import Decimal

from witch_doctor import WitchDoctor

from src.adapters.extensions.exceptions.extension_exceptions import (
    EntityCreationException,
)
from src.adapters.extensions.exceptions.extensions_base_exception import (
    ExtensionsBaseException,
)
from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.domain.entities.bank_account_entity import BankAccountEntity
from src.use_cases.data_types.dtos.bank_account_dto import BankAccountDto
from src.use_cases.data_types.requests.bank_accounts.create_new_account_request import (
    CreateNewAccountRequest,
)
from src.use_cases.exceptions.use_case_exceptions import (
    UnableToCreateNewAccountException,
)

from src.use_cases.ports.extensions.bank_accounts.i_create_new_account_extension import (
    ICreateNewAccountExtension,
)
from src.use_cases.ports.repositories.postrgresql.i_bank_accounts_repository import (
    IBankAccountsRepository,
)
from src.use_cases.ports.use_cases.bank_accounts.i_create_new_account_use_case import (
    ICreateNewAccountUseCase,
)


class CreateNewAccountUseCase(ICreateNewAccountUseCase):

    @WitchDoctor.injection
    def __init__(
        self,
        create_new_account_extension: ICreateNewAccountExtension,
        bank_accounts_repository: IBankAccountsRepository,
    ):
        self.create_new_account_extension = create_new_account_extension
        self.bank_accounts_repository = bank_accounts_repository

    async def create_new_account(
        self,
        request: CreateNewAccountRequest,
    ) -> BankAccountDto:
        bank_account_entity = self.__create_bank_account_entity(request=request)
        await self.__insert_new_account(bank_account_entity=bank_account_entity)
        dto = self.__create_dto(bank_account_entity=bank_account_entity)

        return dto

    def __create_bank_account_entity(self, request: CreateNewAccountRequest):
        try:
            account_entity = self.create_new_account_extension.from_request_to_entity(
                request=request
            )
            return account_entity

        except ExtensionsBaseException as original_exception:
            raise UnableToCreateNewAccountException(
                message="Error trying to create account entity.",
                original_error=original_exception,
            ) from original_exception

    async def __insert_new_account(self, bank_account_entity: BankAccountEntity):
        try:
            await self.bank_accounts_repository.insert_new_account(
                bank_account_entity=bank_account_entity
            )

        except RepositoryBaseException as original_exception:
            raise UnableToCreateNewAccountException(
                message="Unable to insert new account in database.",
                original_error=original_exception.original_error,
            ) from original_exception

    async def __insert_initial_balance_transaction(
        self, bank_account_entity: BankAccountEntity
    ):
        try:
            if bool(bank_account_entity.balance):

                transaction_entity = (
                    self.create_new_account_extension.create_transaction_entity(
                        bank_account_entity=bank_account_entity
                    )
                )

                await self.bank_accounts_repository.insert_new_transaction(
                    transaction_entity=transaction_entity
                )

        except RepositoryBaseException as original_exception:
            raise UnableToCreateNewAccountException(
                message="Unable to insert initial transaction in database.",
                original_error=original_exception.original_error,
            ) from original_exception

    def __create_dto(self, bank_account_entity: BankAccountEntity) -> BankAccountDto:
        try:
            dto = self.create_new_account_extension.from_entity_to_dto(
                entity=bank_account_entity
            )

            return dto

        except ExtensionsBaseException as original_exception:
            raise UnableToCreateNewAccountException(
                message="Error trying to create account dto.",
                original_error=original_exception,
            ) from original_exception
