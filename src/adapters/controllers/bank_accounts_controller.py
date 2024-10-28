from pydantic import UUID4
from witch_doctor import WitchDoctor

from src.adapters.controllers import controller_error_handler
from src.adapters.ports.controllers.i_bank_accounts_controller import (
    IBankAccountsController,
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
from src.use_cases.data_types.responses.bank_account.get_balance_response import (
    GetBalanceResponse,
)
from src.use_cases.data_types.responses.bank_account.list_accounts_response import (
    ListAccountsResponse,
)
from src.use_cases.data_types.responses.bank_account.list_transactions_response import (
    ListTransactionsByAccountResponse,
)
from src.use_cases.data_types.responses.bank_account.movement_cash_between_accounts_response import (
    MovementCashBetweenAccountsResponse,
)
from src.use_cases.ports.extensions.bank_accounts.i_bank_accounts_extension import (
    IBankAccountsExtension,
)
from src.use_cases.ports.extensions.bank_accounts.i_create_new_account_extension import (
    ICreateNewAccountExtension,
)
from src.use_cases.ports.extensions.bank_accounts.i_transactions_extension import (
    ITransactionsExtension,
)
from src.use_cases.ports.use_cases.bank_accounts.i_create_new_account_use_case import (
    ICreateNewAccountUseCase,
)
from src.use_cases.ports.use_cases.bank_accounts.i_list_accounts_use_case import (
    IListAccountsUseCase,
)
from src.use_cases.ports.use_cases.bank_accounts.i_list_transactions_by_account_use_case import (
    IListTransactionsByAccountUseCase,
)


class BankAccountsAccountsController(IBankAccountsController):
    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def create_new_bank_account(
        cls,
        request: CreateNewAccountRequest,
        create_new_account_use_case: ICreateNewAccountUseCase,
        create_new_account_extension: ICreateNewAccountExtension,
    ) -> CreateNewAccountResponse:

        dto = await create_new_account_use_case.create_new_account(request=request)

        response = create_new_account_extension.from_dto_to_response(dto=dto)

        return response

    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def list_accounts(
        cls,
        list_accounts_use_case: IListAccountsUseCase,
        bank_accounts_extension: IBankAccountsExtension,
    ) -> ListAccountsResponse:

        dtos = await list_accounts_use_case.list_accounts()

        response = bank_accounts_extension.from_dto_list_to_response(dtos=dtos)

        return response

    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def checking_account_deposit(
        cls, account_id: UUID4, amount: float
    ) -> MovementCashResponse:
        request = checking_account_deposit_extension.from_router_request_to_request(
            balance=balance,
        )

        use_case_response = await get_balance_use_case.get_shortlist_by_company_id_and_job_opportunity_id(
            request=request
        )

        response = get_balance_extension.from_dto_to_response(dto=use_case_response)

        return response

    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def checking_account_withdraw(
        cls, account_id: UUID4, amount: float
    ) -> MovementCashResponse:
        request = checking_account_withdraw_extension.from_router_request_to_request(
            balance=balance,
        )

        use_case_response = await get_balance_use_case.get_shortlist_by_company_id_and_job_opportunity_id(
            request=request
        )

        response = get_balance_extension.from_dto_to_response(dto=use_case_response)

        return response

    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def transfer_between_accounts(
        cls, account_id: UUID4, amount: float, target_account_id: UUID4
    ) -> MovementCashBetweenAccountsResponse:

        use_case_response = await transfer_between_accounts_use_case.get_shortlist_by_company_id_and_job_opportunity_id(
            request=request
        )

        response = transfer_between_accounts.from_dto_to_response(dto=use_case_response)

        return response

    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def get_balance(cls, account_id: UUID4) -> GetBalanceResponse:
        request = get_balance_extension.from_router_request_to_request(
            balance=balance,
        )

        use_case_response = await get_balance_use_case.get_shortlist_by_company_id_and_job_opportunity_id(
            request=request
        )

        response = get_balance_extension.from_dto_to_response(dto=use_case_response)

        return response

    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def list_transactions_by_account(
        cls,
        account_id: UUID4,
        list_transactions_by_account_use_case: IListTransactionsByAccountUseCase,
        transactions_extension: ITransactionsExtension,
    ) -> ListTransactionsByAccountResponse:

        dtos = await list_transactions_by_account_use_case.list_by_account(
            account_id=account_id
        )

        response = transactions_extension.from_dto_list_to_response(dtos=dtos)

        return response
