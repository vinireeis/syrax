from witch_doctor import WitchDoctor

from src.adapters.extensions.exceptions.extensions_base_exception import (
    ExtensionsBaseException,
)
from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.adapters.repositories.exceptions.repository_exceptions import (
    InvalidOperationInsufficientBalanceException,
)
from src.domain.entities.transaction_entity import TransactionEntity
from src.use_cases.data_types.dtos.moviment_cash_dto import MovementCashDto
from src.use_cases.data_types.requests.bank_accounts.movement_cash_between_accounts_request import (
    MovementCashBetweenAccountsRequest,
)

from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from src.use_cases.exceptions.use_case_exceptions import (
    UseCaseUnexpectedException,
    InsufficientBalanceException,
    UnableToTransferBetweenAccountsException,
)
from src.use_cases.ports.extensions.bank_accounts.i_movement_cash_between_accounts_extension import (
    IMovementCashBetweenAccountsExtension,
)

from src.use_cases.ports.repositories.postrgresql.i_bank_accounts_repository import (
    IBankAccountsRepository,
)
from src.use_cases.ports.use_cases.i_transfer_between_accounts_use_case import (
    ITransferBetweenAccountsUseCase,
)


class TransferBetweenAccountsUseCase(ITransferBetweenAccountsUseCase):

    @WitchDoctor.injection
    def __init__(
        self,
        movement_cash_between_accounts_extension: IMovementCashBetweenAccountsExtension,
        bank_accounts_repository: IBankAccountsRepository,
    ):
        self.movement_cash_between_accounts_extension = (
            movement_cash_between_accounts_extension
        )
        self.bank_accounts_repository = bank_accounts_repository

    async def transfer_amount(
        self, request: MovementCashBetweenAccountsRequest
    ) -> MovementCashDto:
        try:
            transaction_entity = self.__create_transaction_entity(request=request)
            await self.__update_balance(transaction_entity=transaction_entity)
            await self.__insert_transactions(transaction_entity=transaction_entity)
            dto = self.__create_dto(transaction_entity=transaction_entity)
            return dto

        except UseCaseBaseException as original_exceptiom:
            raise original_exceptiom

        except Exception as original_exception:
            raise UseCaseUnexpectedException(
                message="Unexpected use case exception error.",
                original_error=original_exception,
            ) from original_exception

    def __create_transaction_entity(self, request: MovementCashBetweenAccountsRequest):
        try:
            transaction_entity = (
                self.movement_cash_between_accounts_extension.create_transaction_entity(
                    request=request
                )
            )
            return transaction_entity

        except ExtensionsBaseException as original_exception:
            raise UnableToTransferBetweenAccountsException(
                message="Error trying to create transaction entity.",
                original_error=original_exception,
            ) from original_exception

    async def __insert_transactions(self, transaction_entity: TransactionEntity):
        try:
            await self.bank_accounts_repository.insert_transaction_between_accounts(
                transaction_entity=transaction_entity
            )

        except RepositoryBaseException as original_exception:
            raise UnableToTransferBetweenAccountsException(
                message="Fail to insert transaction",
                original_error=original_exception.original_error,
            ) from original_exception

    async def __update_balance(self, transaction_entity: TransactionEntity):
        try:
            await self.bank_accounts_repository.update_amount_balance_between_accounts(
                transaction_entity=transaction_entity
            )
        except InvalidOperationInsufficientBalanceException as original_exception:
            raise InsufficientBalanceException(
                message="Invalid operation, insufficient balance.",
            ) from original_exception

        except RepositoryBaseException as original_exception:
            raise UnableToTransferBetweenAccountsException(
                message=original_exception.message,
                original_error=original_exception.original_error,
            ) from original_exception

    def __create_dto(self, transaction_entity: TransactionEntity) -> MovementCashDto:
        try:
            dto = self.movement_cash_between_accounts_extension.from_entity_to_dto(
                entity=transaction_entity
            )

            return dto

        except ExtensionsBaseException as original_exception:
            raise UnableToTransferBetweenAccountsException(
                message="Error trying to create movement cash between accounts dto.",
                original_error=original_exception,
            ) from original_exception
