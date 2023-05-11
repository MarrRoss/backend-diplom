from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped

from db.declarative import Base


# from database import Base


class AccountCustomerRelation(Base):
    __tablename__ = "accounts_customers_relations_v2"

    account_id: Mapped[int] = Column(
        Integer,
        ForeignKey("customers_accounts.id"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    customer_id: Mapped[int] = Column(
        Integer,
        ForeignKey("customers_data.id"),
        primary_key=True,
        nullable=False,
        index=True,
    )
