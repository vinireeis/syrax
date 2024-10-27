from typing import TypeVar

from src.adapters.extensions.base_controller_extension import BaseControllerExtension
from src.adapters.extensions.exceptions.extensions_base_exception import (
    ExtensionsBaseException,
)
from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException

T = TypeVar("T")


def controller_error_handler(function: T) -> T:
    async def wrap(*args, **kwargs):
        try:
            return await function(*args, **kwargs)
        except UseCaseBaseException as exception:
            response = BaseControllerExtension.create_error_response(
                exception=exception
            )
            return response
        except ExtensionsBaseException as exception:
            response = BaseControllerExtension.create_error_response(
                exception=exception
            )
            return response

    wrap.__wrapped__ = function
    return wrap
