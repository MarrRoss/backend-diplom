from dto.base import BaseSchema


class GetEditionDTO(BaseSchema):
    id: int
    name: str


class CreateEditionDTO(BaseSchema):
    name: str


class UpdateEditionDTO(BaseSchema):
    name: str
