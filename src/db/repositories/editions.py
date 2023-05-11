from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.repositories.base import BaseCRUD
from db.tables.editions import Edition


class ProductEditionRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = Edition
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def add_one(
        self,
        name: str,
    ) -> Edition:
        edition = Edition(
            name=name,
        )
        self.db_session.add(edition)
        await self.db_session.flush()
        return edition

    async def get_one(self, id_: int) -> Edition:
        stmt = select(Edition).filter(Edition.id == id_)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalar_one()

    async def get_all(
        self,
    ) -> Sequence[Edition]:
        stmt = select(Edition)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalars().all()
