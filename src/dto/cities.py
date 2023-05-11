from dto.base import BaseSchema


class GetCityDTO(BaseSchema):
    id: int
    name: str


class CreateCityDTO(BaseSchema):
    name: str


class UpdateCityDTO(BaseSchema):
    name: str
