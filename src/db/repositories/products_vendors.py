from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.repositories.base import BaseCRUD
from db.tables import ProductVendor


class ProductVendorRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = ProductVendor
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def add_one(
        self,
        name: str,
        description: str,
        external_vendor_id: int,
    ) -> ProductVendor:
        product_vendor = ProductVendor(
            name=name,
            description=description,
            external_vendor_id=external_vendor_id,
            active=True,
        )
        self.db_session.add(product_vendor)
        await self.db_session.flush()
        return product_vendor

    async def get_one(self, id_: int) -> ProductVendor:
        stmt = select(ProductVendor).filter(ProductVendor.id == id_)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalar_one()

    async def get_all(
        self,
    ) -> Sequence[ProductVendor]:
        stmt = select(ProductVendor)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalars().all()
