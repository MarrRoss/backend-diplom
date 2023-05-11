from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.repositories.base import BaseCRUD
from db.tables import ProductType
from db.tables import Source


class ProductTypeRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = ProductType
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def get_one(self, id_: int):
        stmt = select(ProductType).filter(ProductType.id == id_)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalar_one()

    async def get_all(
        self,
    ):
        stmt = select(ProductType)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalars().all()
