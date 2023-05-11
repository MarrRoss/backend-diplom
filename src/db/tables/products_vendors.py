from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, BigInteger
from sqlalchemy.orm import Mapped

from db.declarative import Base
from db.mixins.created_at import TimestampMixin


class ProductVendor(TimestampMixin, Base):
    __tablename__ = "products_vendors"

    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, index=True)
    external_vendor_id: Mapped[int] = Column(BigInteger, nullable=True)
    name: Mapped[str] = Column(String(255), nullable=True)
    description: Mapped[str] = Column(String(length=2048), nullable=True)
    active: Mapped[bool] = Column(Boolean, nullable=False)
