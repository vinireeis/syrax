from pydantic import UUID4

from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionsUnexpectedException,
)
from src.domain.entities.bank_account_entity import BankAccountEntity
from src.domain.entities.transaction_entity import TransactionEntity
from src.domain.enums.cash_flow.enum import CashFlowEnum
from src.domain.enums.operations.enum import AccountOperationEnum
from src.use_cases.data_types.dtos.bank_account_dto import BankAccountDto
from src.use_cases.data_types.dtos.moviment_cash_dto import MovementCashDto
from src.use_cases.data_types.requests.bank_accounts.base_movement_cash_request import (
    BaseMovementCashRequest,
)
from src.use_cases.data_types.requests.bank_accounts.create_new_account_request import (
    CreateNewAccountRequest,
)
from src.use_cases.data_types.responses.bank_account.create_new_account_response import (
    CreateNewAccountResponse,
    CreateNewAccountPayload,
)
from src.use_cases.data_types.responses.bank_account.movement_cash_response import (
    MovementCashResponse,
    MovementCashPayload,
)
from src.use_cases.ports.extensions.bank_accounts.i_movement_cash_extension import (
    IMovementCashExtension,
)


class MovementCashExtension(IMovementCashExtension):

    @staticmethod
    def from_router_params_to_request(
        account_id: UUID4, amount: float
    ) -> BaseMovementCashRequest:
        try:

            request = BaseMovementCashRequest(
                account_id=account_id,
                amount=amount,
            )
            return request

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected error trying to create request",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_entity_to_dto(
        entity: TransactionEntity,
    ) -> MovementCashDto:

        try:
            dto = MovementCashDto(
                account_id=entity.account_id,
                amount=entity.amount,
                operation=entity.operation,
                cash_flow=entity.cash_flow,
            )

            return dto

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected error trying to create dto",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_dto_to_response(dto: MovementCashDto) -> MovementCashResponse:
        try:
            payload = MovementCashPayload(
                account_id=dto.account_id,
                amount=dto.amount,
                operation=dto.operation,
            )

            response = MovementCashResponse(
                payload=payload,
                status=True,
                message=f"Operation successfully completed: {dto.operation}.",
            )

            return response

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected error trying to create movement_cash response",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def create_transaction_entity(
        request: BaseMovementCashRequest,
        operation: AccountOperationEnum,
        cash_flow: CashFlowEnum,
    ) -> TransactionEntity:
        try:
            transaction_entity = TransactionEntity(
                account_id=request.account_id,
                operation=operation,
                cash_flow=cash_flow,
                amount=request.amount,
            )

            return transaction_entity

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected error trying to create transaction entity",
                original_error=original_exception,
            ) from original_exception
