from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.functions import current_timestamp

from db.declarative import Base
from db.types.date_time import TZDateTime


class TimestampMixin(Base):
    __abstract__ = True
    creating_date: Mapped[datetime] = Column(TZDateTime, default=current_timestamp())
    last_modified_date: Mapped[datetime] = Column(
        TZDateTime, onupdate=current_timestamp()
    )
