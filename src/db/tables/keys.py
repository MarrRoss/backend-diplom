from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Numeric, DateTime
from sqlalchemy.orm import Mapped

from db.declarative import Base
from db.mixins.created_at import TimestampMixin


class Key(TimestampMixin, Base):
    __tablename__ = "keys"

    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, index=True)
    product_id: Mapped[int] = Column(Numeric, nullable=False)
    key: Mapped[str] = Column(String(255), nullable=False)
    expiration_date: Mapped[datetime] = Column(DateTime, nullable=True)
    count_license: Mapped[int] = Column(Integer, nullable=False)
    is_active: Mapped[bool] = Column(Boolean, nullable=False)
    is_beta_key: Mapped[bool] = Column(Boolean, nullable=False)
    register_name: Mapped[str] = Column(String(255), nullable=True)
