from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped

from db.declarative import Base


class ProductGroup(Base):
    __tablename__ = "products_groups"

    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, index=True)
    name: Mapped[str] = Column(String(255), nullable=True)
