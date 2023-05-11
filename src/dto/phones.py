from dto.base import BaseSchema


class GetPhoneDTO(BaseSchema):
    id: int
    name: str


class CreatePhoneDTO(BaseSchema):
    name: str


class UpdatePhoneDTO(BaseSchema):
    name: str
