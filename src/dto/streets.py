from dto.base import BaseSchema


class GetStreetDTO(BaseSchema):
    id: int
    name: str


class CreateStreetDTO(BaseSchema):
    name: str


class UpdateStreetDTO(BaseSchema):
    name: str
