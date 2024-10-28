from abc import abstractmethod

from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionsUnexpectedException,
)
from src.domain.entities.bank_account_entity import BankAccountEntity
from src.domain.entities.transaction_entity import TransactionEntity
from src.domain.enums.cash_flow.enum import CashFlowEnum
from src.domain.enums.operations.enum import AccountOperationsEnum
from src.use_cases.data_types.dtos.bank_account_dto import BankAccountDto
from src.use_cases.data_types.requests.bank_accounts.create_new_account_request import (
    CreateNewAccountRequest,
)
from src.use_cases.data_types.responses.bank_account.create_new_account_response import (
    CreateNewAccountResponse,
    CreateNewAccountPayload,
)
from src.use_cases.ports.extensions.bank_accounts.i_create_new_account_extension import (
    ICreateNewAccountExtension,
)


class CreateNewAccountExtension(ICreateNewAccountExtension):

    @staticmethod
    def from_request_to_entity(request: CreateNewAccountRequest) -> BankAccountEntity:
        try:

            entity = BankAccountEntity(balance=request.balance)
            entity._generate_new_account_id()

            return entity

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected exception trying to create entity",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_entity_to_dto(entity: BankAccountEntity) -> BankAccountDto:

        try:
            dto = BankAccountDto(account_id=entity.account_id)

            return dto

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected exception trying to create dto",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_dto_to_response(dto: BankAccountDto) -> CreateNewAccountResponse:
        try:
            payload = CreateNewAccountPayload(account_id=dto.account_id)

            response = CreateNewAccountResponse(
                payload=payload,
                status=True,
                message="New account created successfully ",
            )

            return response

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected exception trying to create dto",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def create_transaction_entity(
        bank_account_entity: BankAccountEntity,
    ) -> TransactionEntity:
        try:
            transaction_entity = TransactionEntity(
                account_id=bank_account_entity.account_id,
                operation=AccountOperationsEnum.DEPOSIT,
                cash_flow=CashFlowEnum.CASH_IN,
                amount=bank_account_entity.balance_float_type,
            )

            transaction_entity._generate_transaction_id()

            return transaction_entity

        except Exception as original_exception:
            raise ExtensionsUnexpectedException(
                message="Unexpected exception trying to create dto",
                original_error=original_exception,
            ) from original_exception
