from datetime import datetime
from typing import Optional

from sqlalchemy import CTE
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import cast
from sqlalchemy import func
from sqlalchemy import literal
from sqlalchemy import select
from sqlalchemy import type_coerce
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased
from sqlalchemy.orm import contains_eager
from sqlalchemy.orm import joinedload

from db.repositories.base import BaseCRUD
from db.tables import CustomerData
from db.tables import Order
from db.tables import Product
from db.types.ltree import LtreeType


class OrderRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = Order
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    @classmethod
    def _recursive_cte_upgrades(
        cls,
        union_all: bool = False,
        delete_refund: bool = True,
    ) -> CTE:
        OrderRefund = aliased(Order, name="o_refund")

        stmt_top = (
            select(
                Order.id.label("id"),
                Order.product_id.label("product_id"),
                Order.previous_order_id.label("previous_order_id"),
                Product.version.label("product_version"),
                type_coerce(
                    func.text2ltree(
                        cast(
                            Order.id,
                            Text,
                        )
                    ),
                    LtreeType,
                ).label("path_id"),
                func.nlevel(
                    func.text2ltree(
                        cast(
                            Order.id,
                            Text,
                        )
                    )
                ).label("level"),
            )
            .select_from(Order)
            .join(Product, Product.id == Order.product_id)
            .filter(Order.previous_order_id.is_(None))
        )
        stmt_top = stmt_top.cte("cte", recursive=True)

        stmt_low = (
            select(
                Order.id.label("id"),
                Order.product_id.label("product_id"),
                Order.previous_order_id.label("previous_order_id"),
                Product.version.label("product_version"),
                func.text2ltree(
                    func.concat(
                        func.ltree2text(stmt_top.c.path_id),
                        ".",
                        cast(
                            Order.id,
                            Text,
                        ),
                    )
                ).label("path_id"),
                func.nlevel(
                    func.text2ltree(
                        func.concat(
                            func.ltree2text(stmt_top.c.path_id),
                            ".",
                            cast(
                                Order.id,
                                Text,
                            ),
                        )
                    )
                ).label("level"),
            )
            .select_from(Order)
            .join(Product, Product.id == Order.product_id)
            .join(stmt_top, stmt_top.c.id == Order.previous_order_id)
        )
        if delete_refund:
            stmt_low = stmt_low.filter(
                ~(
                    select(literal(1))
                    .select_from(OrderRefund)  # noqa
                    .filter(
                        OrderRefund.previous_order_id == Order.id,
                        OrderRefund.payment_type_id == 3,
                    )
                    .correlate(Order)
                    .exists()
                )
            )

        if union_all:
            recursive_q = stmt_top.union_all(stmt_low)
        else:
            recursive_q = stmt_top.union(stmt_low)

        return recursive_q

    async def get_one(self, id_: int):
        stmt = (
            select(Order)
            .join(Product, Product.id == Order.product_id)
            .options(
                contains_eager(Order.product).options(
                    joinedload(Product.product_type),
                    joinedload(Product.product_group),
                    joinedload(Product.edition),
                    joinedload(Product.vendor),
                ),
                joinedload(Order.key),
                joinedload(Order.source),
                joinedload(Order.payment_type),
                joinedload(Order.customer).options(
                    joinedload(CustomerData.company),
                    joinedload(CustomerData.country),
                    joinedload(CustomerData.street),
                    joinedload(CustomerData.city),
                    joinedload(CustomerData.zip),
                    joinedload(CustomerData.state),
                    joinedload(CustomerData.phone),
                )
            )
            .filter(Order.id == id_)
        )
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalar_one()

    async def get_all(
        self,
        customers_ids: list[int],
        only_basic: bool = True,
        product_group_id: Optional[int] = None,
    ):
        OrderOwn = aliased(Order, name="o1")
        OrderRefund = aliased(Order, name="o2")

        stmt = (
            select(OrderOwn)
            .join(CustomerData, CustomerData.id == OrderOwn.customer_id)
            .join(Product, Product.id == OrderOwn.product_id)
            .options(
                contains_eager(OrderOwn.product).options(
                    joinedload(Product.product_type),
                    joinedload(Product.product_group),
                    joinedload(Product.edition),
                    joinedload(Product.vendor),
                ),
                joinedload(OrderOwn.key),
                joinedload(OrderOwn.source),
                joinedload(OrderOwn.payment_type),
                joinedload(OrderOwn.customer).options(
                    joinedload(CustomerData.company),
                    joinedload(CustomerData.country),
                    joinedload(CustomerData.street),
                    joinedload(CustomerData.city),
                    joinedload(CustomerData.zip),
                    joinedload(CustomerData.state),
                    joinedload(CustomerData.phone),
                )
            )
        )

        stmt_is_not_refunded = (
            select(literal(1))
            .select_from(OrderRefund)  # noqa
            .filter(
                OrderRefund.previous_order_id == OrderOwn.id,
                OrderRefund.payment_type_id == 3,
            )
            .correlate(OrderOwn)
            .exists()
        )

        stmt = stmt.filter(OrderOwn.customer_id.in_(customers_ids))

        if only_basic:
            stmt = stmt.filter(OrderOwn.previous_order_id.is_(None))
            stmt = stmt.filter(~stmt_is_not_refunded)

        if product_group_id:
            stmt = stmt.filter(Product.product_group_id == product_group_id)

        curr = await self.db_session.execute(statement=stmt)
        return curr.scalars().all()

    async def get_upgrades(
        self,
        order_id: int,
    ):
        recursive_cte = self._recursive_cte_upgrades(union_all=True, delete_refund=False)
        stmt = (
            select(recursive_cte.c.id.label("id"))
            .select_from(recursive_cte)
            .filter(
                cast(
                    cast(
                        func.subltree(recursive_cte.c.path_id, 0, 1),
                        Text,
                    ),
                    Integer,
                )
                == order_id,
                ~recursive_cte.c.previous_order_id.is_(None),
            )
        )
        stmt2 = (
            select(Order)
            .filter(Order.id.in_(stmt.scalar_subquery()))
            .join(CustomerData, CustomerData.id == Order.customer_id)
            .join(Product, Product.id == Order.product_id)
            .options(
                contains_eager(Order.product).options(
                    joinedload(Product.product_type),
                    joinedload(Product.product_group),
                    joinedload(Product.edition),
                    joinedload(Product.vendor),
                ),
                joinedload(Order.key),
                joinedload(Order.source),
                joinedload(Order.payment_type),
                joinedload(Order.customer).options(
                    joinedload(CustomerData.company),
                    joinedload(CustomerData.country),
                    joinedload(CustomerData.street),
                    joinedload(CustomerData.city),
                    joinedload(CustomerData.zip),
                    joinedload(CustomerData.state),
                    joinedload(CustomerData.phone),
                )
            )
            .order_by(Order.creating_date)
        )
        curr = await self.db_session.execute(stmt2)
        return curr.scalars().all()

    async def add_one(
        self,
        date: datetime,
        product_id: int,
        num_license: int,
        purchase_id: int,
        internal_order_type_id: int,
        customer_id: int,
        is_resolved: bool,
        payment_type_id: int,
        source_id: int,
        comments: str = None,
        previous_order_id: int = None,
        key_id: int = None,
        addtional1: str = None,
        addtional2: str = None,
    ):
        model = Order(
            customer_id=customer_id,
            date=date,
            product_id=product_id,
            num_license=num_license,
            purchase_id=purchase_id,
            internal_order_type_id=internal_order_type_id,
            comments=comments,
            is_resolved=is_resolved,
            payment_type_id=payment_type_id,
            previous_order_id=previous_order_id,
            source_id=source_id,
            key_id=key_id,
            addtional1=addtional1,
            addtional2=addtional2,
        )
        self.db_session.add(model)
        await self.db_session.flush(objects=[model])
        return model
