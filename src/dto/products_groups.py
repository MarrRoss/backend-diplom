from dto.base import BaseSchema


class GetProductGroupDTO(BaseSchema):
    id: int
    name: str


class CreateProductTGroupDTO(BaseSchema):
    name: str


class UpdateProductTGroupDTO(BaseSchema):
    name: str
