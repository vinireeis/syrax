from abc import ABC, abstractmethod

from pydantic import UUID4

from src.use_cases.data_types.requests.checking_account.create_new_account_request import (
    CreateNewAccountRequest,
)
from src.use_cases.data_types.responses.bank_account.create_new_account_response import (
    CreateNewAccountResponse,
)
from src.use_cases.data_types.responses.bank_account.deposit_response import (
    DepositResponse,
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
from src.use_cases.data_types.responses.bank_account.transfer_between_accounts_response import (
    TransferBetweenAccountsResponse,
)
from src.use_cases.data_types.responses.bank_account.withdraw_response import (
    WithdrawResponse,
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
    ) -> DepositResponse:
        pass

    @classmethod
    @abstractmethod
    async def checking_account_withdraw(
        cls, account_id: UUID4, amount: float
    ) -> WithdrawResponse:
        pass

    @classmethod
    @abstractmethod
    async def transfer_between_accounts(
        cls,
        account_id: UUID4,
        amount: float,
        beneficiary_account_id: UUID4,
    ) -> TransferBetweenAccountsResponse:
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
