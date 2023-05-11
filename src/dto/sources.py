from dto.base import BaseSchema


class GetSourceDTO(BaseSchema):
    id: int
    name: str


class CreateSourceDTO(BaseSchema):
    name: str


class UpdateSourceDTO(BaseSchema):
    name: str
