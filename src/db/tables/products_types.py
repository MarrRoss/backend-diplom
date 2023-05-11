from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped

from db.declarative import Base


class ProductType(Base):
    __tablename__ = "products_types"

    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, index=True)
    name: Mapped[str] = Column(String(255), nullable=True)
    is_main_product: Mapped[bool] = Column(Boolean, nullable=False)
    lifetime: Mapped[bool] = Column(Boolean, nullable=True)
    versioned: Mapped[bool] = Column(Boolean, nullable=True)
    upgradable: Mapped[bool] = Column(Boolean, nullable=False)
