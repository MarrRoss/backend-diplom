from dto.base import BaseSchema


class GetStateDTO(BaseSchema):
    id: int
    name: str


class CreateStateDTO(BaseSchema):
    name: str


class UpdateStateDTO(BaseSchema):
    name: str
