from abc import abstractmethod, ABC

from pydantic import UUID4

from src.domain.entities.transaction_entity import TransactionEntity
from src.domain.enums.cash_flow.enum import CashFlowEnum
from src.domain.enums.operations.enum import AccountOperationEnum
from src.use_cases.data_types.dtos.moviment_cash_dto import MovementCashDto
from src.use_cases.data_types.requests.bank_accounts.base_movement_cash_request import (
    BaseMovementCashRequest,
)
from src.use_cases.data_types.requests.bank_accounts.movement_cash_request import (
    MovementCashRequest,
)
from src.use_cases.data_types.responses.bank_account.movement_cash_response import (
    MovementCashResponse,
)


class IMovementCashExtension(ABC):

    @staticmethod
    @abstractmethod
    def from_router_params_to_request(
        account_id: UUID4, amount: float
    ) -> MovementCashRequest | BaseMovementCashRequest:
        pass

    @staticmethod
    @abstractmethod
    def create_transaction_entity(
        request: BaseMovementCashRequest | MovementCashRequest,
        operation: AccountOperationEnum,
        cash_flow: CashFlowEnum,
    ) -> TransactionEntity:
        pass

    @staticmethod
    @abstractmethod
    def from_entity_to_dto(
        entity: TransactionEntity,
    ) -> MovementCashDto:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_to_response(dto: MovementCashDto) -> MovementCashResponse:
        pass
