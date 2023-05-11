from db.repositories.base import BaseSession
from db.repositories.products_types import ProductTypeRepository
from db.repositories.products_vendors import ProductVendorRepository
from db.tables import ProductType
from db.tables import ProductVendor
from db.utils.decorators.error_handler import orm_error_handler
from dto.products_vendors import CreateProductVendorDTO


class ProductVendorService:
    def __init__(
        self,
        session: BaseSession,
        vendor_repo: ProductVendorRepository,
    ):
        self.session = session
        self.vendor_repo = vendor_repo

    @orm_error_handler
    async def create_one(
        self,
        data: CreateProductVendorDTO,
    ):
        async with self.session.transaction():
            product_vendor = await self.vendor_repo.add_one(
                name=data.name,
                description=data.description,
                external_vendor_id=data.external_vendor_id,
            )
            return product_vendor

    @orm_error_handler
    async def get_one(self, id_: int) -> ProductVendor:
        async with self.session.transaction():
            product_vendor = await self.vendor_repo.get_one(
                id_=id_,
            )
            return product_vendor

    @orm_error_handler
    async def get_all(
        self,
    ):
        async with self.session.transaction():
            return await self.vendor_repo.get_all()
