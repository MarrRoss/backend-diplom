from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped

from db.declarative import Base
from db.mixins.created_at import TimestampMixin


class CustomerDataCustomerEmailLink(TimestampMixin, Base):
    __tablename__ = "customer_data_customer_email_links_v2"

    customer_email_id: Mapped[int] = Column(
        Integer,
        ForeignKey("customers_emails.id"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    customer_data_id: Mapped[int] = Column(
        Integer,
        ForeignKey("customers_data.id"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    is_main: Mapped[bool] = Column(Boolean, nullable=False)
