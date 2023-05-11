from dto.base import BaseSchema


class GetOrderTypeDTO(BaseSchema):
    id: int
    name: str


class CreateOrderTypeDTO(BaseSchema):
    name: str


class UpdateOrderTypeDTO(BaseSchema):
    name: str
