from datetime import datetime
from typing import Optional

from const.types.datetime_tz import DateTimeWithoutTZ
from dto.base import BaseSchema
from dto.customers_data import CreateCustomerDataDTO
from dto.customers_data import GetCustomerDataDTO
from dto.keys import GetKeyDTO
from dto.orders_types import GetOrderTypeDTO
from dto.products import GetProductDTO
from dto.sources import GetSourceDTO


class GetSmallOrderDTO(BaseSchema):
    id: int
    date: DateTimeWithoutTZ
    product_id: Optional[int] = None
    num_license: Optional[int] = None
    purchase_id: int
    customer_id: Optional[int] = None
    comments: Optional[str] = None
    is_resolved: Optional[bool] = None
    payment_type_id: Optional[int] = None
    previous_order_id: Optional[int] = None
    creating_date: datetime
    source_id: Optional[int] = None
    internal_order_type_id: Optional[int] = None
    key_id: Optional[int] = None
    addtional1: Optional[str] = None
    addtional2: Optional[str] = None
    is_subscription: Optional[bool] = None
    last_modified_date: Optional[datetime] = None


class GetOrderDTO(BaseSchema):
    id: int
    purchase_id: int
    internal_order_type_id: Optional[int] = None
    previous_order_id: Optional[int] = None

    num_license: Optional[int] = None
    comments: Optional[str] = None
    addtional1: Optional[str] = None
    addtional2: Optional[str] = None

    date: DateTimeWithoutTZ
    creating_date: datetime
    last_modified_date: Optional[datetime] = None

    product: GetProductDTO
    payment_type: GetOrderTypeDTO
    customer: GetCustomerDataDTO
    source: GetSourceDTO
    key: GetKeyDTO


class CreateOrderDTO(BaseSchema):
    date: DateTimeWithoutTZ
    product_id: Optional[int] = None
    num_license: Optional[int] = None
    purchase_id: int
    comments: Optional[str] = None
    payment_type_id: Optional[int] = None
    previous_order_id: Optional[int] = None
    source_id: Optional[int] = None
    internal_order_type_id: Optional[int] = None
    key_id: Optional[int] = None
    addtional1: Optional[str] = None
    addtional2: Optional[str] = None

    customer: CreateCustomerDataDTO


class UpdateOrderDTO(BaseSchema):
    date: Optional[datetime] = None
    product_id: Optional[int] = None
    num_license: Optional[int] = None
    purchase_id: Optional[float] = None
    customer_id: Optional[int] = None
    comments: Optional[str] = None
    is_resolved: Optional[bool] = None
    payment_type_id: Optional[int] = None
    previous_order_id: Optional[int] = None
    creating_date: Optional[datetime] = None
    source_id: Optional[int] = None
    internal_order_type_id: Optional[int] = None
    key_id: Optional[int] = None
    addtional1: Optional[str] = None
    addtional2: Optional[str] = None
    is_subscription: Optional[bool] = None
    last_modified_date: Optional[datetime] = None
