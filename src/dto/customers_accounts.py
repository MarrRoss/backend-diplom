from typing import Optional
from dto.base import BaseSchema


class GetCustomerAccountDTO(BaseSchema):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    register_name: Optional[str] = None
    comment: Optional[str] = None


class CreateCustomerAccountDTO(BaseSchema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    register_name: Optional[str] = None
    comment: Optional[str] = None


class UpdateCustomerAccountDTO(BaseSchema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    register_name: Optional[str] = None
    comment: Optional[str] = None
