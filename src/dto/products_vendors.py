from datetime import datetime
from typing import Optional
from dto.base import BaseSchema


class GetProductVendorDTO(BaseSchema):
    id: int
    external_vendor_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    active: bool
    creating_date: datetime
    last_modified_date: Optional[datetime] = None


class CreateProductVendorDTO(BaseSchema):
    external_vendor_id: int
    name: str
    description: Optional[str] = None


class UpdateProductVendorDTO(BaseSchema):
    external_vendor_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    active: Optional[bool] = None
