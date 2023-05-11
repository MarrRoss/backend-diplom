from typing import Optional
from dto.base import BaseSchema


class GetProductTypeDTO(BaseSchema):
    id: int
    name: Optional[str] = None
    is_main_product: bool
    lifetime: Optional[bool] = None
    versioned: Optional[bool] = None
    upgradable: bool


class CreateProductTypeDTO(BaseSchema):
    name: Optional[str] = None
    is_main_product: bool
    lifetime: Optional[bool] = None
    versioned: Optional[bool] = None
    upgradable: bool


class UpdateProductTypeDTO(BaseSchema):
    name: Optional[str] = None
    is_main_product: Optional[bool] = None
    lifetime: Optional[bool] = None
    versioned: Optional[bool] = None
    upgradable: Optional[bool] = None
