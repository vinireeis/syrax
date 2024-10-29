from decimal import Decimal
from uuid import uuid4

from decouple import config


class BankAccountEntity:
    def __init__(
        self,
        account_id: uuid4 = None,
        balance: float = None,
    ):
        self.__account_id = account_id
        self.__balance = balance

    @property
    def balance(self) -> Decimal:
        return self.to_decimal(self.__balance)

    @property
    def balance_float_type(self) -> float:
        return self.__balance

    @property
    def account_id(self) -> uuid4:
        return self.__account_id

    @staticmethod
    def to_decimal(amount: float) -> Decimal:
        amount_formated = Decimal(amount).quantize(Decimal(config("DECIMAL_PRECISION")))
        return amount_formated

    def _generate_new_account_id(self) -> uuid4:
        account_id = uuid4()
        self.__account_id = account_id
        return self.__account_id

    def new_account_document(self) -> dict:
        document_to_insert = {
            "account_id": self.__account_id,
            "balance": self.__balance,
        }

        return document_to_insert
