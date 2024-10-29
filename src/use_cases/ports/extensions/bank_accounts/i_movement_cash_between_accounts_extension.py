from abc import abstractmethod, ABC

from pydantic import UUID4

from src.domain.entities.transaction_entity import TransactionEntity
from src.use_cases.data_types.dtos.moviment_cash_dto import MovementCashDto
from src.use_cases.data_types.requests.bank_accounts.movement_cash_between_accounts_request import (
    MovementCashBetweenAccountsRequest,
)
from src.use_cases.data_types.responses.bank_account.movement_cash_between_accounts_response import (
    MovementCashBetweenAccountsResponse,
)


class IMovementCashBetweenAccountsExtension(ABC):

    @staticmethod
    @abstractmethod
    def from_router_params_to_request(
        account_id: UUID4, amount: float, target_account_id: UUID4
    ) -> MovementCashBetweenAccountsRequest:
        pass

    @staticmethod
    @abstractmethod
    def create_transaction_entity(
        request: MovementCashBetweenAccountsRequest,
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
    def from_dto_to_response(
        dto: MovementCashDto,
    ) -> MovementCashBetweenAccountsResponse:
        pass
