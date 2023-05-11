from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from db.declarative import Base
from db.mixins.created_at import TimestampMixin


if TYPE_CHECKING:
    from db.tables.cities import City
    from db.tables.companies import Company
    from db.tables.countries import Country
    from db.tables.phones import Phone
    from db.tables.states import State
    from db.tables.streets import Street
    from db.tables.zip_codes import ZipCode


class CustomerData(TimestampMixin, Base):
    __tablename__ = "customers_data"

    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, index=True)
    first_name: Mapped[str] = Column(String(255), nullable=False)
    last_name: Mapped[str] = Column(String(255), nullable=False)
    register_name: Mapped[str] = Column(String(255), nullable=False)
    description: Mapped[str] = Column(String(255), nullable=True)
    company_id: Mapped[int] = Column(Integer, ForeignKey("companies.id"), nullable=True)
    country_id: Mapped[int] = Column(Integer, ForeignKey("countries.id"), nullable=True)
    street_id: Mapped[int] = Column(Integer, ForeignKey("streets.id"), nullable=True)
    city_id: Mapped[int] = Column(Integer, ForeignKey("cities.id"), nullable=True)
    zip_id: Mapped[int] = Column(Integer, ForeignKey("zip_codes.id"), nullable=True)
    state_id: Mapped[int] = Column(Integer, ForeignKey("states.id"), nullable=True)
    phone_id: Mapped[int] = Column(Integer, ForeignKey("phones.id"), nullable=True)

    company: Mapped[Company] = relationship("Company", uselist=False)
    country: Mapped[Country] = relationship("Country", uselist=False)
    street: Mapped[Street] = relationship("Street", uselist=False)
    city: Mapped[City] = relationship("City", uselist=False)
    zip: Mapped[ZipCode] = relationship("ZipCode", uselist=False)
    state: Mapped[State] = relationship("State", uselist=False)
    phone: Mapped[Phone] = relationship("Phone", uselist=False)
