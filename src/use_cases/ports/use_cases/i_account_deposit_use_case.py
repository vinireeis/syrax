from abc import ABC, abstractmethod

from src.use_cases.data_types.dtos.moviment_cash_dto import MovementCashDto
from src.use_cases.data_types.requests.bank_accounts.movement_cash_request import (
    MovementCashRequest,
)


class IAccountDepositUseCase(ABC):

    @abstractmethod
    async def account_deposit(self, request: MovementCashRequest) -> MovementCashDto:
        pass