from datetime import datetime
from typing import Optional
from dto.base import BaseSchema


class GetKeyDTO(BaseSchema):
    id: int
    product_id: int
    creating_date: datetime
    key: str
    last_modified_date: datetime
    expiration_date: Optional[datetime] = None
    count_license: int
    is_active: bool
    is_beta_key: bool
    register_name: Optional[str] = None


class CreateKeyDTO(BaseSchema):
    product_id: int
    creating_date: datetime
    key: str
    last_modified_date: datetime
    purchase_id: int
    expiration_date: Optional[datetime] = None
    count_license: int
    is_active: bool
    is_beta_key: bool
    register_name: Optional[str] = None


class UpdateKeyDTO(BaseSchema):
    product_id: Optional[float] = None
    creating_date: Optional[datetime] = None
    key: Optional[str] = None
    last_modified_date: Optional[datetime] = None
    purchase_id: Optional[int] = None
    expiration_date: Optional[datetime] = None
    count_license: Optional[int] = None
    is_active: Optional[bool] = None
    is_beta_key: Optional[bool] = None
    register_name: Optional[str] = None
