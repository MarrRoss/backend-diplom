from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped

from db.declarative import Base


class CustomerEmail(Base):
    __tablename__ = "customers_emails"

    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, index=True)
    email: Mapped[str] = Column(String(255), nullable=False)
    is_main: Mapped[bool] = Column(Boolean, nullable=False)
