from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Boolean, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from db.declarative import Base
from db.mixins.created_at import TimestampMixin

if TYPE_CHECKING:
    from db.tables.customers_data import CustomerData
    from db.tables.orders_types import OrderType
    from db.tables.sources import Source
    from db.tables.keys import Key
    from db.tables.products import Product


class Order(TimestampMixin, Base):
    __tablename__ = "orders"

    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, index=True)
    date: Mapped[datetime] = Column(DateTime, nullable=False)
    product_id: Mapped[int] = Column(Integer, ForeignKey("products.id"), nullable=True)
    num_license: Mapped[int] = Column(Integer, nullable=True)
    purchase_id: Mapped[int] = Column(Numeric, nullable=False)
    customer_id: Mapped[int] = Column(
        Integer, ForeignKey("customers_data.id"), nullable=True
    )
    comments: Mapped[str] = Column(String(255), nullable=True)
    is_resolved: Mapped[bool] = Column(Boolean, nullable=True)
    payment_type_id: Mapped[int] = Column(
        Integer, ForeignKey("orders_types.id"), nullable=True
    )
    previous_order_id: Mapped[int] = Column(
        Integer, ForeignKey("orders.id"), nullable=True
    )
    source_id: Mapped[int] = Column(Integer, ForeignKey("sources.id"), nullable=True)
    internal_order_type_id: Mapped[int] = Column(Integer, nullable=True)
    key_id: Mapped[int] = Column(Integer, ForeignKey("keys.id"), nullable=True)
    addtional1: Mapped[str] = Column(String(255), nullable=True)
    addtional2: Mapped[str] = Column(String(255), nullable=True)

    product: Mapped[Product] = relationship("Product")
    key: Mapped[Key] = relationship("Key")
    source: Mapped[Source] = relationship("Source")
    payment_type: Mapped[OrderType] = relationship("OrderType")
    customer: Mapped[CustomerData] = relationship("CustomerData")
