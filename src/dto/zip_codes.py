from dto.base import BaseSchema


class GetZipCodeDTO(BaseSchema):
    id: int
    name: str


class CreateZipCodeDTO(BaseSchema):
    name: str


class UpdateZipCodeDTO(BaseSchema):
    name: str
