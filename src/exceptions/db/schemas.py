from typing import Optional

from dto.base import BaseSchema


class NotFoundSchema(BaseSchema):
    detail: str
    sql_detail: Optional[str] = None


class AlreadyExistsSchema(BaseSchema):
    detail: str
    sql_detail: Optional[str] = None
