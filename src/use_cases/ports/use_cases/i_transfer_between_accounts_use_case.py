from abc import ABC, abstractmethod

from src.use_cases.data_types.dtos.moviment_cash_dto import MovementCashDto
from src.use_cases.data_types.requests.bank_accounts.movement_cash_between_accounts_request import (
    MovementCashBetweenAccountsRequest,
)


class ITransferBetweenAccountsUseCase(ABC):

    @abstractmethod
    async def transfer_amount(
        self, request: MovementCashBetweenAccountsRequest
    ) -> MovementCashDto:
        pass
