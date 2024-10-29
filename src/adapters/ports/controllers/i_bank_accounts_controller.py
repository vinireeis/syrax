from abc import ABC, abstractmethod

from pydantic import UUID4

from src.use_cases.data_types.requests.bank_accounts.create_new_account_request import (
    CreateNewAccountRequest,
)
from src.use_cases.data_types.responses.bank_account.create_new_account_response import (
    CreateNewAccountResponse,
)
from src.use_cases.data_types.responses.bank_account.movement_cash_response import (
    MovementCashResponse,
)
from src.use_cases.data_types.responses.bank_account.get_balance_response import (
    GetBalanceResponse,
)
from src.use_cases.data_types.responses.bank_account.list_transactions_response import (
    ListTransactionsByAccountResponse,
)
from src.use_cases.data_types.responses.bank_account.list_accounts_response import (
    ListAccountsResponse,
)
from src.use_cases.data_types.responses.bank_account.movement_cash_between_accounts_response import (
    MovementCashBetweenAccountsResponse,
)


class IBankAccountsController(ABC):

    @classmethod
    @abstractmethod
    async def create_new_bank_account(
        cls, request: CreateNewAccountRequest
    ) -> CreateNewAccountResponse:
        pass

    @classmethod
    @abstractmethod
    async def list_accounts(cls) -> ListAccountsResponse:
        pass

    @classmethod
    @abstractmethod
    async def checking_account_deposit(
        cls, account_id: UUID4, amount: float
    ) -> MovementCashResponse:
        pass

    @classmethod
    @abstractmethod
    async def checking_account_withdraw(
        cls, account_id: UUID4, amount: float
    ) -> MovementCashResponse:
        pass

    @classmethod
    @abstractmethod
    async def transfer_between_accounts(
        cls,
        account_id: UUID4,
        amount: float,
        target_account_id: UUID4,
    ) -> MovementCashBetweenAccountsResponse:
        pass

    @classmethod
    @abstractmethod
    async def get_balance(cls, account_id: UUID4) -> GetBalanceResponse:
        pass

    @classmethod
    @abstractmethod
    async def list_transactions_by_account(
        cls, account_id: UUID4
    ) -> ListTransactionsByAccountResponse:
        pass
