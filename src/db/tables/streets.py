from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from db.declarative import Base


class Street(Base):
    __tablename__ = "streets"

    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, index=True)
    name: Mapped[str] = Column(String(255), nullable=False)
