from datetime import datetime
from typing import Optional
from dto.base import BaseSchema


class GetInvalidCustomerEmailDTO(BaseSchema):
    id: int
    customer_email_id: int
    name: str
    creating_date: datetime
    last_modified_date: Optional[datetime] = None
    count: int


class CreateInvalidCustomerEmailDTO(BaseSchema):
    customer_email_id: int
    name: str
    creating_date: datetime
    last_modified_date: Optional[datetime] = None
    count: int


class UpdateInvalidCustomerEmailDTO(BaseSchema):
    customer_email_id: Optional[int] = None
    name: Optional[str] = None
    creating_date: Optional[datetime] = None
    last_modified_date: Optional[datetime] = None
    count: Optional[int] = None
