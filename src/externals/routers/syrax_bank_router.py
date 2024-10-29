from http import HTTPStatus

from pydantic import UUID4

from fastapi import APIRouter
from starlette.routing import Router

from src.adapters.controllers.bank_accounts_controller import (
    BankAccountsAccountsController,
)
from src.use_cases.data_types.requests.bank_accounts.create_new_account_request import (
    CreateNewAccountRequest,
)
from src.use_cases.data_types.responses.bank_account.create_new_account_response import (
    CreateNewAccountResponse,
)
from src.use_cases.data_types.responses.bank_account.movement_cash_response import (
    MovementCashResponse,
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
        status_code=HTTPStatus.CREATED,
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
        response_model=MovementCashResponse,
    )
    async def checking_account_deposit(
        account_id: UUID4, amount: float
    ) -> MovementCashResponse:

        response = await BankAccountsAccountsController.checking_account_deposit(
            account_id=account_id, amount=amount
        )

        return response

    @staticmethod
    @__syrax_bank_router.post(
        path="/{account_id}/withdraw",
        response_model_exclude_none=True,
        response_model=MovementCashResponse,
    )
    async def checking_account_withdraw(
        account_id: UUID4, amount: float
    ) -> MovementCashResponse:
        response = await BankAccountsAccountsController.checking_account_withdraw(
            account_id=account_id, amount=amount
        )

        return response

    @staticmethod
    @__syrax_bank_router.post(
        path="/{account_id}/transfer",
        response_model_exclude_none=True,
        response_model=MovementCashBetweenAccountsResponse,
    )
    async def transfer_between_checking_account(
        account_id: UUID4, amount: float, target_account_id: UUID4
    ) -> MovementCashBetweenAccountsResponse:
        response = await BankAccountsAccountsController.transfer_between_accounts(
            account_id=account_id,
            amount=amount,
            target_account_id=target_account_id,
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
