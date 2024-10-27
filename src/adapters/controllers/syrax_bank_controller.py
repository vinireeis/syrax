from uuid import uuid4

from witch_doctor import WitchDoctor

from src.adapters.controllers import controller_error_handler
from src.adapters.ports.controllers.i_syrax_bank_controller import ISyraxBankController
from src.use_cases.data_types.responses.checking_account.create_new_account_response import (
    CreateNewAccountResponse,
)
from src.use_cases.data_types.responses.checking_account.deposit_response import (
    DepositResponse,
)
from src.use_cases.data_types.responses.checking_account.get_balance_response import (
    GetBalanceResponse,
)
from src.use_cases.data_types.responses.checking_account.list_accounts_response import (
    ListAccountsResponse,
)
from src.use_cases.data_types.responses.checking_account.list_transactions_response import (
    ListTransactionsByAccountResponse,
)
from src.use_cases.data_types.responses.checking_account.withdraw_response import (
    WithdrawResponse,
)


class SyraxBankController(ISyraxBankController):
    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def create_new_bank_account(cls, balance: float) -> CreateNewAccountResponse:
        request = create_bank_account_extension.from_router_request_to_request(
            balance=balance,
        )

        use_case_response = await create_bank_account_use_case.get_shortlist_by_company_id_and_job_opportunity_id(
            request=request
        )

        response = create_bank_account_extension.from_dto_to_response(
            dto=use_case_response
        )

        return response

    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def list_accounts(cls) -> ListAccountsResponse:
        request = create_bank_account_extension.from_router_request_to_request(
            balance=balance,
        )

        use_case_response = await create_bank_account_use_case.get_shortlist_by_company_id_and_job_opportunity_id(
            request=request
        )

        response = create_bank_account_extension.from_dto_to_response(
            dto=use_case_response
        )

        return response

    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def checking_account_deposit(
        cls, beneficiary_account_id: uuid4, amount: float
    ) -> DepositResponse:
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
        cls, beneficiary_account_id: uuid4, amount: float
    ) -> WithdrawResponse:
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
    async def get_balance(cls, beneficiary_account_id: uuid4) -> GetBalanceResponse:
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
        cls, beneficiary_account_id: uuid4
    ) -> ListTransactionsByAccountResponse:
        request = get_transactions_extension.from_router_request_to_request(
            beneficiary_account_id=beneficiary_account_id,
        )

        use_case_response = await get_transactions_use_case.get_shortlist_by_company_id_and_job_opportunity_id(
            request=request
        )

        response = get_transactions_extension.from_dto_to_response(
            dto=use_case_response
        )

        return response
