from dto.base import BaseSchema


class GetCompanyDTO(BaseSchema):
    id: int
    name: str


class CreateCompanyDTO(BaseSchema):
    name: str


class UpdateCompanyDTO(BaseSchema):
    name: str
