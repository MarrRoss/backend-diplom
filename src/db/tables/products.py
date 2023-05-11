from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from db.declarative import Base


if TYPE_CHECKING:
    from db.tables.products_groups import ProductGroup
    from db.tables.products_types import ProductType
    from db.tables.editions import Edition
    from db.tables.products_vendors import ProductVendor


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, index=True)
    external_product_id: Mapped[int] = Column(Numeric, nullable=False)
    name: Mapped[str] = Column(String(255), nullable=False, unique=True)
    product_type_id: Mapped[int] = Column(
        Integer, ForeignKey("products_types.id"), nullable=True
    )
    version: Mapped[int] = Column(Numeric, nullable=True)
    platform_id: Mapped[int] = Column(Integer, nullable=True)
    edition_id: Mapped[int] = Column(Integer, ForeignKey("editions.id"), nullable=True)
    previous_edition_id: Mapped[int] = Column(
        Integer, ForeignKey("editions.id"), nullable=True
    )
    previous_version: Mapped[int] = Column(Numeric, nullable=True)
    previous_platform_id: Mapped[int] = Column(Integer, nullable=True)
    is_released: Mapped[bool] = Column(Boolean, nullable=False)
    short_name: Mapped[str] = Column(String(255), nullable=True)
    is_subscription: Mapped[bool] = Column(Boolean, nullable=False)
    active_months: Mapped[int] = Column(Integer, nullable=True)
    url_for_download: Mapped[str] = Column(String(255), nullable=True)
    vendor_id: Mapped[int] = Column(
        Integer, ForeignKey("products_vendors.id"), nullable=False
    )
    product_group_id: Mapped[int] = Column(
        Integer, ForeignKey("products_groups.id"), nullable=False
    )

    product_type: Mapped[ProductType] = relationship("ProductType")
    product_group: Mapped[ProductGroup] = relationship("ProductGroup")

    edition: Mapped[Edition] = relationship(
        "Edition",
        foreign_keys=[edition_id],
    )
    previous_edition: Mapped[Edition] = relationship(
        "Edition",
        foreign_keys=[previous_edition_id],
    )
    vendor: Mapped[ProductVendor] = relationship("ProductVendor")
