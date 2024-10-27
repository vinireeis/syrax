from typing import Optional, TypedDict, List

from pydantic import BaseModel

from src.adapters.extensions.exceptions.extension_exceptions_reasons_enum import (
    ExtensionExceptionsReasonsEnum,
)
from src.use_cases.exceptions.use_case_exceptions_reasons_enum import (
    UseCaseExceptionsReasonsEnum,
)


class BaseApiResponse(BaseModel):
    status: bool
    error_code: Optional[
        UseCaseExceptionsReasonsEnum | ExtensionExceptionsReasonsEnum
    ] = None
    message: Optional[str] = None
    payload: Optional[TypedDict | List[TypedDict]] = None
