from pydantic import UUID4

from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionsUnexpectedException,
)
from src.domain.entities.transaction_entity import TransactionEntity
from src.domain.enums.cash_flow.enum import CashFlowEnum
from src.domain.enums.operations.enum import AccountOperationEnum
from src.use_cases.data_types.dtos.moviment_cash_dto import MovementCashDto
from src.use_cases.data_types.requests.bank_accounts.movement_cash_between_accounts_request import (
    MovementCashBetweenAccountsRequest,
)

from src.use_cases.data_types.responses.bank_account.movement_cash_between_accounts_response import (
    MovementCashBetweenAccountsResponse,
    MovementCashBetweenAccountsPayload,
)
from src.use_cases.ports.extensions.bank_accounts.i_movement_cash_between_accounts_extension import (
    IMovementCashBetweenAccountsExtension,
)


class MovementCashBetweenAccountsExtension(IMovementCashBetweenAccountsExtension):

    @staticmethod
    def from_router_params_to_request(
        account_id: UUID4, amount: float, target_account_id: UUID4
    ) -> MovementCashBetweenAccountsRequest:
        try:

            request = MovementCashBetweenAccountsRequest(
                account_id=account_id,
                amount=amount,
                target_account_id=target_account_id,
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
                target_account_id=entity.target_account_id,
            )

            return dto

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected error trying to create dto",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_dto_to_response(
        dto: MovementCashDto,
    ) -> MovementCashBetweenAccountsResponse:
        try:
            payload = MovementCashBetweenAccountsPayload(
                account_id=dto.account_id,
                amount=dto.amount,
                operation=dto.operation.value,
                target_account_id=dto.target_account_id,
            )

            response = MovementCashBetweenAccountsResponse(
                payload=payload,
                status=True,
                message=f"Operation successfully completed: {dto.operation.value}.",
            )

            return response

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected error trying to create movement_cash response",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def create_transaction_entity(
        request: MovementCashBetweenAccountsRequest,
    ) -> TransactionEntity:
        try:
            transaction_entity = TransactionEntity(
                account_id=request.account_id,
                operation=AccountOperationEnum.TRANSFER,
                cash_flow=CashFlowEnum.CASH_OUT,
                amount=request.amount,
            )
            transaction_entity.generate_reference_id()

            return transaction_entity

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected error trying to create transaction entity",
                original_error=original_exception,
            ) from original_exception
