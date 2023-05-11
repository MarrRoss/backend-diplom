from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.repositories.base import BaseCRUD
from db.tables import Company


class CompanyRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = Company
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def get_one(self, id_: int):
        stmt = select(Company).filter(Company.id == id_)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalar_one()

    async def get_all(
        self,
    ):
        stmt = select(Company)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalars().all()

    async def get_one_from_name(self, name: str):
        return await self.base.get_one(Company.name == name)

    async def exists(self, name: str):
        return await self.base.exists(Company.name == name)

    async def add_one(self, name: str):
        model = Company(name=name)
        self.db_session.add(model)
        await self.db_session.flush(objects=[model])
        return model
