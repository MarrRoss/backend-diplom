from sqlalchemy import CTE
from sqlalchemy import Text
from sqlalchemy import cast
from sqlalchemy import func
from sqlalchemy import literal
from sqlalchemy import select
from sqlalchemy import type_coerce
from sqlalchemy.orm import aliased

from db.repositories.base import BaseSession
from db.repositories.orders import OrderRepository
from db.tables import Order
from db.tables import Product
from db.tables import Source
from db.types.ltree import LtreeType
from db.utils.decorators.error_handler import orm_error_handler
from dto.orders import CreateOrderDTO


class OrderService:
    def __init__(
        self,
        session: BaseSession,
        order_repo: OrderRepository,
    ):
        self.session = session
        self.order_repo = order_repo

    @orm_error_handler
    async def get_one(self, id_: int) -> Order:
        async with self.session.transaction():
            order = await self.order_repo.get_one(
                id_=id_,
            )
            return order

    @orm_error_handler
    async def get_all(
        self,
        customers_ids: list[int],
        only_basic: bool = True,
    ):
        async with self.session.transaction():
            orders = await self.order_repo.get_all(
                customers_ids=customers_ids,
                only_basic=only_basic,
            )
            return orders

    @orm_error_handler
    async def get_upgrades(
        self,
        order_id: int,
    ):
        async with self.session.transaction():
            orders = await self.order_repo.get_upgrades(order_id=order_id)
            return orders

    @orm_error_handler
    async def add_one(self, customer_id: int, data: CreateOrderDTO):
        async with self.session.transaction() as t:
            result = await self.order_repo.add_one(
                date=data.date,
                product_id=data.product_id,
                previous_order_id=data.previous_order_id,
                internal_order_type_id=data.internal_order_type_id,
                customer_id=customer_id,
                num_license=data.num_license,
                key_id=data.key_id,
                payment_type_id=data.payment_type_id,
                purchase_id=data.purchase_id,
                source_id=data.source_id,
                is_resolved=True,
            )
            await t.commit()
            return result
