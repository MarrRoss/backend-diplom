from db.repositories.base import BaseSession
from db.repositories.products_types import ProductTypeRepository
from db.tables import ProductType
from db.utils.decorators.error_handler import orm_error_handler


class ProductTypeService:
    def __init__(
        self,
        session: BaseSession,
        source_repo: ProductTypeRepository,
    ):
        self.session = session
        self.source_repo = source_repo

    @orm_error_handler
    async def get_one(self, id_: int) -> ProductType:
        async with self.session.transaction():
            product_type = await self.source_repo.get_one(
                id_=id_,
            )
            return product_type

    @orm_error_handler
    async def get_all(
        self,
    ):
        async with self.session.transaction():
            products_types = await self.source_repo.get_all()
            return products_types
