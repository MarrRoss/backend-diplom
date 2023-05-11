from db.repositories.base import BaseSession
from db.repositories.products import ProductRepository
from db.tables import Product
from db.utils.decorators.error_handler import orm_error_handler
from dto.products import CreateProductDTO


class ProductService:
    def __init__(
        self,
        session: BaseSession,
        product_repo: ProductRepository,
    ):
        self.session = session
        self.product_repo = product_repo

    @orm_error_handler
    async def get_one(self, id_: int) -> Product:
        async with self.session.transaction():
            product = await self.product_repo.get_one(
                id_=id_,
            )
            return product

    @orm_error_handler
    async def get_all(
        self,
    ):
        async with self.session.transaction():
            products = await self.product_repo.get_all()
            return products

    @orm_error_handler
    async def add_one(
        self,
        data: CreateProductDTO,
    ):
        async with self.session.transaction():
            product = await self.product_repo.add_one(
                external_product_id=data.external_product_id,
                name=data.name,
                product_type_id=data.product_type_id,
                version=data.version,
                platform_id=data.platform_id,
                edition_id=data.edition_id,
                previous_edition_id=data.previous_edition_id,
                previous_version=data.previous_version,
                previous_platform_id=data.previous_platform_id,
                is_released=data.is_released,
                short_name=data.short_name,
                is_subscription=data.is_subscription,
                active_months=data.active_months,
                url_for_download=data.url_for_download,
                vendor_id=data.vendor_id,
                product_group_id=data.product_group_id,
            )
            return product

