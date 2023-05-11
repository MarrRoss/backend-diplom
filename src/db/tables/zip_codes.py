from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from db.declarative import Base


class ZipCode(Base):
    __tablename__ = "zip_codes"

    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, index=True)
    name: Mapped[str] = Column(String(255), nullable=False)
