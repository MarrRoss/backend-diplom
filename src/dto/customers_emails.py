from typing import Optional
from dto.base import BaseSchema


class GetCustomerEmailDTO(BaseSchema):
    id: int
    email: str
    is_main: bool
    is_tester: bool


class CreateCustomerEmailDTO(BaseSchema):
    email: str
    is_main: bool
    is_tester: bool


class UpdateCustomerEmailDTO(BaseSchema):
    email: Optional[str] = None
    is_main: Optional[bool] = None
    is_tester: Optional[bool] = None
