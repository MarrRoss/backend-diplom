from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped

from db.declarative import Base
from db.mixins.created_at import TimestampMixin


class InvalidCustomerEmail(TimestampMixin, Base):
    __tablename__ = "invalid_customers_emails"

    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, index=True)
    customer_email_id: Mapped[int] = Column(
        Integer, ForeignKey("customers_emails.id"), nullable=False
    )
    count: Mapped[int] = Column(Integer, nullable=False)
