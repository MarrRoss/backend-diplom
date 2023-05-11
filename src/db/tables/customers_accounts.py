from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from db.declarative import Base


class CustomerAccount(Base):
    __tablename__ = "customers_accounts"

    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, index=True)
    first_name: Mapped[str] = Column(String(255), nullable=True)
    last_name: Mapped[str] = Column(String(255), nullable=True)
    register_name: Mapped[str] = Column(String(255), nullable=True, unique=True)
    comment: Mapped[str] = Column(String(255), nullable=True)
