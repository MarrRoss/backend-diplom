from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.repositories.base import BaseCRUD
from db.tables import Street


class StreetRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = Street
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def get_one(self, id_: int):
        stmt = select(Street).filter(Street.id == id_)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalar_one()

    async def get_all(
        self,
    ):
        stmt = select(Street)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalars().all()

    async def get_one_from_name(self, name: str):
        return await self.base.get_one(Street.name == name)

    async def exists(self, name: str):
        return await self.base.exists(Street.name == name)

    async def add_one(self, name: str):
        model = Street(name=name)
        self.db_session.add(model)
        await self.db_session.flush(objects=[model])
        return model
