from pydantic import UUID4

from fastapi import APIRouter
from starlette.routing import Router

from src.adapters.controllers.bank_accounts_controller import (
    BankAccountsAccountsController,
)
from src.use_cases.data_types.requests.checking_account.create_new_account_request import (
    CreateNewAccountRequest,
)
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


class SyraxBankRouter(Router):
    __syrax_bank_router = APIRouter(prefix="/accounts", tags=["Checking account"])

    @staticmethod
    def get_routers() -> list[APIRouter]:
        routers = list()
        routers.append(SyraxBankRouter.__syrax_bank_router)
        return routers

    @staticmethod
    @__syrax_bank_router.post(
        path="",
        response_model_exclude_none=True,
        response_model=CreateNewAccountResponse,
    )
    async def create_new_bank_account(
        request: CreateNewAccountRequest,
    ) -> CreateNewAccountResponse:
        response = await BankAccountsAccountsController.create_new_bank_account(
            request=request
        )

        return response

    @staticmethod
    @__syrax_bank_router.get(
        path="",
        response_model_exclude_none=True,
        response_model=ListAccountsResponse,
    )
    async def list_accounts() -> ListAccountsResponse:
        response = await BankAccountsAccountsController.list_accounts()

        return response

    @staticmethod
    @__syrax_bank_router.post(
        path="/{account_id}/deposit",
        response_model_exclude_none=True,
        response_model=DepositResponse,
    )
    async def checking_account_deposit(
        account_id: UUID4, amount: float
    ) -> DepositResponse:

        response = await BankAccountsAccountsController.checking_account_deposit(
            account_id=account_id, amount=amount
        )

        return response

    @staticmethod
    @__syrax_bank_router.post(
        path="/{account_id}/withdraw",
        response_model_exclude_none=True,
        response_model=WithdrawResponse,
    )
    async def checking_account_withdraw(
        account_id: UUID4, amount: float
    ) -> WithdrawResponse:
        response = await BankAccountsAccountsController.checking_account_withdraw(
            account_id=account_id, amount=amount
        )

        return response

    @staticmethod
    @__syrax_bank_router.post(
        path="/{account_id}/transfer",
        response_model_exclude_none=True,
        response_model=TransferBetweenAccountsResponse,
    )
    async def transfer_between_checking_account(
        account_id: UUID4, amount: float, beneficiary_account_id: UUID4
    ) -> TransferBetweenAccountsResponse:
        response = await BankAccountsAccountsController.transfer_between_accounts(
            account_id=account_id,
            amount=amount,
            beneficiary_account_id=beneficiary_account_id,
        )

        return response

    @staticmethod
    @__syrax_bank_router.get(
        path="/{account_id}/balance",
        response_model_exclude_none=True,
        response_model=GetBalanceResponse,
    )
    async def get_balance(account_id: UUID4) -> GetBalanceResponse:
        response = await BankAccountsAccountsController.get_balance(
            account_id=account_id,
        )

        return response

    @staticmethod
    @__syrax_bank_router.get(
        path="/{account_id}/transactions",
        response_model_exclude_none=True,
        response_model=ListTransactionsByAccountResponse,
    )
    async def list_transactions_by_account(
        account_id: UUID4,
    ) -> ListTransactionsByAccountResponse:
        response = await BankAccountsAccountsController.list_transactions_by_account(
            account_id=account_id,
        )

        return response
