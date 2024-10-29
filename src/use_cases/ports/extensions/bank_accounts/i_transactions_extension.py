from abc import abstractmethod, ABC

from src.domain.models.transaction_model import TransactionModel
from src.use_cases.data_types.dtos.transaction_dto import TransactionDto
from src.use_cases.data_types.responses.bank_account.list_transactions_response import (
    ListTransactionsByAccountResponse,
)


class ITransactionsExtension(ABC):

    @staticmethod
    @abstractmethod
    def from_database_result_to_model(result: dict) -> TransactionModel:
        pass

    @staticmethod
    @abstractmethod
    def from_database_result_list_to_model_list(
        result_list: list[dict],
    ) -> list[TransactionModel]:
        pass

    @staticmethod
    @abstractmethod
    def from_model_list_to_dto_list(
        models: list[TransactionModel],
    ) -> list[TransactionDto]:
        pass

    @staticmethod
    @abstractmethod
    def from_model_to_dto(model: TransactionModel) -> TransactionDto:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_list_to_response(
        dtos: list[TransactionDto],
    ) -> ListTransactionsByAccountResponse:
        pass
