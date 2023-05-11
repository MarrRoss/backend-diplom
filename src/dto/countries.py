from dto.base import BaseSchema


class GetCountryDTO(BaseSchema):
    id: int
    name: str


class CreateCountryDTO(BaseSchema):
    name: str


class UpdateCountryDTO(BaseSchema):
    name: str
