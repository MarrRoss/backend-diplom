from datetime import datetime
from typing import Optional
from dto.base import BaseSchema


class GetUnsubscribedDTO(BaseSchema):
    id: int
    customer_email_id: int
    creating_date: datetime
    last_modified_date: Optional[datetime] = None
    count: int


class CreateUnsubscribedDTO(BaseSchema):
    customer_email_id: int
    creating_date: datetime
    last_modified_date: Optional[datetime] = None
    count: int


class UpdateUnsubscribedDTO(BaseSchema):
    customer_email_id: Optional[int] = None
    creating_date: Optional[datetime] = None
    last_modified_date: Optional[datetime] = None
    count: Optional[int] = None
