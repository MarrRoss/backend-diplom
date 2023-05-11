from typing import Optional
from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from db.repositories.base import BaseCRUD
from db.tables import Product


class ProductRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = Product
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def get_one(self, id_: int) -> Product:
        stmt = select(Product).filter(Product.id == id_)
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalar_one()

    async def add_one(
        self,
        external_product_id: int,
        name: str,
        is_released: bool,
        is_subscription: bool,
        vendor_id: int,
        product_group_id: int,
        product_type_id: Optional[int] = None,
        version: Optional[int] = None,
        platform_id: Optional[int] = None,
        edition_id: Optional[int] = None,
        previous_edition_id: Optional[int] = None,
        previous_version: Optional[int] = None,
        previous_platform_id: Optional[int] = None,
        short_name: Optional[str] = None,
        active_months: Optional[int] = None,
        url_for_download: Optional[str] = None,
    ) -> Product:
        product = Product(
            external_product_id=external_product_id,
            name=name,
            is_subscription=is_subscription,
            short_name=short_name,
            product_type_id=product_type_id,
            version=version,
            platform_id=platform_id,
            edition_id=edition_id,
            previous_edition_id=previous_edition_id,
            previous_version=previous_version,
            previous_platform_id=previous_platform_id,
            is_released=is_released,
            active_months=active_months,
            url_for_download=url_for_download,
            vendor_id=vendor_id,
            product_group_id=product_group_id,


        )
        self.db_session.add(product)
        await self.db_session.flush()
        return product

    async def get_all(
        self,
    ) -> Sequence[Product]:
        stmt = select(Product).options(
            joinedload(Product.vendor),
            joinedload(Product.product_type),
            joinedload(Product.product_group),
            joinedload(Product.edition),
        )
        curr = await self.db_session.execute(statement=stmt)
        return curr.scalars().all()
