from decimal import Decimal
from uuid import uuid4

from decouple import config


class BankAccountEntity:
    def __init__(
        self,
        account_id: uuid4 = None,
        initial_balance: float = None,
        balance_end_of_day: Decimal = None,
    ):
        self.__account_id = account_id
        self.__balance_end_of_day = balance_end_of_day
        self.__initial_balance = initial_balance

    @property
    def initial_balance(self) -> Decimal:
        return self.to_decimal(self.__initial_balance)

    @property
    def account_id(self) -> uuid4:
        return self.__account_id

    @property
    def balance_end_of_day(self) -> Decimal:
        return self.__balance_end_of_day

    @staticmethod
    def to_decimal(amount: float) -> Decimal:
        amount_formated = Decimal(amount).quantize(Decimal(config("DECIMAL_PRECISION")))
        return amount_formated

    def _generate_new_account_id(self) -> uuid4:
        account_id = uuid4()
        self.__account_id = account_id
        return self.__account_id

    def get_current_balance(self) -> Decimal:
        pass
