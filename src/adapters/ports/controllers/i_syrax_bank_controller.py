from abc import ABC, abstractmethod

from pydantic import UUID4

from src.use_cases.data_types.responses.checking_account.create_new_account_response import (
    CreateNewAccountResponse,
)
from src.use_cases.data_types.responses.checking_account.deposit_response import (
    DepositResponse,
)
from src.use_cases.data_types.responses.checking_account.get_balance_response import (
    GetBalanceResponse,
)
from src.use_cases.data_types.responses.checking_account.list_transactions_response import (
    ListTransactionsByAccountResponse,
)
from src.use_cases.data_types.responses.checking_account.list_accounts_response import (
    ListAccountsResponse,
)
from src.use_cases.data_types.responses.checking_account.transfer_between_accounts_response import (
    TransferBetweenAccountsResponse,
)
from src.use_cases.data_types.responses.checking_account.withdraw_response import (
    WithdrawResponse,
)


class ISyraxBankController(ABC):

    @classmethod
    @abstractmethod
    async def create_new_bank_account(cls, balance: float) -> CreateNewAccountResponse:
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
    async def transfer_between_checking_account(
        cls, account_id: UUID4, beneficiary_account_id: UUID4, amount: float
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
