from pydantic import Field

from dto.base import BaseSchema


class BasePaginateDTO(BaseSchema):
    limit: int = Field(default=10)
    offset: int = Field(default="0")
