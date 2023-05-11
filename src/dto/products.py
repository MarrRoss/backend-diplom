from typing import Optional
from dto.base import BaseSchema
from dto.editions import GetEditionDTO
from dto.products_groups import GetProductGroupDTO
from dto.products_types import GetProductTypeDTO
from dto.products_vendors import GetProductVendorDTO


class GetSmallProductDTO(BaseSchema):
    id: int
    external_product_id: int
    name: str
    product_type_id: Optional[int] = None
    version: Optional[int] = None
    platform_id: Optional[int] = None
    edition_id: Optional[int] = None
    previous_edition_id: Optional[int] = None
    previous_version: Optional[int] = None
    previous_platform_id: Optional[int] = None
    is_released: bool
    short_name: Optional[str] = None
    is_subscription: bool
    active_months: Optional[int] = None
    url_for_download: Optional[str] = None
    vendor_id: int


class GetProductDTO(BaseSchema):
    id: int
    external_product_id: int
    name: str
    version: Optional[int] = None
    platform_id: Optional[int] = None
    edition_id: Optional[int] = None
    previous_edition_id: Optional[int] = None
    previous_version: Optional[int] = None
    previous_platform_id: Optional[int] = None
    is_released: bool
    short_name: Optional[str] = None

    product_type: GetProductTypeDTO
    product_group: GetProductGroupDTO
    edition: GetEditionDTO
    vendor: GetProductVendorDTO


class CreateProductDTO(BaseSchema):
    external_product_id: int
    name: str
    product_type_id: Optional[int] = None
    version: Optional[int] = None
    platform_id: Optional[int] = None
    edition_id: Optional[int] = None
    previous_edition_id: Optional[int] = None
    previous_version: Optional[int] = None
    previous_platform_id: Optional[int] = None
    is_released: bool
    short_name: Optional[str] = None
    is_subscription: bool
    active_months: Optional[int] = None
    url_for_download: Optional[str] = None
    vendor_id: int
    product_group_id: int


class UpdateProductDTO(BaseSchema):
    external_product_id: Optional[int] = None
    name: Optional[str] = None
    product_type_id: Optional[int] = None
    version: Optional[float] = None
    platform_id: Optional[int] = None
    edition_id: Optional[int] = None
    previous_edition_id: Optional[int] = None
    previous_version: Optional[int] = None
    previous_platform_id: Optional[int] = None
    is_released: Optional[bool] = None
    short_name: Optional[str] = None
    is_subscription: Optional[bool] = None
    active_months: Optional[int] = None
    url_for_download: Optional[str] = None
    vendor_id: Optional[int] = None
