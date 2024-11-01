from enum import StrEnum


class CashFlowEnum(StrEnum):
    CASH_IN = "cash_in"
    CASH_OUT = "cash_out"


class CashFlowOperator(StrEnum):
    cash_in = "+"
    cash_out = "-"
