from dto.products_vendors import CreateProductVendorDTO
from services.products_vendors import ProductVendorService


class ProductVendorController:
    def __init__(self, service: ProductVendorService):
        self.service = service

    async def get_one_from_id(self, id_: int):
        return await self.service.get_one(id_=id_)

    async def get_all(
        self,
    ):
        return await self.service.get_all()

    async def create_one(
        self,
        data: CreateProductVendorDTO,
    ):
        return await self.service.create_one(data=data)
